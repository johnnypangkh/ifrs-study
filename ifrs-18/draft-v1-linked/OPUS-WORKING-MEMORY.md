# IFRS 18 — Opus working memory

Two jobs are logged in this file. Job #8 (Opus densify) is on top; the Job #7 skill-align log is kept unchanged below it.

---

# Job #8 — Opus 5.5 high densify

**Runner:** Claude Opus 5.5 (high). Pack: IFRS 18 only. No CF. No IAS 2.
**Work tree:** `refs/ifrs-18/draft-v1-linked/` extracted from `ifrs18-draft-v1-linked-2026-10-02b.tgz` (stamp `Last update · 2026-10-02 16:20 HKT`). Shared chrome from `refs-shared-chrome.tgz` placed at `refs/_shared/` so `../../_shared/` resolves.
**Skills read in full:** teaching-body 2026.10.02c (file header; changelog includes 02b locks), teaching-body-qa 2026.10.02 (changelog 02b), visual-grammar 2026.10.02-23. Chrome module design 2026-10-02.

## Gate log

| Gate | Status | HKT | Johnny approval |
|---|---|---|---|
| 1 Overall review | done | 2026-10-02 ~16:55 | **approved** — Johnny: “Continue to Ch1 densify.” Cite asks A1–A4 not approved; S1/S2 guidance given; Bot answered B1/B2 |
| 2a Ch1 densify | done | 2026-10-02 17:20 | **approved** — Johnny: “Continue to Ch2 densify.” Cite Q1–4 still not approved; S3 CSS not approved (leave for consistency gate); Q5/Q6 as Ch1 |
| 2b Ch2 densify | done | 2026-10-02 17:40 | **approved** — Johnny: “Continue to Ch3 densify (incl. mba-nest / classification-path companions as needed).” Cite Q1–4 still not approved; S3 not approved; Q6 = banks/insurers as Ch3 subsections; expand EY Ill 3-x where source has case facts |
| 2c Ch3 densify | done | 2026-10-02 18:55 | **approved** — Johnny: “Continue to Ch4 densify only.” Cite Q1–4 / S3 still not approved; PwC missing; iGAAP Ch04 attached — use Ch04 for Ch4 content |
| 2d Ch4 densify | done | 2026-10-02 19:22 | **approved** — Johnny: “Continue to Ch5 densify only.” Cite Q1–4 / S3 still not approved; PwC missing; iGAAP Ch04 for verification only |
| 2e Ch5 densify | done | 2026-10-02 19:36 | **standing order** — Johnny: auto-continue Ch6 → Ch7 → Ch8 → Map/References consistency without waiting; short gate report per chapter |
| 2f Ch6 densify | done | 2026-10-02 19:45 | standing order — auto-continued to Ch7 |
| 2g Ch7 densify | done | 2026-10-02 19:56 | standing order — auto-continued to Ch8 |
| 2h Ch8 densify | done | 2026-10-02 20:02 | standing order — auto-continued to Map/References consistency |
| 3 Pack Map enhance | done | 2026-10-02 20:06 | standing order — auto-continued to Gate 4 |
| 4 Consistency pass | done | 2026-10-02 20:16 | standing order — auto-continued to Gate 5 |
| 5 KEY CHANGES handoff | done | 2026-10-02 20:16 | awaiting Johnny / Grok review |

**HTML edits at Gate 1: none.** Last update stamp not bumped (no content moved).
**Gate 2a (Ch1):** `ch01.html` teaching body rewritten/densified; pack-wide Last update stamp bumped to `2026-10-02 17:20 HKT` on all 10 pages (chrome line only on the other 9).
**Gate 2b (Ch2):** `ch02.html` teaching body + key terms rewritten/densified; pack-wide stamp bumped to `2026-10-02 17:40 HKT` on all 10 pages (chrome line only on the other 9).
**Gate 2c (Ch3):** `ch03.html` teaching body + key terms rewritten/densified; `visuals/ch03-classification-path.html` stem fixed (`?v=i18ch3path-4`); pack-wide stamp bumped to `2026-10-02 18:55 HKT` on all 10 pages (chrome line only on the other 9).
**Gate 2d (Ch4):** `ch04.html` teaching body + key terms rewritten/densified; Concept Map iframe untouched; pack-wide stamp bumped to `2026-10-02 19:22 HKT` on all 10 pages (Asia/Shanghai time = UTC+8, same offset as the existing HKT label; chrome line only on the other 9).
**Gate 2e (Ch5):** `ch05.html` teaching body + key terms rewritten/densified; Concept Map iframe untouched; pack-wide stamp bumped to `2026-10-02 19:36 HKT` on all 10 pages (Asia/Shanghai).
**Gate 2f (Ch6):** `ch06.html` teaching body + key terms rewritten/densified; Concept Map iframe untouched; pack-wide stamp bumped to `2026-10-02 19:45 HKT` on all 10 pages (Asia/Shanghai).
**Gate 2g (Ch7):** `ch07.html` teaching body + key terms rewritten/densified; Concept Map iframe untouched; pack-wide stamp bumped to `2026-10-02 19:56 HKT` on all 10 pages (Asia/Shanghai).
**Gate 2h (Ch8):** `ch08.html` teaching body + key terms rewritten/densified; Concept Map iframe untouched; pack-wide stamp bumped to `2026-10-02 20:02 HKT` on all 10 pages (Asia/Shanghai).
**Gate 3 (Map):** `index.html` board + `visuals/map-jumpboard.html` mirror updated to match densified chapters; pack-wide stamp bumped to `2026-10-02 20:06 HKT` on all 10 pages (Asia/Shanghai).
**Gate 4 (Consistency):** Ch1/Ch2 link text, all chapter visuals and `references.html` aligned to pack rules; pack-wide stamp bumped to `2026-10-02 20:16 HKT` on all 10 pages (Asia/Shanghai).

## Source-attach checklist (this run)

| Source | Layer | Status this run | Pack chip prefix |
|---|---|---|---|
| Official HKFRS 18 (= IFRS 18), Jun 2026 — Standard p1–67, BC p68–154, IE p155–193 (incl. Figures 1–8) | 1 | **attached**, scanned | `IFRS 18 · para …` / `IFRS 18 · Figure N` |
| EY International GAAP 2026 Ch04 (IFRS 18 + IFRS 19) | 2 (EY manual) | **attached**, scanned (TOC, App A/B indexes, spot sections). **New to the pack — zero chips today.** | none yet — see Ask A3 |
| EY Applying IFRS: A closer look at IFRS 18 (Updated April 2026) | 3 | **attached**, scanned (TOC, App A Ill index, App B FAQ index, App C banks, spot sections) | `EY Closer look 2026 · …` |
| KPMG First Impressions IFRS 18 (2024) | 3 | **attached**, scanned (TOC to 5th level, examples list, illustrative income statements) | `KPMG FI 2024 · …` |
| DTT iGAAP Vol A · A4 Presentation of financial statements (DART, Jun 2022) | IAS 1 bridge only | **attached**, scanned (TOC; section 8.1 Replacement of IAS 1) | `DTT A4 2022 · …` |
| KPMG Insights into IFRS 2019/20 | — | **Bot (locked):** on disk but **pre-IFRS 18 — not an IFRS 18 source.** Pack KPMG source = First Impressions 2024. No Insights IFRS 18 cites. | — |
| PwC IFRS 18 manual | 2 | **missing** — no PwC invent | — |
| Other EY iGAAP chapters | 2 | on disk elsewhere, **not attached** | — |
| Amended IAS 7 / IAS 8 / IAS 33 / IAS 34 Official text | 1 (cross-standard) | **not attached (Bot, locked).** HKFRS 18 App D (p67) says the amendments are incorporated into those Standards, so the attached PDF does not reproduce them. Keep existing chips; densify from the IFRS 18 narrative + FI/EY; ask before needing more PDFs. | `IAS 7 as amended`, `IAS 33 as amended`, `IFRS 18 · App D` |

## Shared-asset verification (HARD prerequisite) — PASS

All 10 live pages (`index.html`, `ch01`–`ch08`, `references.html`) link, in order: `../../_shared/tokens.css` → `chrome.css` → `cite.css` (all `?v=ifrs18-chrome-phase2-20261002f`) → `assets/shared.css` → `assets/draft.css` (`?v=ifrs18-skill-align-20261002b`) → `assets/map.css` on the Map only. Files resolve over HTTP from `refs/_shared/`. Visual iframes link `visuals/shared.css` + their own CSS (expected). Only unresolved href: `../../homepage/homepage-wireframe-v0.1.html` (site Home, outside this pack; pre-existing chrome).

## Gate 1 — overall review findings (internal notes)

### A. Coverage vs Official (cite-chip scan, all chapters)

- Main paras cited 88/132. **Uncited:** 2, 6–14 (scope, objective of FS, complete set), 25–29 (identification, frequency), 32–40 (comparatives), 46, 77, 86–95 (statement presenting comprehensive income / OCI), 113–116 (notes structure), 129–132 (capital tail, other disclosures).
- App B cited 99/142. **Uncited:** B1–B7 (materiality, roles), B10–B13 (identification, consistency, comparatives), B27–B28 (offsetting), B77–B79 (P&L line items), B86–B112 (OCI, current/non-current, SFP line items, notes structure).
- App C 8/8. IE paras 17/17. IN 14/19 (IN1, IN2, IN13, IN18, IN19 uncited). BC 71 distinct paras cited (BC heavy only in BC84–BC91, BC246–BC275, BC325–BC387).
- **IE Figures:** 2, 3.1, 3.2, 3.3, 4, 5, 6, 7 cited. **Figure 1 (IFRS 18 on one page) and Figure 8 (useful structured summary and the materiality process) uncited.**
- **IE Part I Notes 3–4** (reclassification adjustments; tax effects on OCI), the statement presenting comprehensive income and the SCE are not taught anywhere.
- Most of the uncited block is IAS 1 material carried forward. Pack identity so far = "new requirements" (same stance as EY iGAAP Ch04 overview: carried-forward IAS 1 material only where needed for context). **Scope question for Johnny (Ask S1)** — do not add a new chapter without approval.

### B. Coverage vs firms

- **KPMG FI 2024** — Examples 1–5 all present (1–3 merged into one plate 3.5.4; 4 = 5.1.2; 5 = 2.3.1, also pointer in Ch7). **Uncited sections:** 1.2 key actions; 2.1.1.2–2.1.1.3 (investing MBA assessment; change in assessment); 2.1.3.1–2.1.3.2 (MBA specific requirements); 2.1.5 (derecognition / change in classification); 2.2.3 (change in opex presentation method); 3.4 (interaction with regulatory requirements); 5.1.1 (interest and dividend cash flows); 5.2 balance sheet; 5.3 EPS; 6.1 interim; **8.1 banks and 8.2 insurers (p69–84) entirely uncited**. **4 illustrative income statements** (general — section 2; retail/investment banks — 8.1.1.1; insurers — 8.2.1; bancassurers — 8.2.5) not in the pack.
- **EY Closer look 2026** — Illustrations: 2-1, 2-2, 3-10, 3-12, 3-13, 4-1, 5-1, 6-1 have plates; 5-2 + 5-3 merged into one plate (7.3.1); **3-1 to 3-9 and 3-11 exist only as one-paragraph sketches in the `#s-3-9-ey` index grid** (chips inside box bodies; some sketch text is hedged or unverified, e.g. Ill 3-8 "Based on IFRS IC discussion path", Ill 3-4 "per B48-style guidance"). **FAQs: only Q3-43, Q4-1, Q4-4, Q4-6 carry a chip** out of Q2-1…Q5-2 (~60) plus Appendix C bank FAQs. Term scan: money-market funds, finance leases, contract liabilities, time value, service concessions, intercompany FX, hyperinflation / net monetary position, business combinations, separate FS, realised vs unrealised, "what-if" APMs = zero or near-zero hits. **Appendix C (banks) and Appendix D (defined terms) uncited.** Sections uncited: 1.1–1.3, 2.1.2–2.1.3, 2.2.3, 3.2.6 (derecognition / change in classification), 3.2.7, 3.2.8, 3.3.1–3.3.6 (only via Ill), 3.4.1, 3.4.3 (NCI), 3.5 (non-recurring items prose), 4.3.1, 4.3.4, 4.3.5, 5.3, 5.4, 7.
- **EY iGAAP 2026 Ch04** — not in pack. Structure mirrors Closer look sections 1–7 (+ section 8 IFRS 19 — out of IFRS 18 scope). It is the older, smaller EY text: Ch3 Ill 3-1…3-9 vs Closer look 3-1…3-13; FAQs Q3-1…Q3-28 and Q4-1…Q4-5 vs Closer look Q3-1…Q3-43 and Q4-1…Q4-8. **Numbering trap: iGAAP Ill/Q numbers ≠ Closer look numbers** (e.g. iGAAP Ill 3-1 incremental acquisition costs = Closer look Ill 3-2; iGAAP Q3-1 = Closer look Q3-6). Spot check (PPE operating-lease rental income, finance-lease income, returns test): **same view, Closer look adds entity facts** (e.g. Entity L, Entity C excavator Q3-7, Entity R). No EY-vs-EY difference found yet. Rule for densify: write once; both EY chips where both texts support; Closer-look-only FAQs carry only the Closer look chip.
- **DTT A4 2022** — chips use locator `IAS 1 bridge`, which is not a section. Real sections exist (e.g. 1.1 Overview of IAS 1; 8.1 Replacement of IAS 1). Ask A4.

### C. Wrong-shape vs true invent (classified separately)

- **True invent:** none found. Named entities on plates trace to Official IE (XYZ, AA–FF Groups) or EY Ill / KPMG Example facts where checked. Ch1 Concept Map "Prepare — category mapping · MPM inventory · systems" node has no chip — verify against KPMG FI 1.2 key actions at Ch1 gate before calling anything.
- **Wrong-shape candidates (fix at chapter gates, keep ids):**
  - Ch1 `s-1-3-ex` "Teaching cue" `.worked-strip` (Firm observation / Standard aim / Conclusion) — firm quote + Official restatement, no case facts; author meta "No invented entity fact pattern" in the Conclusion peer; bare `KPMG FI 2024` chip inside box body.
  - Ch3 `#s-3-9-ey` EY index grid — not wrong-shape for content (EY Ills have entity facts = true Illustrations) but wrong **format**: 12 sketches in one strip, chips in bodies. Fix = full `.worked-strip` Illus at each home section.
  - Ch3 3.5.4 merges KPMG Examples 1–3 (three named examples) into one plate; Ch7 7.3.1 merges EY Ill 5-2 + 5-3. Split so each named example is its own plate.
  - Ch8 `s-8-3-appc` and `s-8-4-kpmg` single-column worked-strips (not Illus) — convert to plain section units.
  - "Decision strip" `.worked-strip` units (Ch2 2.4, Ch3 3.5, Ch4 4.4, Ch5 5.3, Ch6 6.4, Ch7 7.1, Ch8 8.4): Start | Decision | Output peers. The Decision peer is a statement, not a question with arms → fails body mini-flow grammar (question never shares a box with outcomes; decision = question + labelled arms). Several repeat a table or companion visual already on the page (Ch3 3.5 shows the same ordered tests three times: companion diagram + table + strip). Fix at each gate: one mini-flow per decision, write-once.
