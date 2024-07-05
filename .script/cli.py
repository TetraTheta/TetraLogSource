#!/usr/bin/env python
# Internal dependencies
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from collections import namedtuple
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List, Optional

root = Path(__file__).resolve().parent.parent
os.chdir(root)

#######################
# Virtual Environment #
#######################
# Check if python is running on venv
if __name__ == "__main__":
    venv_path = root / ".venv"
    if sys.prefix == sys.base_prefix:
        # create venv
        if not venv_path.is_dir():
            result = subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
            if result.returncode != 0:
                print(result.stderr)
                sys.exit(result.returncode)
        # re-launch with same arguments
        python_executable = venv_path / "Scripts" / "python.exe" if sys.platform == "win32" else venv_path / "bin" / "python"
        subprocess.run([python_executable, "-m", "pip", "install", "-r", root / "requirements.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # not using 'run' function because it is not defined yet
        result = subprocess.run([python_executable] + sys.argv)
        sys.exit(result.returncode)

# External dependencies
from colorama import Fore, Style  # noqa: E402
from colorama import init as colorinit  # noqa: E402
from dotenv import load_dotenv  # noqa: E402


############
# Function #
############
def error(msg, header="ERROR", color=Fore.RED):
    print(f"{color}{header}{Style.RESET_ALL} {msg}{Style.RESET_ALL}", file=sys.stderr)


def info(msg, header="INFO", color=Fore.GREEN):
    print(f"{color}{header}{Style.RESET_ALL} {msg}{Style.RESET_ALL}")


def getenv(envvar: str) -> str:
    ev = os.environ[envvar]
    if ev is None or ev == "":
        error(f"{envvar} is not set!")
        sys.exit(1)
    return ev


def run(cmd, silent=False):
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL if silent else subprocess.PIPE, stderr=subprocess.DEVNULL if silent else subprocess.STDOUT, shell=True, encoding="utf-8", errors="replace", text=False)

    while True:
        if proc.poll() is not None:
            break
        elif not silent:
            with os.fdopen(os.dup(proc.stdout.fileno()), newline="", encoding="utf-8") as output:
                for line in output:
                    print(line, end="", flush=True)
    proc.wait()


#########
# Class #
#########
class Kind:
    def __init__(self, name: str, alias: List[str], kind: str, argpath: str):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (isinstance(alias, list) and all(isinstance(a, str) for a in alias)):
            raise ValueError("Alias must be a list of strings")
        if not (isinstance(kind, str)):
            raise ValueError("Kind must be a string")
        if not (isinstance(argpath, str)):
            raise ValueError("Path must be a string")
        self.name = name
        self.alias = alias
        self.kind = kind
        self.path = Path(argpath)


class KindList:
    def __init__(self):
        self.kinds: List[Kind] = []

    def add(self, new_kind: Kind):
        if not isinstance(new_kind, Kind):
            raise ValueError("Only instance of Kind is accepted")
        self.kinds.append(new_kind)

    def get(self, needle: str) -> Optional[Kind]:
        return next((kind for kind in self.kinds if needle in kind.alias), None)

    def show(self) -> str:
        return "\n".join(f"{kind.name}: {', '.join(kind.alias)}" for kind in self.kinds)


##############
# Subcommand #
##############
def clean(_):
    dir_public = Path(root / "public")
    dir_resources = Path(root / "resources")
    info("Removing " + str(dir_public))
    shutil.rmtree(dir_public, ignore_errors=True)
    info("Removing " + str(dir_resources))
    shutil.rmtree(dir_resources, ignore_errors=True)


def deslash(args):
    import re

    from bs4 import BeautifulSoup

    def removeSlashHTML(f: Path):
        with f.open("r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "lxml")
            for tag_a in soup.find_all("a"):
                if tag_a["href"] == "/":
                    continue
                tag_a["href"] = re.sub(r"\/+$", "", tag_a["href"])
            for tag_meta in soup.find_all("meta", attrs={"property": True}):
                if tag_meta["property"] == "og:url":
                    tag_meta["content"] = re.sub(r"\/+$", "", tag_meta["content"])
            new_content = str(soup)
        with f.open("w", encoding="utf-8") as file:
            file.write(new_content)
        info(str(f), "DESLASH", Fore.YELLOW)

    def removeSlashXML(f: Path):
        with f.open("r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "xml")
            for tag_guid in soup.find_all("guid"):
                if tag_guid.string is not None:
                    tag_guid.string = re.sub(r"\/+$", "", tag_guid.string)
            for tag_link in soup.find_all("link"):
                if tag_link.string is not None:
                    tag_link.string = re.sub(r"\/+$", "", tag_link.string)
            for tag_loc in soup.find_all("loc"):
                if tag_loc.string is not None:
                    tag_loc.string = re.sub(r"\/+$", "", tag_loc.string)
            new_content = str(soup)
        with f.open("w", encoding="utf-8") as file:
            file.write(new_content)
        info(str(f), "DESLASH", Fore.YELLOW)

    argpath = Path(args.PATH)

    if not argpath.exists():
        error("Invalid path")

    if argpath.is_file():
        if argpath.suffix in [".html", ".htm"]:
            removeSlashHTML(argpath)
        elif argpath.suffix == ".xml":
            removeSlashXML(argpath)
    elif argpath.is_dir():
        for file_path in argpath.rglob("*"):
            if file_path.suffix in [".htm", ".html"]:
                removeSlashHTML(file_path)
            elif file_path.suffix == ".xml":
                removeSlashXML(file_path)


def new(args):
    Kinds = KindList()
    Kinds.add(Kind("blue-archive", ["ba", "blue-archive", "bluearchive"], "blue-archive", "b/game/blue-archive"))
    Kinds.add(Kind("chit-chat", ["cc", "chat", "chit-chat", "chitchat"], "chit-chat", "b/chit-chat"))
    Kinds.add(Kind("default", ["default"], "default", "b"))
    Kinds.add(Kind("game-misc", ["game-misc", "gm"], "game-misc", "b/game/misc"))
    Kinds.add(Kind("genshin-archon", ["ga", "gaq", "genshin-archon", "genshin-archon-quest", "genshin-archon-quests"], "genshin-impact", "b/game/genshin-impact/archon"))
    Kinds.add(Kind("genshin-event", ["ge", "genshin-event", "genshin-event-quest", "genshin-event-quests", "geq"], "genshin-impact", "b/game/genshin-impact/event"))
    Kinds.add(Kind("genshin-misc", ["genshin-misc"], "genshin-impact", "b/game/genshin-impact/misc"))
    Kinds.add(Kind("genshin-story", ["genshin-story", "genshin-story-quest", "genshin-story-quests", "gs", "gsq"], "genshin-impact", "b/game/genshin-impact/story"))
    Kinds.add(Kind("genshin-world", ["genshin-world", "genshin-world-quest", "genshin-world-quests", "gw", "gwq"], "genshin-impact", "b/game/genshin-impact/world"))
    Kinds.add(Kind("honkai-star-rail", ["honkai", "honkai-star-rail", "hsr", "sr"], "honkai-star-rail", "b/game/honkai-star-rail"))
    Kinds.add(Kind("minecraft", ["mc", "minecraft"], "minecraft", "b/game/minecraft"))
    Kinds.add(Kind("music", ["music"], "music", "b/chit-chat/music"))
    Kinds.add(Kind("the-division", ["d", "division", "td", "td2", "the-division"], "the-division", "b/game/the-division"))
    Kinds.add(Kind("tower-of-fantasy", ["tf", "tof", "tower-of-fantasy"], "tower-of-fantasy", "b/game/tower-of-fantasy"))
    Kinds.add(Kind("wuthering-waves-companion", ["wc", "wcq", "wuthering-companion", "wuthering-waves-companion", "wuthering-waves-companion-quest", "wuthering-waves-companion-quests", "ww-companion", "ww-companion-quest", "ww-companion-quests", "wwc", "wwcq"], "wuthering-waves", "b/game/wuthering-waves/companion"))
    Kinds.add(Kind("wuthering-waves-exploration", ["we", "weq", "wuthering-exploration", "wuthering-waves-exploration", "wuthering-waves-exploration-quest", "wuthering-waves-exploration-quests", "ww-exploration", "ww-exploration-quest", "ww-exploration-quests", "wwe", "wweq"], "wuthering-waves", "b/game/wuthering-waves/exploration"))
    Kinds.add(Kind("wuthering-waves-main", ["wm", "wmq", "wuthering-main", "wuthering-waves-main", "wuthering-waves-main-quest", "wuthering-waves-main-quests", "ww-main", "ww-main-quest", "ww-main-quests", "wwm", "wwmq"], "wuthering-waves", "b/game/wuthering-waves/main"))
    Kinds.add(Kind("wuthering-waves-misc", ["wuthering-misc", "wuthering-waves-misc", "ww-misc"], "wuthering-waves", "b/game/wuthering-waves/misc"))

    kind = Kinds.get(args.kind)
    title = "-".join(args.TITLE).strip().lower()
    content_path = Path(root / "content" / kind.path).resolve()

    print(f"{Fore.YELLOW}-------- Input Information --------{Style.RESET_ALL}")
    print(f"Title: {title}")
    print(f"Kind: {kind.kind}")
    print(f"Content Path: {str(content_path)}")
    print(f"{Fore.YELLOW}-----------------------------------{Style.RESET_ALL}")

    if not content_path.exists():
        info(f"Following path will be created\n{Fore.YELLOW}{str(content_path)}{Style.RESET_ALL}")
        content_path.mkdir(parents=True, exist_ok=True)

    try:
        files = [f.name for f in content_path.iterdir() if f.is_dir()]
    except OSError:
        error(f"Failed to read directory: {str(content_path)}")
        sys.exit(1)

    next_num = 1
    while any(dir.startswith(f"{str(next_num).zfill(3)}-") for dir in files):
        next_num += 1

    new_dir_name = f"{str(next_num).zfill(3)}-{title}"
    new_file_name = Path(content_path / new_dir_name / "index.md").resolve()

    os.chdir(root)
    new_cmd = f"hugo new content -k {kind.kind} {str(new_file_name)}"
    info(new_cmd, "COMMAND", Fore.YELLOW)
    run(new_cmd)


def publish(args):
    local = args.local

    if local:
        tempdir = None
        publish_root = root
        info(f"Build target directory: {str(publish_root)}")
    else:
        tempdir = TemporaryDirectory(prefix="hugo-build-", ignore_cleanup_errors=True)
        publish_root = Path(tempdir.name)
        info(f"Build target directory: {str(publish_root)}")
        info("Fetching latest commit to temporary directory...")
        GIT_PULL_URL = getenv("GIT_PULL_URL")
        run(f"git clone --progress --depth 1 {GIT_PULL_URL} {str(publish_root)}")

    os.chdir(publish_root)
    info("Building site...")
    run("npm ci")
    clean(None)
    run("hugo --gc --minify -e production")

    info("Removing trailing slash...")
    args = namedtuple("args", ["PATH"])
    deslash(args(PATH=Path(publish_root / "public")))

    info("Publish site with rsync...")
    PUBLISH_SSH_KEY = getenv("PUBLISH_SSH_KEY")
    PUBLISH_USER_IP = getenv("PUBLISH_USER_IP")
    PUBLISH_DIR = getenv("PUBLISH_DIR")
    run(f'rsync -vcrmzh --progress --del --force -e "ssh -o StrictHostKeyChecking=no -i {PUBLISH_SSH_KEY}" --rsync-path="sudo rsync" --chown=www-data:www-data --chmod=Du=rwx,Dg=rx,Do=rx,Fu=rw,Fg=r,Fo=r "./public/" {PUBLISH_USER_IP}:{PUBLISH_DIR}')

    info("Cleaning directories...")
    if local:
        clean({})
    else:
        os.chdir(root)
        tempdir.cleanup()

    info("Done!")


########
# Main #
########
if __name__ == "__main__":
    colorinit()  # Initialize colorama
    load_dotenv(Path(root / ".script" / ".env").resolve())  # Load .env file
    # Parse arguments
    cli = ArgumentParser(prog="cli")
    subcli = cli.add_subparsers(title="subcommands", required=True)
    # clean
    subcli_clean = subcli.add_parser("clean", help="Cleanup Hugo temporary files")
    subcli_clean.set_defaults(func=clean)
    # deslash
    subcli_deslash = subcli.add_parser("deslash", help="Remove trailing slash of URL from file(s)")
    subcli_deslash.add_argument("PATH", help="File or Directory path for removing slashes", nargs="?", default=Path(root / "public").resolve())
    subcli_deslash.set_defaults(func=deslash)
    # new
    subcli_new = subcli.add_parser("new", help="Create new Hugo article")
    subcli_new.add_argument("-k", "--kind", help="Kind of new article", required=True)
    subcli_new.add_argument("TITLE", help="Title of the new article", nargs="*")
    subcli_new.set_defaults(func=new)
    # publish
    subcli_publish = subcli.add_parser("publish", help="Build site and push it to remote server")
    subcli_publish.add_argument("-l", "--local", help="Build from local repository, rather than cloning new repository", action="store_true")
    subcli_publish.set_defaults(func=publish)
    #
    args = cli.parse_args()
    args.func(args)
