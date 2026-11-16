#!/usr/bin/env bash

# Resolve the project before deleting generated output, regardless of the caller's directory.
project_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P) || exit 1
cd -- "$project_root" || exit 1
# Set title
printf '\033]0;TetraLog Test Server\007'
# Remove 'public', 'resources'
rm -rf -- "$project_root/public" "$project_root/resources" || exit 1

# Fast Render: Home page + Content page last edited (if any) + Content page last visited (up to 10)
# Note: Using port 80 will break Header Menu active state
hugo server --renderToMemory --disableFastRender -D -p 44
