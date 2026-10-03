# CF 2018 — OPUS working memory

**Pack:** CF 2018 · `refs/cf-2018/draft-v1-linked/`
**Runner:** Claude Opus 5.5 high (Cursor CloudAgent, launched by Grok for Johnny)
**Brief:** `OPUS-REVIEW-BRIEF-CF-IFRS18-2026-10-02.md` + `OPUS-KEY-REITERATIONS-CF-IFRS18-2026-10-02.md`
**Skills read in full:** ifrs-teaching-body v2026.10.02 · ifrs-teaching-body-qa v2026.10.02 · ifrs-visual-grammar v2026.10.02-22 · `CHROME-MODULE-DESIGN-2026-10-02.md`
**Viewport:** desktop only (1440 wide). No mobile / iPad shots or passes.
**This launch:** CF 2018 only. IFRS 18 not started.

---

## Gate log

| Gate | Status | Date (HKT) | HTML changed? | Johnny approval |
|------|--------|------------|---------------|-----------------|
| 1 — Overall review | **DONE** | 2026-10-02 02:05 | **No** (review only) | **CONTINUE into Ch1** + decisions 1–6 (§5a) |
| 2 — Ch1 | **DONE** | 2026-10-02 02:20 | Yes — `ch01.html`, `assets/shared.css` (mini-flow kit), cache key + stamp on 13 pages | **"Go ahead Ch2"** (Ch2 only; same locks) |
| 3 — Ch2 | **DONE** | 2026-10-02 02:39 | Yes — `ch02.html` + `visuals/ch02-qualitative-characteristics.{html,css}` only | **"Continue Ch3 and realign Last update stamps now"** |
| 4 — Ch3 + stamp realign | **DONE** | 2026-10-02 02:50 | Yes — `ch03.html` body; `ch01.html` one cross-link (`#s-3-5` → `#s-3-4`); stamp-only line on all 13 pages | **"Continue Ch4"** (+ Grok invent/Illus nuance, §5e) |
| 5 — Ch4 | **DONE** | 2026-10-02 09:19 | Yes — `ch04.html` body; `visuals/ch04-elements.html` (one bar 4.2.1 → 4.1.2); pack stamp on all 13 pages | **Johnny decisions (§5e-bis) + "Continue Ch5 after flyer and Ch2 fix"** |
| 5b — Johnny decisions | **DONE** | 2026-10-02 09:36 | Yes — `references.html` (one flyer row + intro chip); `ch04.html` (3 flyer cites); `ch02.html` (materiality differ → table); stamp on all 13 pages | (folded into Ch5 continue) |
| 6 — Ch5 | **DONE** | 2026-10-02 09:44 | Yes — `ch05.html` body + key terms; `visuals/ch05-recognition-derecognition.{html,css}` (neutral leaves, CSS `?v=`); pack stamp on all 13 pages | **"Continue Ch6"** (Ch6 only; same locks) |
| 7 — Ch6 | **DONE** | 2026-10-02 10:01 | Yes — `ch06.html` body + key terms; `visuals/ch06-measurement.html` (entry/exit row, 6.9 badge, CSS `?v=`); pack stamp on all 13 pages | **"Continue Ch7"** (Ch7 only; same protocol) |
| 8 — Ch7 | **DONE** | 2026-10-02 11:18 | Yes — `ch07.html` body + key terms; `visuals/ch07-presentation-disclosure.{html,css}` (foot cue, OCI leaf, solid elbow, `?v=` aligned); pack stamp on all 13 pages | **EY attachment: A) protect/audit, B) Ch7 "typically" fix, C) continue Ch8** |
| 8b — EY audit + Ch7 fix | **DONE** | 2026-10-02 11:36 | Yes — `ch01.html` (EY 4.1.1 chip restored on the 1.3 bullet); `ch07.html` 7.0 OCI bullet ("typically" → 7.17/BC7.24 precision); pack stamp on all 13 pages | (folded into Ch8 continue) |
| 9 — Ch8 | **DONE** | 2026-10-02 11:42 | Yes — `ch08.html` body + key terms; `visuals/ch08-capital.{html,css}` (sourced cues, plate border, `?v=` aligned); pack stamp on all 13 pages | **"Continue Ch9"** (Ch9 only; EY Ch2 attached for EY cites) |
| 10 — Ch9 | **DONE** | 2026-10-02 12:19 | Yes — `ch09.html` body + key terms; `visuals/ch09-combined.{html,css}` (neutral leaves, cues removed, binding zone with PwC ∥ KPMG, 9.7 zone, `?v=` aligned); pack stamp on all 13 pages | **"KPMG author-meta removals in Ch9 are OK (confirmed). Continue Ch10."** |
| 11 — Ch10 | **DONE** | 2026-10-02 12:37 | Yes — `ch10.html` body + key terms; `visuals/ch10-carve.{html,css}` (neutral leaves, cues removed, preparation zone, both differs, `?v=` aligned); Ch3 3.5 links; pack stamp on all 13 pages | **"Ch10 KPMG author-meta OK → Continue Ch11 (body + Map together)."** |
| 12 — Ch11 | **DONE** | 2026-10-02 13:55 | Yes — `ch11.html` body + purpose line + key terms; `visuals/ch11-status.{html,css}` rebuilt (neutral leaves, IAS 8.12 step removed, cue bar removed, 3 differ blocks, `?v=` aligned); pack stamp on all 13 pages | **"Ch11 KPMG New Foundation 2018 flyer 4 chips OK — keep. Continue pack Map only (not consistency yet)."** |
| 13 — Pack Map | **DONE** | 2026-10-02 14:21 | Yes — `index.html` board (comment through `</main>`; chrome, disclaimer and footer untouched); `assets/map.css` rewritten (`?v=cf2018-pack-map-20261002`, index only); pack stamp on all 13 pages | **"Pack Map OK → Continue consistency pass (full CF pack)."** |
| 14 — Consistency | **DONE — awaiting Johnny "continue"** | 2026-10-02 14:40 | Yes — Ch1–Ch7 EY chips (rescan vs attached Ch02); visual comments Ch1–Ch11 + Ch5 class rename; reader text Ch3/Ch9/Ch10; Ch9 Map label + chip split; differ titles Ch2/Ch4/Ch5; `references.html` meta; visual cache keys Ch1/Ch3/Ch4/Ch5/Ch9; pack stamp on all 13 pages | _pending_ (IFRS 18 not started) |
| 15 — KEY CHANGES → Grok | not started | — | — | — |

Prior CloudAgent run was cancelled; this run treated Gate 1 as fresh. Pack unpacked from `cf-2018-draft-v1-linked.tgz` (89 entries) as delivered by Grok after local chrome/refs polish.

---

## 1. Shared-asset verification (HARD prerequisite) — PASS

Local layout mirrors the box: `refs/cf-2018/draft-v1-linked/` + `refs/_shared/{tokens,chrome,cite}.css` (copied unchanged from the attached shared files; not edited).

| Check | Result |
|-------|--------|
| `../../_shared/tokens.css` → `chrome.css` → `cite.css` → pack CSS, in that order | **PASS** on all 13 live pages (index, ch01–ch11, references) |
| One cache key pack-wide | **PASS** — `?v=cf2018-chrome-phase2-20261002b` on every stylesheet link |
| `chrome:start/end`, `footer-nav:start/end` exactly once per page | **PASS** (13/13) |
| Last update stamp identical, date + time + HKT | **PASS** — `Last update · 2026-10-02 01:39 HKT` on 13/13 |
| Disclaimer `Disclaimer — personal study pack.` immediately before `footer-nav` | **PASS** (13/13); never under title / Map |
| Tag row `Map · 1…11 · References`, correct `.tag.active`, no JS dependence | **PASS** (13/13) |
| References after last chapter (Ch11 → References; footer back to Status + Map) | **PASS** |
| Map chip-order lecture note ("Section chips follow…") | **absent — PASS** (but see related Map lecture line in §3) |
| Pack CSS forks shared tokens/cite | `assets/*.css` — **no fork**. `visuals/shared.css` (iframe embeds) still owns its own token + `--cite-*` copy — Phase 2 did not migrate visual embeds. **Report only; not forked by this run; do not edit shared CSS.** |

Minor chrome debt (not blocking; chrome is Grok-owned — report, do not fix in Opus run unless Johnny asks):
- Inline style on `scroll tags →` hint in `.chrome-bar-actions` on all 13 pages (design: no inline chrome styling). At 1440 all tags fit, so the hint is noise on desktop.
- `index.html`: `pack-disclaimer` + `footer-nav` sit **outside** `</main>` (design: inside main wrapper) → disclaimer renders full-bleed on the Map page only.
- `ch01.html` footer: `← Prev: Map` **and** mid `Map` → two Map links.
- `references.html`: shell uses `<main class="page">` not `page references-page`; Official intro shows a chip whose text is literally `cite-official`.

---

## 2. Automated audit summary (tool: `tools/cf_pack_audit.py`, read-only)

| QA item | Result |
|---------|--------|
| A1 house-only Big4 chips | **0** |
| A2 `§` in any chip | **0** (1,176 chips scanned) |
| A3 `Official ·` chips | **0**; Official = `CF 2018 · para …` (897) + `IAS 8` (7) + `IFRS 9` (2); 9 chips `CF 2018 · 2026 cover` (cover meta) |
| B all `Illustration:` inside `.worked-strip` | **37/37 PASS** |
| B neutral Illus peers | **PASS** (0 `.ok/.warn/.danger` on Illus peers) |
| C `<p class="box-body"><ul>` | **0** |
| D densify quantitative (≤5 li or <350 chars) | **0 thin** (min 818 chars / 8 li). Structure ≠ source check — see §3 H1/H2 |
| F broken `href`/`src`/`#id` (pages + visuals) | **0** |
| F plain `see N.M` unlinked | **0** |
| `.callout.differ` | **0 in pack** (needs per-chapter check against sources — not inventable) |
| `.mini-flow` | **0 in pack** |
| point-chips without cite | **0** |

Big4 short forms currently on chips (pre-alignment):
`DTT A2 2022 · …` (80) · `PwC MOA 2020 · …` (86, incl. `A2.x` for Appendix 2) · `EY IGAAP 2026 · Ch2 · section …` (23) · `EY IFRS Developments 169 · May 2020` (3) · `KPMG Insights 2019/20 · 1.2.x / Example N` (21) · `KPMG Combined/Carve 2022 · …` (52).

---

## 3. Review findings — by defect class (no HTML amended at Gate 1)

Severity: **H** = violates a HARD lock / no-invent; **M** = QA fail class but low risk; **L** = polish.

### H1 — Illustrations with agent-built fact patterns (no-invent risk)
Plates self-labelled `Cited teaching cue (not an Official numeric IE)` and not traceable to a source example:

| Illus | Cites | Finding |
|-------|-------|---------|
| 3.5.1 Going concern assumption | CF 3.9 · DTT 6.1 · PwC 1.57 | PwC 1.57 is a paragraph (GC basis), **not** an example |
| 4.4.1 Claim that fails liability → equity | CF 4.26–27, 4.63–65 · PwC 1.72 | PwC 1.72 is the equity-residual paragraph; "preferred share" facts are **not** in PwC |
| 4.5.1 Owner cash contribution vs inventory sale | CF 4.68–4.71 only | CF has no entity example here |
| 5.5.1 Not recognising an acquired resource | CF 5.19–22, 5.25(a), BC5.21 · PwC 1.77 | PwC 1.77 is the measurement-uncertainty paragraph |
| 6.6.1 Day-2 P&L from basis flip / deemed cost | CF 6.6, 6.48, 6.78, 6.80–81 only | CU100 / donated machine facts not in CF |
| 8.4.1 Three-way landing of the same CU15 | CF 8.5–8.10, 6.42 · DTT A2 11 | CU100→CU115, +10 % **not** in DTT/Official/PwC (verified by text search of attached PDFs) |

Same "cited teaching cue" facts also sit in the Ch4–Ch8 Decision strips (2 per chapter). Crosswalk B labels 3.5.1/4.4.1/5.5.1 as if PwC plates — misleading.
**Proposed handling (per chapter gate, Johnny to confirm):** keep all sourced CF/firm teaching text; demote the invented facts/numbers to section teaching (no Illus title), or replace with a real source plate where one exists (e.g. 8.4.1 ↔ PwC FAQ 1.93.1 sole-trader car C1,000/C1,200/C2,000, +10 % — real numbers, in the attached PDF).

### H2 — PwC CF-intro FAQ bodies are in the attached PDF but missing from the pack
Attached `01-conceptual-framework-intro.pdf` contains FAQ bodies (pp 13–18). Pack NOTES / Ch2 / Ch8 bodies say "title only / body not in pack" — **stale**.

| PwC FAQ | Topic (from PDF) | Likely home | Shape |
|---------|------------------|-------------|-------|
| 1.21.1 | Information needed for cash-flow prospects / stewardship | Ch1 §1.2/§1.4 | section (FAQ≠Illus unless facts) |
| 1.51.1 / 1.51.2 | Items generally material / not material | Ch2 §2.2 materiality | section list |
| 1.65.1 | Held shares controlled by another party (trustee A for B) | Ch4 asset/control | **Illus** (entity facts) |
| 1.66.1 / 1.66.2 | Costs incurred → asset? control of a resource? | Ch4 asset | check shape at chapter gate |
| 1.66.3 | Asset contributed by government (Entity E leisure park) | Ch4 | **Illus** (entity facts) |
| 1.73.1 | Recognition prohibited by a specific Standard | Ch5 / Ch11 status | section |
| 1.78.1 | Asset and liability approach | Ch4 income/expense | section |
| 1.93.1 | Two concepts of capital maintenance (car C1,000 → C2,000) | Ch8 | **Illus** (numeric) |

Only 1.93.1 is mentioned in HTML (Ch8, as "title only"). Crosswalk B has no PwC FAQ rows → Crosswalk B incomplete for PwC layer 2.

