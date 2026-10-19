"""Write one before/after mock page per STANDARDISE / ENHANCE item into ../mocks.

Before panes are always real crops (mocks/ba/*-before.png from before_after.py,
or evidence/*.png from crops.py). After panes are either the same element
re-rendered with the proposal CSS (mocks/ba/*-after.png) or, where CSS alone
cannot show it, a small token-only drawing that uses only wording already on
the live map. Render with: python3 tools/render_mocks.py S0  (or E0).
"""
import html
import os

from PIL import Image

KIT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MOCKS = os.path.join(KIT, "mocks")


def img(rel):
    return f'<img src="{rel}" alt="">'


def width(rel):
    return Image.open(os.path.join(MOCKS, rel)).size[0]


def pane(kind, src, body):
    label = {"before": "Before · live today", "after": "After · proposal", "ref": "Reference · live today"}[kind]
    kind = "before" if kind == "ref" else kind
    return (f'<div class="pane"><p class="pane-k {kind}">{label}<span class="pane-src">{src}</span></p>{body}</div>')


def pair(b, a, src_b, src_a, cap=""):
    """b / a: image paths relative to mocks/, or ("html", snippet) for a drawn pane."""
    def body(x):
        return x[1] if isinstance(x, tuple) else img(x)
    narrow = all(isinstance(x, str) and width(x) <= 640 for x in (b, a))
    cls = "imgs c2" if narrow else "imgs"
    out = f'<div class="{cls}">{pane("before", src_b, body(b))}{pane("after", src_a, body(a))}</div>'
    if cap:
        out += f'<p class="cap">{cap}</p>'
    return out


def ba(id_, src_b, src_a, cap=""):
    return pair(f"ba/{id_}-before.png", f"ba/{id_}-after.png", src_b, src_a, cap)


DRAW_CSS = """
.draw { display: grid; gap: var(--space-4); }
.dl { font-size: var(--t3-fs); color: var(--muted); margin: 0 0 var(--space-1); }
/* K7 timeline: cards above, leader to a ring on the axis, span caption under the axis */
.k7 { position: relative; height: 11.5rem; margin: 0 var(--space-3); }
.k7 .card { position: absolute; top: 0; width: 15rem; border: var(--stroke-1) solid var(--line); border-radius: var(--card-radius);
  background: var(--surface); padding: var(--space-1) var(--space-cell); font-size: var(--t2-fs); }
.k7 .card b { display: block; }
.k7 .card.now { border-color: var(--accent); }
.k7 .ax { position: absolute; left: 0; right: 0; top: 6.4rem; height: var(--stroke-1); background: var(--accent); }
.k7 .ax::after { content: ""; position: absolute; right: calc(-1 * var(--arrowhead)); top: 50%; transform: translateY(-50%);
  border: var(--arrowhead) solid transparent; border-left-color: var(--accent); border-right: 0; }
.k7 .rg { position: absolute; top: calc(6.4rem - .35rem); width: .75rem; height: .75rem; border-radius: 50%;
  border: var(--stroke-1) solid var(--accent); background: var(--bg); transform: translateX(-50%); }
.k7 .ld { position: absolute; width: var(--stroke-1); background: var(--accent); transform: translateX(-50%); }
.k7 .dt { position: absolute; top: calc(6.4rem - 1.5rem); transform: translateX(-50%); font-size: var(--t3-fs); font-weight: 700; white-space: nowrap; }
.k7 .sp { position: absolute; top: 7.3rem; border-top: var(--stroke-1) dashed var(--dash); padding-top: var(--space-1);
  font-size: var(--t3-fs); color: var(--muted); text-align: center; }
.k7 .sp::before, .k7 .sp::after { content: ""; position: absolute; top: calc(-1 * var(--space-1)); height: var(--space-2); border-left: var(--stroke-1) solid var(--dash); }
.k7 .sp::before { left: 0; } .k7 .sp::after { right: 0; }
.k7 .lane { position: absolute; left: 0; right: 0; height: 1.6rem; border: var(--stroke-1) solid var(--line); border-radius: var(--radius-s); }
.k7 .lane-k { position: absolute; left: var(--space-2); top: 50%; transform: translateY(-50%); font-size: var(--t3-fs); font-weight: 700; }
.k7 .dia { position: absolute; top: 50%; transform: translate(-50%, -50%); color: var(--accent); font-size: var(--t3-fs); }
.k7 .tick { position: absolute; width: 0; border-left: var(--stroke-1) dotted var(--line); transform: translateX(-50%); }
/* K8 / K9 */
.k8 { display: grid; align-items: center; gap: var(--space-cell); }
.k8 .cell { min-height: 3rem; display: flex; align-items: center; gap: var(--space-1); }
.k9 { display: grid; grid-template-columns: 1.5rem minmax(0, 1fr); gap: var(--space-1) var(--space-cell); max-width: 36rem; align-items: center; }
.k9 .op { min-width: 0; }
.k9 .rule1, .k9 .rule2 { grid-column: 2; }
/* echo bar */
.echo { display: flex; align-items: center; gap: var(--space-cell); border: var(--stroke-1) solid var(--line); border-radius: var(--card-radius);
  background: var(--surface); padding: var(--space-1) var(--space-cell); }
.echo-k { font-size: var(--t3-fs); font-weight: 700; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }
.echo-s { font-size: var(--t3-fs); border: var(--stroke-1) solid var(--line); border-radius: var(--card-radius); background: var(--bg);
  padding: var(--space-1) var(--space-cell); color: var(--ink); }
.echo-s.now { border-color: var(--accent); background: var(--surface); font-weight: 700; box-shadow: inset 0 0 0 calc(var(--stroke-1) / 2) var(--accent); }
.echo-s.later { opacity: .55; color: var(--muted); }
.echo-a { color: var(--muted); opacity: .7; font-size: var(--t3-fs); }
"""


