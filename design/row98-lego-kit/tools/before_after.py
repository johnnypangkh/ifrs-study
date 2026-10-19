"""Before / after crops for STANDARDISE and ENHANCE proposals.

For each job: open the live map (dark, 1280), crop the element as it is today
("before"), inject the proposal CSS (and, where noted, a small DOM-free JS
style copy), crop the same element again ("after"). Wording is never edited:
the after CSS only changes borders, fills, type and layout. Pseudo-element
`content` is used only for the signed AND pill (MF §9), which replaces a
glyph, not IFRS text.

Output: ../mocks/ba/<id>-before.png and <id>-after.png.
"""
import os
import sys

from playwright.sync_api import sync_playwright

BASE = os.environ.get("MAP_BASE", "http://localhost:8765/")
CHROME = os.environ.get("CHROME", "/usr/local/bin/google-chrome")
OUT = os.path.join(os.path.dirname(__file__), "..", "mocks", "ba")
PAD = 12
BG = "html{background:var(--bg,#12151a)!important}"

V = "/draft-v1-linked/visuals/"
I16, I2, CF, R18 = "ias-16" + V, "ias-2" + V, "cf-2018" + V, "ifrs-18" + V

# Signed MF §9 AND pill: T3, 700, --accent text, 1px --line, pill radius, knocked out on --bg.
AND_PILL = ("content:'AND';display:inline-block;font-size:var(--t3-fs);font-weight:700;line-height:1.6;"
            "letter-spacing:.06em;color:var(--accent);border:var(--stroke-1) solid var(--line);"
            "border-radius:var(--radius-pill);padding:0 var(--space-2);background:var(--bg);")
# S3 arm label: T3, 700, --muted, no border, knocked out on --bg, first letter capital.
LABEL = ("font-size:var(--t3-fs)!important;font-weight:700!important;color:var(--muted)!important;"
         "text-transform:none!important;letter-spacing:0!important;border:0!important;background:var(--bg)!important;")
FIRST_CAP = "::first-letter{text-transform:uppercase}"

# Copies the computed chrome of a live .inner-rail onto the target, so the
# "after" is the existing signed rail look rather than a new invention.
COPY_RAIL = """(t) => {
  const src = document.querySelector(t.src); const s = getComputedStyle(src);
  for (const el of document.querySelectorAll(t.dst)) {
    for (const k of ['borderTopWidth','borderRightWidth','borderBottomWidth','borderLeftWidth',
                     'borderTopStyle','borderRightStyle','borderBottomStyle','borderLeftStyle',
                     'borderTopColor','borderRightColor','borderBottomColor','borderLeftColor',
                     'borderRadius','backgroundColor','paddingTop','paddingRight','paddingBottom','paddingLeft',
                     'fontSize','fontWeight','display','flexDirection','alignItems','justifyContent','gap'])
      el.style.setProperty(k.replace(/[A-Z]/g, m => '-' + m.toLowerCase()), s[k], 'important');
  }
}"""

# Marks the lowest common ancestor of all matches so the crop holds every one.
MARK_LCA = """(sel) => {
  const els = [...document.querySelectorAll(sel)]; let a = els[0];
  while (a && !els.every(e => a.contains(e))) a = a.parentElement;
  a.setAttribute('data-ba', 'lca');
}"""

