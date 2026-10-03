# CF 2018 draft — JP 図解 page audit (Design)

*(Site chapter numbers remapped 2026.09.27-7: old Ch2→Ch1 … old Ch10→Ch9; Overview topic retired. Official § cites unchanged.)*

**Status:** AUDIT ONLY · propose ranked opportunities · **HOLD** live redraws  
**Audience:** Johnny (PM) · Design · Content · Build  
**Date:** 2026-09-27 (Asia/Shanghai / HKT)  
**Source of truth scanned:** `draft-v1-linked/` (map + Ch1–9 bodies + `visuals/ch01–ch09` + kit CSS)  
**Twin `chapter-visuals/`:** not re-audited for parity (prefer draft-v1-linked)

---

## 1. Meta

| Lock | This audit |
|------|------------|
| Live edits under `draft-v1-linked/` HTML/CSS | **HOLD** — none performed |
| Optional densifiers A–E | **RESEARCH only** — Johnny has **not** signed a trial. Cite as “optional A–E if later unlocked,” not locked kit |
| Free circled step-rail class | **Not proposed** — gated forever unless Standards-prescribed / marked pedagogy + Design-drawn |
| Night-only · dashed rare · Content picks TYPE · no invented CF process | Respected in every recommendation |

---

## 2. Method

Compared Map + Ch1–9 **structure** (classes, plate density, chrome, legend placement) against:

1. Skill **COPY** list — nest/containment · matrix/card-grid · spectrum · waterfall · contrast · worked strip · colour-as-category · numbered steps only when § sequence · tip rails rare · same-format comparison  
2. Research pack devices (入れ子 · マトリクス · 対比 · 計算ストリップ · tip/凡例 · colour-as-category · 1-unit-1-idea)  
3. Prior gap notes in `jp-zukai-notes.md` (§3 Gaps + optional A–E)  
4. `VISUAL-TYPES.md` locked types (esp. matrix card-grid exemplar, Ch4 formula/contain, dashed rare)

**Ranking formula:** teaching-clarity gain × §-safety × effort  
Prefer: high gain · low invent-process risk · feasible with **existing kit TYPE** before optional A–E.

Observable signals used (not taste alone):

- Kit class counts per body (callouts 11–19/ch; contrast ~60–84 words/side; Ch6 matrix = `lofi` `<table>` not card-grid)  
- Visual plate patterns (stack / formula-board / flow-col / nest-parent / stmt-layout / party-cast)  
- Legend always above/beside — no plate-bottom bar  
- Map L2: Boundary nest good; Equity nest = single combined kid; Current value = flat `ul` not nested siblings

---

## 3. Ranked improvement list

### Rank 1 — Ch6 measurement-basis matrix (visual + body)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch6 visual “Measurement-basis matrix” + body current-value compare table |
| **What’s weak** | Primary teaching compare is a plain `lofi` HTML `<table>` (rows of prose). Does **not** match the locked IAS 37-style **card-grid matrix** (equal cells, spectrum cue, solid vs dashed N/A, legend). Feels like a textbook dump, not a 図解 spectrum plate. Body peer-rows for HC ∥ CV and CV siblings help, but the “matrix” label over-promises. |
| **Fix pattern** | Existing kit **TYPE: Matrix / card-grid** (`VISUAL-TYPES.md` matrix lock). Columns = bases (or family→sibling); rows = teaching criteria (applies to / entry–exit / entity vs market / cue). Optional **D footer legend bar** *if later unlocked* only when colour + solid/dashed both need decode. |
| **§-safe?** | **Yes** — Content already cites §6.x bases; no new process. Low invent risk. |
| **Effort** | **Design redraw** of Ch6 visual plate (+ light body align). Not invent-process. |

### Rank 2 — Body `.contrast-pair` density (sitewide; worst: Ch1, Ch4, Ch8, Ch1)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Body contrast pairs (sampled ~60–84 words per side; title + long prose paragraph) |
| **What’s weak** | Kit contrast exists and is used well *structurally*, but cards read as **two mini essays**, not JP 対比板 (title chip + 1–2 lines). Chrome and cite density eat the “one glance” 図解 win. Ch4 definition≠recognition and Ch1 stewardship contrasts are teaching-critical — density loss hurts most there. |
| **Fix pattern** | Existing **Contrast cards** + Content trim to ≤3 short lines/side. **OR** optional **C Dense contrast plate** *if later unlocked* (RESEARCH). Do not invent Before→After process. |
| **§-safe?** | **Yes** if Content keeps same § cites and shortens. Optional C = RESEARCH. Low invent risk. |
| **Effort** | **Quick CSS/kit polish** + **Content restructure** (copy length). C only after Johnny trial lock. |

