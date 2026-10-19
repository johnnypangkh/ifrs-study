# LEGO logic — which visual for which accounting idea

**Status:** analysis for sign-off. Brick IDs (B01–B21) are from `LEGO-BRICKS.md`. Picture: `lego-combos.png`. Real crops: `evidence/C-*.png`.

The visual is chosen by **what the accounting idea is**, not by what looks nice. Ask the five questions below in order and stop at the first “yes”.

---

## 1. Decision guide

| # | Ask about the idea | If yes → component | Not this, because |
|---|---|---|---|
| 1 | **Is it a test the reader answers?** | one question, two outcomes → **K5 Fork** | — |
|   | several conditions, **all** must hold | → **K4 AND-gate** | a plain grid hides that the cells depend on each other (rule 4) |
|   | several options, **any one** is enough | → **K4 OR-gate** (same component, OR operator) | — |
|   | tests in a **fixed order**, first hit decides | → **K6 Ladder** | a fork tree fans out sideways and loses the order |
| 2 | **Is it an amount?** | 2–4 terms on one line → **K8 Formula row** | — |
|   | a running total with subtotals or 4+ lines | → **K9 Ledger** | a long horizontal formula wraps and breaks the reading order |
|   | the face of a financial statement | → **K11 Statement** (the only home of B18 Strip) | — |
| 3 | **Does it happen over time or at dates?** | → **K7 Phase + timeline** | a list of dates loses the “between” (rule 5) |
| 4 | **Is it a set of things?** | same kind, nothing to compare across → **K1 Peer row** | — |
|   | compared on the **same 2+ attributes** | → **K10 Matrix** | an unpivoted list repeats the attribute names in every item (rule 1) |
|   | **groups**, each with its own content | → **K2 Rail stack** | one long column lumps groups together (rules 1, 3) |
|   | a base with **layers added** on top | → **K3 Nest** | folding layers into one box hides what is added (rule 1, “add layers, do not fold”) |
| 5 | **Does it live somewhere else?** | the story continues next chapter → **K12 Hand-off** | — |
|   | related, but a different Standard or topic | → **B09 See-also** (not a component) | — |

**Tie-breaks**
- **One idea, two shapes?** Nest them, don’t pick one. The outer shape is the bigger question. Example: IAS 16 ch05 §5.1 is a *Rail stack* whose rows are *Formula rows*.
- **Same logic in another chapter?** Use the same component, even if the chapter CSS differs today (rule 6). `STANDARDISE.md` lists where this fails.
- **Already shown elsewhere on the same map?** Point to it with B09 or a section chip (B06). Don’t draw it again (rule 7).
- **A cell is a text dump?** Ask this guide again, *for that cell*, and build the answer inside it (snap rule 9). The guide is recursive: there is no depth at which it stops applying.

---

## 2. Snap rules (how bricks join)

1. **Stack order:** Board (B01) › Plate (B02) › [Rail (B10) | Grid (B11) of Cells (B03)] › Note (B04).
   - **The stack repeats inside a cell.** Any Cell may hold its own Grid of Cells (or a Rail stack, Matrix, Formula row), and so on down.
   - **No fixed depth cap**, neither 2 nor a hard L4/L5 maximum (owner rule, 2026-10-19). This replaces the earlier “at most 2 bordered levels, a 3rd only for formula / ledger / see-also” (grammar skill §4; MF §10 draft “Max 2 bordered levels”), which no longer applies. The S13 depth-cut is on HOLD.
   - The ranks L1–L4 name *chrome steps* (plate, cell, inner cell, note), not a depth limit. A deeper grid reuses the L3 cell chrome.
2. **A rail owns its row.** Right of a rail is a grid holding only that group’s content, so a cell can be added later without redrawing (rule 3). Rails at the same level share one track and one chrome (rule 2; signed unify-A track `calc(5*var(--space-6)+var(--space-2)+var(--stroke-1))`).
3. **Operators sit *between* cells on one line.** `+ − = ±` combine amounts. **AND / OR** combine conditions and must not look like arithmetic.
4. **Arrows carry a label only when there is a choice** (Yes / No, or a short condition). A plain sequence arrow has no label.
5. **The continuing path runs down column 1. Exits go right.**
   - At most **one red stop** (B17 `.m-stop`) per fork chain. Source: grammar skill §3.
6. **Bars span the cells they apply to.**
   - **Above** a peer row: “this rule applies to all of these”.
   - **Under** an AND-gate: the junction (“Both required”).
