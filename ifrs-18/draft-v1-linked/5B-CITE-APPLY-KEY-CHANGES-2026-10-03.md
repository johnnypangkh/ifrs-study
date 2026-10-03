# #5b IFRS 18 iGAAP chips on remaining chapters — KEY CHANGES (2026-10-03)

**Job:** #5b — same job as #5 Q3, on the remaining chapters only (ch02, ch04, ch05, ch06, ch08).
**Scope held:** `EY iGAAP 2026 Ch04 · …` chips only, each placed immediately after an existing `EY Closer look 2026 · …` chip. No new prose, no new units, no iGAAP-only content. No densify restart. No chrome / CSS / Map / visual / teaching-prose edits. **S1 HOLD** (nothing done). **S3** untouched. ch01 / ch03 / ch07 not touched. references.html not touched (the iGAAP row from #5 is already there, exactly once). Pack-wide Last update stamp unchanged (`2026-10-02 20:16 HKT`). DTT full name unchanged. PwC still missing (no invent).

## Base pages

Edited the five box copies from `i18-5b-pages.tgz` (md5 `e72b3b14…`), not older Opus copies. Box chrome kept as delivered: `chrome.css?v=7e-tag-bar-20261003`, `draft.css?v=7b3-pointchip-wrap-20261003`, visual iframe `?v=map-orphan-para-20261003`, no "scroll tags →" span. Two box-side heading retitles (ch05 `#s-5-0-1`, ch08 `#s-8-0-1`) kept as delivered. Only new `.cite-ey` iGAAP spans were inserted; nothing else on the pages changed (see QA).

## Attach checklist (this run)

| Source | Status | Use |
|---|---|---|
| EY iGAAP 2026 Ch04 | **ATTACHED** — md5 `0613da32b2a21a3d5184c65c8d081544` (matches brief and #5) | Full text extracted; every section, Illustration and FAQ body used for matching |
| Official IFRS 18 | on disk in HTML — not re-attached | not used (no Official chip changes) |
| EY Closer look 2026 | on disk — not attached | the comparison side of the locked rule only; no new substance |
| KPMG FI / DTT A4 | on disk — not attached | not used |
| PwC | missing | unchanged |

## Method — locked #5 rule, reused

Same rule as `5-CITE-APPLY-KEY-CHANGES-2026-10-03.md` → "Match rule". No new rule was derived.

1. **Illustrations / FAQs / Figures:** pair by identical title (duplicate FAQ titles paired in order), then body compare: **≥ 0.85 of the Closer look body found in iGAAP = chip**; below = partial → no chip.
2. **Sections:** same number + title → same-title renumbered under the same parent → subject overrides (CL 3.2.1.B↔iG 3.2.1.A, 3.2.6.C↔3.2.6.C, 3.3.2.A↔3.3.2.A) → iGAAP parent. Then score the chip's teaching unit (share of its content words found in the section text):
   - iGAAP section ≥ 0.85 of CL section text: add if iGAAP score ≥ 0.9 × CL score (and CL > 0).
   - iGAAP section materially smaller: add only if CL ≥ 0.5 **and** iGAAP ≥ CL.
3. **Manual read** of every addition with CL score < 0.45. Manual reads can only demote.
4. Chapter "Overview", Appendix C, and Figures with no iGAAP counterpart: **skip**.

**Chip shape mirrors the Closer look chip beside it**, with iGAAP numbers substituted: `section X`, `Ill N-N / section X`, `Fig N-N / section X`, `section X · QN-N`. Multi-section CL chips (e.g. `section 3.4.2.D / section 3.4.2.E`) are mirrored in full (#5's builder kept only the first section; ch01 / ch03 / ch07 have no multi-section Closer look chips, so #5 output is unaffected).

### Method-neutral fixes this run (no change to the rule)

- **Heading parser:** iGAAP writes one heading as `3.5.` (trailing period) and one title starts with a curly quote (`‘Cost of sales’ line item`, 3.4.2.C). The #5 parser missed both, so their text was merged into the previous section. Fixed so both books split on these headings. iGAAP 3.5 and CL 3.5 are now each about 1,500 words.
- **Drift check:** #5's ch01 / ch03 / ch07 re-run with the fixed parser gives **0 differences** from the delivered #5 chips other than the known #5 manual demotion (ch03 `#s-3-1` Concept insight). #5 results stand.
- **Fig 2-1:** the CL chip abbreviates "Fig", so the "Figure — no counterpart" skip did not apply. iGAAP has Figure 2-1 with the same title and an identical lead-in (both based on IFRS 18 IE Figure 7) → paired as an item.

### Known partials re-checked (brief: "unless a fresh body compare clears 0.85")

| Item | #5 KEY | Fresh compare | Result |
|---|---|---|---|
| Ill 6-1 ↔ iG Ill 6-1 | 0.67 | **0.98** — body cut at the "Future developments" heading; 157/157 words; only diff Entity Q (CL) vs Entity A (iG) | **chip added.** The #5 capture ran on into "Future developments", which caused the 0.67. **Correction to the #5 KEY note.** |
| Q2-2 ↔ iG Q2-2 | 0.59 | 0.59 — CL answer genuinely rewritten | **no chip** (3 units) |

## Per-page counts

Counts are Closer look chip occurrences. Each one gets either an iGAAP chip, a rejection, or a skip.

| Page | Closer look chips | iGAAP added | Rejected | Skipped | Rejection reasons |
|---|---|---|---|---|---|
| ch02 | 61 | 51 | 10 | 0 | section coverage below rule 7; partial FAQ/Ill match 3 |
| ch04 | 30 | 23 | 7 | 0 | unscorable parent-level pointer (0/0) 1; manual review 1; section coverage below rule 4; Closer-look-only Ill/FAQ 1 |
| ch05 | 33 | 25 | 8 | 0 | section coverage below rule 6; Closer-look-only Ill/FAQ 2 |
| ch06 | 46 | 38 | 8 | 0 | unscorable parent-level pointer (0/0) 2; section coverage below rule 2; Closer-look-only Ill/FAQ 4 |
| ch08 | 22 | 19 | 2 | 1 | section coverage below rule 1; manual review 1 |
| **Total** | **192** | **156** | **35** | **1** | |

**156** iGAAP chips added (**69** distinct locators): ch02 **51**, ch04 **23**, ch05 **25**, ch06 **38**, ch08 **19**. Pack-wide iGAAP chips are now ch01 21, ch02 51, ch03 130, ch04 23, ch05 25, ch06 38, ch07 36, ch08 19 (343 in total). The full list is in Appendix A and every no-chip row is in Appendix B.

Chip HTML (unchanged from #5): `<span class="cite cite-ey"><span class="cite-house">EY</span> iGAAP 2026 Ch04 · section 3.2.1.B</span>`.

## Locator pairs used

### Illustrations / FAQs / Figures

| Page | Closer look | iGAAP Ch04 | Body match (CL found in iG) | Note |
|---|---|---|---|---|
| ch02 | Ill 2-1 | Ill 2-1 | 0.95 | |
| ch02 | Ill 2-2 | Ill 2-2 | 0.99 | |
| ch02 | Fig 2-1 | Fig 2-1 | same title + identical lead-in | both based on IFRS 18 IE Figure 7 |
| ch02 | Q2-1 | Q2-1 | 0.88 | 2 chips |
| ch04 | Ill 3-12 | **Ill 3-8** | 0.89 | as #5 |
| ch04 | Q3-40 | **Q3-27** | 0.98 | as #5 |
| ch04 | Q3-42 | **Q3-28** | 0.95 | specified-MBA copy |
| ch04 / ch06 | Q4-5 | Q4-5 | 0.91 | 2 + 1 chips |
| ch05 | Ill 3-13 | **Ill 3-9** | 0.96 | Entity U (CL) vs Entity A (iG) |
| ch06 | Ill 4-1 | Ill 4-1 | 0.98 | |
| ch06 | Q4-1 / Q4-2 / Q4-3 / Q4-4 | Q4-1 / Q4-2 / Q4-3 / Q4-4 | 1.00 / 0.99 / 0.92 / 0.99 | Q4-4 6 chips |
| ch08 | Ill 6-1 | Ill 6-1 | **0.98** (fresh) | Entity Q (CL) vs Entity A (iG) |

**No chip:** Q2-2 (partial 0.59; 3 units), Q3-43 (Closer look only; ch05 ×2), Q4-6 (Closer look only; ch04 ×1, ch06 ×2), Q4-7 and Q4-8 (Closer look only; ch06).

### Sections

Almost every section locator maps by **same number + same title**. No subject override was needed on these five pages. The exceptions:

| Closer look | iGAAP Ch04 | Chips | Why |
|---|---|---|---|
| section 3.3.3.G | section 3.3.3.A | 4 (ch04) | same title, renumbered under 3.3.3 (as #5: CL 3.3.3.G–K ↔ iG 3.3.3.A–E) |
| section 3.2.1.H | section 3.2.1.D | 2 (ch04) | same title, renumbered under 3.2.1 (as #5) |
| section 4.2.3 · Q4-4 | section 4.2.3.B · Q4-4 | 1 (ch06) | FAQ chips take the iGAAP home section of the paired FAQ (as #5); iGAAP Q4-4 sits in 4.2.3.B |

Multi-section chips are mirrored in full (e.g. `section 3.4.2.D / section 3.4.2.E` → the same in iGAAP). See Appendix A for every locator, with counts and anchors.

## Rejections and skip (36) by reason

| Reason | Count | Where |
|---|---|---|
| Section coverage below rule (iGAAP section shorter or reworded for that unit) | 20 | ch02 7, ch04 4, ch05 6, ch06 2, ch08 1 (`section 7` Future developments — iGAAP section 7 holds 0.13 of CL text) |
| Closer-look-only FAQ (no iGAAP counterpart) | 7 | Q4-6 ×3, Q3-43 ×2, Q4-7, Q4-8 |
| Partial FAQ (< 0.85) | 3 | ch02 Q2-2 |
| Unscorable parent-level pointer (unit 0.00 in both CL and iG section intro texts) | 3 | ch04 `#s-4-1` `section 3.1 / section 3.2.3.A / section 3.2.1.H`; ch06 `#s-6-2` `section 4.2.3`; ch06 `#s-6-3` `section 4.2.4` |
| Manual review demotion | 2 | see below |
| Skip — Overview | 1 | ch08 `#s-8-1` `Overview / section 6` |

**Manual review:** all 29 additions with a CL score below 0.45 were read against the iGAAP text. 27 are supported verbatim or near-verbatim in the mapped iGAAP section. 2 were demoted:

1. ch04 `#s-4-2` Big4-alignment point (`section 3.2.1.H / section 4.2.4`): the claim (the 65(a)(ii) path bars the required middle subtotal; any extra subtotal must be faithfully labelled) is not in CL 3.2.1.H / 4.2.4 and not in iG 3.2.1.D / 4.2.4 → no iGAAP chip.
2. ch08 `#s-8-5` (`section 3.3.5.A`): the unit is about ED/2026/1 (Feb 2026), which appears only in Closer look footnote 25. iGAAP 3.3.5.A does not mention it → no iGAAP chip.

## Flags (no action taken — out of #5b scope)

- **ch04 `#s-4-2`:** the pre-existing `EY Closer look 2026 · section 3.2.1.H / section 4.2.4` chip looks weak. Its support sits in the CL 3.3.3.G area. Left unchanged.
- **#5 KEY correction:** "Off-page: … Ill 6-1 0.67" should read **0.98**. The 0.67 came from a body capture that ran into "Future developments". The #5 KEY file is left unedited; this file records the correction.
- **Unscorable parent pointers** (3 rows above): the chips point at parent sections whose own intro text does not carry the unit. Under the locked rule they get no iGAAP chip. If the chrome owner wants them covered, that needs a rule change (score against the parent plus its children), which #5b was told not to make.

## QA

| Check | Result |
|---|---|
| HTML balanced (5 pages) | pass — 0 unbalanced tags; no duplicate ids |
| Non-chip text identical to uploaded box pages | pass — with every iGAAP chip span (and the single space before it) removed, each page is byte-identical to its box copy |
| Chips removed / non-iGAAP chips added | 0 / 0 |
| Every iGAAP chip immediately after a Closer look chip | pass (156 / 156) |
| Every new locator exists in the attached iGAAP Ch04 text | pass — 69 / 69 distinct locators; every section number is an iGAAP heading and every Ill / Fig / Q label is in the PDF text (md5 `0613da32…`) |
| Repeated chip in the same cell; house-only chips; `§` | 0; 0; 0 |
| Last update stamp | unchanged `2026-10-02 20:16 HKT` on all five pages |
| Stylesheet / iframe query strings | unchanged (`7e-tag-bar-20261003`, `7b3-pointchip-wrap-20261003`, `map-orphan-para-20261003`) |
| ch01 / ch03 / ch07 / references.html | untouched |
| References | exactly 1 `EY iGAAP 2026 Ch04` row; every chip prefix on ch01–ch08 is listed |
| Pack anchors | all in-page and cross-chapter anchors resolve |

## Screenshots (one chip cluster per edited chapter; new iGAAP chip outlined in red)

| Page | Anchor | Cluster | File |
|---|---|---|---|
| ch02 | `#s-2-1-ex` | Ill 2-1 ↔ Ill 2-1 | `screenshots/j5b-ch02-ill21.png` |
| ch04 | `#s-4-1` | section 3.3.3.A | `screenshots/j5b-ch04-s333a.png` |
| ch05 | `#s-5-2-ey` | CL Ill 3-13 ↔ iG Ill 3-9 | `screenshots/j5b-ch05-ill39.png` |
| ch06 | `#s-6-4-ey` | Ill 4-1 ↔ Ill 4-1 | `screenshots/j5b-ch06-ill41.png` |
| ch08 | `#s-8-4-ey` | Ill 6-1 ↔ Ill 6-1 | `screenshots/j5b-ch08-ill61.png` |

## Not done (scope)

- **Last update stamp not bumped** (brief). The chrome owner sets the pack-wide release stamp when syncing.
- **DTT full name unchanged** (brief). The title correction is still open from the old Ask A4.
- index.html not in the bundle → not edited (it carries no EY chips).

## Files in `/opt/cursor/artifacts/5b-cite-apply-20261003.tgz`

`ch02.html`, `ch04.html`, `ch05.html`, `ch06.html`, `ch08.html`, `5B-CITE-APPLY-KEY-CHANGES-2026-10-03.md`.

---

## Appendix A — iGAAP chips added (distinct, with count and section anchors)

| Page | Closer look chip | iGAAP chip added | n | Anchors |
|---|---|---|---|---|
| ch02 | `section 2` | `section 2` | 1 | s-2-0 |
| ch02 | `section 2.1` | `section 2.1` | 6 | s-2-0, s-2-1, s-2-1-2 |
| ch02 | `section 2.2` | `section 2.2` | 6 | s-2-0, s-2-3 |
| ch02 | `section 2.3` | `section 2.3` | 2 | s-2-0, s-2-4 |
| ch02 | `section 2.1.1` | `section 2.1.1` | 6 | s-2-1, s-2-1-2, s-2-2, s-2-2-1 |
| ch02 | `Ill 2-1 / section 2.1` | `Ill 2-1 / section 2.1` | 1 | s-2-1-ex |
| ch02 | `section 2.1.2` | `section 2.1.2` | 3 | s-2-1-3 |
| ch02 | `section 2.1.3` | `section 2.1.3` | 2 | s-2-1-4 |
| ch02 | `section 2.1.1.A` | `section 2.1.1.A` | 4 | s-2-2-1 |
| ch02 | `section 2.1.1.B` | `section 2.1.1.B` | 3 | s-2-2-2 |
| ch02 | `section 2.1.1.B · Q2-1` | `section 2.1.1.B · Q2-1` | 2 | s-2-2-3 |
| ch02 | `section 2.2.1` | `section 2.2.1` | 5 | s-2-3 |
| ch02 | `section 2.2.2` | `section 2.2.2` | 2 | s-2-3 |
| ch02 | `Ill 2-2 / section 2.2` | `Ill 2-2 / section 2.2` | 1 | s-2-2-ex |
| ch02 | `section 2.2.2.A` | `section 2.2.2.A` | 2 | s-2-3-2 |
| ch02 | `section 2.2.2.B` | `section 2.2.2.B` | 1 | s-2-3-3 |
| ch02 | `section 2.2.3` | `section 2.2.3` | 1 | s-2-3-5 |
| ch02 | `section 2.3.1` | `section 2.3.1` | 2 | s-2-4, s-2-4-fig7 |
| ch02 | `Fig 2-1 / section 2.3` | `Fig 2-1 / section 2.3` | 1 | s-2-4-fig7 |
| ch04 | `section 3.3.3.G` | `section 3.3.3.A` | 4 | s-4-1, s-4-2, s-4-2-2, s-4-5 |
| ch04 | `section 3.2.1.H` | `section 3.2.1.D` | 2 | s-4-1 |
| ch04 | `section 3.2.3.A` | `section 3.2.3.A` | 1 | s-4-1 |
| ch04 | `section 3.4` | `section 3.4` | 3 | s-4-3, s-4-3-2 |
| ch04 | `section 3.4.1` | `section 3.4.1` | 3 | s-4-3, s-4-3-3 |
| ch04 | `section 3.4 · Q3-42` | `section 3.4 · Q3-28` | 1 | s-4-3 |
| ch04 | `section 4.2.4` | `section 4.2.4` | 3 | s-4-4 |
| ch04 | `section 4.1 / section 4.2.4` | `section 4.1 / section 4.2.4` | 1 | s-4-4 |
| ch04 | `section 4.2.4.A · Q4-5` | `section 4.2.4.A · Q4-5` | 2 | s-4-4-1 |
| ch04 | `section 4.2.4.B` | `section 4.2.4.B` | 1 | s-4-4-2 |
| ch04 | `section 3.3.5.A · Q3-40` | `section 3.3.5.A · Q3-27` | 1 | s-4-4-2 |
| ch04 | `Ill 3-12` | `Ill 3-8` | 1 | s-4-5-ey |
| ch05 | `section 3.4.2 / section 3.4.2.E` | `section 3.4.2 / section 3.4.2.E` | 1 | s-5-0 |
| ch05 | `section 3.4.2` | `section 3.4.2` | 2 | s-5-0, s-5-1 |
| ch05 | `section 3.4.2.D / section 3.4.2.E` | `section 3.4.2.D / section 3.4.2.E` | 1 | s-5-1 |
| ch05 | `section 3.4.2.D` | `section 3.4.2.D` | 2 | s-5-1 |
| ch05 | `section 3.4.2.E` | `section 3.4.2.E` | 4 | s-5-1, s-5-1-5 |
| ch05 | `section 3.4.2.A` | `section 3.4.2.A` | 1 | s-5-1 |
| ch05 | `section 3.4.2.B` | `section 3.4.2.B` | 4 | s-5-1, s-5-2, s-5-3, s-5-4 |
| ch05 | `section 3.4.2.C` | `section 3.4.2.C` | 2 | s-5-2 |
| ch05 | `section 3.5` | `section 3.5` | 6 | s-5-2-1 |
| ch05 | `Ill 3-13` | `Ill 3-9` | 1 | s-5-2-ey |
| ch05 | `section 3.4.2.A / section 3.4.2.B` | `section 3.4.2.A / section 3.4.2.B` | 1 | s-5-3 |
| ch06 | `section 4` | `section 4` | 1 | s-6-0 |
| ch06 | `section 4.1 / section 4.2.1` | `section 4.1 / section 4.2.1` | 1 | s-6-0 |
| ch06 | `section 4.1` | `section 4.1` | 1 | s-6-0 |
| ch06 | `section 4.2.1` | `section 4.2.1` | 2 | s-6-1 |
| ch06 | `section 4.2.1 · Q4-1` | `section 4.2.1 · Q4-1` | 2 | s-6-1, s-6-1-2 |
| ch06 | `section 4.2.2` | `section 4.2.2` | 4 | s-6-1 |
| ch06 | `section 4.2.3 · Q4-4` | `section 4.2.3.B · Q4-4` | 1 | s-6-1 |
| ch06 | `section 4.2.3.A` | `section 4.2.3.A` | 1 | s-6-1 |
| ch06 | `section 4.2.3.B` | `section 4.2.3.B` | 1 | s-6-1 |
| ch06 | `section 4.2.4.A · Q4-5` | `section 4.2.4.A · Q4-5` | 1 | s-6-1 |
| ch06 | `section 4.2.1 / section 4.4` | `section 4.2.1 / section 4.4` | 1 | s-6-1 |
| ch06 | `section 4.4` | `section 4.4` | 1 | s-6-1 |
| ch06 | `section 4.1 / section 4.2.1 / section 4.2.2` | `section 4.1 / section 4.2.1 / section 4.2.2` | 1 | s-6-1 |
| ch06 | `section 4.2.1 · Q4-2` | `section 4.2.1 · Q4-2` | 1 | s-6-1-2 |
| ch06 | `section 4.2.1 · Q4-3` | `section 4.2.1 · Q4-3` | 1 | s-6-1-2 |
| ch06 | `section 4.2` | `section 4.2` | 1 | s-6-1-2 |
| ch06 | `section 4.2.3.B · Q4-4` | `section 4.2.3.B · Q4-4` | 5 | s-6-1-3 |
| ch06 | `section 4.2.3.C` | `section 4.2.3.C` | 1 | s-6-2 |
| ch06 | `section 4.2.3.D` | `section 4.2.3.D` | 1 | s-6-2 |
| ch06 | `section 4.2.4.A` | `section 4.2.4.A` | 1 | s-6-3 |
| ch06 | `section 4.2.4.B` | `section 4.2.4.B` | 1 | s-6-3 |
| ch06 | `section 4.2.4` | `section 4.2.4` | 1 | s-6-3 |
| ch06 | `section 4.3.2` | `section 4.3.2` | 3 | s-6-4 |
| ch06 | `section 4.3.4` | `section 4.3.4` | 1 | s-6-4 |
| ch06 | `section 4.3.3.A` | `section 4.3.3.A` | 1 | s-6-4 |
| ch06 | `section 4.3.2 / section 4.3.3` | `section 4.3.2 / section 4.3.3` | 1 | s-6-4 |
| ch06 | `Ill 4-1` | `Ill 4-1` | 1 | s-6-4-ey |
| ch08 | `section 6` | `section 6` | 12 | s-8-0, s-8-0-1, s-8-1, s-8-2, s-8-3, s-8-3-appc, s-8-4-ex, s-8-5 |
| ch08 | `section 6.1` | `section 6.1` | 4 | s-8-0-1, s-8-4, s-8-4-1 |
| ch08 | `Ill 6-1` | `Ill 6-1` | 1 | s-8-4-ey |
| ch08 | `section 3.3.5.A` | `section 3.3.5.A` | 2 | s-8-5 |
## Appendix B — Closer look chips with no iGAAP chip (rejected or skipped)

| Page | Anchor | Closer look chip | Why no iGAAP chip |
|---|---|---|---|
| ch02 | s-2-2-2 | `section 2.1.1.B` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.78 vs CL 0.83 |
| ch02 | s-2-2-2 | `section 2.1.1.B` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.41 vs CL 0.96 |
| ch02 | s-2-2-3 | `section 2.1.1.B · Q2-1` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.85 vs CL 0.89 |
| ch02 | s-2-2-3 | `section 2.1.1.B · Q2-1` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.91 vs CL 0.95 |
| ch02 | s-2-2-3 | `section 2.1.1.B · Q2-1` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.86 vs CL 0.93 |
| ch02 | s-2-3-2 | `section 2.2.2.A` | section 2.2.2.A->2.2.2.A (number+title, section-text match 0.94) unit coverage iG 0.78 vs CL 0.89 |
| ch02 | s-2-3-6 | `section 2.2.2 · Q2-2` | Q2-2 partial match only (iGAAP Q2-2); section 2.2.2->2.2.2 (number+title, section-text match 0.8) unit coverage iG 0.74 vs CL 0.84 |
| ch02 | s-2-3-6 | `section 2.2.2 · Q2-2` | Q2-2 partial match only (iGAAP Q2-2); section 2.2.2->2.2.2 (number+title, section-text match 0.8) unit coverage iG 0.78 vs CL 0.87 |
| ch02 | s-2-3-6 | `section 2.2.2 · Q2-2` | Q2-2 partial match only (iGAAP Q2-2) |
| ch02 | s-2-5 | `section 2.2.1` | section 2.2.1->2.2.1 (number+title, section-text match 0.9) unit coverage iG 0.33 vs CL 0.50 |
| ch04 | s-4-1 | `section 3.1 / section 3.2.3.A / section 3.2.1.H` | section 3.1->3.1 (number+title, section-text match 0.87) unit coverage iG 0.00 vs CL 0.00 |
| ch04 | s-4-2 | `section 3.2.1.H / section 4.2.4` | manual review: claim (65(a)(ii) path bars the required middle subtotal; extra subtotal faithfully labelled) not in Closer look 3.2.1.H / 4.2.4 nor iGAAP 3.2.1.D / 4.2.4 — no iGAAP chip; pre-existing CL chip flagged (support sits in CL 3.3.3.G area) |
| ch04 | s-4-2-ex | `section 3.1` | section 3.1->3.1 (number+title, section-text match 0.87) unit coverage iG 0.01 vs CL 0.00 |
| ch04 | s-4-4-2 | `section 4.2.4.B · Q4-6` | Q4-6 Closer look only; section 4.2.4.B->4.2.4.B (number+title, section-text match 0.74) unit coverage iG 0.56 vs CL 0.75 |
| ch04 | s-4-4-2 | `section 4.2.4.B` | section 4.2.4.B->4.2.4.B (number+title, section-text match 0.74) unit coverage iG 0.38 vs CL 0.38 |
| ch04 | s-4-5 | `section 3.2.1.G` | section 3.2.1.G->3.2.1 (parent fallback, section-text match 0.8) unit coverage iG 0.71 vs CL 0.76 |
| ch04 | s-4-5 | `section 2.1.1.B / section 4.2.4` | section 2.1.1.B->2.1.1.B (number+title, section-text match 0.72) unit coverage iG 0.40 vs CL 0.50 |
| ch05 | s-5-1 | `section 3.4.2.B` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.30 vs CL 0.30 |
| ch05 | s-5-1-3 | `section 3.4.2.B · Q3-43` | Q3-43 Closer look only; section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.44 vs CL 0.62 |
| ch05 | s-5-2 | `section 3.4.2.B / section 3.4.2.C` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.47 vs CL 0.47 |
| ch05 | s-5-3 | `section 3.4.2.B` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.74 vs CL 0.79 |
| ch05 | s-5-3 | `section 3.4.2.B` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.22 vs CL 0.22 |
| ch05 | s-5-3 | `section 3.4.2.B · Q3-43` | Q3-43 Closer look only; section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.39 vs CL 0.67 |
| ch05 | s-5-4 | `section 3.4.2.B` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.73 vs CL 0.80 |
| ch05 | s-5-4 | `section 3.4.2.B` | section 3.4.2.B->3.4.2.B (number+title, section-text match 0.71) unit coverage iG 0.39 vs CL 0.39 |
| ch06 | s-6-2 | `section 4.2.3` | section 4.2.3->4.2.3 (number+title, section-text match 1.0) unit coverage iG 0.00 vs CL 0.00 |
| ch06 | s-6-3 | `section 4.2.4.B` | section 4.2.4.B->4.2.4.B (number+title, section-text match 0.74) unit coverage iG 0.92 vs CL 0.96 |
| ch06 | s-6-3 | `section 4.2.4 · Q4-6` | Q4-6 Closer look only |
| ch06 | s-6-3 | `section 4.2.4.B · Q4-6` | Q4-6 Closer look only; section 4.2.4.B->4.2.4.B (number+title, section-text match 0.74) unit coverage iG 0.33 vs CL 0.83 |
| ch06 | s-6-3 | `section 4.2.4` | section 4.2.4->4.2.4 (number+title, section-text match 1.0) unit coverage iG 0.00 vs CL 0.00 |
| ch06 | s-6-5 | `section 4.2.2 / section 4.3.5` | section 4.3.5->4.3.5 (number+title, section-text match 0.47) unit coverage iG 0.22 vs CL 0.33 |
| ch06 | s-6-5 | `section 4.3.5 · Q4-7` | Q4-7 Closer look only; section 4.3.5->4.3.5 (number+title, section-text match 0.47) unit coverage iG 0.55 vs CL 0.73 |
| ch06 | s-6-5 | `section 4.3.5 · Q4-8` | Q4-8 Closer look only; section 4.3.5->4.3.5 (number+title, section-text match 0.47) unit coverage iG 0.42 vs CL 0.75 |
| ch08 | s-8-1 | `Overview / section 6` | no iGAAP counterpart (Overview / Appendix / Figure / App C) |
| ch08 | s-8-1 | `section 7` | section 7->7 (number+title, section-text match 0.13) unit coverage iG 0.13 vs CL 0.87 |
| ch08 | s-8-5 | `section 3.3.5.A` | manual review: ED/2026/1 (Feb 2026) is only in Closer look footnote 25; iGAAP 2026 Ch04 3.3.5.A does not mention it — no iGAAP chip |