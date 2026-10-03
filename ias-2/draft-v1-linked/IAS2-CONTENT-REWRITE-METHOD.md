# IAS 2 Inventories — Content rewrite method (standing, Ch1–Ch6)

**Owner:** Content implement (Grok / agents)  
**Reviewer:** Johnny Pang  
**Locked:** 2026-09-30 (Asia/Shanghai) — Johnny phase + format locks for teaching body  
**EY pack unlocked:** 2026-10-01 — Johnny OK to enrich IAS 2 HTML from EY International GAAP® 2026 Ch23 (short paraphrase + cite chips; no large verbatim)
**EY FS Practical unlock (personal study):** 2026-10-01 — Johnny: pack = personal study notes (not commercial); has legal counsel — **do not skip** EY Ch23 Practical example FS series ×4 solely for copyright; prefer paraphrase + cite chips + teaching tables (numbers from source). Pack disclaimer on `index.html`.
**Official cite chip lock:** 2026-10-01 — Johnny: `[Standard] · para [ref]` e.g. `IAS 2 · para 3`, `IAS 2 · para 3(a)`, `IAS 2 · para B1`, `IAS 2 · para BC1`, `IAS 2 · para IN7`. **Not** `Official · §3` / `Official · IN…` / `Official · BC…`. Keep class `cite-official`. Cross-standard: `IAS 16 · para 8`, `IAS 23 · para 4(b)`; bare `IFRS 13` when no para.  
**EY cite chip label lock:** 2026-10-01 — Johnny: chips use **`EY iGAAP 2026 Ch23`** (not `EY International GAAP 2026`); path e.g. `EY iGAAP 2026 Ch23 · section 2.3` (**no `§` in any cite chip** — Official uses `para`, EY uses `section`). Full book name OK in prose/source paths.  
**Cite-tag typography lock:** 2026-10-01 — Johnny: all `.cite` / `.cite-house` = font **Calibri Light**, **not bold** (`font-weight: 300`; stack `"Calibri Light", Calibri, "Segoe UI", sans-serif`).  
**Cite chip placement lock (REFINED):** 2026-10-01 — Johnny: **split rule** (supersedes title/lead-only for everything). (1) **Illustration** `.box` / `.worked-strip` with `Illustration: N.M.k — …`: chips ONLY at end of title line; body prose only — no chips in/after body. (2) **Main teaching paras / list items** (non-Illustration): chips at the **back** of that para or bullet (end of the unit) — NOT on a fake bold lead-only line if that emptied the body. Non-Illustration callout boxes: chips at end of `box-body`. Keep EY = `EY iGAAP 2026 Ch23`; cite CSS = Calibri Light / weight 300.  
**Applies to:** `draft-v1-linked/ch0N.html` teaching `<article>` bodies; per-chapter `IAS2-CH0N-CONTENT-NOTES.md`  
**Does not apply to:** Concept Map HTML/CSS / iframes / chrome / footer — **set Map aside this pass**; visuals only after Johnny OK  
**Map / index:** `index.html` is the Map page — **do not rewrite Map body / iframe**.

**Skills:**  
- Body / study-pack content → [IFRS teaching body](sand-workflow:ifrs-teaching-body)  
- Post-edit QA gate (mandatory) → [IFRS teaching body QA](sand-workflow:ifrs-teaching-body-qa)  
- Concept Maps / visuals only → [IFRS visual grammar](sand-workflow:ifrs-visual-grammar)  

**HARD Illus locks (canonical in skills — if this METHOD drifts, skills win):** ALL Illus = worked-strip peer grids; peers all neutral (no ok/warn); densify quantitative (≤5 bullets OR ≲350 chars = FAIL densify even if structure PASS); title essence (no bare Official:/firm:/IFRS N: leads); hyperlink review after structure/id change. See skill logic review `SKILL-LOGIC-REVIEW-2026-10-01.md`.

---

## Research essence (Johnny 2026-10-01)

**Consolidate first:** pull **all** Official examples/illustrations **and** all pack Big4 named examples / FAQ-with-body / worked plates into the chapter so the learner does **not** need separate PDFs for one standard. Detail-first; thin teaching is wrong this phase. Multi-firm (DTT + PwC + EY + KPMG), not PwC FAQ-only — after Big4 completeness pre-flight. NOTES-only leftovers = gaps unless body missing, copyright FS-block, or Johnny deferred.


