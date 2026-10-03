# OPUS working memory — IAS 2 pack review / amend (2026-10-01)

**Runner:** Claude Opus 5.5 (high). **PM:** Johnny Pang (via Grok Bot).
**Pack:** `refs/ias-2/draft-v1-linked/` (unpacked from `uploads/ias2-draft-v1-linked.tgz`; the archive nested a second `draft-v1-linked/` folder — flattened so the pack root is this folder).
**Governing docs (read in full, this order wins):** `OPUS-IAS2-REVIEW-BRIEF-2026-10-01.md` → `OPUS-KEY-REITERATIONS.md` → skills `ifrs-teaching-body`, `ifrs-teaching-body-qa`, `ifrs-visual-grammar` (v2026.10.01-18) → `IAS2-CONTENT-REWRITE-METHOD.md`. Older amend notes (`IAS2-OPUS-AMEND.md` etc.) are evidence only; brief overrides them.

---

## Gate log

| # | Gate | Status | Johnny approval |
|---|------|--------|-----------------|
| 1 | Overall review (notes only, no HTML change) | **DONE** | **continue** relayed by Grok Bot (PM) on Johnny's behalf — Johnny skipped the widget; decisions 1–4 below |
| 2 | Ch1 amend (body + chapter-top Map) | **DONE** (body + Map r3) | Johnny: fix Ch1 before Ch2 → "Change all" on Ch1 Concept Map → "fix Ch1 Concept Map only" (r3) |
| 3 | Ch2 amend (body + chapter-top Map) | **DONE** (+ 3b Map chrome fix Ch1/Ch2) | Johnny: "Ch2 body OK" → Map chrome fix → "continue straight to Ch3" |
| 4 | Ch3 amend (body + body visuals + chapter-top Map) | **DONE** | Johnny: "continue straight to Ch3 … STOP only at the Ch3 gate" + 11:05 body-visual reminder → 11:47 "Continue Ch4" |
| 5 | Ch4 amend (body + body visuals + chapter-top Map) | **DONE** — awaiting Johnny | Johnny 11:47: "Continue Ch4 … status + screenshots + ask continue when Ch4 gate ready" |
| 5b | Map yes/no labels pack-wide (Step A) | **DONE** | Johnny 14:18 (via PM): "Fix Map yes/no labels FIRST, then do Ch5. One continuous run" |
| 6 | Ch5 amend (body + body visuals + chapter-top Map) (Step B) | **DONE** — checkpoint, awaiting Johnny; Ch6 NOT started | Johnny 14:18: "stop only when BOTH are done (checkpoint for Johnny) … Do NOT auto-start Ch6" |
| 7 | Ch6 amend (body + body visuals + chapter-top Map; pack Map Ch4–Ch6 labels) | **DONE** — checkpoint, awaiting Johnny; Ch7 NOT started | Johnny: "Continue to Ch6 NOW … STOP when Ch6 done — do NOT auto Ch7" |
| 7b | Ch1–Ch3 debt wave (reading order: chapter Maps + pack Map Ch1–3; Illus 3.5.2; Ch1–2 body visuals; Ch1 h4) | **DONE** — checkpoint, awaiting Johnny; Ch4+ NOT started | Johnny: "HARD next wave — CLEAR Ch1–Ch3 debt first … Do not start Ch4+ unless remaining Ch1–3 debt is zero" |
| 8 | Pack Map enhance | Ch1–3 portion done in 7b; Ch4–6 portion done in 7 | — |
| 9 | Consistency pass | not started | — |
| 10 | KEY CHANGES handoff (`OPUS-IAS2-KEY-CHANGES-2026-10-01.md`) | not started | — |

**Rule:** STOP after each gate; screenshots + this file updated; do not start next gate until Johnny says **continue**.

---

## Environment / tooling (reuse next run)

- Static preview: `python3 -m http.server 47213 --bind 127.0.0.1` from the pack root (tmux session `ias2-static`). Night theme renders by default.
- `tools/pack_audit.py` (read-only): QA-skill automated checks per chapter — cite grammar (house-only, `§`, EY/KPMG/PwC/DTT work labels), Illus-in-strip, peer colour, `<p class="box-body"><ul>`, densify li/char counts (≤5 li or <350 chars = THIN), title-essence leads, flowery heading cues, unlinked `see N.M`, broken anchors. Run `python3 tools/pack_audit.py -v`.
- `tools/gate_shots.py <gate-label>`: Playwright + `/usr/local/bin/google-chrome` → `/opt/cursor/artifacts/screenshots/<gate>-*.png` (pack Map, Ch1 top, Ch3 top + first Illus, Ch4 top + first Illus). Shot sets: `python3 tools/gate_shots.py <gate> <base> review|ch01` (add a `SHOT_SETS["chNN"]` list per chapter gate; modes full / clip / element / range / mobile; sticky header unpinned for element shots).
- Source text for verification: `pypdf` extracts of Official HKAS 2, DTT iGAAP 2022 A11, PwC MOA 2020 Ch25 (to `/tmp/ias2src/`, regenerate if missing); KPMG = `uploads/kpmg-3.8-extract.txt`. **EY iGAAP 2026 Ch23 full PDF not attached** — EY claims can only be checked against site + skills; never add EY substance.
- Rough visuals: **filenames are swapped** — `scope-definition-flow-rough.png` shows the **cost-components matrix**; `cost-components-matrix-rough.png` shows the **scope flow**. Use by content, not filename.

---

## Gate 1 — Overall review notes (no invent; issues/opportunities only)

### A. Pack-wide automated QA baseline (pre-amend)

| Check | ch01 | ch02 | ch03 | ch04 | ch05 | ch06 |
|------|------|------|------|------|------|------|
| Cite chips | 87 | 44 | 202 | 99 | 38 | 56 |
| House-only / `§` / bad EY label | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| Illus (all worked-strip) | 12 | 3 | 41 | 18 | 2 | 3 |
| Peers coloured ok/warn | 0 | 0 (but a `li.warn-note` "Warn:" line inside 2.1.2) | 0 | 0 | 0 | 0 |
| `<p class=box-body><ul>` | 0 | 0 | 0 | 0 | 0 | 0 |
| THIN by quant gate | 0 | 0 | 1 (3.10.3, 346 chars) | 0 | 0 | 0 |
| Illus with any table/diagram | 0/12 | 0/3 | 3/41 | 1/18 | 1/2 | 3/3 |
| Broken anchors / unlinked `see N.M` | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| HKAS on UI | 0 | 0 | 0 | 0 | 0 | 0 |

Near-thin (350–500 chars) to recheck vs source: 3.2.3 (392), 3.10.2 (450), 4.4.1 (459), 1.3.4 (474), 1.1.5 (485), 3.6.2 (493), 3.10.6 (491).
Cite-label odd (legal per skill but inconsistent): ch03 `PwC · IFRS 9 paras 4.3.3, 5.7.1` and `PwC · IFRS 9 para 4.3.1` lack `MOA 2020`.

### B. Recurring patterns (pack-wide — fix in every chapter)

1. **"Same …" duplicate bullets (write-once debt).** Nearly every section has an Official-quote bullet followed by a firm bullet that only says "Same …" with DTT/PwC chips (e.g. 1.2, 1.4, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 4.0, 4.3, 4.4, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.4, 6.1, 6.2, 6.3, 6.4, 6.5). Also lead sentence often repeats the first bullet's Official quote (3.1 says para 10 three times). → Collapse to **one dense unit + chips for every supporting source**; keep any unique firm addition (e.g. DTT warehouse→initial point of sale in 3.6; DTT "still consider obsolescence" in 4.7; DTT/PwC IAS 1 separate presentation in 6.4).
2. **Non-technical headings / labels (E2).** Flowery or chrome: 1.0 "What this chapter decides", 1.5 "How the gate feeds the rest of the pack", 2.0 "A light chapter on purpose", 2.3 "Handoff", 3.0 "Initial measurement is the cost arm", 3.10 "Cost formulas — assignment, not a flow theatre", 4.0 "This is the home of the identity", 4.7 "Reversals are required — and capped", 5.0 "One family of exits", 6.0 "A package, not the measurement model". Body prose also carries "theatre", "ritual", "story", "bites", "slogan", "exam contrast". → Retitle to Official headings/phrases (Objective; Scope; Definitions; Measurement of inventories; Cost of inventories; Cost formulas; Net realisable value; Recognition as an expense; Disclosure).
3. **Irregular numbering.** Sections `2.1a`, `3.3b`; Illus out of DOM order (1.1.5 before 1.1.4; 3.2.13 between 3.2.2 and 3.2.3; 4.2.2 before 4.2.1); `4.5.3b`. → Renumber in order + hyperlink review (preserve Map ids: `#s-3-ex-b`, `#s-3-ex-c`, `#s-4-ex-a`, `#s-4-ex-d`, `#s-3-ex-lifo`, `#s-4-ex-costs-sell`, all `#s-N-M`).
4. **Peer labels / bullet leads not technical or carrying firm ids (E / E2).** "Teaching gate", "Teaching", "Related traps", "Exception / warn", "FS teaching facts (paraphrase)", "Policy facts (paraphrase)", "What para 36 users see", "Contrast with Ch3 FX-in-cost", "Direct costing (3.2.3.1-1)", "Marginal costing (3.2.3.1-2)", "Manufacture path (Ex 11A)", "Development path (Ex 11B)"; leads "DTT pipeline fill", "Crypto tip (DTT)", "Why policy (DTT)", "Firm view —", "Teaching cue." → Substance-first labels; locators only in chips.
5. **Author meta inside teaching / Illus.** "Keep this plate on Chapter 1 — do not move…", "This is a Scope / classification plate — not a Ch3 cost-build formula", "EY places this Practical example immediately after…", "Do not invent hedge accounting maths here", "this plate does not invent…", "Show LIFO in teaching only to explain the ban", "Columns match Inform", "not a sequence of departments the Map has to walk", "Tip sits on 'other costs'…". → Remove meta (not teaching substance; no detail lost).
6. **Unsourced editorial point-chips / bullets (no-invent risk).** No cite chip: 1.1 "Why the definition is drawn this way"; 3.3b "Teaching cue"; 4.1 bullets 1 & 3; point-chips "Why normal capacity", "Why a ceiling", "Why reversals exist", "Concept insight" (ch02, ch05), "Tie back" (ch06), "Trap" (ch01, ch03); ch04 warn chip "Cross-GAAP trap … US GAAP habit" — **US GAAP is outside pack sources**. → Either anchor to an Official/firm locator that says it, fold into a cited unit, or drop the unsourced claim. Ask Johnny before dropping (see Decisions needed).
7. **Multi-firm attribution in prose instead of chips.** e.g. 2.1.2 "(PwC)", "(EY)", "(DTT)", "EY also flags…"; 5.3 "DTT: … PwC FAQ: …"; 1.1.2 "EY likewise treats…". Keep only where it marks a genuinely distinct firm view; otherwise chips only.
8. **Illus visual debt (E3).** Complex plates prose-only: 3.2.6–3.2.8 variable payables (IAS 2 × IFRS 9 — a 3-row comparison matrix would teach the gate), 3.2.9 EY forward (CU40/50/10 mini table), 3.3.3 + 3.3.4 normal-capacity arithmetic (under/normal/over production table), 4.5.3/4.5.3b/4.5.9 covered vs excess vs onerous (bucket diagram), 4.5.5 long-cycle NRV methods (two-route mini-flow), 4.6.1 PwC stage table (stage cost/selling table from source), 2.1.2 consignment control indicators, 1.1.7 CO2e package split, 1.3.3 emissions paths.
9. **FAQ ≠ Illus candidates (B0) — content is not a case study.** 1.3.1 (BC6–BC8 narrative), 1.3.2 (EY structure point + KPMG Ex 3A/3B — split: KPMG gold wholesaler is a case; EY structure point is section text), 1.4.1 (KPMG samples/catalogues guidance list), 3.3.10 (KPMG interruptions capitalise/expense checklist), 3.6.2 (DTT distribution include/expense list), 3.10.4 (LIFO BC narrative; Map-linked id `#s-3-ex-lifo` must be kept), possibly 3.9.4 (base stock practice) and 3.2.9 (EY forward — has CU numbers, likely stays Illus). → Demote to section `h4` + lead + list/table + chips where not a case; keep ids.

### C. Accuracy / no-invent flags (verified against uploads)

| Where | Issue | Evidence |
|------|------|------|
| ch04 `#s-4-ex-a` (4.4.1) | SKU A/B/C numbers (40/55, 30/28, 20/12) not in Official/DTT/PwC/KPMG; only IAS 2 + EY 3.3 chips | grep of all four sources; prior `IAS2-OPUS-AMEND.md` item 2 also flags as teaching numbers |
| ch04 `#s-4-ex-d` (4.7.1) | Peers 1–3 (100/70/90/110; materials 50/30) not in sources; peer 4 = KPMG Ex 9 (100→95→103) is sourced | KPMG 3.8.335.30–40 |
| ch05 5.1 / 5.2 / 5.3 loose `<p>` entries | "80 of carrying amount", "Dr expense 10", "70 to 90" journals derive from the unsourced strips above | — |
| ch06 point-chip "Tie back" | refers to "the 10 write-down and the 20 reversal in Chapter 4" — unsourced numbers | — |
| ch03 3.2.3 (PwC FAQ 25.19.1) | Conclusion "Often P&L as a reduction of the related selling expense" is **not** in the FAQ; FAQ's IFRS IC point (cash and settlement discounts deducted from cost; rebates that specifically and genuinely refund selling expenses not deducted) is **missing** | PwC MOA 2020 Ch25 FAQ 25.19.1 text |
| ch02 2.0 + PwC 25.9 bullet | PwC 25.9 lists **three** criteria (control; expects future economic benefits; **cost can be measured reliably**). Site drops the third and 2.0 lead calls "probable plus reliable measurement" "theatre" — contradicts the cited firm | PwC MOA 25.9 |
| ch03 3.5 | Official para 15 compressed to "design costs for a specific customer" — drops "non-production overheads" example | IAS 2 para 15 |
| ch01 Map "No — stop" leaf | "PPE in use, or a financial asset, does not become inventory because a sale is someday possible" — unsourced phrasing | body 1.1 bullet also unchipped |
| ch04 point-chip | "US GAAP habit that write-downs are not reversed" — outside pack sources | — |
| Verified OK (spot) | PwC FAQ 25.8.1 (C10/C12), KPMG Ex 2 bottles + deposits 3.8.40.30, KPMG Ex 5 (100/800/80/130/6.15), KPMG Ex 9, KPMG Ex 13, DTT TV 2,000/CU16,000, DTT WA 382,000/4.24/87,000, DTT retail 65%/325, PwC FAQ 25.32.1 batches, IAS 2 para 2(a) [deleted] | sources |

### D. Duplicate plates across chapters (write once + pointer + all chips)

| Plate | Locations | Note |
|------|------|------|
| PwC FAQ 25.10.1 spare parts (+ KPMG Ex 1 / 3.8.30) | 1.1.3 and 2.1.1 (near-verbatim) | PwC homes 25.10 under *Recognition*; KPMG 3.8.30 under definition. Pick one home, pointer in the other |
| Pipeline fill (DTT 2.1-2) | 1.1.1 + 2.1 bullet | Ch2 bullet → pointer only |
| KPMG Ex 17 reversal disclosure (cost 100 → 80 → sold 120 → disclose 20) | 5.3 bullet 3, 5.3.2, 6.4 bullet 4, 6.4.1 | Four tellings. Presentation in Ch5, disclosure in Ch6 — one Illus + pointer |
| "Matching principle eliminated" (IN14) | 2.2 and 5.1 | Home = Ch5 (Official IN14 sits under "Recognition as an expense") |
| NRV vs fair value (para 7; PwC FAQ 25.8.1) | 1.3.4, 4.2 bullets, Ch1 table, both Maps | Home = Ch4 4.2; Ch1 keep scope-relevant pointer |
| Broker-trader para 5 text | 1.3 bullet 4, 1.3 table, 1.3.2 Assessment | Collapse |
| Firm-contract "Teaching:" bullets | 4.5.3 and 4.5.3b (verbatim) | Keep both numeric sets (unique), write teaching bullets once |
| Expense exits (para 34–35) | 2.2, 5.0–5.4 | Ch2 → pointer |

