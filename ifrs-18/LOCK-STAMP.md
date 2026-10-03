# IFRS 18 — LOCK-STAMP

**Pack:** IFRS 18 Presentation and Disclosure  
**Owner:** IFRS Website PM / QC  
**Stamp scheme:** `YYYY.MM.DD-N` (Johnny-signed lean versioning — not semver)  
**Created:** 2026-09-27 (Asia/Shanghai)

## Canon Versions currently in force

| Canon | Path | Version |
|-------|------|---------|
| visual_types | `VISUAL-TYPES.md` | **2026.09.27-8** |
| product_spec | `PRODUCT-SPEC.md` | **2026.09.28-1** |
| qc_checklist | `QC-CHECKLIST.md` | **2026.09.28-1** |
| skill | `ifrs-visual-grammar` | **2026.09.27-8** |

Skill frontmatter: `version: 2026.09.27-8` · `depends_on: VISUAL-TYPES 2026.09.27-8`.

## Honesty note (2026-09-28 · stamp 2026.09.27-8 · chrome + Home depth)

Link-audit QC **PASS** (2026-09-28 ~11:08 Asia/Shanghai) under canon **2026.09.27-8**. Chrome single-source LIVE (`refs/ifrs-18/chrome.json` + `tools/generate-chrome.mjs`); sticky/Home match generate. `_review/homepage` → `refs/homepage` junction; Home resolves from BOTH `refs/.../draft-v1-linked/` AND `_review/ifrs-18/preview/`. Prior P1/P2 visuals + Map·1…8 held. **All Map + Ch1–Ch8 `current`**. Homepage READY unchanged.

**Review unit:** `_review/ifrs-18/preview` → `../../refs/ifrs-18/draft-v1-linked`.

## Site chrome note (2026.09.28-1 · homepage Open dual-path)

Homepage READY Open hrefs now use `../<pack>/preview/index.html`; `refs/<pack>/preview` → `draft-v1-linked` so Open resolves from BOTH `refs/homepage/` and `_review/homepage/`. Product-spec / QC bumped to **2026.09.28-1** for this site-chrome lock. **Do not mass-restamp chapter rows** — chapter visuals/content unchanged; page stamps remain at 2026.09.27-8 until next chapter QC. Homepage READY status **unchanged**.

## Page stamp table

A row is **`current` only if** all four Version columns equal the in-force Versions above.

| page | visual_types | product_spec | qc_checklist | skill | status | last_qc | notes |
|------|--------------|--------------|--------------|-------|--------|---------|-------|
| Map (`index.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | chrome.json; Home dual-path |
| Ch1 (`ch01.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | what’s-new visual held |
| Ch2 (`ch02.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | P0 PFS aggregation |
| Ch3 (`ch03.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | P0 P&L categories |
| Ch4 (`ch04.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | P0 totals/subtotals |
| Ch5 (`ch05.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | nature∥function∥mixed |
| Ch6 (`ch06.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | P0 MPMs |
| Ch7 (`ch07.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | thin bridges + SCF |
| Ch8 (`ch08.html`) | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | 2026.09.27-8 | current | 2026-09-28 · link-audit PASS | transition timeline |

**Summary:** 9 rows · **9 current** · **0 stale** · **0 unreviewed** · homepage READY **unchanged**

`status` values: `current` | `stale` | `unreviewed`

When a page is freshly QC’d under the in-force Versions, set all four Version columns to those Version strings, `status=current`, and `last_qc` = date + scope. PASS against an older stamp (any column lag) = still **stale → re-QC required**.