## Big4 completeness pre-flight (Johnny HARD — 2026-10-01)

**Rule:** Never wait for Johnny to name a missing Big4. Before any IAS 2 write/enrich, inventory **PwC + DTT + EY + KPMG + Official**. METHOD must list each firm **path** or explicit **`not on disk`**. Missing firm after scan without Johnny confirm = **Blocking**. “No X invent” lines that mean a firm was **skipped** while its manual is on disk = **FAIL** (QA section I).

**Three-layer source model:** (1) **Official Standard** (IFRS/IAS + BC/IE as applicable); (2) **Big 4 accounting manual / MOA** as the **primary firm interpretation** (PwC MOA, DTT MOA/iGAAP, EY International GAAP, KPMG Insights into IFRS); and (3) **Big 4 technical reference** as a **supplement to layer 2** that reviews / aligns firm interpretation, **not a parallel primary track equal to the MOA/manual**. Scan all available layers; use layer 3 to densify/confirm layer-2 interpretation. A layer-2 firm PDF on disk with an unscanned manual/MOA is **Blocking**.

### Two-way completeness cross-reference (HARD — before claiming this standard pack complete)

The site ↔ firm table below is orientation only, not completion evidence. METHOD/NOTES must contain both non-empty locator-level crosswalks: **`Crosswalk A — Official → Big4`** (every material Official para/BC/IE mapped to each available firm’s MOA/manual and technical reference, or an explicit gap) and **`Crosswalk B — Big4 → Official`** (every named Example, FAQ-with-body, illustration/worked plate, and firm view mapped back to Official para(s)/BC/IE, or an explicit orphan-firm-plate gap). Never invent an Official link. A one-way or partial cross-reference is a QA FAIL; layer 3 remains a supplement to layer 2, not a substitute.

**Inventories on disk (2026-10-01):** `draft-v1-linked/IAS2-XREF-OFFICIAL-TO-BIG4-2026-10-01.md`, `IAS2-XREF-BIG4-TO-OFFICIAL-2026-10-01.md`, `IAS2-XREF-SUMMARY-2026-10-01.md` (+ copies under `/workspace/ias2-content-extract/`). Status: **built, GAP-honest, NOT pack-complete** until SUMMARY GAPs cleared/accepted.

### Current IAS 2 status (pre-flight 2026-10-01 Asia/Shanghai)

| Firm | Work | On disk? | Path | Extract / inventory | Pack cite status |
|------|------|----------|------|---------------------|------------------|
| **Official** | HKAS 2 (=IAS 2 on site) | **Yes** | `inputs/hkas/hkas-2-inventories.pdf` (+ symlink `inputs/ias-2/official-hkas-2-inventories.pdf`) | `ias2-content-extract/hkas2-extract.txt` | Cited pack-wide (`cite-official`) |
| **PwC** | MOA 2020 **Ch25** Inventories | **Yes** | `inputs/pwc-2020-moa/chapters/25-ias2-inventories.pdf` (+ symlink `inputs/ias-2/pwc-2020-moa-25-ias2-inventories.pdf`) | `ias2-content-extract/pwc-ias2-extract.txt` | FAQ-with-body set extracted & cited (`cite-pwc`) |
| **DTT** | **A11** 2022 Inventories | **Yes** | `inputs/dtt-moa-2022-june21/dtt-2022-a11.pdf` (+ symlink `inputs/ias-2/dtt-2022-a11-inventories.pdf`) | `ias2-content-extract/dtt-a11-extract.txt` | Named examples extracted & cited (`cite-dtt`) |
| **EY** | IGAAP 2026 **Ch23** Inventories | **Yes** | `inputs/ey-international-gaap-2026/International-GAAP-2026-part1.pdf` (Ch23 book pp ~1692–1723); part2 also on disk | `ias2-content-extract/ey-ch23-inventories-raw.txt` + `EY-IGAAP-2026-IAS2-HITS.md` | Teaching-critical Scope/broker/forward cited (`cite-ey`); FS Practical examples ×4 **CLOSED** 2026-10-01 (personal-study unlock — paraphrase + cite) |
| **KPMG** | Insights **2019/20** Part1 **· 3.8** Inventories | **Yes** | `inputs/kpmg-2019-2020/part1-non-fi.pdf` | Inventory `IAS2-KPMG-3.8-INVENTORY-2026-10-01.md`; enrich + unfreeze changelogs; durable `refs/ias-2/extracts/kpmg-3.8-extract.txt` (+ copy under `ias2-content-extract/`) | Named Ex 1–17 + tables/sections unfrozen (`cite-kpmg`) |

