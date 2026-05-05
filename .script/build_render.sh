#!/usr/bin/env bash
# This script is meant to be run on Render build server
# This script can't distinguish Hugo and Hugo Extended but it'll be fine because Render does not provide latest Hugo (Extended) binary.

# Check 'HUGO_VERSION' is set
if [ -z "$HUGO_VERSION" ]; then
  echo "ERROR: 'HUGO_VERSION' environment variable is not set!"
  exit 1
fi

# Check 'SASS_VERSION' is set
if [ -z "$SASS_VERSION" ]; then
  echo "ERROR: 'SASS_VERSION' environment variable is not set!"
  exit 1
fi

XDG_CACHE_HOME=${XDG_CACHE_HOME:-$HOME/.cache}
TMP_DIR="$HOME/tmp"
mkdir -p "$TMP_DIR"

# ==== Check pnpm ====
echo "Checking pnpm..."
PNPM_MAJOR_VERSION=10
PNPM_BIN=$(command -v pnpm)
if [ -z "$PNPM_BIN" ]; then
  PNPM_INSTALLED_VERSION="NOT_INSTALLED"
else
  PNPM_INSTALLED_VERSION=$("$PNPM_BIN" --version)
fi
PNPM_INSTALLED_MAJOR=$(printf '%s' "$PNPM_INSTALLED_VERSION" | cut -d. -f1)

if [ "$PNPM_INSTALLED_MAJOR" != "$PNPM_MAJOR_VERSION" ]; then
  echo "pnpm major version mismatch or not installed. Expected: ${PNPM_MAJOR_VERSION}.x | Found: $PNPM_INSTALLED_VERSION"
  mkdir -p "$HOME/project/src/bin"
  corepack enable --install-directory "$HOME/project/src/bin" || {
    echo "Error enabling Corepack."
    exit 1
  }
  export PATH="$HOME/project/src/bin:$PATH"
  corepack prepare "pnpm@${PNPM_MAJOR_VERSION}" --activate || {
    echo "Error preparing pnpm@${PNPM_MAJOR_VERSION} with Corepack."
    exit 1
  }
  PNPM_BIN=$(command -v pnpm)
  if [ -z "$PNPM_BIN" ]; then
    echo "pnpm is still unavailable after bootstrap."
    exit 1
  fi
  PNPM_INSTALLED_VERSION=$("$PNPM_BIN" --version)
  PNPM_INSTALLED_MAJOR=$(printf '%s' "$PNPM_INSTALLED_VERSION" | cut -d. -f1)
  if [ "$PNPM_INSTALLED_MAJOR" != "$PNPM_MAJOR_VERSION" ]; then
    echo "Unsupported pnpm version after bootstrap: $PNPM_INSTALLED_VERSION (expected ${PNPM_MAJOR_VERSION}.x)"
    exit 1
  fi
else
  echo "pnpm major version matches: ${PNPM_MAJOR_VERSION}.x."
fi
echo "Using pnpm binary: $PNPM_BIN"
echo "pnpm version: $PNPM_INSTALLED_VERSION"

# ==== Check Hugo ====
echo "Checking Hugo version..."
HUGO_BIN=$(command -v hugo)
if [ -z "$HUGO_BIN" ]; then
  HUGO_INSTALLED_VERSION="NOT_INSTALLED"
else
  HUGO_INSTALLED_VERSION=$("$HUGO_BIN" version | grep -oP '(?<=hugo v)[0-9]+\.[0-9]+\.[0-9]+')
fi

if [ "$HUGO_INSTALLED_VERSION" != "$HUGO_VERSION" ]; then
  echo "Hugo version mistmatch or not installed. Expected: $HUGO_VERSION | Found: $HUGO_INSTALLED_VERSION"
  HUGO_CACHE_DIR="$XDG_CACHE_HOME/hugo/v$HUGO_VERSION"
  HUGO_BINARY_PATH="$HUGO_CACHE_DIR/hugo"

  if [ ! -f "$HUGO_BINARY_PATH" ]; then
    echo "Downloading 'Hugo Extended v$HUGO_VERSION'..."
    HUGO_RELEASE_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
    HUGO_RELEASE_FILE="$TMP_DIR/hugo_extended_${HUGO_VERSION}.tar.gz"
    curl -L -o "$HUGO_RELEASE_FILE" "$HUGO_RELEASE_URL" || {
      echo "Error downloading Hugo."
      exit 1
    }
    echo "Extracting Hugo..."
    mkdir -p "$HUGO_CACHE_DIR"
    tar -xzf "$HUGO_RELEASE_FILE" -C "$HUGO_CACHE_DIR" hugo || {
      echo "Error extracting Hugo."
      exit 1
    }
    echo "Hugo installed to '$HUGO_CACHE_DIR'."
  fi
  HUGO_BIN="$HUGO_BINARY_PATH"
else
  echo "Hugo version matches: $HUGO_VERSION."
fi

# ==== Check Dart Sass ====
echo "Checking Dart Sass version..."
SASS_BIN=$(command -v sass)
if [ -z "$SASS_BIN" ]; then
  SASS_INSTALLED_VERSION="NOT_INSTALLED"
else
  SASS_INSTALLED_VERSION=$("$SASS_BIN" --version | awk '{print $1}')
fi

if [ "$SASS_INSTALLED_VERSION" != "$SASS_VERSION" ]; then
  echo "Dart Sass version mismatch or not installed. Expected: $SASS_VERSION | Found: $SASS_INSTALLED_VERSION"
  SASS_CACHE_DIR="$XDG_CACHE_HOME/sass/v$SASS_VERSION"
  SASS_BINARY_PATH="$SASS_CACHE_DIR/sass"

  if [ ! -f "$SASS_BINARY_PATH" ]; then
    echo "Downloading 'Dart Sass v$SASS_VERSION'..."
    SASS_RELEASE_URL="https://github.com/sass/dart-sass/releases/download/${SASS_VERSION}/dart-sass-${SASS_VERSION}-linux-x64.tar.gz"
    SASS_RELEASE_FILE="$TMP_DIR/dart-sass-${SASS_VERSION}.tar.gz"
    curl -L -o "$SASS_RELEASE_FILE" "$SASS_RELEASE_URL" || {
      echo "Error downloading Dart Sass."
      exit 1
    }
    echo "Extracting Dart Sass..."
    mkdir -p "$SASS_CACHE_DIR"
    tar -xzf "$SASS_RELEASE_FILE" -C "$SASS_CACHE_DIR" --strip-components=1 || {
      echo "Error extracting Dart Sass."
      exit 1
    }
    echo "Dart Sass installed to $SASS_CACHE_DIR."
  fi

  SASS_BIN="$SASS_BINARY_PATH"
else
  echo "Dart Sass version matches: $SASS_VERSION."
fi

# Make sure Hugo resolves the intended Dart Sass first, even if Render already
# provides another `sass` binary earlier in PATH.
SASS_BIN_DIR=$(dirname "$SASS_BIN")
PATH="$SASS_BIN_DIR:$PATH"
echo "Using Dart Sass binary: $SASS_BIN"
"$SASS_BIN" --version

# ==== Build site ====
cd "$HOME/project/src" || {
  echo "Failed to change directory to build directory"
  exit 1
}
echo "Installing workspace dependencies via pnpm..."
"$PNPM_BIN" install --frozen-lockfile || {
  echo "Failed to install dependencies with pnpm."
  exit 1
}
"$PNPM_BIN" --filter @tetralog/cli run cli clean
"$HUGO_BIN" --gc --minify -e production
"$PNPM_BIN" --filter @tetralog/cli run cli deslash