7. **Paint never makes a new shape.** Tone (B17) only recolours a border. Strip (B18) belongs only to a financial-statement line inside K11.
8. **No cite chips, no graph paper** (R1, R2).
9. **A text dump is a cue to go one layer deeper, not to flatten** (owner heuristic, 2026-10-19; with signed rules “add layers, never fold”, “prefer pivot / matrix”, “wrap rows across”, “right of a rail is a grid for that group”).
   - **Spot it.** A Cell body (or plate region) that:
     - lists **3+ items** in one line, joined by `;`, `·` or commas;
     - says the **same attribute** for several items (“X: a; Y: b”);
     - holds **two or more groups** in one paragraph;
     - ends with a **qualifier for the whole list** (“— evaluated together …”).
   - **Go deeper with the right component, inside that cell:**

     | the dump is … | build inside the cell | brick that carries the extra words |
     |---|---|---|
     | a list of same-kind items | **K1 Peer row**, wrapped across | qualifier for all → B13 Bar / junction |
     | items × the same attribute | **K10 Matrix** (stub = item, column = attribute) | — |
     | several groups | **K2 Rail stack** | rail name = group name |
     | a base rule plus an added layer | **K3 Nest** | — |
     | amounts that combine | **K8 Formula row** / **K9 Ledger** | B14 operators |

   - **Words stay exactly as they are.** Only the separators (`;`, `·`, “ — ”) turn into cell boundaries or a bar, and every word stays in order. If splitting would need new words, stop and ask Johnny.
   - **Where to stop:** when each cell holds one idea (B03's job). A single explanatory sentence stays a Note (B04); not every paragraph is a list.
   - Real examples and mocks: `ENHANCE.md` E7 (`mocks/E07-text-dump-deeper.png`).

---

## 3. Components — recipe and real examples

Each row: the bricks it is made of, what it says to the reader, and where it already exists. **Bold example** = closest to the proposed standard.

### K1 Peer row — “these are the same kind of thing”
- **Bricks:** Grid row of Cells (title + body), plus an optional Bar above for a shared rule and an optional Glyph per cell.
- **Real:**
  - **IAS 16 ch05 §5.5 *Method*:** `.consume-bar` above 3 `article.method-name` with `svg.method-chart` (`evidence/C-peers-bar-ias16-ch05.png`).
  - CF ch02 §2.6 *Enhancing* (4 peers).
  - CF ch04 *Shared by Asset and Liability* (`.el-bar`).
  - IFRS 18 ch02 *Rules shared by both roles* (`.pa-rule`).
- **Also used *inside* a cell**, as the deeper layer for a prose list (snap rule 9). Mocked in E7:
  - IAS 2 ch02 §2.2 *Indicators that control has passed*: 5 peers plus a junction bracket for “evaluated together under IFRS 15, none individually determinative”.
  - IAS 2 master §3.6 *Not included in the cost of inventories*: 4 peers, wrapped 2 × 2.
  - Same list, not mocked: IAS 2 ch03 `.leaf-note`, and IFRS 18 ch04 `.ts-regime-eg` *Listed IFRS subtotals*.

### K2 Rail stack — “each group, with only its own content”
- **Bricks:** Rail | Grid of Cells, repeated down the plate on one shared rail track.
- **Real:**
  - **IAS 16 ch07 *Disclosure*:** 11 `.inner-rail` rows (`evidence/C-rail-stack-ias16-ch07.png`).
  - IAS 16 ch05 §5.1 *Depreciable amount* / *Residual value* / §5.2 / §5.3 / §5.5 (`evidence/B10-rail.png`).
- **Same job done with a top label (Kicker B07) instead of a rail:**
  - CF ch01 (`.ou-label`).
  - IFRS 18 ch02 (`.pa-label`), ch04 (`.ts-label`), ch06 (`.mpm-label`), ch08 (`.tr-label`).
- **Go deeper when** a cell to the right of a rail is a prose list. Give that cell its own grid (wrapped peers, or a matrix if the items share attributes) inside the same row; the rail still owns the row (rule 3). Do not move the list into a longer paragraph or a second column of prose.
  - Live candidate: IFRS 18 index / jumpboard *Other FS impacts* (`.cell-grid.g-3`): each of *SCF*, *SFP*, *EPS*, *Interim* has a body of “·”-joined points that could be peer cells under that heading.

### K3 Nest — “a base, plus a layer, plus a layer”
- **Bricks:** Plate › inner board › Rail stack › Peer row › … Each step adds one level. Add as many as the idea has layers; there is no depth cap (snap rule 1).
- **Real:**
  - **IAS 16 ch05 §5.1:** rail *Depreciable amount* › `.cap-model` rows *Cost model* / *Revaluation model* › formula row.
  - IAS 16 ch05 §5.3 *Useful life* › Definition / Factors / Land & buildings.
  - IFRS 18 ch03 *ch03-mba-nest* (`.pc-mba-rail`; `evidence/C-nest-ifrs18-mba.png`).
- **Deep today, and that is fine:** IAS 16 ch06 and master (5 levels), IAS 16 ch03/04/05 (4), CF ch07 (4), IFRS 18 ch05 (4) (`CENSUS.md` §3). Under the 2026-10-19 rule, depth alone is **not** a defect. The S13 depth-cut is on **HOLD**, superseded by snap rule 9.
- **Go deeper when** one cell holds a base rule *and* an added layer in one paragraph. Split it into the base cell with the layer nested under it, rather than leaving both in one prose block.
  - Live candidate: IAS 16 ch04 `p.thin-tip.revaluation-reversal` (*Revaluation (revaluation model only)*). The base rule is “the carrying amount cannot rise above what it would have been, net of depreciation, had no impairment loss been recognised”; the added layer is “On a revalued asset the reversal is treated as a revaluation increase …”.

### K4 AND-gate / OR-gate — “all of these must hold” / “any one is enough”
- **Bricks:** criteria Cells in one row, an Operator between each pair, a Bar under them (the junction), then Arrows to a result Cell and a stop Cell.
- **Signed (MF §9 Rec pattern):** AND pill between criteria + junction “Both required” → *Both met* / *Not met*.
- **Real today (5 markups for one job):**

| map · section | between criteria | junction | crop |
|---|---|---|---|
| IAS 16 ch01 §1.1 *Is it PPE in IAS 16?* | `span.crit-op` “+” | none (arrow “Yes” down) | `C-and-gate-ias16.png` |
| IAS 16 ch02 §2.0 *Capitalise as PPE?* | `span.crit-op` “+” | none | — |
| IAS 2 ch02 §2.2 *Three criteria, all required* | `span.or` “and” | question text “Are all three criteria met?” | `C-and-gate-ias2.png` |
| CF ch02 §2.5 *Fundamental qualitative characteristics* | `.qc-op` “+” | kicker text “Fundamental — both required” | `C-and-gate-cf02.png` |
| CF ch05 §5.3 *Usefulness tests* | `.rc-op` “+” | `.rc-bar` | `C-and-gate-cf05.png` |
| CF ch03 §3.2 objective sentence | inline `span.re-dual-and` “and” | none | `C-and-gate-cf03.png` |

- **OR-gate today:** IAS 2 ch01 §1.1 three forms of inventory joined by `span.or` “or”, under `div.st-plus` “+” after *Asset* (`C-fork-ias2.png`); IAS 2 ch01 §1.2 exclusions “or”.

### K5 Fork — “one question, two ways out”
- **Bricks:**
  - Question Cell (title = the question).
  - Arrow down = continue, labelled.
  - Arrow right = exit, labelled.
  - Outcome Cells; Tone stop on at most one.
- **Real today (6 markups):**

| map · section | connector | labels | crop |
|---|---|---|---|
| **IAS 16 ch01 §1.1, §1.3** | `.harm` side arm + `.varm` down | “Yes” / “No”, ink 10 px | `C-fork-ias16.png` |
| IAS 2 ch01 §1.1–1.3 | `.st-fork` drop → bar → two down arms | “yes” / “no”, muted 11 px | `C-fork-ias2.png` |
| CF ch05 §5.1 recognition tree | `.rc-link--h` / `--down` | “no”, muted 11 px | `C-fork-cf05.png` |
| CF ch09 *Yes/No — combined label*, ch10, ch11 | `.fork > .branch.leaf-yes/.leaf-no` | `.mid` outlined pill “Yes” / “No” | `C-fork-cf09.png` |
| CF ch06 §6.1 *Recognition to measurement* | `.mx-path--yes/--no` columns | `.mx-leaf-tag` YES / NO | — |
| IFRS 18 ch05 §5.3 *Any function line on the face* | `.oe-gate` + `.oe-branches` | `.oe-link-label` | — |

### K6 Ladder — “test in this order; first hit decides”
- **Bricks:**
  - A column of Forks: continue down, exit right.
  - If every exit lands on the **same** outcome, a collector Bar takes them to one exit Cell.
  - If each exit has **its own** outcome, there is one landing Cell per row.
- **Real:**
  - **IFRS 18 ch06 *Is it an MPM — ordered tests*:** `.gt` + `.gt-exit` collector to *Not an MPM* (`C-ladder-ifrs18-ch06.png`).
  - IFRS 18 ch03 *Classification decision tree:* `.pc-tree` with one `.pc-leaf` per category (`C-ladder-ifrs18-ch03.png`).
  - The two are the same component with a different exit rule — correct by logic. They differ only in label style (S3).

### K7 Phase + timeline — “this happens over time”
- **Bricks:**
  - Rail (phase name) | Axis.
  - Markers on the axis, each joined to its label by a leader.
  - A Span caption between markers (what happens in between).
  - Optional event lane.
- **Signed (kit 25, GB-TL):** rings on the axis; Begins / Ceases leaders; span caption “Depreciate over useful life”; no Year-end markers on Dep. Lives only in `dep-v2.html` so far.
- **Real today (4 markups):**

| map · section | markup | markers ↔ labels | between-marker note | crop |
|---|---|---|---|---|
| IAS 16 ch05 §5.4 *During use* | `.lc-head` › `.lc-head-k` + `.lc-end` cards + `.lc-axis` rings + `.lc-band` ticks | cards sit above the rings, joined by a runtime `.lc-drop` hairline leader (`ias16.css` L5698) | none; 4 “Year-end” ticks (signed Dep lock has none) | `B15-time-axis.png` |
| IAS 16 ch04 §4.5 *Revaluation*; impairment | same `.lc-head`, twice on one map, + `.lc-dia` diamonds | same | none | `C-timeline-ias16-ch04.png` |
| IAS 16 ch03 §3.5 *When recognition of directly attributable costs …* | `.ready-axis` + `.axis-mark` | one mark | none | — |
| CF ch03 §3.2 *Reporting period* | `.re-axis` + `.re-tick` | label under each ring | none | `C-timeline-cf03.png` |
| IFRS 18 ch01 *Effective date timeline* | `ol.wn-tl` + `.wn-tl-node` + `.wn-tl-card` | date above, card below | none | `C-timeline-ifrs18-ch01.png` |
| **IFRS 18 ch08 §8.1–8.2 *Calendar*** | `ol.tr-tl` + `.tr-node` + `.tr-card` + `p.tr-span` | date above, card below | **yes:** §8.2 *Retrospective* bracket | `B16-time-span.png` |

### K8 Formula row — “this amount = these parts”
- **Bricks:** result Cell (accent `.m-result`), Operator `=`, then term Cells joined by Operators.
- **Real:**
  - **IAS 16 ch05 §5.1:** `.cost-eq` *Depreciable amount = Cost − Residual value*.
  - IAS 16 ch03 §3.1: `.cost-identity`.
  - IAS 16 ch06 *Gain or loss equals …*: `.cost-eq`.
  - IAS 2 ch05 §5.1: `.exp-f` (`C-formula-ias2.png`).
  - CF ch04: `.el-eq` (`C-formula-cf04.png`).
  - IFRS 18 ch06 *MPM ± reconciling items = IFRS anchor*: `.rc-bridge` (`C-formula-ifrs18-ch06.png`).
- **Result on the left vs right:** IAS 16 puts the result first (`X = a − b`, ch03/ch05/ch06). IAS 2 ch05, CF ch04 and IFRS 18 ch06 put it last (`a + b − c = X`). See S7.

### K9 Ledger — “running total, down the page”
- **Bricks:** term Cells stacked, an Operator column on the left, a single Rule for a subtotal, a double Rule for the total, and a result Cell.
- **Real:**
  - **IAS 16 ch04 §4.2 / §4.3 carrying amount:** `.vledger`, `.vop`, `.vrule`, `.vrule-2`, `.vresult` (`C-ledger-ias16-ch04.png`; also inside `C-matrix-ias16-ch04.png`).
- **Close relative:** the K11 Statement subtotal lines (`.ts-sub`) do the same job with a different look.

### K10 Matrix — “the same questions, asked of several items”
- **Bricks:** Grid with a stub column (row keys), a header row (column Titles) and Cells. An optional Tag sits in the stub.
- **Real (7 markups):**

| map · section | markup | cell chrome | stub style | crop |
|---|---|---|---|---|
| CF ch06 §6.4 *Measurement — select a basis* | `.mx-grid/.mx-row/.mx-cell` | every cell boxed, accent on some columns | UPPERCASE muted | `C-matrix-cf06.png` |
| **CF ch08 §8.1 *Same lenses on financial and physical capital*** | `.cap-matrix/.cap-m-row/.cap-m-key/.cap-m-cell` | one frame + hairline row rules | sentence case | `C-matrix-cf08.png` |
| IFRS 18 ch02 §2.3 *Aggregation test checklist* | `.pa-matrix/.pa-mx-row/.matrix-cell` | every cell boxed | UPPERCASE bold | `C-matrix-ifrs18-ch02.png` |
| IFRS 18 ch08 §8.3–8.4 | `.tr-mx/.tr-mx-col/.tr-mx-cell` (column-major) | one frame + rules | `.tr-mx-tag` UPPERCASE | `C-matrix-ifrs18-ch08.png` |
| IAS 16 ch04 §4.2/4.3 policy | `.lens-heads/.lens-row/.lens-k/.lens-cell` | boxed row cells holding ledgers | sentence case bold | `C-matrix-ias16-ch04.png` |
| IAS 16 ch04 §4.5 *Revaluation increase and decrease* | `.rev-table/.rev-row/.rev-cell` | — | — | — |
| IAS 16 ch07 *Disclosure* | `.recon-cols` | — | — | — |

- **Go deeper when** a cell says the same attribute for several items in one line (“X: a; Y: b”). That is an unpivoted matrix: pivot it into a small K10 inside the cell (stub = item, value = attribute). A matrix may sit inside a matrix cell or a rail row.
  - Live candidate: IAS 2 ch04 §4.5 *Purpose for which the inventory is held*: “Firm sales or service contracts: contract price; excess quantities: general selling prices.” That is 2 items × 1 attribute (the selling price used); the trailing “Provisions for contracts beyond inventory held: IAS 37” stays a See-also line.

### K11 Statement — “what the face of the statement looks like”
- **Bricks:**
  - Strip bands in category colours (`--cat-*`), one per line or category.
  - Rule lines for subtotals.
  - Tags (DEFAULT).
  - A side callout joined by a Bar.
- **Real:**
  - **IFRS 18 ch04 §4.1 *Required subtotals on the category bands*:** `.ts-band`, `.ts-sub`, `.ts-attach` → `.ts-trap` §4.2 (`C-statement-ifrs18-ch04.png`).
  - IFRS 18 ch03 *pnl-categories* `.pc-band`.
  - IFRS 18 ch05 §5.3 `.oe-row--face`.
  - IFRS 18 ch07 §7.4 `.ofs-line--start`.
  - IFRS 18 index / jumpboard `.mini-pnl-band.m-strip`.

### K12 Hand-off — “the story continues in …”
- **Bricks:** Arrow + label + link, at the plate edge.
- **Real:**
  - **IAS 16 ch04–ch06 `.pack-flow.pack-flow-in`:** “from …” in.
  - IAS 16 ch02–ch05 `.exit-label` + `a.rail-link.handoff`: “to …” out (`C-handoff-ias16-ch04.png`, `B20-hand-off.png`).

### K13 Org chart (one-off) — “who controls whom”
- **Bricks:** Cells joined by Arrows in a tree, with a dashed boundary Bar.
- **Real:** CF ch03 §3.5 `.org-chart` + `.consol-boundary`. Single use; keep as is.

---

## 4. Concept → component, worked from the live maps

| accounting idea (as taught on the map) | component | where |
|---|---|---|
| Is it PPE? Is it inventory? Is it in scope? | K5 Fork (+ K4 inside the question) | IAS 16 ch01 §1.1; IAS 2 ch01 §1.1 |
| Recognise if probable benefits **and** reliable cost | K4 AND-gate | IAS 16 ch02 §2.0; IAS 2 ch02 §2.2; CF ch05 §5.3 |
| Classify income/expense: discontinued? tax? investing? financing? else operating | K6 Ladder (exit per row) | IFRS 18 ch03 |
| Is it an MPM? 4 tests, any “no” exits | K6 Ladder (collector exit) | IFRS 18 ch06 §6.2–6.3 |
| Depreciable amount = cost − residual | K8 Formula row inside K2 rail | IAS 16 ch05 §5.1 |
| Carrying amount after accumulated depreciation and impairment | K9 Ledger | IAS 16 ch04 §4.2/4.3 |
| Required subtotals on the P&L | K11 Statement | IFRS 18 ch04 §4.1 |
| Depreciation runs from available-for-use to derecognition | K7 Phase + timeline | IAS 16 ch05 §5.4 |
| Comparative period → effective date → first interim → first annual | K7 Phase + timeline | IFRS 18 ch08 §8.1 |
| Five measurement bases × entry/exit, whose view, info cue | K10 Matrix | CF ch06 §6.4 |
| Financial vs physical capital × 5 lenses | K10 Matrix | CF ch08 §8.1 |
| Straight-line / diminishing / units of production | K1 Peer row + Glyph | IAS 16 ch05 §5.5 |
| Useful life → definition, factors, land & buildings | K3 Nest | IAS 16 ch05 §5.3 |
| Disclosure items by group | K2 Rail stack | IAS 16 ch07 |