### H3 — Author meta / lecture copy in reader-visible HTML
- 19 Decision-strip titles end with `(cited tests only; no invented entity)` / `(prefer Official/Big4 facts; no invented entity numbers)`.
- h3 titles: `…relationships, not a decision path` (1.1), `…not a shopping list` (2.1), `…not a pipeline` (6.1, 7.1, 8.1), `Optional teaching prompts (not a CF procedure)` (1.9, 2.8, 3.8, 4.9, 5.8, 6.9, 7.7, 8.6), `thin see-also` (1.8, 5.7, 6.8), `(CF Board-guidance — keep short)` (7.5), `(write-once)` (9.3), `(firm application — CF gap)` (9.6), `What this chapter is NOT` (11.6), `(IAS 8 order is prescribed; do not invent…)` (11.7).
- Body leads: `Official PRIMARY = June 2026 CF PDF…` (ch03 ~l.49, ch11 ~l.46); input PDF path in 1.0 Scope; `Official examples (not invented):` (1.4); `Locked teaching label:` (1.4); `2010 Official PDF. Not in pack` (ch02/04/05/06/07); `FAQ bodies not in pack` (ch02); `orphan vs Official CF` leads ×9 (ch09/ch10); `CF drill` (ch04); `Site label note` mentioning HKICPA/HKFRS (ch11 l.64).
- Map: `phase-legend` line on index ("Visit after Elements… not a fifth process step. Chapter order, not a preparer runbook.") = reader lecture on the board; Ch7 visual "not a pipeline"; Ch10 visual band labels "Illus jump", "See also (dashed — secondary)", "PwC A2 / KPMG … vocabulary — not Official CF wording".

### H4 — Title essence: source-as-lead (~74 bold leads pack-wide)
e.g. `DTT alignment.`, `PwC alignment.`, `PwC restatement.`, `EY / KPMG alignment`, `Limitations (EY teaching hook)`, `Official derecognition.`, `DTT 2018-vs-2010.`, `Official status.`, `Orphan vs Official CF:`. Per chapter: ch01 16 · ch02 6 · ch03 7 · ch04 6 · ch05 6 · ch06 5 · ch07 2 · ch08 3 · ch09 8 · ch10 11 · ch11 4. Fix = substance lead + chip at end; often merges with H5.

### H5 — Multi-firm duplication (write-once opportunity)
Same Official point restated per firm (e.g. Ch1 objective + decision set restated in 1.0, 1.1, 1.2 and again in 1.9 prompts; "PwC restatement" / "EY / KPMG alignment" bullets that add no distinct view). Merge into one dense unit + chips for every supporting source; keep only distinct firm detail.