JOBS = [
    # S1 rail chrome: IAS 16 ch05 §5.4 "During use" gets the .inner-rail chrome of §5.1 on the same plate.
    dict(id="S01-ias16-ch05", file=I16 + "ch05-depreciation.html", sel=".ch05-dep > .inner-board", maxh=430,
         css=".ppe .lc-top > .lc-head-k:not(.lc-band-k){align-self:stretch;align-items:flex-start}",
         js=(COPY_RAIL, {"src": ".cap .inner-rail", "dst": ".lc-top > .lc-head-k:not(.lc-band-k)"})),
    # S1(c) kicker recipe: CF ch07 .pd-kicker onto the .ou-label/.pa-label recipe (12px / 700 / uppercase / muted).
    dict(id="S01-cf-ch07-kicker", file=CF + "ch07-presentation-disclosure.html", sel=".pd-board", maxh=240,
         css=".pd-kicker{font-size:var(--t2-band-fs)!important;font-weight:700!important;text-transform:uppercase!important;"
             "letter-spacing:.04em!important;color:var(--muted)!important}"),
    # S2 AND connector.
    dict(id="S02-ias16-ch01", file=I16 + "ch01-scope.html", sel=".fork-ppe .q", maxh=None,
         css=".ppe .crit-op{font-size:0!important;color:transparent!important}"
             ".ppe .crit-op::after{" + AND_PILL + "}"
             ".ppe .fork-ppe .criteria{position:relative;margin-bottom:var(--space-5)}"
             ".ppe .fork-ppe .criteria::after{content:'';position:absolute;left:16%;right:16%;bottom:calc(-1*var(--space-3));"
             "height:var(--space-3);border:var(--stroke-1) solid var(--line);border-top:0;"
             "border-radius:0 0 var(--radius-s) var(--radius-s)}"),
    dict(id="S02-ias2-ch02", file=I2 + "ch02-recognition.html", sel=".st-def", maxh=None,
         css=".classes .or{font-size:0!important;letter-spacing:0!important}.classes .or::after{" + AND_PILL + "}"),
    dict(id="S02-cf-ch02", file=CF + "ch02-qualitative-characteristics.html", sel=".qc-tier", nth=0, maxh=None,
         css=".qc-op{font-size:0!important}.qc-op::after{" + AND_PILL + "}"),
    # S3 one Yes/No label.
    dict(id="S03-ias2-ch01", file=I2 + "ch01-scope.html", sel=".st", maxh=460,
         css=".stem-label{" + LABEL + "}.stem-label" + FIRST_CAP),
    dict(id="S03-ifrs18-ch03", file=R18 + "ch03-classification-path.html", sel=".pc-tree", maxh=330,
         css=".pc-stem-label,.pc-yes-label{" + LABEL + "}.pc-stem-label" + FIRST_CAP + ".pc-yes-label" + FIRST_CAP),
    dict(id="S03-cf-ch09", file=CF + "ch09-combined.html", sel=".fork", maxh=None,
         css=".mid{" + LABEL + "padding:0 var(--space-1)!important}"),
    # S5 one dashed see-also; content boxes lose the dash.
    dict(id="S05-cf-ch09", file=CF + "ch09-combined.html", sel="aside.sec", maxh=None,
         css="aside.sec{border:var(--stroke-1) dashed var(--see)!important;background:transparent!important}"
             "aside.sec > *:first-child{color:var(--see)!important}"),
    dict(id="S05-ias16-ch04", file=I16 + "ch04-models.html", sel=".impair-comp", maxh=None,
         css=".ppe .impair-comp.m-see{border-style:solid!important;border-color:var(--line)!important;background:var(--surface)!important}"),
    dict(id="S05-cf-ch06", file=CF + "ch06-measurement.html", sel=".mx-see", maxh=None,
         css=".mx-see{border-color:var(--see)!important}.mx-see .see-label,.mx-see b,.mx-see strong{color:var(--see)!important}"),
    # S6 strip only on FS lines: traps become full-border warn.
    dict(id="S06-ifrs18-ch02", file=R18 + "ch02-pfs-aggregation.html", sel=".pa-trap", maxh=None,
         css=".pa-trap{border:var(--stroke-1) solid var(--warn)!important}"),
    dict(id="S06-ifrs18-ch04", file=R18 + "ch04-totals-subtotals.html", sel=".ts-trap", maxh=None,
         css=".ts-trap{border:var(--stroke-1) solid var(--warn)!important}"),
    # S8 matrix: one frame, hairline rules, cells unboxed, sentence-case stub.
    dict(id="S08-cf-ch06", file=CF + "ch06-measurement.html", sel=".mx-grid", maxh=None,
         css=".mx-grid{gap:0!important;border:var(--stroke-1) solid var(--line);border-radius:var(--card-radius);overflow:hidden}"
             ".mx-cell{border:0!important;border-radius:0!important;border-top:var(--stroke-1) solid var(--line)!important;"
             "border-left:var(--stroke-1) solid var(--line)!important;background:transparent!important}"
             ".mx-row:first-child > .mx-cell{border-top:0!important}"
             ".mx-row > .mx-cell:first-child{border-left:0!important}"
             ".mx-stub,.mx-head{background:var(--band)!important}"
             ".mx-stub{text-transform:none!important;letter-spacing:0!important;color:var(--ink)!important}"),
    # S10 solid background.
    dict(id="S10-ias2-master", file=I2 + "map-formula-board.html", sel=".m-l0", maxh=300,
         css=".m-l0{background-image:none!important;background-color:var(--bg)!important}"),
    dict(id="S10-cf-index", file="cf-2018/draft-v1-linked/index.html", sel="#conceptMap", maxh=300,
         css=".m-l0{background-image:none!important;background-color:var(--bg)!important}"),
    # S11 cite chips off (markup removal shown as display:none; wording untouched).
    dict(id="S11-ias16-ch04", file=I16 + "ch04-models.html", sel=".impair-routes", maxh=None,
         css=".cite-run{display:none!important}"),
    # S13 second red stop muted.
    dict(id="S13-cf-index", file="cf-2018/draft-v1-linked/index.html", sel="[data-ba=lca]", maxh=None,
         pre=(MARK_LCA, "#conceptMap .leaf-no.m-stop"),
         css="#conceptMap .leaf-no.m-stop:not(:last-of-type){}",
         js=("""() => { const s = document.querySelectorAll('#conceptMap .leaf-no.m-stop')[0];
                 s.style.setProperty('border', 'var(--stroke-1) solid var(--line)', 'important');
                 s.style.setProperty('background', 'transparent', 'important');
                 for (const t of s.querySelectorAll('*')) t.style.setProperty('color', 'var(--muted)', 'important'); }""", None)),
    # S13 depth: IAS 16 ch06 partial disposal is plate > inner-detail > partial-nest > peer > item-rows (5 levels).
    dict(id="S13-depth-ias16-ch06", file=I16 + "ch06-derecognition.html", sel=".inner-detail.story-special", maxh=None,
         css=".ppe .partial-nest .item-rows{border:0!important;background:transparent!important;padding-inline:0!important}"
             ".ppe .partial-nest{border-color:transparent!important;background:transparent!important;padding-inline:0!important}"),
    # Before-only crops for the hand-drawn S7 / E5 after panels.
    dict(id="S07-ias2-master-sum", file=I2 + "map-formula-board.html", sel=".m-sum", maxh=None, css=None),
    dict(id="S07-ias2-master-nrv", file=I2 + "map-formula-board.html", sel=".m-formula", maxh=None, css=None),
    dict(id="S07-ias2-master-eqn", file=I2 + "map-formula-board.html", sel=".m-eqn", maxh=None, css=None),
    dict(id="E05-ias2-ch03", file=I2 + "ch03-initial.html", sel="body", maxh=170, css=None),
    # E1 kicker becomes a left rail with the group's content on a grid to its right.
    dict(id="E01-cf-ch01", file=CF + "ch01-objective-users.html", sel=".ou-board", maxh=None,
         css=".ou-sec{display:grid!important;grid-template-columns:calc(5*var(--space-6) + var(--space-2) + var(--stroke-1)) minmax(0,1fr);"
             "column-gap:var(--space-cell);align-items:stretch}"
             ".ou-sec > .ou-label{grid-column:1;grid-row:1;align-items:flex-start;text-transform:none;letter-spacing:0;"
             "color:var(--ink);font-size:var(--t2-band-fs);border:var(--stroke-1) solid var(--line);background:var(--band);"
             "border-radius:var(--card-radius);padding:var(--space-cell)}"
             ".ou-sec > :not(.ou-label){grid-column:2;grid-row:1}"),
    # E2 AND-of-OR on IAS 2 ch01 §1.1: '+' becomes the AND pill, the OR set gets a group bracket.
    dict(id="E02-ias2-ch01", file=I2 + "ch01-scope.html", sel=".st-def", maxh=None,
         css=".st-plus{font-size:0!important}.st-plus::after{" + AND_PILL + "}"
             ".st-def .classes{border:var(--stroke-1) solid var(--line);border-bottom:0;"
             "border-radius:var(--radius-s) var(--radius-s) 0 0;padding:var(--space-cell) var(--space-cell) 0}"
             ".classes .or{font-size:var(--t3-fs)!important;text-transform:uppercase;letter-spacing:.06em!important;"
             "border:var(--stroke-1) solid var(--line);border-radius:var(--radius-pill);padding:0 var(--space-2);color:var(--formula)}"),
    # E3 show each exclusion once (IAS 16 ch01 §1.3).
    dict(id="E03-ias16-ch01", file=I16 + "ch01-scope.html", sel=".fork-excl .q, .fork-excl .harm, .fork-excl .leaf, .fork-excl .carve-set", union=True, maxh=None,
         css=".ppe .fork-excl .q .item-rows{display:none!important}"),
    # E4 peers share one row grid so they read across like a matrix.
    dict(id="E04-ifrs18-ch05", file=R18 + "ch05-operating-expenses.html", sel=".oe-options", maxh=None,
         css=".oe-options{grid-template-rows:auto auto auto;row-gap:0!important}"
             ".oe-opt{display:grid!important;grid-row:span 3;grid-template-rows:subgrid;gap:0!important}"
             ".oe-opt > *{padding-block:var(--space-1)}"
             ".oe-opt > * + *{border-top:var(--stroke-1) solid var(--line)}"),
]