**Documents-synced refs:** laptop `LAPTOP-MODGPP0C` (`2a06a250-…`) was **disconnected** at pre-flight — box `inputs/` is source of truth; Documents copy of METHOD/NOTES/HTML still pending sync.

**Remaining gaps (not “firm missing”):** (1) optional `inputs/ias-2/` symlinks for EY Ch23 / KPMG 3.8 (Official/PwC/DTT already symlinked); (2) ~~EY FS Practical examples~~ **CLOSED** 2026-10-01 — see `IAS2-EY-FS-UNLOCK-2026-10-01.md`; (3) Documents sync pending laptop; (4) optional Official→EY `_(map)_` densify (hygiene only; named-plate Crosswalk B design GAP cleared). BC chips + DTT 2.1-4/2.1-5 + KPMG 3.8.215 **closed** 2026-10-01 — see `IAS2-XREF-GAP-CLEAR-2026-10-01.md`. *(Hygiene 2026-10-01: durable KPMG extract persisted; XREF inventories built; DISTRIBUTION + content-audit stale “no EY/KPMG” lines cleaned.)*

Full audit: `/workspace/ias2-content-extract/IAS2-BIG4-COMPLETE-PREFLIGHT-2026-10-01.md`.

## Phase lock (Johnny 2026-09-30)

1. **Integrate Official IAS 2 + Big4 into one study pack first** (detail learning). Simplify later — do **not** thin the pack in this phase.
2. Concept Map may **start** the page, but **set Map aside** this pass: update **all chapter teaching bodies** first; **no iframe / visual / cache-bust edits**.
3. **Quote-heavy is OK now** — prefer Official `<q>` extracts + Big4 support over paraphrase.
4. **Decision strips / trees are OK** if **no invented facts** — every gate cites Official or Big4.
5. **Include ALL Official examples/illustrations + Big4 examples** that belong to the chapter topic; wrap each in a **line box** using existing `.box` / `.worked-strip` patterns (title e.g. `Illustration: N.M.k — …`; chips e.g. `IAS 2 · para 16`, `DTT iGAAP 2022 A11 · 3.2.3.3-1`, `PwC MOA 2020 Ch25 · FAQ 25.22.1`). Reproduce tables / key figures faithfully with cites — **not invented numbers**. Do **not** leave examples “thin” or NOTES-only.
6. **Official IAS 2 has limited numbered IE series** (unlike IFRS 18). Still include every Official illustration that exists: §16 exclusion list examples, IN/BC LIFO narrative, harvest deemed-cost §20, any Illustrative Examples in the Official PDF. Cite chips as `IAS 2 · para …` / `IAS 2 · para IN…` / `IAS 2 · para BC…` (not `Official · §…`).

---

## Format rules (mandatory)

1. **Bold key points** — every teaching key idea wrapped in `<strong>…</strong>` (section lead sentences, bullet heads, matrix axis labels that carry the teaching point).
2. **Layers of bullet points** — nested `<ul>` / `<ol>` for **super detail** (not brief). Under each teaching set, expand with:
   - **Official** extract (para / IN / BC) in `<q>…</q>` + cite chip (`IAS 2 · para …`)
   - **Big4** extract (DTT iGAAP 2022 A11; PwC MOA 2020 Ch25 / FAQ) in `<q>…</q>` or short firm paraphrase with cite chip
3. **Tables / matrices — not mandatory; use when multi-column helps**
   - Prefer a table when the content naturally has **more than 2 columns** (comparison, multi-axis, carve-out matrix, firm alignment next to Official).
   - Do **not** force every section into a table. Linear teaching (objective, pitfall, handoff) can stay nested bullets.
   - **Inside table cells**, nested `<ul>` / `<ol>` bullets are OK and **preferred** for detail.
