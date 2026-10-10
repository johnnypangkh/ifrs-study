#!/usr/bin/env python3
"""Set local IAS 16 ?v= stamps to the SHA-256 of the target file.

Every href, src, or CSS url() under ias-16/draft-v1-linked/ that already
has ?v= and points at a local .css, .js, or .html file is rewritten to
the first 12 hex digits of that file's SHA-256. Hand tokens such as
?v=ias16-flow-v3-20261010 are replaced. References with no ?v= are left
alone, so chapter links like ch06.html#s-6-0 stay as they are.

search-index.js and last-update.js are skipped. homepage/build-search-index.py
and tools/build-last-update.py own those stamps.

The hash is of the file on disk, so a stamp inside the target changes
its hash. The script repeats until a pass rewrites nothing, which is
stable for the pack's acyclic asset graph (css/js, then visuals, then
pages that iframe them). A second run of this script rewrites nothing.
"""

import sys
from pathlib import Path

from map_sections import (
    PACK,
    file_stamp,
    iter_versioned_refs,
    set_query_v,
)


def pack_text_files():
    files = []
    for path in sorted(PACK.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".css", ".js"}:
            continue
        files.append(path)
    return files


def stamp_once(files):
    hashes = {path.resolve(): file_stamp(path) for path in files}
    changed = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        refs = [ref for ref in iter_versioned_refs(text, path) if not ref["skip"]]
        if not refs:
            continue
        parts = []
        cursor = 0
        dirty = False
        for ref in refs:
            digest = hashes[ref["local"].resolve()]
            url = ref["path"] + set_query_v(ref["query"], digest) + ref["fragment"]
            if f"v={digest}" not in url:
                raise SystemExit(f"stamp rewrite dropped ?v= in {path}: {url}")
            parts.append(text[cursor:ref["start"]])
            parts.append(url)
            if url != ref["url"]:
                dirty = True
            cursor = ref["end"]
        parts.append(text[cursor:])
        updated = "".join(parts)
        if dirty and updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(path.relative_to(PACK.parent.parent).as_posix())
    return changed


def main():
    if not PACK.is_dir():
        raise SystemExit(f"missing pack {PACK}")
    files = pack_text_files()
    seen = set()
    for _ in range(12):
        changed = stamp_once(files)
        if not changed:
            print(f"stamps stable ({len(files)} files)")
            return 0
        fresh = [name for name in changed if name not in seen]
        seen.update(changed)
        print("stamped " + ", ".join(fresh or changed))
    raise SystemExit("stamp-assets.py did not converge; local ?v= references may be cyclic")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.exit(main())