### E. Chapter-by-chapter opportunities (no invent)

- **Ch1 Scope.** Objective (para 1) told twice (Official + PwC/DTT restatement) → one unit + IAS 2 para 1 + EY 2.1 + DTT 1.1 + PwC 25.2. Section order fine (definition → full exclusions → measurement carve-out → IFRS 15 costs). Johnny scope-flow rough maps onto Ch1 Map: containment "asset + (held for sale OR in production OR materials/supplies)" → scope exclusions (para 2(b)/(c)) → IAS 2 inventory → two measurement branches: lower of cost and NRV (para 9) ∥ measurement carve-out (para 3(a)/(b)). Current Ch1 Map already has 3 gates; rough suggests stronger containment at gate 1 and a fork at the foot.
- **Ch2 Recognition.** Mostly KPMG 3.8.90 + PwC 25.9 — good content. Fix PwC 25.9 accuracy, drop editorial "theatre/ritual", demote duplicates (spare parts, pipeline, expense exits) to pointers; contrast-pair ok/warn is non-Illus → allowed. 2.1.2 consignment = best visual candidate (control indicators).
- **Ch3 Initial measurement.** Strong density (41 Illus). Add Official cost-components **section matrix** in 3.1 per Johnny rough (purchase para 11 / conversion paras 12–13 / other para 15 vs not-in-cost para 16 + paras 17–18 pointers) — section, not Illus; keep PwC 3.1.1 matrix beside it. Renumber 3.2.x; demote checklist plates (3.3.10, 3.6.2, 3.10.4); add variable-payable comparison matrix; densify 3.8 (thin: lead + one "Same" bullet) only from PwC 25.5–25.7 / DTT 3.2.6 if they hold more; LIFO BC10–BC20 detail could be densified from Official BC (in pack).
- **Ch4 Subsequent measurement.** Merge 4.0/4.1 (both para 9). Retitle 4.2 → "Net realisable value and fair value". Renumber 4.2.1/4.2.2 and 4.5.3b. Resolve unsourced 4.4.1 / 4.7.1 strips (Johnny decision). Add tables/diagrams for 4.5.3/4.5.3b/4.5.9 and 4.6.1.
- **Ch5 Derecognition.** Thin chapter (2 Illus). Collapse duplicate exit bullets; resolve unsourced journals; KPMG Ex 17 duplication with Ch6; drop "not a calendar" chrome. Check PwC 25.42–25.46 / DTT 3.4 for unused detail before claiming complete.
- **Ch6 Disclosure.** Good EY FS tables. Retitle 6.0; collapse "Same …" bullets; "Teaching cue" bullets in 6.2.1/6.4.2 → substance labels or drop meta; KPMG Ex 17 de-dup.

### F. Concept Maps (chapter-top + pack Map) — review vs visual-grammar

- **Pack Map (`map-formula-board.html`).** Solid formula board (scope gate → lower-of board with Cost ∥ NRV arms → expense exit → disclosure). Gaps vs brief: (1) no explicit **chapter flow** — Ch2 is only a pointer line; no 1→6 jump spine/rail; (2) no nodes for Ch3 3.4 joint/by-products, 3.8 deemed cost at harvest, 3.9 techniques; Ch4 4.5 evidence/firm contracts, 4.6 materials — consider light pointers only (Map = jump board, not body redraw); (3) chrome label "Thin route"; (4) "Entity-specific recovery ceiling … not a revaluation" fine but check wording vs para 7.
- **Ch1 Map.** Diagnosis tree (3 gates) is the right TYPE. "No — stop" leaf wording unsourced; consider Johnny rough containment for gate 1.
- **Ch2 Map.** Labels "one recognition idea", "second recognition ritual", "Next / handoff" → technical-strict fail. "property held for resale … — not PPE" ok.
- **Ch3 Map.** Containment + cost formulas + LIFO missing route — good; matches Johnny cost rough already. Minor: "idle capacity is not unit cost" ok.
- **Ch4 Map.** Formula board — good. "Contracts and evidence" cell OK.
- **Ch5 Map.** "three routes, not a sequence" restates peer rank (visual-grammar §1.6 fail); hub → exits has no labelled stem; "not income of a new kind" wording.
- **Ch6 Map.** Title "What a user needs to read the inventory story" → technical-strict fail ("Disclosure — IAS 2 para 36–39").
- **Iframe dead space** under Ch1/Ch3 (and others) Concept Maps — Build (`theme.js`/`iframe-fit.js` height measure). Out of Opus scope per visual-grammar unless Johnny unlocks.

---

## Decisions needed from Johnny (before / during Ch amends)

1. **Unsourced teaching strips** `#s-4-ex-a` (4.4.1) and peers 1–3 of `#s-4-ex-d` (4.7.1), plus dependent Ch5 journals and Ch6 "Tie back" chip: (a) replace with sourced figures (KPMG Ex 9 already in 4.7.1; DTT/PwC alternatives) keeping ids, (b) keep but relabel, or (c) remove. Recommendation: (a) — no-invent lock.
2. **Unsourced editorial chips/bullets** (B.6, incl. US GAAP chip): drop or keep? Recommendation: drop unsourced claims; keep only what an Official/firm locator supports.
3. **Home chapter for duplicates** (D): spare parts (Ch1 vs Ch2), KPMG Ex 17 (Ch5 vs Ch6). Recommendation: spare parts → Ch1 (classification), Ch2 pointer; Ex 17 → Ch6 Illus (disclosure), Ch5 keeps presentation sentence + link.
4. **Iframe dead space**: leave for Build, or unlock a fix?

## Decisions / conventions locked so far

- Do not commit `uploads/` (copyrighted PDFs) — pack only.
- No HTML changed at Gate 1.
- **Grok Bot (PM) locked decisions for this wave (relayed after Gate 1, Johnny skipped widget):**
  1. Unsourced 4.4.1 / 4.7.1 strips → replace with sourced figures, keep Map anchors (`#s-4-ex-a`, `#s-4-ex-d`); if no sourced substitute fits, leave an explicit GAP note — never keep unsourced numbers as teaching fact. (Applies at Ch4; dependent Ch5 journals / Ch6 "Tie back" follow.)
  2. Uncited Why / Trap / Concept insight chips and bullets (incl. US GAAP) → drop any claim without an Official or pack Big4 locator; keep only sourced tips.
  3. Duplicate homes: spare parts → **Ch1** (1.1.3) with Ch2 pointer; KPMG Example 17 → **Ch6** with Ch5 pointer. Write once + all supporting chips.
  4. Empty space under Concept Map iframes → leave for Build; do not touch iframe-fit chrome this wave.
- **Demoted (FAQ ≠ Illus) content** goes to a numbered `h4` section when its parent `h3` has no Illustrations left (pattern = Ch3 `3.1.1` h4), or into a dense bullet when it is a rationale paragraph (BC). Old Illus id is kept on the `h4` / `li` so inbound links survive.
- **Two-peer strips leave an empty third column** (shared `.worked-strip-grid` is fixed 3 columns — Build). Content fix: frame cases as three neutral peers (e.g. Facts | Inventories | PPE) rather than touching shared CSS.
- **In-strip supporting table** sits after the peer grid inside `.worked-strip` (skill: "case-study Illus … may keep that table under the worked-strip"). No margin between grid and table — shared CSS = Build note, not fixed here.
- **Chapter-top Map method:** story + visit path written first (recorded per chapter below); chapter-local CSS in `visuals/ias2.css` only, new rules scoped (`.scope-tree …`) so other chapter visuals are untouched; cache-bust iframe `?v=`.
- **Sourcing rule applied in Ch1:** any sentence that only the old site asserted, with no Official / DTT / PwC / KPMG text behind it and no EY chip on site, was removed or replaced with source wording (EY text already on site kept as-is — EY PDF not attached).

---

## Gate 2 — Ch1 amend log (2026-10-01)

**Files:** `ch01.html`, `visuals/ch01-scope.html`, `visuals/ias2.css` (scoped additions), `tools/gate_shots.py` (Ch1 shot set). Iframe `?v=ias2-ch1-amend-20261001`.

**QA after amend (`tools/pack_audit.py -v`):** cites 87 → **146** (Official 78 · KPMG 26 · PwC 17 · DTT 14 · EY 11); house-only 0; `§` 0; HKAS on UI 0; title-essence fails 0; flowery heading cues 0; broken anchors 0 (pack-wide link check incl. Map iframes: all OK); Illus 12 → **10** (2 demoted, not deleted); none THIN; 2 Illus now carry tables (1.1.7, 1.3.2).

**Headings (technical-strict):** 1.0 What this chapter decides → **Objective**; 1.1 What inventories are → **Definition of inventories**; 1.2 Full exclusions → **Scope exclusions**; 1.3 Measurement-only carve-outs → **Inventories excluded from the measurement requirements only**; 1.4 Costs that never become inventory → **Costs that do not give rise to inventories**; new h4 **1.4.1 Advertising and promotional items — samples and catalogues**; 1.5 How the gate feeds the rest of the pack → **Scope outcomes**.

**Write-once merges (all chips kept):** objective (Official para 1 + EY 2.1 + DTT 1.1 + PwC 25.2 — para 1 now quoted in full incl. the omitted cost-formulas sentence); scope exclusions (para 2 + 40E + IN6 + DTT 2.2 + PwC 25.3 + EY 2.3); measurement-only (IN7 + DTT 2.2 + PwC 25.4 + EY 2.3 — former separate "excluded from only measurement" bullet folded in); broker-trader definition (para 3(b) + 5 + IN9 + PwC 25.8 + EY 2.3); IFRS 15 fulfilment costs (para 8 + PwC 25.14 + DTT 2.3 + KPMG 3.8.10; duplicate see-also callout removed).

**Added from pack sources (no invent):** KPMG 3.8.10.20 intangibles produced for resale (software); KPMG 3.8.25 inventory vs investment property / business model; KPMG 3.8.20.20–30 no reclassification of PPE on a decision to sell, rental assets routinely sold → inventories at carrying amount (IAS 16 para 68A); spare-parts rule bullet (IAS 16 para 8, PwC 25.10, KPMG 3.8.30, DTT 2.1); re-usable packaging rule (KPMG 3.8.40.10); DTT 2.1 research-phase supplies; DTT 2.1 IFRIC 20 stripping pointer; KPMG 3.8.10.30 trading financial assets not inventory; PwC 25.5 agricultural activity / harvest definitions; PwC 25.6–25.7 + DTT 3.1 producers carrying at cost apply full measurement; KPMG 3.8.70.10 producers-only (no exemption for processors); KPMG 3.8.70.25 "near future" factors + IFRS 9 own-use; KPMG 3.8.70.40 presentation/disclosure still apply; KPMG 3.8.73 cap-and-trade description + policy choice regardless of bought/granted; DTT 2.1-2 "fixed fee"; DTT 2.1-3 disclosure para numbers (IFRS 13 91–99, IAS 1 122, IAS 10 21).

**Removed (unsourced / meta / editorial — no teaching detail lost):** 1.0 "It is not a purchasing process"; 1.1 unchipped "Why the definition is drawn this way"; 1.1.2 "EY likewise treats…" (prose attribution — EY chip stays); 1.1.3 "not a fake 'always inventory' rule"; 1.1.4 "Same multi-period use test" → now a link to 1.1.3; "not an inventory classification fix"; 1.1.6 "Sale remains the primary recovery path…" (not in DTT 2.1-4); 1.1.7 "Do not bury the offset value…" and duplicate Facts line; 1.2 "do not teach it as a live exit" + **"former construction-contract WIP exclusion"** (not in pack sources — replaced by sourced "Paragraph 2(a) is deleted (IFRS 15 amended paragraph 2)", IAS 2 para 40E); 1.3 **Trap point-chip** (decision 2); table "Not the ordinary retailer's lower-of model"; 1.3.x "Keep this plate on Chapter 1…" ×2, "EY homes the broker-trader rule under Scope…", "This is a Scope / classification plate…", "see IAS 38 pack / EY Ch18" → "(IAS 38)"; 1.4 see-also "Do not force them onto the IAS 2 cost arm" (duplicate of the bullet); 1.4.1 "until sold under the supply arrangement", "The retailer's free giveaway does not re-label…", "so the IAS 2 inventory definition is not met" (beyond KPMG text).

**Illustrations (DOM order = number order):** 1.1.1 pipeline (peers Facts | Classification | Measurement; + IAS 16 para 6 chip per DTT) · 1.1.2 crypto (Classification | Commodity broker-trader measurement | Disclosures noted by the Committee) · **1.1.3 spare parts = home** (PwC FAQ 25.10.1 car manufacturer + KPMG Ex 1 aircraft charter; Facts | Inventories | PPE) · 1.1.4 re-usable bottles (was mislabelled 1.1.5; Facts | Not inventories | PPE; chip IAS 16 para 8 → para 6, since bottles are not spare parts — KPMG points to its PPE-definition section) · 1.1.5 lease-end assets (was 1.1.4) · 1.1.6 property leased before sale · 1.1.7 CO2e offsets (+ table item | classification | initial measurement) · **1.3.1 commodities** (rebuilt from KPMG Ex 3A/3B: same condition | significant services | presentation and disclosure; id `s-1-ex-ey-scope` kept) · 1.3.2 emission rights & green certificates (+ holding-purpose table) · 1.3.3 NRV vs FV (PwC FAQ 25.8.1; stays in Ch1 because PwC places it under scope 25.8; Ch4 4.2 keeps only a pointer).

**Demoted (FAQ ≠ Illus):** old 1.3.1 BC6–BC8 narrative → dense bullet in 1.3 (`li#s-1-ex-bc-broker`); old 1.4.1 KPMG samples/catalogues → `h4#s-1-ex-kpmg-samples` 1.4.1 + lead + four chipped bullets.