4. **Big4 dedupe** — if several firms say the **same** thing, merge into **one** row/bullet with multiple cite chips (e.g. DTT · PwC). Keep distinct firm views in **separate** bullets/rows when they differ (label “DTT only” / “PwC only” as needed).
5. **Line-boxed examples** — for each chapter-relevant Official illustration and Big4 named example / FAQ-with-body (DTT, PwC, EY as packed — not PwC FAQ only):
   - **ALL** Illustrations = `.worked-strip` (title + `.worked-strip-grid` of **neutral** `.box` peers). ~~single `.box` when one plate is enough~~ — SUPERSEDED; short conceptual still uses worked-strip (see skills).
   - **Title = `Illustration: N.M.k — [Teaching Title]`** — `N.M` = parent section (e.g. 3.2); `k` resets per section and increments for each example `.box` / `.worked-strip` in order (e.g. `Illustration: 3.2.1 — Access road / present location and condition`). Firm + FAQ/para ids go in **cite chips** only — never in the title string. Nested strip labels (`Facts` / `Principal`) are not numbered.
   - **List / bullet bold titles ≠ cite strings** — bold lead = scan landmark (who/what in Official wording). Chips alone carry `IAS 2 · para …` / firm. Never bold `Official §N`, `IAS 2 · para N`, or `Big4 / Firm` as the title; do not invent labels.
   - Faithful wording / figures from the source (EY: short paraphrase only). Cite chips: **Illustration** → on title only (not inside `box-body`); **teaching paras/lis** → at **end of the unit** (not fake bold-lead-only hoist).
6. **Decision strip** — optional Start → Gate → Output (or tree) for judgement paths; **every step cited**; remove invented entity patterns.
7. **Visuals** — do **not** rewrite Concept Map HTML/CSS / iframe `?v=` in a content pass. Body-only. Suggest visual adjustments in the chapter NOTES only; implement only after Johnny OK.
8. **Cite-chip sections (Official + EY + typography + placement locks)** — Official chips: `IAS 2 · para 9`, `IAS 2 · para 3(a)`, `IAS 2 · para IN7`, `IAS 2 · para BC1`, `IAS 2 · para 25 fn`. **Not** `Official · §9`. Cross-standard: `IAS 16 · para 8`, `IAS 23 · para 4(b)`; bare `IFRS 13` when no para. EY chips: **`EY iGAAP 2026 Ch23 · …`** (not `International GAAP`). Other firm chips unchanged (`DTT iGAAP 2022 A11 · 3.2.3.3-1`, `PwC MOA 2020 Ch25 · 25.22` / FAQ id). Keep colour classes. Include `fn` inside the tag when applicable. Typography: all chips Calibri Light, `font-weight: 300` (not bold). **Placement (split):** Illustration `.box` / `.worked-strip` → chips on title only, body prose only; main teaching paras/lis → chips at **end of unit** (undo bold-lead over-hoist); non-Illustration callouts → end of `box-body`.
9. **Anchors** — Preserve `#s-N-…` ids that Map / visual chips deep-link to (including `#s-3-ex-b`, `#s-3-ex-c`, `#s-4-ex-a`, `#s-4-ex-d`).
10. **Site labels** — **IAS 2 / IFRS** only (no HKAS dual code on UI). Official HKAS 2 text is treated as IAS 2 on site.

---

## Content rules (substance)

| Rule | Detail |
|------|--------|
| **Quote Official + Big4 (+ EY)** | Official PRIMARY: `inputs/hkas/hkas-2-inventories.pdf` (= IAS 2 on site; symlink under `inputs/ias-2/`). Firms in pack: **DTT** 2022 A11 Inventories; **PwC** MOA 2020 Ch25; **EY** International GAAP® 2026 Ch23 Inventories (`inputs/ey-international-gaap-2026/`); **KPMG** Insights into IFRS 2019/20 Part 1 · 3.8 Inventories (`inputs/kpmg-2019-2020/part1-non-fi.pdf`). EY/KPMG: short paraphrases + cite chips only — **no large verbatim** blocks. **IAS 2 personal-study unlock (2026-10-01):** do **not** refuse EY Ch23 Practical FS examples solely for copyright when Johnny has locked personal study + counsel; still prefer paraphrase + cite (tables OK for source numbers). **No invent outside packed sources.** |
| **Official quotes primary** | Prefer short `<q>` extracts + cite chips over free rewrite. Firms support / align; do not replace Official. |
| **No invented examples** | No entity fact patterns not in Official §§/IN/BC or firm materials. Teaching cues = firm quote + Official aim OK. Decision strips cite gates only. Preserve existing worked strips if they match Standard/Big4 arithmetic; upgrade titles/cites; replace invented-looking patterns. |
| **Examples complete** | Every Official illustration + **all pack firms’** named examples / FAQ-with-body (DTT, PwC, EY short boxes) that belong to the chapter appear as line boxes — not NOTES-only, not PwC-FAQ-only densify. Thin/missing FAQ body → NOTES gap, do not invent. EY = short paraphrase + cite chips, no large verbatim. |
| **Teaching spine** | Organising idea: lower of cost and NRV (§9); Cost∥NRV peers; LIFO banned (IN13/BC + §25 by omission). Ch2 Recognition stays **light**. Ch3 = cost build-up + formulas; Ch4 = subsequent / NRV / write-down / capped reversal. Keep Initial ≠ Subsequent. Do not renumber chapters. |
| **Anchors** | Preserve `#s-N-…` Map deep-links. |
| **Leave iframe / visuals alone** | No cache-bust or copy change in visuals unless Johnny OK’d a visual pass. |
| **Site labels** | IAS 2 / IFRS only (no HKAS dual codes on UI). |
| **Do not split for split’s sake** | Keep existing section grain unless teaching logic truly requires a split. |

