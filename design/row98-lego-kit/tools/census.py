"""Brick census for every rendered concept map (read-only).

Serves nothing and edits nothing: it loads each map from a local static
server (python3 -m http.server 8765 in the repo root), dark theme, 1280 wide,
and counts how often each LEGO brick appears.  Class-based bricks are matched
by the regexes in BRICKS; surface, strip, tone and graph-paper checks use
computed style so they do not depend on per-chapter class names.

Output: census.json next to this file (per map, per brick: count + the first
instance's bounding box, used for evidence crops).
"""
import glob
import json
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = os.environ.get("MAP_BASE", "http://localhost:8765/")
CHROME = os.environ.get("CHROME", "/usr/local/bin/google-chrome")
OUT = os.path.join(os.path.dirname(__file__), "census.json")

# brick id -> (include regex on class tokens, exclude regex, optional allowed tag names)
BRICKS = {
    "title": (r"(^|-)(title|head)$|^frame-title$",
              r"^(lc-|lens|rev-|cap-m|tr-mx|pa-mx|mx-row|mx-head|wn-tl-head|tr-head|oe-leaf-head|zone-head|hub-head|qc-tier-title)"),
    "section-chip": (r"^(fb-num|sec|sec-sm)$", None, ["A", "SPAN"]),
    "kicker": (r"(-label|-kicker|^tier-label|-tier-title|^zone-head|^hub-head)$",
               r"^(see-label|arm-label|stem-label|.*-stem-label|.*-link-label|pack-flow-label|exit-label|"
               r"st-h-label|pc-yes-label|mx-dead-label|cap-m-corner-label|re-fork-label|m-disc-label|"
               r"lc-tick-lab|lc-key.*|facet-label|axis-name.*)$"),
    "tag": (r"(-tag|^src|^differ-note|^differ-tag|^ou-sub|^lane-tag)$", None),
    "see-also": (r"^(see|see-also-strip|re-see|wn-see|tr-see|pd-see|mx-see|cap-see|ofs-see|foot-see|pack-see-not)$", None),
    "see-also-zone": (r"^sec$", None, ["ASIDE"]),
    "cite-chip": (r"^cite$", None),
    "rail": (r"^(inner-rail|qc-rail|pc-mba-rail|cost-rail|lc-head-k)$", None),
    "rail-link": (r"^rail-link$", None),
    "flow-arrow": (r"^(m-flow|m-visit|harm|varm|stem|stem-shaft|st-h-shaft|m-shaft|m-stem|pc-stem|gt-stem|ofs-stem|"
                   r"oe-link|rc-link|qc-link|ou-link|cap-link|re-stem|org-fork-stem|mx-stem|pd-stem|lc-arrow|"
                   r"impair-ca-arrow|formula-stem|hstem|vstem|vline|step-link|gt-exit)$", None),
    "flow-label": (r"^(arm-label|stem-label|m-stem-label|pc-stem-label|re-stem-label|mx-stem-label|ofs-stem-label|"
                   r"qc-link-label|rc-link-label|oe-link-label|mid|pc-yes-label|st-h-label|re-fork-label|mx-dead-label|"
                   r"pack-flow-label|exit-label|gt-ans)$", None),
    "link-bar": (r"^(qc-bar|el-bar|rc-bar|mx-bar|mx-span|wn-span-bar|pa-rule|both-bar|bar|span-bar|"
                 r"pc-bracket|ts-attach|ou-lens-foot|ou-direct|consume-bar)$", None),
    "operator": (r"^(crit-op|vop|mini-op|op-eq|op-p1|op-p2|def-op|differ-op|cost-op|exp-op|m-eq-op|m-minus|m-plus|"
                 r"m-op|nrv-minus|eq|op|el-op|qc-op|rc-op|re-dual-and|st-plus|or|fb-op|when-or)$", None),
    "rule-line": (r"^(vrule|vrule-2|ts-sub|m-rule|mini-pnl-tick)$", None),
    "time-axis": (r"^(lc-axis|re-axis|wn-tl|tr-tl|ready-axis)$", None),
    "time-marker": (r"^(lc-ring|lc-dia|lc-tick|re-tick|wn-tl-node|tr-node|axis-mark|lc-end)$", None),
    "time-span": (r"^(tr-span)$", None),
    "echo-bar": (r"^(master-echo)$", None),
    "hand-off": (r"^(pack-flow|handoff|pack-exit)$", None),
    "glyph": (r"^(method-chart|glyph|party-cast|org-chart)$", None),
    "matrix": (r"^(mx-grid|cap-matrix|pa-matrix|tr-mx|lens-heads|rev-table|recon-cols)$", None),
    "m-see-paint": (r"^m-see$", None),
}

