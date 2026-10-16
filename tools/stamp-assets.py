#!/usr/bin/env python3
"""Set local IAS 16 ?v= stamps, pack-page stamps for IAS 2 and CF, and shared stamps.

Every href, src, or CSS url() under ias-16/draft-v1-linked/ that already
has ?v= and points at a local .css, .js, or .html file is rewritten to
the first 12 hex digits of that file's SHA-256. Hand tokens such as
?v=ias16-flow-v3-20261010 are replaced. References with no ?v= are left
alone, so chapter links like ch06.html#s-6-0 stay as they are.

IAS 2 and CF 2018 pack pages (draft-v1-linked/*.html, not files under
visuals/) get the same treatment for every local css/js/html target
inside that pack. Visual-page stamps in those packs are left alone.
IFRS 18 pack-local stamps are left as they are.

The same hash is written onto _shared asset ?v= values on every pack
page (ias-16, ias-2, ifrs-18, cf-2018 draft-v1-linked). footer-nav.js
keeps its name stamp. search-index.js and last-update.js are skipped.
homepage/build-search-index.py and tools/build-last-update.py own those
stamps.

The hash is of the file on disk, so a stamp inside the target changes
its hash. The script repeats until a pass rewrites nothing, which is
stable for the pack's acyclic asset graph (css/js, then visuals, then
pages that iframe them). A second run of this script rewrites nothing.
"""

import sys
from pathlib import Path

from map_sections import (
    ATTR_URL,
    CSS_URL,
    LOCAL_SUFFIXES,
    PACK,
    ROOT,
    SKIP_STAMP_NAMES,
    file_stamp,
    iter_versioned_refs,
    query_v,
    set_query_v,
    split_url,
)

LIVE_PACKS = ("ias-16", "ias-2", "ifrs-18", "cf-2018")
# Pack pages whose local css/js/html ?v= is hashed. IAS 16 is handled by
# the full-tree walk. Visual files under these packs stay put.
PAGE_LOCAL_PACKS = ("ias-2", "cf-2018")
# Name stamp owned by the chapter template. Do not replace it with a hash.
NAME_STAMP_FILES = {"footer-nav.js"}
TEXT_SUFFIXES = {".html", ".css", ".js"}


def pack_text_files(pack=PACK):
    files = []
    for path in sorted(pack.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        files.append(path)
    return files


def pack_pages():
    """The 44 live pack pages. Visuals keep their own stamps."""
    files = []
    for name in LIVE_PACKS:
        pack = ROOT / name / "draft-v1-linked"
        if not pack.is_dir():
            raise SystemExit(f"missing pack {pack}")
        files.extend(sorted(pack.glob("*.html")))
    return files


def resolve_shared(from_file, url_path):
    """Return a _shared file for a relative css/js/html URL, else None."""
    if not url_path or url_path.startswith(("#", "?", "data:", "mailto:")):
        return None
    if url_path.startswith(("http://", "https://", "//", "/")):
        return None
    path = url_path.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    candidate = (from_file.parent / path).resolve()
    shared = (ROOT / "_shared").resolve()
    try:
        candidate.relative_to(shared)
    except ValueError:
        return None
    if candidate.suffix.lower() not in LOCAL_SUFFIXES:
        return None
    if candidate.name in SKIP_STAMP_NAMES or candidate.name in NAME_STAMP_FILES:
        return None
    if not candidate.is_file():
        return None
    return candidate


def resolve_pack_local(from_file, url_path, pack_root):
    """Return a css/js/html file inside pack_root, else None."""
    if not url_path or url_path.startswith(("#", "?", "data:", "mailto:")):
        return None
    if url_path.startswith(("http://", "https://", "//", "/")):
        return None
    path = url_path.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    candidate = (from_file.parent / path).resolve()
    try:
        candidate.relative_to(pack_root.resolve())
    except ValueError:
        return None
    if candidate.suffix.lower() not in LOCAL_SUFFIXES:
        return None
    if candidate.name in SKIP_STAMP_NAMES or candidate.name in NAME_STAMP_FILES:
        return None
    if not candidate.is_file():
        return None
    return candidate


def iter_pack_local_refs(text, from_file, pack_root):
    """Versioned refs that point at a css/js/html file inside pack_root."""
    spans = []
    for match in ATTR_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    for match in CSS_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    spans.sort()
    for start, end, url in spans:
        path, query, fragment = split_url(url)
        version = query_v(query)
        if version is None:
            continue
        local = resolve_pack_local(from_file, path, pack_root)
        if local is None:
            continue
        yield {
            "start": start,
            "end": end,
            "url": url,
            "path": path,
            "query": query,
            "fragment": fragment,
            "local": local,
        }


def iter_shared_refs(text, from_file):
    """Versioned refs that point at a content-hashed file under _shared/."""
    spans = []
    for match in ATTR_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    for match in CSS_URL.finditer(text):
        spans.append((match.start("url"), match.end("url"), match.group("url")))
    spans.sort()
    for start, end, url in spans:
        path, query, fragment = split_url(url)
        version = query_v(query)
        if version is None:
            continue
        local = resolve_shared(from_file, path)
        if local is None:
            continue
        yield {
            "start": start,
            "end": end,
            "url": url,
            "path": path,
            "query": query,
            "fragment": fragment,
            "local": local,
        }


def stamp_once(ias_files, pack_files):
    hashed = {path.resolve() for path in ias_files}
    # Shared targets are outside the pack trees. Hash them on demand.
    hashes = {path: file_stamp(Path(path)) for path in hashed}
    changed = []

    def apply(path, refs):
        nonlocal hashes
        if not refs:
            return
        text = path.read_text(encoding="utf-8")
        parts = []
        cursor = 0
        dirty = False
        for ref in refs:
            local = ref["local"].resolve()
            if local not in hashes:
                hashes[local] = file_stamp(local)
            digest = hashes[local]
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
            changed.append(path.relative_to(ROOT).as_posix())

    ias_set = {path.resolve() for path in ias_files}
    page_set = {path.resolve() for path in pack_files}
    targets = []
    seen = set()
    for path in list(ias_files) + list(pack_files):
        key = path.resolve()
        if key in seen:
            continue
        seen.add(key)
        targets.append(path)
    for path in targets:
        text = path.read_text(encoding="utf-8")
        refs = []
        key = path.resolve()
        if key in page_set:
            refs.extend(iter_shared_refs(text, path))
            try:
                pack_name = path.resolve().relative_to(ROOT.resolve()).parts[0]
            except ValueError:
                pack_name = ""
            if pack_name in PAGE_LOCAL_PACKS:
                pack_root = ROOT / pack_name / "draft-v1-linked"
                refs.extend(iter_pack_local_refs(text, path, pack_root))
        if key in ias_set:
            refs.extend(ref for ref in iter_versioned_refs(text, path) if not ref["skip"])
        refs.sort(key=lambda ref: ref["start"])
        apply(path, refs)
    return changed


def main():
    if not PACK.is_dir():
        raise SystemExit(f"missing pack {PACK}")
    ias_files = pack_text_files()
    pack_files = pack_pages()
    seen = set()
    for _ in range(12):
        changed = stamp_once(ias_files, pack_files)
        if not changed:
            print(f"stamps stable ({len(pack_files)} files)")
            return 0
        fresh = [name for name in changed if name not in seen]
        seen.update(changed)
        print("stamped " + ", ".join(fresh or changed))
    raise SystemExit("stamp-assets.py did not converge; local ?v= references may be cyclic")


if __name__ == "__main__":
    sys.exit(main())
