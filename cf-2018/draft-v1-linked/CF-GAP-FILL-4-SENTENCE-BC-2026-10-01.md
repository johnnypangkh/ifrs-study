# CF 2018 — Gap-fill-4: sentence-level BC × four firms

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/cf-2018/draft-v1-linked/`  
**Date:** 2026-10-01 Asia/Shanghai (~22:40 HKT)  
**Backup:** `/workspace/cf2018-gap-fill4-20261001-backup/`  
**IAS 2:** untouched  
**Skills:** ifrs-teaching-body · ifrs-teaching-body-qa  

## Completeness claim (HARD)

**Pack-complete / Crosswalk A sentence-level: YES**

- Every Official CF 2018 BC paragraph **BC0.1–BC0.43, BC1.1–BC1.48, BC2.1–BC2.74, BC3.1–BC3.26, BC4.1–BC4.97, BC5.1–BC5.30, BC6.1–BC6.55, BC7.1–BC7.33, BC8.1–BC8.4** = **410 rows**.
- Each row × **PwC / DTT / EY / KPMG** = **1640 cells**.
- Cell = **real harvested BC.nn locator** OR **`not-addressed`**. **Zero invented firm BC cites.**
- Crosswalk B (named plates) remains complete from prior waves → **A+B pack-complete YES** at this grain.

`CF-GAP-FILL-3` TOC-band pack-complete stamp is **superseded → Partial**.

## Row counts

| Metric | Count |
|--------|------:|
| Official BC.nn rows | **410** |
| Firm columns | **4** (PwC, DTT, EY, KPMG) |
| Total cells | **1640** |
| Firm-cited cells | **11** |
| **not-addressed** cells | **1629** |
| Invented cites | **0** |

### Firm-cited breakdown (11 cells)

| Firm | Distinct BC.nn | Locators |
|------|---------------:|----------|
| **PwC** | **0** | MOA intro + Appendix 2: no BC.nn string |
| **DTT** | **1** | BC1.41 — `DTT A2 2022 · CF:BC1.41` (stewardship) |
| **EY** | **7** | BC0.27, BC0.28, BC3.21, BC6.1, BC6.10, BC7.24, BC7.29 — IGAAP Ch2 |
| **KPMG** | **3** | BC1.41, BC3.21 (Combined/Carve); BC7.25 (Insights 1.2) |

Note: BC1.41 and BC3.21 appear for two firms each → 1+7+3 = 11 cell instances (not 1+7+3 distinct BC ids = 9 unique BC.nn with any firm cite).

## Harvest method (no invent)

Scanned:
- Official: `inputs/cf-2018/official-conceptual-framework-2026.pdf` → 410 contiguous BC.nn
- DTT: `dtt-2022-conceptual-framework-moa.pdf` + A2 appendix extract
- PwC: `01-conceptual-framework-intro.pdf` + Appendix 2 Combined/Carve extract
- EY: IGAAP 2026 part1 Ch2 pp 46–103 + devel169
- KPMG: Insights part1 · 1.2; Combined/Carve 2022; flyer Apr 2018

**Excluded:** `pwc-folder-hkas-framework18.pdf` — Official CF reprint (HKICPA), **not** PwC commentary cites.

Chapter-teaching without a BC.nn chip stays in the SP+Ch1–8 spine only — **not** written into BC.nn cells as fake locators.

## Files updated

- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/CF-XREF-OFFICIAL-TO-BIG4-2026-10-01.md` (+ twin under `refs/cf-2018/`)
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/CF-GAP-FILL-4-SENTENCE-BC-2026-10-01.md` (+ twin)
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/CF-GAP-FILL-3-2026-10-01.md` — completeness → Partial / SUPERSEDED

## Sync

Laptop offline → Documents sync **skipped**.

## KEY CHANGES

1. Crosswalk A now has **410 sentence-level BC rows × 4 firms** (1640 cells).
2. **11** real firm-cited cells; **1629** honest **not-addressed**.
3. GAP-FILL-3 pack-complete YES **withdrawn**; gap-fill-4 stamps sentence-level A complete → pack-complete YES with B.
