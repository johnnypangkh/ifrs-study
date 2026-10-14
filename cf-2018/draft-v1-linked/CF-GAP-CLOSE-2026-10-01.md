# CF 2018 — Gap-close wave (after IAS2-parity)

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/cf-2018/draft-v1-linked/`  
**Skills:** ifrs-teaching-body · ifrs-teaching-body-qa · ifrs-visual-grammar  
**Prior:** `CF-IAS2-PARITY-2026-10-01.md`  
**Date:** 2026-10-01 Asia/Shanghai  
**Backup:** `/workspace/cf2018-gap-close-20261001-backup/draft-v1-linked/`

## Completeness claim (HARD)

**Pack-complete / Crosswalk-complete: NO**

Crosswalk A+B are **locator-dense** (SP+Ch1–8 teaching spine, BC clusters, Combined/Carve Ex 1–2 + select 3–4, EY Figure 9-1, PwC A2 spine) but:

- A: discrete BC0–BC8 × four firms not fully rowed (clusters yes; honest Partial).
- B: KPMG Combined/Carve **Ex 3E–3H** and **Ex 4C–4H** still Crosswalk inventory / Illus debt (orphan vs Official CF — firm prep mechanics).

Do **not** stamp pack-complete.

## What changed

### 1. Crosswalk A+B (updated same-date files)
- `CF-XREF-OFFICIAL-TO-BIG4-2026-10-01.md` — finer Official para bands + **BC cluster table** + SUMMARY.
- `CF-XREF-BIG4-TO-OFFICIAL-2026-10-01.md` — Ex 2A–2E / 3C–3D / 4A–4B site Illus rows; Ex 3E–3H / 4C–4H debt; PwC A2 densify rows; EY Figure 9-1 → Ch6; SUMMARY.

### 2. KPMG Combined/Carve Ex 2–4 → Illus (paraphrase+cite; neutral peers)
| Illus | Source | Chapter |
|-------|--------|---------|
| 9.5.3 | Ex 2A Common control owner | Ch9 |
| 9.5.4 | Ex 2B Family common management | Ch9 |
| 9.5.5 | Ex 2C Real estate fund | Ch9 |
| 9.5.6 | Ex 2E Similar business fail | Ch9 |
| 9.6.1 | Ex 3C Top-down | Ch9 |
| 9.6.2 | Ex 3D Bottom-up | Ch9 |
| 10.3.1 | Ex 2D Track record vs undertaking | Ch10 |
| 10.4.1 | Ex 4A Related-party inventory | Ch10 |
| 10.4.2 | Ex 4B Central-cost allocation | Ch10 |

Prior Illus 9.5.1 / 9.5.2 / 10.2.1 retained.

### 3. EY IGAAP Ch2 measurement matrices → Ch6 §6.4
- Section tables (not Illus): assets SoFP + performance; liabilities SoFP + performance — write-once from Official CF 6.23 / EY Figure 9-1.
- Chips: `CF 2018 · para 6.23` · `EY IGAAP 2026 · Ch2 · section 9.2 · Figure 9-1` · `DTT A2 2022 · 9`.
- Narrative 6.24–6.42 paraphrase write-once under tables.

### 4. Ch9 / Ch10 Concept Maps
- Rebuilt `visuals/ch09-combined.html` and `visuals/ch10-carve.html` as usable jump boards (story + visit path in HTML comment; fb-num chips to body ids; peers + dashed see-also).
- **Not** claiming Opus-signed polish.
- Pack Map cell bodies updated; iframe `?v=cf-gap-20261001`; min-height 560px.

### 5. PwC A2 FAQ / para bodies
- Densified extractable spine into Ch9 §9.6: A2.14 five steps; A2.16 / A2.42–A2.48 binding; A2.63–A2.69 + Exhibit A2.7–A2.8 historical vs pro forma (paraphrase).
- Ch10 §10.4: A2.66–A2.69 allocation caution; chips on Illus 10.4.2.
- Not every A2.nn exhibit wrapped as Illus — honest Partial.

## QA (ifrs-teaching-body-qa) — touched Ch6/Ch9/Ch10

| Gate | Result |
|------|--------|
| A Cite — house-only / `§` / Official form | **PASS** |
| B Illus = worked-strip; peers neutral | **PASS** (12 Illus across Ch9/10 + prior Ch6) |
| C `p.box-body>ul` | **PASS** |
| D Densify quantitative | **PASS** — all new Illus li≥8 / chars≫350 |
| E / E2 Title essence / technical-strict | **PASS** |
| E3 Visual-when-complex | **Partial** — multi-gate Ex 2D/4B have Gate peer columns; Ch9/10 Maps usable not Opus |
| F Hyperlink frags (touched) | **PASS** — zero missing among checked |
| I Crosswalk A+B | **Partial densify** — not complete → **no pack-complete** |
| Map | Pack Map cells + Ch9/10 Concept Maps linked |

## Remaining gaps / debt

1. Crosswalk A discrete BC×firm rows (clusters done).
2. KPMG Combined/Carve **Ex 3E–3H**, **Ex 4C–4H** Illus backlog (orphan Official — firm prep).
3. PwC A2 exhibits / A2.50–A2.78 not fully plate-wrapped.
4. Decision-strip `.ok` peers still deferred (Johnny).
5. Ch9/Ch10 Maps — usable; not Johnny-signed Opus redraws.
6. ACCA — visit path only; never cite.

## Sync

Laptop `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` connected — Documents sync: **OK** (~19:58–20:00 Asia/Shanghai) — report, Crosswalk A/B, ch06/ch09/ch10, index, Ch9/10 Concept Maps → `C:\Users\johnny\Documents\ifrs-website-refs\refs\cf-2018\…`.