UNION = """(sel) => { const rs = [...document.querySelectorAll(sel)].map(e => e.getBoundingClientRect()).filter(r => r.width);
  const l = Math.min(...rs.map(r => r.left)), t = Math.min(...rs.map(r => r.top));
  return [l + scrollX, t + scrollY, Math.max(...rs.map(r => r.right)) - l, Math.max(...rs.map(r => r.bottom)) - t]; }"""


def crop(pg, sel, nth, maxh, path, union=False):
    loc = pg.locator(sel)
    if loc.count() <= nth:
        print("MISSING", path, sel, file=sys.stderr)
        return None
    if union:
        x, y, w, h = pg.evaluate(UNION, sel)
    else:
        x, y, w, h = pg.evaluate("e=>{const r=e.getBoundingClientRect();return [r.left+scrollX,r.top+scrollY,r.width,r.height]}",
                                 loc.nth(nth).element_handle())
    if maxh:
        h = min(h, maxh)
    clip = {"x": max(0, x - PAD), "y": max(0, y - PAD), "width": min(1280 - max(0, x - PAD), w + 2 * PAD), "height": h + 2 * PAD}
    pg.screenshot(path=path, clip=clip, full_page=True)
    return [round(v) for v in (x, y, w, h)]


def main(only=None):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark", device_scale_factor=1)
        for j in JOBS:
            if only and only not in j["id"]:
                continue
            pg = ctx.new_page()
            pg.goto(BASE + j["file"], wait_until="networkidle")
            pg.add_style_tag(content=BG)
            if j.get("pre"):
                pg.evaluate(*j["pre"])
            pg.wait_for_timeout(300)
            nth = j.get("nth", 0)
            before = crop(pg, j["sel"], nth, j["maxh"], os.path.join(OUT, j["id"] + "-before.png"), j.get("union"))
            if j["css"] is None:
                print(j["id"], before)
                pg.close()
                continue
            pg.add_style_tag(content=j["css"])
            if j.get("js"):
                fn, arg = j["js"]
                pg.evaluate(fn, arg) if arg is not None else pg.evaluate(fn)
            pg.wait_for_timeout(300)
            after = crop(pg, j["sel"], nth, j["maxh"], os.path.join(OUT, j["id"] + "-after.png"), j.get("union"))
            print(j["id"], before, after)
            pg.close()
        b.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