def chip(n):
    return f'<span class="chip">{n}</span>'


# --- S4: one timeline component, two real maps -------------------------------------------
S04_AFTER = ("html", f"""<div class="draw">
<div><p class="dl">IAS 16 ch05 §5.4 <i>During use</i> — signed kit 25: rings on the axis, leaders, one span caption, no Year-end ticks</p>
<div class="k7">
  <div class="card" style="left:0"><b>Begins</b>When the asset is available for use</div>
  <div class="card" style="right:0"><b>Ceases</b>Earlier of: classified as held for sale or derecognised
    <span class="see" style="margin-top:var(--space-1)"><b>See also</b> IFRS 5</span></div>
  <span class="ld" style="left:1.5rem;top:2.6rem;height:3.5rem"></span><span class="ld" style="right:1.5rem;left:auto;transform:translateX(50%);top:4.6rem;height:1.5rem"></span>
  <span class="ax"></span><span class="rg" style="left:1.5rem"></span><span class="rg" style="left:calc(100% - 1.5rem)"></span>
  <span class="sp" style="left:1.5rem;right:1.5rem">Depreciate over useful life</span>
</div></div>
<div><p class="dl">IFRS 18 ch08 §8.1–8.2 <i>Calendar</i> — same component, four markers; the span is the map’s own §8.2 line</p>
<div class="k7" style="height:14rem">
  <span class="dt" style="left:4%">1 Jan 2026</span><span class="dt" style="left:35%;color:var(--accent)">1 Jan 2027</span>
  <span class="dt" style="left:66%">e.g. 30 Jun 2027</span><span class="dt" style="left:95%">31 Dec 2027</span>
  <span class="ax"></span>
  <span class="rg" style="left:4%"></span><span class="rg" style="left:35%;background:var(--accent)"></span><span class="rg" style="left:66%"></span><span class="rg" style="left:95%"></span>
  <span class="ld" style="left:4%;top:6.8rem;height:4.2rem"></span><span class="ld" style="left:35%;top:6.8rem;height:4.2rem"></span>
  <span class="ld" style="left:66%;top:6.8rem;height:4.2rem"></span><span class="ld" style="left:95%;top:6.8rem;height:4.2rem"></span>
  <span class="sp" style="left:4%;right:65%;top:7.3rem;white-space:normal;line-height:1.3;padding-inline:var(--space-2)">{chip("8.2")} Retrospective (IAS 8) — the comparative period is restated, so IFRS 18 data is needed from 1 Jan 2026</span>
  <div class="card" style="top:11rem;left:0;width:22%"><b>Comparative period begins</b></div>
  <div class="card now" style="top:11rem;left:25%;width:22%">{chip("8.1")} <b style="display:inline">Effective date</b></div>
  <div class="card" style="top:11rem;left:52%;width:22%"><b>First interim report</b></div>
  <div class="card" style="top:11rem;left:78%;width:22%"><b>First annual FS</b></div>
</div></div>
<p class="cap">Drawn with tokens only. Card bodies are shortened to their titles for size; on the map every line stays as it is. CF ch03 and IFRS 18 ch01 get the same component with an empty span until Johnny supplies between-words.</p>
</div>""")