### Rank 3 — Callout chrome pile-up → figure-first (Ch1–Ch2 heaviest)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Body callouts: Ch1≈14, Ch1≈13, Ch2≈19 (also 11–14 elsewhere) |
| **What’s weak** | Gap notes #5/#6: page still feels **callout-led**, not plate-led. Many asides are 1-line pitfalls that compete with backbone + worked strips. 図解 grammar wants tip rails **rare** at the edge — not a vertical stack of asides between every kit block. |
| **Fix pattern** | Cull/merge duplicate pitfalls into nearest contrast or worked-strip. Survivors: keep `.callout`. Ultra-short flags → optional **A Point chip** *if later unlocked* (RESEARCH). Not a second backbone. |
| **§-safe?** | **Yes** for cull/merge of existing §-cited text. Optional A = RESEARCH; chip text must stay §-grounded. Low invent risk. |
| **Effort** | **Content restructure** first; optional A = Build kit later (trial). No Design spine invent. |

### Rank 4 — Map: Current-value family + Equity L2 nest densify

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Map Measurement band (CV box with flat `ul`); Map Elements Equity `nest-parent` (single Income/Expenses kid) |
| **What’s weak** | Boundary L2 nest already teaches 組成 well. Equity nest collapses Income ∥ Expenses into **one** child — weaker than Ch4 formula board (two `.contain-cell` peers). Current value lists FV / VIU / Fulfilment as bullets inside one peer box — misses the same **outer CV + inner siblings** grammar Map already uses for Boundary. |
| **Fix pattern** | Existing **Map nest-parent / nest-kids** + **containment** storytelling (peers solid). Mirror Ch4: Equity outer → Income + Expenses kids; CV outer → FV / VIU / Fulfilment (and current cost if Content wants) as L2 cells. Tip-note Unit of account stays dashed see-also (already rare — keep). |
| **§-safe?** | **Yes** — relationships already taught on Ch4/Ch6; Map is navigation mirror. Low invent risk. |
| **Effort** | **Design redraw** of map HTML structure (still HOLD until unlock). Quick once unlocked. |

### Rank 5 — Ch1 accrual vs cash + Ch5 pre-2018 delta (lofi tables → contrast / matrix)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch1 visual “Accrual vs cash” `lofi` table; Ch5 visual “Pre-2018 vs 2018 delta” `lofi` table |
| **What’s weak** | True **A vs B** teaching points rendered as sparse 2–3 row tables with empty chrome around them. Weaker than body contrast elsewhere; misses same-format 対比 density. |
| **Fix pattern** | Existing **Contrast cards** or **Matrix/card-grid** (2 columns). Optional **C** *if later unlocked* for ultra-tight title+lines. Ch5 delta is explicitly teaching memory vs 2018 filters — contrast, not a process spine. |
| **§-safe?** | **Yes** — §1.17 / §5.x filters already cited. Low invent risk. |
| **Effort** | **Design redraw** (visual sections) or **CSS/kit polish** if body-side twins added. |

### Rank 6 — Legends: above-only → optional footer bar on decode-heavy plates

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Map `.map-legend`; Ch3 org legend; Ch5 filter tree legend; Ch7 stmt legend — all top/side |
| **What’s weak** | Gap #4: no **plate-bottom colour-key bar**. Top legends + section-label + hint + iframe chrome push teaching graphic down (page-as-poster gap). Some legends restate on-node labels (Ch4 correctly omits — good). |
| **Fix pattern** | Existing rule: omit legend when nodes are named. Where colour/line still need decode → optional **D Footer legend bar** *if later unlocked* (RESEARCH). Prefer moving/shrinking existing legend before inventing tokens. |
| **§-safe?** | **Yes** — legend chrome only; no process. Optional D = RESEARCH. |
| **Effort** | **Quick CSS/kit** after trial; until then: omit redundant legends (Content/Design QC). |

### Rank 7 — Ch6 selection-factors “1…5” table (pipeline look)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch6 visual “Selection considerations” numbered `lofi` table (`class="num"` 1–5) |
| **What’s weak** | Page *text* says “not a mandatory 1→5 pipeline,” but the **visual form** is a numbered checklist that JP tools often read as 手順. Competes with the better peer `grid-3` concept map above it. Duplicate teaching of same factors. |
| **Fix pattern** | Existing **Peer row / card-grid** (unordered). Drop numerals or replace with QC category chips (colour-as-category + legend). **Do not** add free circled step-rail. |
| **§-safe?** | **Needs Content cite** — factors are CF considerations (§6.43+), not ordered Board steps. Invent-process risk **medium** if numerals stay without pedagogy mark. |
| **Effort** | **Content restructure** + light Design visual edit. |