- **Case-study Illus kept (24):** no new wrong-shape found in spot reads (4.2.1 DD Group uses IE13 facts). 4.2.1 duplicates DD facts from 3.8.4 → home-chapter write-once.

### D. Structure / placement

- **Illustrations parked at chapter end, away from their numbered home section:** Ch2 2.1.1, 2.1.2, 2.3.1 sit under §2.5; Ch3 3.5.4, 3.5.5 sit under §3.8 and h4 3.4.2 sits under §3.5; Ch4 4.1.1, 4.2.1 under §4.5; Ch5 5.1.1, 5.3.1, 5.1.2, 5.2.1 under §5.4 (also out of numeric order); Ch6 6.4.1, 6.4.2 under §6.6. Fix = move to home section, keep ids, hyperlink review.
- **Demoted figure units (Job #7)** still repeat list + table (Fig 2, 3.1, 3.2, 3.3, 4, 5, 6, 7). Collapse write-once; keep the four unique list-only lines named in the Job #7 log below.
- **Ch2 Illus grid** renders Facts + Assessment in two of three grid tracks (empty right third) — layout debt; check `worked-strip-grid` column count when 2 peers.
- **Duplication:** Ch1 DTT pitfall appears as bullet + point-chip; Ch1 "operating is default" quote appears in table + point-chip; Ch2 Illus 2.1.1 Assessment bullets repeat its table.

### E. Language / title / meta

- **Source-label leads** (title-essence FAIL): Ch1 has 18 (`Standard:`, `Firms (aligned):`, `Standard + firm (aligned):`, `Standard BC spine:`); Ch5 1. Other chapters clear.
- **Hedge / author-meta in reader headings and text:** "(thin)", "thin bridge", "thin pointer", "cue", "orientation only", "Optional teaching prompts (not a Board flowchart)", "Picture 1 / Picture 2", "(no invented entity facts)", "Deep detail can wait for a later pass", "Bank / insurer line-item detail stays for later", "PwC IFRS 18: not in pack (Johnny 2026-09-27…)", "Quote-heavy firm worksheets remain in the EY PDF". ~24 "thin" hits pack-wide incl. Map ("thin IAS 7 bridge") and Ch1/Ch7 visuals.
- **Technical-strict:** Map and Ch1 Concept Map say "Single audited note" / "single audited note" — IFRS 18 says single note (para 122); "generally subject to audit" is a firm observation. Flag for Ch1 and Map gates.
- **§ in prose** (not chips): Ch3 ≈160, Ch6 ≈91, Ch4 ≈70, Ch5 ≈48 (+ Map text "§118", "§C3", "§C4–C5"). visual-grammar F4: § only as fb-num circle chrome on Maps, never in text. Body sweep optional per Big Pass; Map text items fixed at Map gate.
- **Gate word:** ch03 = 0 (Job #7). Remaining reader-visible: `visuals/ch05-operating-expenses.html` `aria-label="Gate — any function line on the face"` (QA C3 counts aria). Classes `pc-gate`/`oe-gate`/`gt-gate` are not reader text.

### F. Cite integrity (no rename done — all ASK)

| Where | Current chip | Proposed (from source) | Evidence |
|---|---|---|---|
| Ch3 `#s-3-9-ey` Entity C, EY Ill 3-1 | `IFRS 18 · para B… returns test` | `IFRS 18 · para B45–B48` (alt: `IFRS 18 · para B48(a)–(b)` + `IFRS 18 · para BC142`) | Official B45 (returns test; return positive or negative), B46 (typical assets), B47 (income/expenses), B48(a)–(b) (assets used in combination; receivables from operating activities). EY Ill 3-1 itself cites IFRS 18.B48(a), B48(b), BC142(a)–(b). |
| Ch3 EY Ill 3-8 sketch | `IFRS 18 · para IE Figure 5` | `IFRS 18 · Figure 5` | Figure 5 is in the IE supporting materials; the pack already uses `IFRS 18 · Figure 5` elsewhere in Ch3. |
| Ch1 `s-1-3-ex` | `KPMG FI 2024` (no locator) | `KPMG FI 2024 · Foreword` | Quote "Although companies' net profit will remain unchanged…" is on KPMG p3 "Re-shaping financial statement presentation" — the page the pack already chips as `Foreword`. |
| Ch1, Ch7 | `DTT A4 2022 · IAS 1 bridge` | `DTT A4 2022 · 8.1` (Replacement of IAS 1) or `· 1.1` (Overview of IAS 1) | DTT A4 TOC. |
| New source | — | `EY iGAAP 2026 Ch04 · section …` / `· Ill N-N` / `· Q N-N` | teaching-body chip grammar (`EY iGAAP 2026 Ch23 · section 2.3`). New work string → ask. |
| References | heading "Big 4 firm manuals"; DTT full name "Deloitte (DTT) iGAAP / Manual of Accounting — A4…" | split layer 2 manual vs layer 3 technical reference; DTT full name "Deloitte iGAAP · Volume A — A guide to IFRS reporting · A4 Presentation of financial statements (DART, 2022)"; add EY iGAAP 2026 row once chipped | KPMG FI and EY Closer look are layer-3 technical references; "Manual of Accounting" is not the DTT title on the PDF. |
| Ch7 | `IFRS 18 · App D`, `IAS 7 as amended`, `IAS 33 as amended` | keep until amended IAS texts are attached | App D text not reproduced in attached Official. |

### G. `.callout.differ`

Zero today. **No verified firm difference yet.** Candidates to test against source text at the chapter gates (no callout unless the texts actually differ): transaction costs on acquiring investments (KPMG 2.1.2.2 table vs EY Q3-9/Ill 3-2); subsidiary- vs group-level MBA assessment (KPMG Examples 1–2 vs EY Q3-22/Q3-23); separate-FS cost-method subsidiaries (KPMG 2.1.1.1 vs EY Q3-24); OPDAI and impairment reversals (KPMG 2.3.4 vs EY Q4-6); interest on contract liabilities with a significant financing component (EY Q3-11 vs KPMG 2.1.2.3 "other liabilities"); EY iGAAP vs Closer look wording on the same FAQ.

### H. Map (index + jumpboard) — Map gate items, not edited now

- Board = Map inline in `index.html`, mirrored by `visuals/map-jumpboard.html` (same text).
- Visit strip 1→8 wraps at 1280: "→" after "Other FS" ends the line and "8 Transition" starts a new line alone — orphan arrow / broken L→R walk.
- Node text uses § ("§118", "§C3", "§C4–C5"); "thin IAS 7 bridge"; See-also "(later; overview in Ch3)"; "Single audited note".
- MPM pillar boxes mostly empty space (box fit).
- No chip-order lecture note (PASS). Official Figure 1 "IFRS 18 on one page" is a sourced story candidate for the Map.

### I. Ch3 companions — Ch3 gate items

- `ch03-classification-path`: the "NO → RESIDUAL" stem starts from the 3.5 MBA note box, not from the last decision (orphan stem through a note); category leaves carry fills (green Investing, gold Financing, purple Discontinued) — visual-grammar: colour only with a one-line meaning, no green by default. Test order vs Official Figure 2 to verify.
- `ch03-mba-nest`: containment reads correctly; "Why only these two?" side card uses warn fill.

### J. Densify priority (proposed for Gate 2 onward, in gate order)

1. Ch1: Figure 1; full carry/move list (KPMG Appendix + EY iGAAP/Closer look 1.1–1.3 + IN1–IN2/IN13/IN18–IN19); KPMG 1.2 key actions; fix leads/meta; Ask S1 outcome.
2. Ch2: Figure 8; B1–B7 materiality/roles; EY 2.1.1.A required line items, 2.1.1.B, 2.1.2, 2.1.3 cross-references; EY 2.2.2.A/B characteristics examples (iGAAP); Q2-1, Q2-2; offsetting B27–B28; move Illus home.
3. Ch3 (largest): 10 EY Ills as full plates at home sections; Closer look FAQs Q3-1…Q3-42 by home section; KPMG 2.1.1.2–2.1.1.3, 2.1.3, 2.1.5; FX (B65–B69 + EY 3.2.7 incl. hyperinflation) and derivatives (EY 3.2.8 A–D) replacing the "thin" stance; KPMG Examples 1–3 split; KPMG illustrative income statements (general) + banks/insurers/bancassurers (section 8) + EY Appendix C banks — home = Ch3 §3.5 or a new §3.10, Johnny to choose (Ask S2).
4. Ch4: EY 3.4.1, Q3-18 (alternative labels for operating profit), Q4-5/Q4-6 interplay; DD write-once with Ch3.
5. Ch5: KPMG 2.2.3; EY Q3-43 retained; EY 3.4.2.A–E vs iGAAP; 3.4.3 NCI; 3.5 non-recurring prose; aria Gate fix.
6. Ch6: EY Q4-2, Q4-3, Q4-5, Q4-7, Q4-8; 4.3.1, 4.3.4, 4.3.5; KPMG 3.4 regulatory; B113–B142 check.
7. Ch7: KPMG 5.1.1, 5.2, 5.3, 6.1; EY 5.2 IAS 8, 5.3, 5.4; capital 129; EY Ill 5-2/5-3 split; amended IAS text status.
8. Ch8: EY 6.1 + 7 future developments; KPMG 6.2/7.2 into plain section; Q4-8 cross-pointer.

### Crosswalk A/B

Still open. Plan: build `Crosswalk A — Official → Big4` and `Crosswalk B — Big4 → Official` chapter by chapter in the CONTENT-NOTES during Gate 2, using the coverage scans above as the row skeleton (layer 2 = EY iGAAP Ch04; layer 3 = EY Closer look, KPMG FI; KPMG Insights / PwC rows = explicit gaps).

## Screenshots — Gate 1 (desktop 1280, `/opt/cursor/artifacts/screenshots/gate1/`)

`g1-map-desktop-{top,full}.png`, `g1-map-jumpboard-desktop-*`, `g1-ch01…ch08-desktop-{top,full}.png`, `g1-ch03-mba-nest-desktop-*`, `g1-ch03-classification-path-desktop-*`, `g1-references-desktop-*`, element crops `g1-ch02-s25-illus-tail.png`, `g1-ch03-s35-decision-strip.png`, `g1-ch03-s39-ey-index.png`, `g1-ch06-s66-illus-tail.png`. Local preview: `python3 -m http.server 47318` from repo root → `/refs/ifrs-18/draft-v1-linked/index.html`.

## Open asks (Gate 1)

- **A1** Entity C chip → `IFRS 18 · para B45–B48` (or B48(a)–(b) + BC142)?
- **A2** `IFRS 18 · para IE Figure 5` → `IFRS 18 · Figure 5`; bare `KPMG FI 2024` → `KPMG FI 2024 · Foreword`?
- **A3** Adopt `EY iGAAP 2026 Ch04 · section … / Ill … / Q …` chips + References row?
- **A4** DTT `IAS 1 bridge` locator → `DTT A4 2022 · 8.1` (or 1.1)? References DTT full name + layer split?
- **S1** Scope: add carried-forward IFRS 18 requirements (paras 2–14, 25–40, 86–95, 107–116, 130–132; B1–B15, B86–B112; IE statement of comprehensive income, SCE, Notes 3–4) — as a locator-level carry table in Ch1 only, or as full teaching (new chapter / Ch7 extension)?
- **S2** Home for banks/insurers material (KPMG section 8 + 3 illustrative income statements; EY Appendix C): Ch3 sub-section, or a new sub-section after Ch3 §3.8?
- **B1** KPMG Insights into IFRS (layer 2) — attached anywhere? If not, record `not attached` for the crosswalk.
- **B2** Amended IAS 7 / IAS 8 / IAS 33 / IAS 34 texts — attach for Ch7, or keep current chips unchanged?

### Answers received with Gate 1 approval

- **A1–A4: NOT approved.** Do not change any cite chips (Entity C, IE Figure 5, KPMG bare chip, EY iGAAP, DTT) until Johnny answers. Leave truncated/broken chips as-is; list them again at every gate.
- **S1 (Q5):** for Ch1, prefer a paragraph-reference table / bridge over full teaching unless densify clearly needs an Official IE plate; flag if a fuller pass is needed.
- **S2 (Q6):** do not create a banks/insurers subsection yet; note for later. Bank/insurer densify stays for Ch3+ after Johnny picks placement.
- **B1 (locked):** KPMG Insights 2019/20 is pre-IFRS 18 — not a source. KPMG = FI 2024 only.
- **B2 (locked):** amended IAS 7/8/33/34 not attached; keep existing chips; densify from IFRS 18 narrative + FI/EY.

## Gate 2a — Ch1 densify (2026-10-02 17:20 HKT)

**Scope kept:** `ch01.html` teaching body + key terms only. Concept Map iframe (`?v=i18ch1-2`), chrome, disclaimer, footer untouched (except pack-wide stamp). No new `h3`; new units are `h4` under existing `#s-1-*` (CONTENT-NOTES “do not split Ch1 sections”). All old ids kept (`s-1-0` … `s-1-5`, `s-1-3-ex`, `s-1-5-ex`).

**Sources read for Ch1 before writing:** Official IN1–IN17, paras 1–15, 25–27, 103(d), C1–C6, B10, BC1–BC16, BC117–BC119, BC314, BC410–BC417, BC424–BC425, App A, Figure 1; KPMG FI p3 (Foreword page), 1.1, 1.2, Appendix p85; EY Closer look Overview pp3–4, sections 1, 1.1, 1.2, 1.3; EY iGAAP Ch04 “What you need to know”, sections 1, 1.1–1.3; DTT A4 1.1 and 8.1.

**Metrics (before → after):** article text 17.7k → 47.5k chars; chips 97 → 227 (distinct 53 → 129); h4 units 1 → 8. Source-label leads 18 → 0; author-meta hits → 0; Gate 0; `§` in chips 0; plain “see N.N” 0; `<p class="box-body"><ul>` 0; HTML balanced; all in-page and cross-chapter anchors resolve. **Every pre-existing chip string still present** (one bullet split was reverted to keep `IFRS 18 · para IN10–IN11` unchanged).

**What changed (by unit):**
- **1.0** objective + scope: para 1/IN1, para 2 (+ EY 1.1: same objective as IAS 1; consolidated and separate FS), para 4; new scope table paras 3, 5, 6, 7, 8 with EY 1.1 effects + chapter links. Supersession bullets: leads rewritten. DTT bullet now carries DTT A4 1.1 IAS 1 baseline content under the **unchanged** `DTT A4 2022 · IAS 1 bridge` chip; pitfall point-chip unchanged. PwC author-meta bullet removed (References already states PwC not on disk).
- **1.1** leads rewritten (no `Standard:` / `Firms (aligned)`); BC3(a) adds same-label diversity + buy-side investors; BC3(c) adds APM/non-GAAP naming + forecasting use; KPMG Foreword adds consistency of measures, credibility of KPIs, connected reporting; EY section 1 adds Primary Financial Statements project (2014) and targeted-improvement stance. **New 1.1.1** Exposure Draft → final: BC4–BC6, BC12–BC13 bullets + 6-row table (ED proposal | feedback | final) from BC7–BC11, BC14–BC16, BC117–BC119, BC410–BC413, IN8, IN14–IN17, KPMG 1.1.
- **1.2** leads rewritten; pervasive-impact bullet (BC415, KPMG 1.1, EY Overview). Table: IN9 last sentence; IN10–IN11 full content; IN13 FX/derivatives/hybrids (+KPMG 1.1); IN17 specified expenses; KPMG 1.1 reporting-entity-level MBA + opex method choice; “KPMG only” label on “other” removed (EY section 1 also lists informative labels) → write-once with both chips; MPM: para 5 interim, KPMG Foreword credibility, EY Overview IAS 34 parity. Operating-default point-chip shortened to a tip (quote kept once in the table). **New 1.2.1** implementation effects (BC415, EY Overview/section 1, KPMG Foreword) + KPMG 1.2 key-actions table (6 areas → chapter links).
- **1.3** title “What carries / what moves (thin)” → “What carries forward and what moves”. Duplicate para 4 quote removed here (kept once in 1.0); SCF para 3 quote moved to the 1.0 scope table and IAS 7 row of 1.3.3. **New 1.3.1** Figure 1 “IFRS 18 on one page” bridge table (13 rows, paragraph ranges as printed, goodwill 103(d)/BC314). **New 1.3.2** = Q5 paragraph bridge: full KPMG Appendix IAS 1 → IFRS 18 / IAS 8 / IFRS 7 table (27 rows) replacing the 6-row “illustrative” table (all its chips kept on the lead/rows). **New 1.3.3** consequential amendments (IAS 7, IAS 8, IFRS 7, IAS 33, IAS 34; BC425 compliance references). **New 1.3.4** terminology + identification (paras 10–15, 25–27, B10, App A, BC424; EY 1.2–1.3 incl. Trade Mark Guidelines / compliance statement view).
- **1.3.5 (`#s-1-3-ex`)** wrong-shape “Teaching cue” worked-strip → plain `h4` + 4 bullets. Bare `KPMG FI 2024` chip **text unchanged**, moved to end of its bullet (C2). Added KPMG Foreword “no live benchmark”. Author meta “No invented entity fact pattern…” removed.
- **1.4** “Effective date cue” → “Effective date and transition”: IN2, BC414/BC416 rationale, EY Overview same-time adoption, C2 + BC417, C3, C4–C6 detail; Ch8 link.
- **1.5** “(orientation only)” / “(thin)” removed; `§` in IE map text → “para(s)”; see-also callout now links Ch3 §3.5 (text “later” removed). Banks/insurers: **no new subsection (S2)** — note for later.

**Q5 outcome:** paragraph-reference bridge (1.3.1 Figure 1 + 1.3.2 KPMG Appendix) was enough for Ch1. **No Official IE plate needed.** Fuller teaching of carried-forward material (S1 full option) is still Johnny’s call — not done.

**EY iGAAP Ch04 (A3 pending — zero chips added):** sections 1, 1.1, 1.2, 1.3 match Closer look sections 1, 1.1, 1.2, 1.3 word-for-word in substance (iGAAP omits the single/two-statement para 12 extract in 1.2 and adds IFRS 19 in “What you need to know”, out of scope). **No iGAAP-only Ch1 content.** If A3 is approved, add `EY iGAAP 2026 Ch04 · section 1 / 1.1 / 1.2 / 1.3` beside every Ch1 `EY Closer look 2026 · section 1 / 1.1 / 1.2 / 1.3` chip, and iGAAP “What you need to know” beside the Overview chips that cover retrospective application in annual and interim FS (1.4).

**DTT A4 (A4 pending — zero new DTT chips):** A4 8.1 (ED/2019/7 proposals: three categories, three subtotals, opex method with indicators, goodwill separate, integral/non-integral JVs, unusual items single note, MPM single note) corroborates 1.1.1, which is cited to Official BC only. If A4 is approved, add `DTT A4 2022 · 8.1` to the 1.1.1 lead and retarget the two Ch1 `IAS 1 bridge` chips (`· 1.1` for the IAS 1 baseline bullet).

**Firm differences checked for Ch1 — none.** KPMG 1.1 / EY Overview / EY section 1 align on the three sets, IAS 1 carry-forward, MPM audit status, IAS 7 changes, effective date. “Other” labelling is in both (KPMG more specific) — not a difference. No `.callout.differ`.

**Concept Map debt seen (Map gate, not edited):** map shows `§` chips (`§47`, `§69`, `§C1` …), “Effective-date cue” label vs page 1.4 “Effective date and transition”, “Prepare” node with no chip. “Single audited note” is supported by KPMG 1.1 (“single note … subject to audit”) — wording OK, chip missing.

**New pack-wide debt found (consistency gate):** `.point-chip` in `assets/shared.css` is `white-space:nowrap; overflow:hidden; text-overflow:ellipsis` — **24 of 25 teaching point-chips are visually truncated** (Ch1 2/2, Ch2 3/3, Ch3 4/4, Ch4 4/4, Ch5 5/5, Ch6 6/6; Ch8 0/1). Skill expects the teaching body to override to block + wrap. Not fixed (no shared-CSS edits). **Ask S3.**

**Screenshots — Gate 2a** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2/`): `g2-ch01-desktop-{top,full}.png`; crops `g2-ch01-s10-scope`, `-s11-why`, `-s111-ed-to-final`, `-s12-three-sets`, `-s121-actions`, `-s131-figure1`, `-s132-ias1-bridge`, `-s133-s134-amend-terms`, `-s135-s14-netprofit-effective`, `-s15-ie-map-tail`.

**Chips listed again (unchanged, still awaiting A1–A4):**
- Ch3 Entity C — `IFRS 18 · para B… returns test` (truncated).
- Ch3 EY Ill 3-8 sketch — `IFRS 18 · para IE Figure 5`.
- Ch1 §1.3.5 — bare `KPMG FI 2024` (no locator; text is on the KPMG p3 “Re-shaping…” page the pack calls Foreword).
- Ch1 ×2 + Ch7 ×1 — `DTT A4 2022 · IAS 1 bridge` (not a section).
- EY iGAAP Ch04 — no chip format yet (zero chips).

**New ask:**
- **S3** Point-chip truncation: allow a pack-local teaching override (e.g. in `assets/draft.css`: `.teaching .point-chip{display:block; white-space:normal; border-radius:10px}`) at the consistency gate, or leave as designed?

### Answers received with Gate 2a approval
- Cite Q1–4 (Entity C, IE Figure 5, KPMG bare chip, EY iGAAP format, DTT locator/References): **still not approved** — leave chips unchanged; re-list at each gate.
- **S3:** do **not** change `shared.css` or `draft.css` yet; leave for the consistency gate after Johnny decides.
- **Q5/Q6:** same as Ch1 — no banks/insurers subsection; no PwC invent.

## Gate 2b — Ch2 densify (2026-10-02 17:40 HKT)

**Scope kept:** `ch02.html` teaching body + key terms only. Concept Map iframe (`?v=i18ch2-2`), chrome, disclaimer, footer untouched (except pack-wide stamp). No new `h3` (CONTENT-NOTES “do not split”); new units are `h4` under existing `#s-2-*`. All old ids kept (`s-2-0` … `s-2-5`, `s-2-1-ex`, `s-2-2-ex`, `s-2-3-ex`, `s-2-4-ex`, `s-2-4-fig7`); inbound links (Ch1 ×14 to `#s-2-1`, etc.) still resolve. Backup: `/tmp/g2/ch02-before.html` (not committed).

**Sources read for Ch2 before writing:** Official paras 15–24, 41–45, 113–116, B1–B28, B78–B79, B85, B109–B112, BC45–BC63, BC71–BC80, BCZ322, BC324, BC315, App A, Figures 7–8; KPMG FI section 4 intro, 4.1, 4.2 (incl. Examples 4–5, fn 16), 4.3 (pp55–62); EY Closer look section 2 (pp10–28: 2, 2.1–2.3.1, Ill 2-1/2-2, Q2-1/Q2-2, Fig 2-1); EY iGAAP Ch04 section 2 (verification only); DTT A4 2.7 materiality/aggregation and 2.8 offsetting (verification only).

**Metrics (before → after):** article text 19.0k → 51.0k chars (2.9k → 7.7k words); chips 99 → 318 (Official 72 → 227, KPMG 12 → 30, EY 15 → 61); h4 units 1 → 13. Source-label leads → 0; author meta → 0 (“thin bridge”, “Teaching.”, “Aligned firm read.” removed); Gate 0; `§` in chips 0 (3 `§` are Ch3/Ch4/Ch7 link texts, Ch1 style); plain “see N.N” 0; bare work chips 0; non-Illus worked-strips 0; HTML balanced; anchors resolve. **Every pre-existing chip string still present** (multiset check: missing = none).

**What changed (by unit):**
- **2.0** fourth decision bullet (labels: 43, B25, KPMG 4.3, EY 2.3); first decision adds BC53 whether-not-where (+KPMG 4.1, EY section 2). **New 2.0.1** materiality: B1, B2 + BCZ51, B4–B5, BCZ50; B3(a)–(e) obscuring table → linked controls; **Figure 8** Step 1–4 table (Practice Statement 2 paras 56/58 as printed in the figure).
- **2.1** table headers “Teaching test / Aligned firm read” → “Location test / Practical consequence” (cells unchanged). **Illus 2.1.1 moved home** under 2.1; Facts/Assessment/Decision peers; duplicate three-aspect table merged into Assessment bullets (full EY/BC55 wording kept); “Aligned firm read.” meta → “Material does not mean an automatic face line”; title chips + BC55, para 114. **New 2.1.2** why roles exist (BC45, BC46, BC49, BC62–BC63, BC54, para 41 item vs line item). **New 2.1.3** notes table B6/B7 + KPMG examples (inventory WIP/FG, contingent-consideration assumptions, risk exposures) + paras 113, 115, 116. **New 2.1.4** cross-references (114 new note→line-item link, BC324, EY 2.1.3 view), BCZ322 ordering, B112 table.
- **2.2** structure bullet now lists para 22(a)–(e) + BC56; “Firm alignment.” lead → “More or fewer line items — it depends…”. **New 2.2.1** paras 75/103/103(d)/96, EY two-step table (19, 23, B8, 42), BC57, BC58 IFRS 9 impairment, KPMG specific line items, EY “difficult judgements”. **New 2.2.2** para 24(a)–(d) table (EY: IAS 1 subtotal precedent, “in accordance” unexplained, ‘gross profit net of income taxes’ conflict; para 30), BC60, BC61, EY factors + regulators; Ch4 §4.5 link. **New 2.2.3** EY Q2-1 realised/unrealised FV gains — plain `h4` unit (FAQ ≠ Illus).
- **2.3** leads rewritten; 41(e) + specific-requirements override; BC73 example; B21 dissimilar-in-line-items (KPMG 4.2, EY 2.2); App A definitions table (item, line item, classification, aggregation, disaggregation); BC71, BC72, BC75 (+KPMG Q&A grouping may change), BC74; BC76 added to lens table. **Illus 2.1.2 → 2.3.1** moved home (B23), Facts/Assessment/Outcome; duplicate step table merged into Assessment; “Teaching.” meta removed; title + B23. **New 2.3.2** characteristics table B78(a)–(i) × B110(a)–(k) with EY 2.2.2.A examples; B109 + BC315. **New 2.3.3** B79(a)–(h) / B111(a)–(f) table; KPMG non-recurring Q&A; ‘unusual’ (BC78, KPMG). **Illus 2.3.1 → 2.3.4** (reverse factoring) placed after B111(d); Outcome box; fn 16 terms; title + B111(d). **New 2.3.5** B85 opex aggregation — KPMG Example 4 summary linked to Ch5 Illus 5.1.2 (not duplicated) + EY 2.2.3 view. **New 2.3.6** EY Q2-2 FX same/separate line (plain unit; Ch3 §3.1 link; IAS 21.52 mentioned as EY’s reference — no IAS 21 chip, text not attached).
- **2.4** BC77–BC78 complete descriptions; “Firm alignment.” → “‘Other’ is permitted but discouraged” + BC79; KPMG label tip merged into the “other” decision table (write-once). **Decision strip `#s-2-4-ex` → `h4` 2.4.1** stage table (wrong shape, not invent; all chips kept). **2.4.1 → 2.4.2 `#s-2-4-fig7`**: duplicate Figure 7 bullets folded into the table; “Official Figure 7 —” / “Teaching:” leads removed; chip-only paragraph → lead paragraph; BC80 rationale; KPMG flowchart noted as same path.
- **2.5** title “Offsetting — thin bridge” → “Offsetting”; para 45 harm + valuation allowances; B27 (IFRS 15 discounts/rebates; (a) disposals; (b) reimbursed provisions), B28 (FX, trading; separate note if material) table. “The Big4 explanation treats…” → neutral (only EY says it; DTT A4 2.8 corroborates IAS 1.32–33 = IFRS 18.44–45).

**Illustration renumbering (titles only, ids unchanged):** 2.1.1 stays 2.1.1 (`#s-2-1-ex`); 2.1.2 → **2.3.1** (`#s-2-2-ex`); 2.3.1 → **2.3.4** (`#s-2-3-ex`). No reader page or visual referenced the old numbers; MD notes that list “2.1.1, 2.1.2, 2.3.1” (I18-BIG-PASS, I18-DEBT-INVENTORY, Job #7 log) are historical — update at consistency gate if wanted. KPMG Example 5 now = Illus 2.3.4.

**EY chip locator observations (not changed — cite lock):** `EY Closer look 2026 · Ill 2-1 / section 2.1` — Ill 2-1 sits in 2.1.1; `· Ill 2-2 / section 2.2` — Ill 2-2 sits in 2.2.2. Both point to the parent section, so not wrong; flag only.

**EY iGAAP Ch04 (A3 pending — zero chips):** section 2 numbering is identical to Closer look (2.1, 2.1.1, 2.1.1.A, 2.1.1.B, 2.1.2, 2.1.3, 2.2, 2.2.1, 2.2.2, 2.2.2.A, 2.2.2.B, 2.2.3, 2.3, 2.3.1); Ill 2-1 (PDF p12), Q2-1 (p15), Ill 2-2 (p19), Q2-2 (p20), “size” (p21), B85 view (p22). Substance identical; minor wording only (“will not always” vs “do not always need to be”; Q2-1 policy bullet shorter). **No iGAAP-only Ch2 content.** If A3 approved: add `EY iGAAP 2026 Ch04 · section 2.x` beside every Ch2 Closer look chip with the same section number.

**DTT A4 (A4 pending — zero DTT chips in Ch2):** 2.7 materiality (incl. 2.7.3.4 Practice Statement 2 four-step approach — corroborates the Figure 8 steps) and 2.8 offsetting (IAS 1.32–33 + IFRS 15 incidental-transaction netting — corroborates B27). DTT 2.8-1 withholding-tax example is IAS 1-era; not used.

**Firm differences checked for Ch2 — none verified. No `.callout.differ`.**
- B85 selling vs admin: KPMG Example 4 separates “in its circumstances”; EY 2.2.3 says a combined line can be equally valid on other facts. B85 itself says “might be necessary”. Same principle, different facts → not a difference; both shown write-once in 2.3.5.
- “Size”: KPMG lists it; EY says its meaning is unclear. EY commentary, not a conflicting reading.
- ‘Other’ further information: KPMG lists the two explanations with “and”; Official B26(b) and EY use “or” as examples. KPMG frames them “for example” → not a substantive difference.

**Concept Map debt seen (Map gate, not edited):** Ch2 visual unchanged (`?v=i18ch2-2`); page now has 2.0.1, 2.1.2–2.1.4, 2.2.1–2.2.3, 2.3.2–2.3.6 units the map does not show (materiality / Figure 8, notes structure + cross-reference, required-line two-step, B78/B110 characteristics, B79/B111). Check map node labels against the renamed 2.5 “Offsetting”.

**Point-chip debt (S3, unchanged):** Ch2 3/3 point-chips still truncated by `assets/shared.css`.

**Screenshots — Gate 2b** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2b/`): `g2b-ch02-desktop-{top,full}.png`; crops `g2b-ch02-s20-scope`, `-s201-materiality-fig8`, `-s21-roles-illus211`, `-s212-s214-why-notes-xref`, `-s22-s221-required-lines`, `-s222-s223-constraints-q21`, `-s23-principles-illus231`, `-s232-characteristics`, `-s233-b79-b111-illus234`, `-s235-s236-opex-fx`, `-s24-labelling`, `-s241-s242-figure7`, `-s25-offsetting-tail`.

**Chips listed again (unchanged, still awaiting Q1–4):**
- Ch3 Entity C — `IFRS 18 · para B… returns test` (truncated).
- Ch3 EY Ill 3-8 sketch — `IFRS 18 · para IE Figure 5`.
- Ch1 §1.3.5 — bare `KPMG FI 2024`.
- Ch1 ×2 + Ch7 ×1 — `DTT A4 2022 · IAS 1 bridge`.
- EY iGAAP Ch04 — no chip format yet (zero chips; Ch1 + Ch2 locations logged).

### Answers received with Gate 2b approval
- Cite Q1–4: **still not approved** — chips unchanged; re-list at each gate.
- S3: **not approved** — no `shared.css` / `draft.css` edits.
- Q6: banks/insurers densify **into Ch3 as subsections under the existing structure** (no new top-level chapter).
- Expand EY Ill 3-x sketches into full Illustrations where the source has case facts; companions (mba-nest / classification-path) as needed.

## Gate 2c — Ch3 densify (2026-10-02 18:55 HKT)

**Scope kept:** `ch03.html` teaching body + key terms; `visuals/ch03-classification-path.html` (layout only). Concept Map iframe (`ch03-pnl-categories.html?v=i18ch3-5`), mba-nest visual (`?v=i18ch3mba-3`), chrome, disclaimer, footer untouched (except pack-wide stamp). No new `h3`: 3.0–3.9 kept, banks / insurers / bancassurers are `h4` units inside 3.5 (Q6). **All 27 pre-existing ids kept** (26 `s-3-*`) (incl. `s-3-5-fig5`, `s-3-8-kpmg`, `s-3-8-ey`, `s-3-9-ey`, which now sit at new homes — see renumbering). Backups (not committed): `/tmp/g3/ch03-orig.html`, `/workspace/ifrs18-ch3-extract/ch03-before-g2c-*.html`.

**Sources read for Ch3 before writing:** Official paras 47–68, 75(a)(v), B29–B76, BC83–BC93, BC97–BC99, BC120–BC128, BC142, BC159–BC235 (selected), Figures 2, 3.1–3.3, 4, 5, IE10–IE13; KPMG FI section 2.1 (2.1.1–2.1.7 incl. Examples 1–3, all Q&As) and section 8 (banks 8.1, insurers 8.2.1–8.2.2, bancassurers 8.2.5); EY Closer look section 3.1–3.3 (pp29–103: Ill 3-1 … 3-12, Q3-1 … Q3-41, How we see it boxes, Figure 3-6) and Appendix C (banks: C.2–C.10 incl. Figure C.2-1, Ill C.5-1, Q C.x-y). **EY iGAAP Ch04 section 3 not re-read this gate** (A3 pending; zero chips). DTT A4: no Ch3 content (IAS 1 had no categories) — not used.

**Metrics (before → after):** article text 46.4k → 136.6k chars (7.3k → 22.2k words); chips 222 → 861 (Official 170 → 546, EY 32 → 217, KPMG 20 → 98; distinct 128 → 480); `h4` units 6 → 36; Illustrations 6 (+1 decision strip, +1 index strip) → 19 Illustrations, 0 non-Illustration worked-strips. Source-label leads 0; author meta 0; Gate word 0; `§` in prose 160 → 0 (Figure tables and links now say “para”); `§` in chips 0; plain “see N.N” 0; bare work chips 0; HTML balanced; all in-page / cross-chapter anchors resolve (only unresolved href = site Home, pre-existing). **Chip multiset: every pre-existing chip string still present at ≥ original count** (one chip text fixed: `IAS 20 · para 26–29` was never in the original — new chip written as `IAS 20 · para 26–27, 29`).

**What changed (by section):**
- **3.0 / 3.1** general vs specific requirements; “thin” FX bridge → link to 3.7; KPMG category descriptions + key premise; Figure 2 (3.1.1) as one table with footnote row (duplicate bullets folded).
- **3.2 Operating** BC89 residual; **3.2.1** KPMG “typically captures” table + practice-change Q&A; **3.2.2** operating profit subtotal (BC88–BC93, EY view, Q3-18 labels); **3.2.3** Q3-13 … Q3-17 table; **Illus 3.2.4** EY Ill 3-4 government grants, Entities A/B gross vs net.
- **3.3 Investing** intro/table/point-chip kept (point-chip + KPMG PPE-sale example); **3.3.1** specified income/expenses table; **3.3.2** associates/JVs; **3.3.3** cash; **3.3.4** returns test; **Illus 3.3.5** EY Ill 3-1 Entity C four assets (full facts; locked `para B… returns test` chip stays in the 3.9 index row); **3.3.6** Q3-6/7/8 common assets; **3.3.7** incremental costs; **Illus 3.3.8** EY Ill 3-2 Entity P (CU5m / CU200,000 as printed); **3.3.9** subtotals.
- **3.4 Financing** **3.4.1** Type 1 table; **3.4.2** Type 2; **3.4.3** commitment fees; **Illus 3.4.4** EY Ill 3-3 four scenarios (EY “CU600,000” reproduced and footnoted); **3.4.5** Figure 4 one table + B56–B57; **Illus 3.4.6** KPMG Example 3 (Entity W convertible, Entity Y prepayable payable); **3.4.7** finance costs + para 64 exclusions, Q3-41.
- **3.5** retitled “Specified main business activities”; nest + path iframes and ordered-tests table kept; decision strip `#s-3-5-ex` → `h4` **3.5.1** table (wrong shape, not invent; chips kept); **3.5.2** evidence/indicators; **3.5.3** unit/timing/disclosure; **Illus 3.5.4** KPMG Example 1 Entity X (`#s-3-8-kpmg` moved home); **3.5.5** group/subsidiary/separate FS (Q3-22, Q3-24); **Illus 3.5.6** KPMG Example 2 Parents P/Q; **3.5.7** KPMG entity-type table; **3.5.8** Figure 3.1; **3.5.9** investing MBA (Q3-25 … Q3-29); **3.5.10** Figure 3.2; **3.5.11** customer financiers Type 1/2; **Illus 3.5.12** EY Ill 3-9 Bank B; **Illus 3.5.13** EY Ill 3-10 Entity R (`#s-3-8-ey` moved home, original chips kept); **Illus 3.5.14** EY Ill 3-11 conglomerate; **3.5.15** customer-financier subtotal/hybrids/derivatives/derecognition/FX; **3.5.16** Figure 3.3; **3.5.17** banks + EY Figure C.2-1 table (no amounts); **3.5.18** bank FAQ table (EY App C); **3.5.19** insurers (KPMG 8.2.1, EY 3.3.5, Q3-39/Q3-40); **Illus 3.5.20** EY Ill 3-12 Entity I (placeholder face as printed); **3.5.21** bancassurers (KPMG 8.2.5).
- **3.6** original bullets kept + BC83 subtotals, IFRS IC March 2026 non-IAS-12 taxes (not yet authoritative), discontinued disposal groups (BC204).
- **3.7** “Optional teaching prompts (not a Board flowchart)” → **“Other requirements — derecognition, FX, net monetary position and derivatives”** (old chips para 48, B65–B76, BC86–BC87 kept in intro). **3.7.1** derecognition table (B60–B61, Q3-19, KPMG 2.1.5.1 incl. HFS associate Q&A); **Illus 3.7.2** EY Ill 3-5; **3.7.3** change in use + tainting (B62–B64, KPMG decision table); **Illus 3.7.4** EY Ill 3-6 Entity G; **3.7.5** FX + net monetary position (B65–B69, BC209–BC221, KPMG Q&As, Q3-20); **Illus 3.7.6** EY Ill 3-7; **3.7.7** intercompany FX (KPMG 2024 vs IFRS IC March 2026 two readings, Q3-21); **3.7.8** Figure 5 (`#s-3-5-fig5` moved from 3.5) one table + B71–B76, BC225–BC235, KPMG 2.1.7 table; **Illus 3.7.9** EY Ill 3-8 (CU100/CU120/CU20 as printed).
- **3.8** IE10–IE13 strips verbatim; BB “Entity R sketch (Illustration 3.5.5)” → link to **Illustration 3.5.13**; DD “Illustration 4.2.1” → link `ch04.html#s-4-2-ex`; old KPMG/EY strips moved out (now 3.5.4 / 3.5.13).
- **3.9** “EY classification illustrations” box grid (non-Illus worked-strip) → **“Illustration index”** table `#s-3-9-ey`: EY Ill 3-1 … 3-12, KPMG Examples 1–3, Standard IE10–IE13 → home links. Locked chips kept verbatim in their rows.
- **Key terms** + Type 1 / Type 2 liability, individually and largely independently, undue cost or effort.

**Renumbering (ids unchanged unless noted):** h4 3.4.1 Figure 4 → **3.4.5**; 3.5.1 Figure 3.1 → **3.5.8**; 3.5.2 Figure 3.2 → **3.5.10**; 3.5.3 Figure 3.3 → **3.5.16**; 3.4.2 Figure 5 (`#s-3-5-fig5`) → **3.7.8**; Decision strip `#s-3-5-ex` → **3.5.1**; Illus 3.5.4 “Examples 1–3” (`#s-3-8-kpmg`) → **3.5.4** Example 1 only + new 3.5.6 (`#s-3-5-ex2`) Example 2 + new 3.4.6 (`#s-3-4-ex2`) Example 3; Illus 3.5.5 Entity R (`#s-3-8-ey`) → **3.5.13**. IE 3.8.1–3.8.4 unchanged (Ch4 still cites “Illustration 3.8.4” — correct).

**Companions:** `ch03-classification-path` — “no → residual” stem now runs from the Financing test straight into Operating; the SMBA note moved below the residual leaf (Gate 1 item I fixed); ch03 iframe `?v=i18ch3path-4`, legend “(SMBA note below)”, 3.5 text updated. **Not changed:** `§47`-style short chips in all visuals (Ch1–Ch8 + Map use the same style) and category leaf fills — pack-wide visual consistency item. `ch03-mba-nest` unchanged.

**Source inconsistencies reproduced and flagged in the page (not corrected):** EY Ill 3-3 “CU600,000 of the loan” (= 60% of the CU1m fee, not the loan) — footnote in 3.4.4. EY App C Ill C.5-1 vs conclusion “Bank A/Bank B”; Q C.5-1 cites “IFRS 16.56(a)” — row in 3.5.18.

**Firm differences checked for Ch3 — none verified. No `.callout.differ`.**
- Intercompany FX: KPMG FI 2024 “no guidance, judgemental” vs EY 2026 reporting the IFRS IC March 2026 two readings — later development, not a conflicting reading; both shown in 3.7.7.
- Held-for-sale associate: KPMG “not entirely clear… arguably investing” vs EY general HFS rule (old category) — same direction.
- Gross grant income: EY “generally operating” view (Q3-17) — no KPMG statement.

**Debt for later gates (not edited):**
- Map: `index.html` See-also “(later; overview in Ch3)” and mini-P&L bands (link 3.3/3.4/3.6 only; no 3.7 node). Concept Map `ch03-pnl-categories` shows no node for 3.7 other requirements or the 3.5 banks/insurers units; both Income taxes and Discontinued carry “3.6” (correct).
- Ch2 2.3.6 (EY Q2-2) links FX classification to `ch03.html#s-3-1`; better target now `#s-3-7-5` (consistency pass — Ch2 already approved).
- Point-chips (S3): Ch3 4/4 still truncated by `assets/shared.css`.

**Screenshots — Gate 2c** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2c/`): `g2c-ch03-desktop-{top,full}.png`; crops `g2c-ch03-s30-s31-scope-fig2`, `-s32-operating-illus324-p1/p2`, `-s33-investing-units`, `-s334-s339-illus335-338-p1`, `-s34-financing-illus344-p1/p2`, `-s345-s347-fig4-illus346`, `-s35-nest-path-p1/p2`, `-s351-s356-mba-illus354-356-p1/p2`, `-s357-s3510-fig31-fig32`, `-s3511-s3514-illus3512-3514`, `-s3515-s3516-fig33`, `-s3517-s3518-banks`, `-s3519-s3521-insurers-banc`, `-s36-s372-tax-derecognition`, `-s373-s376-groups-fx`, `-s377-s379-intercompany-fig5`, `-s38-ie-faces-p1/p2`, `-s39-index-tail`.

**Chips listed again (unchanged, still awaiting Q1–4):**
- Ch3 Entity C — `IFRS 18 · para B… returns test` (truncated) — now in the 3.9 index row for EY Ill 3-1.
- Ch3 EY Ill 3-8 — `IFRS 18 · para IE Figure 5` — now in the 3.9 index row for EY Ill 3-8.
- Ch1 §1.3.5 — bare `KPMG FI 2024`.
- Ch1 ×2 + Ch7 ×1 — `DTT A4 2022 · IAS 1 bridge`.
- EY iGAAP Ch04 — no chip format yet (zero chips; Ch3 section 3 not compared this gate).

### Answers received with Gate 2c approval
- “Continue to Ch4 densify only.” — Ch4 only; do not start Ch5+.
- Cite Q1–4 / S3: **still not approved** — chips unchanged; no `shared.css` / `draft.css` edits.
- Attach checklist: Official, KPMG FI 2024, EY Closer look Apr 2026, EY iGAAP 2026 Ch04 (use Ch04 for Ch4), DTT A4 2022 attached; PwC missing (no invent); KPMG Insights 2019/20 is pre-IFRS 18.
- Stamp in Asia/Shanghai time when done; screenshots under `gate2d/`.

## Gate 2d — Ch4 densify (2026-10-02 19:22 HKT)

**Scope kept:** `ch04.html` teaching body + key terms. Concept Map iframe (`ch04-totals-subtotals.html?v=i18ch4-2`), chrome, disclaimer, footer untouched (except stamp). No new `h3`: 4.0–4.5 kept (4.3 retitled). **All 10 pre-existing ids kept** (`s-4-0` … `s-4-5`, `s-4-1-ex`, `s-4-2-ex`, `s-4-4-ex`, `s-4-5-ey`); inbound links (Ch1, Ch2, Ch3 `#s-4-2-ex`, index, visuals) still resolve. Backup (not committed): `/tmp/g4/ch04-orig.html`.

**Sources read for Ch4 before writing:** Official paras 22–24, 43, 47, 65(a)(ii), 69–77, 86–87, 117–118, B9, B77–B79, B123, BC84–BC93, BC120, BC148–BC152, BC189–BC191, BC236–BC245 (incl. BCZ244), BC362–BC367, IE7 (incl. attribution, EPS, footnote (a)), IE13; KPMG FI section 2.3, 2.3.1–2.3.4, 3.1.3, 5.3; EY Closer look section 2.1.1.B, 3.2.1.G, 3.2.1.H, 3.3.3.G, 3.4, 3.4.1, 4.2.4.A (Q4-5), 4.2.4.B (Q4-6, EBITDA, equity-accounted subset), Q3-40, Q3-42, Ill 3-12; **EY iGAAP Ch04 sections 3.4 and 4.2.4** (compared; zero chips, A3); DTT A4 5.1.2, 5.1.3.3-1 (verification only).

**Metrics (before → after):** article prose 2,737 → 5,215 words (+91%; chips excluded); article size 37.5k → 68.9k chars (whole page); chips 128 → 249 (Official 104 → 188, KPMG 11 → 31, EY 13 → 30; distinct 66 → 125); `h4` units 0 → 8; tables 3 → 11; Illustrations 3 (+1 decision strip) → 3 Illustrations (all Facts / Assessment / Decision), 0 non-Illustration worked-strips. Source-label leads 0; author meta 0; Gate word 0; `§` in prose 70 → 0; `§` in chips 0; plain “see N.N” 0; bare work chips 0; point-chips 4 → 5 (all cited); HTML balanced; all anchors resolve (only unresolved href = site Home, pre-existing). **Chip multiset: every pre-existing chip string still present at ≥ original count.**

**What changed (by section):**
- **4.0** fourth decision (line items → 4.3); KPMG 2.3 four building blocks.
- **4.1** link to Ch3 3.2.2 (residual rationale, labels); EY comparability note; attribution bullet; BC152 digital wording; KPMG 2.3.1 new-vs-carried-forward table incl. para 86 total OCI / TCI; point-chip adds “no investing-only subtotal” (BC87). **Illus 4.1.1** IE7 XYZ moved home: IE7(a)/(b) facts (function rationale, goodwill impairment, two statements), “do not invent alternative figures” author line removed, Decision box, attribution + EPS rows and footnote (a) as printed. **4.1.2** rejected alternatives (BC91, BC92–BC93, BC150–BC151, BC149, BC152, BC87).
- **4.2** “who can reach this path” (links Ch3 3.5.11 / 3.5.15 / 3.5.21); contrast plate shortened to fit the 3-line dense clamp (detail already in bullets). **Illus 4.2.1** IE13 DD moved home: IE13(a)(i)/(ii) paragraph refs, plain “See … Illustration 3.8.4” → link, Decision box, IE13 face extract (operating profit → PROFIT). **4.2.2** labelling and tagging table (BC189, BC190, para 74 + EY How we see it, BC191 tags, 118(d), KPMG trigger wording).
- **4.3** “Line items — thin pointer” → **“Line items in the statement of profit or loss”**; BCZ244 / para 87 / 107(a); BC237–BC238 (link Ch2 2.2.1); BC236; para 77 / B78–B79 (link Ch2 2.3.2 / 2.3.3); BC240–BC241; BC245; Q3-42 → Ch3 3.3.2. **4.3.1** para 75(b)/(c) table; **4.3.2** B77 / BC239 multi-category (EY ECL labels; banks → Ch3 3.5.18); **4.3.3** financing line items (BC242–BC243, IE7 two lines).
- **4.4** “OPDAI vs EBITDA (thin)” lead → “OPDAI vs EBITDA”; B123 net financial result definition; MPM row links Ch6. **4.4.1** additional subtotals can be MPMs (KPMG 3.1.3 diagram, EY Q4-5) + four-group table. **4.4.2** listed-subtotals table (KPMG face compatibility, EY Q4-6, BC364, BC367 vs EY, 118(d)–(f) with IE links) + EBITDA label (BC365–BC366 vs KPMG), BC363, IAS 33.73B → Ch7 7.3. **4.4.3** decision strip `#s-4-4-ex` → table (wrong shape, not invent; all chips kept).
- **4.5** link to Ch2 2.2.2; “Investing-category extras (thin)” → “Investing-category extras” + EY How we see it (link Ch3 3.3.9); EY no cap on number. **Illus 4.5.1** Entity I: extract table linked to Ch3 3.5.20 (no duplicate face), Decision box (not 118(c); may be an MPM).
- **Key terms** `§` → para; + similar to gross profit (B123), OPDAI, additional subtotal (para 24), allocation of profit or loss (NCI / owners).

**Renumbering (ids unchanged):** Decision strip `#s-4-4-ex` → **4.4.3**; Illustrations keep 4.1.1 / 4.2.1 / 4.5.1 (now at home units). New ids: `s-4-1-2`, `s-4-2-2`, `s-4-3-1`, `s-4-3-2`, `s-4-3-3`, `s-4-4-1`, `s-4-4-2`.

**Firm differences / source wording — flagged, not reconciled; no `.callout.differ`:**
- KPMG 2.3.1 footnote: para 73 trigger worded as cash and cash equivalents + ‘financing liabilities’ all in operating vs Official para 73 (para 65(a)(ii) policy only). Shown side by side in 4.2.2.
- KPMG 2.3.4: EBITDA label accurate if no investing income **and no interest income in operating** vs BC366 (no investing income only). Shown in 4.4.2.
- BC367 “would be” an MPM vs EY 4.2.4.B “could be”. Shown in 4.4.2 row (c).
- EY Q4-6 locator “[IFRS 18.118(a)]” for OPDAI (= 118(b)) — not reproduced.
- KPMG 3.1.3 and EY Q4-5 agree (additional subtotals can be MPMs) — not a difference.

**EY iGAAP Ch04 findings:** sections 3.4 and 4.2.4 match Closer look in substance (Q4-5 present); **Q4-6 (IAS 36 reversals) absent from iGAAP**; FAQ numbering differs (iGAAP Q3-14 = CL Q3-18, iGAAP Q3-27 = CL Q3-40, iGAAP Q3-18 different). No iGAAP-only Ch4 content; zero iGAAP chips.

**DTT A4 verification:** IAS 1.85–85B / BC58B and 5.1.3.3-1 (EBIT/EBITDA under IAS 1) consistent with KPMG 2.3.2; no DTT chips.

**Debt for later gates (not edited):**
- Concept Map `ch04-totals-subtotals` has nodes 4.1 / 4.2 / 4.4 only — no 4.3 line items, 4.4.1 subtotal groups or 4.5 additional subtotals; short `§` chips (pack-wide visual style).
- Ch4 Illus 4.5.1 and Ch3 Illus 3.5.20 both use EY Ill 3-12 (different angles; 4.5.1 links 3.5.20 for the face). Consider noting in the Ch3 3.9 index row at the consistency pass (Ch3 approved — not edited).
- Point-chips (S3): Ch4 5/5 subject to the `assets/shared.css` clamp.

**Screenshots — Gate 2d** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2d/`): `g2d-ch04-desktop-{top,full}.png`; crops `g2d-ch04-s40-scope`, `-s41-required-anchors`, `-illus411-xyz`, `-s412-rejected-alternatives`, `-s42-para73`, `-illus421-dd`, `-s422-labelling-tagging`, `-s43-line-items`, `-s431-s433-ifrs9-17-financing`, `-s44-matrix`, `-s441-s442-groups-listed`, `-s443-decision-table`, `-s45-additional`, `-illus451-entity-i-tail`.

**Chips listed again (unchanged, still awaiting Q1–4 / S3):**
- Ch3 Entity C — `IFRS 18 · para B… returns test` (truncated) — Ch3 3.9 index row.
- Ch3 EY Ill 3-8 — `IFRS 18 · para IE Figure 5` — Ch3 3.9 index row.
- Ch1 §1.3.5 — bare `KPMG FI 2024`.
- Ch1 ×2 + Ch7 ×1 — `DTT A4 2022 · IAS 1 bridge`.
- EY iGAAP Ch04 — no chip format yet (zero chips; Ch4 compared, no iGAAP-only content).
- DTT · 8.1 / References — unchanged. Point-chip wrap (S3) — unchanged.

### Answers received with Gate 2d approval
- “Continue to Ch5 densify only.” — Ch5 only at that point.
- Cite Q1–4 / S3: **still not approved** — chips unchanged; no `shared.css` / `draft.css` edits.
- Attach checklist: Official, KPMG FI 2024, EY Closer look Apr 2026, EY iGAAP 2026 Ch04 (verification only; no invent beyond sources), DTT A4 2022 attached; PwC missing; KPMG Insights 2019/20 pre-IFRS 18.
- Stamp Asia/Shanghai when done; screenshots under `gate2e/`.
- **Standing order (received mid-Ch5):** after Ch5, auto-continue Ch6 → Ch7 → Ch8 → Map/References consistency, one chapter per commit cycle; short gate report between chapters; do not idle for Continue. Same hard locks; screenshots `gate2f/`, `gate2g/`, …

## Gate 2e — Ch5 densify (2026-10-02 19:36 HKT)

**Scope kept:** `ch05.html` teaching body + key terms. Concept Map iframe (`ch05-operating-expenses.html?v=i18ch5-8`), chrome, disclaimer, footer untouched (except stamp). No new `h3`: 5.0–5.4 kept (5.1 retitled from the “Selection cue” hedge title; 5.4 “Para” capitalised). **All 9 pre-existing ids kept** (`s-5-0` … `s-5-4`, `s-5-1-ex`, `s-5-1-kpmg`, `s-5-2-ey`, `s-5-3-ex`, `s-5-3-ie`); inbound links (Ch2 `#s-5-1-kpmg`, Ch4 `#s-5-1-ex`, `#s-5-1`…`#s-5-4`) still resolve and Illustration numbers 5.1.1 / 5.1.2 unchanged. Backup (not committed): `/tmp/g5/ch05-orig.html`.

**Sources read for Ch5 before writing:** Official paras 30, 41, 78–85, B80–B85, BC246–BC276, IN17, IE7(b) face + Note 1 (incl. footnote (a) and the capitalisation text), IE10–IE13 faces; KPMG FI section 2.2, 2.2.1, 2.2.2 (incl. footnote table, depreciation diagram, Q&As, IAS 1 vs IFRS 18 table), 2.2.3, Example 4; EY Closer look section 3.4.2, 3.4.2.A–E, Q3-43, section 3.5 (five questions, Ill 3-13); **EY iGAAP Ch04 section 3.4.2 / 3.5** (compared; zero chips); DTT A4 5.4.2.1–5.4.2.5 (verification only).

**Metrics (before → after):** article prose 3,074 → 5,243 words (+71%; chips excluded); page size 41.2k → 68.2k chars; chips 141 → 210 (Official 106 → 153, KPMG 16 → 24, EY 19 → 33; distinct 78 → 104); `h4` units 0 → 6; tables 3 → 13; Illustrations 4 (+1 decision strip) → 6 Illustrations (all Facts / Assessment / Decision), 0 non-Illustration worked-strips. Source-label leads 0; author meta 0; Gate word 0; `§` in prose 26 lines → 0; `§` in chips 0; plain “see N.N” 0; point-chips 5 → 5 (all cited); HTML balanced; all anchors resolve (only unresolved href = site Home, pre-existing). **Chip multiset: every pre-existing chip string still present at ≥ original count.**

**What changed (by section):**
- **5.0** BC249 (no function info for nature presenters); KPMG practice-change bullet (legacy GAAP / regulatory / industry). **5.0.1** KPMG IAS 1 vs IFRS 18 table.
- **5.1** retitled “Choosing nature, function or mixed — most useful structured summary”; KPMG 2.2.3 policy-change bullet; EY general aggregation still applies (link Ch2 2.3.5); BC253 practicability + EY “widely understood”. **Illus 5.1.1** XYZ moved home: plain “see Illustration 4.1.1” → link; Decision box; IE7 operating-expense table with function/nature tags (basis of “other operating expenses” stated as not given). **Illus 5.1.2** KPMG Ex 4 moved home: Decision box; link Ch2 2.3.5. **5.1.3** table of IE examples XYZ / AA / BB / CC / DD (links Ch3 3.8.1–3.8.4, Ch4 4.1.1; CC insurance service expenses = EY Q3-43 view). **Illus 5.1.4 (new, `s-5-1-ie10`)** AA all-by-nature, operating band extract with changes in inventories (B84(a)). **5.1.5** why mixed is allowed and its limits (BC250–BC252, EY no free choice).
- **5.2** BC255 gross margins; BC256 reasons; BC257(a)/(b); EY cost-of-sales scope view; BC258 nature lines except “other” (link Ch2 2.4); gross profit → Ch4 4.4.2. **5.2.1** EY five questions on non-recurring items (FAQ table, not an Illustration; links Ch2 2.3.3, Ch4 4.4.1, Ch6). **Illus 5.2.1 → 5.2.2** Entity U: “EY How we see it:” lead reworded to “EY view:”; Decision box.
- **5.3** BC265(b)(i)–(iii) (link Ch7 7.1), BC266, BC268(b) wording, EY systems view, Q3-43 lead “EY only — IFRS 17 trigger” → “Function lines required by another Standard” (link Ch3 3.5.19). **Illus 5.3.1** XYZ Note 1 moved home: **20X1 amortisation corrected 12,870 → 12,690** (R&D line and total; Official IE, EY CL and iGAAP all print 12,690); footnote (a) row; IE capitalisation text; Decision box. **Illus 5.3.2 (new, `s-5-3-kpmg`)** KPMG depreciation trace 72 / 50 / 3 / 15 / 68 with footnotes (a)/(b). **5.3.3** alternatives table (BC249, BC262, BC263, BC264–BC265, BC267, BC276). **5.3.4** decision strip `#s-5-3-ex` → table (wrong shape, not invent; all chips kept).
- **5.4** para 84 lead-in quoted; BC274(a)/(b); EY no-threshold / apparent para 41 conflict; wording table Official vs KPMG vs EY (neutral).
- **Key terms** `§` → para; + specified nature expenses (five), capitalised amounts (B84), changes in inventories line, non-recurring items (persistence).

**Renumbering (ids unchanged):** EY Ill 3-13 Illustration 5.2.1 → **5.2.2** (no external refs); decision strip `#s-5-3-ex` → **5.3.4**. New ids: `s-5-0-1`, `s-5-1-3`, `s-5-1-ie10`, `s-5-1-5`, `s-5-2-1`, `s-5-3-kpmg`, `s-5-3-3`.

**Flags — reproduced, not reconciled; no `.callout.differ`:**
- **Pack figure error fixed:** Illus 5.3.1 printed 20X1 amortisation 12,870 (twice); Official IE Note 1 = 12,690 (EY CL + iGAAP agree).
- KPMG 2.2.2 IAS 1 column: mixed “not explicitly prohibited, as long as by-nature information is included”; DTT A4 heading 5.4.2.5 “Inappropriate to present an analysis of expenses on a ‘mixed’ basis” (IAS 1-era). KPMG shown in 5.0.1; DTT verification only, no chip.
- KPMG 2.2.2 exemption wording (“only required to provide disaggregated information about the five specific nature expenses”) reads broader than para 84(a)/(b). Both shown side by side in 5.4 table.
- Official internal: BC272(a) cites “paragraph 42” for the general disaggregation requirement; para 84 says “Paragraph 41”. Pack follows para 84; not reproduced on the page.

**EY iGAAP Ch04 findings:** section 3.4.2 / 3.5 match Closer look in substance (incl. systems How we see it, cost-of-sales scope view, five non-recurring questions); **no Q3-43 / IFRS IC March 2026 in iGAAP**; meteor case is **iGAAP Ill 3-9 Entity A = CL Ill 3-13 Entity U**; prints 12,690. No iGAAP-only Ch5 content; zero iGAAP chips.

**DTT A4 verification:** IAS 1.99–1.105 (choice on reliable and more relevant; face analysis encouraged; nature example with changes in inventories; function → cost of sales at minimum; IAS 1.104 depreciation/amortisation/employee benefits) consistent with KPMG’s IAS 1 column except the mixed heading above. No DTT chips.

**Debt for later gates (not edited):**
- Concept Map `ch05-operating-expenses` has no node for 5.1.3 IE examples, 5.2.1 non-recurring or 5.3.3 alternatives; its aria-label still uses “Gate — any function line on the face” (visual; consistency gate).
- Ch5 5.1.3 and Illus 5.1.4 reuse IE10–IE13 faces held in Ch3 3.8.x (operating band extract only).

**Screenshots — Gate 2e** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2e/`): `g2e-ch05-desktop-{top,full}.png`; crops `g2e-ch05-s50-scope-ias1-table`, `-s51-choosing-method`, `-illus511-xyz`, `-illus512-kpmg-ex4`, `-s513-ie-examples`, `-illus514-aa`, `-s515-mixed-limits`, `-s52-cost-of-sales`, `-s521-non-recurring`, `-illus522-entity-u`, `-s53-para83`, `-illus531-xyz-note1`, `-illus532-kpmg-depreciation`, `-s533-s534-alternatives-decision`, `-s54-exemption-tail`.

**Chips listed again (unchanged, still awaiting Q1–4 / S3 — NOT APPROVED):**
- Ch3 Entity C — `IFRS 18 · para B… returns test` (truncated) — Ch3 3.9 index row.
- Ch3 EY Ill 3-8 — `IFRS 18 · para IE Figure 5` — Ch3 3.9 index row.
- Ch1 §1.3.5 — bare `KPMG FI 2024`.
- Ch1 ×2 + Ch7 ×1 — `DTT A4 2022 · IAS 1 bridge`.
- EY iGAAP Ch04 — no chip format yet (zero chips).
- DTT · 8.1 / References — unchanged. Point-chip wrap (S3) — unchanged.

## Gate 2f — Ch6 densify (2026-10-02 19:45 HKT)

**Scope kept:** `ch06.html` teaching body + key terms. Concept Map iframe, chrome, disclaimer, footer untouched (except stamp). No new `h3`: 6.0–6.6 kept (6.3 “Para” capitalised; 6.6 “Test-order teaching prompts” hedge title → “Identify, disclose, change — the MPM sequence”). **All 11 pre-existing ids kept** (`s-6-0` … `s-6-6`, `s-6-1-fig6`, `s-6-4-ex`, `s-6-4-ie8`, `s-6-4-ey`); inbound links (`#s-6-1` ×10, `#s-6-2`, `#s-6-3`, `#s-6-4`) still resolve. Backup (not committed): `/tmp/g6/ch06-orig.html`.

**Sources read for Ch6 before writing:** Official paras 24, 31, 69, 117–125, B113–B142, BC325–BC390, IN14–IN15, Figure 6, IE8 (text (a)–(g), 20X2 and 20X1 tables and tax notes); KPMG FI section 3, 3.1, 3.1.1–3.1.3, 3.2, 3.3, 3.4; EY Closer look section 4.1, 4.2, 4.2.1–4.2.4 (Q4-1 to Q4-6), 4.3.1–4.3.5 (Ill 4-1, Q4-7, Q4-8), 4.4; **EY iGAAP Ch04 FAQ index** (compared; zero chips).

**Metrics (before → after):** article prose 4,127 → 6,168 words (+49%; chips excluded); page size 51.8k → 76.4k chars; chips 172 → 263 (Official 133 → 188, KPMG 18 → 29, EY 21 → 46; distinct 111 → 166); `h4` units 1 → 6; tables 6 → 11; Illustrations 2 (+1 decision strip) → 2 Illustrations (both Facts / Assessment / Decision), 0 non-Illustration worked-strips. Source-label leads 0; author meta 0; `§` 63 lines → 0; plain “see N.N” 2 → 0; point-chips 6 → 6; HTML balanced; all anchors resolve. **Chip multiset: every pre-existing chip string still present at ≥ original count.**

**What changed (by section):**
- **6.0** BC327 three design questions; BC334 consistency; jurisdiction-neutral (BC326); audit (KPMG 3.4) + EY scrutiny view; link Ch4 4.4.2.
- **6.1** BC330, BC332–BC333 (why only income/expenses); BC335–BC336 rationale; BC337 + EY interim view (link Ch7 7.4); BC339–BC340; KPMG completeness/auditor view; BC342 private entities; BC341 internal-only rejected; BC343–BC344 entity vs management performance; EY group vs subsidiary view; Q4-5 additional subtotal can be an MPM (link Ch4 4.4.1); BC354 replicated P&amp;L; BC374–BC375 face MPMs; KPMG list of IAS 1-era face subtotals + columns. **6.1.1** Figure 6 duplicate list removed (table kept verbatim; footnote kept as lead paragraph). **6.1.2** edge-of-definition table (Q4-1, Q4-2, Q4-3, KPMG/EY non-GAAP in notes, BC372). **6.1.3** segment indicators (B115 + EY Q4-4 (b)–(d), labelled as Board discussion per EY).
- **6.2** BC347–BC348 why a presumption; BC352; EY common vs rare B129 reasons; BC355 rationale; BC356 IFRS 9 precedent; EY 4.2.3.D on B131. **6.2.1** Board rebuttal examples (BC350, BC353 cost of net debt, BC354).
- **6.3** required subtotals (EY 4.2.4.A); BC362 rationale; B123 link Ch5 5.2; “OPDAI vs EBITDA (thin bridge from Ch4)” → “OPDAI vs EBITDA” + BC364 (link Ch4 4.4.2); Q4-6 reversals; “EY only — partial equity-method subtotal” lead → “Only some equity-accounted investees”; KPMG overlapping-groups diagram; contrast plate shortened to the 3-line dense clamp.
- **6.4** BC369–BC371 single note, no cross-referencing; BC373; BC357–BC361 no calculation restrictions; KPMG MPMs vs additional subtotals; BC378 reasons; BC379–BC381; BC383–BC385 EPS (link Ch7 7.3); BC386–BC387 tax methods. **Illus 6.4.1** IE8 moved home: author line “do not invent alternative figures” removed; adjusting-item list and 20X1 tax notes (Countries E/F/G, 14.5%) added; year captions on both tables; Decision box. **Illus 6.4.2** EY Ill 4-1 moved home: vague “multi-firm write-once” line replaced with concrete layout point; Decision box. **6.4.3** layout / format / effort / regulators table (KPMG 3.3, 3.4; BC382). **6.4.4** decision strip `#s-6-4-ex` → table (wrong shape; chips kept).
- **6.5** BC368 / BC388 rationale; BC390 trend; BC389 zero adjustment; BC338; Q4-7 cessation; Q4-8 year of adoption (link Ch8 8.2).
- **6.6** retitled; + interim bullet (link Ch7 7.4).
- **Key terms** `§` → para; + ratio numerator (B117), without prominence (B126), changes to MPMs (para 124).

**Renumbering (ids unchanged):** decision strip `#s-6-4-ex` → **6.4.4**. Illustrations keep 6.4.1 / 6.4.2. New ids: `s-6-1-2`, `s-6-1-3`, `s-6-2-1`, `s-6-4-3`.

**Flags — reproduced, not reconciled:**
- None between firms on Ch6 substance (KPMG and EY agree on definition, presumption, exclusions, disclosures).
- EY Q4-6 locator “[IFRS 18.118(a)]” for OPDAI (= 118(b)) — as Gate 2d; not reproduced.
- EY Q4-4 indicators (b)–(d) come from Board discussion / staff paper per EY, not the Standard — labelled so in 6.1.3.
- KPMG 3.4 SEC / ESMA / IOSCO statements are KPMG’s; no regulator text attached — shown as KPMG.

**EY iGAAP Ch04 findings:** FAQ index carries Q4-1 to Q4-5 only — **no Q4-6, Q4-7, Q4-8** (Closer look only); iGAAP also has an Ill 4-1 MPMs note. No iGAAP-only Ch6 content; zero chips.

**DTT A4:** not used for Ch6 (IAS 1 had no MPM regime). **PwC:** missing.

**Debt (not edited):** Concept Map `ch06` not updated for 6.1.2 / 6.1.3 / 6.2.1 / 6.4.3.

**Screenshots — Gate 2f** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2f/`): `g2f-ch06-desktop-{top,full}.png`; crops `g2f-ch06-s60-scope`, `-s61-para117-tests`, `-s611-figure6`, `-s612-s613-edge-segment`, `-s62-presumption`, `-s621-rebuttal-examples`, `-s63-para118`, `-s64-single-note`, `-illus641-ie8`, `-illus642-ey-ill41`, `-s643-s644-layout-decision`, `-s65-s66-changes-tail`.

**Chips listed again (unchanged, still awaiting Q1–4 / S3 — NOT APPROVED):** Ch3 `IFRS 18 · para B… returns test`; Ch3 `IFRS 18 · para IE Figure 5`; Ch1 bare `KPMG FI 2024`; Ch1 ×2 + Ch7 ×1 `DTT A4 2022 · IAS 1 bridge`; EY iGAAP no chip format (zero chips); DTT · 8.1 / References and point-chip wrap (S3) unchanged.

## Gate 2g — Ch7 densify (2026-10-02 19:56 HKT)

**Scope kept:** `ch07.html` teaching body + key terms. Concept Map iframe, chrome, disclaimer, footer untouched (except stamp). No new `h3`: 7.0–7.5 kept; titles: 7.0 “Scope of this chapter” → “Scope — consequential amendments beyond the statement of profit or loss”; 7.1 + “and interest and dividend classification”; 7.2 “carried with structured-summary lens” → “limited changes and the structured-summary lens”; 7.3 → “permitted numerators for additional amounts per share”; 7.4 “MPM parity pointer” (hedge) → “aggregation, headings and MPM disclosures”; 7.5 → “paragraphs 126–129 and IE Part III”. **All 11 pre-existing ids kept** (`s-7-0` … `s-7-5`, `s-7-1-ex`, `s-7-1-ey`, `s-7-2-ie`, `s-7-3-ey`, `s-7-5-ie14`, `s-7-5-ie16`); inbound links (`#s-7-1` ×11, `#s-7-2` ×7, `#s-7-3` ×6, `#s-7-4` ×5, `#s-7-5` ×2) still resolve. Backup (not committed): `/tmp/g7/ch07-orig.html`.

**Sources read for Ch7 before writing:** Official paras 3, 5, 96–106, 126–132, B120, BC86, BC313–BC315, BCZ285, BC337, BCZ391–BCZ406, BC421–BC422 (Ch8 material, not used here), IE6–IE7, IE14–IE17, XYZ SFP (full lines), Figure 1, Appendix D; KPMG FI 2.1 / 2.1.2.2 FAQ, 5.1, 5.1.1, 5.2, 5.3, 6.1; EY Closer look section 5, 5.1 (Ill 5-1 + footnote (a)), 5.2, 5.3 (Q5-1, Q5-2, Ill 5-2, Ill 5-3), 5.4, 4.2.2; **EY iGAAP Ch04 section 5.1–5.4** (compared; mirrors Closer look; zero chips).

**Metrics (before → after):** article prose 1,792 → 4,705 words (chips excluded); page size 29.2k → 63.0k chars; chips 52 → 154 (Official 38 → 86, KPMG 5 → 31, EY 8 → 36, DTT 1 → 1; distinct 42 → 75); `h4` units 0 → 10; tables 5 → 15; Illustrations 5 (+1 decision strip) → 5 Illustrations (all Facts / Assessment / Decision), 0 non-Illustration worked-strips. Source-label leads 0; author meta 1 → 0; `§` 6 lines → 0; plain “see N.N” 0; HTML balanced; all anchors resolve. **Chip multiset: every pre-existing chip string still present at ≥ original count.**

**What changed (by section):**
- **7.0** Figure 1 “limited changes / no changes” framing; para 3 (general requirements 9–43, 113–114 apply to SCF); App D effective date; banks/insurers see-also replaced by links to 7.1.2 and Ch3 3.5; “What stays thin” and “do not structure Ch7 as…” author lines removed; DTT locked chip kept. **7.0.1** consequential amendments map (IAS 7, SFP, IAS 33, IAS 34, IAS 8, capital).
- **7.1** EY BC47 reasons; EY impact view; interest/dividend option removal (BC48 reason via EY), dividends paid financing; BC86 + KPMG PPE example (categories ≠ activities); EY Ill 5-1 based on IAS 7 IE A. **7.1.1** before/after table (EY Effects Analysis Table 4 / KPMG). **7.1.2** specified main business activities single-activity rule, separate assessment, 34D policy choice, dividends paid on liability instruments. **Illus 7.1.3** EY Ill 5-1: “multi-firm write-once” meta removed; OCI footnote (a); Decision box with arithmetic. **7.1.4** decision strip `#s-7-1-ex` → table; “(no invented entity facts)” author meta removed from title; chips kept.
- **7.2** para 96 liquidity exception text; BC314 goodwill; BC315 nature/function; BC313 list not revisited; para 106 financial institution descriptions; Illustration 2.3.1 → correct **2.3.4** link. **7.2.1** carried/changed table (96–106). **Illus 7.2.2** XYZ SFP: author lines (“not … invent”, “do not invent alternative figures”) removed; equity and liabilities table expanded from totals to the full Official lines (share capital, retained earnings, OCE, borrowings, leases, pensions, provisions, DTL, payables, tax); section sub-headers; Decision box.
- **7.3** 73B numerators; 73C(a)–(d); BC16–BC18 reasons via EY; Q5-1; local-law EPS; KPMG EBITDA-per-share example. **7.3.1** conditions table. **Illus 7.3.2** EY Ill 5-2 / 5-3 + Decision box. **7.3.3** decision table.
- **7.4** para 5; IAS 34.10 headings/subtotals (KPMG); IAS 34.16A(m) scope (EY); BC10A/BC10B via EY; no reconciliation relief (KPMG); EY prescriptiveness view; link Ch8 8.4. **7.4.1** B120 / BC337 period table. **7.4.2** KPMG cross-reference FAQ table.
- **7.5** para 126–129 full content; “moved into IFRS 18” corrected to carried forward from IAS 1 (Figure 1, BCZ394); BCZ392–BCZ393, BCZ396–BCZ397. **7.5.1** required vs not required (BCZ399–BCZ406). **Illus 7.5.2** EE: not-regulated, IAS 7 44A–44E, adjustment tools, equity components, reason for ratio fall, dividend CU2.8m / CU2.5m; table header “(in thousands of CU)”; Decision box. **Illus 7.5.3** FF: plan/sale moved into Facts; BCZ403 temporary non-compliance; Decision box.
- **Key terms** “(thin)” removed; + interest and dividend cash flows, goodwill line item, para 73B numerators, IAS 34 MPM disclosures, capital (para 126–129).

**Renumbering (ids unchanged):** Illus `#s-7-1-ey` 7.1.1 → **7.1.3**; decision strip `#s-7-1-ex` → **7.1.4**; `#s-7-2-ie` 7.2.1 → **7.2.2**; `#s-7-3-ey` 7.3.1 → **7.3.2**; `#s-7-5-ie14` 7.5.1 → **7.5.2**; `#s-7-5-ie16` 7.5.2 → **7.5.3**. New ids: `s-7-0-1`, `s-7-1-1`, `s-7-1-2`, `s-7-2-1`, `s-7-3-1`, `s-7-3-ex`, `s-7-4-1`, `s-7-4-2`, `s-7-5-1`. No external page cited old Ch7 Illustration numbers.

**Chip re-homing (text unchanged, multiset unchanged):** pre-existing `KPMG FI 2024 · section 6` and `EY Closer look 2026 · section 5.2` sat on the EPS bullet, but KPMG EPS is section 5.3 (ch 6 = interim) and EY EPS is section 5.3 (5.2 = IAS 8). Both chips moved to where their locator is right (KPMG 6 → 7.4 interim lead; EY 5.2 → 7.0.1 IAS 8 row). Correct EPS chips added (`section 5.3`).

**Flags — reproduced, not reconciled:**
- None between firms on Ch7 substance (KPMG and EY agree on IAS 7, IAS 33 and IAS 34 changes; iGAAP mirrors Closer look).
- EY 5.1 cites “[IAS 7(2027).34A, IFRS 18.BC53]” for interest classification; IFRS 18 BC53 is about materiality — likely IAS 7 BC; not reproduced.
- KPMG lists three numerator types (required total/subtotal; listed common subtotal; MPM); EY lists two (paras 69/86/118 total or subtotal; MPM) — same content, different grouping; shown as Official-paragraph grouping in 7.3.1.
- IAS 7 / IAS 33 / IAS 34 paragraph numbers (18(b), 33A, 34A–34D, 73B–73C, 10, 16A(m)) come from firm text; amended texts not attached (App D says incorporated into those Standards). Shown in prose with firm chips; no new Official IAS 7 / IAS 34 chips.
- S1 scope still open: paras 130–132 referenced by locator only (Ch1 1.3.2), not taught.

**DTT A4:** locked chip only. **PwC:** missing.

**Debt (not edited):** Concept Map `ch07` not updated for 7.0.1 / 7.1.1–7.1.2 / 7.3.1 / 7.4.1–7.4.2 / 7.5.1.

**Screenshots — Gate 2g** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2g/`): `g2g-ch07-desktop-{top,full}.png`; crops `g2g-ch07-s70-s701-scope-amendments`, `-s71-s711-s712-scf-interest-dividends`, `-illus713-ey-ill51-scf`, `-s714-scf-decision`, `-s72-s721-sfp-carried-changed`, `-illus722-xyz-sfp`, `-s73-s731-eps-numerators`, `-illus732-ey-ill52-53-s733`, `-s74-s741-s742-interim`, `-s75-s751-capital`, `-illus752-ee-group`, `-illus753-ff-group-tail`.

**Chips listed again (unchanged, still awaiting Q1–4 / S3 — NOT APPROVED):** Ch3 `IFRS 18 · para B… returns test`; Ch3 `IFRS 18 · para IE Figure 5`; Ch1 bare `KPMG FI 2024`; Ch1 ×2 + Ch7 ×1 `DTT A4 2022 · IAS 1 bridge`; EY iGAAP no chip format (zero chips); DTT · 8.1 / References and point-chip wrap (S3) unchanged.

## Gate 2h — Ch8 densify (2026-10-02 20:02 HKT)

**Scope kept:** `ch08.html` teaching body + key terms. Concept Map iframe, chrome, disclaimer, footer untouched (except stamp). No new `h3`: 8.0–8.6 kept; titles: 8.0 “Scope of this chapter” → “Scope — effective date, transition and first-year duties”; 8.5 “Optional election (thin)” (hedge) → “IAS 28 fair value election on initial application”. **All 10 pre-existing ids kept** (`s-8-0` … `s-8-6`, `s-8-3-appc`, `s-8-4-ex`, `s-8-4-ey`, `s-8-4-kpmg`); inbound links (`#s-8-2`, `#s-8-4` from Ch6 / Ch7) still resolve. Backup (not committed): `/tmp/g8/ch08-orig.html`.

**Sources read for Ch8 before writing:** Official App C (C1–C8, incl. IFRS 19 references in C2 / C5), App D, BC414–BC423, B14–B15; KPMG FI 6.2, 7, 7.1, 7.2 (FAQ additional comparatives; FAQ why elect FV), 5.2; EY Closer look section 6 (incl. How we see it: plan ahead, phased transition; local-regulator reconciliations), 6.1 (Ill 6-1), 7 (future developments), 3.3.5.A (IAS 28.18 extract, ED/2026/1); **EY iGAAP Ch04 section 6–7** (compared; zero chips).

**Metrics (before → after):** article prose 980 → 2,186 words (chips excluded); page size 16.7k → 30.1k chars; chips 48 → 95 (Official 31 → 58, KPMG 10 → 15, EY 7 → 22; distinct 22 → 39); `h4` units 0 → 5; tables 4 → 8; Illustrations 1 (+3 non-Illus strips) → 1 Illustration (Facts / Assessment / Decision), 0 non-Illustration worked-strips. Source-label leads 0; author meta 1 → 0; `§` 8 lines → 0; plain “see N.N” 0; point-chips 1 (rewritten from a page-layout instruction to an entity pitfall; shortened to stay inside the S3 clamp — scrollWidth = clientWidth); HTML balanced; all anchors resolve. **Chip multiset: every pre-existing chip string still present at ≥ original count** (one `para C3` re-added after first QA).

**What changed (by section):**
- **8.0** retitled; “Standard primary” → “Big4 alignment.”; “No invented timelines” (author meta) → “Calendar used here.”; App D link to Ch7 7.0.1; pitfall rewritten. **8.0.1** Appendix C at a glance (C1–C8).
- **8.1** BC414 / BC416 why 2027; BC415 implementation (systems, covenants, remuneration, MPM audit discussions); EY plan-ahead and phased-transition views; EY section 7 pending IFRS IC submissions; link Ch1 1.2.1.
- **8.2** IAS 8.28(f) content (EY); IFRS 19 178(f); BC417 why retrospective; BC418 replacement; KPMG additional-comparatives FAQ moved here from the KPMG strip; link Ch6 6.5.
- **8.3** BC418 why; BC419–BC420 why not current period; EY local-regulator note; “Firm cue” → “Systems.” **8.3.1** App C strip `#s-8-3-appc` → h4 table (title “(para C3; no Official numeric IE)” removed; “Teaching paraphrase” column → “Requirement”; + Not required / Replaces rows).
- **8.4** lead adds IAS 34.10 set-aside; BC421 / BC422 reasons; 16A(a) meaning (EY); link Ch7 7.4. **8.4.1** duties table (former untitled table; + optional extras, IFRS 19 246(a)). **Illus 8.4.2** EY Ill 6-1: meta lines (“not invented CU amounts”, “multi-firm write-once”, “see App C box”) removed; table headers + “* Retrospectively restated” footnote; Decision box. **8.4.3** decision strip `#s-8-4-ex` → table (“(Standard dates only)” removed). **8.4.4** KPMG strip `#s-8-4-kpmg` → table (“Honest gap” meta removed; goodwill transitional silence kept as KPMG’s point).
- **8.5** C7 full; IAS 28.18 eligible entities (EY extract) + KPMG examples; BC423 why; KPMG FAQ operating-profit effect (link Ch3 3.3.2); ED/2026/1 (EY). “Teaching awareness only” removed.
- **8.6** list → timeline table (before 1 Jan 2027 → after first annual).
- **Key terms** `§` → para; + IAS 8 para 28(f), IAS 28 fair value election (para C7).

**Renumbering (ids unchanged):** `#s-8-3-appc` → **8.3.1**; former untitled interim table → **8.4.1** (new id `s-8-4-1`); Illus `#s-8-4-ey` 8.4.1 → **8.4.2**; `#s-8-4-ex` → **8.4.3**; `#s-8-4-kpmg` → **8.4.4**. New ids: `s-8-0-1`, `s-8-4-1`.

**Flags — reproduced, not reconciled:**
- None between firms on Ch8 substance.
- EY Ill 6-1 entity is “Entity Q” in Closer look but “Entity A” in iGAAP Ch04 — same facts; pack uses Closer look (Q).
- EY iGAAP section 7 “Future developments” (IFRS IC agenda decisions referencing IAS 1) differs from Closer look section 7 (pending IFRS IC submissions); pack cites Closer look only.
- KPMG: IFRS 18 silent on the goodwill line item in the transitional-year interim balance sheet — shown as KPMG’s observation.
- EY phased-transition and local-regulator points are EY views — labelled “EY’s view”.

**DTT A4:** not used. **PwC:** missing.

**Debt (not edited):** Concept Map `ch08` not updated for 8.0.1 / 8.4.1 / 8.4.4 / 8.6 table.

**Screenshots — Gate 2h** (desktop 1280, `/opt/cursor/artifacts/screenshots/gate2h/`): `g2h-ch08-desktop-{top,full}.png`; crops `g2h-ch08-s80-s801-scope-appc`, `-s81-effective-date`, `-s82-retrospective`, `-s83-s831-annual-recon`, `-s84-s841-interim-duties`, `-illus842-ey-ill61`, `-s843-s844-calendar-practical`, `-s85-s86-election-timeline`.

**Chips listed again (unchanged, still awaiting Q1–4 / S3 — NOT APPROVED):** Ch3 `IFRS 18 · para B… returns test`; Ch3 `IFRS 18 · para IE Figure 5`; Ch1 bare `KPMG FI 2024`; Ch1 ×2 + Ch7 ×1 `DTT A4 2022 · IAS 1 bridge`; EY iGAAP no chip format (zero chips); DTT · 8.1 / References and point-chip wrap (S3) unchanged.

## Gate 3 — Pack Map enhance (2026-10-02 20:06 HKT)

**Scope:** `index.html` Map board and its mirror `visuals/map-jumpboard.html` (same edits, `../` + `target="_parent"`). No CSS edits (`map.css`, `shared.css`, `draft.css`, `map-jumpboard.css` untouched). Backups (not committed): `/tmp/g9/index-orig.html`, `/tmp/g9/map-jumpboard-orig.html`.

**Changes (Gate 1 section H items closed):**
- Header rules: “Replaces IAS 1 for presentation &amp; disclosure teaching” (author wording) → “Supersedes IAS 1 · much of IAS 1 carried forward or moved to IAS 8 / IFRS 7” (→ Ch1 1.3); + **Figure 1** rule “changes focus on the P&amp;L · limited SCF / SFP changes” (→ Ch1 1.3.1; Official Figure 1 as the sourced story); 1 Jan 2027 rule → “annual periods beginning on or after · early application permitted”.
- Structured P&amp;L see-also: “(later; overview in Ch3)” hedge → specified-main-business-activity sentence (→ Ch3 3.5).
- Grouping pillar: + “Cross-references” cell (para 114 → Ch2 2.1.4) — fills the empty column height.
- MPM pillar: “Single audited note” (technical-strict fail; para 122 says single note) → “Single note”; `§118` → para 118; + “Presumed management’s view” (→ Ch6 6.2) and “Interim notes too” (→ Ch7 7.4) — fills the empty boxes.
- Visit strip: step 5 label “Operating expenses” → “Expenses” (`title="Operating expenses"`), so 1→8 fits one row at 1280 (measured: all steps on one line; was “8 Transition” orphaned on line 2).
- Ch7 close box: 3 → 6 cells (SCF, SFP, EPS, Interim, Capital, IAS 8); “thin IAS 7 bridge”, “Carried with structured-summary lens”, “Additional-measure limits” replaced with sourced one-liners.
- Ch8 close box: 2 → 4 cells (Retrospective, Annual reconciliation, First-year interims, IAS 28 election); “Apply as if always in force” → “Restate comparatives under IAS 8 · no para 28(f) amounts”; `§C3` / `§C4–C5` → para.
- Result: `§` 0, “thin” 0, “audited” 0, “(later” 0 on both Map files; all hrefs resolve (only the pre-existing homepage link is outside the pack).

**Not changed:** chrome tag row, pillar structure / mini-P&amp;L bands, span bar, disclaimer, footer. Concept Map visuals per chapter → Gate 4.

**Screenshots — Gate 3** (`/opt/cursor/artifacts/screenshots/gate3/`): `g3-map-desktop-before.png`, `g3-map-desktop-full.png`, `g3-map-jumpboard-desktop-full.png`.

**Chips:** Map has no cite chips (unchanged). Cite Q1–4 / S3 — NOT APPROVED, unchanged.

## Gate 4 — Consistency pass (2026-10-02 20:16 HKT)

**Scope:** `ch01.html`, `ch02.html`, `ch03.html`, `references.html`, `visuals/ch01…ch08-*.html` (10 visuals). No CSS edits (`shared.css`, `draft.css`, visual `*.css` untouched). Backups (not committed): `/tmp/g10/`.

**Changes:**
- Ch1 (23) / Ch2 (3) cross-chapter link text “Ch7 §7.1” → “Ch7 7.1” (Ch4–Ch8 form). Pack chapters + Map + References: `§` 0.
- Visuals: chip text `§47` → `para 47` (range form `para X–Y`, as chapter chips); label/title text → “Para N” / “para N”; sentence text → “paragraph N” (e.g. Ch4 “paragraph 65(a)(ii)”, Ch8 “paragraph 69–74 subtotals, despite IAS 34 paragraph 10 relief”). Visuals `§` 0. Chip count per visual unchanged; IDs unchanged.
- Visual hedge/meta: Ch1 “Thin rules” → “Limited rules”; Ch1 “Effective-date cue” → “Effective date and transition” (matches Ch1 1.4 h3); Ch1 MPM “single audited note” → “single note” (para 122; same fix as Map Gate 3); Ch5 aria “Gate — any function line…” → “Test — …”; Ch7 “See also … SCF nuances (later)” → 7.1 badge deep-linked to Ch7 7.1.2 (specified main business activities in the statement of cash flows).
- Ch1 visual “Prepare — category mapping · MPM inventory · systems” node (Gate 1 item: no chip): + 1.2 badge → Ch1 1.2.1, which carries the KPMG FI 2024 · section 1.2 key-actions chips (classify into the new categories; completeness of MPMs identified; systems, processes and controls). No firm chip added to the visual (visuals carry Official short chips only).
- Heading form: Ch1 (7) / Ch2 (13) h4 “1.1.1 Title” → `<strong>1.1.1 — Title</strong>` (Ch3–Ch8 form); Ch1 five h3 wrapped in `<strong>` like Ch2–Ch8. Text otherwise identical; IDs and chips unchanged.
- Ch2 2.3.6 FX: + link “category detail: Ch3 3.7.5”.
- Ch3 3.9 index: EY Ill 3-12 row + “also Ch4 Illustration 4.5.1” (same EY illustration taught in both places).
- `references.html`: + Official rows for every chip prefix in use but missing (IAS 8 — renamed title per KPMG FI 2024 / EY Closer look 2026 —, IAS 20, 21, 28, 29, 40; IFRS 3, 8, 9, 17); method note: these appear only as cross-reference locators, texts not attached. Big 4 rows unchanged (no iGAAP row, no DTT rename — A3/A4 not approved).

**QA:** `/tmp/audit/qa.py` all chapters `§inProse=0`, `authorMetaHits=0`, `plainSee=0`, `gateWord=0`; Ch1 `bareWorkChips=1` = locked bare `KPMG FI 2024`. Cross-ref link-number check: 0 mismatches (2 accepted: Ch1 range “2.3–2.4”; Ch3 path visual 3.5 → embedded anchor in 3.5). Chip multiset ch01–ch03 unchanged (227 / 318 / 861). Visual overflow scan on edited text: none.

**Not changed:** Concept Map structure of ch04–ch08 visuals (no new nodes — densified units reachable via chapter h4s; adding nodes would need visual CSS work); S3 point-chip CSS; Cite Q1–4 chips.

**Screenshots — Gate 4** (`/opt/cursor/artifacts/screenshots/gate4/`): `g4-visual-<name>.png` ×8 (ch02, ch03 ×3, ch04, ch05, ch06, ch08), `g4-visual-ch01-whats-new-prepare.png`, `g4-visual-ch07-other-fs-see-also.png`, `g4-references-desktop-top.png`, `g4-references-desktop-full.png`, `g4-ch02-s236-fx-link.png`, `g4-ch03-s39-illus-index.png`, `g4-ch01-desktop-top.png`, `g4-ch07-desktop-top.png`, `g4-ch01-s11-s111-heading-form.png`, `g4-ch02-s20-s201-heading-form.png`.

**Chips listed again (unchanged, NOT APPROVED):** Ch3 `IFRS 18 · para B… returns test`; Ch3 `IFRS 18 · para IE Figure 5`; Ch1 bare `KPMG FI 2024`; Ch1 ×2 + Ch7 ×1 `DTT A4 2022 · IAS 1 bridge`; EY iGAAP zero chips; S3 point-chip wrap unchanged.

## Gate 5 — KEY CHANGES handoff (2026-10-02 20:16 HKT)

**Written:** `OPUS-IFRS18-KEY-CHANGES-2026-10-02.md` (pack folder) for Grok review — gate log, baseline → now metrics (words 23,845 → 54,048; chips 959 → 2,377; h4 9 → 92; Illustrations 24 → 39; tables 45 → 118), key changes by chapter, Map + consistency summary, flags table, NOT APPROVED asks (A1–A4, S1, S3), known debt, untouched files, screenshot folders, re-check commands. No HTML edits at Gate 5 (stamp stays `2026-10-02 20:16 HKT`).

**S3 measured at 1280 (for the handoff):** 25 of 26 point-chips clamped (Ch1 2, Ch2 3, Ch3 4, Ch4 5, Ch5 5, Ch6 6); Ch8 1 fits; Ch7 0.

**Gate 1 KPMG uncited sections — all now cited** (1.2, 2.1.1.2–2.1.1.3, 2.1.3.1–2.1.3.2, 2.1.5, 2.2.3, 3.4, 5.1.1, 5.2, 5.3, 6.1, 8.1, 8.2). KPMG illustrative income statements not reproduced as plates (bank shape from EY Figure C.2-1).

---

# Job #7 — skill-align log (unchanged)

**Date:** 2026-10-02 16:20 HKT  
**Runner:** Grok 4.7. Structure / chrome / vocabulary only. No densify. No CF. No IAS 2.  
**Pack:** `refs/ifrs-18/draft-v1-linked/`  
**Stamp:** `Last update · 2026-10-02 16:20 HKT` (was `2026-10-02 01:48 HKT`)  
**draft.css cache:** `ifrs18-skill-align-20261002b` (h4 rule only). Other CSS cache keys unchanged.

---

## Demotions — wrong-shape, not invent

Nine reference matrices were still titled `Illustration:` inside `.worked-strip`. They are now numbered `h4` sections. Old `id`s kept. No fake company, CU, or case facts were added or labelled invent. `Illustration:` and the italic “(section matrix — not an Illustration)” note are gone. Cite chips moved off the title to a paragraph at the end of the unit (non-Illustration placement).

| Was | Now | id |
|---|---|---|
| Illus 1.5.1 IE pack map | `h4` + part lists | `s-1-5-ex` |
| Illus 2.4.1 Informative labels / Fig 7 | `h4` + list + table | `s-2-4-fig7` |
| Illus 3.1.1 Categories without specified MBA / Fig 2 | `h4` + list + table | `s-3-1-fig2` |
| Illus 3.4.1 Hybrid host liabilities / Fig 4 | `h4` + list + table | `s-3-4-fig4` |
| Illus 3.5.1 Investing MBA / Fig 3.1 | `h4` + list + table | `s-3-5-fig31` |
| Illus 3.5.2 Financing-to-customers MBA / Fig 3.2 | `h4` + list + table | `s-3-5-fig32` |
| Illus 3.5.3 Cash & CE with specified MBA / Fig 3.3 | `h4` + list + table | `s-3-5-fig33` |
| Illus 3.4.2 Derivatives gains/losses / Fig 5 | `h4` + list + table | `s-3-5-fig5` (left in place; not moved under §3.4) |
| Illus 6.1.1 Identifying MPMs / Fig 6 | `h4` + list + table | `s-6-1-fig6` |

Facts / Assessment column labels were the wrong-shape dressing and were dropped. The sentences inside those columns were kept, except the author-meta lines below. Where a peer title was a real part name (Part I / II / III on 1.5.1), the label was kept.

**Overlap left for Opus (do not treat as missing content):** on the figure plates the bullet list still restates the table. Unique lines that are not in the table and must survive any later collapse:

- Fig 2 footnote on FX / derivatives (B65–B76) — list only
- Fig 6 presumption footnote (§119) — list only
- Fig 7 “other” is a last-resort label — list only
- Fig 7 starting-point sentence — list only

**Author-meta removed from the reader page** (was inside the wrong-shape peers; recorded here, not deleted from the record):

- `No invent: do not add entity facts beyond the cited IE / firm plate.` (was on 3.5.1, 3.5.2, 3.5.3, 3.4.2)
- `Supporting table/figure below carries Official or firm amounts and gate labels — read peers with the table.` (same four; “peers” no longer exist after unwrap)
- `See supporting table/figure below — labels and amounts from the cited Official or firm source.` (was the empty Facts column on 3.5.3 and 3.4.2)

---

## Gate wording (Ch3 narrative only)

15 reader-facing hits (inventory said ~12). The questions were not rewritten.

| From | To | Count |
|---|---|---|
| next gate | next test | 6 |
| gate labels | test labels | 4 |
| Investing / Financing gates | Investing / Financing tests | 2 |
| ordered category gates | ordered category tests | 1 |
| overview gate | overview decision | 1 |
| at that gate | at that test | 1 |

Ch3 `ch03.html` word-bounded `gate` / `gates` = 0 after the swap.

**Not this wave (visual class / aria, not Ch3 narrative):**

- `visuals/ch03-classification-path.html` class `pc-gate` (reader text already says the test questions; no visible word Gate)
- `visuals/ch05-operating-expenses.html` `aria-label="Gate — any function line on the face"` and class `oe-gate`
- `visuals/ch06-mpms.html` class `gt-gate`

Renaming those classes is a visual CSS edit. Not done. No pillar redraw.

METHOD author lines that told the next writer to put “Gate” on the page were aligned to Decision / Test (four lines in `IFRS18-CONTENT-REWRITE-METHOD.md`).

---

## Differ callout — not added

Zero `.callout.differ` before and after. No page already states two different treatments side by side in a form that only needed shaping. No callout invented.

---

## Cite ask — do not rename

Ch3 Entity C box (`#s-3-9-ey`, EY Ill 3-1) still has:

`IFRS 18 · para B… returns test`

**ASK Johnny** for the Official locator from the PDF before any rename. Not invented here. Body-prose `§` outside chips was not swept. Zero `§` inside `.cite` chips (unchanged PASS). PwC still not on disk. No PwC chips.

---

## Map — drift log (agents only)

No chip-order lecture note on `index.html` or `visuals/map-jumpboard.html`. None added.

**Reading-order narration (desktop, DOM = walk). Verdict: PASS.** No geometry change.

Start → frame title chip 1 (What’s new vs IAS 1) → header rules L→R (Replaces IAS 1 | 1 Jan 2027) → pillar row L→R: Structured P&L (chips 3/4, statement T→B, operating expenses chip 5 nested inside Operating) → Grouping (chip 2) → MPM (chip 6) → spanning bar → visit strip L→R 1→8 → close row L→R Other FS (7) | Transition (8). End.

Chip jumps 3/4 → 2 → 6 match the three requirement-set story, not chapter TOC. Continuing route does not run R→L.

| Visual | Chip order on the visual | Body / chapter order | Proposed restructure |
|---|---|---|---|
| Pack Map pillar row (`index.html` and `visuals/map-jumpboard.html`) | 1 (frame) then 3/4 with 5 nested, then 2, then 6; visit strip separately 1→8; close 7 then 8 | Chapters 1→8 | None this wave. Keep the pillar row on the three-set story. Do not renumber body sections to force 1→8 across the pillars. |

---

## Case-study Illustrations left as Illustrations

24 plates still titled `Illustration:` and already `.worked-strip` + `.worked-strip-grid`, neutral peers, `<div class="box-body"><ul>`. No structure patch. No bullets added.

2.1.1, 2.1.2, 2.3.1, 3.5.4, 3.5.5, 3.8.1–3.8.4, 4.1.1, 4.2.1, 4.5.1, 5.1.1, 5.1.2, 5.2.1, 5.3.1, 6.4.1, 6.4.2, 7.1.1, 7.2.1, 7.3.1, 7.5.1, 7.5.2, 8.4.1.

Bullet-text floor (≤5 lis or ≲350 chars) is clear on all 24. That is not a densify PASS. Thinnest bullet text is 3.8.2 (6 lis / ~524 chars) beside an IE face table. Re-classify against the PDFs is still Opus.

Ch8 `s-8-3-appc` and `s-8-4-kpmg` are single-column `.worked-strip` boxes and are **not** titled Illustration. Left as teaching. Not given a fake peer grid.