# --- S7: IAS 2 master, three recipes → ledger + formula rows -------------------------------
S07_AFTER = ("html", f"""<div class="draw">
<div><p class="dl">K9 Ledger — <i>Cost of inventories</i> (compute → result last, like IAS 16 ch04 <code>.vledger</code>)</p>
<div class="k9">
  <span></span><div class="cell">{chip("3.2")} <b>Costs of purchase</b></div>
  <span class="op">+</span><div class="cell">{chip("3.3")} <b>Costs of conversion</b></div>
  <span class="op">+</span><div class="cell">{chip("3.5")} <b>Other costs</b></div>
  <span></span><div class="rule1"></div>
  <span class="op">=</span><div class="cell result"><b>Cost of inventories</b></div>
  <span></span><div class="rule2"></div>
</div></div>
<div><p class="dl">K8 Formula row — <i>Measure NRV</i> (define → result first)</p>
<div class="k8" style="grid-template-columns:1fr auto 1fr auto 1fr auto 1fr">
  <div class="cell result">{chip("4.1")} <b>Net realisable value</b></div><span class="op">=</span>
  <div class="cell"><b>Estimated selling price</b></div><span class="op">−</span>
  <div class="cell"><b>Estimated costs of completion</b></div><span class="op">−</span>
  <div class="cell"><b>Estimated costs necessary to make the sale</b></div>
</div></div>
<div><p class="dl">K8 Formula row — <i>Inventories sold …</i> (compute → result last); same cell recipe as the NRV row</p>
<div class="k8" style="grid-template-columns:1fr auto 1fr auto 1fr auto 1fr">
  <div class="cell">{chip("5.1")} <b>Inventories sold</b></div><span class="op">+</span>
  <div class="cell">{chip("5.2")} <b>Write-downs to NRV and losses</b></div><span class="op">−</span>
  <div class="cell">{chip("5.3")} <b>Reversals of write-downs</b></div><span class="op">=</span>
  <div class="cell result">{chip("6.4")} <b>Recognised as an expense</b></div>
</div></div>
<p class="cap">Titles, chips and operators are the live ones; bodies are left off for size and stay unchanged on the map. “Net realisable value” is the live arm head (4.1) above <code>.m-formula</code>. One term recipe (Cell + T2 title + chip), one operator class.</p>
</div>""")

# --- S12: IAS 16 master, one axis + event lanes ------------------------------------------
S12_AFTER = ("html", f"""<div class="draw">
<div><p class="dl">IAS 16 master — the <i>During use</i> axis drawn once; revaluation and impairment become event lanes under it</p>
<div class="railrow" style="align-items:start">
  <div class="rail">{chip("5.4")}<span>During use</span></div>
  <div class="k7" style="height:14.5rem;margin:0">
    <div class="card" style="left:0"><b>Begins</b>When the asset is available for use</div>
    <div class="card" style="right:0"><b>Ceases</b>Earlier of: classified as held for sale or derecognised
      <span class="see" style="margin-top:var(--space-1)"><b>See also</b> IFRS 5</span></div>
    <span class="ld" style="left:1.5rem;top:2.6rem;height:3.5rem"></span><span class="ld" style="left:calc(100% - 1.5rem);top:4.6rem;height:1.5rem"></span>
    <span class="ax"></span><span class="rg" style="left:1.5rem"></span><span class="rg" style="left:calc(100% - 1.5rem)"></span>
    <span class="sp" style="left:1.5rem;right:1.5rem">Depreciate over useful life</span>
    <span class="tick" style="left:35%;top:6.8rem;height:2.9rem"></span><span class="tick" style="left:70%;top:6.8rem;height:2.9rem"></span>
    <span class="tick" style="left:50%;top:6.8rem;height:5.1rem"></span>
    <div class="lane" style="top:9.6rem"><span class="lane-k">◆ Revaluation date</span>
      <span class="dia" style="left:35%">◆</span><span class="dia" style="left:70%">◆</span></div>
    <div class="lane" style="top:11.8rem"><span class="lane-k">◆ Impairment date</span><span class="dia" style="left:50%">◆</span></div>
  </div>
</div></div>
<p class="cap">Lanes and diamond positions are the live ones (<code>.lc-band-rev</code> left 35% / 70%, <code>.lc-band-imp</code> left 50%). Each lane keeps its own plate below (<i>Revaluation</i>, <i>Impairment</i>); only the repeated axis goes. Needs the splice tool (<code>tools/build-map-includes.py</code>) to stop copying <code>ch05-axis</code> — direction only.</p>
</div>""")

