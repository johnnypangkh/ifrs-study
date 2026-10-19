"""Flag objects (text, chips, inner boxes) that sit flush against a bordered parent's inner edge.

For every element with a visible border, measure the gap from its inner left/top edge to each
visible text run or bordered descendant that starts at that edge. Gap < MIN_GAP px = flush.
Only the part each crop shows is checked (job maxh).
Usage: python3 tools/flush_check.py [filter]  (needs the local server on :8765)
"""
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import before_after as ba  # noqa: E402

MIN_GAP = 4
MOCKS = "http://localhost:8765/design/row98-lego-kit/mocks/"

SCAN = r"""([root, minGap, maxH]) => {
  const scope = root ? document.querySelector(root) : document.body;
  if (!scope) return ['MISSING ' + root];
  const cut = maxH ? scope.getBoundingClientRect().top + maxH : Infinity;
  const vis = e => { const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
    return cs.visibility !== 'hidden' && cs.display !== 'none' && r.width > 0 && r.height > 0; };
  const boxed = e => { const cs = getComputedStyle(e);
    return parseFloat(cs.borderLeftWidth) > 0 && cs.borderLeftStyle !== 'none' && cs.borderLeftStyle !== 'hidden'
        && parseFloat(cs.borderTopWidth) > 0 && cs.borderTopStyle !== 'none'; };
  const name = e => e.tagName.toLowerCase() + (e.classList.length ? '.' + [...e.classList].join('.') : '');
  const out = [];
  for (const box of [scope, ...scope.querySelectorAll('*')]) {
    if (!vis(box) || !boxed(box)) continue;
    const br = box.getBoundingClientRect(); const cs = getComputedStyle(box);
    if (br.width < 24 || br.height < 14 || br.top > cut) continue;
    // A pill (chip, tag, see-also pill) centres its own label; only boxes with corners are cells.
    if (parseFloat(cs.borderTopLeftRadius) >= br.height / 2 - 1) continue;
    const inL = br.left + parseFloat(cs.borderLeftWidth), inT = br.top + parseFloat(cs.borderTopWidth);
    const items = [];
    const w = document.createTreeWalker(box, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) {
      if (!n.textContent.trim() || !vis(n.parentElement)) continue;
      const r = document.createRange(); r.selectNodeContents(n);
      for (const q of r.getClientRects()) if (q.width > 0) items.push([q, n.parentElement, '"' + n.textContent.trim().slice(0, 28) + '"']);
    }
    for (const d of box.querySelectorAll('*')) if (vis(d) && boxed(d)) items.push([d.getBoundingClientRect(), d, '']);
    for (const [q, el, txt] of items) {
      let a = el, inner = false;
      while (a && a !== box) { if (a !== el && boxed(a) && vis(a)) { inner = true; break; } a = a.parentElement; }
      if (inner || q.top > cut) continue;
      // Emoji and tall glyphs can paint above their line box; measure from the element box instead.
      const er = el.getBoundingClientRect(), ec = getComputedStyle(el);
      const own = el === box ? [parseFloat(ec.borderLeftWidth) + parseFloat(ec.paddingLeft), parseFloat(ec.borderTopWidth) + parseFloat(ec.paddingTop)] : [0, 0];
      const gl = Math.max(q.left, er.left + own[0]) - inL, gt = Math.max(q.top, er.top + own[1]) - inT;
      if (gl >= -0.5 && gl < minGap) out.push(`L ${gl.toFixed(1)}px  ${name(box)} > ${name(el)} ${txt}`);
      if (gt >= -0.5 && gt < minGap && gl < 40) out.push(`T ${gt.toFixed(1)}px  ${name(box)} > ${name(el)} ${txt}`);
    }
  }
  return [...new Set(out)];
}"""


def report(label, hits):
    print(f"== {label}: {len(hits)} flush")
    for h in hits:
        print("   ", h)


def main(only=None):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=ba.CHROME, args=["--no-sandbox"])
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark", device_scale_factor=1)
        for f in ("lego-sheet.html", "lego-combos.html"):
            if only and only not in f:
                continue
            pg = ctx.new_page()
            pg.goto(MOCKS + f, wait_until="networkidle")
            report(f, pg.evaluate(SCAN, [None, MIN_GAP, None]))
            pg.close()
        for j in ba.JOBS:
            if j["css"] is None or (only and only not in j["id"]):
                continue
            pg = ctx.new_page()
            pg.goto(ba.BASE + j["file"], wait_until="networkidle")
            if j.get("pre"):
                pg.evaluate(*j["pre"]) if j["pre"][1] is not None else pg.evaluate(j["pre"][0])
            pg.add_style_tag(content=j["css"])
            if j.get("js"):
                fn, arg = j["js"]
                pg.evaluate(fn, arg) if arg is not None else pg.evaluate(fn)
            pg.wait_for_timeout(300)
            report(j["id"] + " AFTER", pg.evaluate(SCAN, [j["sel"], MIN_GAP, j["maxh"]]))
            pg.close()
        b.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