---

## Per-chapter workflow

0. **Big4 completeness pre-flight (HARD)** — confirm PwC + DTT + EY + KPMG + Official each listed above with path or `not on disk` before write/enrich; never skip a firm until Johnny names it.
1. Inventory sources in NOTES `(a)` (paths under `inputs/hkas/`, `inputs/dtt-moa-2022-june21/`, `inputs/pwc-2020-moa/chapters/`, `inputs/ey-international-gaap-2026/`, `inputs/kpmg-2019-2020/`) — list Official §§/IN/BC illustrations + **every on-disk firm’s** pieces that belong to the chapter.
2. Gap prior body in NOTES `(b)` — missing quotes, thin examples, invented patterns, missing firm section chips, **and** missing named examples from every pack firm (not only PwC FAQ backlog; not “skip KPMG/EY until asked”).
3. Backup `ch0N.html` under `/workspace/ias2-content-extract/` with timestamp before edit.
4. Rewrite **body only** to format rules; keep chrome, Concept Map fieldset/iframe, key-terms (unless cite chips broken), footer-nav.
5. Record boxes added, matrices kept/added, left-outs, backup paths in NOTES `(c)–(e)`; open questions / honest gaps in `(f)`.
6. Fold any Johnny format steer into **this METHOD** and the **IFRS teaching body** skill (principle only — no chapter dump).

---

## Site chapter ↔ Official / firm map

| Site | Official | DTT iGAAP 2022 A11 | PwC MOA 2020 Ch25 | EY iGAAP 2026 Ch23 | KPMG Insights 2019/20 · Part 1 · 3.8 |
|------|----------|--------------|------------------|---------------------|
| Ch1 Scope | §2–§8, §20 tip, IN6–IN9; BC6–BC8 | 2 Scope; pipeline fill 2.1-2; crypto 2.1-3; fulfilment 2.3 | 25.3–25.8; FAQ 25.8.1; spare parts FAQ 25.10.1 | §2.3 Scope / broker; §2.3.1 practical (emission, green certs, crypto) | 3.8.10–80; Ex 1–3B; samples/catalogues 3.8.50–60; emissions 3.8.73 |
| Ch2 Recognition | §6, §8 (light); expense exits → Ch5 | pipeline / inventory definition cues | 25.9–25.14; FAQ 25.10.1; consignment FAQ 25.46.x | §2.3.1.H–I consignment / returns (light cues) | 3.8.90–100 recognition/consignment (light cites) |
| Ch3 Initial measurement | §10–27, §17–18, §20–22; IN13; BC9–BC20 | 3.2 cost; discounts/rebates; normal capacity OH; joint/by-product; retail; FIFO/WA | 25.15–25.33; FAQs 25.19.x, 25.21.1, 25.22.1, 25.25.x, 25.32.1 | §3.1 cost; §3.1.3.E forward contracts (IFRS 9 edge) | 3.8.120–320; Ex 4A–8; ROU/ST lease; interruptions; std-cost var; base stock |
| Ch4 Subsequent measurement | §9, §6–7, §28–33; IN15 | 3.3 NRV; post-period; firm contracts; materials; reversals; costs to sell | 25.34–25.41; FAQs 25.8.1, 25.36.1, 25.39.1, 25.40.1 | §3.3 NRV | 3.8.330–390; Ex 9–16 intended use / FX NRV / firm+derivatives |
| Ch5 Derecognition | §34–35; IN14 | 3.4 Recognition as expense | 25.42–25.46; FAQ 25.42.1 | §5 Recognition in P&L | 3.8.400 Ex 17 reversal disclosure (presentation) |
| Ch6 Disclosure | §36–39; IN16–IN17 | 4.2 Disclosure | 25.47–25.51 | §6 Disclosure (+ crypto extras) | 3.8.400 presentation & disclosures |

