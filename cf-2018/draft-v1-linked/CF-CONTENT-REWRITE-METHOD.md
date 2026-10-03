# Conceptual Framework 2018 — Content rewrite method (standing, Ch1–Ch9)

**Owner:** Content implement (Grok / agents)  
**Reviewer:** Johnny Pang  
**Locked:** 2026-09-30 (Asia/Shanghai) — Johnny phase + format locks for teaching body
**IAS 2 parity wave:** 2026-10-01 — EY Ch2 + KPMG 1.2 unlocked; Ch9 Combined + Ch10 Carve-out; Status → Ch11; Crosswalk A/B started.
**Cite / Illus grammar:** IAS 2 trial rollout applied **2026-10-01** (see `CF-SKILL-ROLLOUT-2026-10-01.md`) — `CF 2018 · para …`; firm+work+locator; **zero `§` in chips**; Illus = `Illustration: N.M.k — Title` + title chips; **Map enhance unlocked 2026-10-01** (chapter-top + pack Map)  
**Applies to:** `draft-v1-linked/ch0N.html` teaching `<article>` bodies; per-chapter `CF-CH0N-CONTENT-NOTES.md`  
**Map unlock (Johnny 2026-10-01 full pass):** chapter-top Concept Maps + pack `index.html` Map may be enhanced per [IFRS visual grammar](sand-workflow:ifrs-visual-grammar) (story + visit path; technical-strict labels; cache-bust iframes). Do **not** restyle Illus peers with Map leaf green/red. Overview retired (site Ch1–Ch9).

**Skills:**  
- Body / study-pack content → [IFRS teaching body](sand-workflow:ifrs-teaching-body)  
- Concept Maps / visuals only → [IFRS visual grammar](sand-workflow:ifrs-visual-grammar)

---

## Big4 completeness pre-flight (CF 2018 — fixed 2026-10-01)

**Prior full-pass error:** EY/KPMG wrongly marked `not on disk`. **Corrected** — both layer-2 manuals are on disk (see table). Crosswalk A/B files: `CF-XREF-OFFICIAL-TO-BIG4-2026-10-01.md`, `CF-XREF-BIG4-TO-OFFICIAL-2026-10-01.md`.

| Layer | Firm / source | Work | On disk? | Path |
|-------|---------------|------|----------|------|
| 1 | Official | CF 2018 (2026 stamp) | **Yes** | `inputs/cf-2018/official-conceptual-framework-2026.pdf` (+ HTML / HK archive) |
| 2 | DTT | A2 2022 Conceptual Framework | **Yes** | `inputs/cf-2018/dtt-2022-conceptual-framework-moa.pdf` |
| 2 | PwC | MOA 2020 intro · Conceptual Framework | **Yes** | `inputs/pwc-2020-moa/01-conceptual-framework-intro.pdf` |
| 2 | PwC | MOA 2020 Appendix 2 Combined/Carve | **Yes** | `inputs/pwc-2020-moa/appendix-2-combined-carve-out.pdf` |
| 2 | EY | IGAAP 2026 **Ch2** The IASB’s conceptual framework | **Yes** | `inputs/ey-international-gaap-2026/International-GAAP-2026-part1.pdf` (book ~pp 46–103) |
| 2 | KPMG | Insights 2019/20 Part1 **· 1.2** Conceptual Framework (= **2018 CF**) | **Yes** | `inputs/kpmg-2019-2020/part1-non-fi.pdf` |
| 3 | KPMG | Combined and/or carve-out FS (Feb 2022) — CF Ch3 app | **Yes** | `inputs/cf-2018/kpmg-public/kpmg-combined-and-carve-out-financial-statements.pdf` |
| 3 | KPMG | Flyer Apr 2018 (background) | **Yes** | `inputs/cf-2018/kpmg-public/kpmg-2018-04-conceptual-framework-print-friendly.pdf` |
| 3 | EY | IFRS Developments 169 (IFRS 3 ↔ CF) | **Yes** | `inputs/cf-2018/ey-public/ey-devel169-ifrs-3-conceptual-frwk-may-2020.pdf` |
| — | ACCA | SBR CF storyline | **Yes** | `inputs/cf-2018/acca/ACCA-SBR-CF-storyline-NOTE.md` — **visit path only; no cite authority** |

