#!/usr/bin/env python
# Internal dependencies
import os
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from collections import namedtuple
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


def run(cmd, cwd=root, silent=False):
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL if silent else subprocess.PIPE, stderr=subprocess.DEVNULL if silent else subprocess.STDOUT, cwd=cwd, shell=True, encoding="utf-8", errors="replace", text=False)

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
    import html
    import re

    from bs4 import BeautifulSoup, NavigableString, Tag
    from bs4.formatter import HTMLFormatter

    class CustomHTMLFormatter(HTMLFormatter):
        ATTR_ORDER = ["itemprop", "name", "property", "content", "id", "class", "src", "rel", "type", "href", "width", "height", "alt", "crossorigin", "async"]

        def attributes(self, tag: Tag):
            new_order = []
            for attr in self.ATTR_ORDER:
                if attr in tag.attrs:
                    new_order.append((attr, tag[attr]))
            for pair in tag.attrs.items():
                if pair not in new_order:
                    new_order.append(pair)
            return new_order

        def format_tag(self, tag: Tag):
            return tag.decode(formatter=None).strip()

    def cleanupHTML(f: Path):
        with f.open("r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "lxml")
            # <code>, <pre>: Properly preserve content
            for tags_code in soup.find_all(["code", "pre"]):
                if tags_code.string:
                    raw_text = tags_code.string
                    escaped_text = html.escape(html.unescape(raw_text), quote=False)
                    tags_code.string.replace_with(NavigableString(escaped_text))
            # <a>: Remove trailing slash from href
            for tag_a in soup.find_all("a"):
                if tag_a.get("href") and tag_a["href"] != "/":
                    tag_a["href"] = re.sub(r"\/+$", "", tag_a["href"])
            # <meta>: Remove trailing slash from URL
            for tag_meta in soup.find_all("meta", attrs={"property": True}):
                if tag_meta["property"] == "og:url":
                    tag_meta["content"] = re.sub(r"\/+$", "", tag_meta["content"])
            new_content = soup.encode(formatter=CustomHTMLFormatter()).decode("utf-8")
            # TODO: Find good HTML minifier (not 'minify-html' which is broken)
        with f.open("w", encoding="utf-8") as file:
            file.write(new_content)
        info(str(f), "DESLASH", Fore.YELLOW)

    def cleanupXML(f: Path):
        with f.open("r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "xml")
            # <guid>, <link>, <loc>: Remove trailing slash from URL
            for tag_url in soup.find_all(["guid", "link", "loc"]):
                if tag_url.string:
                    tag_url.string.replace_with(NavigableString(re.sub(r"\/+$", "", tag_url.string)))
            # <description>: Remove new line from content
            for tag_description in soup.find_all("description"):
                if tag_description.string:
                    tag_description.string.replace_with(NavigableString(re.sub(r"(?m)^\s*\n", "", tag_description.string)))
            new_content = str(soup)
        with f.open("w", encoding="utf-8") as file:
            file.write(new_content)
        info(str(f), "DESLASH", Fore.YELLOW)

    argpath = Path(args.PATH)

    if not argpath.exists():
        error("Invalid path")

    if argpath.is_file():
        if argpath.suffix in [".html", ".htm"]:
            cleanupHTML(argpath)
        elif argpath.suffix == ".xml":
            cleanupXML(argpath)
    elif argpath.is_dir():
        for file_path in argpath.rglob("*"):
            if file_path.suffix in [".htm", ".html"]:
                cleanupHTML(file_path)
            elif file_path.suffix == ".xml":
                cleanupXML(file_path)


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
    Kinds.add(Kind("pivox-desktop", ["pd", "pivox-desktop"], "pivox", "d/desktop"))
    Kinds.add(Kind("pivox-development", ["pdev", "pivox-dev", "pivox-development"], "pivox", "d/development"))
    Kinds.add(Kind("pivox-game", ["pg", "pivox-game"], "pivox", "d/game"))
    Kinds.add(Kind("pivox-misc", ["pivox-misc"], "pivox", "d/misc"))
    Kinds.add(Kind("pivox-mobile", ["pivox-mobile", "pm"], "pivox", "d/mobile"))
    Kinds.add(Kind("pivox-server", ["pivox-server", "ps"], "pivox", "d/server"))
    Kinds.add(Kind("pivox-web", ["pivox-web", "pw"], "pivox", "d/web"))
    Kinds.add(Kind("the-division", ["d", "division", "td", "td2", "the-division"], "the-division", "b/game/the-division"))
    Kinds.add(Kind("tower-of-fantasy", ["tf", "tof", "tower-of-fantasy"], "tower-of-fantasy", "b/game/tower-of-fantasy"))
    Kinds.add(Kind("wuthering-waves-companion", ["wc", "wcq", "wuthering-companion", "wuthering-waves-companion", "wuthering-waves-companion-quest", "wuthering-waves-companion-quests", "ww-companion", "ww-companion-quest", "ww-companion-quests", "wwc", "wwcq"], "wuthering-waves", "b/game/wuthering-waves/companion"))
    Kinds.add(Kind("wuthering-waves-event", ["wuthering-event", "wuthering-waves-event", "ww-event"], "wuthering-waves", "b/game/wuthering-waves/event"))
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
    PUBLIC_PATH = Path(publish_root / "public")
    deslash(args(PATH=PUBLIC_PATH))

    info("Removing previous site files...")
    PUBLISH_REPO_DIR = Path(getenv("PUBLISH_REPO_DIR")).resolve()
    for item in PUBLISH_REPO_DIR.iterdir():
        if item.name != ".git":
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    info("Moving site files to another repository...")
    for item in PUBLIC_PATH.iterdir():
        shutil.move(item, PUBLISH_REPO_DIR)

    info("Creating required files...")
    with (PUBLISH_REPO_DIR / ".nojekyll").open("w") as f:
        f.write("")
    with (PUBLISH_REPO_DIR / "CNAME").open("w") as f:
        f.write(getenv("CUSTOM_DOMAIN"))

    info("Tracking changes with Git...")
    os.chdir(PUBLISH_REPO_DIR)
    run("git add -A", cwd=PUBLISH_REPO_DIR)

    from datetime import datetime

    commit_message = datetime.now().strftime("Deploy: %Y-%m-%d %H:%M:%S")
    run(f'git commit -m "{commit_message}"', cwd=PUBLISH_REPO_DIR)

    info("Pushing changes to remote...")
    run("git push origin main --force", cwd=PUBLISH_REPO_DIR)

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
