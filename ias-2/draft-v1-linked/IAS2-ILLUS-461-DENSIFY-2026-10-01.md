# IAS 2 Illus 4.6.1 densify — Stage-1 WIP NRV via finished product — 2026-10-01 (Asia/Shanghai)

**Trigger:** Leftover thin plate from Ch4 densify pass (`IAS2-CH04-DENSIFY-THIN-2026-10-01.md`): 4.6.1 was 5 / ~315 vs densify bar (>5 bullets AND >350 chars; aim ~4.2.1 density).

**Skill:** `ifrs-teaching-body` + QA gate `ifrs-teaching-body-qa`. Map / CSS / visuals untouched. No invent.

**Backup:** `ias2-content-extract/ch04-before-illus-461-densify-20261001-154801+0800.html`

## Source (faithful)

PwC MOA 2020 Ch25 · FAQ 25.40.1 illustrative text (`/tmp/pwc25.txt` / layout PDF extract) · IAS 2 para 32 · standing text 25.40.

Entity manufactures telecommunication equipment in three stages; market for semi-finished at each stage but entity only sells completed product; 31 Dec 20X2:

| | Cost/unit (C) | Selling price/unit (C) |
|--|-------------:|----------------------:|
| Stage 1 | 150 | 120 |
| Stage 2 – conversion costs | 40 | 90 |
| cumulative after stage 2 | 190 | 210 |
| Stage 3 – conversion costs | 60 | 70 |
| completed | 250 | 280 |

Selling costs immaterial. NRV stage 1 via finished path: 280 − 60 − 40 = **180**.

## Before → after

| | Before | After |
|--|--------|-------|
| Bullets | 5 | **13** |
| Teaching chars | ~315 | **~1702** |
| Columns | Facts / Not this / Conclusion | **Facts / Assessment / Conclusion** |
| Peer colour | neutral | neutral (unchanged) |
| Markup | `div.box-body > ul` | same |
| Cite chips | title only (PwC FAQ 25.40.1 + IAS 2 para 32) | same |

## HARD locks observed

- Title form `Illustration: 4.6.1 — …` + cite-row FULL; no `§`; no bare `PwC:` lead.
- All Illus peers neutral `.box` (zero `.ok`/`.warn`).
- Markup `div.box-body > ul` only; chips on title only.
- Numbers/conclusions only from FAQ + para 32 materials rule already in §4.6 body.

## QA gate (`ifrs-teaching-body-qa`) — green

- [x] A Cite: zero house-only; zero `§` in chips; Illus title-only chips
- [x] B Markup: zero `p.box-body > ul`; peer pattern match
- [x] B0 Colour: Illustration peers zero ok/warn
- [x] C Detail: 13 / ~1702 ≫ densify bar and toward 4.2.1 peer (~11 / ~1586)
- [x] E Title essence: clean
- [x] No invent beyond FAQ + Official para 32 alignment

## Files

- `draft-v1-linked/ch04.html` (Illus 4.6.1 densify)
- `draft-v1-linked/IAS2-ILLUS-461-DENSIFY-2026-10-01.md` (this note)
- `draft-v1-linked/IAS2-CH04-DENSIFY-THIN-2026-10-01.md` (leftover row updated)

## Sync

Documents machine `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` →  
`C:\Users\johnny\Documents\ifrs-website-refs\refs\ias-2\draft-v1-linked\`

## Sync status

**PENDING** — Documents machine `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` disconnected at edit time (2026-10-01 ~15:50 Asia/Shanghai). Content work complete on box; retry CopyFromBox when online. ch02/ch03 title-link sync also still pending from prior offline.