**Extracts:** `/workspace/cf2018-content-extract/ey-ch2-cf-raw.txt`, `kpmg-1.2-cf-raw.txt`, `kpmg-combined-carve-ch1-2.txt`, `pwc-appendix2-combined-carve.txt`.

**Two-way crosswalk:** required before pack-complete claim — see Crosswalk A/B files under `refs/cf-2018/` and `draft-v1-linked/`.


## Phase lock (Johnny 2026-09-30)

1. **Integrate Official CF + Big4 into one study pack first** (detail learning). Simplify later — do **not** thin the pack in this phase.
2. Concept Map may **start** the page. **Map enhance unlocked** for CF (2026-10-01): chapter-top Maps + pack Map in scope with body densify; story + visit path required; no invent.
3. **Quote-heavy is OK now** — prefer Official `<q>` extracts + Big4 support over paraphrase.
4. **Decision strips / trees are OK** if **no invented facts** — every gate cites Official CF or Big4.
5. **Include ALL Official examples/illustrations + Big4 examples** that belong to the chapter topic; wrap case-study / worked plates as **`.worked-strip`** titled `Illustration: N.M.k — Teaching Title` + FULL cite chips on the title. Decision strips / teaching cues are **not** Illus. Reproduce tables / key figures faithfully with cites — **not invented numbers**. Do **not** leave examples “thin” or NOTES-only.
6. **CF has no separate IE/IG series** — examples live inside Official paras / BC narrative and in firm MOA text / FAQs. Cite as `CF 2018 · para …` / `BC` / `SP` / firm locator (**no `§`**).

---

## Format rules (mandatory)

1. **Bold key points** — every teaching key idea wrapped in `<strong>…</strong>` (section lead sentences, bullet heads, matrix axis labels that carry the teaching point).
2. **Layers of bullet points** — nested `<ul>` / `<ol>` for **super detail** (not brief). Under each teaching set, expand with:
   - **Official CF** extract (`SP` / `para` / `BC`) in `<q>…</q>` + cite chip
   - **Big4** extract (DTT A2; PwC MOA intro when present) in `<q>…</q>` or short firm paraphrase with cite chip
3. **Tables / matrices — not mandatory; use when multi-column helps**
   - Prefer a table when the content naturally has **more than 2 columns** (comparison, multi-axis, three sets, firm alignment next to Official).
   - Do **not** force every section into a table. Linear teaching (objective, pitfall, status cue) can stay nested bullets.
   - **Inside table cells**, nested `<ul>` / `<ol>` bullets are OK and **preferred** for detail.
4. **Big4 dedupe** — if several firms say the **same** thing, merge into **one** row/bullet with multiple cite chips (e.g. DTT · PwC). Keep distinct firm views in **separate** bullets/rows when they differ. Overlap → one dense unit + ensure supporting cite chips present (no invent-piled chips; no unique-detail thin).
5. **Line-boxed examples / Illustrations** — for each chapter-relevant Official illustration and Big4 FAQ/illustration:
   - **IS Illus** (case study / worked entity / numeric / multi-gate Facts→Assessment) → `.worked-strip` + peer grid titled `Illustration: N.M.k — Teaching Title` + FULL cite chips **on the title only** (C1); peers **neutral** (no `.ok`/`.warn`).
   - **NOT Illus** (reference matrix / definition list / FAQ label alone / Decision strip) → section table/list or Decision strip; cite chips at **end of unit** (C2).
   - Faithful wording / figures from the source; **no invent**.
