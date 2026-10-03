**Official PRIMARY (2026-09-30):** `inputs/cf-2018/official-conceptual-framework-2026.pdf` — see `inputs/cf-2018/OFFICIAL-SOURCE-NOTE.md`.

# Conceptual Framework 2018 pack inventory

Status: **PARTIAL but UNLOCKED for Phase B skeletons** (2026-09-27 Johnny).
Official Framework (+ BC) is primary; Big 4 still thin (only DTT 2022 summary). Prefer more Big 4 later; do **not** block rough skeletons.

Teaching target: **Conceptual Framework for Financial Reporting (2018)** — site labels Conceptual Framework / IFRS only (no HK dual codes). HK text treated as IFRS.

## Items

### 0b. Official — Conceptual Framework (IFRS Foundation Issued 2026 HTML) — PRIMARY for quotes
- File: `inputs/cf-2018/official-conceptual-framework-ifrs-2026-issued.html`
- Note: Bound Volume **2026 Issued** container; substance still **March 2018** CF (no post-2018 CF text amendments). See `inputs/cf-2018/OFFICIAL-SOURCE-NOTE.md`.
- Authority: **PRIMARY for teaching quotes** (site IFRS/Board labels)
- Prior HK PDF remains: `inputs/cf-2018/official-conceptual-framework-hk-2022-09.pdf` (Revised Aug 2020 / Sept 2022)

### 0. Official — Conceptual Framework for Financial Reporting (HKICPA) — archive twin
- File: `inputs/cf-2018/official-conceptual-framework-hk-2022-09.pdf` (155 pages)
- Publisher: **HKICPA** (IFRS Foundation material)
- Edition marks: Revised **August 2020 / September 2022**; CONCEPTUAL FRAMEWORK (2022)
- Substance: **2018 Conceptual Framework** chapters 1–8 + Status/Purpose + Appendices + **Basis for Conclusions**
- Authority: **ARCHIVE / HK twin** (same 2018 substance; prefer 0b for quotes)
- Copyright: teach/summarise only — never paste verbatim

### 1. Deloitte (DTT) — A2 Conceptual framework for financial reporting (DART Volume A)
- File: `inputs/cf-2018/dtt-2022-conceptual-framework-moa.pdf` (9 pages)
- PDF stamp: **2022-06-21** — covers **2018 CF** vs 2010
- Use: content + illustrations summary; copyrighted reference only

### Still needed (preferred before unlock)
- [ ] KPMG CF refs (structure/visuals)
- [ ] PwC CF FAQ-style
- [ ] EY CF / relevant GAAP chapter slices


## IGNORE
- Any `HKAS/` subfolder files from PwC MOA folder — Johnny: ignore entirely.
- Structure v0 **APPROVED** 2026-09-26; map **v2.1 APPROVED** 2026-09-27; homepage **v0.1 LOCKED**.
- Phase B: rough sub-page skeletons — see `SUBPAGE-SKELETON-BRIEF.md`.

## Lock stamp

Per-page QC vs canon Versions: see [`LOCK-STAMP.md`](LOCK-STAMP.md).

## Site chapter scheme (2026.09.27-7)

Teaching chapters **Ch1–Ch9** (Objective … Status); Overview **retired**. Aligns official CF Chapters 1–8 + Status as site Ch9. See `subpages/INDEX.md` + `LOCK-STAMP.md`.


## Sticky chrome (single-source)

Config: [`chrome.json`](chrome.json) (pack title, Home, chapter tags).

After chapter add/renumber, edit `chrome.json` then regenerate:

```bash
node tools/generate-chrome.mjs cf-2018
```

See [`tools/README.md`](../../tools/README.md). Targets: `draft-v1-linked/` Map + chapters only (not `visuals/`, `_archive*`).

## Site chrome (2026.09.28-1)

Homepage Open dual-path locked: READY Open → `../<pack>/preview/index.html` + `refs/<pack>/preview` → `draft-v1-linked`. See root `FOLDER-RULES.md` / `PRODUCT-SPEC.md`.
