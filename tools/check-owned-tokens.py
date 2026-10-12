#!/usr/bin/env python3
"""Fail if a tokens.css custom property is defined elsewhere in _shared.

tokens-core.css is the generated owner copy and is excluded. The four mobile
type-scale declarations are the F1 exception and may also appear in the
type-scale module.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "_shared"
TOKENS = SHARED / "tokens.css"
PROP = re.compile(r"(--[\w-]+)\s*:")
F1 = {
    "--type-scale: 0.85;",
    "--vis-body: calc(12px * var(--type-scale));",
    "--vis-meta: calc(11px * var(--type-scale));",
    "--nx-chip-font: calc(10px * var(--type-scale));",
}
SKIP = {"_shared/tokens.css", "_shared/tokens-core.css"}
# Visual pages did not load tokens.css. ias16.css uses
# var(--space-2, 0.45rem) on .ch01-scope .carve-set, so the used gap was
# 7.2px. tokens-core defines --space-2 as .5rem. This one declaration
# keeps that used value. Any other foreign definition still fails.
RESTORE = {
    "_shared/modules/visuals/colour-1.css": {"--space-2: var(--space-cell);"},
}


def strip_comments(text):
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def defined_in(text, allow_f1, rel):
    names = []
    for line in strip_comments(text).splitlines():
        stripped = line.strip()
        if allow_f1 and stripped in F1:
            continue
        if stripped in RESTORE.get(rel, ()):
            continue
        names.extend(PROP.findall(line))
    return names


def main():
    owned = []
    seen = set()
    for name in PROP.findall(TOKENS.read_text(encoding="utf-8")):
        if name not in seen:
            seen.add(name)
            owned.append(name)
    owned_set = set(owned)
    hits = []
    for path in sorted(SHARED.rglob("*.css")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP:
            continue
        allow_f1 = "type-scale" in rel
        found = sorted({name for name in defined_in(path.read_text(encoding="utf-8"), allow_f1, rel) if name in owned_set})
        if not found:
            continue
        hits.append(rel)
        print(f"{rel}\t{len(found)}\t{', '.join(found)}")
    print(f"owned names {len(owned)}; files with a foreign definition {len(hits)}")
    if hits:
        return 1
    print("owned-token grep: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