JS = r"""
([bricks, scopeSel]) => {
  const scope = scopeSel ? document.querySelector(scopeSel) : (document.querySelector('body.embed .page') || document.body);
  const all = [scope, ...scope.querySelectorAll('*')];
  const rx = {};
  for (const [k, [inc, exc, tags]] of Object.entries(bricks)) rx[k] = [new RegExp(inc), exc ? new RegExp(exc) : null, tags || null];
  const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const box = el => { const r = el.getBoundingClientRect();
    return [Math.round(r.left + scrollX), Math.round(r.top + scrollY), Math.round(r.width), Math.round(r.height)]; };
  const out = {};
  for (const k of Object.keys(rx)) out[k] = {count: 0, first: null, classes: {}};
  for (const el of all) {
    if (!(el instanceof Element) || !vis(el)) continue;
    const cls = [...el.classList];
    for (const [k, [inc, exc, tags]] of Object.entries(rx)) {
      if (tags && !tags.includes(el.tagName)) continue;
      const hit = cls.filter(c => inc.test(c) && !(exc && exc.test(c)));
      if (!hit.length) continue;
      out[k].count++;
      for (const c of hit) out[k].classes[c] = (out[k].classes[c] || 0) + 1;
      if (!out[k].first) out[k].first = {box: box(el), cls: el.className.baseVal ?? el.className};
    }
  }
  // computed-style bricks
  const px = v => parseFloat(v) || 0;
  const rgb = v => (v.match(/\d+(\.\d+)?/g) || []).slice(0, 3).map(Number);
  const boxes = []; const strips = []; const tones = {};
  const toneOf = c => ({'201,122,122': 'stop', '201,163,90': 'warn', '123,163,201': 'accent', '168,148,196': 'see',
                        '77,184,165': 'cat-investing', '212,137,94': 'mpm', '232,234,237': 'ink'})[rgb(c).join(',')] || null;
  for (const el of all) {
    if (!(el instanceof HTMLElement) || !vis(el)) continue;
    const s = getComputedStyle(el);
    const bw = ['Top', 'Right', 'Bottom', 'Left'].map(sd => s['border' + sd + 'Style'] !== 'none' ? px(s['border' + sd + 'Width']) : 0);
    const r = el.getBoundingClientRect();
    const pill = px(s.borderTopLeftRadius) >= r.height / 2 - 1;
    if (bw.every(w => w >= 1) && r.width > 12 && r.height > 12 && !pill) {
      boxes.push(el);
      const t = toneOf(s.borderTopColor); if (t) { tones[t] = (tones[t] || 0) + 1; }
    }
    if (bw[3] >= 3 && bw[3] > bw[1] + 1 && r.height > 8) strips.push({cls: el.className, w: bw[3], box: box(el), text: (el.innerText || '').trim().slice(0, 50)});
  }
  const depth = el => { let d = 0; let p = el.parentElement; while (p && p !== scope.parentElement) { if (boxes.includes(p)) d++; p = p.parentElement; } return d; };
  const levels = {}; let maxd = 0; let deepest = null;
  for (const b of boxes) { const d = depth(b); levels[d] = (levels[d] || 0) + 1; if (d > maxd) { maxd = d; deepest = {cls: b.className, box: box(b)}; } }
  // graph paper on the board or scope
  let grid = false;
  for (const el of [scope, ...scope.querySelectorAll('.m-l0, .board-l0-div')]) {
    const bi = getComputedStyle(el).backgroundImage; if (bi && bi.includes('gradient')) grid = true;
  }
  // paragraph references in visible text
  const paraRx = /\b(para|paras|paragraph)\s*\d|\bIN\d{1,2}\b|\bBC\d+|\bD16\(|\bApp(endix)? [A-D]\b/;
  const paras = []; const tw = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT);
  while (tw.nextNode()) { const t = tw.currentNode.textContent.trim(); const p = tw.currentNode.parentElement;
    if (t && paraRx.test(t) && vis(p)) paras.push({text: t.slice(0, 60), cls: p.className}); }
  // near-invisible text: luminance of text colour < 0.25 in dark theme
  const lum = c => { const [r, g, b] = rgb(c).map(v => v / 255); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
  const dark = []; const tw2 = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT);
  while (tw2.nextNode()) { const t = tw2.currentNode.textContent.trim(); const p = tw2.currentNode.parentElement;
    if (t.length > 2 && vis(p) && lum(getComputedStyle(p).color) < 0.25) dark.push({text: t.slice(0, 60), cls: p.className, color: getComputedStyle(p).color, box: box(p)}); }
  const grids = [...scope.querySelectorAll('*')].filter(e => vis(e) && getComputedStyle(e).display.includes('grid')).length;
  const sb = box(scope);
  return {bricks: out, boxes: boxes.length, box_levels: levels, max_box_depth: maxd, deepest, strips, tones,
          graph_paper: grid, para_text: paras, dark_text: dark, grid_containers: grids, scope_box: sb};
}
"""


def pages():
    os.chdir(ROOT)
    out = [(f, None) for f in sorted(glob.glob("*/draft-v1-linked/visuals/*.html"))]
    out += [("cf-2018/draft-v1-linked/index.html", "#conceptMap"),
            ("ifrs-18/draft-v1-linked/index.html", "#conceptMap")]
    return out


def main():
    res = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark")
        pg = ctx.new_page()
        for f, sel in pages():
            pg.goto(BASE + f, wait_until="networkidle")
            pg.wait_for_timeout(400)
            res[f] = pg.evaluate(JS, [BRICKS, sel])
            print(f, file=sys.stderr)
        b.close()
    with open(OUT, "w") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
