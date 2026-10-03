# IAS 2 Ch4 densify thin Illustrations + Ch5 Official lead — 2026-10-01 (Asia/Shanghai)

**Trigger:** PDF-replace densify for Ch4 Illus 4.3.1 / 4.5.1–4.5.5 from pack DTT iGAAP 2022 A11 + PwC FAQ extracts; fix bare `Official:` lead in Ch5 Illus 5.3.1. Johnny does not QC — QA gate mandatory before sync.

**Skill:** `ifrs-teaching-body-qa`. Map / CSS / visuals untouched. No invent beyond Official / pack Big4 extracts provided.

**Backups:** `ias2-content-extract/ch04.html.bak-20261001-153727`, `ch05.html.bak-20261001-153727`

## Before → after (bullet count / approx teaching-bullet chars)

| Illus | Source | Before | After | Columns |
|-------|--------|--------|-------|---------|
| **4.3.1** Formula write-downs | PwC FAQ 25.36.1 | 2 / ~206 | **8 / ~1034** | Facts / Assessment / Conclusion |
| **4.5.1** Sales after reporting period | DTT iGAAP 2022 A11 3.3.1-2 | 5 / ~302 | **9 / ~1000** | Facts / Usual gate / Exception |
| **4.5.2** Developer WIP | DTT iGAAP 2022 A11 3.3.1-3 | 5 / ~532 | **9 / ~1158** | Facts / Assessment / Conclusion |
| **4.5.3** Firm sales contracts | DTT iGAAP 2022 A11 3.3.1-4 | 5 / ~224 | **11 / ~929** | Facts / Covered 500 / Excess 500 |
| **4.5.4** Post-BS model change | PwC FAQ 25.39.1 | 5 / ~314 | **10 / ~1289** | Facts / Assessment / Conclusion |
| **4.5.5** Long production cycle NRV | DTT iGAAP 2022 A11 3.3.1-1 | 4 / ~307 | **11 / ~862** | Facts / Method 1 / Method 2 |
| Peer bar **4.2.1** (untouched) | DTT 3.3.2-1 | — | 11 / ~1586 | reference density |

Cite locator fix on 4.5.5 title chip: `3.3.1` → `3.3.1-1` (matches sibling `-2/-3/-4` and extract).

## Ch5 Official: lead fix

- Illus **5.3.1** Usual-gate li: bare `Official:` prefix → teaching-lead bold **Reversal reduces inventory expense (not a new income category).** + substance sentence retained.
- Pack scan: no other bare `Official:` / `Official.` body-title prefixes (ch01 “same structure as Official” is prose, not a lead prefix).

## HARD locks observed

- Title form `Illustration: N.M.k — …` + cite-row FULL firm+work+locator; Official = `IAS 2 · para N`; no `§`.
- All Illus = `.worked-strip` + `.worked-strip-grid` + neutral peer `.box` (zero `.ok`/`.warn`).
- Markup `div.box-body > ul` only.
- Cite chips on title only (no body chips on Illus).
- Numbers/facts only from provided extracts (CU100→80; printers 1000/150/130/170/10k/140k; C1m; six-year / year-2; formula age/movement/scrap + market/order book).

## QA gate (`ifrs-teaching-body-qa`) — green

- [x] A Cite: zero house-only; zero `§` in chips; Illus title-only chips
- [x] B Markup: zero `p.box-body > ul`; peer pattern match
- [x] B0 Colour: Illustration peers zero ok/warn
- [x] C Detail: each touched Illus ≫ pre-edit (≥8 bullets / ~800+ chars); long paras → bullets; no invent
- [x] Official bare-prefix scan clean

## Leftover thinner Illus in Ch4 (not in this priority pass)

| Illus | n / chars | Note |
|-------|-----------|------|
| **4.4.1** item-by-item teaching | 9 / ~463 | Numeric teaching strip; short by design — boost only if Johnny wants Official/para 29 narrative added |
| **4.6.1** Stage-1 WIP via finished | **13 / ~1702** | Densified 2026-10-01 ~15:50 CST — see `IAS2-ILLUS-461-DENSIFY-2026-10-01.md` |
| **4.7.1** capped reversal / materials | 8 / ~503 | Borderline; teaching strip — optional boost |

## Files

- `draft-v1-linked/ch04.html` (densify)
- `draft-v1-linked/ch05.html` (Official lead)
- `draft-v1-linked/IAS2-CH04-DENSIFY-THIN-2026-10-01.md` (this changelog)

## Sync

Documents machine `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` →  
`C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`


---

## Follow-on — Illus 4.6.1 densify (2026-10-01 ~15:50 Asia/Shanghai)

**Source:** PwC MOA 2020 Ch25 FAQ 25.40.1 illustrative text (full body) + IAS 2 para 32 / standing 25.40 materials rule.

| Metric | Before | After |
|--------|--------|-------|
| Bullets | 5 | **13** |
| Teaching chars | ~315 | **~1702** |
| Columns | Facts / Not this / Conclusion | **Facts / Assessment / Conclusion** (all neutral) |

Teaching numbers pulled (no invent): Stage 1 150/120; Stage 2 conversion 40/90 → cum 190/210; Stage 3 conversion 60/70 → completed 250/280; NRV path 280−60−40=**180**; selling costs immaterial; only sells completed product.

Backup: `ias2-content-extract/ch04-before-illus-461-densify-20261001-154801+0800.html`
