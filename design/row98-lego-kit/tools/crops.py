"""Evidence crops: one real rendered instance per brick / component.

Dark theme, 1280 viewport, live map files served from the repo root.
CF chapter embeds have a transparent body (the host page paints --bg), so the
script paints --bg behind every embed to match what readers see in the iframe.
"""
import os
import sys

from playwright.sync_api import sync_playwright

BASE = os.environ.get("MAP_BASE", "http://localhost:8765/")
CHROME = os.environ.get("CHROME", "/usr/local/bin/google-chrome")
OUT = os.path.join(os.path.dirname(__file__), "..", "evidence")

V = "/draft-v1-linked/visuals/"
# name, file, selector, nth, max height (px) or None
CROPS = [
    ("B01-board", "ias-2" + V + "ch02-recognition.html", ".st", 0, 520),
    ("B02-plate", "ias-16" + V + "ch02-recognition.html", ".plate", 0, 520),
    ("B03-cell", "ias-16" + V + "ch01-scope.html", ".peer", 0, None),
    ("B04-note", "ias-16" + V + "ch05-depreciation.html", ".soft-note", 0, None),
    ("B05-title", "ias-16" + V + "ch05-depreciation.html", ".plate-title", 0, None),
    ("B06-section-chip-fb-num", "ias-16" + V + "ch05-depreciation.html", ".inner-rail", 0, None),
    ("B06-section-chip-a-sec", "cf-2018/draft-v1-linked/index.html", "#conceptMap .status-purpose", 0, None),
    ("B07-kicker", "cf-2018" + V + "ch01-objective-users.html", ".ou-sec", 1, 320),
    ("B08-tag", "ifrs-18" + V + "ch03-pnl-categories.html", ".pc-band--operating", 0, None),
    ("B09-see-also", "ias-16" + V + "ch05-depreciation.html", "p.see", 0, None),
    ("B10-rail", "ias-16" + V + "ch05-depreciation.html", ".cap", 0, 420),
    ("B11-grid", "cf-2018" + V + "ch02-qualitative-characteristics.html", ".qc-tier", 1, None),
    ("B12-arrow-and-label", "ias-2" + V + "ch02-recognition.html", ".st-fork", 0, None),
    ("B13-bar", "ias-16" + V + "ch05-depreciation.html", ".method-band", 0, None),
    ("B14-operator", "ias-16" + V + "ch03-initial.html", ".cost-identity", 0, None),
    ("B15-time-axis", "ias-16" + V + "ch05-depreciation.html", ".lc-head", 0, None),
    ("B16-time-span", "ifrs-18" + V + "ch08-transition.html", ".tr-sec", 0, None),
    ("B17-tone-stop", "ias-16" + V + "ch01-scope.html", ".pack-stop", 0, None),
    ("B18-accent-strip", "ifrs-18" + V + "ch04-totals-subtotals.html", ".ts-sec", 0, 520),
    ("B19-echo-bar", "ias-16" + V + "ch05-depreciation.html", "nav.master-echo", 0, None),
    ("B20-hand-off", "ias-16" + V + "ch05-depreciation.html", ".pack-flow", 0, None),
    ("B21-glyph", "ias-16" + V + "ch05-depreciation.html", ".method-set", 0, None),
    ("R1-cite-chip-retire", "ias-16" + V + "ch04-models.html", ".cite", 0, None),
    ("R2-graph-paper-retire", "ias-2" + V + "map-formula-board.html", ".m-l0", 0, 260),
    # components
    ("C-and-gate-ias16", "ias-16" + V + "ch01-scope.html", ".scope-stack", 0, 420),
    ("C-and-gate-ias2", "ias-2" + V + "ch02-recognition.html", ".st-def", 0, None),
    ("C-and-gate-cf02", "cf-2018" + V + "ch02-qualitative-characteristics.html", ".qc-tier", 0, None),
    ("C-and-gate-cf05", "cf-2018" + V + "ch05-recognition-derecognition.html", ".rc-test--useful", 0, None),
    ("C-and-gate-cf03", "cf-2018" + V + "ch03-reporting-entity.html", "p.re-dual", 0, None),
    ("C-fork-ias16", "ias-16" + V + "ch01-scope.html", ".scope-stack", 0, None),
    ("C-fork-ias2", "ias-2" + V + "ch01-scope.html", ".st", 0, 640),
    ("C-fork-cf09", "cf-2018" + V + "ch09-combined.html", ".fork", 0, None),
    ("C-fork-cf05", "cf-2018" + V + "ch05-recognition-derecognition.html", ".rc-tree", 0, 520),
    ("C-ladder-ifrs18-ch06", "ifrs-18" + V + "ch06-mpms.html", ".gt", 0, None),
    ("C-ladder-ifrs18-ch03", "ifrs-18" + V + "ch03-classification-path.html", ".pc-tree", 0, None),
    ("C-timeline-cf03", "cf-2018" + V + "ch03-reporting-entity.html", ".re-axis", 0, None),
    ("C-timeline-ifrs18-ch01", "ifrs-18" + V + "ch01-whats-new.html", "ol.wn-tl", 0, None),
    ("C-timeline-ias16-ch04", "ias-16" + V + "ch04-models.html", ".lc-head", 0, None),
    ("C-formula-ias2", "ias-2" + V + "ch05-derecognition.html", ".exp-f", 0, None),
    ("C-formula-cf04", "cf-2018" + V + "ch04-elements.html", ".el-eq", 0, None),
    ("C-formula-ifrs18-ch06", "ifrs-18" + V + "ch06-mpms.html", ".rc-bridge", 0, None),
    ("C-ledger-ias16-ch04", "ias-16" + V + "ch04-models.html", ".vledger", 0, None),
    ("C-matrix-cf06", "cf-2018" + V + "ch06-measurement.html", ".mx-grid", 0, None),
    ("C-matrix-cf08", "cf-2018" + V + "ch08-capital.html", ".cap-matrix", 0, None),
    ("C-matrix-ifrs18-ch02", "ifrs-18" + V + "ch02-pfs-aggregation.html", ".pa-matrix", 0, None),
    ("C-matrix-ifrs18-ch08", "ifrs-18" + V + "ch08-transition.html", ".tr-mx", 0, None),
    ("C-matrix-ias16-ch04", "ias-16" + V + "ch04-models.html", ".policy-kids", 0, 420),
    ("C-rail-stack-ias16-ch07", "ias-16" + V + "ch07-disclosure.html", ".inner-board", 0, 520),
    ("C-nest-ifrs18-mba", "ifrs-18" + V + "ch03-mba-nest.html", ".page", 0, None),
    ("C-statement-ifrs18-ch04", "ifrs-18" + V + "ch04-totals-subtotals.html", ".ts-sec", 0, None),
    ("C-peers-bar-ias16-ch05", "ias-16" + V + "ch05-depreciation.html", ".method-set", 0, None),
    ("C-handoff-ias16-ch04", "ias-16" + V + "ch04-models.html", ".pack-flow", 0, None),
    ("S-thick-left-non-line-ifrs18-ch02", "ifrs-18" + V + "ch02-pfs-aggregation.html", ".pa-trap", 0, None),
    ("S-thick-left-non-line-ifrs18-ch06", "ifrs-18" + V + "ch06-mpms.html", ".rc-bridge", 0, None),
    ("S-m-see-on-content-ias16-ch04", "ias-16" + V + "ch04-models.html", ".impair-formula-contrast-cell.m-see", 0, None),
    ("S-see-solid-cf09", "cf-2018" + V + "ch09-combined.html", "aside.sec", 0, None),
    ("S-master-timeline-repeat", "ias-16" + V + "master-concept-map.html", ".ch04-reval", 0, 360),
    ("S-red-stops-cf-index", "cf-2018/draft-v1-linked/index.html", "#conceptMap", 0, 700),
]

PAD = 12


def main(only=None):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark",
                           device_scale_factor=1).new_page()
        cur = None
        for name, f, sel, nth, maxh in CROPS:
            if only and only not in name:
                continue
            if f != cur:
                pg.goto(BASE + f, wait_until="networkidle")
                pg.add_style_tag(content="html{background:var(--bg,#12151a)!important}"
                                         ".site-header,header.site,.topbar{display:none!important}")
                pg.wait_for_timeout(400)
                cur = f
            loc = pg.locator(sel)
            if loc.count() <= nth:
                print("MISSING", name, sel, file=sys.stderr)
                continue
            el = loc.nth(nth)
            bb = pg.evaluate("e=>{const r=e.getBoundingClientRect();return [r.left+scrollX,r.top+scrollY,r.width,r.height]}",
                             el.element_handle())
            x, y, w, h = bb
            if maxh:
                h = min(h, maxh)
            clip = {"x": max(0, x - PAD), "y": max(0, y - PAD), "width": min(1280, w + 2 * PAD), "height": h + 2 * PAD}
            pg.screenshot(path=os.path.join(OUT, name + ".png"), clip=clip, full_page=True)
            print(name, [round(v) for v in bb])
        b.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
