# IFRS 18 — Content rewrite method (standing, Ch1–Ch8)

**Owner:** Content implement (Grok / agents)  
**Reviewer:** Johnny Pang  
**Locked:** 2026-09-30 (Asia/Shanghai) — Johnny phase + format locks for teaching body
**Skill grammar rollout:** 2026-10-01 — cite/title/Illus-shape aligned to IAS 2 trial (CF 2018 still WAIT)  
**Applies to:** `draft-v1-linked/ch0N.html` teaching `<article>` bodies; per-chapter `IFRS18-CH0N-CONTENT-NOTES.md`  
**Maps:** Johnny unlocked I18 chapter-top Maps + pack Map tab for big-pass 2026-10-01 (visual-grammar story → visit path → draw). Content still owns Standard; Map chrome follows visual-grammar.  

**Skills:**  
- Body / study-pack content → [IFRS teaching body](sand-workflow:ifrs-teaching-body)  
- Concept Maps / visuals only → [IFRS visual grammar](sand-workflow:ifrs-visual-grammar)

---

## Phase lock (Johnny 2026-09-30)

1. **Integrate Standard + Big4 into one study pack first** (detail learning). Simplify later — do **not** thin the pack in this phase.
2. Concept Map may **start** the page; **I18 Maps unlocked** for big-pass 2026-10-01 (chapter-top + pack Map visit path). Follow visual-grammar; cache-bust iframes when Map HTML/CSS changes.
3. **Quote-heavy is OK now** — prefer Standard `<q>` extracts + Big4 support over paraphrase.
4. **Decision strips / trees are OK** if **no invented facts** — every decision cites Standard or Big4.
5. **Include ALL Standard IE/IG and Big4 examples/illustrations** that belong to the chapter topic; wrap each in a **line box** using existing `.box` / `.worked-strip` patterns (title e.g. `Standard IE7`, `KPMG FI 2024 · Illustration`, `EY Closer look 2026 · Ill 4-1`). Reproduce tables / key figures faithfully with cites — **not invented numbers**. Do **not** leave examples “thin” or NOTES-only.
6. **No separate IG numbered series** in the pack Official PDF — Application Guidance lives in **App B** (cite as B§). Illustrative Examples = **IE1–IE17** + Part I–III figures.

---

## Format rules (mandatory)

1. **Bold key points** — every teaching key idea wrapped in `<strong>…</strong>` (section lead sentences, bullet heads, matrix axis labels that carry the teaching point).
2. **Layers of bullet points** — nested `<ul>` / `<ol>` for **super detail** (not brief). Under each teaching set, expand with:
   - **Standard** extract (`IN` / `§` / `BC` / `C` / `B` / `IE`) in `<q>…</q>` + cite chip
   - **Big4** extract (KPMG FI; EY Closer look / MOA) in `<q>…</q>` or short firm paraphrase with cite chip
3. **Tables / matrices — not mandatory; use when multi-column helps**
   - Prefer a table when the content naturally has **more than 2 columns** (comparison, multi-axis, carry/move, three sets, firm alignment next to Standard).
   - Do **not** force every section into a table. Linear teaching (objective, pitfall, effective-date cue) can stay nested bullets.
   - **Inside table cells**, nested `<ul>` / `<ol>` bullets are OK and **preferred** for detail.
4. **Big4 dedupe** — if several firms say the **same** thing, merge into **one** row/bullet with multiple cite chips (e.g. KPMG · EY). Keep distinct firm views in **separate** bullets/rows when they differ (label “KPMG only” / “EY only” as needed).
5. **Line-boxed examples** — for each chapter-relevant Standard IE and Big4 illustration:
   - Prefer `.worked-strip` (title + `.worked-strip-grid` of `.box` peers) **or** a single `.box` with `.box-title` / `.box-body` when one plate is enough.
   - Title pattern: `Illustration: N.M.k — Teaching Title` + FULL cite chips on the title (firm/FAQ/IE ids in chips only). Decision strips / teaching cues are **not** Illus.
   - **FAQ ≠ Illus:** case study / worked entity / numeric → Illus; reference matrices / pack indexes / “no numeric Ill” → section content, not `Illustration:`.
   - **ALL Illus** = `.worked-strip` with **neutral** peer columns (no `.ok`/`.warn` on Illus peers). Prefer `.worked-strip-grid` peer boxes; table plates may keep supporting tables under peers.
   - Faithful numbers / line items from the source; no invent.