# --- E5: echo bar on IAS 2 chapters -------------------------------------------------------
E05_AFTER = ("html", """<div class="draw">
<div><p class="dl">IAS 2 ch03 — the IAS 16 echo bar recipe (<code>nav.master-echo</code>), steps = the six IAS 2 chapter titles</p>
<div class="echo"><span class="echo-k">Master path</span>
  <span class="echo-s">Scope <span class="echo-a">→</span></span><span class="echo-s">Recognition <span class="echo-a">→</span></span>
  <span class="echo-s now">Initial measurement <span class="echo-a">→</span></span><span class="echo-s later">Subsequent measurement <span class="echo-a">→</span></span>
  <span class="echo-s later">Derecognition <span class="echo-a">→</span></span><span class="echo-s later">Disclosure</span></div></div>
<p class="cap">Step names are the IAS 2 chapter titles (<code>ias-2/draft-v1-linked/ch01–ch06.html</code> &lt;title&gt;). The kicker “Master path” is IAS 16’s label; reusing it on IAS 2 is new chrome text, so it needs Johnny’s OK.</p>
</div>""")

PAGES = {
    "S01-rail-chrome": dict(
        t="S1 · Group label on the left: one rail chrome",
        why="Rule 2 — same-level left rails align in style. Applies the signed dep-v2 unify-A to the live map.",
        body=[ba("S01-ias16-ch05", "IAS 16 ch05 §5.4 <code>.lc-head-k</code> (unboxed) next to §5.1 <code>.inner-rail</code>",
                 "§5.4 takes the computed <code>.inner-rail</code> chrome of §5.1 on the same plate"),
              ba("S01-cf-ch07-kicker", "CF ch07 <code>.pd-kicker</code> — 10 px / 700 + 0.8 px tracking",
                 "one kicker recipe: 12 px / 700 / uppercase / muted (= <code>.ou-label</code>, <code>.pa-label</code>)")]),
    "S02-and-connector": dict(
        t="S2 · “All must hold”: AND pill, not +",
        why="Rule 4 — an explicit AND when all conditions must hold; “+” stays for arithmetic. Signed MF §9 pill.",
        body=[ba("S02-ias16-ch01", "IAS 16 ch01 §1.1 <code>span.crit-op</code> “+”",
                 "AND pill + junction under the row (the Yes arm already leaves the box)"),
              ba("S02-ias2-ch02", "IAS 2 ch02 §2.0 <code>span.or</code> “and”", "AND pill; question text stays as the junction label"),
              ba("S02-cf-ch02", "CF ch02 §2.5 <code>.qc-op</code> “+”", "AND pill; kicker “both required” already says it")]),
    "S03-yes-no-label": dict(
        t="S3 · Yes / No on arrows: one label",
        why="Rule 6 — same logic, same format. Six live styles become one: T3 700 muted, first letter capital, no border.",
        body=[ba("S03-ias2-ch01", "IAS 2 ch01 <code>.stem-label</code> “yes / no”", "“Yes / No” via <code>::first-letter</code>; source text unchanged"),
              ba("S03-ifrs18-ch03", "IFRS 18 ch03 <code>.pc-stem-label</code> CSS UPPERCASE", "uppercase dropped; first letter capital"),
              ba("S03-cf-ch09", "CF ch09 <code>.mid</code> outlined pill", "pill border dropped; same label as every other fork")]),
    "S04-timeline": dict(
        t="S4 · Timeline: one shared component (kit 25)",
        why="Rules 5 and 6 — every marker joined to its label, one note for what happens between markers, same markup on all 7 maps.",
        body=[pair("../evidence/B15-time-axis.png", S04_AFTER, "IAS 16 ch05 §5.4 <code>.lc-head</code> + 4 “Year-end” ticks", "kit 25 component"),
              f'<div class="imgs c2">{pane("before", "CF ch03 §3.2 <code>.re-axis</code> — labels under rings, no leader", img("../evidence/C-timeline-cf03.png"))}'
              f'{pane("before", "IFRS 18 ch08 <code>ol.tr-tl</code> — dates above, cards below, the only span", img("../evidence/B16-time-span.png"))}</div>']),
    "S05-see-also": dict(
        t="S5 · See-also: one dashed pointer",
        why="Shared grammar (<code>_shared/visuals.css</code> header): dashed = see-also only. A reader tells “go elsewhere” from “this is the rule” at a glance.",
        body=[ba("S05-cf-ch09", "CF ch09 <code>aside.sec</code> — solid frame", "dashed <code>--see</code> frame, “See also” in <code>--see</code>"),
              ba("S05-cf-ch06", "CF ch06 <code>.mx-see</code> — dashed grey <code>--dash</code>", "dashed <code>--see</code>"),
              ba("S05-ias16-ch04", "IAS 16 ch04 <code>.impair-comp.m-see</code> — rule text in a dashed box",
                 "content box becomes a plain solid Cell; the inner 6.6 pointer stays dashed")]),
    "S06-strip-scope": dict(
        t="S6 · Thick-left strip: financial-statement lines only",
        why="One meaning per paint. Once the bar also means “trap”, it stops meaning “line on the statement”.",
        body=[ba("S06-ifrs18-ch02", "IFRS 18 ch02 <code>.pa-trap</code> — strip on a trap", "full 1 px <code>--warn</code> border (Tone warn)"),
              ba("S06-ifrs18-ch04", "IFRS 18 ch04 §4.2 <code>.ts-trap</code> — strip on an exception", "full 1 px <code>--warn</code> border")]),
    "S07-formula": dict(
        t="S7 · Formula: one row recipe, one ledger recipe",
        why="Rule 6. The IAS 2 master alone uses three term recipes and three operator classes for one job.",
        body=[f'<div class="imgs c2">{pane("before", "IAS 2 master <code>.m-sum</code> — vertical, + at left", img("ba/S07-ias2-master-sum-before.png"))}'
              f'{pane("before", "IAS 2 master <code>.m-formula</code> — <code>a.m-term</code>, 11 px, no chip", img("ba/S07-ias2-master-nrv-before.png"))}</div>'
              f'<div class="imgs">{pane("before", "IAS 2 master <code>.m-eqn</code> — chip + title + body, 12 px", img("ba/S07-ias2-master-eqn-before.png"))}</div>',
              f'<div class="imgs">{pane("after", "K9 ledger + K8 formula rows, same cell recipe", S07_AFTER[1])}</div>']),
    "S08-matrix": dict(
        t="S8 · Matrix: one table recipe",
        why="Grammar skill §4 — an all-boxed grid adds a border level for no meaning; ruled rows read straight across.",
        body=[ba("S08-cf-ch06", "CF ch06 §6.4 <code>.mx-grid</code> — every cell boxed, UPPERCASE stub",
                 "one frame, hairline rules, stub on <code>--band</code> in sentence case")]),
    "S10-solid-bg": dict(
        t="S10 · Graph paper off (rule 9)",
        why="Rule 9 and signed GB-SOLID / MF §9 “kit 2 STRUCK”. One shared rule in <code>map-box.css</code> L22–37; no chapter edits.",
        body=[ba("S10-ias2-master", "IAS 2 master <code>.m-l0</code> gradient", "<code>background: var(--bg)</code>"),
              ba("S10-cf-index", "CF index <code>#conceptMap.m-l0</code> gradient", "<code>background: var(--bg)</code>")]),
    "S11-cite-chip": dict(
        t="S11 · Paragraph cite chips off IAS 16 maps (rule 8)",
        why="Rule 8 — no paragraph-number pills on maps. Finishes the 2026-10-03 strip pass, which skipped IAS 16.",
        body=[ba("S11-ias16-ch04", "IAS 16 ch04 <code>.impair-routes</code> — 4 <code>.cite</code> chips",
                 "chip markup removed (shown here as <code>.cite-run{display:none}</code>); wording unchanged",
                 "Before removal, each reference is checked against the chapter body text — that check is content and is listed for Johnny.")]),
    "S12-draw-once": dict(
        t="S12 · Draw the During-use axis once (rule 7)",
        why="Rule 7 — don’t restate content already on the same map. The master shows the same Begins / Ceases axis three times.",
        body=[pair("../evidence/S-master-timeline-repeat.png", S12_AFTER,
                   "IAS 16 master <code>.ch04-reval</code> — 2nd copy of the axis (3rd is in <code>.ch04-impair</code>)", "one axis + event lanes")]),
    "S13-stop-and-depth": dict(
        t="S13 · One red stop per board; max two box levels",
        why="Grammar skill §3 (≤ 1 red stop, justify a second) and §4 (2 bordered levels, a 3rd only for formula / ledger / see-also).",
        body=[ba("S13-cf-index", "CF index — 2 red <code>.leaf-no.m-stop</code>", "<i>Not that element</i> muted; <i>Do not recognise</i> keeps red (Johnny to confirm)"),
              ba("S13-depth-ias16-ch06", "IAS 16 ch06 <i>Partial disposal</i> — 5 bordered levels",
                 "<code>.partial-nest</code> frame and <code>.item-rows</code> boxes dropped → 3 levels")]),
    "E01-kicker-to-rail": dict(
        t="E1 · PROPOSAL — stacked groups get a left rail, not a top kicker",
        why="Rules 2–3: a group label on the left, that group’s content on a grid to its right; all rails on one track.",
        body=[ba("E01-cf-ch01", "CF ch01 — three <code>.ou-sec</code> groups, each with a top <code>.ou-label</code> kicker",
                 "<code>.ou-label</code> as a rail on the shared track; content unchanged in column 2")]),
    "E02-and-of-or": dict(
        t="E2 · PROPOSAL — show “Asset AND (one of three)” on IAS 2 ch01 §1.1",
        why="Rule 4: the definition is an AND of an OR-set; today a lone “+” sits between them and the OR-set has no bracket.",
        body=[ba("E02-ias2-ch01", "IAS 2 ch01 §1.1 <code>div.st-plus</code> “+” over <code>div.classes</code>",
                 "AND pill + an open bracket over the OR-set; <code>span.or</code> as small OR pills")]),
    "E03-exclusions-once": dict(
        t="E3 · PROPOSAL — each IAS 16 exclusion shown once (ch01 §1.3)",
        why="Rule 7: the four exclusions are listed in the question and again as cards; the cards already carry each See-also.",
        body=[ba("E03-ias16-ch01", "IAS 16 ch01 §1.3 <code>.q .item-rows</code> + <code>.carve-set</code> (same four items)",
                 "question keeps its title; the four live on the cards only",
                 "Touches what is shown (the question’s list goes), so it is a proposal, not a formatting fix.")]),
    "E04-shared-row-grid": dict(
        t="E4 · PROPOSAL — peers share one row grid (reads as a matrix, no new words)",
        why="Rule 1: prefer pivot / matrix. With CSS subgrid the head, rule and example lines line up across peers.",
        body=[ba("E04-ifrs18-ch05", "IFRS 18 ch05 §5.1 <code>.oe-options</code> — three free-height <code>.oe-opt</code> cards",
                 "<code>grid-template-rows: subgrid</code> — rows align, hairline between rows")]),
    "E05-echo-bar-ias2": dict(
        t="E5 · PROPOSAL — the echo bar on IAS 2 chapters",
        why="Rule 6: IAS 2 chapters walk the same life cycle as IAS 16, which already shows the reader where they are.",
        body=[pair("ba/E05-ias2-ch03-before.png", E05_AFTER, "IAS 2 ch03 top — no path marker", "IAS 16 echo recipe"),
              f'<div class="imgs">{pane("ref", "IAS 16 ch05 <code>nav.master-echo</code> — the recipe being reused", img("../evidence/B19-echo-bar.png"))}</div>']),
}


def main():
    for name, p in PAGES.items():
        doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="color-scheme" content="dark">
<title>{html.escape(p['t'])}</title><link rel="stylesheet" href="kit.css"><style>{DRAW_CSS}</style></head>
<body>
<p class="ba-h">{p['t']}</p>
<p class="ba-why">{p['why']}</p>
<div class="ba">{''.join(p['body'])}</div>
</body></html>
"""
        with open(os.path.join(MOCKS, name + ".html"), "w") as f:
            f.write(doc)
        print(name)


if __name__ == "__main__":
    main()