6. **Decision strip** — optional Start → Gate → Output (or tree) for judgement paths; **every step cited**; remove invented entity patterns. Decision strips are **not** titled `Illustration:`.
7. **Visuals / Map** — **unlocked for CF** (Johnny 2026-10-01 full pass): enhance chapter-top Maps + pack Map per visual-grammar; cache-bust iframes; Illus peers stay neutral. Content-only micro-edits may still leave Map alone if handoff says so.
8. **Cite chips (IAS 2 trial grammar — Johnny 2026-10-01)** — firm+work+locator inside each `.cite` span; **zero `§` in any chip**.
   - Official: `CF 2018 · para [ref]` (e.g. `CF 2018 · para 2.16`, `CF 2018 · para SP1.2`, `CF 2018 · para BC4.14`). Cross-standard: `IAS 8 · para 11`. Cover meta: `CF 2018 · 2026 cover`. **Never** `Official · …` or bare `§N`.
   - DTT: `DTT A2 2022 · …` (no `§`).
   - PwC: `PwC MOA 2020 · …` / FAQ id (no `§`).
   - EY: `EY IGAAP 2026 · Ch2 · section …` (no `§`).
   - KPMG: `KPMG Insights 2019/20 · 1.2.…` / Example id; Combined/Carve app: `KPMG Combined/Carve 2022 · …` (class `cite-kpmg`).
   - PwC Combined/Carve: `PwC MOA 2020 · A2.…`.
   - ACCA storyline: **no cite chips** (visit path / Map narrative only).
   - Typography: Calibri Light / 11px / weight 300; house inherits.
   - Placement: Illus → title chips only; teaching `<p>`/`<li>`/non-Illus boxes → chips at **end of unit**.
9. **Anchors** — Preserve `#s-N-…` ids that Map / visual chips deep-link to.
10. **Site labels** — Conceptual Framework / IFRS / IAS only (no HKFRS / HKICPA dual code on UI). Official HK text is treated as IFRS; say **Board** / **IFRS Standards** on site.
11. **Technical-strict titles** — h2/h3/h4, Illus teaching names, peer labels use IFRS/CF wording (no consultancy/flowery labels).

---

## Content rules (substance)

| Rule | Detail |
|------|--------|
| **Quote Official + Big4** | Official PRIMARY: `inputs/cf-2018/official-conceptual-framework-2026.pdf` (HK June 2026 / CF (2027) stamp — March 2018 substance; see `inputs/cf-2018/OFFICIAL-SOURCE-NOTE.md`). Compare archive `official-conceptual-framework-hk-2022-09.pdf`. **2010 CF PDF not in pack** — DTT A2 for 2018-vs-2010 deltas only. Firms: **DTT** 2022 A2; **PwC** MOA 2020 intro + Appendix 2 Combined/Carve; **EY** IGAAP 2026 Ch2; **KPMG** Insights 2019/20 · 1.2 (+ KPMG Combined/Carve 2022 app + flyer). Ignore `pwc-2020-moa/HKAS/`. ACCA storyline = visit-path only (no cite authority). |
| **Official quotes primary** | Prefer short `<q>` extracts + cite chips over free rewrite. Firms support / align; do not replace Official. |
| **No invented examples** | No entity fact patterns not in Official §§/BC or firm materials. Teaching cues = firm quote + Official aim OK. Decision strips cite gates only. |
| **Examples complete** | Every Official illustration / Big4 FAQ-with-body that belongs to the chapter appears as a line box in the body (not NOTES-only). If a PwC FAQ title has **no answer body** in the pack extract, note the gap in NOTES — do not invent the answer. |
| **Anchors** | Preserve `#s-N-…` Map deep-links. |
| **Leave iframe / visuals alone** | No cache-bust or copy change in visuals unless Johnny OK’d a visual pass. |
| **Site labels** | CF / IFRS / IAS only (no HK dual codes on UI). |
| **Do not split for split’s sake** | Keep existing section grain unless teaching logic truly requires a split. |

---

## Per-chapter workflow

