# CF visual kit ↔ JP 工具書／図解書 — gap notes

*(Site chapter numbers remapped 2026.09.27-7: old Ch2→Ch1 … old Ch10→Ch9; Overview topic retired. Official § cites unchanged.)*

**Status:** TRIAL unlocked (Johnny 2026-09-27 BOTH) · A+D first → C/B · hold E · pack-then-notify  
**Audience:** Johnny (PM / Design lock) · Design · Build  
**Date:** 2026-09-27 (Asia/Shanghai)  
**Scope:** Visual *grammar* patterns only — not CF technical claims, not new process spines.

---

## 1. Context

Johnny target (2026-09-27): sharpen the CF learning site toward Japanese **工具書／図解書** (illustrated textbook / how-to diagram book) page grammar — dense plate, tight grids, numbered rails, icon+label cells, dual contrast, footer legend bars, ポイント chips.

The kit **already leans that way**: night-only, 簡約 chrome / heavy dense teaching graphics, containment over SmartArt hang, dashed rare, Content picks TYPE / Design draws tops. This note is research to name the remaining gaps and propose **optional** kit adds — not a mandate to redraw chapters.

**UNLOCKED trial:** Build ships A–D classes; Design/Content apply per PM sequencing. Hold E and free step-rails.

Sources skimmed (box): `VISUAL-TYPES.md` (site + twin `refs/cf-2018/`), Ch4 formula board exemplar, `visuals/shared.css`, body kit in `assets/shared.css`, map `index.html` + `assets/map.css`, Ch2 stack / Ch3 contain+org / Ch6 matrix. Light web skim of generic JP 図解 publishing grammar (step rails, AB対比, icon+caption, plate density) — used only as layout reference.

---

## 2. What we already match

Map kit patterns → typical 図解 traits. Pointers are class / file, not a redraw brief.

| 図解 trait (generic) | Kit match | Pointers |
|---|---|---|
| Part–whole / 組成 as nested plate | **Containment** (outer + inner grid; peers solid) | `.contain` / `.contain-grid` / `.contain-cell` (`visuals/shared.css`); body `.containment` / `.containment-inner` (`assets/shared.css`); Ch4 Equity on formula board; Ch3 Boundary |
| Equal-rank peers side-by-side | **Peer rows / peer pair** | `.peer-row`, `.peer-pair`, solid `.box`; map L1 peer bands |
| Hierarchy (not chronology) | **Stack** | `.stack` — Ch2 QC fundamental → enhancing → cost |
| Spectrum / multi-criteria compare | **Matrix / card-grid** (IAS 37 exemplar lock) | `VISUAL-TYPES.md` matrix rules; Ch6 measurement-basis compare |
| Identity as organising idea | **Formula / equation board** | `.formula-board`, `.fb-term`, `.fb-op` — Ch4 exemplar |
| Facts → gate → conclusion (pedagogy) | **Worked-example strip** | `.worked-strip` / `.worked-strip-grid` — Ch4 body |
| What-it-is vs trap | **Contrast cards (two-column)** | `.contrast-pair` + `.kit-label` — Ch4 body |
| See-also / Standard bridge (not nest) | **Dashed see-also** (rare) | `.see-strip`, `.box.see`, `.fb-related`; tip-quiet / tip-nest |
| Where amounts land | **Statement schematic** | `.stmt-layout` / `.stmt-block` |
| Site map as nested chapters | **Map nest-parent** | `.map .nest-parent` / `.nest-kids` — `assets/map.css`, `index.html` |
| Colour needs decode → legend | **Legend + swatches** | `.legend` / `.legend-swatch*` (visuals + map `.map-legend`) |
| Actors before process | **Party / role icons** (cast layer) | Ch3 org chart `legend-icon` + party tokens in `VISUAL-TYPES.md` |
| Quiet chrome, dense teaching | **Density lock** | `VISUAL-TYPES.md` § Visual density — 簡約 chrome / heavy infographics; night-only |

**Net:** containment storytelling, peer solidity, matrix spectrum, formula board, worked strips, and contrast pairs already put us in 図解 territory. Gaps below are about *extra plate density and micro-grammar*, not a missing backbone taxonomy.

---

## 3. Gaps

Honest gaps vs denser textbook / 工具書 plates (grammar only):

1. **Numbered step rails / circled process columns** — Kit forbids inventing CF Board procedures; there is no sanctioned “circled ①②③ rail” pattern even for *Content-grounded* reading order or Standards-prescribed sequences (IAS 8-style stays Design-drawn flowchart, not a reusable rail).
2. **Icon + short label cells (ピクト＋2–4字)** — Party icons exist in places; no reusable **icon-label cell** grid (pictogram + terse caption) for cast / checklist densification.
3. **Dual-column contrast *density*** — `.contrast-pair` exists but often reads as two prose cards; JP plates pack title chip + 1–2 lines + optional mini-icon per side with almost no chrome.
4. **Footer legend bars** — Legends are typically above / beside the graphic; no **plate-bottom colour-key bar** pattern common on 図解 spreads.
5. **Page-as-poster density** — Section labels, page headers, and iframe framing still leave more empty chrome than a one-topic-fills-the-frame textbook plate.
6. **ポイント／注意 chips** — Callouts (`.callout`, tip-*) exist; no ultra-compact **chip** (1-line teaching flag) that sits in a gutter or plate corner without competing with the backbone.
7. **Cross-section / layered sandwich** — Containment covers 組成; true “sandwich slice” (layers labelled as strata) is not a named kit pattern.
8. **Input→output / before→after strip** — Closest is `.worked-strip`; no dedicated **IO band** with fixed In | Transform | Out (or Before | After) cells for pedagogy without looking like a CF process spine.
9. **Table + adjacent diagram on one plate** — Matrix and maps usually occupy separate sections; no compose rule for “lofi table left + small contain/map right” on a single plate.