### Rank 8 — Worked-strip compression (Ch2/Ch4 long 3-cell strips)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Body `.worked-strip` (Facts / Concept·gate / Conclusion) — often long multi-sentence cells |
| **What’s weak** | Grammar is right (pedagogy strip, not Board spine), but cells balloon into essay columns. Gap #8: no compressed IO band; closest is worked-strip. |
| **Fix pattern** | Existing **Worked strips** — tighten to one fact line / one gate line / one conclusion chip. Optional **E IO / before–after strip** *if later unlocked* (RESEARCH) — **hold E** per skill (risk of looking like Board steps). Prefer compression of current strip first. |
| **§-safe?** | **Yes** for length trim. Optional E = RESEARCH; must not look like Framework Step 1–n. Invent risk **medium** if E ships casually. |
| **Effort** | **Content restructure** first; E only after Johnny unlock + Design care. |

### Rank 9 — Ch2 QC visual: three separate sections vs one dense hierarchy plate

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch2 visual: stack + separate 2-col fundamentals + separate 4-card enhancers |
| **What’s weak** | Stack spine is strong, but fundamentals and enhancers live in **extra section chrome** (label + hint + whitespace). Body already shows Relevance⊃Materiality containment — visual could nest predictive/confirmatory + materiality *inside* Relevance hub, and four enhancers as inner grid under Enhancing band, for one poster plate. |
| **Fix pattern** | Existing **Hierarchy stack** + **Containment** (outer band + `.contain-grid`). Not a QC decision tree. |
| **§-safe?** | **Yes** — §2 hierarchy already taught; body contain exemplar exists. Low invent risk. |
| **Effort** | **Design redraw** of Ch2 visual (compose, not new TYPE). |

