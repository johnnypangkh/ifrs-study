# Design pass — chrome strip · legends · Ch2 connectors · § chips
**Canon:** 2026.09.27-4 · unlock Johnny 2026-09-27 tidy · Design executor  
**When:** 2026-09-27 (Asia/Shanghai)

## Overview (Build-owned — verified only)
- `ch01-overview.html` unused / archived; no live iframe. Design did **not** redo Overview kill.

## Files touched
### Live visuals (`draft-v1-linked/visuals/`)
- `shared.css` — global `a.fb-num`; `.rel-connect` redraw (taller stems, kiss edges, label right of stem track); `.concept-map` column flex gap:0; dense connector heights; `.visual-with-legend` covers maps/stacks; title/chip flex helpers
- `ch02-objective-users.html` … `ch04-reporting-entity.html`, `ch06`…`ch10` (Ch5 left as signed exemplar)
- Twins synced: `chapter-visuals/` same HTML + `shared.css`

### Not edited
- Map `index.html` — already clean; teaching band-hints kept (`CF ≠ Standard`, `2018 filters`, `HC vs current value`, `maintenance concepts`)
- Parent chapter pages — Concept Map fieldsets kept; no Start-here / section-hint chrome found on Ch2–10 parents
- Ch5 visual — already `.fb-num` exemplar

## Per-chapter summary

| Ch | Chrome strip | Legend | Connectors | § chips |
|----|--------------|--------|------------|---------|
| 2 | Removed section-hint ×2, peer-note, footer-note, top legend | Dropped (party cast + titles clear); right-rail kit unused | Redrew causal chain: 3× `.rel-connect--down` stems 60–64px, labels right of stem; Purpose/Users → Decisions → Info needs / Accountability → GPFS | 2.2, 2.3, 2.4, 2.5, 2.6 (+ GPFS 2.2) |
| 3 | Removed section-hint, section-label layout meta, footer-note, top legend | Dropped (containment self-labelled) | Hierarchy `arrow-down` kept (not relation kit) | 3.2, 3.3, 3.5, 3.6, 3.7 |
| 4 | Removed section-hints, layout section-labels, footer-note, top legend + legend-bar | Dropped (labels + see-strips clear) | Org `.rel-connect--down` stem quality via shared CSS | 4.3–4.6 on L1 / consol nodes + table |
| 5 | Unchanged (exemplar) | — | — | Already `.fb-num` |
| 6 | Removed section-hints, peer-note, footer-note, legend-bar, “not a pipeline” point-chip chrome | Dropped (YES/NO boxes self-labelled) | Twin-aim `.rel-connect--both` kept | 6.2, 6.3, 6.6 section chips |
| 7 | Removed section-hints, footer-note, legend-bar, matrix-note chrome | Dropped | Selection `.rel-connect--down` kept | 7.2, 7.3, 7.5 on hubs + matrix heads |
| 8 | Removed section-hints, peer-note, footer-note, dual top legends | Dropped | Classification/aggregation connectors; first link → `--down` | 8.1, 8.3, 8.4, 8.6 |
| 9 | Removed section-hint, footer-note, top legend | Dropped | N/A | 9.2 ×2 (financial / physical) |
| 10 | Removed section-hint, footer-note, top legend | Dropped | Hierarchy/IAS8 arrows kept | 10.1, 10.2, 10.3 |
| Map | No redundant chrome found | N/A | N/A | N/A |

## Build-needed CSS notes
- **No Build collision expected** for `.rel-connect` (lives in Design `visuals/shared.css`).
- New **global** `a.fb-num` in visuals CSS — iframe-scoped; parent `assets/shared.css` does not need it unless Build wants body-kit chips later.
- Right-rail kit already present: `.visual-with-legend` + `.legend.legend-side`. This pass **dropped** student legends where graphics self-label; kit remains if a future plate needs decode.
- Kit leftovers still in CSS (unused): `.section-hint`, `.footer-note`, `.peer-note`, `.legend-bar`, `.start-here`, neutralized `.visual-shell` — safe; HTML no longer uses them on live Ch2–10.

## Self-scan before SAVE
- No `.visual-shell` on live visuals
- No duplicate Concept Map titles inside iframes
- No empty chrome strips
- Parent `fieldset.visual-fieldset` / Concept Map legend untouched
- Twin parity: `draft-v1-linked/visuals/{ch02–10,shared.css}` ≡ `chapter-visuals/`

## Ambiguities
- Legends: chose **drop** over right-rail because nodes/outcomes are self-labelled; say if Johnny wants colour decode rails back on Ch4 org / Ch6 tree / Ch7 matrix.
- Ch2 first connector changed from `--both` to `--down` (Purpose/Users → Decisions) for clearer causal direction.
- Teaching callouts kept where they teach (Ch6 pre-2018 delta; Ch9 practice; Ch10 not-a-licence; Ch2 stewardship tip).
