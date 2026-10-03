# Design pass — IFRS 18 P0 Concept Map / priority visuals
**Canon:** VISUAL-TYPES / skill **2026.09.27-6** · night-only · spacing ~14px · § chips `a.fb-num` → `#s-x-y` `target="_parent"` · single-frame fieldset on chapters · Map = NO fieldset · dashed rare · colour only with teaching meaning · FIRST DRAFT dense kit  
**When:** 2026-09-27 (Asia/Shanghai) · Design executor  
**Pack:** `refs/ifrs-18/draft-v1-linked/`  
**Tokens:** Build **GREEN** — mount only (no provisional hex)

## Token status
Build landed in `visuals/shared.css` (+ `assets/shared.css` mirror):
- Categories: `--cat-operating|investing|financing|tax|discontinued` (+ softs) → classes `.cat-*` / `.band.cat-*` / aliases `.cat-band--*`
- Measures: `--ifrs-subtotal` / `--mpm` → `.ifrs-subtotal` / `.mpm` (+ `.stmt-block .subtotal.*`) / aliases `.measure-ifrs` / `.measure-mpm`
- Legend swatches present for all seven

**Design did not invent parallel token names or provisional hex.**

## Files touched
| Path | Action |
|------|--------|
| `visuals/ch03-pfs-aggregation.html` | Replace stub → P0 dual plate + checklist matrix |
| `visuals/ch04-pnl-categories.html` | Replace stub → five-band schematic + main-path gate |
| `visuals/ch05-totals-subtotals.html` | Replace stub → brackets on skeleton + 3-col matrix |
| `visuals/ch07-mpms.html` | Replace stub → gate tree + waterfall |
| `visuals/map-jumpboard.html` | Replace stub → optional pillar twin |
| `wip/design-notes-2026-09-27/DESIGN-PASS-P0-concept-maps.md` | This note |

**Not edited:** parent chapter teaching bodies · homepage READY · P1/P2 stubs (Ch2/6/8/9) · `shared.css` colour tokens (Build owns) · no `chapter-visuals` twin (does not exist for IFRS 18)

**Preview:** `_review/ifrs-18/preview` is symlink → `draft-v1-linked` (auto-live)

## Per-P0 plate summary

### Map jump board
- **Live** on `index.html`: three pillars → Ch4–5 / Ch3 / Ch7; thin “1 Jan 2027” hub → Ch9; banks/insurers `.see-also` dashed.
- **No** Concept Map fieldset on Map (confirmed).
- Optional `visuals/map-jumpboard.html` mirrors pillars + timeline chip + dashed banks see-also (iframe twin; Map page does not embed it).

### Ch3 — PFS ∥ Notes + aggregation checklist
- Dual plate (PFS hub ∥ Notes) with `.rel-connect--both` “roles decide where”.
- Checklist = `.matrix` (not a fake flowchart); trap callout on §41 order; labelling see-callout → 3.4.
- Chips: 3.1 / 3.2 / 3.3 / 3.4.

### Ch4 — five category bands
- Vertical `.pnl-schematic` (page-local structural CSS only) mounting `.cat-band--operating|investing|financing|tax|discontinued`.
- Ch5 bracket placeholders as dashed italic cues (not required subtotals yet).
- Right-rail legend (on-band labels + swatches).
- Compact main-path gate (pedagogy · not Board flowchart); banks = text see-also only (Map-only dashed chip lock).
- Chips: 4.1 / 4.2 / 4.3 / 4.4 / 4.5 / 4.6.

### Ch5 — brackets + measure matrix
- Same band skeleton; required anchors as `.subtotal.ifrs-subtotal` with heavier border weight (not a third colour).
- §73 trap callout between middle bracket and financing band.
- Three-column matrix: Required / §118 / MPM using `.measure-ifrs` vs `.measure-mpm`.
- Legend for two measure tokens only.
- Chips: 5.1 / 5.2 / 5.4.

### Ch7 — gate tree + waterfall
- Four §117 gates → `.box.mpm` outcome.
- Waterfall: MPM (`.measure-mpm` / `.mpm`) → reconciling item → IFRS anchor (`.measure-ifrs` / `.ifrs-subtotal`).
- Contrast pair restates Ch5 grammar.
- Chips: 7.1 / 7.2 / 7.3 / 7.4.

## Parent fieldset status
| Page | Fieldset “Concept Map” | iframe src |
|------|------------------------|------------|
| `index.html` (Map) | **None** (correct) | — |
| `ch03.html` | Wired | `visuals/ch03-pfs-aggregation.html` |
| `ch04.html` | Wired | `visuals/ch04-pnl-categories.html` |
| `ch05.html` | Wired | `visuals/ch05-totals-subtotals.html` |
| `ch07.html` | Wired | `visuals/ch07-mpms.html` |

Content teaching bodies untouched.

## Twin sync
**Skipped** — no `refs/ifrs-18/chapter-visuals/` tree (unlike CF). Note for Build/PM if twin pattern is wanted later.

## Standing bar self-scan (pre-SAVE)
- [x] Night-only (theme.js force dark; no day invent)
- [x] § chips `a.fb-num` → parent `#s-x-y` + `target="_parent"` on teaching nodes
- [x] Chapter Concept Map = single fieldset chrome; Map has none
- [x] Stub “Design draws next” chrome stripped on P0 plates
- [x] Spacing: `.concept-map` gap 14px; peer-row / matrix / stacks use kit gaps; page-local `.pnl-schematic` gap 10px (inner band rhythm); no `gap:0` major stacks
- [x] Dashed rare: banks see-also · Ch4 bracket placeholders · matrix N/A not used
- [x] Colour only with teaching meaning — Build category + measure tokens only
- [x] No invented classification pipeline beyond § order (main-path labelled pedagogy)
- [x] No Big4 art copy
- [x] Homepage READY **not** flipped
- [x] P1/P2 chapter visuals left as Content stubs

## Build follow-ups (non-blocking)
1. Optional: promote page-local `.pnl-schematic` / `.gate-tree` / `.waterfall` into kit `shared.css` if reused on P1.
2. Optional: title ink for `.cat-band--*` (Design used inline `color:var(--cat-*)` on titles because alias class does not set title colour the way `.band.cat-* .box-title` does — Build could extend alias).
3. Twin `chapter-visuals/` tree if pack wants CF-parity offline twins.
4. Ch4 left-border accent relies on page CSS `border-left-width:4px` + Build `border-color` — confirm contrast on night remount if Build tweaks softs.

## Ambiguities
- Map optional iframe unused by `index.html` (live pillars preferred) — keep file as optional / review aid.
- Ch5 middle bracket shows §69(b) then §73 trap beneath — pedagogy order; not claiming every entity presents §69(b).
- Waterfall example (“adjusted operating profit”) is teaching paraphrase — not Foundation IE art.