6. **Decision strip** — optional Start → Decision → Output (or tree) for judgement paths; **every step cited**; remove invented entity patterns. Reader-visible labels use Decision / Test / Assessment — never Gate.
7. **Visuals** — I18 Maps unlocked 2026-10-01: chapter-top Concept Maps + pack Map tab may be enhanced per visual-grammar (story → visit path; yes/no mid-arrow; box fit; lengthen short forks). Illus peers stay neutral.
8. **Cite chips (IAS 2 trial grammar — Johnny 2026-10-01)** — firm+work+locator inside each `.cite` span; **zero `§` in any chip**.
   - Official: `IFRS 18 · para [ref]` (e.g. `IFRS 18 · para 52`, `IFRS 18 · para IN9`, `IFRS 18 · para B42`, `IFRS 18 · para C1`, `IFRS 18 · Figure 2`). **Never** `Official · …` or bare `§N`.
   - EY: `EY Closer look 2026 · section …` / `Ill N` (use **`section`**, not `§`).
   - KPMG: `KPMG FI 2024 · section …` / `Example N` (use **`section`**, not `§`).
   - DTT: `DTT A4 2022 · …` (IAS 1 bridge only). **No PwC invent.**
   - **Placement split:** Illustration title chips only (C1); main teaching `<p>`/`<li>` chips at **end of unit** (C2).
   - Typography: Calibri Light / 11px / weight 300 (house inherits).
9. **Anchors** — Preserve `#s-N-…` ids that Map / visual chips deep-link to.
10. **Site labels** — IFRS / IAS only (no HKFRS dual code on UI).

---

## Content rules (substance)

| Rule | Detail |
|------|--------|
| **Quote Standard + Big4** | Official HKFRS 18 (= IFRS 18 on site): IN / § / BC / App B / App C / IE. Firms: **KPMG** First Impressions; **EY** Applying IFRS closer look. **DTT A4** only as IAS 1 / pre-IFRS 18 pitfall bridge. **No PwC invent** (no IFRS 18 PwC in pack). |
| **Standard quotes primary** | Prefer short `<q>` extracts + cite chips over free rewrite. Firms support / align; do not replace Standard. |
| **No invented examples** | No entity fact patterns not in Standard IE or firm materials. Teaching cues = firm quote + Standard aim OK. Decision strips cite each decision only. |
| **Examples complete** | Every IE / Big4 illustration that belongs to the chapter appears as a line box in the body (not NOTES-only). |
| **Anchors** | Preserve `#s-N-…` Map deep-links. |
| **Leave iframe / visuals alone** | No cache-bust or copy change in visuals unless Johnny OK’d a visual pass. |
| **Site labels** | IFRS / IAS only (no HKFRS dual code on UI). |

---

## Per-chapter workflow

1. Inventory sources in NOTES `(a)` (paths under `inputs/ifrs-18/`) — list Official IE/IG + KPMG/EY illustrations that belong to the chapter.
2. Gap prior body in NOTES `(b)` — missing quotes, thin examples, invented patterns.
3. Backup `ch0N.html` under `/workspace/ifrs18-chN-extract/` with timestamp before edit.
4. Rewrite **body only** to format rules; keep chrome, Concept Map fieldset/iframe, key-terms (unless cite chips broken), footer-nav.
5. Record IE/Big4 boxes added, matrices kept/added, left-outs, backup paths in NOTES `(c)–(e)`; open questions in `(f)`.
6. Fold any Johnny format steer into **this METHOD** and the **IFRS teaching body** skill (principle only — no chapter dump).

---

## Ch1–Ch8 checklist (quick)

- [ ] Lead of each section + each major bullet head is **bold**
- [ ] Nested bullets under each set with **Standard** + **Big4** extracts (quote-heavy OK)
- [ ] **All** chapter-relevant Standard IE + Big4 illustrations in `.box` / `.worked-strip` line boxes (faithful figures)
- [ ] Table/matrix only where **>2 columns** helps (not forced); nested `<ul>` OK inside cells
- [ ] Decision strips (if any) cite every decision; no invented entity facts
- [ ] Same Big4 points merged (multi cite chips); distinct firm views kept separate
- [ ] No invented examples; no PwC invent; DTT A4 = IAS 1 bridge only
- [ ] Cite chips: `IFRS 18 · para …` / firm+work+`section`…; **zero `§`**; Illus chips on title; teaching chips at end of unit
- [ ] Anchors preserved; iframe/visuals/Concept Map untouched
- [ ] NOTES updated with IE/Big4 box IDs added; visual suggestions (if any) in NOTES only


## Big4 pre-flight inventory (I18 pack — 2026-10-01)

| Firm | Work | Path / status |
|------|------|----------------|
| Official | HKFRS 18 (= IFRS 18 on site) | `inputs/ifrs-18/official-hkfrs18-2026-06.pdf` |
| KPMG | First Impressions IFRS 18 (2024) | `inputs/ifrs-18/kpmg-first-impressions-ifrs18.pdf` |
| EY | Applying IFRS: A closer look at IFRS 18 (Updated April 2026) | `inputs/ifrs-18/ey-2026-04-applying-ifrs-closer-look-ifrs18.pdf` |
| DTT | A4 Presentation of FS (IAS 1 bridge only) | `inputs/ifrs-18/dtt-2022-a4-presentation-fs-ias1.pdf` |
| PwC | — | **not on disk** for IFRS 18 (no invent) |

**Crosswalk A/B locator tables:** still open debt before any pack-complete claim (see I18-BIG-PASS note).