### M1 — "Gate" in reader-visible text (QA F4: word-bounded = fail)
ch04 table cell "recognition gates"; ch05 `.box-body` "Gates = relevance + FR"; ch05 trap "…as CF gates". (Grok's refs pass deliberately left these; QA lock says replace with Test / Decision.)

### M2 — Decision strips (19) vs body mini-flow grammar
`Start | Test | Output/Conclusion` worked-strips with `.ok` (green) on the output peer. QA B automated check flags ok/warn inside `worked-strip-grid`; mini-flow grammar wants question → arms → one outcome each, never question + outcomes in one box (e.g. Ch1 "Test" box holds the question and "→ not primary"). Proposal: rebuild as neutral `.mini-flow` with branch kit where the source gives two outcomes; otherwise a cited section list.

### M3 — HK labels on site
ch08 l.124 "…the HKICPA / Board…"; ch11 l.64 site-label note (HKICPA / HKFRS). Site lock = Board / IFRS only.

### M4 — Cite short-form alignment (skill 2026.10.02 IAS 2 pattern) — **needs Johnny decision**
Proposed mechanical rename (no locator change):

| Now | Proposed (IAS 2 pattern) |
|-----|--------------------------|
| `DTT A2 2022 · 6.1` | `DTT iGAAP 2022 A2 · 6.1` |
| `EY IGAAP 2026 · Ch2 · section 7.1.2` | `EY iGAAP 2026 Ch2 · section 7.1.2` |
| `KPMG Insights 2019/20 · 1.2.130.20` / `· Example 2` | `KPMG Insights 2019/20 · Part 1 · 1.2 · 1.2.130.20` / `· Example 2` |
| `PwC MOA 2020 · 1.57` | `PwC MOA 2020 Ch1 · 1.57`? — PwC PDF is the **Introduction** chapter, paras `1.x`; "Ch1" is an inference → Johnny to choose `Ch1` vs `Intro` |
| `PwC MOA 2020 · A2.4` | `PwC MOA 2020 App2 · A2.4`? (Johnny to choose) |
| `KPMG Combined/Carve 2022 · …` / `EY IFRS Developments 169 · May 2020` | keep (layer-3 works; no IAS 2 analogue) |

Touches ~210 Big4 chips (DTT 80 + PwC 86 + EY IGAAP 23 + KPMG Insights 21) + `references.html` short-form column. Can be one scripted pass before Ch1 or applied chapter-by-chapter.

### M5 — Maps / visuals (visual grammar)
- Index Map: Objective ← QC stem points **right-to-left** ("make information useful for") — reverse walk vs L→R; `phase-legend` lecture line (H3); Ch9/Ch10 cells use inline `border-style:dashed` (dashed = see-also only) and jargon labels ("binding/fit Illus", "app of 3.13–3.14").
- Ch5, Ch6, Ch9, Ch10, Ch11 visuals: green Yes / red No leaves (correction at Gate 7: the Ch6 Map leaves were already neutral — no colour change needed); Ch9/Ch10 have **2 red** per board, neither a true scope stop → should be neutral/muted (≤1 red only for a hard stop; no green by default).
- CSS `order:` present in `map.css`, `ch02/ch04/ch05` visual CSS — check at each chapter gate that DOM order = reading order.
- Iframe `?v=` ≠ visual CSS `?v=` (ch03, ch07, ch08, ch09, ch10); ch01/02/04/05/06/11 visuals link CSS without `?v=`. Cache keys must move together when a Map is touched.
- Ch1 Map iframe shows ~180 px dead space under the board (iframe-fit — Build-owned; report only).

### M6 — Process / evidence (QA gate I)
- Ch1, Ch2, Ch4, Ch5, Ch7, Ch8 NOTES still say "KPMG/EY CF absent / not in pack" (METHOD corrected 2026-10-01) → stale skipped-firm lines = QA I fail; refresh at each chapter gate.
- Crosswalk B is locator-level for KPMG + PwC A2, but DTT / EY / PwC-intro rows are band-level ("A2 · 5 → 2.x", "QC / materiality blocks") → not locator-level per QA I.1. PwC FAQ rows missing (H2).
- EY Ch2 and KPMG Insights 1.2 PDFs **not attached to this run** → per skill "Source on disk but not attached": keep their existing text/chips unchanged; add no new EY/KPMG Insights substance; do not attribute new reasoning to them. DTT A2, PwC intro + Appendix 2, Official, KPMG 2018-04 flyer **are** attached.

### L — Layout polish
- Ch9/Ch10 4-peer Illus grids wrap 3 + 1 at 1440 (Conclusion stranded on row 2); stray trailing `·` in 9.5.1 Conclusion.
- Ch1 1.8 is a heading + one see-also with no cite chip.

---

## 4. Page-by-page short notes

| Page | Notes |
|------|-------|
| `index.html` Map | Story sound (Status wraps; Objective∥QC; RE contains Elements; Recognise → Measure → Present; Capital off Measure). Fix: R→L Objective/QC stem; remove `phase-legend` lecture; Ch9/10 dashed inline cells + jargon; disclaimer outside main. Pack Map enhance is the gate **after** Ch11. **Gate 13:** stem, legend, inline cells/jargon and status pills fixed (§5n); disclaimer placement left to Grok. |
| ch01 Objective & users | Map strong (relationship scene, decisions × assessments, accrual∥cash). Body: 16 source leads; objective restated 4×; 2 Decision strips (meta titles, green output); 1.4 meta leads; 1.8 empty see-also; 1.9 prompts duplicate body; PwC FAQ 1.21.1 body available; NOTES stale; no Illus (CF Ch1 has no example — OK unless FAQ 1.21.1 has entity facts: it does not). |
| ch02 Qualitative | 3 Decision strips (meta); "2010 Official PDF. Not in pack" + "FAQ bodies not in pack" in body; PwC FAQ 1.51.1/1.51.2 to add; `order:` in visual CSS; 2.1 lecture title. |
| ch03 Reporting entity | Illus 3.5.1 (H1), 3.5.2 KPMG Ex 1 (sourced); "Official PRIMARY" lead; 2 Decision strips. |
| ch04 Elements | Illus 4.4.1, 4.5.1 (H1); 4.6.1 KPMG Ex 2 (sourced); "gates" in table; "CF drill"; PwC FAQ 1.65.1, 1.66.1–1.66.3, 1.78.1 to add; 2 Decision strips with invented facts. |
| ch05 Recognition | Illus 5.5.1 (H1); 2× "gate"; EY Dev 169 chips (layer 3, not attached → keep as is). |
| ch06 Measurement | Illus 6.6.1 (H1); 6.7.1 KPMG Ex 3 (sourced); Map green/red leaves; "write-once"/"thin see-also" meta. |
| ch07 Presentation | No Illus; 2 Decision strips; 7.5 "keep short" title; visual "not a pipeline". |
| ch08 Capital | Illus 8.4.1 invented CU15 → PwC FAQ 1.93.1 real plate available; "HKICPA / Board" line; FAQ "title only" now false. |
| ch09 Combined FS | 16 Illus, all sourced (KPMG Combined/Carve Ex 1B/1D/2A–2C/2E/3C–3H; PwC Exhibits A2.2–A2.5); 3+1 grid wrap; "orphan vs Official CF" leads; Map 2 red leaves. |
| ch10 Carve-out | 12 Illus, all sourced (KPMG Ex 1C/2D/4A–4H; PwC Exhibits A2.10/A2.15); 11 source leads; Map green/red + layout-meta labels. |
| ch11 Status | "Official PRIMARY" + HK site-label note; 2 Decision strips; 11.6/11.7 meta titles. |
| `references.html` | Shape OK (Full name \| short form; Official + Big4; derived-from note). Short forms follow pre-alignment chips (M4). Literal `cite-official` chip in intro. |
| styles | `assets/*` consume shared module (no fork). `visuals/shared.css` keeps its own tokens/cite vars (Phase 2 gap — report). |

---

## 5. Decisions needed from Johnny (before / at Ch1)

1. **Continue into Ch1?** (Gate 1 stop.)
2. **H1 invented plates:** demote to section teaching (drop invented facts/numbers) vs keep. Default if no answer: demote; replace with a real source plate where one exists (8.4.1 → PwC FAQ 1.93.1).
3. **H2 PwC FAQ bodies:** OK to add from the attached PwC intro PDF (paraphrase + cite; Illus only where entity facts)?
4. **M4 cite short-form alignment:** apply? `PwC MOA 2020 Ch1` vs `PwC MOA 2020 Intro`; `PwC MOA 2020 App2 · A2.x` vs current `PwC MOA 2020 · A2.x`. One scripted pass up-front, or per chapter?
5. **M2 Decision strips:** rebuild as neutral mini-flow (branch kit) where sources give two outcomes; otherwise cited list. OK?
6. **Chrome debt (§1 minor):** leave to Grok, or allow Opus to fix the index disclaimer/footer placement + Ch1 duplicate Map link?

## 5a. Johnny's decisions at Gate 1 (recorded 2026-10-02)

Johnny said **CONTINUE into Ch1** with:
1. **Clear invent plates** — remove made-up facts/numbers from Illus 3.5.1, 4.4.1, 4.5.1, 5.5.1, 6.6.1, 8.4.1 and the matching Decision-strip invent; keep sourced teaching text; swap in real source examples where available (e.g. PwC FAQ 1.93.1 for 8.4.1). → applies at Ch3, Ch4, Ch5, Ch6, Ch8 gates.
2. **Add PwC FAQ bodies** from the attached PwC intro PDF — paraphrase + cite chips; Illustrations only where they have real case facts. → Ch1 done (1.21.1); Ch2 1.51.x; Ch4 1.65.1, 1.66.x, 1.78.1; Ch5/Ch11 1.73.1; Ch8 1.93.1.
3. **Rebuild Decision strips** as neutral flow diagrams with labelled branches where sources give two outcomes; cited lists otherwise. No invent. → every chapter.
4. **Cite short-form rename (M4) — DO NOT do yet.** Ask Johnny before any global rename.
5. **Author-note cleanup + firm-name bullet merge** (write once + multi cite chips) as each chapter comes up; densify not thin; no invent.
6. **Desktop-only screenshots at each gate stop**, then STOP and ask to continue.
Not decided: §5 item 6 chrome debt → left to Grok (Ch1 duplicate Map link unchanged).

## 5b. Gate 2 — Ch1 (DONE 2026-10-02 02:20 HKT)

**Changed:** `ch01.html` body (ids `s-1-0`…`s-1-8`, `s-1-3-ex`…`s-1-6-ex` kept; `s-1-9` removed — no inbound links); `assets/shared.css` appended `.mini-flow` branch kit (tokens only; neutral; question → join → bar → labelled arms ≥76px → one outcome step each; DOM order = reading order). Pack-wide: cache key `…20261002b` → `cf2018-chrome-phase2-20261002c`; stamp → `Last update · 2026-10-02 02:20 HKT` (13/13). Map untouched.

| Decision | Ch1 result |
|----------|------------|
| 1 invent | Ch1 had no invented plate; removed "not invented" / "no invented entity" meta |
| 2 PwC FAQ | FAQ 1.21.1 body as section units (no case facts): 1.4 voting/influence bullet; 1.5 table rows (resources/claims, two types of change, return variability); 1.6 cash-flow box. Also PwC 1.18 other parties, 1.29 stewardship |
| 3 Decision strips | `#s-1-3-ex` primary user → `.mini-flow` Test → Yes / No (para 1.5 fn 4 → 1.5, 1.8 / 1.9–1.10, PwC 1.18). `#s-1-6-ex` accrual vs cash → neutral 2-box `.peer-row` (sources give complementary views, not two outcomes) |
| 4 rename | not done |
| 5 meta + merge | 16 source leads → 0; PDF path, "Cites stay", "Locked teaching label", "Official examples (not invented)", h3 lecture suffixes removed; 1.9 prompts removed (pure duplicate); duplicate table/rows/point-chip removed; EY 4.1.1 / KPMG 1.2.20 chips moved with the same objective content to 1.2; EY 4.1.2 chip moved with limitations to 1.7; DTT chip removed from the stewardship-meaning unit (DTT doesn't state it; BC1.41 does) |
| densify | added CF 1.1 aspect list, 1.3 return examples, fn 1–4, BC1.16 (a)–(c), BC1.19, BC1.35(a) replace-management example, BC1.36 holding decisions, CF 1.11 goal detail, 1.16, 1.18–1.19, 1.21 detail |

**QA:** audit rc 0; ch01 `gate`/`§`/HKICPA/invent = 0; firm-name bold leads 0; internal anchors OK (`#s-1-4`, `#s-1-5`, `#s-1-6`, `ch03.html#s-3-5`); every teaching `<p>`/`<li>` ends with a chip; 98 chips; plain `.contrast-pair` used (`.dense` clamps body to 3 lines — would hide densified text). Known audit false positive: "content between disclaimer and footer" (40-char backoff).
**Ch1 Map narration (unchanged, passes):** 1.3 primary users → rely on → 1.2 GPFS (objective inside) → provided by → Reporting entity; tailored-report route shown as missing; 3 decision columns; 1.5 and 1.4 spanning rows; 1.6 two lenses (accrual ∥ cash). ~180px dead space below board = iframe-fit (Build-owned, report only).

## 5c. Gate 3 — Ch2 (DONE 2026-10-02 02:39 HKT)

**Johnny's instruction:** "Go ahead Ch2" — Ch2 HTML + related visuals only; do NOT edit shared chrome / References tag row / other chapters; no cite rename; Ch1 Map untouched.
**Changed:** `ch02.html` (body + its own stamp + iframe `?v=`); `visuals/ch02-qualitative-characteristics.html/.css`. No `assets/*.css` change (mini-flow kit from Gate 2 reused; `.callout.differ` renders with base `.callout` — dedicated style is Phase 2 shared-chrome design, `CHROME-MODULE-DESIGN` §7). Also `tools/cf_crops.py` (sticky bar static for crops).
**Stamp drift (deliberate):** ch02 = `2026-10-02 02:39 HKT`; other 12 pages stay `02:20 HKT` because this gate forbids editing other pages. Realign pack-wide at the Consistency gate (or when Johnny allows). Pack cache key unchanged `…20261002c` on all 13.

| Decision | Ch2 result |
|----------|------------|
| invent | No invented plate in Ch2; removed "cited tests only" titles, "FAQ bodies not in pack", "2010 Official PDF. Not in pack", 2022-reprint meta |
| PwC FAQ | FAQ 1.51.1 (items often material regardless of size — full 14-item list) and FAQ 1.51.2 (immaterial items need not be reported, obscuring, no fixed monetary limits) as section units in 2.2 (no case facts → not Illus) |
| differ | `.callout.differ` (first in pack): materiality definition — Official 2.11 as amended Oct 2018 (BC2.20A) vs PwC 1.51 quoting pre-amendment "omitting it or misstating it could influence"; flagged, not reconciled |
| Decision strips | 3 strips → 4 neutral mini-flows where the source gives two outcomes (`#s-2-2-ex` materiality 2.11/FAQ; `#s-2-5-ex` 2.21 third step; `#s-2-5-tradeoff` 2.22; `#s-2-6-ex` 2.37) + prudence strip → plain contrast-pair `#s-2-3-ex` (BC2.37 cautious vs asymmetric — two concepts, not two outcomes) |
| firm leads | 4 source leads → 0; PwC 1.29–1.51 band chip (1.29 is stewardship) replaced by point chips 1.30–1.51; `PwC MOA 2020 · cost constraint` (no locator) → 1.50 |
| EY/KPMG | Same 4 chips before/after (EY section 5, 5.1.1; KPMG 1.2.30, 1.2.40), moved only with their own content; nothing new attributed |
| densify | see `CF-CH02-CONTENT-NOTES.md` Opus section (Official 2.2, 2.10, 2.14–2.18 examples, 2.24–2.43 detail; BC2.20–22, 32–48; PwC 1.44 IFRS 1) |
| Map | Upward "enhance" arrow (reverse walk) → downward "usefulness enhanced by"; materiality "could reasonably be expected to influence"; iframe `?v=` = visual CSS `?v=` `cf2018-ch02-map-20261002`; `order:` only in ≤720px media and equals DOM order (OK) |

**QA:** audit rc 0; ch02 gate/§/HKICPA/"not in pack"/firm leads = 0 ("invent" hit = "inventory"); all links resolve (`#s-2-2/4/5`, `ch04.html#s-4-8`, `ch05.html#s-5-5`, `ch06.html#s-6-5`); every teaching unit ends with a chip; 132 chips; no ok/warn in mini-flows. Ids `s-2-0`…`s-2-7`, `s-2-2-ex`, `s-2-3-ex`, `s-2-6-ex` kept; `s-2-8` removed (no inbound links).
**Ch2 Map narration:** 2.1 board → 2.5 Fundamental tier: 2.2 Relevance (predictive / confirmatory; materiality) + 2.3 Faithful representation (complete / neutral / free from error; prudence / measurement uncertainty) → spanning bars: trade-off, 2.4 2018 reinstatement → stem down "usefulness enhanced by" → 2.6 four enhancers L→R → 2.7 Cost rail spans the whole stack on the right. ~170px dead space below board = iframe-fit (Build-owned).

## 5d. Gate 4 — Ch3 + pack stamp realign (DONE 2026-10-02 02:50 HKT)

**Johnny's instruction:** "Continue Ch3 and realign Last update stamps now". Two tasks: (A) one pack-level Last update stamp on all CF 2018 pages; (B) Ch3 content only, same locks as Ch1/Ch2.
**Stamp (A):** all 13 pages (index, ch01–ch11, references) now read `Last update · 2026-10-02 02:50 HKT` (`data-last-update="2026-10-02T02:50:00+08:00"`). This resolves the Gate 3 drift (ch02 at 02:39, others at 02:20). The commit changes only the stamp line (13 insertions, 13 deletions). `_archive-index-stub.html` has no chrome or stamp and is unchanged. The cache key stays `cf2018-chrome-phase2-20261002c` because no CSS changed.
**Changed (B):** `ch03.html` body and key terms. `ch01.html` gets one cross-link fix forced by the renumbering. Ch3 Map, visual CSS, shared chrome and References are untouched.

| Decision | Ch3 result |
|----------|------------|
| invent | Illustration 3.5.1 (`#s-3-5-gc`, teaching-cue facts) removed. PwC 1.57 is plain text, now the 3.4 lead plus the `#s-3-4-ex` mini-flow |
| author meta | "Official PRIMARY", 2010 gap, 2022 reprint and `2026 cover` chip removed; "DTT teaching hook" and "DTT / 2010" leads rewritten to substance |
| numbering | Body renumbered to the existing Map and index numbering (3.3 perspective · 3.4 going concern · 3.5 reporting entity · 3.6 consolidated/unconsolidated · 3.7 combined). The index needs no edit. Fixed `ch01.html` link to `ch03.html#s-3-4` |
| Decision strips | 2 old strips replaced by `#s-3-3-ex` contrast-pair (BC3.10, two perspectives, not two outcomes) and 3 neutral mini-flows: `#s-3-4-ex` going concern, `#s-3-6-ex` consolidated vs unconsolidated, `#s-3-6-boundary` boundary (BC3.19 vs 3.14). Plus a 3.1 peer-row |
| Illus | KPMG Example 1 retitled to **3.4.1** (`#s-3-4-ex-liq`); body and chips unchanged, so its "KPMG view:" and "Related KPMG notes:" leads stay (locked text) |
| differ | None found in Ch3 |
| EY/KPMG | Same 2 EY and 5 KPMG chips before and after, moved only with their own content |
| densify | See the Opus section of `CF-CH03-CONTENT-NOTES.md` (3.1 fn7, 3.3 list with fn9, 3.4–3.7, BC3.4–BC3.25; PwC 1.52–1.61; DTT 6.1–6.2 point chips) |

**QA:**
- Audit rc 0. In ch03, gate, §, HKICPA, invent, "not in pack", "Official PRIMARY", firm leads and author meta all count 0, except the locked KPMG Illus lead.
- All anchors resolve: in-page, `ch02.html#s-2-0`, `ch09.html`, `ch10.html`, and inbound links from index, ch01, ch09, ch10 and the visuals.
- Every teaching unit ends with a chip. Ids `s-3-0`…`s-3-7` are present.

**Ch3 Map narration:**
- 3.0 Financial statements, then 3.2 Objective: dual assessment (net cash inflows and stewardship), three statements L→R, and the reporting-period axis (Preceding, This period, After period-end), with a forward-looking note.
- Then 3.3 Entity perspective ∥ 3.4 Going concern.
- Then the stem "are about" leads to 3.5 Reporting entity: consolidated org-chart plate | 3.6 consolidated/unconsolidated stack | "Harder boundary" aside.
- Then 3.7 Combined.
- About 130px of iframe-fit dead space sits below the board (Build-owned). No Map change was needed.

**For later gates:** `ch10.html` wording "Ch3 · 3.6 states the Official portion-of-entity possibility" (portion = CF 3.10, now Ch3 3.5). Revisit at the Ch10 gate.

## 5e. Gate 5 — Ch4 (DONE 2026-10-02 09:19 HKT)

**Johnny's instruction:** "Continue Ch4" — Chapter 4 only, same locks; no cross-chapter edits except inbound-link fixes forced by a Ch4 renumber (none needed); bump the pack stamp on all pages if content changes.

**LOCK — Grok invent / Illus nuance (Johnny, 2026-10-02; applies Ch4 onward):**
- A plain firm paragraph, or a FAQ without case facts, becomes teaching (+ Decision/Test/Assessment if the source gives binary outcomes), **not** an Illustration.
- A named Example (KPMG/DTT/etc.), or an entity FAQ with facts → conclusion, becomes an Illustration densified from source (skill chooser: "Entity FAQ with facts → conclusion path" = Illus).
- Call it "invent" **only** when facts, numbers or companies are not in Official or pack Big4. Pure restatement of Official is not invent.
- In KEY CHANGES, report wrong-shape Illus and true invent **separately**.
- Ch3 re-read under this lock: Illus 3.5.1 was **wrong shape** (PwC 1.57 is a plain paragraph). Its bullets mostly restated Official 3.9 — no fake company or CU — so "invent" was overstated in Gate 1 H1. Dropping it was still correct because of its shape.

**Stamp:** all 13 pages `Last update · 2026-10-02 09:19 HKT` (`2026-10-02T09:19:00+08:00`). Cache key unchanged (no CSS change). Ch4 iframe `?v=` → `cf2018-ch04-map-20261002` (Map HTML changed).

| Decision | Ch4 result |
|----------|------------|
| wrong shape (not invent) | Illus 4.5.1 owner contribution vs inventory sale (restated 4.70 / 5.5) → three-arm Assessment `#s-4-5-ex`; Decision strip OTM call (restated 4.17 / BC4.9(a)) → asset mini-flow `#s-4-2-ex` |
| true invent | Illus 4.4.1 "preferred share" fact pattern (PwC 1.72 is a plain paragraph; scenario not in any source) → equity mini-flow `#s-4-4-ex`; refund strip's "30-day cash-refund custom" → obligation `#s-4-3-ex` + past-events `#s-4-3-past` mini-flows; 4.8 "lease of equipment" cue → Official 4.60–4.62 examples |
| sourced Illus added | PwC FAQ 1.65.1, 1.66.1, 1.66.2, 1.66.3 (4.2.1–4.2.4) and FAQ 1.78.1 (4.5.1); Gate 1 had 1.78.1 as "section" — corrected to Illus (Entity G facts + C500,000) |
| named Example kept | KPMG Example 2 → Illus 4.7.1, moved into 4.7 (was after the 4.9 prompts); chips identical; only "Teaching cue:" meta lead → substance lead (same sentence) |
| differ | 3 `.callout.differ` in skill table form (Source \| Treatment + "Shown side by side and not reconciled."): existence uncertainty (Official vs PwC 1.65); FAQ asset-test wording (PwC FAQ 1.66.1/1.66.3 vs Official + DTT 8.1); income/expense "recognition criterion" label (PwC 1.78–1.79) |
| Decisions | 6 neutral mini-flows (asset; obligation; past events; equity; element Assessment ×3 arms; executory Assessment ×3 arms) + neutral contrast pairs `#s-4-0-ex`, linkers |
| densify | Official 4.6–4.62 lists in full; BC4.1–BC4.97 (2010 wording table, BC4.9 excluded items, testing BC4.19–22, rights/goodwill/identifiability BC4.28–39, control BC4.40–43, three views BC4.51–52, terminology BC4.56–58, counterparty right BC4.59–61, chain of events BC4.64–68, non-reciprocal BC4.69–70, contingent table BC4.71–73, unit of account BC4.74–77, executory BC4.78–87, equity BC4.89–92, BC4.93–97); PwC 1.62–1.81; DTT 7.1–7.4, 8.1. Words ~4.6k → ~9.2k; chips 178 → 336 |
| EY/KPMG | Same 2 EY + 3 KPMG chips before and after |
| Map | One bar renumbered 4.2.1 → 4.1.2 (shared A ∥ L group). Reading order unchanged |

**QA:** audit rc 0; ch04 author-meta [] ; gate, §, HKICPA, invent, "teaching cue", "組成", "dashed" = 0; firm leads 0 except "CF:" inside the locked KPMG Illus; no duplicate ids; all inbound links (index, ch02 `#s-4-8`, Ch4 visual) resolve; every teaching unit ends with a chip (the differ closing lines are exempt by skill); Illus peers neutral and chip-free in bodies; no ok/warn in mini-flows. Audit "C2 placement" heuristic flags the two bold-only lead paragraphs that introduce lists (chip at the end of the unit — OK).
**Ch4 Map narration:** 4.1 formula board L→R: 4.2 Asset − 4.3 Liability = 4.4 Equity, with 4.5 Income ∥ Expenses nested inside Equity, and the bar "owner contributions and distributions are not income or expenses". Under the A/L pair, shared bars 4.1.1 (past events; low probability) and 4.1.2 (expected flow removed from both). Then the "Applying the definitions" row: 4.6 Unit of account | 4.7 Executory contracts | 4.8 Substance. About 170px of iframe-fit dead space below (Build-owned).
**Raise with Johnny:** ~~KPMG flyer row~~ and ~~Ch2 materiality differ~~ — both resolved by Johnny's decisions, see §5e-bis.

## 5e-bis. Johnny's decisions after Gate 5 (DONE 2026-10-02 09:36 HKT)

1. **KPMG 2018-04 flyer — ADDED.** References row "KPMG — Conceptual Framework: The new foundation for IFRS (29 March 2018)" after Combined/Carve, plus the intro chip list. Chip short form **`KPMG New Foundation 2018 · p1` / `· p2`** (flyer page). It is the only new short form allowed this wave. Cited in Ch4: 4.2 bullet "Bundles of rights" (p2); 4.3 bullet "A new and untested concept" (p1, p2); 4.4 FICE out-of-scope callout sentence (p1). Ch5 must cite it where it uses practical ability → recognition, or control-based derecognition / retained rights (p2). Crosswalk B has a new flyer section. The flyer has no named Examples, so it never feeds an Illustration.
2. **Ch2 materiality differ — FIXED.** Now in the skill table (Source | Treatment: Official 2.11 + BC2.20A vs PwC 1.51 + FAQ 1.51.2), with the closing line "Shown side by side and not reconciled." The reconcile sentence ("Quote the Official wording; read the PwC quotation as …") was removed.
3. **Consistency gate (14) MUST re-sweep every `.callout.differ` pack-wide** (table form, closing line, no reconcile sentence, chips at the end of each cell) at the end of the wave — Johnny's instruction.
4. **Stamp:** bump on all 13 pages whenever the stamp is touched. Now `Last update · 2026-10-02 09:36 HKT` (`2026-10-02T09:36:00+08:00`).
5. **Screenshots:** `refs/cf-2018/opus-checkpoints/decisions-20261002/` — `ch02-differ-materiality-table.png`, `references-big4-flyer-row.png`, `references-chrome-stamp.png`, `ch04-flyer-{bundles-of-rights,practical-ability,fice-callout}.png`.
6. Commits a4a0f78 (flyer), b3d077e (Ch2 differ), 7b4cb1a (stamp).

## 5f. Gate 6 — Ch5 (DONE 2026-10-02 09:44 HKT)

**Johnny's instruction:** "Continue Ch5 after flyer and Ch2 fix" — same locks as Ch1–4; cite the flyer where Ch5 uses its points; STOP after Ch5 with KEY CHANGES and screenshots, then ask to continue to Ch6.
**Stamp:** all 13 pages `Last update · 2026-10-02 09:44 HKT` (`2026-10-02T09:44:00+08:00`). Cache key unchanged. Ch5 iframe and visual CSS `?v=cf2018-ch05-map-20261002`.

| Decision | Ch5 result |
|----------|------------|
| wrong shape (not invent) | Illus 5.5.1 (PwC 1.77 plain paragraph; facts restate 5.25(a)) → 5.25(a)–(c) list + 5.19 paragraph; 5.4 Decision strip (restates 5.17(b)) → Assessment `#s-5-4-ex` |
| true invent | 5.6 Decision strip "sells receivables + written put + retained credit exposure" (receivables / credit exposure not in source) → three-arm Assessment `#s-5-6-ex` using 5.29–5.32 only |
| sourced Illus added | PwC FAQ 1.73.1 (Entity F brand) → Illus 5.2.1 `#s-5-2-ex-brand` |
| differ | 2 tables: brand FAQ IAS 38 "reliably measured / probable flow" wording vs 2018 criteria (Official 5.7, BC5.19, BC5.21, BC5.11 \| PwC FAQ 1.73.1); derecognition approach (Official BC5.28–29 \| DTT 8.2 \| KPMG flyer p2 "control-based") |
| Decisions | 1 Decision `#s-5-2-ex` (recognise?) + 4 Assessments `#s-5-4-ex`, `#s-5-5-ex` (3 arms), `#s-5-6-ex` (3 arms), `#s-5-7-ex` (3 arms); contrasts `#s-5-0-ex`, `#s-5-3-ex` neutral, not `.dense` |
| author meta | site-home/cite meta, "not in pack", "2026 cover" chip, "Gates =", "Content-invented" asides, "does not invent an extra process spine", "(one-line)", "thin see-also", 5.8 prompts — all removed |
| densify | Official 5.1–5.33 lists in full; BC5.1–BC5.30 (concerns/response table BC5.15–22; control vs risks-and-rewards BC5.24; BC5.30); PwC 1.73–1.83; DTT 8, 8.1, 8.2; flyer p1, p2. Words 3.5k → 5.8k; chips 113 → 185 |
| flyer | 4 chips: 5.0 (p1), 5.4 practical ability (p2), 5.6 bundles/retained rights (p2), 5.6 differ KPMG row (p2) |
| EY/KPMG | Same 1 EY IGAAP + 1 EY Dev 169 + 1 KPMG Insights chip; Dev 169 callout moved from the removed 5.8 to 5.2 with identical text |
| Map | Leaves neutral (Gate 1 M5); no text or DOM change |

**QA:** audit rc 0 (only the known "between disclaimer and footer" false positive); gate, §, HKICPA, invent, "teaching cue", "not in pack", "2026 cover", firm leads = 0; no duplicate ids; inbound links index `#s-5-2/3/6`, ch02 `#s-5-5`, visual `#s-5-1…5-7` resolve; every teaching unit ends with a chip; Illus peers neutral and chip-free; no ok/warn in mini-flows; 2 differ tables with closing line.
**Ch5 Map narration:** 5.1 title bar → 5.2 Decision "meets an element definition?" (no → "Not that element" side leaf) → yes trunk → usefulness Decision with 5.4 Relevance + 5.5 Faithful representation peers, then the Cost constraint and 5.3 "2018: no probability threshold…" bars → yes / no forks to Recognise | Do not recognise → "later" stem → 5.6 Derecognition (retained + change aims; align / conflict cells) → 5.7 see-also bar. About 120px of iframe-fit dead space below (Build-owned).
**For later gates:** Consistency gate re-sweeps every differ (§5e-bis). Flyer p1 "granularity" and "Check your policies" points are not placed yet (Ch1 / Ch6 / Ch7 / Ch11 candidates).

## 5g. Gate 7 — Ch6 (DONE 2026-10-02 10:01 HKT)

**Johnny's instruction:** "Continue Ch6" — Chapter 6 only, same locks as Ch1–5; Ch10 wording debt about Ch3 section numbers only if Ch6 requires it (it did not — left for the Ch10 gate); STOP after Ch6 and ask to continue to Ch7.
**Stamp:** all 13 pages `Last update · 2026-10-02 10:01 HKT` (`2026-10-02T10:01:00+08:00`; 09:59 for the content commit, 10:01 after a one-line 6.6 wording fix). Cache key unchanged. Ch6 iframe and visual CSS `?v=cf2018-ch06-map-20261002`.

| Decision | Ch6 result |
|----------|------------|
| wrong shape (not invent) | none |
| true invent | 6.4 Decision strip "listed equity held for sale" (not in source; Official 6.55–6.56 names PPE, inventory, assets sold independently); 6.5 Decision strip "specialised right … near-equivalent current cost observable" (constructed facts); Illus 6.6.1 "CU100 / donated machine" (number + path) — all removed; taught by `#s-6-5-ex`, `#s-6-5-mu`, `#s-6-6-ex` with Official wording only |
| named Example kept | KPMG Insights Example 3 → Illus 6.7.1 `#s-6-ex-shareholder`, moved into the new 6.7 (equity) so the Ch10 carve visual `#s-6-7` link lands on it; chips unchanged; "CF 6.82" source lead → substance lead |
| differ | 1 table: is outcome uncertainty a factor in selecting a basis? (Official 6.58–6.62, BC6.43 \| PwC 1.86) |
| Decisions | Assessment `#s-6-5-ex` (Combined / Directly / Contract, 6.54–6.57); Decision `#s-6-5-mu` (No / Yes, 6.60); Decision `#s-6-6-ex` (market terms Yes / No, 6.78–6.82); contrast `#s-6-0-ex` neutral |
| structure | 6.7 is now equity measurement (6.87–6.90) + owner transactions; 6.8 more than one basis; 6.9 prompts → cash-flow-based measurement techniques (6.91–6.95). No inbound link to the old 6.9 prompts |
| author meta | "site home", "June 2026 CF PDF", "2010 not in pack", "2026 cover", "Read the visual…", "Matrix: … card-grid above", "Content-invented", "(one-line)", old DTT source-lead callout — all removed |
| densify | Official 6.1–6.95 + BC6.1–BC6.55; PwC 1.84–1.89, 1.94–1.99; DTT 1.2, 9, 9.1, 9.2–9.2.4; flyer p1. Words 4.3k → 7.2k; chips 141 → 226 |
| flyer | 1 chip: 6.0 "measurement a list of choices" (p1 granularity point now placed) |
| EY/KPMG | EY Figure 9-1 matrices, Table 6.1 notes text and EY narrative text unchanged; EY + KPMG Insights chip set identical to HEAD (flyer excluded). Official 6.23 income-received sentence put in its own note, not inside the EY-chipped note |
| Map | Leaves already neutral. Entry/exit row VIU and Fulfil "Entity path" → "Exit" (BC6.14; DTT 9.1 table). `mx-miss` note gets a 6.9 badge link. CSS `?v=` added to match iframe |

**QA:** audit rc 0 (known "between disclaimer and footer" false positive; C2 heuristic flags the `#s-6-6-ex` Test — false positive, the audit stops at the `, ` chip separator); gate, §, HKICPA, invent, "teaching cue", "not in pack", "2026 cover", firm leads = 0; no duplicate ids; inbound links index `#s-6-1/2/3/5`, ch02 `#s-6-5`, visual `#s-6-1…6-6, 6-8, 6-9`, ch10 visual `#s-6-7` resolve; every teaching unit ends with a chip (two key-term items without chips, as before); Illus peers neutral and chip-free; no ok/warn in mini-flows; 1 differ table with closing line.
**Ch6 Map narration:** Ch5 "recognised?" Yes → "then measure" → 6.1 board: 6.2 Historical cost ∥ 6.3 Current value (FV, VIU, Fulfilment, Current cost) → "neither family preferred" bar → 6.4 matrix (entry/exit, whose view, info cue) → 6.9 "not a third family" note → 6.5 four factor clusters + "weigh together" bar → 6.6 ∥ 6.8 leaves. No side leaf → "disclosure may still apply".
**For later gates:** Ch10 wording debt about Ch3 section numbers still open (Ch10 gate). Flyer "Check your policies" not placed yet (Ch1 / Ch11). PwC 1.90–1.93 (capital maintenance) → Ch8 gate.

## 5h. Gate 8 — Ch7 (DONE 2026-10-02 11:18 HKT)

**Johnny's instruction:** "Continue Ch7" — Chapter 7 only, same protocol (full teaching-body + visual-grammar + QA pass; densify; no invent; FAQ ≠ Illustration; wrong shape vs true invent separately; differ side by side; Decision/Test/Assessment; no § in chips; desktop only; pack stamp; no shared chrome or cite renames; Ch10 debt left unless Ch7 inbound links break — they did not). Grok-local advisory comments on earlier chapters may arrive later; not waited for.
**Stamp:** all 13 pages `Last update · 2026-10-02 11:18 HKT` (`2026-10-02T11:18:00+08:00`). Cache key unchanged. Ch7 iframe and visual CSS `?v=cf2018-ch07-map-20261002` (were `cf-ias2-parity-20261001` / `pres-opus1b`).

| Decision | Ch7 result |
|----------|------------|
| wrong shape (not invent) | none |
| true invent | 7.3 Decision strip "CU80 receivable + CU50 payable → net CU30" (numbers + counterparty); 7.4 Decision strip "Other income/(expense) nets FX + associate disposal gain + intangible impairment" (constructed facts) — both removed; taught by Decisions `#s-7-3-ex`, `#s-7-4-ex` with Official wording only |
| named Example | none in Ch7 sources → no Illustration |
| differ | 2 tables: how the statement of profit or loss is described (Official 7.16 \| PwC 1.107 "primary performance indicator" \| DTT 1.2 "primary measure" + 10.3 "primary source"); when OCI amounts are reclassified (Official 7.19 \| DTT 10.3 "more relevant than not reclassifying" \| PwC 1.108 "deferred through OCI") |
| Decisions | `#s-7-3-ex` (Separate / One unit), `#s-7-4-ex` (No / Yes), `#s-7-5-ex` (P&L / OCI — No / Yes), `#s-7-5-rc` (reclassify — Yes / No); contrasts `#s-7-0-ex`, `#s-7-5-who` neutral (were `.dense` ok/warn "trap" boxes) |
| structure | 7.0 … 7.6; 7.7 prompts removed (no inbound links). Body numbers already matched the Map |
| author meta | "site home / cites stay", "June 2026 CF PDF", "2010 not in pack", "2026 cover", "Read the visual…", "do not invent a numbered CF communication procedure", "(CF Board-guidance — keep short)", "Teaching paraphrase" / "CF teaching cue" headers, "(one-line)", chip-first DTT callouts — all removed |
| densify | Official 7.1–7.22 (+ fn11) and BC7.1–BC7.33 all taught; PwC 1.62, 1.69, 1.70, 1.100–1.108; DTT 1.2, 10–10.3; flyer p1. Words 2.6k → 3.3k (duplicates removed); chips 107 → 130 |
| cites | Vague `PwC MOA 2020 · presentation` chip (no locator) removed with its content-free bullet; PwC content now cited at 1.100–1.108. Not a short-form rename |
| flyer | 1 chip: 7.0 "presentation and disclosure a list of choices" (p1) |
| EY/KPMG | The one EY chip (`Ch2 · section 10`) and its bullet text unchanged (lead only → substance). The "typically" wording was fixed after the EY attachment (§5i Part B) |
| Map | Leaves already neutral. Foot cue (audit lecture cue) → substance; OCI leaf wording per 7.17; reclassification elbow dashed → solid; `?v=` aligned |

**QA:** audit rc 0 (known "between disclaimer and footer" false positive only; no Ch7 lecture cue; no C2 flag on Ch7); gate, §, HKICPA, invent, "teaching cue", "not in pack", "2026 cover", firm leads = 0; no duplicate ids; inbound links index `#s-7-2/3/4/6` and visual `#s-7-1…7-5` resolve; outbound `ch06.html#s-6-8` resolves; every teaching unit ends with a chip; no ok/warn in mini-flows; 2 differ tables with closing line.
**Ch7 Map narration:** Goal column — 7.1 Useful communication ⇄ balance ⇄ 7.1 Cost, foot cue → Tools column (equal, not steps) — 7.2 Objectives & principles; 7.3 Classification with nested income & expenses (Primary source → P&L; Exceptional → OCI; solid elbow OCI → P&L; 7.5 Reclassification card); 7.4 Aggregation with Face / Notes levels → What this shapes — 7.3 Grouping, 7.4 Detail level, 7.5 Performance home, IFRS 18 see-also (dashed). About 130px iframe-fit dead space below (Build-owned).
**For later gates:** Ch10 debt still open. Flyer "Check your policies" (p2) still unplaced (Ch1 / Ch11). The 7.0 "typically" wording was resolved in §5i.

## 5i. EY attachment — Part A audit + Part B Ch7 fix (DONE 2026-10-02 11:36 HKT)

**Johnny's instruction:** EY iGAAP 2026 Ch2 (pp. 46–106) now attached. Do not delete or weaken EY-cited teaching without verifying; restore any EY-supported teaching removed as "invent" / wrong shape; keep Official + EY side by side where they differ.
**Method:** compared every EY-chipped unit at baseline `5fc9478` with HEAD (`/tmp/ey/eyscan.py`), then checked each HEAD unit against the EY text.

| EY-risk item | Result |
|--------------|--------|
| Ch1 section 4.1.1 ×2 | The two units had been merged and one EY chip was dropped → **restored** on the 1.3 "expected returns" bullet |
| Ch1 section 4.1.2 | present, supported |
| Ch2 section 5; 5.1.1 | supported (history also DTT); 5.1.1 with BC2.20A |
| Ch3 section 6.2 ×2 | supported |
| Ch4 section 7; 7.1.2 | supported (history also DTT) |
| Ch5 section 8; EY Dev 169 | supported; Dev 169 unchanged |
| Ch6 section 9; Figure 9-1 notes + footnotes; 9.2.1–9.2.2 | supported |
| Ch7 section 10 | "typically" → fixed in Part B |
| Removed strips / Illus Ch1–Ch7 | none EY-supported — EY Ch2 has no named Examples, and none of the removed facts appear in it |

**Part B:** Ch7 7.0 bullet now follows 7.17 / BC7.24 ("only in exceptional circumstances may the Board … decide"). EY section 10.2.3.A states the same rule → EY chip kept, no differ.
**EY-only commentary for later gates (not added):** Ch1 tax / distribution uses outside the objective (IAS 1.30A); Ch2 EY prudence remark; Ch4 balance-sheet approach; Ch3/Ch9/Ch10 combined FS compliance + carve-out "How we see it"; Ch7 IFRS 18 OCI definition and B87 list.

## 5j. Gate 9 — Ch8 (DONE 2026-10-02 11:42 HKT)

**Johnny's instruction:** "C) Continue Ch8 — same full skill gate … use EY CF Chapter 2 for any EY-cited Ch8 points. Stop after Ch8."
**Stamp:** all 13 pages `Last update · 2026-10-02 11:42 HKT`. Cache key unchanged. Ch8 iframe + visual CSS `?v=cf2018-ch08-map-20261002` (were `cf-full-20261001` / `cap-8c`).

| Decision | Ch8 result |
|----------|------------|
| wrong shape (not invent) | Two Decision strips that only restated 8.7/8.8; duplicate concept / maintenance lists; `.dense` ok/warn contrasts; "Teaching cue" table row; Map "Cue" row |
| true invent | CU100 → CU115 inventory / +10% / CU110, CU5, CU10, CU15 in `#s-8-4-ex1`, `#s-8-4-ex2`, Illus 8.4.1 `#s-8-4-ex3` — removed |
| named Example / entity FAQ | PwC FAQ 1.93.1 sole trader → Illustration 8.4.1 at `#s-8-4-ex1` (Map link target kept) |
| differ | carried-forward origin (Official 2010 / 1989 · DTT 2001 · EY 1989); "relevance and reliability" in 8.9 (Official · DTT · EY drafting error) |
| Decisions / contrasts | `#s-8-1-dec` (Invested / Capacity); `#s-8-1-ex`, `#s-8-2-ex` neutral |
| EY | Old EY chip sat on "no preference" (EY does not say that) → "no preference" now DTT only; EY chips on the units EY restates (30, all verified) |
| structure | 8.0 … 8.5; 8.6 prompts removed (no inbound links) |
| densify | Official 8.1–8.10, BC8.1–BC8.4, BC0.16–BC0.17, BC6.6; PwC 1.90–1.93 + FAQ 1.93.1; DTT 11; EY 11, 11.1, 11.2. Words 2,642 → 2,548; chips 84 → 102 |
| Map | Legend, "Price changes" key, "Users mainly concerned with" row, 8.3 card, 8.4 link, 8.5 strip (drops "typically financial"), plate border, `?v=` |

**QA:** `/tmp/qa.py` clean (exemption widened to whole `.worked-strip` — Illustration content is chip-free by rule); audit known false positive only; no HKICPA / § / gate / invent; no duplicate ids; inbound `index #s-8-2` ×3 and Map links resolve; outbound `ch02#s-2-4`, `ch06#s-6-1`, `ch06#s-6-3`, `ch07#s-7-5` resolve.
**Ch8 Map narration:** 8.1 title → containment plate (users' needs select; most entities financial; no preference stated) around the Financial ∥ Physical lens matrix (what is capital, when is profit, price changes, measurement pairing, users mainly concerned with) → three consequence cards 8.2 maintenance → profit, 8.3 bases × concept → model, 8.4 adjustments vs income (→ Illustration 8.4.1) → dashed 8.5 strip. About 120px iframe-fit dead space below (pack-wide shared `iframe-fit.js`, as Ch7; Build-owned).

## 5k. Gate 10 — Ch9 (DONE 2026-10-02 12:19 HKT)

**Johnny's instruction:** "Continue Ch9 … Use [EY Ch2] to verify any EY cites in Ch9 … Stop after Ch9."
**Stamp:** all 13 pages `Last update · 2026-10-02 12:19 HKT` (12:17 bump, then re-bumped after a Map badge fix). Cache key unchanged. Ch9 iframe + visual CSS `?v=cf2018-ch09-map-20261002` (were `cf-gap3` / `cf-ch09-skill-clear-20261001`).

| Decision | Ch9 result |
|----------|------------|
| wrong shape (not invent) | Decision strip `#s-9-2-ex` → mini-flow; site-built tables / step rows in PwC Illus 9.5.7–9.5.10; 9.6 "five key steps" paraphrase ≠ PwC A2.14; prompts section; author meta (Map link, "Do not invent an Official CF flowchart", "orphan vs Official CF" ×4) |
| true invent | "not a substitute for required consolidated FS" chipped to 3.15–3.18; PwC Illus additions ("Disclose the Newco insertion", "Manager is not the binder", "Do not invent a pack that mixes unrelated segments", CODM / forecast reasoning, "Contract + control distinguishes from Illus 9.5.7") — removed |
| named Example / entity FAQ | PwC Exhibit A2.7 → Illus 9.7.1, A2.8 → Illus 9.7.2; Exhibits A2.6, A2.9 = extracts → teaching; KPMG Illus kept |
| differ | 9.1 IFRS-compliance claim (Official / DTT / PwC / EY); 9.5 whether common control is needed (Official / PwC / KPMG) |
| Decisions / contrasts | `#s-9-1-dec`, `#s-9-2-ex`, `#s-9-5-bind` (3 arms), `#s-9-7-pf`, `#s-9-7-dg`; contrasts `#s-9-3-ex`, `#s-9-4-ex` |
| EY | 3 → 11 chips (section 6.2 2 → 10; 6.2.1 ×1) — all verified; "seems to confirm IFRS compliance" + BC3.21 "hesitancy" in the 9.1 differ |
| KPMG | Not attached — text kept; chip moves: Combined/Carve 1.3 5 → 4 (prompt removed, content stays in 9.5 table); Example 2B, 2C +1 each (differ row). Author meta inside KPMG Illus removed — listed in `CF-CH09-CONTENT-NOTES.md` for Johnny's veto |
| structure | 9.0 … 9.7; old 9.7 prompts → new 9.7 historical / pro forma, presentation and disclosure |
| densify | Official 3.10–3.14, BC3.20–BC3.21; PwC A2.2–A2.78, A2.132, A2.134–A2.137, A2.139–A2.140, Exhibits A2.1–A2.9; DTT 6.2; EY 6.2. Words 5,725 → 7,967; chips 121 → 203 |
| Map | Neutral leaves; lecture cues removed; binding zone (Control ∥ Mgmt ∥ Business) with PwC ∥ KPMG on management; 9.6 approach row; 9.7 zone; See also; inline style removed |

**QA:** `/tmp/qa.py` clean except the three nested 3.13 sub-items inside the verbatim KPMG quote (known false positive); audit known false positive only; 9.5.10 THIN cleared with A2.37; no HKICPA / § / gate / invent; all in/out anchors resolve (`ch03#s-3-5`, `#s-3-6`, `#s-3-7`, `ch10#s-10-1`; inbound `s-9-1`, `s-9-2`, `s-9-6`, `s-9-ex-*`).
**Ch9 Map narration:** 9.0 hub → Decision 9.1 label (Yes / No → 3.6, 10.1) → stem → Decision 9.2 boundary (Yes / No) → stem → 9.5 what binds (control ∥ management, sources differ ∥ business) → 9.6 top-down ∥ bottom-up → 9.7 historical ∥ pro forma → dashed See also (10.1, 3.6). About 150px iframe-fit dead space below (pack-wide shared `iframe-fit.js`; Build-owned).

## 5l. Gate 11 — Ch10 (DONE 2026-10-02 12:37 HKT)

**Johnny's instruction:** "KPMG author-meta removals in Ch9 are OK (confirmed). Continue Ch10 … EY carve-out 'How we see it' … address if in scope … Ch3 3.6 → 3.5 — FIX in this Ch10 gate … Stop after Ch10."
**Stamp:** all 13 pages `Last update · 2026-10-02 12:37 HKT`. Cache key unchanged. Ch10 iframe + visual CSS `?v=cf2018-ch10-map-20261002` (were `cf-ch09-ch10-skill-clear-20261001` / `cf-ch10-skill-clear-20261001`).

| Decision | Ch10 result |
|----------|------------|
| wrong shape (not invent) | Decision strip `#s-10-3-ex` → mini-flow; PwC Exhibit A2.10 Illus site table / "orphan" conclusion → 3 boxes; Exhibit A2.15 extract Illus → teaching; prompts; "Closed:" bullet; source-label leads; "PwC overlap" li inside KPMG Illus 10.5.1 |
| true invent | none found |
| named Example / entity FAQ | Exhibit A2.10 stays Illus 10.4.1; Exhibits A2.11–A2.15 = extracts → teaching; KPMG Illus kept (renumbered by section; ids unchanged) |
| differ | 10.5 central-cost basis (Official / PwC incremental / KPMG actual); 10.7 hindsight (PwC closed / KPMG three approaches) |
| Decisions / contrasts | `#s-10-1-dec`, `#s-10-3-ex`, `#s-10-5-alloc`, `#s-10-6-int` (Any / None); contrasts `#s-10-6-tax`, `#s-10-6-pen`; 2 pitfalls; transaction-cost table |
| EY | 1 → 7 chips (section 6.2), all verified; "How we see it" carve-out view in 10.1 |
| KPMG | Not attached — text kept; author meta removed in 9 Illus (listed in `CF-CH10-CONTENT-NOTES.md`); Combined/Carve 1.3 6 → 5 (prompt); Example 4B, 4H +1 (differ rows) |
| structure | 10.0 … 10.8; old 10.6 prompts removed |
| densify | Official 3.10, 3.13–3.14, BC3.13, BC3.17–BC3.19, 6.80–6.82; PwC A2.5, A2.17, A2.65–A2.69, A2.79–A2.133, A2.138, A2.139, Exhibits A2.10–A2.15; DTT 6.2; EY 6.2. Words 4,315 → 6,893; chips 86 → 163 |
| Map | Neutral leaves; cues removed; Decision 10.3 overheads test; preparation zone 10.4 ∥ 10.5 ∥ 10.6 / 10.7 ∥ 10.8 with PwC ∥ KPMG on both differs; See also 3.5, 9.1, 6.7 |
| Ch3 debt | "Ch3 · 3.6" portion bridge → `#s-3-5`; boundary links stay `#s-3-6` |

**QA:** `/tmp/qa.py` clean; audit known false positives only (disclaimer/footer; C2 chip-separator heuristic ×2); no HKICPA / § / gate / invent / orphan; all Ch10 in/out anchors resolve.
**Ch10 Map narration:** 10.0 hub → Decision 10.1 portion (Yes → carve-out, Illus 10.2.1; No → 3.6, 9.1) → stem → Decision 10.3 complete and neutral boundary (Yes / No; Illus 10.3.1 foot) → stem → Preparing the carve-out: 10.4 assets/debt ∥ 10.5 allocations (sources differ) ∥ 10.6 specific areas, then 10.7 equity/EPS/hindsight (sources differ) ∥ 10.8 disclosure → dashed See also (3.5, 9.1, 6.7). About 150px iframe-fit dead space below (shared `iframe-fit.js`; Build-owned).

## 5m. Gate 12 — Ch11 (DONE 2026-10-02 13:55 HKT)

**Johnny's instruction:** "Ch10 KPMG author-meta OK → Continue Ch11 (body + Map together)" — EY Ch02 PDF attached (byte-identical, md5 `b9461c94…`); clear the audit-flagged no-invent author meta; verify every EY cite; differ tables; stop after Ch11 body + Map + QA + desktop screenshots.
**Stamp:** all 13 pages `Last update · 2026-10-02 13:55 HKT` (13:52 first, re-bumped after the KPMG flyer commit). Cache key unchanged. Ch11 iframe + visual CSS `?v=cf2018-ch11-map-20261002` (iframe was `cf-ias2-parity-20261001`; CSS had none).

| Decision | Ch11 result |
|----------|------------|
| author meta (no-invent lock) | 11.0 site/PRIMARY lead; "Vs 2022" / 2026 cover banner; "Site label note" (HKICPA); SP1.5 HK parenthetical; **"Do not invent extra steps"**; ".ok" "no invented extra hierarchy steps"; "What this chapter is NOT" list; prompts + h3 suffix — all removed, substance kept elsewhere |
| wrong shape (not invent) | Decision strip `#s-11-5-ex1` → mini-flow `#s-11-2-dec`; strip `#s-11-5-ex2` → IAS 8.11 ordered list; 2 chip-leading DTT callouts → end-chip bullets; Map "Not a licence" bar → body pitfall |
| true invent | Map IAS 8.12 "May also consider…" step — no source on disk → removed |
| named Example / entity FAQ | none in sources → no Illustrations |
| differ | 11.1 purposes weighting (Official / PwC / DTT / EY / KPMG flyer); 11.4 departures (Official / EY 1.2); 11.6 effective date (Official / EY / DTT / KPMG flyer); 11.6 earlier versions (Official / DTT "2001" / EY "1989") |
| Decisions / contrasts | `#s-11-2-dec` (Yes / No); 1 pitfall; 2 peer-rows (purpose triad, SP1.5 outcomes); 11.4 summary table; 11.6 older-references table |
| EY | 1 → 27 chips (Overview, 1, 1.2, 2, 3.1, 3.2), all verified against the attached EY extract |
| KPMG | Insights 1.2.10 kept with its bullet; flyer New Foundation p1/p2 +4 (row was "Ch11 gates may use") |
| structure | 11.0 … 11.7; old 11.5 worked cues, 11.6 "NOT", 11.7 prompts removed; new 11.5 Foundation, 11.6 References/effective date, 11.7 SMEs |
| densify | Official SP1.1–SP1.5, BC0.18–BC0.28 (+ fns); EY Overview/1/1.2/2/3.1/3.2; DTT 1.1/2/3/12; PwC 1.6/1.10–1.11/1.15–1.17; KPMG flyer p1/p2. Words 1,174 → 3,488; chips 58 → 122 |
| Map | Rebuilt in Ch9/Ch10 grammar: hub → Purpose (source lines) → Decision 11.2 → IAS 8.11 order → 11.4 ∥ 11.5 / 11.6 ∥ 11.7 → See also 1.2, 4.1, 5.2, 6.5, 7.5 |

**QA:** `/tmp/qa.py` clean (only the (a)/(b)/(c) sub-items under a chipped parent li, as before); audit known false positives only (disclaimer/footer; chrome inline style); author-meta [] ; all Ch11 in/out anchors resolve.
**Ch11 Map narration:** 11.0 hub → Purpose 11.1 (Board ∥ Preparers ∥ All parties; Official / DTT / EY / KPMG lines, sources differ) → stem → Decision 11.2 "Does a Standard or an Interpretation specifically apply?" (Yes → apply the Standard; No → IAS 8 judgement) → stem → 11.3 IAS 8.11 order (1 similar and related → then → 2 Framework) → stem → 11.4 departures (Official ∥ EY) ∥ 11.5 foundation; 11.6 references/effective date (two differ blocks) ∥ 11.7 SMEs → dashed See also.

## 5n. Gate 13 — Pack Map (DONE 2026-10-02 14:21 HKT)

**Johnny's instruction:** "Ch11 KPMG New Foundation 2018 flyer 4 chips OK — keep. Continue pack Map only (not consistency yet)" — rebuild/densify the pack-level Concept Map; visual-grammar + teaching-body; L→R then T→B; neutral leaves; no lecture cues; prefer structure over DECISION pills; chip order = decision walk; EY-cited text untouched unless verified; desktop only; stop before consistency.
**Stamp:** all 13 pages `Last update · 2026-10-02 14:21 HKT`. Pack cache key unchanged; `assets/map.css` is index-only → `?v=cf2018-pack-map-20261002`.

| Decision | Pack Map result |
|----------|-----------------|
| wrong shape (not invent) | Objective/QC stem drawn R→L ("make information useful for") → L→R "useful information has"; `phase-legend` lecture ("Chapter order, not a preparer runbook", "not a fifth process step") removed; Ch9/Ch10 inline-styled dashed cells + jargon ("CF 3.12 label · binding/fit Illus", "app of 3.13–3.14") → reporting-entity form peers under one boundary bar; Status pills → 11.2 question with Yes/No arms; "Story"/visit-path comment → teaching arc + visit path (no "story"/"spine"/§); page purpose was a chip-order lecture → SP1.1–SP1.2 status sentence with Official chip |
| true invent | none — every node restates its chapter Map / body; no new facts |
| DECISION chrome | none — decisions read from the tree (question ending "?", labelled arms ≤ 8 characters, column-1 route, terminal leaves column 3) |
| differ | flagged only, pointing to the chapter tables: 11.1 purposes, 11.4 departures, 11.6 effective date/references, 9.5 binding, 10.5 allocations · 10.7 hindsight ("Sources differ" tags; not reconciled on the Map) |
| EY | index has no EY chips before or after; no EY-cited chapter text touched |
| densify | 40 links → 73 section-chip anchors (all resolve); Status 11.1–11.7; Ch1 1.3/1.5/1.4/1.6; Ch2 2.5/2.2/2.3/2.6/2.7; Ch3 3.2–3.7; Ch4 4.1.1/4.1.2/4.6–4.8 added; Ch5 decision walk 5.2 → 5.4 ∥ 5.5 (5.3) → 5.1 → 5.6; Ch6 6.5/6.6/6.8/6.9; Ch7 7.1/7.3/7.4/7.5/7.6; Ch8 8.1/8.2/8.3 |
| untouched | chrome bar (incl. its inline style), `aside.pack-disclaimer`, footer-nav, `refs/_shared/*`, all chapters, Ch11 flyer chips |

**QA:** anchors 73/73; no banned words; no "Decision"/"Gate" chrome; audit lecture cue on index gone (remaining: disclaimer-between-main-and-footer + chrome inline style — known, out of scope). `/tmp/qa.py` "no end chip" lines on Map nodes are the body-paragraph heuristic (chapter Map visuals trip it the same way) — Map nodes carry section chips, not cite chips.
**Pack Map narration:** Status frame (11) → 11.1 purposes (sources differ) → 11.2 "Does a Standard or an Interpretation specifically apply to the transaction or other event?" — Yes → Apply the Standard (right); No ↓ 11.3 IAS 8 judgement (4.1 · 5.2 · 6.5) → 11.4 · 11.5 · 11.6 · 11.7 strip. Inside: Objective hub 1.3 → 1.5 ∥ 1.4 → 1.6 → "useful information has" → QC 2.5 (2.2 ∥ 2.3) → 2.6, cost rail 2.7 ↓ "financial statements report about a reporting entity" → Ch3 frame 3.2 · 3.3 · 3.4 → 3.5 forms 3.6 ∥ 3.7/9.1 ∥ 10.1 → boundary bar → Elements 4.2 − 4.3 = 4.4 ⊃ 4.5 ↓ "each defined item" → 5.2? (No → Not that element) ↓ Yes → 5.4 ∥ 5.5? (No → Do not recognise) ↓ Yes → 5.1 Recognise (Later → 5.6 Derecognise) ↓ "then measure" → Ch6 → "then present and disclose" → Ch7 (right); ↓ "measurement basis × capital concept → profit" (8.3) → Ch8 (end).

## 5o. Gate 14 — Consistency pass, full pack (DONE 2026-10-02 14:40 HKT)

**Johnny's instruction:** "Pack Map OK → Continue consistency pass (full CF pack)" — cross-chapter cites, XREF, Map↔body anchors, differ tables not reconciled, no invent, density stay/increase; clear leftover "Story:" visual comments and similar lecture cues; EY text only after verifying against attached Ch02 and rescan EY cites pack-wide; desktop only; stamp; keep Ch11 KPMG flyer chips; do not redesign chrome (log debt instead); do not start IFRS 18.
**Attached:** `uploads/EY-IGAAP-2026-Ch02-Conceptual-Framework.pdf` (full Ch02; text extracted with pypdf to `/tmp/ey/ey_full.txt`). Official / PwC / DTT / KPMG from the repo set.
**Stamp:** all 13 pages `Last update · 2026-10-02 14:40 HKT` (re-bumped after the Ch3 lead fix landed post-14:35).

| Decision | Consistency result |
|----------|--------------------|
| EY rescan (densify) | 307 EY section chips added on Ch1–Ch7 body units (ch01 4→35, ch02 2→40, ch03 2→28, ch04 2→87, ch05 2→61, ch06 4→88, ch07 1→31). Method: index of EY's own `[CF x.y]` references (313 refs, 83 sections); a chip is placed only where the unit's Official paragraphs are restated in EY's matching home section (CF ch N → EY section N+3; Ch0/SP → sections 1–3), first citing section only. Illustrations, differ tables, tables and mini-flows excluded. Ch8–Ch11 already carried verified EY chips (no change) |
| EY verification | Every pre-existing EY chip re-checked against Ch02: 413 section-OK/related, 28 chips sit on units with no CF paragraph (Overview / How-we-see-it remarks — verified by text), 8 locator-only (older-references table, Overview). No EY-cited text deleted or altered. Overview chips support the 2018 substance, not the 2010→2018 framing |
| wrong shape (not invent) | Lecture cues: `<!-- Story:` / "Story:" in all 11 visual files → "Teaching arc:"; Ch5 class `rc-gate` → `rc-test`; "gate"/"spine" stylesheet comments → test/route wording. Reader-visible: Ch10 heading "10.1 Reporting entity — a portion of an entity"; Ch10 table cell "Framework test (both lenses)"; Ch9 "Framework test:"; Ch3 Illus 3.4.1 lead "Liquidation does not trigger derecognition"; Ch3 "Related KPMG notes:" → "Related going-concern cases:"; References author notes → method bullets (no dummy chip) |
| true invent | none — every added chip is a locator to existing text; no new facts |
| XREF / anchors | 216 cross-section links: link text number = target anchor; all chapter Map badges exist in their bodies (others are cross-chapter links that resolve); 0 broken links (audit) |
| Map ↔ body | Ch9 Map "3.6 Reporting entity boundary" now matches the Ch3 heading (visual CSS + iframe key `…b`) |
| cite shape | Ch9 combined chip `para 3.12, BC3.21` split into one chip per locator; no § on chips; family order Official · PwC · DTT · EY · KPMG |
| differ | 19 `.callout.differ` tables: "Sources differ — …" title (trailing full stop removed in Ch2, Ch4 ×3, Ch5), Source | Treatment headers, closing "Shown side by side and not reconciled."; no reconciling wording |
| cache keys | visual iframe `?v=` = visual CSS `?v=`: Ch1, Ch3, Ch4 `cf2018-chNN-map-20261002`; Ch5, Ch9 `…20261002b`. Shared stylesheets: comment-only edits (no bump) |
| untouched | chrome bar, disclaimer/footer, `refs/_shared/*`, `assets/map.css`, Ch11 KPMG New Foundation flyer chips (4), KPMG Insights / Combined-Carve substance |

**Density (words · chips, before → after):** ch01 3277·99 → 3522·130; ch02 4220·132 → 4508·170; ch03 2868·90 → 3067·116; ch04 9665·340 → 10326·425; ch05 6005·185 → 6440·244; ch06 7455·226 → 8100·310; ch07 3582·132 → 3795·162; ch08 unchanged; ch09 8211·203 → 8214·204; ch10 7111 → 7112; ch11, index unchanged; references 481·20 → 452·19 (author meta + dummy chip removed only).
**QA:** `/tmp/qa.py` clean on all pages (only the accepted "no end chip" lines on sub-items / key terms / Map nodes); audit: no "gate" hits, no title-essence flags, 0 broken links. Remaining audit items are known debt (below).

**Chrome job 3 (layout only, no densify):** Ch4 peer keys now match the 4.1.1 lens names (Right ↔ obligation, Direction of benefits, Linking test) and the apply row reads “Applying the definitions — not further elements”. Section titles on Ch1–Ch11 share one number column (`.sec-no` / `.sec-title`). Ch5 Map Decision pills removed; each “no” leaf sits to the right and “yes” continues down. Ch7 7.5 sits beside the solid P&L↔OCI elbow. Ch10 section numbers are rectangular chips (10.3.1 / 10.4.x no longer clipped in a circle). Stamp: all 13 pages `Last update · 2026-10-02 15:51 HKT`.
**Open debt (deferred):**
- Decision pills remain on the Ch9, Ch10 and Ch11 visuals (Ch5 Map pills are gone).
- Ch3 Map still in the older grammar.
- CSS `order:` inside mobile media queries (ch02, ch04, ch05 visual CSS; `assets/shared.css`) — mobile only.
- `assets/iframe-fit.js` "Gate:" comment (build-owned); unused `.start-here .sh-gate` rules in `visuals/shared.css`; `visuals/shared.css` token fork.
- Chrome inline style and disclaimer/footer placement (Grok-owned).
- Ch3 inline `<style id="ch03-iframe-floor">`.
- Prose drift: inline "CF 3.9" references (Ch1–Ch7) vs "the Framework" (Ch8–Ch11).
- Official → Big4 per-paragraph crosswalk not yet updated with the 307 EY placements (section-level counts are in the XREF file).
- Audit C2 heuristic false positives (ch04 2, ch06 1, ch10 2).

## 6. Proposed Ch1 scope (Gate 2) — DONE, see §5b

- Rewrite leads to substance (16 source leads); merge per-firm restatements into one dense unit per point with all supporting chips (no unique detail cut).
- Remove reader meta (1.0 input path, "Locked teaching label", "Official examples (not invented)", h3 lecture suffixes); 1.9 prompts → keep only if non-duplicative, retitled technically.
- Add PwC FAQ 1.21.1 body (section unit, cite `PwC MOA 2020 [Ch1] · FAQ 1.21.1`).
- Decision strips → neutral mini-flow or cited list per M2 decision.
- Ch1 Map: check vs grammar (reading order looks clean); cache keys aligned if touched.
- Refresh `CF-CH01-CONTENT-NOTES.md` (stale "KPMG/EY not in pack"); add PwC FAQ rows to Crosswalk B.
- Run QA A–F + J; desktop shots of Ch1 Map + body changes; update this file.

---

## 7. Section-order drift log (authors only — not reader-facing)

| Visual | Chip order on visual | Body section order | Proposed restructure |
|--------|----------------------|--------------------|----------------------|
| Pack Map | Status frame: 11.1 → 11.2 (Yes → apply the Standard) → 11.3 (4.1, 5.2, 6.5); 11.4 · 11.5 · 11.6 · 11.7 → inside: 1.3 → 1.5 ∥ 1.4 → 1.6 → 2.5 (2.2 ∥ 2.3) → 2.6, rail 2.7 → 3.2 · 3.3 · 3.4 → 3.5 forms (3.6 ∥ 3.7/9.1 [9.5] ∥ 10.1 [10.5, 10.7]) → bar 3.5 · 9.2 · 10.3 → 4.2 − 4.3 = 4.4 ⊃ 4.5; bar 4.1.1 · 4.1.2; 4.6 · 4.7 · 4.8 → 5.2 → 5.4 ∥ 5.5 (5.3) → 5.1 (later 5.6) → 6.2 ∥ 6.3 → 6.5; 6.6 · 6.8 · 6.9 → 7.1 → 7.3 ∥ 7.4 → 7.5; 7.6 see-also → (8.3) 8.1 ∥ 8.1 → 8.2 | 1 … 11 | none — decision-walk order (Gate 13); each band mirrors its chapter Map; nav order unchanged |
| Ch1 Map | 1.3 → 1.2 → (RE) → 1.5 → 1.4 → 1.6 | 1.0 … 1.8 (1.9 removed at Gate 2) | none — Map tells the users-first story; body keeps CF paragraph order (objective 1.2 before users 1.3) so Official cites read in sequence |
| Ch2 Map | 2.1 → 2.5 → 2.2 ∥ 2.3 → 2.4 → 2.6; 2.7 rail | 2.0 … 2.7 (2.8 removed at Gate 3) | none — hierarchy story (tier 2.5 contains 2.2/2.3); body teaches each fundamental before "applying both" (2.5) |
| Ch3 Map | 3.0 → 3.2 (period axis) → 3.3 ∥ 3.4 → 3.5 (3.6 stack inside) → 3.7 | 3.0 … 3.7 (renumbered at Gate 4 to match the Map; 3.8 removed) | none — the body now follows the Map numbers; the old body/Map mismatch is resolved |
| Ch4 Map | 4.1 board: 4.2 − 4.3 = 4.4 (4.5 nested); bars 4.1.1, 4.1.2; row 4.6 \| 4.7 \| 4.8 | 4.0, 4.1, 4.1.1, 4.1.2, 4.2 … 4.8 (4.9 removed; 4.2.1 → 4.1.2 at Gate 5) | none — body follows the Map numbers |
| Ch5 Map | 5.1 → 5.2 definition → usefulness (5.4 ∥ 5.5; bars cost, 5.3) → Recognise \| Do not → 5.6 → 5.7 bar | 5.0 … 5.7 (5.8 removed at Gate 6) | none — body already followed the Map numbers |
| Ch7 Map | Goal (7.1 useful ⇄ 7.1 cost) → Tools (7.2; 7.3 with nested P&L / OCI / 7.5 reclassification; 7.4) → Shapes (7.3, 7.4, 7.5, IFRS 18 see-also) | 7.0 … 7.6 (7.7 prompts removed at Gate 8) | none — body follows Map numbers; Official teaches P&L/OCI (7.15–7.19) inside classification before aggregation (7.20), and the Map nests it the same way while the body keeps it as 7.5 after 7.4 to match the Map badge |
| Ch8 Map | 8.1 (Financial ∥ Physical matrix in user-needs plate) → 8.2 \| 8.3 \| 8.4 → 8.5 strip | 8.0 … 8.5 (8.6 prompts removed at Gate 9) | none — body already followed the Map numbers |
| Ch9 Map | 9.0 hub → 9.1 → 9.2 → 9.5 → 9.6 → 9.7; See also 10.1, 3.6 | 9.0 … 9.7 (old 9.7 prompts → new 9.7 at Gate 10) | none — 9.3 (combined vs consolidated — firm definitions) and 9.4 (why combined FS are prepared) have no Map zone; they teach around the 9.2 boundary test |
| Ch10 Map | 10.0 hub → 10.1 → 10.3 → 10.4 ∥ 10.5 ∥ 10.6 → 10.7 ∥ 10.8; See also 3.5, 9.1, 6.7 | 10.0 … 10.8 (old 10.6 prompts removed; 10.4–10.8 rebuilt at Gate 11) | none — 10.2 (firm definitions) has no Map zone; its Illus 10.2.1 sits on the 10.1 Yes leaf |
| Ch11 Map | 11.0 hub → 11.1 → 11.2 → 11.3 → 11.4 ∥ 11.5 → 11.6 ∥ 11.7; See also 1.2, 4.1, 5.2, 6.5, 7.5 | 11.0 … 11.7 (rebuilt at Gate 12; old 11.5 cues / 11.6 "NOT" / 11.7 prompts removed) | none — body follows the Map numbers; index Status frame links `#s-11-2` / `#s-11-3` keep their topics |
| Ch6 Map | 6.1 → 6.2 ∥ 6.3 → 6.4 → 6.9 note → 6.5 → 6.6 ∥ 6.8 | 6.0 … 6.9 (6.7 equity + owner transactions added; 6.9 prompts → cash-flow techniques at Gate 7) | none — 6.9 sits after 6.8 in the body because Official 6.91–6.95 closes the chapter; the Map shows it beside 6.4 as a "not a third family" note. 6.7 has no Map chip (equity is a residual, not a basis) |

## 8. Checkpoints (desktop 1440)

Stored in `refs/cf-2018/opus-checkpoints/gate1/` (and cloud artifacts):

| File | Proves |
|------|--------|
| `gate1-desktop-index-full.png` | Map + chrome bar (Home · title · Last update HKT · tag row incl. References) + bottom disclaimer + footer; shows R→L Objective/QC stem and `phase-legend` lecture line |
| `gate1-desktop-ch01-concept-map.png` | Ch1 Concept Map (clean relationship scene; dead space under board) |
| `gate1-desktop-ch01-decision-strip.png` | Decision strip meta title + green Output + question/outcome in one box (M2/H3) |
| `gate1-desktop-ch04-illus-4-4-1.png` | Illus with "Cited teaching cue (not an Official numeric IE)" facts (H1) |
| `gate1-desktop-ch09-illus-9-5-1.png` | Sourced dense Illus (KPMG Ex 1B) — reference standard; 3+1 grid wrap |
| `gate1-desktop-ch10-concept-map.png` | Map green/red leaves ×2 + layout-meta band labels (M5/H3) |
| `gate1-desktop-references-full.png` | References page after Ch11; full name \| short form |

Gate 2 (Ch1) — `refs/cf-2018/opus-checkpoints/ch01/`:

| File | Proves |
|------|--------|
| `ch01-gate-desktop-ch01-top.png` / `ch01-gate-desktop-ch01-full.png` | Ch1 top (chrome stamp 02:20 HKT + Map) and full page incl. disclaimer + footer |
| `ch01-1-1-peer-row.png` | 1.1 four neutral peers, L→R story |
| `ch01-1-2-contrast.png` | 1.2 full-scope vs narrow reading with BC1.36 holding decisions |
| `ch01-1-3-mini-flow.png` | Primary-user Decision: Test → labelled Yes / No arms → one outcome each, neutral |
| `ch01-1-4-contrast.png` | BC1.35 single home: input vs rejected separate objective |
| `ch01-1-5-table.png` | Densified 1.5 table with PwC FAQ 1.21.1 chips; pointer rows to 1.4 / 1.6 |
| `ch01-1-6-peer-row.png` | Accrual ∥ cash neutral peers replacing the old Decision strip |

Gate 3 (Ch2) — `refs/cf-2018/opus-checkpoints/ch02/`:

| File | Proves |
|------|--------|
| `ch02-gate-desktop-ch02-top.png` / `ch02-gate-desktop-ch02-full.png` | Ch2 top (stamp 02:39 HKT + Map) and full page incl. disclaimer + footer |
| `ch02-map.png` | Map with downward "usefulness enhanced by" stem; Official materiality wording |
| `ch02-2-1-peer-row.png` | Fundamental · Enhancing · Cost peers |
| `ch02-2-2-differ.png` | `.callout.differ` — materiality wording Official vs PwC |
| `ch02-2-2-materiality-flow.png` | Assessment — material? Yes / No |
| `ch02-2-3-prudence-contrast.png` | Cautious vs asymmetric prudence (BC2.37–BC2.42) |
| `ch02-2-5-process-flow.png` / `ch02-2-5-tradeoff-flow.png` | 2.21 third step; 2.22 trade-off |
| `ch02-2-6-enhancing-flow.png` | Enhancers add usefulness only if fundamentals met |
| `ch02-2-7-cost-peer-row.png` | Costs ∥ benefits peers |

Gate 4 (Ch3 + stamp) — `refs/cf-2018/opus-checkpoints/ch03/`:

| File | Proves |
|------|--------|
| `ch03-gate-desktop-ch03-top.png` / `ch03-gate-desktop-ch03-full.png` | Ch3 top (stamp 02:50 HKT + Map) and full page incl. disclaimer + footer |
| `ch03-chrome-stamp.png` / `index-chrome-stamp.png` | Same pack stamp `2026-10-02 02:50 HKT` on Ch3 and index chrome |
| `ch03-map.png` | Ch3 Map (unchanged), chip numbers matching the renumbered body |
| `ch03-3-1-peer-row.png` | Financial statements · Perspective and going concern · Reporting entity peers |
| `ch03-3-3-perspective-contrast.png` | Entity perspective adopted vs particular-group perspective not adopted (BC3.10) |
| `ch03-3-4-going-concern-flow.png` | Decision — going concern basis (No / Yes arms) |
| `ch03-3-4-illus-liquidation.png` | Illustration 3.4.1 (KPMG Ex 1), body unchanged |
| `ch03-3-6-consolidated-flow.png` / `ch03-3-6-boundary-flow.png` | Consolidated vs unconsolidated; boundary BC3.19 vs 3.14 |

Gate 5 (Ch4) — `refs/cf-2018/opus-checkpoints/ch04/`:

| File | Proves |
|------|--------|
| `ch04-gate-desktop-ch04-top.png` / `ch04-gate-desktop-ch04-full.png` | Ch4 top (stamp 09:19 HKT + Map) and full page incl. disclaimer + footer |
| `ch04-chrome-stamp.png` / `index-chrome-stamp.png` | Same pack stamp on Ch4 and index |
| `ch04-map.png` | Map with shared bars 4.1.1 / 4.1.2 |
| `ch04-4-0-definition-vs-recognition.png`, `ch04-4-1-table-4-1.png`, `ch04-4-1-1-linkers.png`, `ch04-4-1-2-2010-vs-2018.png` | 4.0–4.1.2 components |
| `ch04-4-2-asset-flow.png`, `ch04-4-2-illus-1-trustee.png` … `ch04-4-2-illus-4-grant.png`, `ch04-4-2-differ-existence.png`, `ch04-4-2-differ-faq-wording.png` | Asset Decision, PwC FAQ Illus 4.2.1–4.2.4, two differ callouts |
| `ch04-4-3-three-views.png`, `ch04-4-3-obligation-flow.png`, `ch04-4-3-past-events-flow.png`, `ch04-4-3-contingent-table.png` | Liability components |
| `ch04-4-4-equity-flow.png`, `ch04-4-5-differ-label.png`, `ch04-4-5-element-flow.png`, `ch04-4-5-illus-accrual.png` | Equity Decision; income/expense differ, Assessment and FAQ 1.78.1 Illus |
| `ch04-4-7-executory-flow.png`, `ch04-4-7-illus-kpmg.png` | Executory Assessment; KPMG Example 2 Illus 4.7.1 |

Gate 6 (Ch5) — `refs/cf-2018/opus-checkpoints/ch05/`:

| File | Proves |
|------|--------|
| `ch05-gate-desktop-ch05-top.png` / `ch05-gate-desktop-ch05-full.png` | Ch5 top (stamp 09:44 HKT + Map) and full page incl. disclaimer + footer |
| `ch05-chrome-stamp.png` | Pack stamp |
| `ch05-map.png` | Map with neutral outcome leaves |
| `ch05-5-0-contrast.png`, `ch05-5-1-diagram.png` | 5.0 contrast; Diagram 5.1 peer-row |
| `ch05-5-2-decision-recognise.png`, `ch05-illus-5-2-1-brand.png`, `ch05-differ-brand-faq.png` | Recognition Decision; FAQ 1.73.1 Illus; brand FAQ differ |
| `ch05-5-3-old-vs-2018.png`, `ch05-5-3-concerns-table.png` | 2010 vs 2018 table; BC5.15–22 concerns table |
| `ch05-5-4-assessment-low-prob.png`, `ch05-5-4-flyer-practical-ability.png` | Low-probability Assessment; flyer bullet |
| `ch05-5-5-assessment-mu.png` | Measurement-uncertainty Assessment (3 arms) |
| `ch05-5-6-assessment-derec.png`, `ch05-differ-derec-approach.png` | Derecognition Assessment; Official / DTT / KPMG differ |
| `ch05-5-7-assessment-modification.png` | Contract-modification Assessment |

Gate 7 (Ch6) — `refs/cf-2018/opus-checkpoints/ch06/`:

| File | Proves |
|------|--------|
| `ch06-gate-desktop-ch06-top.png` / `ch06-gate-desktop-ch06-full.png` | Ch6 top (stamp 10:01 HKT + Map) and full page incl. disclaimer + footer |
| `ch06-chrome-stamp.png` | Pack stamp |
| `ch06-map.png` | Map: neutral leaves; entry/exit row VIU / Fulfil = Exit; 6.9 badge in the "not a third family" note |
| `ch06-6-0-contrast.png` | Recognition vs measurement neutral contrast |
| `ch06-6-2-hc-update-table.png`, `ch06-6-3-transaction-costs-table.png` | 6.7/6.8 update table; BC6.30–33 transaction costs table |
| `ch06-6-4-table61-assets.png` | EY Figure 9-1 asset matrix (unchanged) |
| `ch06-6-5-assessment-cashflows.png`, `ch06-6-5-decision-mu.png`, `ch06-differ-outcome-uncertainty.png`, `ch06-6-5-enhancing-table.png` | 6.54–6.57 Assessment (arm labels fit); 6.60 Decision; outcome-uncertainty differ; enhancing-by-basis table |
| `ch06-6-6-decision-market-terms.png` | Market-terms Decision replacing invented Illus 6.6.1 |
| `ch06-illus-6-7-1-shareholder.png` | KPMG Example 3 Illus in 6.7 |
| `ch06-6-9-central-estimates-table.png` | 6.93 central estimates table |

Gate 8 (Ch7) — `refs/cf-2018/opus-checkpoints/ch07/`:

| File | Proves |
|------|--------|
| `ch07-gate-desktop-ch07-top.png` / `ch07-gate-desktop-ch07-full.png` | Ch7 top (stamp 11:18 HKT + Map) and full page incl. disclaimer + footer |
| `ch07-chrome-stamp.png` | Pack stamp |
| `ch07-map.png` | Map: substance foot cue; OCI leaf per 7.17; solid reclassification elbow |
| `ch07-7-0-contrast.png`, `ch07-7-1-tools-peer-row.png` | Neutral scope contrast; four tools peer-row |
| `ch07-7-2-principles-table.png`, `ch07-7-3-classification-table.png` | Principles table; classification table (assets/liabilities, equity claims, components, income/expenses) |
| `ch07-7-3-decision-offsetting.png`, `ch07-7-4-decision-aggregation.png` | Decisions replacing the two invented strips (arm labels fit) |
| `ch07-differ-pl-description.png`, `ch07-7-5-decision-pl-oci.png`, `ch07-7-5-decision-reclassify.png`, `ch07-differ-reclassification.png`, `ch07-7-5-contrast-board-entities.png` | 7.5 differs, Decisions and Board vs entities contrast |

EY audit (after Gate 8) — `refs/cf-2018/opus-checkpoints/ey-audit/`:

| File | Proves |
|------|--------|
| `ch01-ey-411-restore.png` | Ch1 1.3 bullet with restored EY section 4.1.1 chip |
| `ch07-70-oci-fix.png` | Ch7 7.0 OCI bullet without "typically" (7.17 / BC7.24 precision; EY section 10 chip kept) |

Gate 9 (Ch8) — `refs/cf-2018/opus-checkpoints/ch08/`:

| File | Proves |
|------|--------|
| `ch08-gate-desktop-ch08-top.png` / `ch08-gate-desktop-ch08-full.png` | Ch8 top (stamp 11:42 HKT + Map) and full page incl. disclaimer + footer |
| `ch08-stamp.png` | Pack stamp |
| `ch08-map.png` | Map: sourced legend, "Users mainly concerned with" row, 8.3/8.4/8.5 cards |
| `ch08-differ-origin.png`, `ch08-differ-reliability.png` | The two differ tables |
| `ch08-contrast-capital.png`, `ch08-decision-user-needs.png`, `ch08-contrast-return.png`, `ch08-price-peers.png` | 8.1 contrast + Decision; 8.2 return on/of contrast; price-change peer-row |
| `ch08-illus-841.png` | PwC FAQ 1.93.1 sole-trader Illustration replacing the invented CU15 strips |

Gate 10 (Ch9) — `refs/cf-2018/opus-checkpoints/ch09/`:

| File | Proves |
|------|--------|
| `ch09-gate-desktop-ch09-top.png` / `ch09-gate-desktop-ch09-full.png` | Ch9 top (stamp 12:19 HKT + purpose chip + Map) and full page incl. disclaimer + footer |
| `ch09-stamp.png` | Pack stamp |
| `ch09-map.png` | Map: neutral leaves, binding zone with PwC ∥ KPMG, 9.6 and 9.7 zones |
| `ch09-differ-ifrs-claim.png`, `ch09-differ-common-control.png` | The two differ tables |
| `ch09-dec-9-1.png`, `ch09-dec-9-2.png`, `ch09-dec-9-5-bind.png`, `ch09-dec-9-7-pf.png`, `ch09-dec-9-7-dg.png` | Decisions |
| `ch09-contrast-9-3.png`, `ch09-contrast-9-4.png` | Contrasts |
| `ch09-illus-9-5-7.png`, `ch09-illus-9-7-1.png`, `ch09-illus-9-7-2.png`, `ch09-illus-9-5-2.png` | PwC Illus (3 boxes, Exhibit text only); new Exhibit A2.7 / A2.8 Illus; KPMG Illus with meta removed |
| `ch09-disclosure-table.png` | 9.7 minimum-disclosure table (A2.139–A2.140) |

Gate 11 (Ch10) — `refs/cf-2018/opus-checkpoints/ch10/`:

| File | Proves |
|------|--------|
| `ch10-gate-desktop-ch10-top.png` / `ch10-gate-desktop-ch10-full.png` | Ch10 top (stamp 12:37 HKT + purpose chip + Map) and full page incl. disclaimer + footer |
| `ch10-stamp.png` | Pack stamp |
| `ch10-map.png` | Map: neutral leaves, preparation zone, PwC ∥ KPMG differ lines |
| `ch10-differ-central-costs.png`, `ch10-differ-hindsight.png` | The two differ tables |
| `ch10-dec-10-1.png`, `ch10-dec-10-3.png`, `ch10-dec-10-5-alloc.png`, `ch10-dec-10-6-interest.png` | Decisions |
| `ch10-contrast-tax.png`, `ch10-contrast-pensions.png`, `ch10-transaction-costs.png` | Contrasts and transaction-cost table |
| `ch10-illus-10-4-1.png` | PwC Exhibit A2.10 Illus in 3 boxes |
| `ch10-illus-10-5-1.png`, `ch10-illus-10-5-2.png`, `ch10-illus-10-7-1.png` | KPMG Illus with author meta removed and new numbers |

Gate 12 (Ch11) — `refs/cf-2018/opus-checkpoints/ch11/`:

| File | Proves |
|------|--------|
| `ch11-gate-desktop-top.png` / `ch11-gate-desktop-full.png` | Ch11 top (stamp 13:55 HKT + purpose chip + Map) and full page incl. disclaimer + footer |
| `ch11-gate-desktop-stamp.png`, `ch11-gate-desktop-purpose.png` | Pack stamp; purpose line |
| `ch11-gate-desktop-map.png` | Map: neutral leaves, IAS 8.11 order, source lines and sources-differ notes |
| `ch11-gate-desktop-differ-purposes.png`, `-differ-departures.png`, `-differ-effective-date.png`, `-differ-references.png` | The four differ tables |
| `ch11-gate-desktop-decision-11-2.png`, `-ias8-order-11-3.png` | Decision and IAS 8.11 order |
| `ch11-gate-desktop-foundation-11-5.png`, `-references-table-11-6.png` | SP1.5 peer-row; EY older-references table |

Gate 13 (Pack Map) — `refs/cf-2018/opus-checkpoints/pack-map/`:

| File | Proves |
|------|--------|
| `gate13-desktop-index-top.png` / `gate13-desktop-index-full.png` | Index top (stamp 14:21 HKT, status purpose line, Status frame, Objective → QC) and full page incl. disclaimer + footer |
| `gate13-desktop-stamp.png`, `gate13-desktop-status-head.png` | Pack stamp; Status title + 11.1 purposes with sources-differ tag |
| `gate13-desktop-status-fork.png` | 11.2 question, Yes → Apply the Standard (right), No ↓ 11.3 |
| `gate13-desktop-purpose-row.png` | Objective hub → L→R stem → QC with cost rail |
| `gate13-desktop-entity-frame.png` | Ch3 frame, forms 3.6 ∥ Ch9 ∥ Ch10, boundary bar, Elements nested |
| `gate13-desktop-recognition.png` | 5.2 → 5.4 ∥ 5.5 → 5.1 walk with neutral No leaves and Later → 5.6 |
| `gate13-desktop-phase-grid.png` | then measure → Ch6 → Ch7 (right); Ch8 below Measure |

Gate 14 (Consistency) — `refs/cf-2018/opus-checkpoints/consistency/`:

| File | Proves |
|------|--------|
| `cons-desktop-stamp.png` | Pack stamp after the consistency pass |
| `cons-desktop-ch01-ey-chip.png`, `-ch04-ey-chip.png`, `-ch06-ey-chip.png` | Added EY section chips in family order after Official / PwC / DTT |
| `cons-desktop-ch02-differ-title.png` | Differ title without trailing full stop; closing line kept |
| `cons-desktop-ch03-map.png`, `-ch05-map.png`, `-ch09-map.png` | Visuals load with aligned cache keys; Ch9 "3.6 Reporting entity boundary" |
| `cons-desktop-ch03-illus-3-4-1.png` | Illus 3.4.1 lead + "Related going-concern cases:" |
| `cons-desktop-ch10-heading-10-1.png` | "10.1 Reporting entity — a portion of an entity" |
| `cons-desktop-references.png` | References purpose + method bullets (no author notes, no dummy chip) |

Decisions (after Gate 5) — `refs/cf-2018/opus-checkpoints/decisions-20261002/`: see §5e-bis.

## 9. Tools (repo root, read-only on pack)

- `tools/cf_pack_audit.py` — QA A–F + J automated checks; `python3 tools/cf_pack_audit.py refs/cf-2018/draft-v1-linked`
- `tools/cf_shots.py`, `tools/cf_crops.py` — desktop screenshots via local server `http://127.0.0.1:47318/` (`python3 -m http.server 47318` from repo root)

## 10. Traps to remember

- Running a file write and a command that reads it in the same batch races (hit once this run) — sequence them.
- Attached PDFs are under `uploads/` — never commit them (QA H10).
- KPMG Insights 1.2 / KPMG Combined-Carve not attached: no new substance or chips for them this run.
- EY Ch2 IS attached since the EY audit (`uploads/EY-IGAAP-2026-Ch2-CF-p46-106_c98d.txt`): verify every EY chip against the text; move an EY chip off a claim EY does not make rather than dropping it (Ch8 "no preference").
- Do not edit `refs/_shared/*` during the Opus run.
- `.contrast-pair.dense` line-clamps `.box-body` to 3 lines — use plain `.contrast-pair` for dense content.
- When `assets/shared.css` changes: bump `?v=` on all 13 pages together + stamp (exact-string `sed`, check count 6 on index / 5 elsewhere).
- Official HK text says "HKICPA" (1.8, 1.11, 2.11, 2.13, 2.42–2.43) — write "the Board" on site.
- From Gate 3, scope is per chapter: do not touch other pages (stamp/cache) — log stamp drift instead.
- Gate 4: Johnny allowed a pack-wide stamp realign. Stamp is one pack-level time on all 13 pages (no per-chapter stamps). Regex-replace the whole `chrome-last-update` span and check for 13 identical spans.
- If Map chip numbers differ from body numbers, renumber the body to the Map and index (not the other way round), then fix inbound cross-links.
- `.callout.differ` format (skill): title "Sources differ — …", Source | Treatment table with each source's full chips, closing line "Shown side by side and not reconciled." The audit checks for the closing line.
- `.table-wrap` crop indices include tables inside differ callouts — count them when cropping.
- The image viewer may show a stale copy of a re-shot PNG at the same path — copy to a new name to verify.
- Mini-flow arm labels sit in a 76px slot: keep them to about 8 characters ("Changes", "Owners", "Other").
- PwC MOA 2020 predates/straddles the Oct 2018 materiality amendment — quotes old definition (1.51); watch for similar timing differences in later chapters → `.callout.differ`.
- Flyer cite short form is `KPMG New Foundation 2018 · p1/p2`; the QA EY/KPMG chip-set check must exclude it (it is new, not locked).
- Under the Grok lock a "teaching cue" strip that only restates Official is wrong shape; it is invent only if it adds a fact not in source (Ch5: "receivables").
- `cf_crops.py` now forces `.chrome-bar` static so tall crops (Maps) are not overlaid.
- The audit C2 placement heuristic stops at the `, ` separator between same-source chips, so a long chip run after a bold Test reads as "prose after chip" — false positive.
- When a fix lands after a stamp commit, re-bump the stamp (one pack time) and re-shoot the top/full/stamp crops.
- A firm chip with no locator (e.g. `PwC MOA 2020 · presentation`) is not a short form to rename — replace it with the precise paragraph chips when the content is densified, and log it.
- KPMG Combined/Carve Illus carried author meta ("CF does not invent…", "orphan vs Official CF", Map links). Gate 10 removed those sentences without touching KPMG facts or conclusions and listed them for Johnny's veto — do the same in Ch10.
- PwC Appendix 2 A2.79–A2.133 — used in Ch10 10.4–10.7 (Gate 11).
- EY section 6.2 carve-out "How we see it" remark — used in Ch10 10.1 (Gate 11).
- Johnny confirmed the KPMG author-meta removals (Ch9); Ch10 applied the same treatment. Ch11 author meta (incl. the audit-flagged "Do not invent extra steps") cleared at Gate 12.
- The uploads folder is `~/.cursor/projects/workspace/uploads/` (EY PDF + TXT there); `/workspace/uploads/` holds the older set. Extracted text copies are in `/tmp/src/` and `/tmp/ey/`.
- `/tmp/build11.py` reads the pre-gate page from commit `b9bf2d4` (not HEAD) — rebuilding from HEAD fails its purpose-line / iframe asserts.
- The EY Ch2 slice (p46–106) ends with the contents page of EY Ch3 only — it cannot support IAS 8.10–12 detail; IAS 8 teaching rests on DTT 2 and Official BC0.28 fn.
- EY "What you need to know" is cited `IGAAP 2026 · Ch2 · Overview` (new locator, Gate 12).
- KPMG New Foundation flyer is not under the Insights / Combined-Carve lock — Ch11 placed its p2 "Check your policies" row.
- Pack Map (Gate 13): `assets/map.css` is loaded only by `index.html` — rewrite freely and bump only the index link. Decision grids share `--c1/--c2/--c3`; `phase-grid` / `drop-flow` padding = `--frame-inset` (16px) so column 1 lines up with `.rec-frame` content.
- "Story:" visual comments were cleared pack-wide at Gate 14 ("Teaching arc:") — do not reintroduce "story", "spine" or "gate" in comments or class names.
- EY index tool (`/tmp/ey/eyindex.py` → `eyidx.json`): EY often cites a CF paragraph outside its home section (e.g. CF 1.2 inside EY 6.1.1). Place EY chips by the home-section rule (CF ch N → EY section N+3; Ch0/SP → 1–3) and the first citing section only; check with `/tmp/eycheck.py`.
- EY Overview ("What you need to know") supports the 2018 substance, not 2010 → 2018 change framing — do not hang it on "what changed" sentences.
- The full EY Ch02 PDF (`uploads/EY-IGAAP-2026-Ch02-Conceptual-Framework.pdf`) supersedes the p46–106 slice for EY checks.
- The image viewer intermittently returns "File not found" for fresh PNGs — re-read once, or read from the tool's own output folder.
