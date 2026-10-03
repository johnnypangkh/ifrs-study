#!/usr/bin/env python3
"""Rebuild search-index.js from chapter pages that exist on disk.

The homepage search script does not name packs or chapters. Add or remove
a draft-v1-linked/ch*.html page, then run this script again.
"""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
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
    OUT.write_text(
        "/* Generated from existing chapter pages. Do not hand-edit.\n"
        "   Re-run build-search-index.py after a chapter is added or removed. */\n"
        "window.HOMEPAGE_SEARCH_INDEX = " + payload + ";\n",
        encoding="utf-8",
    )
    print(f"pages {len(chapter_pages())} entries {len(index)} -> {OUT.relative_to(ROOT)}")
    for name in touched:
        print("id", name)


def os_relpath(path, start):
    import os
    return os.path.relpath(path, start)


if __name__ == "__main__":
    main()
