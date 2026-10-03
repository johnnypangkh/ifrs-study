# #5 IFRS 18 Cite apply — KEY CHANGES (2026-10-03)

**Job:** #5 Cite apply only (Johnny approved 2026-10-03). Brief `BRIEF-5-CITE-APPLY-2026-10-03.md`.
**Scope held:** cite chips + References row only. No densify rewrite, no invent, no chrome / CSS / Map / visuals edits. **S1 HOLD** (nothing done). **S3** not retouched (#7b3 owns point-chip CSS). PwC still missing (no invent).

## Base pages

Edited the four pages from `i18-cite-pages.tgz` (`ch01.html`, `ch03.html`, `ch07.html`, `references.html`). They carry Johnny's newer chrome (`chrome.css?v=7e-tag-bar-20261003`, `draft.css?v=7b3-pointchip-wrap-20261003`, visual `?v=7b1…` / `map-orphan-para-20261003`, no "scroll tags →" span). Teaching body was byte-identical to the Opus live pack, so the bundle chrome is kept as delivered. Only `.cite` spans changed (verified: after stripping chips, page text is identical to the bundle; References adds one row + one intro chip).

## Attach checklist (this run)

| Source | Status | Use |
|---|---|---|
| Official IFRS 18 | on disk in HTML — not re-attached | Q1 / Q2a locators already evidenced in pack (B45–B48 read at Gate 1; body 3.7.8 already `IFRS 18 · Figure 5`) |
| EY iGAAP 2026 Ch04 | **ATTACHED** (112 pp; md5 `0613da32…` = same file used at densify gates) | Q3 — full text scanned (contents, Appendix A Illustrations, Appendix B FAQs, all section bodies 1–6) |
| EY Closer look / KPMG FI / DTT A4 | on disk — not attached | locator fixes only (DTT 1.1 / 8.1 headings confirmed from on-disk text extract; no new substance) |
| PwC | missing | unchanged |

## Q1 / Q2 / Q4 — locator fixes

| ID | Page · place | Before | After |
|---|---|---|---|
| Q1 | ch03 `#s-3-9-ey` index, EY Ill 3-1 row (Entity C) | `IFRS 18 · para B… returns test` | `IFRS 18 · para B45–B48` |
| Q2a | ch03 `#s-3-9-ey` index, EY Ill 3-8 row | `IFRS 18 · para IE Figure 5` | `IFRS 18 · Figure 5` (= body 3.7.8) |
| Q2b | ch01 1.3.5 (`#s-1-3-ex`, `<q>` "Although companies' net profit…") | `KPMG FI 2024` | `KPMG FI 2024 · Foreword` |
| Q4 | ch01 1.0 "What IAS 1 covered" bullet | `DTT A4 2022 · IAS 1 bridge` | `DTT A4 2022 · 1.1` (Overview of IAS 1 — text matches DTT 1.1) |
| Q4 | ch01 1.0 Pitfall point-chip | `DTT A4 2022 · IAS 1 bridge` | `DTT A4 2022 · 1.1` |
| Q4 | ch07 7.0 (`#s-7-0`) "IAS 1 bridge" bullet (old vs new comparison) | `DTT A4 2022 · IAS 1 bridge` | `DTT A4 2022 · 8.1` (Replacement of IAS 1 — ED/2019/7) |

References: KPMG / EY Closer look / DTT short-form title chips left as short form (brief). DTT full name left as is (title correction "Manual of Accounting" → DART Vol A was part of old Ask A4 but not in the #5 approval — still open).

## Q3 — EY iGAAP 2026 Ch04 chips

**Result:** **187** iGAAP chips added (**94** distinct locators) — ch01 **21**, ch03 **130**, ch07 **36**. Every one sits immediately after an existing `EY Closer look 2026 · …` chip on the same unit (C1 title / C2 end-of-unit placement inherited). **No new prose, no new unit, no iGAAP-only content.** References: new row `EY International GAAP 2026 — Chapter 4: Presentation and disclosure in financial statements – IFRS 18 and IFRS 19` | `EY iGAAP 2026 Ch04`; intro chip list updated. METHOD chip grammar + pre-flight row added.

Chip HTML: `<span class="cite cite-ey"><span class="cite-house">EY</span> iGAAP 2026 Ch04 · section 3.2.1.B</span>` (shapes: `section X`, `Ill N-N`, `Ill N-N / section X`, `section X · QN-N` — mirrors the Closer look chip it sits beside).

### Match rule ("only where iGAAP matches")

1. **Illustrations / FAQs — pair by identical title, then body.** iGAAP numbers ≠ Closer look numbers. Duplicate FAQ titles (general 3.2 vs specified-MBA 3.3 copies) paired in order. Then body text compared: **≥ 0.85 of the Closer look body found in iGAAP = match**; below = partial → no chip.
2. **Sections — map, then test the unit.** Same number + same title; else same title renumbered within the same parent (e.g. CL 3.2.1.F ↔ iG 3.2.1.B; CL 3.3.3.G–K ↔ iG 3.3.3.A–E; CL 3.3.2.C ↔ iG 3.3.2.B; CL 3.3.1.C ↔ iG 3.3.1.A; CL 3.2.1.H ↔ iG 3.2.1.D); subject overrides CL 3.2.1.B ↔ iG 3.2.1.A (equity-method investees), CL 3.2.6.C ↔ iG 3.2.6.C, CL 3.3.2.A ↔ iG 3.3.2.A; else iGAAP parent section (CL 3.2.1.A/D/E/G → iG 3.2.1; CL 3.3.1.A/B → iG 3.3.1; CL 3.3.3.A–F → iG 3.3.3). Then the chip's teaching unit (li / tr / p / whole Illustration for title chips; cite-only rows use the preceding block) is scored: share of its content words found in the iGAAP section vs the Closer look section.
   - iGAAP section near-identical to Closer look (≥ 0.85 of CL section text): add if iGAAP unit score ≥ 0.9 × CL score.
   - iGAAP section materially smaller: add only if CL score ≥ 0.5 **and** iGAAP score ≥ CL score.
3. **Manual read** of every addition with CL score < 0.45 and spot reads in the smaller sections (3.2.1, 3.2.4, 3.2.7, 3.2.8.B, 3.3.2) — claims found verbatim in iGAAP. One demoted (below).
4. Chapter "Overview", Appendix C (banks), Figure 3-6 and Ill C.x chips: **no iGAAP counterpart → skipped** (45 chips).

### Illustration / FAQ pairs used on these pages

| Closer look | iGAAP Ch04 | Body match | Note |
|---|---|---|---|
| Ill 3-2 | Ill 3-1 | 0.99 | Entity P both |
| Ill 3-3 | Ill 3-2 | 0.91 | entity letter B (CL) vs A (iG) |
| Ill 3-4 | Ill 3-3 | 0.99 | |
| Ill 3-5 | Ill 3-4 | 0.84 | only diff = CL footnote 14 (IFRS 3.42); facts + conclusion identical — accepted |
| Ill 3-6 | Ill 3-5 | 0.98 | Entity G (CL) vs Entity A (iG) |
| Ill 3-9 | Ill 3-6 | 0.87 | CL adds footnote 23 (IFRS 18.60) |
| Ill 3-10 | Ill 3-7 | 0.96 | Entity R (CL) vs Entity A (iG) |
| Ill 3-12 | Ill 3-8 | 0.89 | CL adds IFRS 18.24 / BC367 note; facts + conclusion identical |
| Ill 5-1 / 5-2 / 5-3 | Ill 5-1 / 5-2 / 5-3 | 0.94 / 0.98 / 0.97 | Ill 5-3 Entity E (CL) vs A (iG) |
| Q3-1 / Q3-2 / Q3-3 / Q3-5 | Q3-3 / Q3-4 / Q3-5 / Q3-7 | 0.94–0.99 | general (3.2) copies |
| Q3-9 / Q3-11 / Q3-12 / Q3-13 / Q3-14 / Q3-16 / Q3-17 / Q3-18 / Q3-19 | Q3-6 / Q3-8 / Q3-9 / Q3-10 / Q3-11 / Q3-12 / Q3-13 / Q3-14 / Q3-15 | 0.92–1.00 | Q3-12 title adds "voluntarily" — body 0.92 |
| Q3-25 / Q3-27 / Q3-28 / Q3-29 / Q3-30 | Q3-18 / Q3-20 / Q3-21 / Q3-22 / Q3-23 | 0.91–1.00 | specified-MBA (3.3) copies |
| Q3-35 / Q3-36 / Q3-37 / Q3-40 | Q3-24 / Q3-25 / Q3-26 / Q3-27 | 0.98–0.99 | Q3-36 title "Do" vs "Does" |
| Q5-1 / Q5-2 | Q5-1 / Q5-2 | 1.00 / 0.86 | |

**Partial (no chip):** Q3-6 ↔ iG Q3-1 (0.68 — CL adds Entity L facts), Q3-8 ↔ iG Q3-2 (0.22 — CL adds Entity R/S), Q3-21 ↔ iG Q3-16 (0.27 — CL adds IFRS IC March 2026), Q3-24 ↔ iG Q3-17 (0.21), Q3-26 ↔ iG Q3-19 (0.40). (Off-page: Q2-2 0.59, Ill 6-1 0.67.)
**Closer look only (no chip):** Ill 3-1, 3-7, 3-8, 3-11; Q3-4, 3-7, 3-10, 3-15, 3-20, 3-22, 3-23, 3-31, 3-32, 3-33, 3-34, 3-38, 3-39, 3-41, 3-43; all Appendix C.

### Rejections (64) by reason

- Section coverage below rule: 33 (mostly CL-expanded sections 3.2.1.D/E, 3.2.6.C parent, 3.2.7, 3.3.1.A/B, 3.3.3.E/F, 3.3.5; ch01 two section 1.2 rows — iGAAP 1.2 lacks the para 12 extract).
- Closer-look-only Illustration / FAQ: 21. Partial FAQ: 9.
- Manual: 1 — ch03 `#s-3-1` Concept-insight point-chip ("investing ≠ IAS 7 investing activities"): claim not found in Closer look 3.1 **or** iGAAP 3.1 → no iGAAP chip. **Flag:** the pre-existing `EY Closer look 2026 · section 3.1` chip on that point-chip looks weak — left unchanged (out of #5 scope).

### Not done (scope)

- **ch02, ch04, ch05, ch06, ch08, index**: not in the #5 page bundle → no iGAAP chips there. Not edited so Johnny's newer chrome on those pages is not overwritten by older Opus copies. Same method applies when those pages are sent (candidates: Ch2 Ill 2-1/2-2, Q2-1, section 2.x; Ch4–Ch6 section 3.4.x / 4.x / Q4-1–Q4-5, Ill 3-13 ↔ iG 3-9, Ill 4-1; Ch8 section 6.1).
- **Last update stamp not bumped.** Chrome design: one pack-wide value per release wave, set by chrome owner — pages still read `2026-10-02 20:16 HKT`. Bot/chrome: set the #5 release stamp pack-wide when syncing.

## QA (teaching-body QA skill)

- HTML balanced (4 pages); no duplicate ids; all in-page + cross-chapter anchors resolve (10 pages).
- Zero house-only Big4 chips; zero `§` in any `.cite`; Official `para` / `Figure`; EY `section`.
- Every chip work prefix on ch01–ch08 is listed in References (incl. `EY iGAAP 2026 Ch04`).
- Locked strings gone pack-wide: `para B… returns test` 0, `para IE Figure 5` 0, bare `KPMG FI 2024` in chapters 0, `IAS 1 bridge` chip 0.
- Every iGAAP section locator exists in the iGAAP Ch04 text; every Ill/Q locator is a paired item above.
- Non-chip page text identical to bundle; screenshots: `j5-ch03-index.png`, `j5-ch03-illus.png`, `j5-ch07-eps.png`, `j5-ch01-dtt.png`, `j5-references.png`.

## Files in `/opt/cursor/artifacts/5-cite-apply-20261003.tgz`

`ch01.html`, `ch03.html`, `ch07.html`, `references.html`, `5-CITE-APPLY-KEY-CHANGES-2026-10-03.md`, `IFRS18-CONTENT-REWRITE-METHOD.md`, `OPUS-WORKING-MEMORY.md`.

---

## Appendix A — iGAAP chips added (distinct, with count and section anchors)

| Page | Closer look chip | iGAAP chip added | n | Anchors |
|---|---|---|---|---|
| ch01 | `EY Closer look 2026 · section 1.1` | `EY iGAAP 2026 Ch04 · section 1.1` | 5 | s-1-0 |
| ch01 | `EY Closer look 2026 · section 1` | `EY iGAAP 2026 Ch04 · section 1` | 8 | s-1-1, s-1-2, s-1-2-1, s-1-3, s-1-3-3 |
| ch01 | `EY Closer look 2026 · section 1.3` | `EY iGAAP 2026 Ch04 · section 1.3` | 2 | s-1-3-4 |
| ch01 | `EY Closer look 2026 · section 1.2` | `EY iGAAP 2026 Ch04 · section 1.2` | 6 | s-1-3-4 |
| ch03 | `EY Closer look 2026 · section 3.2` | `EY iGAAP 2026 Ch04 · section 3.2` | 1 | s-3-0 |
| ch03 | `EY Closer look 2026 · section 3.3` | `EY iGAAP 2026 Ch04 · section 3.3` | 1 | s-3-0 |
| ch03 | `EY Closer look 2026 · section 3.2.3` | `EY iGAAP 2026 Ch04 · section 3.2.3` | 3 | s-3-1, s-3-2 |
| ch03 | `EY Closer look 2026 · section 3.2.2` | `EY iGAAP 2026 Ch04 · section 3.2.2` | 2 | s-3-1, s-3-4 |
| ch03 | `EY Closer look 2026 · section 3.2.4` | `EY iGAAP 2026 Ch04 · section 3.2.4` | 3 | s-3-1, s-3-6 |
| ch03 | `EY Closer look 2026 · section 3.2.5` | `EY iGAAP 2026 Ch04 · section 3.2.5` | 3 | s-3-1, s-3-6 |
| ch03 | `EY Closer look 2026 · section 3.1.1` | `EY iGAAP 2026 Ch04 · section 3.1.1` | 2 | s-3-1, s-3-4 |
| ch03 | `EY Closer look 2026 · section 3.1` | `EY iGAAP 2026 Ch04 · section 3.1` | 1 | s-3-1 |
| ch03 | `EY Closer look 2026 · section 3.2.3.A` | `EY iGAAP 2026 Ch04 · section 3.2.3.A` | 5 | s-3-2-2 |
| ch03 | `EY Closer look 2026 · section 3.2.3.A · Q3-18` | `EY iGAAP 2026 Ch04 · section 3.2.3.A · Q3-14` | 1 | s-3-2-2 |
| ch03 | `EY Closer look 2026 · section 3.2.3 · Q3-13` | `EY iGAAP 2026 Ch04 · section 3.2.3 · Q3-10` | 1 | s-3-2-3 |
| ch03 | `EY Closer look 2026 · section 3.2.3 · Q3-14` | `EY iGAAP 2026 Ch04 · section 3.2.3 · Q3-11` | 1 | s-3-2-3 |
| ch03 | `EY Closer look 2026 · section 3.2.3 · Q3-16` | `EY iGAAP 2026 Ch04 · section 3.2.3 · Q3-12` | 1 | s-3-2-3 |
| ch03 | `EY Closer look 2026 · section 3.2.3 · Q3-17` | `EY iGAAP 2026 Ch04 · section 3.2.3 · Q3-13` | 1 | s-3-2-3 |
| ch03 | `EY Closer look 2026 · Ill 3-4 / section 3.2.3` | `EY iGAAP 2026 Ch04 · Ill 3-3 / section 3.2.3` | 1 | s-3-2-ex |
| ch03 | `EY Closer look 2026 · section 3.2.1.A` | `EY iGAAP 2026 Ch04 · section 3.2.1` | 2 | s-3-3-1 |
| ch03 | `EY Closer look 2026 · section 3.2.1.F` | `EY iGAAP 2026 Ch04 · section 3.2.1.B` | 4 | s-3-3-1, s-3-3-7 |
| ch03 | `EY Closer look 2026 · section 3.2.1.A · Q3-1` | `EY iGAAP 2026 Ch04 · section 3.2.1 · Q3-3` | 1 | s-3-3-1 |
| ch03 | `EY Closer look 2026 · section 3.2.1.B` | `EY iGAAP 2026 Ch04 · section 3.2.1.A` | 4 | s-3-3-2 |
| ch03 | `EY Closer look 2026 · section 3.2.1.B · Q3-3` | `EY iGAAP 2026 Ch04 · section 3.2.1.A · Q3-5` | 1 | s-3-3-2 |
| ch03 | `EY Closer look 2026 · section 3.2.1.C` | `EY iGAAP 2026 Ch04 · section 3.2.1.C` | 1 | s-3-3-3 |
| ch03 | `EY Closer look 2026 · section 3.2.1.C · Q3-5` | `EY iGAAP 2026 Ch04 · section 3.2.1.C · Q3-7` | 1 | s-3-3-3 |
| ch03 | `EY Closer look 2026 · section 3.2.1.D` | `EY iGAAP 2026 Ch04 · section 3.2.1` | 2 | s-3-3-4 |
| ch03 | `EY Closer look 2026 · section 3.3.2.C · Q3-25` | `EY iGAAP 2026 Ch04 · section 3.3.2.B · Q3-18` | 2 | s-3-3-6, s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.2.1.F · Q3-9` | `EY iGAAP 2026 Ch04 · section 3.2.1.B · Q3-6` | 1 | s-3-3-7 |
| ch03 | `EY Closer look 2026 · Ill 3-2 / section 3.2.1.F` | `EY iGAAP 2026 Ch04 · Ill 3-1 / section 3.2.1.B` | 1 | s-3-3-ex2 |
| ch03 | `EY Closer look 2026 · section 3.2.1.G` | `EY iGAAP 2026 Ch04 · section 3.2.1` | 1 | s-3-3-9 |
| ch03 | `EY Closer look 2026 · section 3.2.1.H` | `EY iGAAP 2026 Ch04 · section 3.2.1.D` | 1 | s-3-3-9 |
| ch03 | `EY Closer look 2026 · section 3.2.2.A` | `EY iGAAP 2026 Ch04 · section 3.2.2.A` | 2 | s-3-4-1 |
| ch03 | `EY Closer look 2026 · section 3.2.2.B` | `EY iGAAP 2026 Ch04 · section 3.2.2.B` | 4 | s-3-4-2 |
| ch03 | `EY Closer look 2026 · section 3.2.2.C` | `EY iGAAP 2026 Ch04 · section 3.2.2.C` | 1 | s-3-4-3 |
| ch03 | `EY Closer look 2026 · Ill 3-3 / section 3.2.2.C` | `EY iGAAP 2026 Ch04 · Ill 3-2 / section 3.2.2.C` | 1 | s-3-4-ex |
| ch03 | `EY Closer look 2026 · section 3.2.2.D` | `EY iGAAP 2026 Ch04 · section 3.2.2.D` | 3 | s-3-4-fig4 |
| ch03 | `EY Closer look 2026 · section 3.3.5.B` | `EY iGAAP 2026 Ch04 · section 3.3.5.B` | 1 | s-3-4-7 |
| ch03 | `EY Closer look 2026 · section 3.3.6` | `EY iGAAP 2026 Ch04 · section 3.3.6` | 1 | s-3-4-7 |
| ch03 | `EY Closer look 2026 · section 3.1.2` | `EY iGAAP 2026 Ch04 · section 3.1.2` | 1 | s-3-5-mba |
| ch03 | `EY Closer look 2026 · section 3.3.1` | `EY iGAAP 2026 Ch04 · section 3.3.1` | 2 | s-3-5-2 |
| ch03 | `EY Closer look 2026 · section 3.3.1.B` | `EY iGAAP 2026 Ch04 · section 3.3.1` | 1 | s-3-5-2 |
| ch03 | `EY Closer look 2026 · section 3.3.1.C` | `EY iGAAP 2026 Ch04 · section 3.3.1.A` | 1 | s-3-5-3 |
| ch03 | `EY Closer look 2026 · section 3.3.1.A` | `EY iGAAP 2026 Ch04 · section 3.3.1` | 1 | s-3-5-5 |
| ch03 | `EY Closer look 2026 · section 3.3.2` | `EY iGAAP 2026 Ch04 · section 3.3.2` | 2 | s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.3.2.A` | `EY iGAAP 2026 Ch04 · section 3.3.2.A` | 1 | s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.3.2.C` | `EY iGAAP 2026 Ch04 · section 3.3.2.B` | 1 | s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.3.2.C · Q3-27` | `EY iGAAP 2026 Ch04 · section 3.3.2.B · Q3-20` | 2 | s-3-5-9, s-3-7-1 |
| ch03 | `EY Closer look 2026 · section 3.3.2.C · Q3-28` | `EY iGAAP 2026 Ch04 · section 3.3.2.B · Q3-21` | 1 | s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.3.2.C · Q3-29` | `EY iGAAP 2026 Ch04 · section 3.3.2.B · Q3-22` | 1 | s-3-5-9 |
| ch03 | `EY Closer look 2026 · section 3.3.3.B` | `EY iGAAP 2026 Ch04 · section 3.3.3` | 2 | s-3-5-11 |
| ch03 | `EY Closer look 2026 · section 3.3.3.C` | `EY iGAAP 2026 Ch04 · section 3.3.3` | 1 | s-3-5-11 |
| ch03 | `EY Closer look 2026 · section 3.3.3.D` | `EY iGAAP 2026 Ch04 · section 3.3.3` | 1 | s-3-5-11 |
| ch03 | `EY Closer look 2026 · Ill 3-9 / section 3.3.3.C` | `EY iGAAP 2026 Ch04 · Ill 3-6 / section 3.3.3` | 1 | s-3-5-ex3 |
| ch03 | `EY Closer look 2026 · Ill 3-10` | `EY iGAAP 2026 Ch04 · Ill 3-7` | 2 | s-3-8-ey, s-3-9-ey |
| ch03 | `EY Closer look 2026 · section 3.3.3.G` | `EY iGAAP 2026 Ch04 · section 3.3.3.A` | 1 | s-3-5-15 |
| ch03 | `EY Closer look 2026 · section 3.3.3.H` | `EY iGAAP 2026 Ch04 · section 3.3.3.B` | 1 | s-3-5-15 |
| ch03 | `EY Closer look 2026 · section 3.3.3.I` | `EY iGAAP 2026 Ch04 · section 3.3.3.C` | 2 | s-3-5-15, s-3-7 |
| ch03 | `EY Closer look 2026 · section 3.3.3.J` | `EY iGAAP 2026 Ch04 · section 3.3.3.D` | 2 | s-3-5-15, s-3-7 |
| ch03 | `EY Closer look 2026 · section 3.3.3.K` | `EY iGAAP 2026 Ch04 · section 3.3.3.E` | 2 | s-3-5-15, s-3-7 |
| ch03 | `EY Closer look 2026 · section 3.3.4 · Q3-35` | `EY iGAAP 2026 Ch04 · section 3.3.4 · Q3-24` | 1 | s-3-5-fig33 |
| ch03 | `EY Closer look 2026 · section 3.3.4 · Q3-37` | `EY iGAAP 2026 Ch04 · section 3.3.4 · Q3-26` | 1 | s-3-5-fig33 |
| ch03 | `EY Closer look 2026 · section 3.3.4` | `EY iGAAP 2026 Ch04 · section 3.3.4` | 1 | s-3-5-fig33 |
| ch03 | `EY Closer look 2026 · section 3.3.4 · Q3-36` | `EY iGAAP 2026 Ch04 · section 3.3.4 · Q3-25` | 1 | s-3-5-fig33 |
| ch03 | `EY Closer look 2026 · section 3.3.5.A` | `EY iGAAP 2026 Ch04 · section 3.3.5.A` | 1 | s-3-5-insurers |
| ch03 | `EY Closer look 2026 · section 3.3.5.A · Q3-40` | `EY iGAAP 2026 Ch04 · section 3.3.5.A · Q3-27` | 1 | s-3-5-insurers |
| ch03 | `EY Closer look 2026 · Ill 3-12 / section 3.3.5.A` | `EY iGAAP 2026 Ch04 · Ill 3-8 / section 3.3.5.A` | 1 | s-3-5-ex5 |
| ch03 | `EY Closer look 2026 · section 3.2.6.C` | `EY iGAAP 2026 Ch04 · section 3.2.6.C` | 4 | s-3-6, s-3-7-3 |
| ch03 | `EY Closer look 2026 · section 3.2.6` | `EY iGAAP 2026 Ch04 · section 3.2.6` | 3 | s-3-7, s-3-7-1 |
| ch03 | `EY Closer look 2026 · section 3.2.6.A · Q3-19` | `EY iGAAP 2026 Ch04 · section 3.2.6.A · Q3-15` | 2 | s-3-7-1 |
| ch03 | `EY Closer look 2026 · section 3.2.6.B` | `EY iGAAP 2026 Ch04 · section 3.2.6.B` | 1 | s-3-7-1 |
| ch03 | `EY Closer look 2026 · Ill 3-5 / section 3.2.6` | `EY iGAAP 2026 Ch04 · Ill 3-4 / section 3.2.6` | 1 | s-3-7-ex |
| ch03 | `EY Closer look 2026 · section 3.2.6.A` | `EY iGAAP 2026 Ch04 · section 3.2.6.A` | 1 | s-3-7-3 |
| ch03 | `EY Closer look 2026 · Ill 3-6 / section 3.2.6.C` | `EY iGAAP 2026 Ch04 · Ill 3-5 / section 3.2.6.C` | 1 | s-3-7-ex2 |
| ch03 | `EY Closer look 2026 · section 3.2.7` | `EY iGAAP 2026 Ch04 · section 3.2.7` | 3 | s-3-7-5 |
| ch03 | `EY Closer look 2026 · section 3.2.7.A` | `EY iGAAP 2026 Ch04 · section 3.2.7.A` | 1 | s-3-7-5 |
| ch03 | `EY Closer look 2026 · section 3.2.8` | `EY iGAAP 2026 Ch04 · section 3.2.8` | 2 | s-3-5-fig5 |
| ch03 | `EY Closer look 2026 · section 3.2.8.A` | `EY iGAAP 2026 Ch04 · section 3.2.8.A` | 2 | s-3-5-fig5 |
| ch03 | `EY Closer look 2026 · section 3.2.8.B` | `EY iGAAP 2026 Ch04 · section 3.2.8.B` | 2 | s-3-5-fig5 |
| ch03 | `EY Closer look 2026 · section 3.2.8.C` | `EY iGAAP 2026 Ch04 · section 3.2.8.C` | 1 | s-3-5-fig5 |
| ch03 | `EY Closer look 2026 · section 3.2.8.D` | `EY iGAAP 2026 Ch04 · section 3.2.8.D` | 1 | s-3-5-fig5 |
| ch03 | `EY Closer look 2026 · Ill 3-2` | `EY iGAAP 2026 Ch04 · Ill 3-1` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-3` | `EY iGAAP 2026 Ch04 · Ill 3-2` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-4` | `EY iGAAP 2026 Ch04 · Ill 3-3` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-5` | `EY iGAAP 2026 Ch04 · Ill 3-4` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-6` | `EY iGAAP 2026 Ch04 · Ill 3-5` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-9` | `EY iGAAP 2026 Ch04 · Ill 3-6` | 1 | s-3-9-ey |
| ch03 | `EY Closer look 2026 · Ill 3-12` | `EY iGAAP 2026 Ch04 · Ill 3-8` | 1 | s-3-9-ey |
| ch07 | `EY Closer look 2026 · section 5` | `EY iGAAP 2026 Ch04 · section 5` | 2 | s-7-0 |
| ch07 | `EY Closer look 2026 · section 5.1` | `EY iGAAP 2026 Ch04 · section 5.1` | 12 | s-7-0-1, s-7-1, s-7-1-1, s-7-1-2, s-7-1-ex |
| ch07 | `EY Closer look 2026 · section 5.3` | `EY iGAAP 2026 Ch04 · section 5.3` | 9 | s-7-0-1, s-7-3, s-7-3-1, s-7-3-ex |
| ch07 | `EY Closer look 2026 · section 5.4` | `EY iGAAP 2026 Ch04 · section 5.4` | 5 | s-7-0-1, s-7-4, s-7-4-1 |
| ch07 | `EY Closer look 2026 · section 5.2` | `EY iGAAP 2026 Ch04 · section 5.2` | 1 | s-7-0-1 |
| ch07 | `EY Closer look 2026 · Ill 5-1 / section 5.1` | `EY iGAAP 2026 Ch04 · Ill 5-1 / section 5.1` | 1 | s-7-1-ey |
| ch07 | `EY Closer look 2026 · section 2` | `EY iGAAP 2026 Ch04 · section 2` | 1 | s-7-2 |
| ch07 | `EY Closer look 2026 · section 5.3 · Q5-1` | `EY iGAAP 2026 Ch04 · section 5.3 · Q5-1` | 1 | s-7-3 |
| ch07 | `EY Closer look 2026 · section 5.3 · Q5-2` | `EY iGAAP 2026 Ch04 · section 5.3 · Q5-2` | 1 | s-7-3-1 |
| ch07 | `EY Closer look 2026 · Ill 5-2` | `EY iGAAP 2026 Ch04 · Ill 5-2` | 1 | s-7-3-ey |
| ch07 | `EY Closer look 2026 · Ill 5-3` | `EY iGAAP 2026 Ch04 · Ill 5-3` | 1 | s-7-3-ey |
| ch07 | `EY Closer look 2026 · section 4.2.2` | `EY iGAAP 2026 Ch04 · section 4.2.2` | 1 | s-7-4 |

## Appendix B — Closer look chips with no iGAAP chip (rejected)

| Page | Anchor | Closer look chip | Why no iGAAP chip |
|---|---|---|---|
| ch01 | s-1-3-4 | `section 1.2` | section 1.2->1.2 (number+title, section-text match 0.86) unit coverage iG 0.33 vs CL 0.42 |
| ch01 | s-1-3-4 | `section 1.2` | section 1.2->1.2 (number+title, section-text match 0.86) unit coverage iG 0.59 vs CL 0.76 |
| ch03 | s-3-1 | `section 3.1.1` | section 3.1.1->3.1.1 (number+title, section-text match 0.75) unit coverage iG 0.65 vs CL 0.76 |
| ch03 | s-3-1 | `section 3.1` | section 3.1->3.1 (number+title, section-text match 0.87) unit coverage iG 0.07 vs CL 0.00 |
| ch03 | s-3-1 | `section 3.2.1` | section 3.2.1->3.2.1 (number+title, section-text match 0.27) unit coverage iG 0.65 vs CL 0.40 |
| ch03 | s-3-2 | `section 3.2.3` | section 3.2.3->3.2.3 (number+title, section-text match 0.82) unit coverage iG 0.44 vs CL 0.44 |
| ch03 | s-3-2-3 | `section 3.2.3 · Q3-15` | Q3-15 Closer look only; section 3.2.3->3.2.3 (number+title, section-text match 0.82) unit coverage iG 0.50 vs CL 0.95 |
| ch03 | s-3-3 | `section 3.2.1` | section 3.2.1->3.2.1 (number+title, section-text match 0.27) unit coverage iG 0.70 vs CL 0.80 |
| ch03 | s-3-3 | `section 3.2.1` | section 3.2.1->3.2.1 (number+title, section-text match 0.27) unit coverage iG 0.38 vs CL 0.77 |
| ch03 | s-3-3 | `section 3.2.1` | section 3.2.1->3.2.1 (number+title, section-text match 0.27) unit coverage iG 0.54 vs CL 0.25 |
| ch03 | s-3-3 | `section 3.1` | manual review: point-chip claim (P&L investing ≠ IAS 7 investing activities) not found in Closer look 3.1 or iGAAP 3.1 — no iGAAP chip; pre-existing CL chip flagged |
| ch03 | s-3-3-3 | `section 3.2.1.C` | section 3.2.1.C->3.2.1.C (number+title, section-text match 0.48) unit coverage iG 0.69 vs CL 0.85 |
| ch03 | s-3-3-3 | `section 3.2.1.C · Q3-4` | Q3-4 Closer look only; section 3.2.1.C->3.2.1.C (number+title, section-text match 0.48) unit coverage iG 0.09 vs CL 0.73 |
| ch03 | s-3-3-4 | `section 3.2.1.D` | section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.36 vs CL 0.71 |
| ch03 | s-3-3-4 | `section 3.2.1.D` | section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.53 vs CL 0.74 |
| ch03 | s-3-3-4 | `section 3.2.1.D` | section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.85 vs CL 0.95 |
| ch03 | s-3-3-4 | `section 3.2.1.D` | section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.62 vs CL 0.94 |
| ch03 | s-3-3-4 | `section 3.2.1.D` | section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.57 vs CL 0.91 |
| ch03 | s-3-3-ex | `Ill 3-1 / section 3.2.1.D` | Ill 3-1 Closer look only; section 3.2.1.D->3.2.1 (parent fallback, section-text match 0.26) unit coverage iG 0.36 vs CL 0.86 |
| ch03 | s-3-3-6 | `section 3.2.1.E · Q3-6` | Q3-6 partial match only (iGAAP Q3-1); section 3.2.1.E->3.2.1 (parent fallback, section-text match 0.31) unit coverage iG 0.62 vs CL 0.88 |
| ch03 | s-3-3-6 | `section 3.2.1.E · Q3-7` | Q3-7 Closer look only; section 3.2.1.E->3.2.1 (parent fallback, section-text match 0.31) unit coverage iG 0.41 vs CL 0.71 |
| ch03 | s-3-3-6 | `section 3.2.1.E · Q3-8` | Q3-8 partial match only (iGAAP Q3-2); section 3.2.1.E->3.2.1 (parent fallback, section-text match 0.31) unit coverage iG 0.65 vs CL 0.87 |
| ch03 | s-3-3-6 | `section 3.2.1.E · Q3-8` | Q3-8 partial match only (iGAAP Q3-2); section 3.2.1.E->3.2.1 (parent fallback, section-text match 0.31) unit coverage iG 0.74 vs CL 0.89 |
| ch03 | s-3-4-1 | `section 3.2.2.A` | section 3.2.2.A->3.2.2.A (number+title, section-text match 0.68) unit coverage iG 0.84 vs CL 0.89 |
| ch03 | s-3-4-1 | `section 3.2.2.A · Q3-10` | Q3-10 Closer look only; section 3.2.2.A->3.2.2.A (number+title, section-text match 0.68) unit coverage iG 0.25 vs CL 0.75 |
| ch03 | s-3-4-2 | `section 3.2.2.E · Q3-11` | section 3.2.2.E->3.2.2.E (number+title, section-text match 0.76) unit coverage iG 0.75 vs CL 0.83 |
| ch03 | s-3-4-2 | `section 3.2.2.E · Q3-12` | section 3.2.2.E->3.2.2.E (number+title, section-text match 0.76) unit coverage iG 0.67 vs CL 0.81 |
| ch03 | s-3-4-7 | `section 3.3.6 · Q3-41` | Q3-41 Closer look only |
| ch03 | s-3-5-2 | `section 3.3.1.B · Q3-23` | Q3-23 Closer look only; section 3.3.1.B->3.3.1 (parent fallback, section-text match 0.26) unit coverage iG 0.50 vs CL 0.64 |
| ch03 | s-3-5-2 | `section 3.3.1.A` | section 3.3.1.A->3.3.1 (parent fallback, section-text match 0.51) unit coverage iG 0.73 vs CL 1.00 |
| ch03 | s-3-5-2 | `section 3.3.1.B` | section 3.3.1.B->3.3.1 (parent fallback, section-text match 0.26) unit coverage iG 0.43 vs CL 0.78 |
| ch03 | s-3-5-3 | `section 3.3.1.A` | section 3.3.1.A->3.3.1 (parent fallback, section-text match 0.51) unit coverage iG 0.71 vs CL 0.76 |
| ch03 | s-3-5-3 | `section 3.3.1.A` | section 3.3.1.A->3.3.1 (parent fallback, section-text match 0.51) unit coverage iG 0.58 vs CL 0.45 |
| ch03 | s-3-5-5 | `section 3.3.1.A · Q3-22` | Q3-22 Closer look only; section 3.3.1.A->3.3.1 (parent fallback, section-text match 0.51) unit coverage iG 0.50 vs CL 0.80 |
| ch03 | s-3-5-5 | `section 3.3.1.B · Q3-24` | Q3-24 partial match only (iGAAP Q3-17); section 3.3.1.B->3.3.1 (parent fallback, section-text match 0.26) unit coverage iG 0.53 vs CL 0.83 |
| ch03 | s-3-5-5 | `section 3.3.1.B · Q3-24` | Q3-24 partial match only (iGAAP Q3-17) |
| ch03 | s-3-5-9 | `section 3.3.2` | section 3.3.2->3.3.2 (number+title, section-text match 0.55) unit coverage iG 0.27 vs CL 0.73 |
| ch03 | s-3-5-9 | `section 3.3.2.C · Q3-26` | Q3-26 partial match only (iGAAP Q3-19); section 3.3.2.C->3.3.2.B (title (renumbered), section-text match 0.85) unit coverage iG 0.73 vs CL 0.91 |
| ch03 | s-3-5-11 | `section 3.3.3.E · Q3-32` | Q3-32 Closer look only; section 3.3.3.E->3.3.3 (parent fallback, section-text match 0.32) unit coverage iG 0.39 vs CL 0.72 |
| ch03 | s-3-5-11 | `section 3.3.3.E · Q3-33` | Q3-33 Closer look only; section 3.3.3.E->3.3.3 (parent fallback, section-text match 0.32) unit coverage iG 0.39 vs CL 0.72 |
| ch03 | s-3-5-11 | `section 3.3.3.E · Q3-31` | Q3-31 Closer look only; section 3.3.3.E->3.3.3 (parent fallback, section-text match 0.32) unit coverage iG 0.44 vs CL 0.60 |
| ch03 | s-3-5-11 | `section 3.3.3.E · Q3-30` | section 3.3.3.E->3.3.3 (parent fallback, section-text match 0.32) unit coverage iG 0.42 vs CL 0.37 |
| ch03 | s-3-5-11 | `section 3.3.3.E · Q3-34` | Q3-34 Closer look only |
| ch03 | s-3-5-11 | `section 3.3.3.F` | section 3.3.3.F->3.3.3 (parent fallback, section-text match 0.27) unit coverage iG 0.62 vs CL 0.85 |
| ch03 | s-3-5-ex4 | `Ill 3-11 / section 3.3.3.E` | Ill 3-11 Closer look only; section 3.3.3.E->3.3.3 (parent fallback, section-text match 0.32) unit coverage iG 0.45 vs CL 0.75 |
| ch03 | s-3-5-15 | `section 3.3.3.H` | section 3.3.3.H->3.3.3.B (title (renumbered), section-text match 0.75) unit coverage iG 0.77 vs CL 0.85 |
| ch03 | s-3-5-insurers | `section 3.3.5` | section 3.3.5->3.3.5 (number+title, section-text match 0.23) unit coverage iG 0.57 vs CL 0.64 |
| ch03 | s-3-5-insurers | `section 3.3.5 · Q3-39` | Q3-39 Closer look only; section 3.3.5->3.3.5 (number+title, section-text match 0.23) unit coverage iG 0.14 vs CL 0.71 |
| ch03 | s-3-5-insurers | `section 3.3.5.A` | section 3.3.5.A->3.3.5.A (number+title, section-text match 0.92) unit coverage iG 0.54 vs CL 0.62 |
| ch03 | s-3-5-insurers | `section 3.3.5.B` | section 3.3.5.B->3.3.5.B (number+title, section-text match 0.78) unit coverage iG 0.46 vs CL 0.46 |
| ch03 | s-3-6 | `section 3.2.4` | section 3.2.4->3.2.4 (number+title, section-text match 0.42) unit coverage iG 0.44 vs CL 0.89 |
| ch03 | s-3-7-1 | `section 3.2.6.B` | section 3.2.6.B->3.2.6.B (number+title, section-text match 0.69) unit coverage iG 0.26 vs CL 0.31 |
| ch03 | s-3-7-5 | `section 3.2.7` | section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.73 vs CL 0.87 |
| ch03 | s-3-7-5 | `section 3.2.7` | section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.25 vs CL 0.62 |
| ch03 | s-3-7-5 | `section 3.2.7 · Q3-20` | Q3-20 Closer look only; section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.40 vs CL 0.80 |
| ch03 | s-3-7-ex3 | `Ill 3-7 / section 3.2.7` | Ill 3-7 Closer look only; section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.45 vs CL 0.84 |
| ch03 | s-3-7-7 | `section 3.2.7 · Q3-21` | Q3-21 partial match only (iGAAP Q3-16) |
| ch03 | s-3-7-7 | `section 3.2.7 · Q3-21` | Q3-21 partial match only (iGAAP Q3-16); section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.17 vs CL 0.83 |
| ch03 | s-3-7-7 | `section 3.2.7 · Q3-21` | Q3-21 partial match only (iGAAP Q3-16); section 3.2.7->3.2.7 (number+title, section-text match 0.41) unit coverage iG 0.68 vs CL 0.89 |
| ch03 | s-3-7-ex4 | `Ill 3-8 / section 3.2.8.B` | Ill 3-8 Closer look only; section 3.2.8.B->3.2.8.B (number+title, section-text match 0.41) unit coverage iG 0.21 vs CL 0.85 |
| ch03 | s-3-9-ey | `Ill 3-1` | Ill 3-1 Closer look only |
| ch03 | s-3-9-ey | `Ill 3-7` | Ill 3-7 Closer look only |
| ch03 | s-3-9-ey | `Ill 3-8` | Ill 3-8 Closer look only |
| ch03 | s-3-9-ey | `Ill 3-11` | Ill 3-11 Closer look only |

## Appendix C — skipped (no iGAAP counterpart)

| Page | Closer look chip | n |
|---|---|---|
| ch01 | `Overview` | 18 |
| ch01 | `Overview fn2` | 2 |
| ch03 | `section C.3 · Q C.3-3` | 1 |
| ch03 | `section C.5 · Q C.5-2` | 1 |
| ch03 | `section C.5 · Q C.5-3` | 1 |
| ch03 | `section C.5 · Q C.5-7` | 1 |
| ch03 | `section C.3` | 1 |
| ch03 | `section C.3 · Q C.3-1` | 1 |
| ch03 | `Figure C.2-1 / section C.2` | 1 |
| ch03 | `section C.2 · Q C.2-1` | 1 |
| ch03 | `section C.2 · Q C.2-2` | 1 |
| ch03 | `section C.8 · Q C.8-1` | 1 |
| ch03 | `section C.3 · Q C.3-2` | 1 |
| ch03 | `section C.4 · Q C.4-1` | 1 |
| ch03 | `section C.4 · Q C.4-2` | 1 |
| ch03 | `Ill C.5-1 / section C.5` | 1 |
| ch03 | `section C.5 · Q C.5-1` | 1 |
| ch03 | `section C.5 · Q C.5-4` | 1 |
| ch03 | `section C.5 · Q C.5-5` | 1 |
| ch03 | `section C.6 · Q C.6-1` | 1 |
| ch03 | `section C.7 · Q C.7-1` | 1 |
| ch03 | `section C.9 · Q C.9-1` | 1 |
| ch03 | `section C.9 · Q C.9-2` | 1 |
| ch03 | `section C.9 · Q C.9-3` | 1 |
| ch03 | `section C.10 · Q C.10-1` | 1 |
| ch03 | `Figure 3-6 / section 3.2.8` | 1 |
| ch03 | `section 3 / Appendix A` | 1 |