Dashed remains correctly rare; do not “close” gaps by adding decorative dashed chrome.

---

## 4. Optional kit adds (3–5)

Each is **optional**. Content still picks TYPE from relationship; Design builds only when grounded. No invented CF process.

### A. Point chip（ポイント／注意チップ）

- **When to use:** One local teaching flag beside a backbone or body card — pitfall, reminder, or “do not confuse X with Y” — not a second backbone.
- **§-safe rule:** Chip text must cite or paraphrase a §/BC teaching move already on the page. **Not** for inventing numbered Board steps. Prefer over a full callout when the flag is ≤1 line.
- **Night-palette:** Surface = `--surface` or soft band; ink = `--ink`; border = solid `--line` (or semantic `--warn` / `--ok` **only** if legend/chip label states the meaning). No rainbow pills. Dashed border not for chips.

### B. Icon-label cell（ピクト＋短標セル）

- **When to use:** Party / role cast, or a short equal-rank checklist of *named* actors/objects where a pictogram speeds scan (entity, user, lender…).
- **§-safe rule:** Always **icon + label**; label carries the accounting meaning. Do not decorate peer definition pages with people icons. Not a substitute for containment or matrix.
- **Night-palette:** Neutral cell surface + ink border; icon monochrome / single semantic token if role colour is legend-able. Match stroke weight across the cast. No colourful sticker sets.

### C. Dense contrast plate（左右対比板）

- **When to use:** FAQ / trap / definition≠recognition style **A vs B** when both sides are short (title chip + ≤3 lines). Relationship = contrast, not process.
- **§-safe rule:** Same as body contrast cards — Content grounds both sides. Do **not** use when a full matrix/spectrum is required. Do not turn into Before→After of a fake CF procedure.
- **Night-palette:** Two solid peer frames; optional `.ok` / `.warn` title ink only with teaching meaning. Tight gutters; kill decorative washes. Dashed only if one side is literally see-also / absence.

### D. Footer legend bar（図版フッター凡例バー）

- **When to use:** Backbone already uses colour and/or solid vs dashed that need decoding **and** on-node labels are insufficient — put a thin **bottom bar** of swatch + one plain line each.
- **§-safe rule:** Existing legend lock still applies — if every node is already named, **omit** the bar (chrome, not teaching). Never invent tokens; reuse site semantic swatches.
- **Night-palette:** Bar background = quiet band/surface; swatches = existing `--elem-*` / outcome / see-also tokens; ink labels. No decorative rainbow key.

### E. IO / before–after strip（入出力帯 · 変化帯）

- **When to use:** Pedagogy only — facts **in** → which definition/gate applies → **out** (conclusion); or Before misconception | After correct reading. Sibling to worked-strip, more compressed.
- **§-safe rule:** **Must not** look like a Board-mandated procedure. No circled “Step 1–n of the Framework.” Content cites the § that justifies the conclusion. Prefer hierarchy/containment/matrix when those relationships are the point.
- **Night-palette:** Three (or two) solid cells; operators as no-box chrome; optional muted arrow labels. Dashed only for N/A cell. Same peer surface/ink as worked-strip.

**Deliberately not proposed as a free kit add:** generic circled **step rails** for CF chapters. If Johnny wants a rail later, gate it to (a) Standards-prescribed order Content cites, or (b) clearly marked pedagogy reading path — never a new CF spine. Design draws; Build does not ship a temptingly reusable “①②③” class without that gate.

---

## 5. Out of scope / still HOLD

- **No** new CF process spines, Board checklists-as-law, or flowchart defaults.
- **Night-only** stays Build lock — do not touch `theme.js` or reintroduce day theme.
- **E IO strip** held this pass unless worked-strip compression clearly needs it.
- Free circled step-rails still gated forever unless § order / marked pedagogy.
- Sandwich / table+diagram compose can wait.
- Content still picks TYPE; Design draws tops; Build owns shared CSS.

---

## 6. Trial sequencing (signed Johnny 2026-09-27)

1. **Wave 1:** A Point chip + D Footer legend bar (+ existing-kit polish / debt).
2. **Wave 2:** C Dense contrast on FAQ-heavy bodies; B Icon-label on Ch3 cast where it helps scan.
3. **Hold E** unless a worked-strip clearly needs In|Gate|Out.
4. Pack-then-notify — QC + Computer before Johnny ping.

---

*End of notes · trial unlocked · 2026-09-27*
