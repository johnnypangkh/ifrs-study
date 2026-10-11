#!/usr/bin/env python3
"""Every custom property in tokens.css and type-scale.css is in exactly one settings row."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "_shared" / "tokens.css"
TYPE_SCALE = ROOT / "_shared" / "type-scale.css"
PAGE = ROOT / "site" / "settings" / "index.html"
PARTIAL = ROOT / "_shared" / "settings-rows.html"
PROP = re.compile(r"(--[\w-]+)\s*:")
ROW = re.compile(r'<tr class="row\b[^"]*">.*?</tr>', re.S)
CODE = re.compile(r"<code>(--[\w-]+)</code>")
BEGIN = "<!-- BEGIN SETTINGS ROWS -->"
END = "<!-- END SETTINGS ROWS -->"


def defined_names():
    names = []
    seen = set()
    for path in (TOKENS, TYPE_SCALE):
        for name in PROP.findall(path.read_text(encoding="utf-8")):
            if name not in seen:
                seen.add(name)
                names.append(name)
    return names


def main():
    page = PAGE.read_text(encoding="utf-8")
    partial = PARTIAL.read_text(encoding="utf-8")
    start = page.index(BEGIN) + len(BEGIN)
    end = page.index(END)
    injected = page[start:end].strip("\n")
    if injected != partial.strip("\n"):
        print("settings page rows differ from _shared/settings-rows.html")
        return 1
    rows = ROW.findall(page)
    counts = {}
    for row in rows:
        for name in CODE.findall(row):
            counts[name] = counts.get(name, 0) + 1
    defined = defined_names()
    missing = [name for name in defined if counts.get(name, 0) == 0]
    duplicated = [name for name, count in counts.items() if count != 1]
    extra = [name for name in counts if name not in set(defined)]
    placeholders = all(title in page for title in ("Box", "Components", "TopBar"))
    covered = len(defined) - len(missing)
    print(
        f"{len(defined)} tokens / {covered} covered / {len(missing)} missing / "
        f"{len(duplicated)} duplicated / {len(rows)} rows"
    )
    if missing:
        print("missing: " + ", ".join(missing))
    if duplicated:
        print("duplicated: " + ", ".join(duplicated))
    if extra:
        print("not a token: " + ", ".join(extra))
    if not placeholders:
        print("missing Box, Components, or TopBar placeholder")
    if missing or duplicated or extra or not placeholders:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
