#!/bin/bash
# NOFORMAT='\033[0m'
# RED='\033[0;31m'
# GREEN='\033[0;32m'
# ORANGE='\033[0;33m'
# BLUE='\033[0;34m'
# PURPLE='\033[0;35m'
# CYAN='\033[0;36m'
# YELLOW='\033[1;33m'
error() {
  echo >&2 -e "\033[0;31mERROR\033[0m ${*}"
}
gitadd() {
  git add --ignore-errors "$@"
}
info() {
  echo >&2 -e "\033[0;32mINFO\033[0m ${*}"
}
main() {
  echo "Git Repository Purger"
  echo "__          __     _____  _   _ _____ _   _  _____ "
  echo "\ \        / /\   |  __ \| \ | |_   _| \ | |/ ____|"
  echo " \ \  /\  / /  \  | |__) |  \| | | | |  \| | |  __ "
  echo "  \ \/  \/ / /\ \ |  _  /| . \` | | | | . \` | | |_ |"
  echo "   \  /\  / ____ \| | \ \| |\  |_| |_| |\  | |__| |"
  echo "    \/  \/_/    \_\_|  \_\_| \_|_____|_| \_|\_____|"
  echo "This script will destroy current repository and create a new git repository."
  echo "Do you wish to continue?"
  echo "Current directory: $(pwd)"
  select yn in "Yes" "No"; do
    case $yn in
    Yes) purge; break;;
    No) exit ;;
    esac
  done
}
purge() {
  # Check if '.git' directory exists
  if [ ! -d .git ]; then
    error ".git directory not found. Aborting..."
    exit 1
  fi
  read_env ".script/.env"
  # Check 'GIT_PUSH_URL' variable and 'GIT_PUSH_URL' exists
  if [ -n "$GIT_PULL_URL" ]; then
    info "GIT_PULL_URL: " "$GIT_PULL_URL"
  else
    error "GIT_PULL_URL variable is blank or not set"
    exit 1
  fi
  if [ -n "$GIT_PUSH_URL" ]; then
    info "GIT_PUSH_URL: " "$GIT_PUSH_URL"
  else
    error "GIT_PUSH_URL variable is blank or not set"
    exit 1
  fi
  # Remove '.git' directory
  rm -rf .git
  info "Git repository is destroyed"
  # Create a new git repository and configure it
  git init
  info "New Git repository is created"
  git remote add origin "${GIT_PUSH_URL}"
  #
  info "Commiting files... (1/14) - Everything except for 'content/b/'"
  git add --all -- ':!content/b/'
  git commit -m "Repository Reconstruction (Base)" -m "Everything except for 'content/b/'"
  #
  info "Commiting files... (2/14) - chit-chat"
  gitadd "content/b/_index.md"
  gitadd "content/b/chit-chat/*"
  git commit -m "Repository Reconstruction (chit-chat)" -m "- content/b/chit-chat/"
  #
  info "Commiting files... (3/14) - blue-archive, honkai-star-rail, minecraft, misc"
  gitadd "content/b/game/_index.md"
  gitadd "content/b/game/blue-archive/*"
  gitadd "content/b/game/honkai-star-rail/*"
  gitadd "content/b/game/minecraft/*"
  gitadd "content/b/game/misc/*"
  git commit -m "Repository Reconstruction (BA, H:SR, MC, MISC)" -m $'- content/b/game/blue-archive/\n- content/b/game/honkai-star-rail/\n- content/b/game/minecraft/\n- content/b/game/misc/'
  #
  info "Commiting files... (4/14) - the-division"
  gitadd "content/b/game/the-division/*"
  git commit -m "Repository Reconstruction (TD)" -m "- content/b/game/the-division/"
  #
  info "Commiting files... (5/14) - tower-of-fantasy"
  gitadd "content/b/game/tower-of-fantasy/*"
  git commit -m "Repository Reconstruction (ToF)" -m "- content/b/game/tower-of-fantasy/"
  #
  info "Commiting files... (6/14) - genshin-impact/archon (00X ~ 09X)"
  gitadd "content/b/game/genshin-impact/_index.md"
  gitadd "content/b/game/genshin-impact/archon/*"
  git commit -m "Repository Reconstruction (GI/A)" -m "- content/b/game/genshin-impact/archon/"
  #
  info "Commiting files... (7/14) - genshin-impact/event (00X ~ 04X)"
  gitadd "content/b/game/genshin-impact/event/_index.md"
  gitadd "content/b/game/genshin-impact/event/00*"
  gitadd "content/b/game/genshin-impact/event/01*"
  gitadd "content/b/game/genshin-impact/event/02*"
  gitadd "content/b/game/genshin-impact/event/03*"
  gitadd "content/b/game/genshin-impact/event/04*"
  git commit -m "Repository Reconstruction (GI/E) (1/2)" -m "- content/b/game/genshin-impact/event/ (00X ~ 04X)"
  #
  info "Commiting files... (8/14) - genshin-impact/event (05X ~ 09X)"
  gitadd "content/b/game/genshin-impact/event/05*"
  gitadd "content/b/game/genshin-impact/event/06*"
  gitadd "content/b/game/genshin-impact/event/07*"
  gitadd "content/b/game/genshin-impact/event/08*"
  gitadd "content/b/game/genshin-impact/event/09*"
  git commit -m "Repository Reconstruction (GI/E) (2/2)" -m "- content/b/game/genshin-impact/event/ (05X ~ 09X)"
  #
  info "Commiting files... (9/14) - genshin-impact/misc"
  gitadd "content/b/game/genshin-impact/misc/*"
  git commit -m "Repository Reconstruction (GI/M)" -m "- content/b/game/genshin-impact/misc/"
  #
  info "Commiting files... (10/14) - genshin-impact/story"
  gitadd "content/b/game/genshin-impact/story/*"
  git commit -m "Repository Reconstruction (GI/S)" -m "- content/b/game/genshin-impact/story/"
  #
  info "Commiting files... (11/14) - genshin-impact/world (00X ~ 02X)"
  gitadd "content/b/game/genshin-impact/world/_index.md"
  gitadd "content/b/game/genshin-impact/world/00*"
  gitadd "content/b/game/genshin-impact/world/01*"
  gitadd "content/b/game/genshin-impact/world/02*"
  git commit -m "Repository Reconstruction (GI/W) (1/2)" -m "- content/b/game/genshin-impact/world/ (00X ~ 02X)"
  #
  info "Commiting files... (12/14) - genshin-impact/world (03X ~ 05X)"
  gitadd "content/b/game/genshin-impact/world/03*"
  gitadd "content/b/game/genshin-impact/world/04*"
  gitadd "content/b/game/genshin-impact/world/05*"
  git commit -m "Repository Reconstruction (GI/W) (2/2)" -m "- content/b/game/genshin-impact/world/ (03X ~ 05X)"
  #
  info "Commiting files... (13/14) - wuthering-waves"
  gitadd "content/b/game/wuthering-waves/*"
  git commit -m "Repository Reconstruction (WW)" -m "- content/b/game/wuthering-waves/"
  #
  info "Cleaning repo... (14/14)"
  git reflog expire --expire=now --expire-unreachable=now --all
  git gc --prune=now
  #
  info "Push repo to origin"
  #git push origin main --force
}
read_env() {
  local filePath="${1:-'.env'}"
  if [ ! -f "$filePath" ]; then
    error "missing ${filePath}"
    exit 1
  fi
  set -o allexport
  # shellcheck disable=SC2046 # This is intended behavior
  export $(grep -v "^#" "$filePath" | xargs)
  set +o allexport
}

# Change directory to parent-parent directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.." || exit

main
read -r -s -n 1 -p "Press any key to continue..."
