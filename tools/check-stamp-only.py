#!/usr/bin/env python3
"""Existing pages may change only the Last update stamp text and ?v= restamps.

The homepage may also gain the one Settings link. Writes nothing unless
--csv is given.
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V_QUERY = re.compile(r"\?v=[A-Za-z0-9._~%-]*")
STAMP = re.compile(r"Last update · \d{4}-\d{2}-\d{2} \d{2}:\d{2} HKT")
HOME = "homepage/homepage-wireframe-v0.1.html"
LINK = (
    '    <p><a href="../site/settings/index.html" style="color:var(--blue)">Settings</a></p>\n'
)
STAMPS_OBJ = re.compile(r"var STAMPS = \{.*?\n  \};", re.S)
PATHS_OBJ = re.compile(r"var PACK_PATHS = \[.*?\n  \];", re.S)


def git_text(rev, path):
    result = subprocess.run(
        ["git", "show", f"{rev}:{path}"],
        cwd=ROOT,
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8")


def git_paths(rev):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", rev],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines() if line.endswith(".html")]


def norm(text):
    return V_QUERY.sub("?v=", text)


def load_stamps(text):
    match = re.search(r"var STAMPS = (\{.*?\n  \});", text, re.S)
    if not match:
        raise SystemExit("last-update.js has no STAMPS object")
    import json
    return json.loads(match.group(1))


def logic_same(base, head):
    def mask(text):
        text = STAMPS_OBJ.sub("var STAMPS = {};", text, count=1)
        text = PATHS_OBJ.sub("var PACK_PATHS = [];", text, count=1)
        return text
    return mask(base) == mask(head)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--csv")
    args = parser.parse_args()
    failed = False
    rows = []
    for path in git_paths(args.base):
        base = git_text(args.base, path)
        file = ROOT / path
        if base is None or not file.is_file():
            print(f"missing existing page {path}")
            failed = True
            continue
        head = file.read_text(encoding="utf-8")
        base_n = norm(base)
        head_n = norm(head)
        if path == HOME:
            if LINK not in head:
                print("homepage is missing the Settings link")
                failed = True
            head_n = head_n.replace(LINK, "", 1)
        if head_n != base_n:
            print(f"HTML changed outside ?v= and the homepage link: {path}")
            failed = True
    base_js = git_text(args.base, "_shared/last-update.js")
    head_js = (ROOT / "_shared" / "last-update.js").read_text(encoding="utf-8")
    if not logic_same(base_js, head_js):
        print("last-update.js changed more than stamp data")
        failed = True
    base_stamps = load_stamps(base_js)
    head_stamps = load_stamps(head_js)
    if "site" not in head_stamps:
        print("site stamp missing")
        failed = True
    for key, base_stamp in sorted(base_stamps.items()):
        head_stamp = head_stamps.get(key)
        if not head_stamp:
            print(f"stamp removed: {key}")
            failed = True
            continue
        only = STAMP.fullmatch(head_stamp["text"]) and set(head_stamp) == set(base_stamp)
        if not only:
            print(f"stamp shape changed: {key}")
            failed = True
        rows.append({
            "page": key,
            "base_stamp": base_stamp["text"],
            "head_stamp": head_stamp["text"],
            "only_stamp_changed": "yes" if only else "no",
        })
    if args.csv:
        with open(args.csv, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["page", "base_stamp", "head_stamp", "only_stamp_changed"],
            )
            writer.writeheader()
            writer.writerows(rows)
    for row in rows:
        print(
            f"{row['page']}\t{row['base_stamp']}\t{row['head_stamp']}\t{row['only_stamp_changed']}"
        )
    if failed:
        return 1
    print("stamp-only: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