---

## Ch1–Ch6 checklist (quick)

- [ ] **Big4 pre-flight** — PwC + DTT + EY + KPMG + Official each path or `not on disk` in this METHOD; no skipped-firm invent lines
- [x] **Two-way completeness cross-reference** — both inventories exist (2026-10-01): `IAS2-XREF-OFFICIAL-TO-BIG4-2026-10-01.md` (Crosswalk A) + `IAS2-XREF-BIG4-TO-OFFICIAL-2026-10-01.md` (Crosswalk B) + `IAS2-XREF-SUMMARY-2026-10-01.md` under pack and `ias2-content-extract/`. Locator-level + GAP-honest. **GAPs remaining:** optional Official→EY `_(map)_` densify only (non-blocking). **EY Practical FS ×4 CLOSED** 2026-10-01 (personal-study unlock). Closed earlier same day: BC4–BC5 / BC21 / BC22–BC23 chips; DTT 2.1-4 / 2.1-5 Illus; KPMG 3.8.215. Crosswalk B design GAP for EY FS **cleared** — pack-complete claim may be asserted for named-plate inventory (optional `_(map)_` densify remains hygiene). **Re-sweep 2026-10-01:** `IAS2-COMPLETENESS-RESWEEP-2026-10-01.md` — crosswalk-complete **Y**; densify thin ×4 closed; Map parked.
- [ ] Lead of each section + each major bullet head is **bold**
- [ ] Nested bullets under each set with **Official** + **Big4** extracts (quote-heavy OK)
- [ ] **All** chapter-relevant Official + pack Big4 named examples / FAQ-with-body in `.box` / `.worked-strip` (multi-firm; titles `Illustration: N.M.k — …`; cite chips hold firm/FAQ ids)
- [ ] Table/matrix only where **>2 columns** helps (not forced); nested `<ul>` OK inside cells
- [ ] Decision strips (if any) cite every gate; no invented entity facts
- [ ] Same Big4 points merged (multi cite chips); distinct firm views kept separate
- [ ] No invented examples; **no invent outside packed sources** (Official/DTT/PwC/EY/KPMG Insights 2019/20 · Part 1 · 3.8); EY/KPMG = short paraphrase + cite chips (no large verbatim); box titles + list bold leads do not duplicate cite chips / § numbers
- [ ] Official cite chips = `IAS 2 · para …` (not `Official · §…`); EY chips = `EY iGAAP 2026 Ch23 · …`; include `fn` when applicable; other firm chips keep house + section/FAQ id; cite CSS = Calibri Light / weight 300; **split placement** — Illustration chips on title only; teaching paras/lis chips at end of unit
- [ ] Anchors preserved; iframe/visuals/Concept Map untouched
- [ ] NOTES updated with box IDs added; visual suggestions (if any) in NOTES only
- [ ] Ch2 stays light; Ch3 ≠ Ch4 (Initial ≠ Subsequent); LIFO ban cites IN13/BC


## Illustration peer-column HTML (Johnny lock 2026-10-01)

- Bullets in peer columns: `<div class="box-body"><ul>…</ul></div>` — **never** `<p class="box-body"><ul>`.
- Keep peer columns same typography (13px teaching override).
- Title chips: FULL firm+work+locator on title; strong title may sit on its own line so chips wrap as a group (no orphan chip).

## Illustration peer colour lock + densify (2026-10-01)

Johnny lock: **all Illustration peer columns neutral** — strip `.ok`/`.warn` from worked-strip peers (and Illustration-internal contrast / Illustration-root warn). Design owns CSS fills. Non-Illustration contrast-pairs may keep ok/warn. Peer body markup: always `div.box-body > ul`. See `ias2-content-extract/IAS2-ILLUS-NEUTRAL-DENSIFY-2026-10-01.md`.
