# IFRS 18 — KEY CHANGES (Job #8, Opus densify) — handoff for Grok review

**Runner:** Claude Opus 5.5 (high). **Pack:** IFRS 18 only — `refs/ifrs-18/draft-v1-linked/`. No CF files, no IAS 2.
**Baseline:** commit `e80e993` (pack stamp `2026-10-02 16:20 HKT`). **Final stamp:** `Last update · 2026-10-02 20:16 HKT` on all 10 pages (Asia/Shanghai).
**Diff to review:** `git diff e80e993..HEAD -- refs/ifrs-18/draft-v1-linked/` (30 files; no file outside the pack folder).
**Full per-gate log:** `OPUS-WORKING-MEMORY.md` (Job #8 section) and `IFRS18-CH01…CH08-CONTENT-NOTES.md` (Crosswalk A — Official → Big4, Crosswalk B — Big4 → Official, per chapter).

---

## 1. Gate log

| Gate | Scope | Stamp (HKT) | Johnny |
|---|---|---|---|
| 1 | Overall review (no HTML edits) | — | approved — A1–A4 not approved; S1/S2 guidance; B1/B2 locked |
| 2a | Ch1 densify | 17:20 | approved |
| 2b | Ch2 densify | 17:40 | approved |
| 2c | Ch3 densify (+ classification-path companion) | 18:55 | approved |
| 2d | Ch4 densify | 19:22 | approved |
| 2e | Ch5 densify | 19:36 | standing order: auto-continue Ch6 → Ch8 → Map / consistency |
| 2f | Ch6 densify | 19:45 | standing order |
| 2g | Ch7 densify | 19:56 | standing order |
| 2h | Ch8 densify | 20:02 | standing order |
| 3 | Pack Map (`index.html` + `visuals/map-jumpboard.html`) | 20:06 | standing order |
| 4 | Consistency pass (chapters, visuals, References) | 20:16 | standing order |
| 5 | This file | 20:16 | **awaiting Johnny / Grok review** |

---

## 2. Pack-wide metrics (baseline → now)

Words = teaching-article prose with chips stripped. Chips = all `.cite` chips in the article.

| Chapter | Words | Chips | h4 units | Illustrations | Tables |
|---|---|---|---|---|---|
| Ch1 What’s new | 2,379 → 6,236 | 97 → 227 | 1 → 8 | 0 → 0 | 3 → 9 |
| Ch2 PFS & aggregation | 2,694 → 7,197 | 99 → 318 | 1 → 13 | 3 → 3 | 7 → 17 |
| Ch3 P&L categories | 6,062 → 17,104 | 222 → 861 | 6 → 36 | 6 → 19 | 14 → 34 |
| Ch4 Totals & subtotals | 2,737 → 5,210 | 128 → 249 | 0 → 8 | 3 → 3 | 3 → 11 |
| Ch5 Operating expenses | 3,074 → 5,242 | 141 → 210 | 0 → 6 | 4 → 6 | 3 → 13 |
| Ch6 MPMs | 4,127 → 6,168 | 172 → 263 | 1 → 6 | 2 → 2 | 6 → 11 |
| Ch7 Other FS impacts | 1,792 → 4,705 | 52 → 154 | 0 → 10 | 5 → 5 | 5 → 15 |
| Ch8 Transition | 980 → 2,186 | 48 → 95 | 0 → 5 | 1 → 1 | 4 → 8 |
| **Total** | **23,845 → 54,048** | **959 → 2,377** | **9 → 92** | **24 → 39** | **45 → 118** |

Pack-wide now: `§` 0 (chapters, visuals, Map, References); reader-facing “Gate” 0; source-label leads 0; author meta 0; plain “see N.N” 0; `.callout.differ` 0; every pre-existing `id` kept; every true Illustration is a `.worked-strip` with Facts / Assessment / Decision peers; non-Illustration worked-strips 0.

---

## 3. Key changes by chapter

**Ch1.** 1.3 rebuilt around Official Figure 1 (1.3.1 “IFRS 18 on one page”) plus the KPMG Appendix IAS 1 paragraph bridge (1.3.2), consequential amendments (1.3.3) and terminology (1.3.4). 1.1.1 ED 2019 → final Standard (BC). 1.2.1 KPMG FI section 1.2 key actions. 1.4 “Effective date cue” → full effective-date and transition summary linking Ch8. Wrong-shape “Teaching cue” strip 1.3.5 → plain h4 (not invent).

**Ch2.** Materiality four-step process (2.0.1); why the roles exist and what notes provide (2.1.2–2.1.3); cross-references (2.1.4); required vs additional line items with the four constraints (2.2.1–2.2.2); realised / unrealised FV (2.2.3); characteristics tables (2.3.2–2.3.3); opex-by-function aggregation (2.3.5, KPMG Example 4 vs EY 2.2.3 shown write-once); FX same-line vs separate-line (2.3.6, EY Q2-2).

**Ch3** (largest). 36 h4 units across 3.2–3.7; 19 Illustrations at home sections (EY Ill 3-1…3-12, KPMG Examples 1–3 split into separate plates, Official IE10–IE13). Banks / insurers / bancassurers as h4 units 3.5.17–3.5.21 inside 3.5 (Johnny Q6), from KPMG section 8 and EY Appendix C (bank statement shape from EY Figure C.2-1). New 3.7 other requirements: derecognition and held for sale, change in use, FX and net monetary position, intercompany FX (IFRS IC March 2026 per EY), derivatives (Figure 5). 3.9 Illustration index. Companion `ch03-classification-path` stem fixed.

**Ch4.** Board-rejected alternatives (4.1.2); para 73 replacement-subtotal labelling (4.2.2); IFRS 9 / IFRS 17 line items, one listed line in more than one category, financing line items (4.3.1–4.3.3); additional subtotals can be MPMs (4.4.1); listed subtotals in practice incl. EBITDA (4.4.2).

**Ch5.** IAS 1 vs IFRS 18 table (5.0.1); IE examples of opex presentation (5.1.3); mixed presentation and its limits (5.1.5); non-recurring items by function (5.2.1); why five natures (5.3.3); para 84 exemption side by side with KPMG wording. **Pack figure error fixed:** Illus 5.3.1 amortisation 12,870 → 12,690 (Official IE Note 1; EY agrees).

**Ch6.** Edge-of-definition measures (6.1.2); segment measures as MPMs (6.1.3); BC rebuttal examples (6.2.1); reconciliation layout, effort and regulators (6.4.3); decision table 6.4.4.

**Ch7.** All six h3s retitled to their actual content. Consequential-amendments table (7.0.1); IAS 7 interest / dividend before and after (7.1.1); specified-MBA cash flows (7.1.2); EY Ill 5-1 SCF Illustration (7.1.3); SFP carried forward and changed (7.2.1) with full Official XYZ SFP (7.2.2); IAS 33 73B–73C conditions (7.3.1); interim MPM placement and cross-referencing (7.4.1–7.4.2); capital disclosures with IE14 / IE16 plates (7.5.2–7.5.3). Wrong chip `IFRS 18 · para IE Figure 3.3` removed from 7.1.2 (Figure 3.3 is not about cash flows).

**Ch8.** Appendix C at a glance (8.0.1); para C3 reconciliation elements (8.3.1); first-year interim duties (8.4.1); EY Ill 6-1 Illustration (8.4.2); calendar-year outputs (8.4.3); KPMG practical points (8.4.4); IAS 28 election (8.5); timeline table (8.6).

---

## 4. Map (Gate 3) and consistency (Gate 4)

- **Map:** header rules now “Supersedes IAS 1” (→ 1.3) and Figure 1 (→ 1.3.1); “Single audited note” → “Single note” (para 122); “(later…)” see-also replaced; Grouping + Cross-references cell; MPM + presumption and interim cells; Ch7 box 3 → 6 cells, Ch8 box 2 → 4 cells; visit strip fits one row at 1280.
- **Consistency:** Ch1 / Ch2 link text “Ch7 §7.1” → “Ch7 7.1”; Ch1 / Ch2 h4 form → `<strong>N.x.y — Title</strong>` (as Ch3–Ch8); visual chips `§47` → `para 47`, visual text `§` → para / paragraph; visual hedge wording (“Thin”, “cue”, “audited”, “(later)”, aria “Gate —”) replaced; Ch1 visual “Prepare” node linked to 1.2.1 (KPMG section 1.2); Ch2 2.3.6 → Ch3 3.7.5 link; Ch3 3.9 EY Ill 3-12 row also points to Ch4 4.5.1; `references.html` + Official rows for every Standard prefix already used on chips (IAS 8, 20, 21, 28, 29, 40; IFRS 3, 8, 9, 17).

---

## 5. Flags — reproduced, not reconciled (no `.callout.differ` used)

No substantive Big 4 difference was verified in any chapter; wording differences are shown side by side or labelled as the firm’s view.

| Ch | Flag |
|---|---|
| 2 | EY chip locators `Ill 2-1 / section 2.1`, `Ill 2-2 / section 2.2` point to parent sections (Ill sits in 2.1.1 / 2.2.2) — not changed (cite lock). |
| 3 | EY Ill 3-3 “CU600,000 of the loan” (= 60% of the fee) — footnoted in 3.4.4. EY App C Ill C.5-1 vs conclusion “Bank A / Bank B”; Q C.5-1 cites “IFRS 16.56(a)” — row in 3.5.18. |
| 4 | KPMG 2.3.1 para 73 trigger wording vs Official para 73 (4.2.2). KPMG 2.3.4 EBITDA condition vs BC366 (4.4.2). BC367 “would be” vs EY “could be” an MPM (4.4.2). EY Q4-6 locator `118(a)` for OPDAI (= 118(b)) — not reproduced. |
| 5 | KPMG 2.2.2 exemption wording broader than para 84(a)/(b) — side by side in 5.4. KPMG IAS 1 “mixed not prohibited” vs DTT A4 heading “inappropriate” (IAS 1-era; DTT verification only). Official BC272(a) “paragraph 42” vs para 84 “Paragraph 41” — pack follows para 84. |
| 6 | EY Q4-4 indicators (b)–(d) from Board / staff papers — labelled so. KPMG regulator statements shown as KPMG’s. |
| 7 | EY 5.1 locator “IFRS 18.BC53” for IAS 7.34A (BC53 = materiality) — not reproduced. KPMG three numerator types vs EY two (same content). IAS 7 / 33 / 34 paragraph numbers from firm text; amended texts not attached. |
| 8 | EY Ill 6-1 entity “Q” (Closer look) vs “A” (iGAAP) — pack uses Q. iGAAP section 7 ≠ Closer look section 7 — pack cites Closer look. KPMG: IFRS 18 silent on goodwill line in transition-year interim — shown as KPMG’s observation. |

**Invent check:** no true invent found or added. Named entities trace to Official IE (XYZ, AA–FF Groups) or EY Ill / KPMG Example facts. PwC absent — zero PwC cites. EY iGAAP 2026 Ch04 used for verification only — zero iGAAP chips. KPMG Insights 2019/20 not used (pre-IFRS 18).

---

## 6. Still NOT APPROVED — chips unchanged

| Ask | Item | Where |
|---|---|---|
| A1 | `IFRS 18 · para B… returns test` (truncated; proposed `para B45–B48`) | Ch3 3.9 index row, EY Ill 3-1 |
| A2 | `IFRS 18 · para IE Figure 5` (proposed `IFRS 18 · Figure 5`); bare `KPMG FI 2024` (proposed `· Foreword`) | Ch3 3.9 index row, EY Ill 3-8; Ch1 1.3.5 |
| A3 | EY iGAAP 2026 Ch04 chip format + References row | none added |
| A4 | `DTT A4 2022 · IAS 1 bridge` locator (proposed `· 8.1` / `· 1.1`); References DTT name | Ch1 ×2, Ch7 ×1 |
| S1 | Teach carried-forward material (paras 2–14, 25–40, 86–95, 107–116, 130–132; B1–B15, B86–B112) — locator-level only today (Ch1 1.3.2) | — |
| S3 | Point-chip clamp in `assets/shared.css` — CSS not edited. Measured at 1280: 25 of 26 point-chips still clamped (Ch1 2, Ch2 3, Ch3 4, Ch4 5, Ch5 5, Ch6 6); Ch8’s one rewritten point-chip fits; Ch7 has none. Text not shortened elsewhere (would cut detail) | Ch1–Ch6 |

---

## 7. Known debt (not done this job)

- **Concept Maps ch03–ch08:** labels and chips aligned (Gate 4), but no new nodes for the densified h4 units (e.g. Ch3 3.7, Ch5 5.1.3 / 5.2.1 / 5.3.3, Ch6 6.1.2 / 6.1.3 / 6.2.1 / 6.4.3). Adding nodes needs visual CSS layout work.
- **KPMG illustrative income statements** (general, banks, insurers, bancassurers) not reproduced as plates; bank shape taught from EY Figure C.2-1.
- Homepage link `../../homepage/homepage-wireframe-v0.1.html` resolves outside the pack (pre-existing; not a pack file).

---

## 8. Not touched

`assets/shared.css`, `assets/draft.css`, `assets/map.css`, every `visuals/*.css`, `refs/_shared/*`, all CF files, chrome tag rows, disclaimers, footers (except the stamp). `uploads/` and `ifrs18-ch3-extract/` not committed.

---

## 9. Screenshots (desktop 1280)

`/opt/cursor/artifacts/screenshots/` — `gate1/` (baseline), `gate2/` (Ch1), `gate2b/` … `gate2h/` (Ch2–Ch8: top + full + section / Illustration crops), `gate3/` (Map before / after, jumpboard), `gate4/` (all 10 visuals, References top + full, Ch2 2.3.6 link, Ch3 3.9 index, Ch1 / Ch2 heading form).

## 10. Re-check commands

```bash
cd refs/ifrs-18/draft-v1-linked
grep -c '§' index.html ch0*.html references.html visuals/*.html     # all 0
grep -o 'Last update · [0-9: -]* HKT' index.html ch0*.html references.html | sort -u -t: -k2
grep -c 'callout differ' ch0*.html                                   # all 0
```
