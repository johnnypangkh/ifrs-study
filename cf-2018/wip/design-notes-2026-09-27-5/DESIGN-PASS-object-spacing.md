# Design pass — Concept Map object-spacing
**Canon:** 2026.09.27-5 · spacing FAIL gate · PM unlock  
**When:** 2026-09-27 (Asia/Shanghai) · Design executor  
**Fail exemplar:** Ch8 Presentation Concept Map (`ch08-presentation-disclosure.html`)  
**Fail refs:** Johnny attachments `53c389…png`, `56122…png`, `3f286…png` (+ archive preview `ch08-presentation-disclosure.png`)

## Problem (Ch8 before)
1. **Major objects kiss** — `.concept-map { gap: 0 }` collapsed hub → Classification → Aggregation into a zero-air stack; Aggregation bottom also kissed the 8.5 stmt panels because `body.embed .section { margin: 0 }` zeroed sibling section air.
2. **Detached rel label** — Classification↔Aggregation `.rel-connect--both` used ~60–64px dense stems with parent gap wiped; the “both **inform** …” label read as floating under sticky chapter chips rather than sitting *between* the two boxes.
3. **8.5 panels cramped** — `.stmt-block { padding: 8px 10px }` + tight `.inner-cues` / `.bracket` / `.subtotal` margins left chips kissing the panel footer edge across all three peer columns.

## Fix (CSS-global — no HTML nudge)
All live changes in twin `shared.css` only. HTML for Ch2–Ch10 unchanged.

| Selector | Before | After |
|----------|--------|-------|
| `.concept-map` gap | `0` | `14px` (~12–16 target) |
| `.stack` / `.flow-col` / `.tree` / `.org-chart` gap | `0` (org had no flex gap) | `14px` (org-chart → column flex) |
| `.rel-connect` min-height | `64px` | `48px` |
| `.rel-connect-stem` min-height | `64px` | `48px` |
| `.rel-connect` margin | `0` | `-14px 0` (cancels parent gap so stem still meets box edges; connector height alone spaces the pair) |
| `.concept-map.dense .rel-connect` | min-height `60px`, margin `0` | min-height `44px`, margin `-14px 0` |
| `.rel-connect-label` padding | `8px 4px 8px 0` | `4px 4px 4px 0` |
| `.stmt-block` padding | `8px 10px` | `12px 12px` |
| `.stmt-layout` gap | `10px` | `12px` |
| `.stmt-block .inner-cues` | margin-top `6px`, gap `4px` | margin-top `10px`, gap `6px` |
| `.stmt-block .subtotal` / `.bracket` | mt `6px` / `4px` | mt `8px` / `8px` |
| `.box` padding | `10px 12px` | `12px 14px` |
| `body.embed .section + .section` | *(none — all sections margin 0)* | `margin-top: 14px` |

Stems still kiss adjacent box edges via the negative margin cancel; crowding is **not** solved by zeroing parent gap (Canon rule).

## Ch8 after (expected read)
- Hub / Classification / Aggregation breathe with ~14px object rhythm; “both **inform** …” sits in the shorter stem track between Classification and Aggregation.
- Aggregation no longer kisses the 8.5 three-panel row (section sibling air).
- P&L / OCI / Cash-flow panels share the same inner vertical rhythm; chips clear the panel edge.

## Chapter inherit matrix

| Ch | Via CSS-global | HTML nudge |
|----|----------------|------------|
| 2 | `.concept-map.dense` gap + shorter dense stems; `.box` padding | none |
| 3 | `.stack` gap 14; `.box`/`.contain` air | none |
| 4 | `.org-chart` flex+gap; `.rel-connect` shorter; section sibling air; `.flow-col` | none |
| 5 | `.box` padding only (formula-board / peer columns untouched; still signed exemplar) | none |
| 6 | `.concept-map` + `.flow-col` gap; `.rel-connect--both` shorter | none |
| 7 | `.concept-map` + `.rel-connect--down` | none |
| 8 | **Fail exemplar** — all of the above + `.stmt-block` / `.stmt-layout` / section sibling | none |
| 9 | `.box` padding; section sibling if multi-section | none |
| 10 | `.stack` + `.flow-col` gap; section sibling air | none |

## Files touched
- `refs/cf-2018/draft-v1-linked/visuals/shared.css`
- `refs/cf-2018/chapter-visuals/shared.css` (twin sync — identical)
- `refs/cf-2018/wip/design-notes-2026-09-27-5/DESIGN-PASS-object-spacing.md` (this note)

**Not edited:** any `ch*.html`, parent chapter pages, `assets/shared.css` (Build/parent), Overview, chrome strips, colour-decode legends, § chips markup.

## Self-scan (pre-SAVE)
- [x] No `.concept-map` / `.stack` / `.flow-col` / `.tree` / `.org-chart` at `gap: 0`
- [x] No kissing majors inside concept-map stacks (gap restored; stems cancel into gap)
- [x] Rel labels shortened/centered between related boxes (not floating under sticky tags)
- [x] Fieldset Concept Map remains sole outer frame (`body.embed` shell neutralization untouched)
- [x] § chips (`a.fb-num`) stay
- [x] No double frames / duplicate titles / empty chrome introduced
- [x] Twin parity draft visuals ↔ chapter-visuals

## Build notes
- **No parent CSS tokens needed.** All rhythm lives in Design iframe `visuals/shared.css`.
- Parent `draft-v1-linked/assets/shared.css` not touched; iframe does not link it for these kits.
- Iframe-fit / SAVE-report remains PM/parent.

## Ambiguities
- Left `.flow-col` / `.tree` / `.org-chart` on the same 14px rhythm as `.concept-map` / `.stack` so self-scan “no gap:0 stacks” holds beyond concept-maps; say if Johnny wants decision-tree arrows denser than relation stems.
- Horizontal `.rel-connect--h` / Overview study-path unchanged (out of scope; Overview not live).
- Ch5 formula-board `row-gap: 0` left alone (signed exemplar; horizontal peer gap already 10px).