1. Inventory sources in NOTES `(a)` (paths under `inputs/cf-2018/` and allowed PwC intro) — list Official §§/BC illustrations + DTT/PwC pieces that belong to the chapter.
2. Gap prior body in NOTES `(b)` — missing quotes, thin examples, invented patterns, missing firm section chips.
3. Backup `ch0N.html` under `/workspace/cf2018-content-extract/` with timestamp before edit.
4. Rewrite **body only** to format rules; keep chrome, Concept Map fieldset/iframe, key-terms (unless cite chips broken), footer-nav.
5. Record boxes added, matrices kept/added, left-outs, backup paths in NOTES `(c)–(e)`; open questions / honest gaps in `(f)`.
6. Fold any Johnny format steer into **this METHOD** and the **IFRS teaching body** skill (principle only — no chapter dump).

---

## Site chapter ↔ Official / firm map

| Site | Official | DTT A2 | PwC | EY IGAAP Ch2 | KPMG |
|------|----------|--------|-----|--------------|------|
| Ch1 Objective & users | CF Ch1 / BC1 | A2 · 4 | MOA · 1.18–1.28 | Ch2 · section 4 | Insights 1.2.20 |
| Ch2 Qualitative | CF Ch2 / BC2 | A2 · 5 | QC / materiality | Ch2 · section 5 | Insights 1.2.30–1.2.45 |
| Ch3 Reporting entity | CF Ch3 / BC3 | A2 · 6 | FS + RE | Ch2 · section 6 | Insights 1.2.50–1.2.100 |
| Ch4 Elements | CF Ch4 / BC4 | A2 · 7 | elements | Ch2 · section 7 | Insights 1.2.110–1.2.130 |
| Ch5 Recognition | CF Ch5 / BC5 | A2 · 8 | recognition | Ch2 · section 8 | Insights 1.2.140–1.2.160 |
| Ch6 Measurement | CF Ch6 / BC6 | A2 · 9 | measurement | Ch2 · section 9 | Insights 1.2.170 / Ex3 |
| Ch7 Presentation | CF Ch7 / BC7 | A2 · 10 | presentation / OCI | Ch2 · section 10 | Insights 1.2.180 |
| Ch8 Capital | CF Ch8 / BC8 | A2 · 11 | capital | Ch2 · section 11 | (thin in 1.2) |
| Ch9 Combined FS | CF 3.10–3.14 / BC3.20–21 | A2 · 6.2 | MOA A2 Combined | Ch2 · section 6.2 | Combined/Carve 2022 · 1–2 |
| Ch10 Carve-out | CF 3.10–3.14 (application) | A2 · 6.2 | MOA A2 Carve | Ch2 · section 6.2 | Combined/Carve 2022 · 1–2 |
| Ch11 Status | SP1.x / BC0 + IAS 8 | A2 · 2, 3, 12 | MOA · 1.16–1.17 | Ch2 · section 3.2 | Insights 1.2.10 |

---

## Ch1–Ch9 checklist (quick)

- [ ] Lead of each section + each major bullet head is **bold**
- [ ] Nested bullets under each set with **Official** + **Big4** extracts (quote-heavy OK)
- [ ] **All** chapter-relevant Official illustrations + Big4 examples (with bodies in pack) in `.box` / `.worked-strip` line boxes
- [ ] Table/matrix only where **>2 columns** helps (not forced); nested `<ul>` OK inside cells
- [ ] Decision strips (if any) cite every gate; no invented entity facts
- [ ] Same Big4 points merged (multi cite chips); distinct firm views kept separate
- [ ] No invented examples; EY/KPMG/PwC A2 only from packed paths; no HKAS/ PwC use
- [ ] Cite chips: `CF 2018 · para …` / firm+work+locator; **zero `§`**; Illus chips on title; teaching chips at end of unit; Official `fn` when applicable
- [ ] Anchors preserved; Map enhance OK when unlocked (story + visit path; Illus peers still neutral)
- [ ] NOTES updated with box IDs added; visual suggestions (if any) in NOTES only
- [ ] Site labels CF / IFRS English only
