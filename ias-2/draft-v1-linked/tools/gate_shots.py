"""Capture gate screenshots of the IAS 2 pack from the local static server.

Usage: python3 tools/gate_shots.py <gate-label> [base-url] [shot-set]
Writes PNGs to /opt/cursor/artifacts/screenshots/<gate-label>-*.png
shot-set: "review" (default) or a chapter set such as "ch01".
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

GATE = sys.argv[1] if len(sys.argv) > 1 else "gate"
BASE = sys.argv[2] if len(sys.argv) > 2 else "http://127.0.0.1:47213"
SET = sys.argv[3] if len(sys.argv) > 3 else "review"
OUT = Path("/opt/cursor/artifacts/screenshots")
OUT.mkdir(parents=True, exist_ok=True)

# (name, page, mode, selector-or-height)
SHOT_SETS = {}
SHOT_SETS["review"] = [
    ("pack-map-index", "index.html", "full", None),
    ("ch01-top", "ch01.html", "clip", 2200),
    ("ch03-illus-sample", "ch03.html", "element", ".worked-strip"),
    ("ch03-top", "ch03.html", "clip", 1800),
    ("ch04-dense-top", "ch04.html", "clip", 2400),
    ("ch04-illus-sample", "ch04.html", "element", ".worked-strip"),
]
SHOT_SETS["ch01"] = [
    ("ch01-concept-map", "ch01.html", "element", ".visual-section"),
    ("ch01-top", "ch01.html", "clip", 2400),
    ("ch01-illus-1-1-3-spare-parts", "ch01.html", "element", "#s-1-ex-spare"),
    ("ch01-illus-1-1-7-co2e-table", "ch01.html", "element", "#s-1-ex-dtt-co2e-offsets"),
    ("ch01-section-1-3", "ch01.html", "range", ("#s-1-3", "#s-1-ex-ey-scope")),
    ("ch01-illus-1-3-1-commodities", "ch01.html", "element", "#s-1-ex-ey-scope"),
    ("ch01-section-1-4-1-5", "ch01.html", "range", ("#s-1-4", ".key-terms")),
    ("ch01-mobile-map", "ch01.html", "mobile", ".visual-section"),
]
SHOT_SETS["ch01-map"] = [
    ("ch01-concept-map-desktop", "ch01.html", "element", ".visual-section"),
    ("ch01-concept-map-mobile", "ch01.html", "mobile", ".visual-section"),
]
SHOT_SETS["ch02"] = [
    ("ch02-concept-map-desktop", "ch02.html", "element", ".visual-section"),
    ("ch02-concept-map-mobile", "ch02.html", "mobile", ".visual-section"),
    ("ch02-section-2-0-2-1", "ch02.html", "range", ("#s-2-0", "#s-2-2")),
    ("ch02-section-2-2", "ch02.html", "range", ("#s-2-2", "#s-2-3")),
    ("ch02-section-2-3", "ch02.html", "range", ("#s-2-3", "#s-2-ex-consign")),
    ("ch02-illus-2-3-1-consignment", "ch02.html", "element", "#s-2-ex-consign"),
    ("ch02-section-2-4-key-terms", "ch02.html", "range", ("#s-2-4", ".footer-nav")),
]
SHOT_SETS["maps-ch1-ch2"] = [
    ("ch01-concept-map-desktop", "ch01.html", "element", ".visual-section"),
    ("ch01-concept-map-mobile", "ch01.html", "mobile", ".visual-section"),
    ("ch02-concept-map-desktop", "ch02.html", "element", ".visual-section"),
    ("ch02-concept-map-mobile", "ch02.html", "mobile", ".visual-section"),
]
SHOT_SETS["ch03"] = [
    ("ch03-concept-map-desktop", "ch03.html", "element", ".visual-section"),
    ("ch03-concept-map-mobile", "ch03.html", "mobile", ".visual-section"),
    ("ch03-section-3-0-3-1", "ch03.html", "range", ("#s-3-0", "#s-3-ex-pwc-252")),
    ("ch03-illus-3-2-2-volume-refund-flow", "ch03.html", "element", "#s-3-ex-vol-rebate"),
    ("ch03-illus-3-2-3-beds-table", "ch03.html", "element", "#s-3-ex-kpmg-vol-4b"),
    ("ch03-variable-payable-matrix", "ch03.html", "range", ("#s-3-2-variable", "#s-3-ex-pwc-195")),
    ("ch03-section-3-3-capacity", "ch03.html", "range", ("#s-3-3", "#s-3-ex-b")),
    ("ch03-illus-3-3-1-televisions", "ch03.html", "element", "#s-3-ex-b"),
    ("ch03-illus-3-3-3-overhead-rates", "ch03.html", "element", "#s-3-ex-pwc-oh"),
    ("ch03-illus-3-3-5-shutdown-flow", "ch03.html", "element", "#s-3-ex-kpmg-shutdown"),
    ("ch03-interruptions-allocation", "ch03.html", "range", ("#s-3-ex-kpmg-interrupt", "#s-3-3-leases")),
    ("ch03-section-3-4", "ch03.html", "range", ("#s-3-4", "#s-3-5")),
    ("ch03-distribution-table", "ch03.html", "range", ("#s-3-ex-dtt-distrib", "#s-3-ex-pwc-194")),
    ("ch03-section-3-7-3-8", "ch03.html", "range", ("#s-3-7", "#s-3-9")),
    ("ch03-illus-3-9-1-retail", "ch03.html", "element", "#s-3-ex-retail"),
    ("ch03-section-3-10-lifo", "ch03.html", "range", ("#s-3-10", "#s-3-ex-kpmg-fifo-wa")),
    ("ch03-illus-3-10-2-fifo-wa", "ch03.html", "element", "#s-3-ex-c"),
    ("ch03-formula-comparison-key-terms", "ch03.html", "range", ("#s-3-ex-pwc-fifo", ".footer-nav")),
    ("ch03-mobile-illus-3-3-5", "ch03.html", "mobile", "#s-3-ex-kpmg-shutdown"),
    ("ch03-mobile-illus-3-3-1", "ch03.html", "mobile", "#s-3-ex-b"),
]
SHOT_SETS["ch04"] = [
    ("ch04-concept-map-desktop", "ch04.html", "element", ".visual-section"),
    ("ch04-concept-map-mobile", "ch04.html", "mobile", ".visual-section"),
    ("ch04-section-4-0-4-1", "ch04.html", "range", ("#s-4-0", "#s-4-ex-costs-sell")),
    ("ch04-section-4-2", "ch04.html", "range", ("#s-4-2", "#s-4-ex-ey-anglogold")),
    ("ch04-section-4-3", "ch04.html", "range", ("#s-4-3", "#s-4-ex-kpmg-fx-nrv")),
    ("ch04-section-4-4-formulas", "ch04.html", "range", ("#s-4-4", "#s-4-ex-formula")),
    ("ch04-section-4-5-events", "ch04.html", "range", ("#s-4-5", "#s-4-ex-post")),
    ("ch04-illus-4-5-2-kpmg-post", "ch04.html", "element", "#s-4-ex-kpmg-post"),
    ("ch04-illus-4-5-3-developer", "ch04.html", "element", "#s-4-ex-dev"),
    ("ch04-illus-4-5-6-intended-use", "ch04.html", "element", "#s-4-ex-kpmg-intended"),
    ("ch04-section-4-5-contracts", "ch04.html", "range", ("#s-4-5-contracts", "#s-4-ex-firm")),
    ("ch04-illus-4-5-9-firm-contracts", "ch04.html", "element", "#s-4-ex-kpmg-firm15"),
    ("ch04-section-4-6", "ch04.html", "range", ("#s-4-6", "#s-4-ex-pwc-mat")),
    ("ch04-section-4-7", "ch04.html", "range", ("#s-4-7", "#s-4-ex-d")),
    ("ch04-key-terms", "ch04.html", "range", (".key-terms", ".footer-nav")),
    ("ch04-mobile-illus-4-6-1", "ch04.html", "mobile", "#s-4-ex-pwc-mat"),
    ("ch04-mobile-illus-4-7-1", "ch04.html", "mobile", "#s-4-ex-d"),
]
SHOT_SETS["map-yesno"] = [
    (f"ch0{n}-{mode_name}", f"ch0{n}.html", mode, ".visual-section")
    for n in (1, 2, 3, 4)
    for mode_name, mode in (("desktop", "element"), ("mobile", "mobile"))
]
SHOT_SETS["ch05"] = [
    ("ch05-concept-map-desktop", "ch05.html", "element", ".visual-section"),
    ("ch05-concept-map-mobile", "ch05.html", "mobile", ".visual-section"),
    ("ch05-section-5-0", "ch05.html", "range", ("#s-5-0", "#s-5-1")),
    ("ch05-section-5-1", "ch05.html", "range", ("#s-5-1", "#s-5-2")),
    ("ch05-section-5-2-5-3", "ch05.html", "range", ("#s-5-2", "#s-5-ex-rev")),
    ("ch05-illus-5-3-1", "ch05.html", "element", "#s-5-ex-rev"),
    ("ch05-section-5-4-key-terms", "ch05.html", "range", ("#s-5-4", ".footer-nav")),
    ("ch05-mobile-illus-5-3-1", "ch05.html", "mobile", "#s-5-ex-rev"),
    ("ch05-mobile-section-5-0", "ch05.html", "mobile", "#s-5-0 ~ .mini-flow"),
]
SHOT_SETS["ch06"] = [
    ("ch06-concept-map-desktop", "ch06.html", "element", ".visual-section"),
    ("ch06-concept-map-mobile", "ch06.html", "mobile", ".visual-section"),
    ("ch06-section-6-0", "ch06.html", "range", ("#s-6-0", "#s-6-1")),
    ("ch06-section-6-1", "ch06.html", "range", ("#s-6-1", "#s-6-2")),
    ("ch06-section-6-2-presentation", "ch06.html", "range", ("#s-6-2", "#s-6-ex-ey-stora")),
    ("ch06-illus-6-2-1", "ch06.html", "element", "#s-6-ex-ey-stora"),
    ("ch06-section-6-3", "ch06.html", "range", ("#s-6-3", "#s-6-4")),
    ("ch06-section-6-4", "ch06.html", "range", ("#s-6-4", "#s-6-ex-kpmg-rev17")),
    ("ch06-illus-6-4-1", "ch06.html", "element", "#s-6-ex-kpmg-rev17"),
    ("ch06-illus-6-4-2", "ch06.html", "element", "#s-6-ex-ey-unilever"),
    ("ch06-section-6-5-6-6-key-terms", "ch06.html", "range", ("#s-6-5", ".footer-nav")),
    ("ch06-mobile-illus-6-4-1", "ch06.html", "mobile", "#s-6-ex-kpmg-rev17"),
    ("ch06-mobile-section-6-0-table", "ch06.html", "mobile", "#s-6-0 ~ .table-wrap"),
    ("ch06-pack-map-desktop", "index.html", "element", ".visual-section"),
    ("ch06-pack-map-mobile", "index.html", "mobile", ".visual-section"),
]
SHOTS = SHOT_SETS[SET]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/usr/local/bin/google-chrome")
        ctx = browser.new_context(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
        for name, page_path, mode, arg in SHOTS:
            page = ctx.new_page()
            page.goto(f"{BASE}/{page_path}", wait_until="networkidle")
            page.wait_for_timeout(800)
            if mode in ("element", "mobile"):
                page.add_style_tag(content=".chrome-bar{position:static !important}")
            dest = OUT / f"{GATE}-{name}.png"
            if mode == "full":
                page.screenshot(path=str(dest), full_page=True)
            elif mode == "clip":
                height = min(arg, page.evaluate("document.body.scrollHeight"))
                page.screenshot(path=str(dest), full_page=True,
                                clip={"x": 0, "y": 0, "width": 1280, "height": height})
            elif mode == "range":
                top = page.locator(arg[0]).first.bounding_box()
                end = page.locator(arg[1]).first.bounding_box()
                y0 = page.evaluate("window.scrollY") + top["y"] - 8
                y1 = page.evaluate("window.scrollY") + end["y"] + end["height"] + 8
                page.screenshot(path=str(dest), full_page=True,
                                clip={"x": 0, "y": y0, "width": 1280, "height": y1 - y0})
            elif mode == "mobile":
                page.set_viewport_size({"width": 420, "height": 900})
                page.wait_for_timeout(800)
                page.locator(arg).first.screenshot(path=str(dest))
            elif mode == "element":
                el = page.locator(arg).first
                el.scroll_into_view_if_needed()
                el.screenshot(path=str(dest))
            print(dest)
            page.close()
        browser.close()


if __name__ == "__main__":
    main()
