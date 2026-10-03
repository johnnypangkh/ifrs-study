# CF 2018 — Full 大執 pass (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/cf-2018/draft-v1-linked/`  
**Skills (read full):** ifrs-teaching-body · ifrs-teaching-body-qa · ifrs-visual-grammar  
**Prior wave:** cite-only (`CF-SKILL-ROLLOUT-2026-10-01.md`) — densify / title-essence / Map were OPEN  
**IFRS 18 / IAS 2:** NOT touched

## Pack path

`/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/` — ch01–ch09.html · index.html · visuals/ · METHOD/NOTES  
Pack root: `/workspace/ifrs-website/refs/cf-2018/`

## Big4 pre-flight (this wave)

| Firm / source | Path / status |
|---------------|---------------|
| Official | `inputs/cf-2018/official-conceptual-framework-2026.pdf` (+ archive extract) |
| DTT A2 2022 | `inputs/cf-2018/dtt-2022-conceptual-framework-moa.pdf` |
| PwC MOA 2020 intro | `inputs/pwc-2020-moa/01-conceptual-framework-intro.pdf` |
| EY CF | **not on disk** — no invent |
| KPMG CF | **not on disk** — no invent |

**Crosswalk A/B (locator-level Official ↔ Big4):** still **debt** before any pack-complete claim (same as prior rollout). This wave densified from scanned Official + DTT/PwC; did not invent EY/KPMG.

## What changed (this wave)

### 1. Illus → worked-strip-grid, neutral peers
All **6** Illus rewritten as `.worked-strip` + `.worked-strip-grid` with **neutral** peer columns (`div.box-body > ul`); **zero** `.ok`/`.warn` on Illus peers.

| Illus | Peers | Source densify |
|-------|-------|----------------|
| 3.5.1 Going concern | Facts \| Assessment \| Conclusion | CF para 3.9 · DTT A2 · 6.1 · PwC 1.57 |
| 4.4.1 Claim fails liability → equity | Facts \| Assessment \| Conclusion | CF para 4.26–27, 4.63–65 · PwC 1.72 |
| 4.5.1 Owner cash vs inventory sale | Facts \| Assessment \| Conclusion | CF para 4.68–71 |
| 5.5.1 Non-recognition distorts performance | Facts \| Assessment \| Conclusion | CF para 5.19–22, 5.25(a) · PwC 1.77 |
| 6.6.1 Day-2 P&L / deemed cost | Facts \| Assessment \| Conclusion | CF para 6.6, 6.48, 6.78, 6.80–81 |
| 8.4.1 Three-way CU15 | Facts \| Nominal \| Constant PP \| Physical | CF para 8.5–8.10 · DTT A2 · 11 (table → peer grid) |

Decision strips remain Decision strips (not Illus); their `.ok` peers left as non-Illus teaching contrast.

### 2. Densify (quantitative)
All 6 Illus: **≥10 bullets** and **≳1300 chars** peer text — densify gate **PASS** (was thin Start\|Gate\|Conclusion / table-only). Teaching cues remain labelled “not an Official numeric IE” where CF has no IE series. **No invent** EY/KPMG.

### 3. Map enhance unlocked (CF this wave)
- **Pack Map (`index.html`):** story + visit path documented in HTML comment; purpose line for cross-chapter jump board; phase-legend visit wording; “2018 recognition criteria” technical label; `map.css?v=cf-full-20261001`.
- **Chapter-top Maps:** story/visit HTML comments on all 9 visuals; `data-theme="dark"` on ch02/ch04/ch05 embeds that lacked it; iframe cache-bust `?v=cf-full-20261001` on ch01–ch09.
- **Not a full Opus redraw** of signed boards (Ch1/Ch2/Ch4/Ch6/Ch7 already Johnny-locked method). Geometry/chrome of those boards preserved; enhance = visit-path documentation + night + cache-bust + pack Map flow copy.
- Illus peers **not** restyled with Map leaf green/red.

### 4. Cite locks kept
`CF 2018 · para …`; firm+work+locator; **zero `§` in chips**; Illus title chips (C1); no house-only chips. No EY/KPMG invent.

### 5. Title essence (~25 firm leads)
Rewrote bare `<strong>DTT.</strong>` / `<strong>PwC.</strong>` / `<strong>Official.</strong>` / `<strong>Official PRIMARY.</strong>` leads to teaching substance; chips unchanged. Residual PwC leads inside Illus peers also fixed. Automated E gate **PASS**.

### 6. METHOD
`CF-CONTENT-REWRITE-METHOD.md` updated: Map unlock for CF; densify/Illus/cite locks unchanged in substance.

## QA summary (ifrs-teaching-body-qa)

| Gate | Result |
|------|--------|
| A Cite — house-only / `§` / Official=`CF 2018 · para…` | **PASS** |
| A Placement C1 Illus title chips | **PASS** |
| B Illus = worked-strip-grid | **PASS** (6/6) |
| B Illus peers neutral | **PASS** |
| C `p.box-body>ul` | **PASS** |
| D Densify quantitative | **PASS** (all 6) |
| E Title essence | **PASS** |
| E2 Technical-strict titles | **PASS** (flowery scan clean) |
| E3 Visual-when-complex | **Partial** — Illus now have multi-peer grids; extra mini-diagrams inside Illus not added (debt if Johnny wants diagram chrome beyond peers) |
| F Hyperlink | No id renumbers of Illus anchors (`s-3-5-gc`, `s-4-4-ex`, … preserved) |
| I Big4 pre-flight | Official+DTT+PwC on disk; EY/KPMG **not on disk**; Crosswalk A/B still debt |
| Map (unlocked) | Pack Map + chapter-top enhance as above; Illus peers still neutral |

## Files touched

- `draft-v1-linked/ch01.html` … `ch09.html`
- `draft-v1-linked/index.html`
- `draft-v1-linked/visuals/ch01…ch09-*.html` (story comments; dark theme on 3)
- `draft-v1-linked/CF-CONTENT-REWRITE-METHOD.md`
- `refs/cf-2018/CF-FULL-PASS-2026-10-01.md` (this note)

## Backups

`/workspace/cf2018-full-pass-20261001-191841+0800/` (pre-edit ch01–ch09 + index + METHOD + visuals + CSS)

## Open gaps / debt

1. **Crosswalk A/B** locator tables — required before pack-complete claim.
2. **EY/KPMG CF** — not on disk; Blocking for complete claim until scanned or Johnny confirms unavailable.
3. **Decision-strip `.ok` peers** — still used on non-Illus strips; confirm vs convert to `.contrast-pair` if Johnny wants zero ok/warn inside any worked-strip-grid.
4. **Body prose `§`** — chips clean; running text may still say “Teaching §§” in places (optional later pass → `para`).
5. **Illus mini-diagrams** — peer grids dense; optional extra diagram chrome for complex plates (E3) if Johnny wants beyond peers.
6. **Full Map Opus redraw** — not this wave; signed boards kept; enhance = visit-path + night + pack flow + cache-bust.

## Sync target

Documents laptop `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` → `C:\Users\johnny\Documents\ifrs-website-refs\…` under `refs/cf-2018/…`

**Sync status (2026-10-01 ~19:25 Asia/Shanghai):** **FAIL** — laptop `LAPTOP-MODGPP0C` (`2a06a250-…`) **connected: false**. Box edits complete; retry CopyFromBox when Johnny reconnects.