**Chip corrections:** DTT "2" → "2.2" (DTT's scope-exclusion section); PwC "25.11" for the IFRS 15 sentence → "25.14" (where PwC states it); PwC 25.3–25.4 split to the units each supports.

**Ch1 Concept Map (`visuals/ch01-scope.html`) — story + visit path (written before draw):**
- *Story:* An asset is an inventory only if it fits one of the three para 6 classes. An inventory is outside IAS 2 entirely if it is a financial instrument or a biological asset / agricultural produce at the point of harvest (para 2). Every other inventory is IAS 2 inventory, measured at the lower of cost and NRV (para 9) unless para 3 removes only the measurement requirements (NRV producers; broker-traders at FV less costs to sell; changes in P&L) — presentation and disclosure apply either way. *Not the story:* "a sale is someday possible"; a recognition procedure.
- *Visit path:* (1) enter gate 1.1 — asset containment with the three classes joined by **or** (Johnny scope rough); (2) branch — "no" stem → red stop leaf "Not inventories" (spare parts / re-usable packaging → PPE; samples/catalogues expensed; links 1.1.3, 1.1.4, 1.4.1) + IFRS 15 see-also beside it; (3) "yes" stem enters gate 1.2 — two exclusions joined by **or**; (4) "yes" stem → red stop leaf "IAS 2 does not apply" + IAS 41 see-also (link Ch3 3.8); (5) "no — IAS 2 inventory" stem enters the 1.3 containment plate; (6) inside: two neutral peers — lower of cost and NRV (links Ch3 / Ch4) ∥ excluded from the measurement requirements only; (7) spanning bar under both: presentation and disclosure apply to both (link Ch6 6.3).
- *Colour:* red only on the two stop leaves (one-line legend: "IAS 2 does not apply / not inventories"); in-scope peers neutral; accent on the IAS 2 inventory containment (continuing route). Replaced the old green "Yes" gate boxes (visual-grammar: yes/no = stems, leaves = outcomes).
- Mobile (420px): classes stack with centred "or"; fork keeps the stem in a 72px left rail so "yes" still runs down the left into the next gate.

**Carry-forward for later gates (not done here):**
- ~~Ch2 2.1.1 spare parts duplicate → pointer; pipeline lead~~ — done at Gate 3.
- Ch4 4.2 link text "Chapter 1 FAQ box" → "Illustration 1.3.3".
- Pack Map (`map-formula-board.html`) still shows old Ch1 labels ("Full exclusion", "Measurement carve-out") — align at pack-Map gate.
- Ch3 3.8 heading "Deemed cost at harvest" — para 20 wording is "cost … at that date"; Ch1 key term now "Cost at the point of harvest".
- Build notes: iframe dead space (decision 4); `.worked-strip-grid` fixed 3 columns; no gap between strip grid and an in-strip table.

## Johnny approvals (verbatim record)

- **After Gate 1 (relayed by Grok Bot PM — Johnny skipped the continue widget):** "Reply: **continue** to Ch1." + locked decisions 1–4 (recorded under *Decisions / conventions*). Not Johnny's own words; recorded as PM default.
- After Gate 2 (Ch1), 2026-10-01 10:25 UTC — Johnny: "**fix Ch1 before Ch2**. Do NOT start Ch2. Hold at Ch1 gate and wait for specific fix instructions from Grok/Johnny." → **HOLD at Ch1 gate.** No Ch2 work. Awaiting the Ch1 fix list.
- 2026-10-01 10:25 UTC — Johnny: "**Change all** on Ch1 Concept Map — address every issue: 1. Full redraw from Johnny scope rough + visual-grammar (story → visit path → draw). 2. Reduce red stop leaves — red only on true hard stops; do not over-use red. 3. All labels technical-strict IAS 2 wording (no consultancy/flowery). 4. Fix flow logic so it matches IAS 2 (definition → scope exclusions → measurement carve-out peer path correctly). Map only; no Ch2. STOP with desktop+mobile screenshots + ask continue when done." → done (see *Ch1 Map — full redraw*).
- 2026-10-01 — Johnny: "**fix Ch1 Concept Map only** (do not start Ch2; leave body HTML alone unless Map labels require a tiny anchor sync). READ FULL uploads/ifrs-visual-grammar-SKILL.md. Use Johnny rough at pack `visuals/johnny-rough/` — note filenames may be swapped (scope vs cost); use the scope-definition FLOW sketch for this Map, not the cost matrix. Fix wording to **technical-strict IAS 2** labels (no consultancy/flowery). Story first, then learner visit path, then redraw. Keep: inventories definition (para 6 three classes with or); clear yes/no stems; financial instruments / IAS 41 exclusion gate; measurement-carve-out peer vs full IAS 2 path; presentation/disclosure apply; red only on true stop leaves. Work at ~420px iframe width. When done: STOP — screenshots (desktop+mobile Map) + ask continue. Update OPUS-WORKING-MEMORY.md." → done (see *Ch1 Map — r3*).
- 2026-10-01 10:39 UTC — Johnny: "**continue Ch2**. Amend Ch2 Recognition (body + chapter-top Concept Map) per brief/skills/WORKING-MEMORY. Carry forward: spare-parts Illus 2.1.1 → pointer to Ch1 1.1.3; write-once multi-firm; technical-strict titles; FAQ≠Illus; no invent; no densify-down; Map yes/no grammar like Ch1 r3 if redrawing Ch2 Map. STOP at Ch2 gate: status + screenshots + ask continue. Update OPUS-WORKING-MEMORY.md." → done (see *Gate 3 — Ch2 amend log*).
- 2026-10-01 10:56 UTC — Johnny: "Ch2 body OK. Before Ch3, fix Concept Map chrome on **Ch1 and Ch2**: 1. Concept Map **box/iframe size fit** — no odd empty gap / overflow; map content fits the iframe cleanly. 2. **yes / no labels** — place in the **middle of the arrow/stem**, not oddly offset (Johnny finds current location odd). 3. **Bottom fork arrows too short** (「最底嗰個位，個分叉箭嘴好奇快」) — lengthen the T-fork stems at the bottom so the split reads clearly. Apply same stem-label + fork-length grammar to both Ch1 Map r3 and Ch2 Map. Body HTML leave alone unless cache-bust. STOP with desktop+mobile+iframe screenshots for Ch1 and Ch2 Maps; ask continue to Ch3." → done (see *Gate 3b*).
- 2026-10-01 10:56 UTC — Johnny: "after the Map chrome fix (Ch1+Ch2: box fit, yes/no mid-arrow, lengthen bottom fork stems), **continue straight to Ch3** without waiting for another continue. Still take Map-fix screenshots, then immediately amend Ch3 Initial measurement; STOP only at the Ch3 gate (status + screenshots + ask continue)." → Gate 3b screenshots taken; Ch3 started without a stop. **Decision 4 (iframe dead space → Build) is superseded by this unlock.**
- 2026-10-01 11:05 UTC — Johnny reminder HARD: "for **each chapter** (from Ch3 onward, and backfill Ch1–2 if complex units still lack diagrams), after/alongside the chapter-top Concept Map, **consider whether complex main-body content or Illustrations need supplementary visuals** (mini-flows, tables, diagrams) — not Map-only. Many Illus still have zero diagram; add when complexity warrants; peers stay neutral. No invent. Apply on Ch3 now; note in WORKING-MEMORY which Ch1–2 spots still need a visual pass." → applied in Ch3 (see *Gate 4*); Ch1–2 backlog under *Body visual pass — Ch1–2 backlog*.
- 2026-10-01 11:47 UTC — Johnny: "**Continue Ch4.** Sync to Documents later — do NOT wait for sync. Gate rules unchanged: Ch4 body amend (densify preserve, no invent, multi-firm write-once + chips) + Concept Map + supplementary visuals for complex Illus/body; status + screenshots + ask continue when Ch4 gate ready. Accumulate OPUS-WORKING-MEMORY.md. No rush, quality first." → done (see *Gate 5 — Ch4 amend log*). Documents sync not attempted (Johnny: later).

---

## Ch1 Map — full redraw (Johnny "Change all", 2026-10-01)

**Files:** `visuals/ch01-scope.html` (rewritten), `visuals/ias2.css` (old `.scope-tree` / `.fork` block replaced by scoped `.st-*` block; `.classes`, `.or`, `a.thin-link`, `a.bar` kept), `ch01.html` iframe `?v=ias2-ch1-map-redraw-20261001`, `tools/gate_shots.py` set `ch01-map`. Body text unchanged.

**Story (written before draw):** Para 6 — inventories are **assets** in one of three classes (held for sale in the ordinary course; in the process of production for such sale; materials or supplies to be consumed in production or in rendering services). Para 2 — IAS 2 applies to all inventories except financial instruments and biological assets / agricultural produce at the point of harvest: the only true hard stop. What remains is inventory within the scope of IAS 2. Para 3 then splits it into two peers: normally the lower of cost and NRV (para 9); producers at NRV under well-established industry practice and commodity broker-traders at fair value less costs to sell are excluded from the measurement requirements only (changes in profit or loss). Presentation and disclosure apply to both. *Not the story:* "sale someday possible"; measurement carve-out as a stop; a recognition procedure.

**Visit path (forced by geometry):** (1) enter 1.1 plate — Asset bar, "+", three classes joined by "or" (Johnny rough); non-match is a **muted** line inside the plate ("None of the three — not inventories" + links 1.1.3 / 1.1.4 / 1.4.1) with the IFRS 15 see-also beside it; (2) spine stem "meets the definition" from the plate's bottom edge into 1.2; (3) 1.2 gate lists the para 2 exceptions; side exit "excluded" runs from the gate's right edge into the single **red** leaf "Outside the scope of IAS 2" (IAS 32 and IFRS 9; IAS 41) with IAS 41 see-also directly under it; (4) spine stem "not excluded" enters 1.3 "Inventories within the scope of IAS 2", which asks the para 3 question; (5) fork — "no" drops straight to "Lower of cost and NRV" (para 9; links Ch3/Ch4), "yes" runs along the bar to "Excluded from the measurement requirements only" (para 3(a)/(b); changes in profit or loss); (6) spanning bar under both peers: presentation and disclosure requirements apply to both (paras 36–39 → Ch6).

**Issue-by-issue:**
1. *Full redraw from rough:* spine column (left) = Johnny's narrow Asset → Scope exclusion → IAS 2 Inventory stack; fork to two bottom peers exactly as the rough (left peer under the spine, right peer offset right). Side column holds the exit and the measurement-only peer.
2. *Red reduced 2 → 1:* only para 2 exclusion (true hard stop: IAS 2 does not apply). "Not inventories" is muted (missing-route grammar). In-scope peers neutral — the measurement-only exclusion is no longer drawn as a stop. Exit stem muted grey; continuing stems accent.
3. *Technical-strict labels:* "Definition of inventories"; para 6 wording for the three classes; para 8 examples; "Scope exclusions — This Standard applies to all inventories, except:"; "Outside the scope of IAS 2"; "Inventories within the scope of IAS 2"; "Lower of cost and NRV"; "Excluded from the measurement requirements only". Dropped "Is it an inventory asset?", "Full exclusion?", "Measurement carve-out only?", "skip 'lower of', keep the rest", "This route does not enter the formula board".
4. *Flow logic:* definition → scope exclusions → in-scope inventory → para 3 fork into **peers** (lower of cost and NRV ∥ measurement-only exclusion) with disclosure shared. Previous versions drew the para 3 path as a red stop / or as a "which requirements" container; now it is the yes-arm of a para 3 question on the in-scope node.

**Mobile (≤560px):** same three-column tree with a 54px gutter; classes stack with centred "or"; side exit and right peer stay in the right column so the spine never passes through an exit.

*(Superseded by r3 below.)*

---

## Ch1 Map — r3 yes/no question tree (Johnny "fix Ch1 Concept Map only", 2026-10-01)

**Files:** `visuals/ch01-scope.html` (rewritten), `visuals/ias2.css` (`.st-*` block: `.st-list`, `.st-ask`, `.st-out`, `.st-down-mute`, `.leaf.mute`, `.st-exit` sub-grid, `.st-fork-drop`; gutter 72px desktop / 40px ≤560px), `ch01.html` iframe + CSS `?v=ias2-ch1-map-r3-20261001`. Body HTML unchanged (no anchor sync needed — all 11 Map links resolve to existing ids).

**Rough used:** `visuals/johnny-rough/cost-components-matrix-rough.png` (filename swapped — it is the scope-definition FLOW sketch: Asset + three classes → scope exclusion → IAS 2 inventory → two bottom peers).

**Story:** An item is inventories only if it is an asset in one of the three para 6 classes — held for sale in the ordinary course of business, or in the process of production for such sale, or materials or supplies to be consumed in production or in rendering services; otherwise it is not inventories (e.g. major spare parts → PPE; free samples → expense). Inventories that are financial instruments or biological assets / agricultural produce at the point of harvest are outside the scope of IAS 2 (para 2) — the only true stop. Everything else is within the scope of IAS 2. If held by para 3 producers measuring at NRV under well-established practices in those industries, or by commodity broker-traders measuring at fair value less costs to sell, it is excluded from the measurement requirements only; otherwise lower of cost and NRV applies (para 9). Presentation and disclosure apply to both (paras 36–39).

**Visit path:** (1) 1.1 plate: Asset + three classes joined by "or"; (2) **no** (muted stem from the plate's right) → muted leaf "Not inventories" (links 1.1.3, 1.1.4, 1.4.1) + IFRS 15 see-also; **yes** (spine) ↓; (3) gate 1.2 "Is it excluded from the scope of IAS 2?" — Financial instruments **or** Biological assets related to agricultural activity and agricultural produce at the point of harvest; (4) **yes** → (horizontal, from gate edge) the single red leaf "Outside the scope of IAS 2" (IAS 32 and IFRS 9; IAS 41) + IAS 41 see-also under it; **no** ↓; (5) node 1.3 "Inventories within the scope of IAS 2" asks "Is it held by either of the following (para 3)?" — producers (para 3(a) condition) **or** commodity broker-traders (para 3(b) condition); (6) fork: **no** → "Lower of cost and NRV" (para 9; Ch3 / Ch4); **yes** → "Excluded from the measurement requirements only" (changes in profit or loss; paras 3–5); (7) spanning bar: presentation and disclosure requirements of IAS 2 apply to both (paras 36–39 → Ch6).

**Changes vs previous redraw:**
1. Every gate is a real yes/no question; stems labelled **yes** / **no** only ("meets the definition", "excluded" / "not excluded" dropped).
2. Definition now has its own **no** stem to a muted "Not inventories" leaf (was an in-plate line).
3. 1.2 rewritten as a question gate; the two para 2 exceptions joined by "or".
4. 1.3 carries the para 3 question; holder conditions in para 3 wording ("to the extent that they are measured at NRV in accordance with well-established practices in those industries"; "who measure their inventories at fair value less costs to sell"). Peer cells no longer repeat holder text (no route-label/destination repeat).
5. Red = 1 leaf only (para 2). "Not inventories" muted; peers neutral; carve-out drawn as a peer of the full IAS 2 path, never a stop.
6. Exit arrow on its own sub-grid column aligned to the red leaf (no longer lands between leaf and see-also).
7. ≤560px (≈420 iframe): 40px gutter; node 1.3 spans full width with a centred T-fork drop so both peers sit under it.

**Verified:** desktop 1100 element shot, mobile 420 page shot, iframe 420 full shot; `pack_audit.py` broken anchors none; Map link targets all OK.

---

## Gate 3 — Ch2 amend log (2026-10-01)

**Files:** `ch02.html` (article + key terms rewritten; iframe `?v=ias2-ch2-map-r2-20261001`), `visuals/ch02-recognition.html` (redrawn), `visuals/ias2.css` (two `.st` additions: `.st-beside`, `.st-down .stem-label {max-width:100%}`; ≤560px `.st-node + .st-beside` full width), `ch01.html` (one anchor sync: property-transfer link `ch02.html#s-2-3` → `#s-2-1-property`, text "Chapter 2 · 2.1"), `tools/gate_shots.py` set `ch02`. Backup of old body: `/tmp/ch02.orig.html` (session only).

**Sources re-read for Ch2:** PwC MOA 25.9–25.15, 25.42–25.46, FAQ 25.46.1, FAQ 25.46.2; KPMG 3.8.90.10–40, 3.8.100.10–20, Ex 3B; DTT 2.4-1, 3.1, 3.4; Official paras 6, 8, 9, 10, 31, 34, 35, IN14. EY = site text only (section 2.3.1.H).

**QA after amend:** cites 44 → **81** (Official 32 · KPMG 21 · PwC 21 · DTT 5 · EY 2); house-only 0; `§` 0; HKAS on UI 0; title-essence fails 0; flowery heading cues 0; broken anchors 0 (pack-wide + all Map links); Illus 3 → **1** (2 handled per FAQ ≠ Illus / write-once, none deleted); the remaining Illus carries an indicator table.

**Headings (technical-strict):** 2.0 A light chapter on purpose → **Recognition of inventories**; 2.1 When an item enters as inventory → **Items recognised as inventories**; 2.1a Timing — control, shipping terms, principal vs agent → **2.2 Timing of recognition — control** (irregular "2.1a" numbering removed); new **2.3 Consignment stock and reservation of title** (KPMG 3.8.100 / PwC 25.46 heading); 2.2 No second recognition model + 2.3 Handoff → **2.4 Derecognition and recognition as an expense** (PwC heading) + 2.0 "Measurement on initial recognition — at cost" bullet.

**Accuracy fix (Gate 1 flag C):** PwC 25.9 now carries all **three** criteria (control; expects future economic benefits; **cost can be measured reliably**) with PwC's Conceptual Framework paras 4.3 / 4.4 / BC5.1; the "probable plus reliable measurement theatre" sentence (which contradicted PwC) removed.

**Write-once / pointers:**
- Spare parts Illus 2.1.1 → pointer bullet `li#s-2-ex-spare` to Ch1 Illustration 1.1.3 (decision 3), carrying all five chips (PwC 25.10, FAQ 25.10.1, IAS 16 para 8, KPMG 3.8.30, Example 1). Editorial "not a fake 'always inventory' rule" / "not a purchase-order date alone" dropped.
- Pipeline bullet → substance lead ("Pipeline fill — recognised at cost when acquired and classified as inventories") + link Illustration 1.1.1.
- Para 6 classes → folded into the PwC 25.9 criteria unit + link Ch1 1.1 (not re-taught). Para 8 "typical entry events" → 2.1 lead (para 8 + PwC 25.10/25.11/25.14).
- Expense exits / IN14 / "de-recognised when sold" (home Ch5) → one 2.4 pointer unit with all chips (paras 34, 35, IN14; PwC 25.42, 25.43; DTT 3.4). DTT 3.4 chip no longer carries the "de-recognised when sold" claim it did not make.
- Property: home stays Ch2 (Ch1 links here) — PwC 25.12/25.13 + IAS 40 paras 9(a), 57(b) + **DTT 3.1** (IAS 2 applies in its entirety to property for sale / under development for sale). `li#s-2-1-property`.

**FAQ ≠ Illus:**
- Old 2.1.2 consignment: generic PwC narrative (motor trade), IFRS 15 B77/B78 indicators, DTT buyer view, EY cues → section bullets in 2.3; the **PwC retail example** (Manufacturer/Retailer) is the only real case → **Illustration 2.3.1** (id `s-2-ex-consign` kept — Ch5 links it), peers Facts | Control | Manufacturer's inventory + in-strip table *Indicator (IFRS 15 B78) | Facts in this arrangement* (Gate 1 visual-debt item).
- Old 2.1.3 reservation of title (no case facts — general FAQ) → dense bullet `li#s-2-ex-rot` in 2.3.

**Added from pack sources (no invent):** KPMG 3.8.90.15 control "at a point in time or over time"; PwC 25.45 control includes ability to prevent others (IFRS 15 para 33); KPMG 3.8.90.17 indicators "not a list of conditions"; KPMG 3.8.90.20 bill of lading / risk on loading at seller's port; KPMG 3.8.90.25 principal-vs-agent two-step (general control guidance first, then specific indicators) + Ex 3B agent (link Ch1 1.3.1); KPMG 3.8.90.30 shipped-before-loading stays in seller's inventory; KPMG 3.8.90.40 right of return → revenue requirements; KPMG 3.8.100.10 consignment definition; KPMG 3.8.100.20 consignor includes / consignee excludes; DTT 2.4-1 "substantial risks and rewards and legal title" + no buyer-side guidance → IAS 8 + manufacturer does not derecognise on delivery; PwC FAQ 25.46.1 "cleared funds … not to the dealer if already sold on"; PwC 25.15 initial measurement at cost.

**Rebuilt contrast pair (ok / warn, non-Illus):** "Included in the entity's inventory" (FOB in transit; shipped but control not transferred; consignor's goods at another's premises) ∥ "Excluded from the entity's inventory" (items sold even with expected returns; agent goods; consignee goods; firm purchase contracts → IAS 37 para 31; outside definition/scope → Ch1 1.1/1.2 incl. intangibles in use). Dropped "usual exam contrast".

**Removed (unsourced / meta / editorial — no teaching detail lost):** "theatre", "ritual", "five-step entry ritual", "Do not teach a parallel…", "Teach the link to related revenue (IFRS 15), not retired wording"; **Concept insight** point-chip (decision 2 — no locator); warn-note "do not invent an IAS 2 'recognise on shipment' shortcut" (meta; the sourced substance — shipping terms alone do not decide; no derecognition on delivery of consigned goods — is in 2.2 / 2.3); prose firm attributions "(PwC)", "(EY)", "(DTT)", "EY also flags" → chips only; peer label "Exception / warn", "Usual gate"; key terms "No recognition theatre", "Ordinary course — … not a one-off PPE disposal" (unsourced gloss).

**Ch2 Concept Map (`visuals/ch02-recognition.html`) — story + visit path (written before draw):**
- *Story:* Inventory is recognised when three criteria are met together — control of the inventory, expected future economic benefits, and a cost that can be measured reliably (PwC 25.9). IAS 2 is silent on timing, so recognition falls on the date the entity obtains control; the indicators are weighed together, shipping terms and title inform but do not decide, and an intermediary recognises inventory only as a principal. Recognised inventory is measured at cost (Ch3) and is derecognised when control transfers to the customer (2.4 → Ch5). *Not the story:* a recognition procedure; "one recognition idea"; "second recognition ritual"; "Next / handoff".
- *Visit path:* (1) plate 2.0 "Initial recognition of inventory" — "Are all three criteria met?" — three criteria joined by **and**; (2) **no** (muted stem, right) → muted leaf "Not recognised as inventory of the entity" (consignee 2.3; agent, items sold 2.2) + see-also Ch1 (definition and scope exclusions); (3) **yes** (spine) → node 2.2 "Recognised on the date the entity obtains control" (indicators evaluated together — IFRS 15 para 38; shipping terms FOB; intermediary only as principal), see-also *Reservation of title* beside it; (4) unlabelled stem → "Measured at cost on initial recognition" (para 10 → Ch3; then lower of cost and NRV, para 9 → Ch4); (5) stem **"control transfers to the customer"** with see-also *Illustration 2.3.1* (consigned product not derecognised on delivery) beside the stem → node 2.4 "Derecognition and recognition as an expense" (paras 34–35 → Ch5).
- *Colour:* **no red** — Ch2 has no true stop (items not recognised are another entity's inventory or are outside Ch1's definition); "no" leaf muted; continuing nodes neutral; stems accent.
- *Mobile (≤560px / 420 iframe):* criteria stack with centred "and"; nodes 2.2, cost and 2.4 span full width; reservation-of-title see-also drops full width under 2.2; long stem label wraps inside its column.
- `.st-*` is now the IAS 2 decision-tree kit shared by Ch1 and Ch2 Maps (pack-local `ias2.css`; Ch1 unaffected by the two additions).

**Carry-forward:**
- Pack Map (`map-formula-board.html` line ~22) Ch2 pointer wording — align at pack-Map gate.
- Ch5 bullet (ch05.html line ~50) that links `ch02.html#s-2-ex-consign` ("see Chapter 2") → link text "Illustration 2.3.1" at Ch5 gate.
- Ch5 is the home for IN14 / "de-recognise when sold" (Ch2 now points there) — keep at Ch5 gate.

---

## Gate 3b — Concept Map chrome fix, Ch1 + Ch2 (2026-10-01)

1. **Iframe fit (root cause, pack-wide):** `assets/theme.js` (embed notify) and `assets/iframe-fit.js` (parent measure) both took `max(body…, html.scrollHeight, html.offsetHeight) + 12`. `<html>` in an iframe is at least the iframe viewport, so every notify ratcheted the iframe taller and it never shrank — +100–180px dead space on every chapter (measured: Ch1 1137 vs content 1029 at 1280px; Ch6 440 vs 255). Now both measure **body only** (`scrollHeight` / bounding height) with PAD 2. After: iframe − body = 2–3px on all 6 chapters at 1280 / 420 / 360px; horizontal overflow 0. Script tags cache-busted `?v=ias2-fit-20261001` on all chapter pages + all visuals (head only).
2. **Stem labels mid-arrow:** `.st-down` / `.st-arm` `.stem-label` absolutely centred on the shaft (top `calc(50% − 3px)` to discount the head), masked with `var(--bg)` so the line breaks around the word; `max-width:100%` so long labels wrap inside their column. Horizontal exit `.st-h-label` centred on the line the same way (Ch1 "yes" → Outside the scope). Stem min-height 42 → 52; muted stem 30 → 44.
3. **Fork stems longer:** `.st-fork .st-arm` min-height 76px desktop / 64px ≤560px; ≤560px centre drop 12 → 24px (bar at 24px).
- Applied through the shared `.st` kit, so Ch1 r3 and Ch2 use the same grammar. Iframe + `ias2.css` `?v=ias2-map-chrome-20261001`. No body HTML change (cache-bust only).
- Screenshots: `gate3b-mapfix-ch01-concept-map-{desktop,mobile}.png`, `gate3b-mapfix-ch01-iframe-420.png`, same for ch02. Shot set `maps-ch1-ch2`.

---

## Body visual pass — Ch1–2 backlog (Johnny HARD reminder 2026-10-01 11:05 UTC)

Rule (now standing for every chapter gate): alongside the chapter-top Map, check each complex body unit / Illustration for a supplementary visual (mini-flow, in-strip table, small diagram). Peers stay neutral; visuals carry only sourced facts/figures. Audit `vis=` column (`tools/pack_audit.py -v`) flags strips with no table / `.mini-flow`.

Ch1–2 spots still without a visual (as of Gate 4; not changed in this gate — backfill when Johnny reopens Ch1/Ch2, or at the consistency pass):
- **Ch1 Illus 1.1.5** Assets acquired for sale at the end of a lease term (DTT 2.1-1) — three parties + time sequence (lease term → extension → sale) → mini-flow (lessor X / guarantor A / lessee; who holds the asset when).
- **Ch1 Illus 1.1.6** Property leased out briefly before sale (DTT 2.1-4) — IAS 40 para 57(d) two-condition test → mini-flow (evidence of change in use → meets investment-property definition? → reclassify / remains inventory).
- **Ch1 Illus 1.1.3** Spare parts (PwC FAQ 25.10.1 + KPMG Ex 1) — two-way classification by period of use → small table (use · consumed within one period? · classification).
- **Ch1 Illus 1.1.2** Cryptocurrencies (IFRS IC) — classification then measurement branch (held for sale in ordinary course → IAS 2; broker-trader → FV less costs to sell) → mini-flow.
- **Ch1 Illus 1.3.1** Commodities resold in the same condition vs processed (EY / KPMG 3.8.70.30–.35) — contrast table (activity · broker-trader? · measurement).
- **Ch1 Illus 1.3.3** NRV is entity-specific; fair value is not (para 7) — side-by-side formula table (NRV vs fair value less costs to sell inputs).
- Ch1 Illus 1.1.1 pipeline fill, 1.1.4 re-usable bottles — single-gate; visual optional (low priority).
- **Ch2 2.2** Timing — FOB shipping terms (KPMG 3.8.90.20/.30) — mini time strip (seller's warehouse → loading at seller's port → in transit at reporting date → arrival) showing whose inventory at each point; body unit, not an Illus.
- Ch2 Illus 2.3.1 already has the IFRS 15 B78 indicator table — done.

**Cleared in the Ch1–Ch3 debt wave (see that section):** 1.1.1, 1.1.2, 1.1.3, 1.1.5, 1.1.6, 1.3.1, 1.3.3 and the Ch2 2.2 FOB strip all now carry a visual. Only 1.1.4 (re-usable bottles) has none — a single test, and it already links to the 1.1.3 table.

---

## Gate 4 — Ch3 amend log (2026-10-01)

**Files:** `ch03.html` (article + key terms rewritten; `draft.css?v=ias2-ch3-body-vis-20261001`; iframe `?v=ias2-ch3-map-r1-20261001`), `assets/draft.css` (appended neutral body-visual kit: `.vis-title`, `.mini-flow` / `.mini-flow-steps` / `.mini-step` / `.mini-step-head` / `.mini-out` / `.mini-arrow` — stacks vertically ≤720px; `.vis-table td.num`, `.vis-table tr.row-mute`; in-strip table / mini-flow spacing), `visuals/ch03-initial.html` (redrawn on the `.st` kit), `visuals/ias2.css` (6 small rules: `.st > .bar.st-top`, `.st-def .bar`, `a.leaf`, `.st-peer .st-sub`, `.st-sub .leaf-note`, hover), `tools/gate_shots.py` set `ch03`. Backups (session only): `/tmp/ch03.orig.html`, `/tmp/ch03-initial.orig.html`; drafting halves `/tmp/ch03.part{1,2}.html` (cite macros expanded into `ch03.html`).

**Sources re-read for Ch3:** Official paras 9–27, IN10, IN11, IN13, BC9–BC21; PwC MOA 25.5–25.7, 25.15–25.33, FAQs 25.19.1–.7, 25.21.1, 25.22.1, 25.22.3, 25.22.4, 25.25.1–.5, 25.32.1; DTT 3.1, 3.2.1–3.2.8.6-1 (incl. 3.2.2.2-1/-2, 3.2.2.3-1, 3.2.3.1-1/-2, 3.2.3.3-1/-2/-3, 3.2.4.2-1/-2, 3.2.4.3-1, 3.2.4.5-1, 3.2.4.6-1, 3.2.7-1, 3.2.8.4-1, 3.2.8.5-1); KPMG 3.8.110–3.8.320 (`kpmg-3.8-extract.txt`). EY = site chips/text only (21 EY chips before and after, same units).

**QA after amend:** cites 202 → **438** (Official 172 · KPMG 107 · PwC 69 · DTT 69 · EY 21); house-only 0; `§` 0; official/KPMG/PwC/DTT/EY chip oddities 0; HKAS on UI 0; title-essence fails 0; flowery heading cues 0; plain "see N.M" 0; broken anchors 0 pack-wide (all inbound `ch03.html#s-3-1 … #s-3-10`, Map, pack Map, Ch1/Ch2/Ch4 links resolve); point-chips 2 → 0. Illus strips 41 → **28**; strips with a table or mini-flow 3 → **14**; tables 8 → 24; mini-flows 0 → 5. THIN: only **3.5.2** (DTT 3.2.4.2-1 is a two-sentence source — documented source-short, not padded). Iframe fit: 1050 vs body 1047 (1280px), 1553 vs 1551 (420px).

**Headings (technical-strict, IAS 2 sub-headings):** 3.0 **Measurement of inventories** (new; para 9 + KPMG 3.8.110 exceptions); 3.1 **Cost of inventories**; 3.2 **Costs of purchase**; 3.3 "Costs of conversion and normal capacity" → **Costs of conversion**; 3.3b "Learning curve costs" h3 → h4 under 3.3 (id `s-3-3b` kept); 3.4 **Joint products and by-products**; 3.5 **Other costs**; 3.6 "Excluded from cost" → **Costs excluded from the cost of inventories**; 3.7 "Financing and borrowing costs" → **Borrowing costs and deferred settlement terms**; 3.8 "Deemed cost at harvest (IAS 41 hand-off)" → **Cost of agricultural produce harvested from biological assets**; 3.9 "Techniques that only approximate cost" → **Techniques for the measurement of cost**; 3.10 "Cost formulas — assignment, not a flow theatre" → **Cost formulas**. Unnumbered h4: Types of cost included…or expensed; Discounts and rebates; Variable payments for the purchase of inventories; Allocation of fixed production overheads — normal capacity; Restricted operating periods, planned shut-downs and interruptions; Classification and allocation of overheads; Right-of-use assets and lease costs in the production of inventory; Learning curve costs; Distribution, packaging and transport costs; Borrowing costs; Deferred settlement terms and long-term prepayments; Prohibition of LIFO.

**Accuracy fixes:**
- PwC FAQ 25.19.1 (`li#s-3-ex-pwc-rebate`): only the PwC sentence "Rebates that specifically and genuinely refund selling expenses are not deducted from the cost of inventories" — invented "often P&L" line removed.
- IFRS 9 chips on 3.2.7–3.2.9 corrected to the paras PwC cites (4.3.3, 5.7.1, 4.3.1, B4.3.4).
- 3.3.4 PwC FAQ 25.22.1 arithmetic laid out exactly as PwC (closing 1,380; COGS 4,200 × C0.6 = 2,520; unabsorbed 200; total 2,720).
- Normal-capacity presentation: PwC (idle capacity in cost of sales) and KPMG (by function / "other expenses" by nature, IAS 2 para 38) shown side by side, attributed — not merged.
- Old Illus 3.3.3 combined DTT televisions + KPMG coffee machines in one strip → two Illustrations (3.3.1 DTT, 3.3.2 KPMG Example 5), each with its own facts and table.
- Old 3.3.10 interruption box "Do not accrue second-half maintenance…" belonged to KPMG 3.8.190.80 (planned shut-down), not 3.8.210 → now in its own Illustration 3.3.5 (Company F); "abnormal idle capacity remains an expense (same family…)" dropped (not in KPMG 3.8.210).
- Old 3.6.1 storage "contrast: finished bottled stock…", "Do not capitalise warehouse rent…" (not in PwC FAQ 25.25.3) removed; KPMG 3.8.240 exceptions added instead.
- Old 3.10.1 "formula choice moves profit…", 3.9.3 "formula choice changes how much variance stays…", 3.10.4 "Show LIFO in teaching only" removed (not in source).
- Base stock: KPMG 3.8.310 in full (PPE if used > one period; otherwise inventory, lower of cost and NRV).

**FAQ ≠ Illus — demoted to bullets / h4 (ids kept, so inbound links still land):** `s-3-ex-dtt-direct-marginal`, `s-3-ex-pwc-211` (normal-capacity factors + KPMG 3.8.190.20), `s-3-ex-kpmg-interrupt` (+ interruption table), `s-3-ex-pwc-224`, `s-3-ex-dtt-oh-alloc`, `s-3-ex-dtt-xfer` (moved 3.4 → 3.3, it is a conversion-cost point), `s-3-ex-dtt-distrib` (h4 + table), `s-3-ex-pwc-251` (+ deferred-terms table), `s-3-ex-dtt-borrow`, `s-3-ex-kpmg-basestock`, `s-3-ex-lifo` (h4), `s-3-ex-dtt-formula-change`, `s-3-ex-pwc-rebate`, `s-3-ex-dtt-fx`, `s-3-ex-dtt-wastage`, `s-3-ex-pwc-252` (h4 + PwC table). New Illus ids: `s-3-ex-kpmg-oh` (3.3.2), `s-3-ex-kpmg-shutdown` (3.3.5).

**Added from pack sources (no invent):** KPMG 3.8.110.20/.30 exceptions; 3.8.120; 3.8.130.20 several assets; 3.8.140 sales tax; 3.8.150.10–.30 cash price equivalent / normal credit terms; 3.8.155 IU 11-15; 3.8.160.20–.70 rebate timing + Ex 4A/4B; 3.8.170.10 software amortisation, labour taxes, not external/incremental; 3.8.170.20 impairment / finance department; 3.8.180 decommissioning; 3.8.190.10–.90 (presentation, factors, Ex 5, revision, Company F shut-down); 3.8.200 common costs; 3.8.205 / Ex 6A; 3.8.208 / Ex 6B; 3.8.210; 3.8.215 learning curve (all three paras); 3.8.220.10–.20; 3.8.230 distribution / packaging; 3.8.240 storage; 3.8.250 grappa / same margin; 3.8.260.10–.20 (IU 03-19); 3.8.270; 3.8.280–3.8.320 (incl. 3.8.315 minimum levels, 3.8.320.40/.50). PwC 25.20 (direct expenses, sub-contracted work, business rates), 25.22 presentation, 25.23 wine/whisky/cheese + "can still capitalise", 25.24 "to the extent recoverable", 25.26 "more generous than normal trade terms" + prepayment, 25.32 "more up-to-date prices". DTT 3.2.3.1 share-based payment, 3.2.3.2 direct labour, 3.2.3.3 revaluation-model depreciation, 3.2.4.3 qualifying assets, 3.2.7 standard cost / retail, 3.2.8.1 standard costs at year end, 3.2.8.4 computer systems, retail-method constraints (newsagent and confectioner; marked-down items). Official para 12–27 quotes in full; BC10–BC20 reasoning.

**Removed (unsourced / meta / editorial):** point-chips "Why normal capacity" and "Trap: capitalise every factory invoice"; peer labels "Gate", "Usual gate / expense", "Exception / capitalise", "Teaching", "Related traps", "Peer arithmetic"; "not a flow theatre"; "not peers of NRV"; "Specific identification is not an invitation…" (para 24 quoted instead); 3.3b "Firm view" / "Teaching cue"; 3.3.9 "Gate" box and "not an automatic P&L label"; 3.5.3 "dumps" / "same gate"; 3.7 see-also "Tip sits on 'other costs'…"; "Columns match Inform" meta line; one-line "Same …" peer bullets (DTT/PwC chips folded into the full units).

**Body visuals added (Johnny 11:05 rule):** mini-flows — 3.2.2 refund recognition and allocation; 3.3.5 Company F reporting period; overhead identification → allocation → normal activity (3.3 h4); 3.4 joint process → separable → allocation / by-product NRV; 3.8 biological asset → point of harvest → after harvest. Tables — 3.1 components of cost (paras 10–22); variable-payable matrix (3.2.7–3.2.9); 3.2.3 beds; 3.2.4 once-a-year rebates; 3.2.10 forward contract; normal-capacity levels; 3.3.1 televisions; 3.3.2 coffee machines; 3.3.3 overhead computation; interruptions; distribution / packaging / transport; deferred-settlement terms; 3.9.1 retail; 3.10.2 purchases + FIFO layers; 3.10.3 batches; FIFO vs weighted average closing inventory across 3.10.1–3.10.3. All neutral tokens; source columns carry cite chips.

**Ch3 Concept Map (`visuals/ch03-initial.html`) — story + visit path (written before draw):**
- *Story:* Inventories are measured at the lower of cost and NRV (para 9); this chapter is the cost side. Cost of inventories is one amount — all costs incurred in bringing the inventories to their present location and condition (para 10): costs of purchase (11) + costs of conversion (12–14) + other costs (15), with borrowing costs only in IAS 23's limited circumstances (17). Harvested produce takes fair value less costs to sell at harvest as cost (20); standard cost / retail method may stand in if they approximate cost (21–22). Costs that do not bring inventories to present location and condition are excluded and expensed (16); a financing element is interest expense (18). Cost is then assigned to items: specific identification for items not ordinarily interchangeable / segregated for specific projects (23–24); otherwise FIFO or weighted average, same formula for similar nature and use (25–27); LIFO not permitted (IN13). *Not the story:* containment "arms", "missing route", "flow theatre".
- *Visit path:* (1) thin bar 3.0 — para 9, NRV → Ch4; (2) plate 3.1 "Cost of inventories" — para 10 line — three component cells joined by **+** (3.2 / 3.3 with 3.4 link / 3.5) — dashed see-also IAS 23 → `#s-3-7-borrowing` — two bars 3.8 harvest, 3.9 techniques; (3) spine stem **"assigned to items"**; side muted stem **"excluded"** → muted leaf "Not in the cost of inventories — expenses when incurred" (para 16 → 3.6; para 18 → 3.7); (4) node 3.10 "Cost formulas" — para 23 question; see-also beside it: changing cost formula = change in accounting policy; (5) fork **yes** → Specific identification (paras 23–24) ∥ **no** → FIFO or weighted average (paras 25–27) with nested muted dead-end "LIFO — not permitted (IN13; BC9–BC21)" → `#s-3-ex-lifo`.
- *Colour:* **no red** — Ch3 has no true stop leaf; exclusions and LIFO muted; stems accent; dashed only for the two see-alsos.
- *Mobile (420 iframe):* component cells stack; exit leaf stays in the right column under its muted stem; node 3.10 and its see-also go full width; fork uses the centre drop.

**Carry-forward:**
- Ch1 h4 "1.4.1" numbering inconsistency (Ch3 h4s are unnumbered) — consistency pass.
- Pack Map (`map-formula-board.html`) Ch3 cell wording ("Purchase", "Conversion", "Other", LIFO) — align with the new Ch3 Map labels at the pack-Map gate.
- Ch4 4.1 / Ch5 links into Ch3 all land on `#s-3-1`; Ch4 may want `#s-3-3-capacity` (unallocated overheads) or `#s-3-10` — check at Ch4 gate.
- KPMG Example 7A / 7C tables (numbers) are site text — the extract has the headings but not the tables; kept as on site.
- Ch1–2 body-visual backlog above still open.

---

## Gate 5 — Ch4 amend log (2026-10-01)

**Files:** `ch04.html` (article + key terms rewritten; `draft.css?v=ias2-ch4-body-vis-20261001`; iframe `?v=ias2-ch4-map-r4-20261001`), `assets/draft.css` (+ `.mini-op` operator cell for formula mini-flows, 26px / 24px ≤720px), `visuals/ch04-subsequent.html` (redrawn on the `.st` kit), `visuals/ias2.css` (block scoped `.st-nrv` + `.st-fork-c`: span chip `span.fb-num` for chips inside link cells — nested `<a>` avoided; `.eq` weighting .85fr / 1.5fr; `.arm-lite`; `.nrv-f` / `.nrv-term` / `.nrv-minus` formula row; `.nrv-ask`; `.cells.g3`; hover; centred fork drop on desktop; stacks ≤800 / ≤720 / ≤520), `tools/gate_shots.py` set `ch04`. Backup (session only): `/tmp/ch04.orig.html`; macro source `/tmp/ch04.draft.html` → `/tmp/expand_cites.py` → `ch04.html` (exits on any leftover macro).

**Sources re-read for Ch4:** Official paras 6, 7, 9, 28–34, IN15, IAS 10 para 9(b) (as PwC cites it); PwC MOA 25.15, 25.34–25.41, FAQs 25.8.1, 25.22.4, 25.36.1, 25.39.1, 25.40.1; DTT 3.3, 3.3.1 (incl. 3.3.1-1 … -4), 3.3.2 (incl. 3.3.2-1, IFRIC June 2021), 3.3.3; KPMG 3.8.330–3.8.390 (Examples 9–16). EY = site chips/text only (9 EY chips before and after, same units; no EY substance added).

**QA after amend:** cites 99 → **216** (Official 43 → 81 · PwC 11 → 38 · DTT 12 → 35 · KPMG 24 → 53 · EY 9 → 9); house-only 0; `§` 0; chip oddities 0; HKAS on UI 0; title-essence fails 0; flowery heading cues 0; plain "see N.M" 0; broken anchors 0 pack-wide. Point-chips 3 → 0. Illus strips 18 → **15**; strips with a table or mini-flow 1 → **12** (the 3 without — 4.2.1 EY, 4.5.10 KPMG Ex 16, 4.7.2 EY — have no numbers in source); tables 2 → 16; body mini-flows 0 → 5 (+ 2 in strips). THIN: none. Iframe fit: 1021 vs body 1019 (1280px), 1749 vs 1747 (420px).

**Headings (technical-strict):** 4.0 "This is the home of the identity" → **Measurement of inventories**; 4.1 "The lower-of rule" → **Net realisable value**; 4.2 "NRV is not fair value" → **Net realisable value and fair value**; 4.3 "When cost may not be recoverable" → **Circumstances in which the cost of inventories may not be recoverable**; 4.4 "Unit of account — usually item by item" → **Item by item and groups of similar or related items**; 4.5 "Evidence, and what the inventory is for" → **Estimates of net realisable value**; 4.6 "Materials held for production" → **Materials and other supplies held for use in production**; 4.7 "Reversals are required — and capped" → **Reversal of write-downs**. Unnumbered h4: Costs necessary to make the sale (`s-4-ex-costs-sell`); Write-down formulas (`s-4-ex-formula`); Events after the reporting period (`s-4-5-events`); Purpose for which the inventory is held — intended use (`s-4-5-purpose`); Firm sales contracts (`s-4-5-contracts`).

**Illustrations (15, renumbered in order):** 4.2.1 EY PE 3-1 AngloGold (`s-4-ex-ey-anglogold`; EY text kept, meta line removed); 4.3.1 KPMG Ex 14 FX (`s-4-ex-kpmg-fx-nrv`, + table); 4.5.1 DTT 3.3.1-2 sale below cost (`s-4-ex-post`, + table); 4.5.2 KPMG Ex 13 (`s-4-ex-kpmg-post`, **new id** — split out of old 4.5.1, + mini-flow); 4.5.3 DTT 3.3.1-3 developer (`s-4-ex-dev`, + table); 4.5.4 PwC FAQ 25.39.1 car models (`s-4-ex-pwc-post`, + mini-flow); 4.5.5 DTT long cycle (`s-4-ex-long`, + table); 4.5.6 KPMG Ex 11A/11B (`s-4-ex-kpmg-intended`, + table); 4.5.7 KPMG Ex 12 (`s-4-ex-kpmg-oploss`, + table); 4.5.8 DTT 3.3.1-4 printers (`s-4-ex-firm`, + table); 4.5.9 KPMG Ex 15 (`s-4-ex-kpmg-firm15`, was 4.5.3b, + table); 4.5.10 KPMG Ex 16 (`s-4-ex-kpmg-firm-deriv`); 4.6.1 PwC FAQ 25.40.1 (`s-4-ex-pwc-mat`, + stage table + NRV table); 4.7.1 KPMG Ex 9 (`s-4-ex-d`, rebuilt, + table); 4.7.2 EY PE 3-2 CRH (`s-4-ex-ey-crh`, stays after reversals as EY places it).

**Accuracy fixes:**
- **4.7.1 (`#s-4-ex-d`) — locked decision 1:** old unsourced strip (Year 2 "70 to 90" peers) replaced by KPMG Example 9 only — 100 → 95 → 103, reversal 5, carrying amount 100. Anchor kept.
- **4.4.1 (`#s-4-ex-a`) — locked decision 1, GAP:** no sourced numeric item-by-item example exists in Official / PwC / DTT / KPMG text. Unsourced SKU strip removed; anchor `#s-4-ex-a` now sits on the sourced "Basis for writing inventories down to NRV" table (para 29, PwC 25.36, DTT 3.3.1/3.3.2, KPMG 3.8.340.10–.30). GAP noted here and for KEY CHANGES — not on the UI.
- 4.5.3 table: 31 March "costs incurred to date" cell said CU20m (not in DTT) → "—".
- 4.5.7 chip para 30 → **para 31** (KPMG cites IAS 2.31 for intended use).
- DTT 3.3.1-1 chip on the broker-trader bullet was mis-located → PwC FAQ 25.8.1 + para 3(b).
- 4.5.2 conclusion trimmed to KPMG 3.8.360.10 wording (dropped my "even though the estimate was 110" link clause).
- 4.6.1 conclusion trimmed to PwC's result (NRV at stage 1 = 180); dropped a derived "150 below 180 → stays at cost" line PwC does not state.

**FAQ ≠ Illus — demoted (ids kept):** DTT 3.3.2-1 costs to sell / IFRIC June 2021 → h4 `s-4-ex-costs-sell`; PwC FAQ 25.36.1 write-down formulas → h4 `s-4-ex-formula` (+ mini-flow); KPMG Ex 10 excess materials → bullet `li#s-4-ex-kpmg-excess` in 4.6; KPMG Ex 16 onerous-contract box → body bullet in *Firm sales contracts*.

**Added from pack sources (no invent):** PwC 25.34 (irrecoverable cost charged as expense), 25.35 (marketing-strategy loss; production / purchasing error), 25.38 onerous contracts, 25.40 parts / sub-assemblies / on order, FAQ 25.22.4 (distribution costs in NRV), IAS 10 para 9(b); DTT 3.3.1 (binding contracts; management considers all facts), 3.3.2, 3.3.3 obsolescence on long-held items; KPMG 3.8.330.10 (costs of sale incl. marketing and distribution), 3.8.335.10/.20, 3.8.340.20 (textiles) / .30 (department stores), 3.8.350.10/.25/.30 (operating losses no automatic write-down), 3.8.360.10, 3.8.370 (lower replacement cost), 3.8.380 FX, 3.8.390.10/.50/.60/.70 (sales commitment derivatives; contract below cost of fulfilling).

**Removed (unsourced / meta / editorial):** point-chips "Why a ceiling", "Why reversals exist", "Cross-GAAP trap … US GAAP" (locked decision 2); 4.0 editorial lead ("home of the identity"); Conceptual Framework see-also and IAS 37 see-also (IAS 37 now in the firm-contracts table); "Same …" duplicate bullets (chips folded into the full units); meta lines "Teaching", "Teaching cue", "Do not invent hedge maths", "EY places …"; 4.5.10 "Reason …" line.

**Body visuals added (Johnny 11:05 rule):** tables — 4.0 result of the comparison (cost / NRV / reversal → carrying amount, P&L, paras, section); 4.2 NRV vs fair value; 4.3 circumstances (para 28, PwC 25.35, KPMG FX / operating losses) with source column; 4.4 basis for writing down; 4.5 firm-contracts quantity → NRV / accounting. Mini-flows — 4.1 NRV formula (selling price − completion − costs to sell = NRV, `.mini-op`); write-down formulas; para 30 event → confirms condition? → NRV at reporting date; 4.6 decline in materials price → finished products at/above cost? → materials; 4.7 write-down → each subsequent period → reversal. All neutral tokens; peers neutral.

**Ch4 Concept Map (`visuals/ch04-subsequent.html`) — story + visit path (written before draw):**
- *Story:* After initial recognition, inventories are measured at the lower of cost and NRV (para 9). Cost is the Ch3 amount (para 10) assigned by specific identification / FIFO / weighted average (23–27). NRV is estimated selling price − estimated costs of completion − estimated costs necessary to make the sale (para 6); entity-specific, may not equal fair value less costs to sell (7). NRV estimates use the most reliable evidence incl. events confirming period-end conditions (30), the purpose for which inventory is held — firm contracts at contract price, IAS 37 for excess contracts (31) — and materials are not written down if the finished products sell at or above cost (32). The comparison is item by item or by groups of similar/related items, never a classification or segment (29). Cost may not be recoverable (28) → yes: written down to NRV, expense (34, Ch5); no: stays at cost. Each subsequent period a new assessment; reversal capped at the original write-down (33), recognised as a reduction in inventories expense (34, Ch5).
- *Visit path:* (1) board 4.0 para 9 — arm 3.1 **Cost** (lighter; two cells → Ch3 `#s-3-1`, `#s-3-10`) | **lower of** | arm 4.1 **NRV** (three-term formula with − operators; dashed see-also 4.2 fair value); full-width row "Estimates of NRV take into consideration:" — 4.5 evidence (`#s-4-5-events`), 4.5 purpose (`#s-4-5-contracts`), 4.6 materials; bar 4.4 para 29; (2) stem **compared**; (3) node 4.3 "Is NRV lower than cost?" with para 28 circumstances; (4) centred fork **no** → "Measured at cost" (para 9) ∥ **yes** → "Written down to NRV" (para 34 → Ch5 `#s-5-2`); (5) stem **each subsequent period** from the yes leaf → plate 4.7 "Reversal of a write-down" (para 33 + para 34 → Ch5 `#s-5-3`).
- *Colour:* **no red** — no true stop in Ch4; stems accent; dashed only for the fair-value see-also.
- *Mobile (420 iframe):* arms stack, formula terms stack with centred −, three NRV cells stack, fork keeps the centre drop.

**Source-short (documented, not padded):** 4.5.2 KPMG Ex 13 (two source sentences + 3.8.360.10 rule); 4.5.10 KPMG Ex 16 (no numbers in source — no table).

**Carry-forward:**
- **Ch5 / Ch6 dependents of removed numbers** (fix at their gates): `ch05.html` ~l.58 "item-by-item SKU strip: Dr expense 10" → `#s-4-ex-a` (no numbers now); `ch05.html` ~l.69 "Year 2 … 70 to 90" → `#s-4-ex-d` (now KPMG Ex 9: 95 → 103, reversal 5); `ch06.html` ~l.235 "Tie back" chip to Ch4 strips.
- Pack Map (`map-formula-board.html`) Ch4 labels "Recovery ceiling", "Reversal, capped", Conceptual Framework see-also → align with the Ch4 Map labels at the pack-Map gate.
- Ch1 link text pointing to "4.2" — check wording at consistency pass (target `#s-4-2` still resolves).
- Ch3 carry-forward "Ch4 links into Ch3" — resolved: Ch4 now links `#s-3-1`, `#s-3-10`, `#s-3-ex-dtt-distrib`, `#s-3-ex-dtt-fx` ("Chapter 3 · 3.2").
- Ch1–2 body-visual backlog still open.

**Gate 5 screenshots:** `/opt/cursor/artifacts/screenshots/gate5-ch04-*.png` (17: Map desktop + mobile; 4.0–4.1, 4.2, 4.3, 4.4 + formulas, 4.5 events, 4.5 contracts, 4.6, 4.7, key terms; Illus 4.5.2, 4.5.3, 4.5.6, 4.5.9; mobile Illus 4.6.1, 4.7.1).

---

## Johnny instruction 14:18 (via PM) — recorded verbatim intent

"Johnny decided: Fix Map yes/no labels FIRST, then do Ch5. One continuous run; stop only when BOTH are done (checkpoint for Johnny)."
- **Step A:** put **yes** / **no** "centered mid-arrow on EACH branch of the fork — one label per outgoing branch arrow, not on the stem into the decision diamond/node"; every yes/no fork ch01–ch06 + any shared map. "Keep Decision-diamond / fork visual grammar from ifrs-visual-grammar; do not invent new decision logic — label placement + arrow length/centering only unless a fork is structurally broken." Use **Decision**, NOT "Gate" — "Do not introduce 'Gate' in HTML/labels/comments Johnny sees." Screenshots `map-yesno-ch0N-desktop.png` (+ mobile).
- **Step B:** Ch5 full Opus pass — read ifrs-teaching-body + -qa + ifrs-visual-grammar fully; densify, no invent, no thin unique detail; FAQ ≠ Illustration; worked-strip for numeric/multi-gate; chips no §; peers neutral; write-once + multi-firm chips; technical-strict titles; Ch5 Map uses the Step A rule; Official + all Big4 in pack; fix stale Ch4 cross-refs; self-QA. Screenshots `checkpoint-ch05-*.png`.
- **Stop:** short KEY CHANGES + screenshot paths + deferred debt. **Do NOT auto-start Ch6.** Model stays Claude Opus 5.5 high. Sync to Documents is not Opus's job.

## Step A — Map yes/no labels (DONE)

- **Pattern (`visuals/ias2.css`):** unlabelled drop from the decision node → horizontal bar → one equal-length arm per outcome, each arm carrying its own label at mid-arm (same y on both arms). `.st-fork` (centred drop, full-width decision node); `.st-fork-l` (drop from column-1 centre); `.st-arm-mute` / `.st-fork-mute3` (dashed outcome arm / bar half); `.st-col` + `.st-tail` carry a continuing column-1 route down beside a column-3 outcome stack. Old `.st-fork-c` and mobile drop overrides removed.
- **Files:** `visuals/ch01-scope.html`, `ch02-recognition.html`, `ch03-initial.html`, `ch04-subsequent.html` (+ `ch01–ch04.html` iframe `?v=ias2-map-yesno-20261001`); comments "Gate question" → "Decision question"; aria-labels "Decision: …".
- **Not changed:** `visuals/map-formula-board.html` (pack Map) has no yes/no fork (one question, three outcomes) — comment now "Decision: …"; Ch6 Map has no fork. `assets/shared.css` `sh-gate` start-here component naming is Build-owned site-wide — left untouched (not visible text).
- **Screenshots:** `/opt/cursor/artifacts/screenshots/map-yesno-ch0{1,2,3,4}-{desktop,mobile}.png`.

## Checkpoint — Ch5 amend log (Step B, DONE)

**Files:** `ch05.html` (body + head; draft `/tmp/ch05.draft.html`, backup `/tmp/ch05.orig.html`); `visuals/ch05-derecognition.html` (redrawn; backup `/tmp/ch05-derecognition.orig.html`); `visuals/ias2.css` (`.st-exp` block; `.st-nrv span.fb-num` → `.ias2 span.fb-num`; `.gate-body` removed); `tools/gate_shots.py` (`SHOT_SETS["ch05"]`); `IAS2-CH05-CONTENT-NOTES.md`.

**Sources used:** Official IAS 2 paras 9, 28, 29, 33, 34, 35, 36(d)–(g), 38 (pointer), IN14, IN15; IFRS 15 paras 31, 33, 38, B77. PwC MOA 25.42, 25.43, 25.45, 25.46, FAQ 25.42.1, FAQ 25.46.1, FAQ 25.46.2. DTT iGAAP 2022 A11 3.3.2, 3.3.3, 3.4, 2.4-1, 4.2.5. KPMG 3.8.90.30, 3.8.90.40, 3.8.100.20, 3.8.335.10/.20/.30/.40, 3.8.400.50/.70/.80, Example 17. EY: kept existing chips only (section 1 on IN14; section 5 on Illus 5.3.1 and the Ex 17 pointer) — no EY substance added.

**QA:** cite chips 38 → 93 (Official 35, PwC 22, DTT 12, KPMG 21, EY 3); Illus 2 → 1 (5.3.2 demoted to pointer, locked decision 3); 0 house-only / § / odd chips / HKAS / THIN / broken anchors / unlinked "see N.M"; title-essence and flowery checks clean; iframe fit 1280: 638/635, 420: 1072/1070. No "Gate" in Ch5 HTML or Map.

**Headings (technical-strict):** 5.0 Recognition as an expense · 5.1 Inventories sold · 5.2 Write-downs to net realisable value and losses of inventories · 5.3 Reversals of write-downs · 5.4 Inventories allocated to other assets. Illus 5.3.1 "Presentation of the reversal of a write-down of inventories and its tax effect" (peers Facts | Requirement | Conclusion + table).

**Removed (invent / meta / stale):** 5.1 "80 of carrying amount" Dr/Cr entry; 5.2 "item-by-item SKU strip: Dr expense 10" (stale Ch4 ref); 5.3 "Year 2 … 70 to 90" (stale Ch4 ref) — both replaced by KPMG Ex 9 via Illus 4.7.1 (100 → 95; NRV 103 → reversal 5); 5.4 Dr PPE entry and IAS 16/IAS 38 see-also; "Concept insight" point-chip (locked decision 2); "Usual gate" peer → "Requirement"; "not a new income category" / "capped … selling above original cost does not create extra reversal" (not in sources); "Same …" duplicate bullets; 5.0 "not a calendar" editorial.

**Added (sourced):** DTT 3.4 amount-recognised-as-expense composition; PwC 25.45 control + benefits list (a)–(f); KPMG 3.8.90.30 "derecognition depends on the timing of revenue recognition" + 3.8.90.40; PwC 25.46 complex transactions; consignment derecognition consequence (DTT 2.4-1, KPMG 3.8.100.20, PwC FAQ 25.46.1 — sold to consumer or lost/damaged); PwC 25.42 no future economic value → derecognise; PwC 25.42 reversal "amount of inventories is increased accordingly … offset"; KPMG 3.8.400.70 cost-of-sales view; KPMG 3.8.400.80 + Ex 17 pointer (li `#s-5-ex-kpmg-rev17` kept for Ch6 inbound links) → Ch6 Illus 6.4.1; PwC 25.43 derecognised when incorporated in cost of construction; DTT 3.4 used rather than sold → depreciation.

**Body visuals:** 5.0 mini-flow (sold + write-downs and losses − reversals = amount recognised as an expense → Ch6 6.4); 5.0 table by event (inventories / profit or loss / IAS 2 / section); 5.1 mini-flow (control → revenue → derecognised; not yet transferred → still inventory); 5.4 mini-flow (used rather than sold → incorporated in cost of other asset → expense through depreciation); Illus 5.3.1 table (C12,000 cost of sales; C3,600 tax line).

**Ch5 Concept Map — story + visit path:**
- *Story:* Inventories are carried at the lower of cost and NRV (para 9). When the customer obtains control (IFRS 15 paras 31, 33) they are sold and derecognised, the carrying amount expensed in the period the related revenue is recognised (para 34); otherwise they remain the entity's inventory (e.g. consignment — Ch2). The period's amount recognised as an expense is sold + write-downs and losses − reversals (limited to the original write-down, para 33), often referred to as cost of sales (para 38), disclosed under para 36(d)–(g). Inventories allocated to another asset become part of its cost and are expensed over its useful life (para 35).
- *Visit path:* top bar 4.0 (→ Ch4) → Decision 5.1 "Has control of the inventories transferred to the customer?" + IFRS 15 ask + nested see-also (Ch2 2.3) → centred fork **yes** (c1) / **no** (c3), labels mid-arm → leaves "Sold — inventories derecognised" / "Still the entity's inventory" → stems "carrying amount sold" / "write-downs, losses, reversals" → board 5.0 formula 5.1 + 5.2 − 5.3 = 6.4 → bar 5.4.
- *Colour:* no red (no true stop); no fork arm muted (the no outcome is not a dead end).

**Deferred debt (not Ch5):**
- Ch6: Illus 6.4.1 should absorb the Ex 17 stage table; its "Full teaching path … Illus 5.3.2" link and 6.4 bullet label "Illus 5.3.2" now point to a Ch5 body pointer (circular) — fix at the Ch6 gate; Ch6 6.4 bullets on para 38 / 3.8.400.70 become pointers or stay as home (write-once decision at Ch6); invented "cap … above original cost" line in 6.4.1 Presentation cue; Ch6 "Tie back" chip (10 / 20) at ~l.235.
- Pack Map (`map-formula-board.html`) Ch5 panel: "Thin route" + IAS 16 / IAS 38 see-also, and Ch4 labels — align at the Pack Map gate.
- `ch03` Illus 3.5.2 `#s-3-ex-dtt-amenity` flagged THIN by audit (5 li) — pre-existing; review at consistency pass.
- Ch1–2 body-visual backlog; Ch1 h4 numbering; 4.4.1 GAP; `shared.css` "gate" naming (Build-owned).

**Checkpoint screenshots:** `/opt/cursor/artifacts/screenshots/checkpoint-ch05-*.png` (Map desktop + mobile; 5.0; 5.1; 5.2–5.3; Illus 5.3.1; 5.4 + key terms; mobile Illus 5.3.1; mobile 5.0 mini-flow).

## Johnny — Ch6 instruction (verbatim)

"Johnny: Continue to **Ch6** NOW. Interrupt any screenshot-only idle work. ## HARD Full Opus Ch6 pass (same standard as Ch1–Ch5). READ ifrs-teaching-body + QA + visual-grammar. - Densify; no invent; FAQ≠Illus; worked-strip; cite chips no § (IAS 2 · para; EY section); Illus peers neutral; write-once + multi-firm chips; Decision/Test/Assessment wording (no Gate). - Fix deferred debt from Ch5 notes: Illus 5.3.2 stale links; take KPMG Ex17 into Illus 6.4.1 (drop unsourced cap-above-cost); clean Tie-back chip issues; pack Map Ch5/Ch4 label debt if in scope. - Concept Map Ch6 with yes/no mid-branch if forks exist. - Self-QA; screenshots checkpoint-ch06-*.png. - STOP when Ch6 done — do NOT auto Ch7. KEY CHANGES + screenshot paths. Sync not your job."

(Preceded by: "Do NOT start Ch6 … Only: re-save / re-list the checkpoint screenshots … Confirm paths in a one-line KEY note" — done, all 17 files present; no HTML edits.)

## Checkpoint — Ch6 amend log (DONE)

**Files:** `ch06.html` (body; draft `/tmp/ch06.draft.html`, backup `/tmp/ch06.orig.html`); `visuals/ch06-disclosure.html` (redrawn on the `.st` kit; backup `/tmp/ch06-disclosure.orig.html`); `visuals/ias2.css` (`.st-disc` block; `.m-disc-list` 5 → 6 columns); `visuals/map-formula-board.html` + `index.html` iframe key (pack Map Ch4–Ch6 labels; backup `/tmp/map-formula-board.orig.html`); `tools/gate_shots.py` (`SHOT_SETS["ch06"]`); `IAS2-CH06-CONTENT-NOTES.md`.

**Sources used:** Official IAS 2 paras 25, 36(a)–(h), 37, 38, 39, IN16, IN17, BC22–BC23; IAS 1 paras 54, 61, 65, 97, 98(a); IFRS 15 paras 33, 105–106; IFRS 13 (crypto pointer). PwC MOA 25.45, 25.48–25.51, FAQ 25.42.1. DTT iGAAP 2022 A11 2.2, 3.2.8.6-1, 3.4, 4.1, 4.2.1–4.2.6. KPMG 3.8.70.40, 3.8.80.30, 3.8.400.10–.90 (Example 17). EY: kept existing chips only (section 6.1; Practical examples 3-2, 6-1, 6-2) — no EY substance added; two new EY chips drafted on non-EY text were removed before expansion.

**QA:** cite chips 56 → 135 (Official 66, PwC 11, DTT 29, KPMG 21, EY 8); Illus 3 (6.2.1 EY Stora Enso, 6.4.1 KPMG Ex 17, 6.4.2 EY Unilever), all with visuals; 8 tables; 0 house-only / § / odd chips / HKAS / THIN / broken anchors / unlinked "see N.M"; title-essence and flowery checks clean; no "Gate", "Teaching cue", "Tie back", "story", "Illus 5.3.2" or "firm view" in Ch6 HTML or Map. Iframe fit 1280: 755/753; 420: 1197/1194. Pack Map index iframe 1420/1417 and 3015/3013.

**Headings (technical-strict):** 6.0 Disclosure requirements · 6.1 Accounting policies, including the cost formula used · 6.2 Total carrying amount and classifications of inventories (h4 Presentation in the statement of financial position) · 6.3 Inventories carried at fair value less costs to sell · 6.4 Amounts recognised in profit or loss · 6.5 Analysis of expenses by function or by nature · 6.6 Inventories pledged as security for liabilities (new; 36(h) was buried in 6.4).

**Deferred debt cleared:** Illus 6.4.1 now carries KPMG Ex 17 (Facts | Requirement | Conclusion + period table 36(e) → 36(f)/(g)); unsourced "cap … above original cost" line, "Do not bury" line and "Full teaching path … Illus 5.3.2" link removed; 6.4 bullet label "Illus 5.3.2" removed; Tie-back point-chip (10 / 20) removed; "Teaching cue" peer in 6.2.1 renamed to neutral peers; "Same …" duplicate bullets collapsed. Ch5 `#s-5-ex-kpmg-rev17` pointer → Ch6 6.4.1 now one-directional.

**Write-once pointers:** excluded inventories (KPMG 3.8.70.40 / 80.30) → Ch1 1.3; crypto → Ch1 Illus 1.1.2; cost formula change / LIFO / unallocated overheads / abnormal amounts → Ch3; recognition as an expense → Ch5 5.0–5.3; pledging and control (PwC 25.45, IFRS 15 para 33) → Ch5 5.1.

**Ch6 Concept Map — story + visit path:**
- *Story:* Disclosure packages the amounts measured in Ch3–Ch5. The accounting policies, including the cost formula (36(a)), apply across. Carrying amounts in the statement of financial position (36(b) total and classifications, 36(c) fair value less costs to sell, 36(h) pledged) sit beside the amounts recognised in profit or loss (36(d) expense, 36(e) write-downs, 36(f)/(g) reversals and circumstances). The amount recognised as an expense then follows the entity's analysis of expenses: by function → cost of inventories sold within cost of sales (para 38); by nature → raw materials and consumables, labour costs, other costs and the net change in inventories (para 39).
- *Visit path:* top bar 6.1 → stems "statement of financial position" / "profit or loss" → plate c1 Carrying amounts (6.2, 6.3, 6.6) beside plate c3 6.4 Amounts recognised in profit or loss (expense; write-downs; reversals and circumstances) → stem "amount recognised as an expense" → Decision 6.5 "Are expenses in profit or loss analysed by function or by nature?" → centred fork **by function** (c1) / **by nature** (c3), labels mid-arm → leaves para 38 / para 39.
- *Colour:* no red, no muted arm (neither outcome is a stop).

**Pack Map (Ch4–Ch6 portions only):** NRV chip 4.2 → 4.1 and def per para 7 ("recovery ceiling … not a revaluation" removed); write-down row per para 29 ("Do not lump a whole class" removed); "Reversal, capped … never above cost" → "Reversal of write-downs" per para 33; Conceptual Framework see-also → para 7 NRV vs fair value; stem "carrying amount derecognised"; "Expense exit" → "Recognition as an expense" with IAS 2 wording in the three cells; "Thin route … or an intangible" → para 35 wording; see-also IAS 16 only; disclosure list 6.1–6.6 with 6.6 pledged added.

**Deferred debt (not Ch6):**
- ~~Pack Map Ch1–Ch3 portions (e.g. "Resource consumed …", "Banned (IN13 / BC9–BC20)")~~ — resolved in the Ch1–Ch3 debt wave.
- ~~Illus 6.2.1 advance payments EY vs KPMG~~ — resolved by the sources-differ callout (see *Ch6 follow-up* below).
- ~~`ch03` Illus 3.5.2 THIN; Ch1–2 body-visual backlog; Ch1 h4 numbering~~ — resolved in the Ch1–Ch3 debt wave. Still open: 4.4.1 GAP (Ch4); `shared.css` "gate" naming (Build-owned).

**Checkpoint screenshots:** `/opt/cursor/artifacts/screenshots/checkpoint-ch06-*.png` (15: Map desktop + mobile; 6.0; 6.1; 6.2 + presentation; Illus 6.2.1; 6.3; 6.4; Illus 6.4.1; Illus 6.4.2; 6.5–6.6 + key terms; mobile Illus 6.4.1; mobile 6.0 table; pack Map desktop + mobile).

## Johnny — HARD lock: sources differ (verbatim)

"Johnny HARD lock: when firms differ, **flag the difference** — do NOT force-reconcile or invent one view. Fix Illus **6.2.1** (and nearby Ch6 teaching if needed): keep EY Stora Enso plate; add clear teaching contrast that **KPMG 3.8.400.20** treats advance payments for purchases as **not inventory**, while the EY illustration presents advance payments / cutting rights inside inventories. Cite both; write-once difference callout; no invent. Screenshots if you change the Illus. STOP after this — no Ch7. KEY CHANGES short."

**Convention (all chapters from now):** where firms differ, add one `aside.callout.differ` ("Sources differ — …") at the home of the difference: a Source | Treatment table with each firm's chip, then "shown side by side and not reconciled". Neutral tokens only (`assets/draft.css`); other mentions point to it by anchor.

## Ch6 follow-up — sources differ on advance payments (DONE)

- `ch06.html` Illus 6.2.1: EY Stora Enso plate unchanged (peers, figures, chips). New `aside.callout.differ#s-6-diff-advance` inside the strip: KPMG 3.8.400.20 (not inventory; right to receive inventory or refund of cash) vs EY Practical example 6-2 (“Advance payments and cutting rights” within inventories, EUR 63m / 2021 EUR 55m, in total EUR 1,810m / 1,478m). Closing line: not reconciled; IAS 2 contains no requirement on advance payments for purchases (checked: no "advance"/"prepay" in the official text); related pointer → Ch3 3.7 `#s-3-ex-pwc-251` (PwC FAQ 25.25.1 long-term prepayment measurement).
- 6.2 presentation bullet (KPMG .20/.30) now points to the callout instead of repeating it (write-once).
- EY: no new EY substance — the EY row restates the plate figures already on site with the existing Practical example 6-2 chip. EY source text is not in the pack, so no EY reasoning is attributed.
- `assets/draft.css`: `.callout.differ` (neutral surface + accent border); ch06 key `draft.css?v=ias2-ch6-differ-r2-20261001`.
- QA: cite chips 135 → 137 (KPMG 22, EY 9); 0 odd / § / HKAS / broken anchors; no "Gate".
- Screenshots: `checkpoint-ch06-illus-6-2-1.png` (re-captured), `checkpoint-ch06-mobile-illus-6-2-1-differ.png`, `checkpoint-ch06-section-6-2-advance-pointer.png`.

## Johnny — Ch1–Ch3 debt wave (verbatim intent)

"Johnny HARD next wave — CLEAR Ch1–Ch3 debt first (pack ends at Ch6; there is NO Ch7 — do not invent Ch7). … Reading order / visual hierarchy (HARD — do not skip) … Default scan for our boards: **left → right**, then **top → bottom**. Reader must always know **start → next → end** in one breath. PASS: clear entry (top-left / top spine); forced L→R / T→B walk; equation/peer ops vertically centred; nested parts after parent. FAIL: eye must reverse often …; hunt for start/next/end; floating ops; zig-zag that fights the story. If a Concept Map, pack-Map chrome for Ch1–3, Illus grid, or body visual FAILS — **rearrange / restructure objects** (geometry + DOM), do not only tweak colours. Self-test: narrate start→next→end with chrome covered. Scope: Ch1 + Ch2 + Ch3 only — 1. Pack Map chrome for Ch1–Ch3 (Decision Yes/No mid-branch on EACH arm; section chips; L→R/T→B); 2. Chapter-top Concept Maps Ch1–Ch3; 3. Thin Illus 3.5.2; 4. Ch1–Ch2 visuals backlog; 5. Ch1 h4 numbering. OUT OF SCOPE: Ch4 4.4.1 GAP, Ch5–Ch6, inventing Ch7. … Do not start Ch4+ unless remaining Ch1–3 debt is zero. When done, write /opt/cursor/artifacts/ias2-opus-ch1-3-debt-2026-10-01.tar.gz of draft-v1-linked."

**Reading-order rule (standing, all Maps and body visuals):** narrate start → next → end with the chrome covered. If the eye reverses, hunts, or meets a floating operator, rearrange the objects (geometry + DOM order), not colours.

## Checkpoint — Ch1–Ch3 debt wave (DONE)

Commits: `cbc85d3` (Ch1), `36e98f0` (Ch2), `dafa0f3` (Ch3), `a2b4415` (pack Map Ch1–3).

**Reading-order verdicts (before → after):**

| Map | Before | After | What was rearranged |
|-----|--------|-------|---------------------|
| Ch1 chapter-top | PASS (left spine top to bottom, exits right) | PASS | 1.1 now states its question ("Does the asset meet the definition of inventories (para 6)?") so the spine starts with a decision; 1.4 link label fixed |
| Ch2 chapter-top | FAIL — Illus 2.3.1 see-also floated in the right column beside the 2.4 node (eye had to jump right, then back) | PASS | See-also nested inside the 2.4 node (after its parent); 2.1 route added inside 2.0 |
| Ch3 chapter-top | FAIL — para 10 sum stacked vertically with no operators; "assigned to items / excluded" drawn as a pseudo-fork; 3.8 / 3.9 stacked as if more cost terms | PASS | Rebuilt as `.st-cost`: 3.0 bar → 3.1 with purchase + conversion + other costs left to right (operators centred) and the IAS 23 see-also inside Other costs → 3.6 excluded leaf beneath the sum → 3.8 / 3.9 as lighter peers → one stem → 3.10 decision → yes/no fork → specific identification ∥ FIFO / weighted average, LIFO muted inside the FIFO / WA cell |
| Pack Map, Ch1–3 portion | FAIL — 1.1 / 1.2 / 1.3 as three peer cards in a row with no yes/no; the only stem ran from the left card, so the eye read left to right and had to come back left; house wording ("Build", "Resource consumed", "Banned") | PASS | Rebuilt as one decision spine down the left column: 1.1 (para 6) → 1.2 (para 2) → 2.0 recognition → 1.3 (para 3), each with a horizontal exit arm (labelled mid-arm) to a leaf on the right and a vertical continuing arm (labelled mid-arm); see-alsos nested inside their leaves so each arm lands on one object; the last arm ("no") lands on the Cost arm of the 4.0 board. Cost arm: para 10 wording; plate "Cost of inventories (para 10)" read top to bottom with + operators in the chip column; 3.4 link in conversion; IAS 23 see-also → `#s-3-7-borrowing` (para 17); 3.6 in para 16 wording; 3.9 added; 3.10 is now a yes/no decision (para 23) inside its plate, LIFO nested under FIFO / weighted average ("not permitted", IN13; BC9–BC21) |

**Pack Map ordering note:** 2.0 (recognition) sits between 1.2 and 1.3 on purpose — para 3 holders are excluded from the measurement requirements only, so they still pass recognition; putting 1.3 last makes it the switch into measurement. Chip order therefore reads 1.1, 1.2, 2.0, 1.3, then 4.0 / 3.x. If Johnny prefers strict chapter order, swap the 2.0 and 1.3 rows (DOM order only).

**Body visuals added / rearranged:**
- Ch1: Illus 1.1.1 pipeline mini-flow; 1.1.2 cryptocurrencies mini-flow (otherwise branch, para 9); 1.1.3 spare-parts table; 1.1.5 lease-term mini-flow (4 steps); 1.1.6 IAS 40 para 57(d) mini-flow; 1.3.1 broker-trader / principal / agent table (agent row muted); 1.3.3 NRV vs fair value less costs to sell table (PwC FAQ 25.8.1 C10 / C12). h4 `#s-1-ex-kpmg-samples` unnumbered ("Advertising and promotional items — samples and catalogues"), like other chapters.
- Ch2: 2.2 FOB mini-flow (KPMG 3.8.90.20) after the 2.2 list, before the contrast pair.
- Ch3: Illus 3.5.2 `#s-3-ex-dtt-amenity` densified (no longer THIN: li 8, chars 1334) — peers Facts | Requirement | Conclusion, plus a comparison table (amenity row DTT 3.2.4.2-1; access-road row PwC FAQ 25.19.4 → 3.5.1; gift row muted); chips DTT, IAS 2 paras 10 / 15 / 16(c), PwC, EY section 3.1. Overheads mini-flow: "1 " / "2 " prefixes removed from step heads.

**QA (all six chapters):** 0 broken anchors, 0 § in chips, 0 HKAS/HKFRS, 0 flowery cues, 0 THIN; all 81 Map links in the Ch1–3 Maps + pack Map resolve; no "gate" / "story" / § in Ch1–3 HTML, Maps or index. Chips: Ch1 146, Ch2 81, Ch3 444 (Ch4–6 unchanged: 216 / 93 / 137). Iframe fit checked at 1280 and 420 (pack Map 2113 / 3965 px iframe vs 2110 / 3962 px content).

**Cache keys:** Ch1 `ias2-ch1-debt-20261001`, Ch2 `ias2-ch2-debt-20261001`, Ch3 `ias2-ch3-debt-20261001`, pack Map `ias2-packmap-ch1-3-20261001` (CSS link + `index.html` iframe).

**Remaining Ch1–3 debt:** none required. Optional: 1.1.4 visual (single test; links to the 1.1.3 table). Outside this wave: 4.4.1 GAP (Ch4); `shared.css` "gate" class naming (Build-owned, not reader-visible). Pack Map Cost arm is now taller than the NRV arm (IAS 2 paras 10–27 against 28–33); left as is, since balancing would mean cutting cost content or changing the Ch4 arm.

**Screenshots:** `/opt/cursor/artifacts/screenshots/checkpoint-ch01-debt-*.png` (11), `checkpoint-ch02-debt-*.png` (4), `checkpoint-ch03-debt-*.png` (13: Ch3 Map desktop + mobile, Illus 3.5.2 desktop + mobile, overheads flow, pack Map before desktop + mobile, pack Map after desktop + mobile, pack Map scope spine desktop + mobile, pack Map board desktop + mobile).

**Pull-back tarball:** `/opt/cursor/artifacts/ias2-opus-ch1-3-debt-2026-10-01.tar.gz`.

## Johnny — locked full pipeline (recorded 2026-10-01 15:53 UTC)

Do not start a later step until the prior one is done **and** Grok Bot replies to start it. After each step: STOP and report.

1. Ch1–Ch3 debt + reading-order wave — **DONE** (checkpoint above; screenshots + tarball delivered). Waiting for Grok Bot.
2. Ch4–Ch6 reading-order / visual hierarchy check (rearrange if FAIL) — **DONE** (checkpoint below). Waiting for Grok Bot to start step 3.
3. Pack Map (index) final revision based on locked Ch1–6, same reading-order test — **DONE** (checkpoint below). Waiting for Grok Bot to start step 4.
4. Opus 5.5 written advice: how to enhance the `ifrs-visual-grammar` / `ifrs-teaching-body` / QA skill MDs (concrete, from what was changed on pages) — not started.
5. Grok folds the advice and learnings into the skills for IFRS 18 — Grok's step, not Opus.

**Step 2 started 2026-10-01 15:54 UTC** (Ch1–3 wave accepted). Verbatim intent: "Same HARD test as Ch1–3 … Cover chrome; narrate start → next → end in one breath. Prefer L→R then T→B; FAIL if primary walk is R→L or bottom→top / hunt. On FAIL: rearrange / restructure geometry+DOM (not colour-only). Scope: chapter-top Concept Maps Ch4, Ch5, Ch6; any Ch4–Ch6 body / Illus boards that fail the walk (incl. Illus grids, formula strips, Decision branches). Do NOT invent; do NOT thin; do NOT regress Ch1–3 or 6.2.1 differ callout. Pack Map FINAL revision is STEP 3 — only light touch Ch4–6 pack-Map chips if a reading-order FAIL is in that band. Open choice: pack Map chip order 1.1, 1.2, 2.0, 1.3 — leave as is until Johnny answers. Screenshots checkpoint-ch04-ro-*, ch05-ro-*, ch06-ro-* (desktop + key mobile); copy Ch1–3 desktop highlight shots; tar /opt/cursor/artifacts/ias2-opus-ch4-6-ro-2026-10-01.tar.gz; STOP when step 2 done."

**Johnny LOCKED (15:57 UTC):** pack Map chips keep decision order 1.1 → 1.2 → 2.0 → 1.3 (not chapter-numeric). Do not swap. At step 3 (pack Map final), optionally add a one-line note that the chips follow decision order, not chapter order.

**Johnny HARD lock (16:01 UTC, skill soon):** "Visuals are storytelling — always follow story/decision order, not TOC section numbers. If visual sequence and body section numbering drift, keep the visual on story order; flag later section restructure." → Keep every Map / body visual in decision order; log each place where chip order departs from section numbering under *Section-order drift* (below) for a later restructure decision.

Notes to carry into step 4, from the Ch1–3 wave: the narrate-with-chrome-covered test; nest see-alsos inside the leaf an arm points at; put sum operators in the chip column when a sum must read top to bottom; use a yes/no fork inside a plate for in-board decisions (3.10); order the pack spine by logic (recognition before para 3) and say so when the chip order departs from chapter order.

## Checkpoint — step 2: Ch4–Ch6 reading order (DONE)

Method: Maps shot at 1280 and 420; every Ch4–6 body visual (mini-flows, standalone tables, worked strips, differ callout — 37 items) shot as elements onto contact sheets; each narrated start → next → end with the chrome covered.

| Visual | Before | After | What was rearranged |
|--------|--------|-------|---------------------|
| Ch4 Map | FAIL — continuing route ("yes — written down") in the right column dropped into 4.7, whose title starts at the left (eye reversed right to left); 4.7 a decision written as a statement, no branches | PASS | Fork swapped: yes / written down to NRV in column 1, no / measured at cost in column 3; stem "each subsequent period" runs down column 1 into 4.7; 4.7 now asks the para 33 question with its own yes/no fork (write-down reversed — limited to the original write-down, para 34 → Chapter 5 / no reversal — NRV assessed again next period) |
| Ch4 4.5 events mini-flow (para 30) | FAIL — question step, then one box holding both "Confirms" and "Does not confirm" | PASS | New `.mini-branch` kit: question joins a bar, yes / no arms labelled mid-arm, one outcome step each (reflected in NRV at the reporting date / not reflected) |
| Ch4 4.6 materials mini-flow (para 32) | FAIL — same pattern ("Yes —" / "No —" in one box) | PASS | Same branch kit (materials not written down below cost / written down to NRV) |
| Ch4 other body visuals (tables 4.0, 4.2, 4.3, 4.4.1 basis table, 4.5 contracts; NRV formula flow; PwC FAQ 25.36.1 flow; 4.7 flow; all worked strips 4.2.1–4.7.2) | PASS | — | — |
| Ch5 Map | FAIL — 5.4 bar floated under the board with no parent (reader hunted for its route) | PASS | 5.4 nested as a muted sub-leaf inside the "no — still the entity’s inventory" leaf (inventory used by the entity never passes control to a customer, para 35); bar removed; Chapter 2 link kept as a thin link |
| Ch5 5.1 sale mini-flow | FAIL — step 1 asserted control had passed, the alternative ("Control not yet transferred") appeared only in the last box | PASS | Step 1 is now the control question; yes → performance obligation satisfied — inventories derecognised (revenue; profit or loss line kept) / no → still the entity’s inventory (Chapter 4) |
| Ch5 other body visuals (5.0 equation flow, event table, 5.4 flow, Illus 5.3.1) | PASS | — | — |
| Ch6 Map | FAIL — the only continuing route (6.4 → amount recognised as an expense → 6.5) ran down the right column into a full-width decision starting at the left; left column (carrying amounts) a dead end | PASS | Columns swapped: profit or loss (6.4) in column 1 with the stem straight down into 6.5; statement of financial position (6.2, 6.3, 6.6) in column 3 as the terminal branch |
| Ch6 body visuals (6.0 table, 6.2 classifications table, Illus 6.2.1 + differ callout, 6.4 table, Illus 6.4.1, Illus 6.4.2, 6.5 table) | PASS | — | Untouched; 6.2.1 differ callout unchanged (regression shot taken) |
| Pack Map, Ch4–6 band (board → carrying amount derecognised → expense exits → disclosure) | PASS | — | Not touched in step 2 (step 3 is the final revision) |

**Kit added:** `assets/draft.css` `.mini-join` / `.mini-branch` / `.mini-arm` / `.mini-bar` / `.mini-arm-label` — a decision at the end of a mini-flow. Desktop: question → short join → bar → labelled arms → outcome steps. ≤720px: join and bar run down the left edge, arms point right into the stacked outcomes.

**Convention reinforced (all Maps):** the continuing route sits in column 1; terminal outcomes go to column 3. A full-width node below a fork must be fed from column 1.

**Cache keys:** Ch4 Map + iframe `ias2-ch4-ro-20261001`, ch04 draft.css `ias2-ch4-ro-20261001`; Ch5 Map + iframe `ias2-ch5-ro-20261001`, ch05 draft.css `ias2-ch5-ro-20261001`; Ch6 Map + iframe `ias2-ch6-ro-20261001` (ch06 draft.css unchanged — no new kit used).

**QA:** 0 broken anchors (pages and all seven Maps), 0 § / HKAS / flowery / THIN; chips unchanged (Ch4 216, Ch5 93, Ch6 137); no "gate" / "story" / § in Ch4–6 HTML or Maps; no content added beyond regrouping existing sourced text (two short outcome heads restate what the steps already said; "No reversal — NRV is assessed again in the next period (para 33)" restates para 33's new-assessment sentence).

### Section-order drift (story order kept per Johnny lock; flag for a later restructure decision)

| Visual | Chip order on the visual | Section order |
|--------|--------------------------|---------------|
| Pack Map scope spine | 1.1 → 1.2 → 2.0 → 1.3 (locked by Johnny) | 1.1, 1.2, 1.3, 2.0 |
| Ch4 Map | 4.0 → (3.1) → 4.1 → 4.5, 4.5, 4.6 → 4.4 → 4.3 → 4.7 | 4.3 "is NRV below cost" before 4.4 / 4.5 / 4.6 — the story measures NRV, compares item by item, then decides |
| Ch5 Map | 4.0 → 5.1 decision → 5.4 (nested under "no") → 5.0 board (5.1 + 5.2 − 5.3 = 6.4) | 5.0 opens the chapter; 5.4 last |
| Ch6 Map | 6.1 → 6.4 → (6.2, 6.3, 6.6 beside) → 6.5 | 6.2, 6.3 before 6.4; 6.6 after 6.5 |
| Pack Map disclosure row | 6.1 → profit or loss (6.4, 6.5) → statement of financial position (6.2, 6.3, 6.6) — aligned with the Ch6 Map at step 3 | 6.2, 6.3 before 6.4; 6.6 after 6.5 |
| Pack Map NRV arm | 4.1 → 4.5–4.6 → 4.4 → 4.3 → 4.7 (aligned with the Ch4 Map at step 3) | 4.3 before 4.4–4.6 |

**Johnny (16:05 UTC): section restructuring NOT now — flag drift only; do not renumber or move body sections. Keep visuals on story order.** Flag only, for a future decision: Ch4 could move 4.4 (item by item) and 4.5–4.6 (estimates) ahead of 4.3; Ch6 could place 6.6 with 6.2–6.3 (all carrying amounts) before 6.4. No body section has been moved or renumbered.

**Screenshots (step 2):** `/opt/cursor/artifacts/screenshots/checkpoint-ch04-ro-*` (8: Map before / after desktop + mobile; 4.5 events flow and 4.6 materials flow desktop + mobile), `checkpoint-ch05-ro-*` (6: Map before / after desktop + mobile; 5.1 sale flow desktop + mobile), `checkpoint-ch06-ro-*` (6: Map before / after desktop + mobile; Illus 6.2.1 unchanged desktop + mobile). Ch1–3 highlight shots for pull-to-box: `checkpoint-ch01-debt-concept-map-desktop.png`, `checkpoint-ch02-debt-concept-map-desktop.png`, `checkpoint-ch03-debt-concept-map-desktop.png`, `checkpoint-ch03-debt-pack-map-before-desktop.png`, `checkpoint-ch03-debt-pack-map-desktop.png` (after; retaken at the final state).

**Pull-back tarball:** `/opt/cursor/artifacts/ias2-opus-ch4-6-ro-2026-10-01.tar.gz`.

**Notes for step 4 (skill advice):** branch-at-end-of-flow kit and rule ("a question step never shares one box with its outcomes"); "continuing route in column 1"; "a node with no parent is a hunt — nest it under the route it belongs to"; story-order drift table as a QA artefact.

## Checkpoint — step 3: pack Map final revision (DONE)

Started 2026-10-01 16:07 UTC. Locks: story / decision order (1.1 → 1.2 → 2.0 → 1.3 kept); L→R / T→B; no section moves; disclosure row to match the Ch6 Map; no invent / no thin; no regress of 6.2.1 or the Ch1–6 reading-order fixes; optional one-line note on chip order.

Narration after the revision (chrome covered): note → 1.1 → 1.2 → 2.0 → 1.3 → 4.0 board [Cost: 3.1 → para 10 sum (3.2 + 3.3 + 3.5) → 3.6, 3.9 → 3.10 yes/no] lower of [NRV: 4.1 → formula → 4.5–4.6 estimates → 4.4 item by item → 4.3 yes/no → 4.7 nested under "written down"] → "carrying amount derecognised" → 5.1 control line → 5.1 + 5.2 − 5.3 = 6.4 → 5.4 thin route → disclosure 6.1 → profit or loss (6.4, 6.5) → statement of financial position (6.2, 6.3, 6.6). **PASS** at 1280 and 420.

| Band | Before | After |
|------|--------|-------|
| Reader note | — | One muted line at the top: "Section chips follow the order of the decisions, not the chapter order." (own grid area `note`) |
| Scope spine (1.1 → 1.2 → 2.0 → 1.3) | PASS (step 1) | Unchanged |
| Cost arm | PASS (step 1) | Unchanged; `.m-plate .m-out` chips now top-aligned with multi-line text (was `.m-sum` only) |
| NRV arm | FAIL vs locked Ch4 Map — "If NRV < cost" a plain list (4.3–4.4 write-down, 4.7 reversal) with no decision; estimates 4.5–4.6 missing | Measure plate: formula → 4.5–4.6 estimates (paras 30–32) → 4.4 item by item (para 29). New decision plate "Write-down (para 28)": 4.3 "Is NRV lower than cost?" → yes: written down to NRV (para 28 causes), with 4.7 reversal nested as a sub-cell (para 33) / no: measured at cost (para 9). Wording from the Ch4 Map and body; the two arms are now close in height |
| Expense band (5.1–5.4) | FAIL vs locked Ch5 Map — three loose peer cells | Context line (control transfers to the customer, IFRS 15 paras 31, 33; until then still the entity’s inventory), then the para 34 equation left to right: 5.1 sold + 5.2 write-downs and losses − 5.3 reversals = 6.4 recognised as an expense (cost of sales, para 38; disclosed under para 36(d)–(g)); operators centred; top to bottom at ≤800px. 5.4 thin route and IAS 16 see-also kept |
| Disclosure (6.1–6.6) | FAIL vs locked Ch6 Map — six numeric peers | Grouped as the Ch6 Map: 6.1 policies → **Profit or loss** (6.4, 6.5) → **Statement of financial position** (6.2, 6.3, 6.6), with chips on each entry; 6.5 now "by function or by nature" (paras 38, 39) instead of "by nature" only; head "Disclosure (paras 36–39)" |

**Files:** `visuals/map-formula-board.html`, `visuals/ias2.css` (`.m-eqn`, `.m-eq-op`, `.m-eq-res`, `.m-sub`, `.m-ask-lite`, `.m-order-note`, `.m-disc-group` / `.m-disc-g2` / `.m-disc-g3` / `.m-disc-label`; removed unused `.m-grid3`), `index.html` (iframe key + accessible title). Cache key `ias2-packmap-final-20261002`. Chapter pages and chapter Maps untouched in step 3.

**QA:** 45 pack Map links resolve; 0 broken anchors on all six pages; 0 § / HKAS / "gate" / "story" in the pack Map or index; iframe fit 2276 / 4891 px vs content 2274 / 4888 px (1280 / 420).

**Screenshots:** `/opt/cursor/artifacts/screenshots/checkpoint-pack-map-final-*.png` (12): before desktop + mobile; final full desktop + mobile; scope, board, exit, disclosure crops desktop + mobile.

**Tarball:** `/opt/cursor/artifacts/ias2-opus-pack-map-final-2026-10-02.tar.gz`.

**Notes for step 4:** pack Map bands should mirror each locked chapter Map's decision order (a pack Map drifts when a chapter Map is revised — add a QA row "pack band matches chapter Map order"); group long disclosure lists by the statement they land in; a nested part (4.7) goes inside its parent outcome cell.
