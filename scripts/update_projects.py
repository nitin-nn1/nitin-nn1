"""Regenerate the project list in README.md from public GitHub repos.

Lists every public, non-fork repo owned by the user that has the topic
named in PROFILE_TOPIC (default "featured"). Repos already linked in the
hand-written part of the README are skipped, so nothing shows up twice.
Only the text between the PROJECTS:START and PROJECTS:END markers changes.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime

USER = os.environ.get("PROFILE_USER", "nitin-nn1")
TOPIC = os.environ.get("PROFILE_TOPIC", "featured")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = os.environ.get("PROFILE_README", "README.md")
START, END = "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", f"{USER}-profile-readme")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def render(repo):
    name = repo["name"].replace("-", " ").replace("_", " ")
    lines = [f"#### [{name}]({repo['html_url']})"]
    if repo.get("description"):
        lines.append(repo["description"])
    langs = list(api(f"/repos/{USER}/{repo['name']}/languages"))[:4]
    updated = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
    meta = " ".join(f"`{lang}`" for lang in langs)
    meta = (meta + " · " if meta else "") + f"Updated {updated:%b %Y}"
    lines += ["", meta]
    return "\n".join(lines)


def main():
    with open(README, encoding="utf-8") as f:
        text = f.read()
    if START not in text or END not in text:
        sys.exit(f"{README} is missing the {START} / {END} markers")

    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    handwritten = (before + after).lower()

    repos = api(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
    picked = [
        r for r in repos
        if not r["fork"] and not r["archived"] and not r["private"]
        and r["name"].lower() != USER.lower()
        and (not TOPIC or TOPIC in r.get("topics", []))
        and f"github.com/{USER}/{r['name']}".lower() not in handwritten
    ]

    body = "\n\n".join(render(r) for r in picked)
    if body:
        body = "### More projects\n\n" + body
    section = f"{START}\n{body}\n{END}" if body else f"{START}\n{END}"
    new = before + section + after
    if new != text:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new)
    print(f"{len(picked)} project(s): " + ", ".join(r["name"] for r in picked))


if __name__ == "__main__":
    main()
