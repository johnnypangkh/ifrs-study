#!/usr/bin/env python3
"""Rebuild search-index.js from chapter pages that exist on disk.

The homepage search script does not name packs or chapters. After any
draft-v1-linked/ch*.html page changes, run this script again and commit
homepage/search-index.js plus the search-index.js?v= stamps it writes.

The ?v= value is the first 12 hex digits of the SHA-256 of the generated
index file. It changes exactly when that file changes, and a second run
on unchanged chapters rewrites nothing.
"""

import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

# Site root is the directory that contains homepage/ and the packs.
# That is this repo (on disk: ifrs-website-refs/refs/, on GitHub Pages:
# /ifrs-study/). parents[2] is the folder above that root. Indexing it
# stored ../../ links to a sibling copy. Those links 404 on GitHub Pages
# (johnnypangkh.github.io/<pack>/...) and skip the chapters in this tree.
ROOT = Path(__file__).resolve().parents[1]
HOME = Path(__file__).resolve().parent
OUT = HOME / "search-index.js"

SKIP_TAGS = {"script", "style", "noscript"}


class ChapterText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.skip_link = 0
        self.capture_h1 = False
        self.h1_done = False
        self.h1 = []
        self.sections = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "a" and "sec-top" in attrs.get("class", "").split():
            self.skip_link += 1
            return
        if tag == "h1" and not self.h1_done:
            self.capture_h1 = True
        if tag in ("h2", "h3", "h4"):
            self.current = {
                "id": attrs.get("id") or "",
                "parts": [],
            }
            self.sections.append(self.current)

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1
            return
        if tag == "a" and self.skip_link:
            self.skip_link -= 1
            return
        if tag == "h1":
            self.capture_h1 = False
            self.h1_done = True

    def handle_data(self, data):
        if self.skip or self.skip_link:
            return
        if self.capture_h1:
            self.h1.append(data)
        elif self.current is not None:
            self.current["parts"].append(data)


def plain(parts):
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def ensure_ids(html):
    html, n1 = re.subn(
        r"<h1(?![^>]*\bid=)>",
        '<h1 id="chapter-title">',
        html,
        count=1,
    )
    html, n2 = re.subn(
        r"<h2(?![^>]*\bid=)>\s*Key terms\s*</h2>",
        '<h2 id="key-terms">Key terms</h2>',
        html,
        count=1,
    )
    return html, n1, n2


def chapter_pages():
    pages = []
    for path in ROOT.glob("*/draft-v1-linked/ch*.html"):
        if path.parent.name != "draft-v1-linked":
            continue
        if not path.is_file():
            continue
        pages.append(path)
    return sorted(pages)


def os_relpath(path, start):
    import os
    return os.path.relpath(path, start)


# Only the search-index.js script src is rewritten. Other script tags stay
# byte-for-byte, including their own ?v= query strings.
SCRIPT_SRC = re.compile(
    r'(<script\b[^>]*?\bsrc=")([^"]*?search-index\.js)(?:\?[^"]*)?(")'
    r"|(<script\b[^>]*?\bsrc=')([^']*?search-index\.js)(?:\?[^']*)?(')"
)


def index_stamp(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def pages_loading_index():
    """HTML files that load search-index.js, one path per real file.

    preview/ is a symlink to draft-v1-linked/, so both paths name the same
    chapter file. Resolve and skip duplicates so the stamp is written once.
    """
    seen = set()
    pages = []
    for path in sorted(ROOT.rglob("*.html")):
        if not path.is_file():
            continue
        real = path.resolve()
        if real in seen:
            continue
        seen.add(real)
        if b"search-index.js" not in real.read_bytes():
            continue
        pages.append(real)
    return pages


def stamp_references(stamp):
    """Point every search-index.js script src at ?v=<stamp>."""
    changed = []
    missed = []
    for path in pages_loading_index():
        html = path.read_text(encoding="utf-8")

        def repl(match, stamp=stamp):
            if match.group(1) is not None:
                return f"{match.group(1)}{match.group(2)}?v={stamp}{match.group(3)}"
            return f"{match.group(4)}{match.group(5)}?v={stamp}{match.group(6)}"

        updated, count = SCRIPT_SRC.subn(repl, html)
        rel = str(path.relative_to(ROOT))
        if count == 0:
            missed.append(rel)
            continue
        if updated != html:
            path.write_text(updated, encoding="utf-8")
            changed.append(rel)
    return changed, missed


def main():
    index = []
    touched = []
    for path in chapter_pages():
        html = path.read_text(encoding="utf-8")
        updated, n1, n2 = ensure_ids(html)
        if updated != html:
            path.write_text(updated, encoding="utf-8")
            touched.append(str(path.relative_to(ROOT)))
            html = updated
        parser = ChapterText()
        parser.feed(html)
        chapter = plain(parser.h1)
        if not chapter:
            continue
        href_base = Path(os_relpath(path, HOME)).as_posix()
        index.append({
            "chapter": chapter,
            "href": href_base + "#chapter-title",
            "text": chapter,
        })
        for section in parser.sections:
            if not section["id"]:
                continue
            text = plain(section["parts"])
            if not text:
                continue
            index.append({
                "chapter": chapter,
                "href": href_base + "#" + section["id"],
                "text": text,
            })
    payload = json.dumps(index, ensure_ascii=False, indent=2)
    payload = payload.replace("<", "\\u003c")
    generated = (
        "/* Generated from existing chapter pages. Do not hand-edit.\n"
        "   Re-run build-search-index.py after a chapter page changes.\n"
        "   That run also refreshes search-index.js?v= from a hash of this file. */\n"
        "window.HOMEPAGE_SEARCH_INDEX = " + payload + ";\n"
    )
    OUT.write_text(generated, encoding="utf-8")
    stamp = index_stamp(generated)
    changed, missed = stamp_references(stamp)
    print(
        f"pages {len(chapter_pages())} entries {len(index)} "
        f"stamp {stamp} -> {OUT.relative_to(ROOT)}"
    )
    for name in touched:
        print("id", name)
    for name in changed:
        print("stamp", name)
    for name in missed:
        print("unstamped", name)


if __name__ == "__main__":
    main()
