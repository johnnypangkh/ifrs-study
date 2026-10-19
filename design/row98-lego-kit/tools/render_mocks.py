"""Render the token-only mock pages in ../mocks to PNG (dark, 1280 wide).

lego-sheet.html and lego-combos.html go to the kit folder root; every other
mock page goes next to its HTML in mocks/.
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

BASE = os.environ.get("MAP_BASE", "http://localhost:8765/")
CHROME = os.environ.get("CHROME", "/usr/local/bin/google-chrome")
KIT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.abspath(os.path.join(KIT, "..", ".."))
TOP = {"lego-sheet", "lego-combos"}


def main(only=None):
    pages = sorted(glob.glob(os.path.join(KIT, "mocks", "*.html")))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_context(viewport={"width": 1280, "height": 800}, color_scheme="dark").new_page()
        for f in pages:
            name = os.path.basename(f)[:-5]
            if only and only not in name:
                continue
            pg.goto(BASE + os.path.relpath(f, ROOT), wait_until="networkidle")
            pg.wait_for_timeout(300)
            out = os.path.join(KIT if name in TOP else os.path.join(KIT, "mocks"), name + ".png")
            pg.screenshot(path=out, full_page=True)
            print(out)
        b.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