### Rank 10 — Overview tag→chapter cheat matrix (lofi table) *(topic RETIRED — archive only)*

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Overview visual secondary “Tag → chapter cheat matrix” `lofi` table *(retired; was old site Ch1)* |
| **What’s weak** | Useful nav, but visually a spreadsheet under a denser start-here path. Same-format 図鑑 energy is missing (fixed slot per chapter). Start-here `sh-path` numbered 1–5 is OK as **marked pedagogy** (not Board procedure) — do **not** generalise it into a free kit rail class. |
| **Fix pattern** | Existing **Matrix / card-grid** or same-format catalog (research pack device #8 → matrix variant). Keep study path as one-off Design-drawn pedagogy strip — never ship free ①②③ class. |
| **§-safe?** | **Yes** for nav catalog. Study-path numerals: pedagogy-only (already labelled) — invent risk **low** if gated. |
| **Effort** | **Design redraw** / CSS polish of cheat grid; leave `sh-path` as custom. |

### Rank 11 — Ch1 concept-map vertical sparsity

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch1 visual users↔decisions↔info↔GPFS vertical stack |
| **What’s weak** | Correct TYPE (concept map, not procedure), but lots of vertical chrome (`rel-label` spacers, section padding). Party cast sits above hub as loose row; 3-box purpose grid **repeats** hub content. Feels like two half-plates instead of one dense map. |
| **Fix pattern** | Existing **Concept map** densify (tighter peer grid; party cast as icon+label row glued to hub). Optional **B Icon-label cell** *if later unlocked* for cast densification (RESEARCH). Drop or demote redundant 3-box if map already carries Purpose/Users/Accountability. |
| **§-safe?** | **Yes** — relationships §1.x; no sequence invent. Optional B = RESEARCH. |
| **Effort** | **Design redraw**; Content may cut duplicate 3-box. |

### Rank 12 — Ch5 twin-aim plate uses ad-hoc `grid-2`, not `.contrast-pair`

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch5 visual derecognition twin aims + full vs partial transfer |
| **What’s weak** | Teaching is strong (peers, not pipeline), but markup bypasses body kit `.contrast-pair` / `.kit-label`. Two stacked grids + rel-label = more chrome than a single dense 対比 plate. |
| **Fix pattern** | Existing **Contrast cards** (Aim1 vs Aim2; full-transfer vs partial). Optional **C** *if later unlocked* for tighter packing. |
| **§-safe?** | **Yes** — §5.26+ twin aims; low invent risk. |
| **Effort** | **Quick CSS/kit polish** (reuse classes) + light Design compose. |

### Rank 13 — Ch3 party cast → optional icon-label densifier

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch3 visual party-cast (emoji glyphs) + org chart |
| **What’s weak** | Org chart + Boundary contain are already strong. Cast uses emoji + role — works, but no reusable **ピクト＋短標** cell grammar (gap #2). Slightly sticker-ish vs night toolbook. |
| **Fix pattern** | Optional **B Icon-label cell** *if later unlocked* (RESEARCH). Until then: keep cast; monochrome/single-token icons; always icon+label (already). Not a substitute for containment/org chart. |
| **§-safe?** | **Yes** — actors only. Optional B = RESEARCH. Low invent risk. |
| **Effort** | Trial kit later; **do not** redraw org chart for emoji taste alone. |

### Rank 14 — Ch7 statement schematic densify (classification inside blocks)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Ch7 `stmt-layout` schematic + separate “CF-level classification grid” |
| **What’s weak** | Stmt schematic is already a win. Classification 3-box sits as a third section — same ideas could be **inner chips** inside P&L / OCI / SCF blocks (containment of communication cues). Concept map above is a bit hub-and-spoke sparse. |
| **Fix pattern** | Existing **Statement layout** + **Containment** inner chips. Keep IFRS 18 as dashed see-also (already correct). |
| **§-safe?** | **Yes** — CF communication principles; Standards detail stays see-also. Low invent risk. |
| **Effort** | **Design redraw** compose; lower priority because plate already teaches. |

### Rank 15 — Map Capital + Presentation bands (thin but honest)

| Field | Detail |
|-------|--------|
| **Chapter / plate** | Map Capital 2-box; Presentation hub + see-also |
| **What’s weak** | Intentionally thin (CF chapters are short). Not “broken” — just less 図解 density than Elements/Boundary. Capital could use a micro contrast cue (financial vs physical) on-node; Presentation already correctly uses dashed see-also for IFRS 18. |
| **Fix pattern** | Existing **Contrast** micro-labels on Capital peers; leave Presentation see-also rare. Optional **A** chip for “CF-level only” *if later unlocked*. |
| **§-safe?** | **Yes**. Low invent risk. |
| **Effort** | **Quick CSS/kit polish** if unlocked; else leave — honesty > fake density. |

---

## 4. Already strong (do not rework winners)

| Plate | Why it already hits 図解 |
|-------|-------------------------|
| **Ch4 formula board** | Equation backbone + Equity `.contain` with Income/Expenses `.contain-cell`; UoA tip; related see strip — signed exemplar |
| **Ch4 body** | `.containment` + multiple contrasts + worked strips — densest body kit mix |
| **Ch2 QC stack** (visual) | Fundamental → enhancing → cost hierarchy; correct TYPE; not a fake decision tree |
| **Ch2 body Relevance⊃Materiality** | `.contain` / `.contain-grid` — 組成 done right |
| **Ch3 Boundary containment** (visual + Map nest) | Outer Boundary + Consolidated/Unconsolidated L2; dashed only for IFRS 10 / IAS 27 see-also |
| **Ch3 org chart + party cast** | Group structure + actors before process — matches VISUAL-TYPES |
| **Ch7 `stmt-layout`** | Schematic P&L / OCI / SCF with brackets — statement TYPE used correctly |
| **Ch8 visual financial vs physical** | True contrast + formula cues + practice callout — chapter-appropriate |
| **Ch9 hierarchy + IAS 8 flowchart** | Rare legitimate process (Standards authority / IAS 8 order) — not invented CF spine |
| **Map overall** | Peer bands, nest-parent containment, hub vs peer legend, night-only, dashed rare (see-also + tip-note only) |
| **Dashed discipline** | Sitewide rare; no SmartArt hang observed on audited plates |
| **Ch5 recognition filters tree** | Genuine diagnostic branching — correct decision-tree use |

---

## 5. Do-not-do

| Ban | Why |
|-----|-----|
| **Free circled step-rail class** (reusable ①②③) | Skill gate: Standards-prescribed or marked pedagogy only; Design draws; never tempt Build with a free class |
| **Invent CF process spines** / Sankey / ops pipelines | Conceptual Framework ≠ bookkeeping money-flow book; Big 4 alone ≠ licence |
| **Ship optional A–E without Johnny lock** | RESEARCH densifiers only; suggested first trial *if* signed later: **A + D**, then C/B; hold E |
| **Decorative rainbow / pastel washes** | Colour = category with legend-able meaning; night-only |
| **Mascot / cartoon clutter** | Steal grammar, not ゴエモン navigator |
| **Dashed as hierarchy / nest hang** | Containment only for 組成; dashed = see-also or matrix N/A |
| **Redraw live `draft-v1-linked/` from this audit** | Propose only — PM unlocks trial before HTML/CSS shipping |
| **Numbered Board checklists-as-law** | Content pedagogy order ≠ Framework procedure (already labelled on several chapters — keep that discipline) |

---

## 6. Suggested unlock order (if Johnny later signs — not this audit)

1. Content/Design: **Rank 1** Ch6 card-grid matrix + **Rank 4** Map L2 densify (existing kit — no A–E needed)  
2. Content: **Rank 2–3** contrast trim + callout cull (existing kit)  
3. Trial densifiers (skill suggestion): **A + D**, then C on one FAQ body; B on Ch3 cast; **hold E** and free step-rails  

---

*End of audit · research/propose only · no live draft HTML/CSS changed · 2026-09-27 HKT*
