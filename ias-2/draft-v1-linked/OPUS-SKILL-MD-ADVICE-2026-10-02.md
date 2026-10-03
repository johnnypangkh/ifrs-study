# Opus 5.5 advice — enhancing the IFRS skill MDs (step 4)

**From:** Opus 5.5 (IAS 2 pack: Ch1–6 amends, Ch1–3 debt wave, Ch4–6 reading-order wave, pack Map final)
**For:** Grok Bot, to fold into the skills in step 5 (IFRS 18 next)
**Skills read in full:** `ifrs-visual-grammar` 2026.10.02-20, `ifrs-teaching-body`, `ifrs-teaching-body-qa`
**Pack:** `refs/ias-2/draft-v1-linked/` (evidence paths below are relative to it; screenshots under `/opt/cursor/artifacts/screenshots/`)

This is advice only. Nothing below has been written into the live skills. Section 3 gives paste-ready text; everything else is the reasoning and evidence behind it.

---

## 1. What worked — already encoded well

These carried the IAS 2 pack with little or no local invention. Keep them as they are.

1. **Story first, then visit path, then draw (visual-grammar §0, §1 steps 1–1b).** Writing the 2–5 sentence story and a numbered eye-walk before any HTML stopped every Map from becoming a box collage. Every chapter Map (Ch1 r3 through Ch6) was drafted this way, and the stories are kept in `OPUS-WORKING-MEMORY.md`. When a Map failed later, the visit path showed where it failed.
2. **Logic → type table (§2).** The right type was obvious each time: Ch1 = decision tree, Ch3 = containment + formula, Ch4 = formula board + decision, Ch5 = equation board, Ch6 = carrying amounts beside profit or loss, then a decision. "Missing-route contrast" (muted "Not inventories" leaf beside the working route) and "shared rule across peers = spanning bar" (Ch1 "presentation and disclosure apply to both") were used exactly as written.
3. **Containment and nesting rules (§1 step 5, §2 part–whole).** "Nest the child inside the correct parent node" and "attach see-also tips next to the categories they qualify" fixed the Ch2 Map (Illus 2.3.1 see-also floated in the right column → nested inside 2.4) and the Ch3 cost plate (IAS 23 see-also inside Other costs).
4. **Reading-order lock (§0, Johnny HARD 2026-10-01).** The PASS/FAIL lists were concrete enough to score 7 Maps and 37+ body visuals. "Cover the chrome and narrate in one breath" was the most useful sentence in all three skills.
5. **Story order over section numbers (§0, Johnny HARD 2026-10-02).** This settled the pack Map 1.1 → 1.2 → 2.0 → 1.3 question and the Ch4 / Ch5 / Ch6 chip orders without anyone re-arguing the point.
6. **Ownership table (visual-grammar top).** It separates Map leaf colour from Illus peer colour. That let the Maps use one red leaf and muted leaves while every Illus peer stayed neutral, with no conflict.
7. **Cite-chip grammar + QA A (teaching-body Cite-tag formatting; QA A).** Firm + work + locator, no `§`, and the split placement rule (Illus → title; teaching unit → end) are unambiguous. The pack went from ~526 to ~1,100 chips with 0 house-only, 0 `§` and 0 odd labels, because the rule is mechanical and `tools/pack_audit.py` checks it.
8. **FAQ ≠ Illustration chooser (teaching-body; QA B0).** It decided every borderline plate in the Gate 1 list cleanly (e.g. Ch2 old 2.1.2 consignment split into section bullets plus one real case, Illus 2.3.1; Ch5 5.3.2 demoted to a pointer).
9. **Quantitative densify gate (QA D4).** "≤5 bullets or ≲350 chars = THIN" is objective. It caught Ch3 Illus 3.5.2 (5 li) and confirmed the fix (8 li / 1,334 chars).
10. **Hyperlink review (QA F) and the repeat-mistake rule (QA G).** After renumbers, 0 broken anchors and 0 unlinked "see N.M" across six pages. The repeat-mistake rule is the right escalation mechanism; section 3 uses it to justify new automated checks.
11. **Technical-strict titles (teaching-body; QA E2).** It removed "theatre", "ritual", "handoff", "a light chapter on purpose", etc. and replaced them with Official headings without debate.

---

## 2. Gaps and friction — where I had to invent local patterns

Each item gives what the skills say (or don't), what happened on IAS 2, and the local pattern I used. Section 3 turns each into skill text.

### 2.1 Fork geometry is under-specified

- **Skill says:** "Yes/No labels sit on their own branch arrows" (§0 PASS) and "yes/no = attached stems" (§2 decision tree). Nothing on where the label sits, how long arms are, or what joins the decision to the arms.
- **IAS 2:** Johnny rejected the first labels as "oddly offset" and the bottom fork stems as too short (Gate 3b, Step A). The fix was a precise kit: an unlabelled drop from the decision, a horizontal bar, one arm of equal length per outcome, and the label centred mid-arm with a `var(--bg)` mask, on the same y on both arms. Minimum arm height is 76px desktop / 64px narrow. The label is never on the stem *into* the decision.
- **Local pattern:** `.st-fork` / `.st-arm` / `.stem-label` / `.st-h-label` in `visuals/ias2.css`; screenshots `map-yesno-ch0{1,2,3,4}-{desktop,mobile}.png`.

### 2.2 No column convention for decision boards (the Ch4 and Ch6 column swaps)

- **Skill says:** nothing about which side of a fork the continuing route goes on.
- **IAS 2:**
  - **Ch4 Map** FAILED because the continuing route ("yes — written down") was in the right column and dropped into 4.7, whose title starts at the left. The eye went right then back left.
  - **Ch6 Map** FAILED the same way: the only continuing route (6.4 → amount recognised as an expense → 6.5) ran down the right column into a full-width decision.
  - Both passed after swapping columns: continuing route in column 1, terminal outcomes in column 3.
- **Local pattern:** "continuing route in column 1; terminal outcomes in column 3; a full-width node below a fork is fed from column 1." Evidence: `checkpoint-ch04-ro-*`, `checkpoint-ch06-ro-*` (before/after).

### 2.3 "A decision written as a statement" is not called out

- **Skill says:** "question = gate" in the decision-tree row, but no rule that every decision node *ends in a question with its own arms*.
- **IAS 2:** Ch4 4.7 was "Reversal of write-downs" (a statement) with no arms, although para 33 is a yes/no test. Ch5 5.1 mini-flow step 1 *asserted* control had passed, and the alternative appeared only in the last box. Both FAILED narration ("then where does the no case go?").
- **Local pattern:** every decision node carries the Standard's test as a question ending in "?" plus para cite, and has exactly one labelled arm per outcome.

### 2.4 Body mini-flows have no grammar at all

- **Skill says:** teaching-body mentions "mini flow / diagram" as a visual-when-complex option (Illustration ambition 3; QA E3) but gives no shape. Visual-grammar's fork grammar is scoped to Maps.
- **IAS 2:** Ch4 4.5 events (para 30) and 4.6 materials (para 32) mini-flows put the question in one step and *both* outcomes ("Confirms / Does not confirm") in one box, so it read as a process with no branch. The Ch3 overheads mini-flow had "1 " / "2 " step prefixes (free ①②③ rail).
- **Local pattern:** new branch kit in `assets/draft.css`: `.mini-join` → `.mini-bar` → `.mini-arm` (label mid-arm, `background:var(--bg)`) → one outcome step per arm. At ≤720px the join and bar run down the left edge and arms point right into stacked outcomes. Rule: **a question step never shares one box with its outcomes.** Evidence: `checkpoint-ch04-ro-*-4-5*`, `-4-6*`, `checkpoint-ch05-ro-*-5-1*`.

### 2.5 Orphan nodes are not named as a failure

- **Skill says:** §1 step 3 lists many mistake classes but not "a node nothing points at".
- **IAS 2:** Ch5 Map 5.4 (inventories allocated to other assets) was a bar under the board with no incoming stem, so the reader hunted for its route. Fixed by nesting it as a muted sub-leaf inside the "no — still the entity's inventory" leaf (para 35), with a thin link to Ch2. Pack Map 4.7 (reversal) was a loose list item. Fixed by nesting it inside the "yes — written down to NRV" cell.
- **Local pattern:** "a node with no parent is a hunt — nest it under the route or outcome it belongs to."

### 2.6 Equations: L→R identity vs vertical sum is ambiguous

- **Skill says:** FAIL when "a formula or peer row is stacked so it reads like a process when the story is left-to-right identity". There is no guidance for when a sum *must* stack (narrow column, long terms), or what happens to an L→R equation on mobile.
- **IAS 2:**
  - Ch3 para 10 cost was stacked with no operators (FAIL).
  - The pack Map Cost arm sits in a half-width column, so a horizontal sum was impossible. I stacked it top→bottom with `+` operators in the chip column (`.m-plus`, `.m-sum`) and the result titled as the plate.
  - The pack Map expense band (step 3) is the para 34 identity read L→R (`5.1 + 5.2 − 5.3 = 6.4`, `.m-eqn` 7-column grid, operators vertically centred). It becomes one column at ≤800px with operators centred on their own rows.
- **Local pattern:** an identity reads L→R at desktop. If width forces a stack, every operator keeps its own row or column between the terms and the result comes last after `=`. A stack *without operators* is always FAIL.

### 2.7 The pack Map silently drifts from the chapter Maps

- **Skill says:** "Map vs body — map points rather than redraws" (§1 step 9). Nothing on keeping a jump board aligned with chapter Maps once those change.
- **IAS 2 (step 3):** after the Ch4 / Ch5 / Ch6 Maps were rearranged in step 2, the pack Map bands were out of step:
  - The NRV arm had no 4.3 decision and was missing 4.5–4.6 estimates.
  - The expense band was three loose peer cells rather than the para 34 equation.
  - Disclosure was six numeric peers rather than the Ch6 grouping.

  All three FAILED against the locked chapter Maps, though each passed on its own.
- **Local pattern:** each pack band mirrors the decision order of its locked chapter Map and is re-checked in the same wave as any chapter Map change.

### 2.8 Long disclosure lists have no grouping rule (directly relevant to IFRS 18)

- **Skill says:** nothing on how to order or group a disclosure package on a Map.
- **IAS 2:** six peers 6.1–6.6 in numeric order read as a flat list with no story. The Ch6 Map story is policies (36(a)) → amounts in profit or loss (36(d)–(g), then the 6.5 analysis by function or by nature) beside carrying amounts in the statement of financial position (36(b), (c), (h)). The pack Map now groups as `6.1 → Profit or loss (6.4, 6.5) → Statement of financial position (6.2, 6.3, 6.6)`, with small uppercase group labels and explicit grid columns (`.m-disc-group`, `--m-disc-n`).
- **Local pattern:** group disclosure items by the statement (or note) they land in, in story order. Label the group with the statement's name. Keep a chip on each entry.

### 2.9 The cover-chrome self-test is a sentence, not a procedure

- **Skill says:** "Cover the page chrome and narrate the walk in one breath."
- **IAS 2:** to make it repeatable I had to define what "chrome" is, at which widths to test, what to record, and how to catch DOM-order failures. On mobile the grid collapses to DOM order, so a desktop layout that passes via CSS placement can fail on mobile or for a screen reader. That is why Johnny's lock says "rearrange geometry **and DOM**."
- **Local pattern:**
  - Shoot at 1280 and 420 (IAS 2).
  - Crop each band.
  - Write the narration as an arrow chain of chip numbers (e.g. pack Map final: `note → 1.1 → 1.2 → 2.0 → 1.3 → 4.0 [3.1 → 3.2+3.3+3.5 → 3.6, 3.9 → 3.10 y/n] lower of [4.1 → 4.5–4.6 → 4.4 → 4.3 y/n → 4.7] → 5.1 → 5.1+5.2−5.3=6.4 → 5.4 → 6.1 → (6.4, 6.5) → (6.2, 6.3, 6.6)`).
  - Mark any "back"/"jump" word as FAIL.
  - Confirm the DOM source order gives the same sequence.

### 2.10 Section-number drift has a lock but no artefact

- **Skill says:** "keep the visual on story order; flag a later section restructure." It does not say *where* to flag it or in what form. Johnny then added (16:05) "restructuring NOT now — flag only."
- **IAS 2:** I kept a *Section-order drift* table (visual chip order vs body section order) for the pack scope spine, Ch4, Ch5, Ch6, pack disclosure and pack NRV. Without a fixed place, drift flags get lost between waves.
- **Local pattern:** one drift table per pack in working memory or METHOD, with columns Visual | chip order | section order | proposed restructure (not applied).

### 2.11 Chip-order note for readers

- **Skill says:** numeric jumps are PASS when story-correct. It is silent on telling the reader.
- **IAS 2:** Johnny allowed an optional note. The pack Map now carries one muted line: "Section chips follow the order of the decisions, not the chapter order." It sits in its own grid area so it does not join the walk.

### 2.12 Colour on decision leaves — the skill and Johnny's practice differ

- **Skill says:** "green/red only on true yes/no *leaves*" (§1 step 6, §2 colour). That reads as if every leaf may be green or red.
- **IAS 2:** Johnny's Ch1 "Change all" was "reduce red stop leaves — red only on true hard stops". The final pack has **one** red leaf per board at most: Ch1 / pack Map "Outside the scope of IAS 2" (para 2). "Not inventories" is muted. Measurement-only exclusion (para 3) is a *neutral peer*, not a stop. Ch2, Ch5 and Ch6 have no red and no green at all.
- **Local pattern:** red = the Standard does not apply (true hard stop); muted = "not X / no further route here"; every other outcome neutral; green not used.

### 2.13 Vocabulary leak: "gate" in the skills vs "never Gate" for readers

- **Skill says:** visual-grammar uses "gate" throughout as a method word ("gates vs outcomes", "Gate spine", "gate tree"). QA C3 lists peer labels "Facts / **Gate** / Conclusion / Exception". Teaching-body's preferred-layout table lists "`Usual gate`, `Gate`" as peer labels, and its reference shape is "4.5.1 — Facts | **Usual gate** | Exception".
- **Johnny lock (14:18):** "Use **Decision**, NOT 'Gate' — do not introduce 'Gate' in HTML / labels / comments Johnny sees."
- **IAS 2:** I renamed "Usual gate" → "Requirement" (Ch5, Ch2), "Gate question" comments → "Decision question", and aria-labels → "Decision: …". The skills still *teach* the forbidden labels, so the next writer will reintroduce them.
- **Tooling trap:** a naive `rg -i gate` gives 11 hits in the final pack, all false: 10 are "segre**gate**d" (para 23 wording in Ch3 and two Maps) and 1 is "aggre**gate**". The word-bounded check gives 0. Use `rg -w`.

### 2.14 Stale reference shapes in teaching-body

- Teaching-body "Reference shapes (live in IAS 2 ch04)" lists 4.5.1 "Facts | Usual gate | Exception", 4.5.2 "Facts | Conclusion", 4.5.3 "Facts | Covered … | Excess …". After the Ch4 amend and renumber these ids and labels no longer exist. Live 4.5.1 is "Sale after the reporting period at a price below cost — Facts | Sale at a lower price | Damage after the reporting period"; 4.5.4 "Facts | Did the condition exist at the year end? | Conclusion". A skill that points at live HTML goes stale on the next amend.

### 2.15 Firms that differ: no body pattern

- **Skill says:** teaching-body "Distinct firm views … stay separate units". That is all.
- **IAS 2:** Johnny's HARD lock (Ch6) was to flag, not reconcile. I invented `aside.callout.differ` (neutral surface + accent border, `assets/draft.css`). It has a "Sources differ — …" title, a Source | Treatment table with each firm's chip, and a closing line "shown side by side and not reconciled", plus a note when the Standard itself is silent (no "advance"/"prepay" in IAS 2). Other mentions point to it by anchor (write-once). Evidence: Illus 6.2.1 `#s-6-diff-advance`, `checkpoint-ch06-illus-6-2-1.png`, `checkpoint-ch06-mobile-illus-6-2-1-differ.png`.

### 2.16 Cross-chapter duplicates: "write once" covers a unit, not a pack

- **Skill says:** duplication rule is unit-level (one dense unit + all chips).
- **IAS 2:** the same plate lived in up to four places:
  - KPMG Ex 17 was told in Ch5 5.3, 5.3.2, Ch6 6.4 and 6.4.1.
  - Spare parts appeared in both 1.1.3 and 2.1.1.
  - Expense exits appeared in both 2.2 and 5.0–5.4.

  Grok locked "one home + pointer that carries all supporting chips"; I applied it pack-wide.
- **Gap:** no rule for choosing the home. The choice used was "the chapter whose Official heading owns the requirement" (Ex 17 → Ch6 disclosure; IN14 → Ch5 recognition as an expense).

### 2.17 Unsourced editorial chips and author meta are not banned explicitly

- **IAS 2:**
  - Point-chips "Why normal capacity", "Why a ceiling", "Concept insight", "Trap", "Tie back" had no locator. One ("US GAAP habit that write-downs are not reversed") cited a source outside the pack.
  - Teaching prose carried author meta ("Keep this plate on Chapter 1 — do not move…", "this plate does not invent…", "Columns match Inform").
  - Grok locked "drop any claim without an Official or pack Big4 locator". The skills still list "Point chip" as a container with no source requirement.

### 2.18 "Source not attached to this run" vs "not on disk"

- **Skill says:** pre-flight treats a firm as on disk (scan it) or `not on disk` (Blocking until Johnny confirms).
- **IAS 2:** EY iGAAP 2026 Ch23 exists on the box but was not in the Opus run. The working rule became "keep existing EY text and chips; add no EY substance; never attribute EY reasoning", e.g. the 6.2.1 differ row restates figures already on site under the existing chip. Two new EY chips drafted on non-EY text in Ch6 were removed before shipping. The skills have no status for this case.

### 2.19 Build-owned chrome that blocked teaching

- Iframe ratchet: `theme.js` / `iframe-fit.js` measured `max(body, html)`, so every chapter had +100–180px dead space. Fixed (body-only, PAD 2) only once Johnny unlocked it.
- `.worked-strip-grid` is fixed at 3 columns, so two-peer strips leave an empty third column. The workaround was to split existing content into three neutral peers.
- In-strip tables sit with no margin under the grid.
- The skills say "Build" but give no QA check that would catch these regressions.

### 2.20 Cache keys

- Two places must change together: the visual's CSS link `?v=` and the chapter iframe `?v=`, plus the page `draft.css?v=` when a body kit is added. Missing one made screenshots show stale geometry. The skills mention "cache-bust the iframe" only.

---

## 3. Concrete patch proposals (paste-ready)

Format: **where** → `### Subsection title` → bullets. Where a patch *replaces* text, the old text is quoted. Keep chapter specifics out of rules; IAS 2 appears only as one-line examples or §3 method rows, per the skill's own "encode principles" instruction.

### 3A. `ifrs-visual-grammar`

**VG-1 — after "Self-test (before show Johnny)" in §0 → add:**

### Reading-order self-test — procedure
- Shoot every board at each viewport the pack requires (see *Viewport scope per pack*), then crop each band or plate.
- "Chrome" = page header, legend, chapter tabs, the reader note, cite chips' colours. Cover them; narrate only nodes, stems, labels.
- Write the narration as one line of chip numbers and arrows, e.g. `1.1 → 1.2 → 2.0 → 1.3 → 4.0 [Cost … ] lower of [NRV … ] → 5.x → 6.x`. Record it in the pack working memory or NOTES next to the board.
- Any of these words in the narration = FAIL: "back", "go up", "jump left", "look for", "then also".
- Read the DOM source order of the board top to bottom. It must give the same sequence as the narration (mobile collapse and screen readers follow DOM, not grid placement).
- Score each board PASS / FAIL with one sentence of cause; on FAIL, record what was rearranged (geometry + DOM), never "recoloured".

**VG-2 — §0, new subsection after the reading-order lock:**

### DOM order is reading order
- Fix a reading-order FAIL by moving nodes in the DOM and in the grid together. Do not fake order with CSS `order:` or by placing grid areas out of source order.
- When a layout collapses to one column, nodes stack in DOM order, so that order must itself be the story walk.
- Grid areas may name bands (`note`, `scope`, `board`, `exit`, `disc`), but the area sequence must equal the DOM sequence.

**VG-3 — §2, new subsection after "Connector grammar":**

### Column convention on decision boards
- The continuing route sits in column 1 (left); terminal outcomes sit in column 3 (right). The eye never crosses right-to-left to continue.
- A full-width node below a fork is fed by a stem from column 1.
- If the Standard's "yes" is the terminal outcome, put "yes" on the right arm; do not swap arm labels to keep "yes" on the left. Label truth beats left/right habit.
- Side see-alsos nest inside the leaf the arm lands on, so each arm ends on one object.

**VG-4 — §2, replace the PASS bullet "Yes/No labels sit on their own branch arrows" with a pointer to, and add:**

### Fork grammar (yes / no arms)
- Every decision node states the Standard's test as a question ending in "?", with the para in brackets (e.g. "Is NRV lower than cost? (para 28)"). A statement is not a decision.
- Every decision has one labelled arm per outcome (normally two). A decision with no arms = FAIL.
- Shape: unlabelled drop from the decision's bottom edge → horizontal bar → arms of equal length → outcome leaves. The stem *into* a decision carries no yes/no.
- One label per arm, centred mid-arm on the shaft (masked so the line breaks around the word), same height on both arms. Arms are long enough to read as a split (IAS 2 kit: ≥76px desktop, ≥64px narrow).
- Horizontal exit arms (decision → side leaf) carry their label mid-arm too.
- Sub-decisions that follow an outcome sit *inside or directly under* that outcome, never beside the parent decision.

**VG-5 — §1 step 6 and §2 "Colour": replace "green/red only on true yes/no *leaves*" with:**

### Colour on decision leaves
- **Red** only on a true hard stop: the Standard does not apply (e.g. outside the scope). Expect at most one per board; justify any second.
- **Muted** (lighter border, no fill, muted stem) for "not X / no further route on this board".
- **Neutral** for every other outcome, including carve-outs that are peers of the main path (e.g. "excluded from the measurement requirements only" is a peer, not a stop).
- Green: do not use by default; continuing routes are shown by geometry and accent stems, not fill.
- Illus peers stay neutral regardless (ownership table).

**VG-6 — §1 step 3 mistake classes: append:**
- **orphan node** — a box with no incoming stem and no parent plate (fix: nest it under the route or outcome it belongs to);
- **decision as statement** — a test written as a heading with no arms;
- **outcomes sharing one box** — "yes / no" both written inside one step;
- **continuing route on the right** feeding a full-width node that starts at the left.

**VG-7 — §2, new subsection after "Residual / identity":**

### Equations and sums
- An identity reads L→R: terms, then operators (`+` `−` `=`) unboxed and vertically centred on the term midline, then the result last and visually distinct.
- If width forces a stack (narrow column, mobile), keep every operator on its own row or in a dedicated operator column between terms; result last after `=`. A stacked sum without operators = FAIL.
- The result node may carry its follow-on (e.g. where it is disclosed) inside it, not as a new band.
- When the result of one board is the input of another chapter, chip the result with that chapter's section (e.g. `= 6.4`).

**VG-8 — new section after §2 (before §3):**

### Pack Map / jump board
- Each band mirrors the decision order of its locked chapter Map: same nodes, same order, same decision questions, fewer words. The pack Map points; it never re-teaches or re-orders.
- Any chapter Map change → re-check the matching pack band in the same wave (QA row *pack band mirrors chapter Map*).
- One spine of decisions down column 1 with exits to column 3; the last continuing arm lands on the measurement board.
- Long lists are grouped by where they land (statement / note / component), in story order, each group labelled with its technical name (e.g. "Profit or loss", "Statement of financial position"); every entry keeps its own chip.
- Nested parts sit inside their parent outcome cell (e.g. a reversal inside "written down").
- If chip numbers jump on the board, add one muted reader line in its own grid area: "Section chips follow the order of the decisions, not the chapter order."

**VG-9 — §0 "Story order over section numbers": append:**

### Section-order drift log
- Every pack keeps one drift table (working memory or METHOD): Visual | chip order on the visual | body section order | proposed restructure.
- Add a row whenever a board's chip order departs from section numbering. Do not renumber or move body sections unless Johnny opens a restructure wave.

**VG-10 — §4 product locks: replace "Map chips are chapter numbers, not step numbers." with:**
- Map chips show the **target section number** (e.g. `4.3`), never a sequence number (①②③). Their order follows the story (§0), so numeric jumps are expected.

**VG-11 — vocabulary note at the top of §0:**

### Words on the page vs words in this skill
- This skill uses "decision" and "outcome" for method. Reader-visible HTML, labels, aria-labels and comments use **Decision / Test / Assessment** only — never "Gate", "story", "spine", "pipeline".
- Recommendation for the fold-in: replace "gate" with "decision" throughout this skill so the forbidden word cannot leak into drafts (meaning unchanged: "gate drawn as an outcome" → "decision drawn as an outcome").

**VG-12 — new subsection in §4:**

### Viewport scope per pack
- IAS 2: desktop (1280) + mobile (420) screenshots and narration are both required.
- CF 2018 / IFRS 18: desktop-only unless Johnny says otherwise. Still keep DOM order = reading order (VG-2); do not spend time on mobile restacks; do not design mobile-first.
- State the viewport set in each Opus handoff.

**VG-13 — §3 method rows (one line each; IAS 2 signed moves):**

| Signed redraw | Logic it was teaching | Visual move to reuse |
|---|---|---|
| IAS 2 Ch1 (r3) | Definition → scope exclusion → measurement-only carve-out | Every node a yes/no question; one red leaf (true stop); "not X" muted; carve-out = neutral peer; shared rule = spanning bar under both peers. |
| IAS 2 Ch3 | Cost = sum of components; formula choice | Sum with operators centred; see-also inside the component it qualifies; banned option (LIFO) muted *inside* the allowed cell. |
| IAS 2 Ch4 | Measure NRV → compare item by item → decide → later reversal | Continuing outcome in column 1 feeds the next decision; the later test (reversal) is its own decision nested under the outcome it follows. |
| IAS 2 Ch5 | Control decision → derecognise → expense identity | Decision first, then outcomes, then the identity L→R; orphan route nested under the outcome it belongs to. |
| IAS 2 Ch6 | Disclosure package by destination, then analysis decision | Continuing branch (profit or loss) in column 1 into the by-function / by-nature decision; carrying amounts terminal in column 3. |
| IAS 2 pack Map | Jump board across six chapters | Bands mirror locked chapter Maps; decision spine with exits right; disclosure grouped by statement; reader note on chip order. |

**VG-14 — "Before shipping": add:**
- 1e. **Column / fork check:** continuing route in column 1; each decision a question with labelled arms; no orphan nodes; red count justified.
- 1f. **Pack band mirror:** if a chapter Map changed this wave, the pack band was re-checked and its chip order matches.
- 1g. **Drift log** updated for every chip-order departure.

### 3B. `ifrs-teaching-body`

**TB-1 — fix contradictions (replace text):**
- Preferred-layout table row `Gate / mid | .box (neutral) or omit | Usual gate, Gate, Covered 500, …` → `Requirement / mid | .box (neutral) or omit | Requirement, Test, the test's own question, Covered 500, …`.
- Delete the "Reference shapes (live in IAS 2 ch04)" list (ids and labels are stale after renumber). Replace with **shape descriptions** that do not point at live ids:
  - *Facts | Requirement | Conclusion* — single test.
  - *Facts | [the test as a question] | Conclusion* — when the plate turns on one question.
  - *Facts | [outcome A] | [outcome B]* — two outcomes of the same facts.
  - *Facts | [measure] | [result] + table* — numeric plate.
- Anywhere a column label example says "Gate" → "Decision" / "Test" / "Assessment".

**TB-2 — new subsection after "Mandatory format (other)" item 4:**

### Sources differ — flag, do not reconcile (Johnny HARD)
- When pack sources give different treatments of the same point, add one `aside.callout.differ` at the home of the difference: title "Sources differ — [point]", a Source | Treatment table with each source's full chip, closing line "Shown side by side and not reconciled."
- If the Standard is silent on the point, say so in one line (after checking the Official text).
- Neutral tokens only — neither treatment styled as right or wrong (no ok/warn).
- Other mentions link to the callout's id instead of repeating it (write-once).
- Never invent a third "reconciled" view; never attribute reasoning to a source whose text is not in the run (see TB-6).

**TB-3 — new subsection after the duplication rule:**

### Home chapter and pointers (pack-level write-once)
- A plate or teaching unit lives in exactly one chapter: the chapter whose Official heading owns the requirement (e.g. a disclosure example → Disclosure; derecognition timing → Recognition as an expense).
- Every other chapter carries a one-line pointer `li` (keeping the old id if one existed) that links the home and carries **all** the supporting chips.
- After moving a home, run the hyperlink review on the pack and remove any circular pointer (A → B → A).

**TB-4 — new subsection under Illustration ambition 3 ("Visual when complex"):**

### Body mini-flow grammar
- Steps read L→R at desktop and stack T→B at narrow width; step heads are technical labels with no "1 / 2 / 3" prefixes.
- A **question step never shares one box with its outcomes.** A decision at the end of a flow uses the branch kit: question → join → bar → one labelled arm per outcome (label mid-arm) → one outcome step each. Narrow width: join and bar run down the left edge, arms point right into stacked outcomes.
- The first step of a decision flow is the test as a question, not an assertion that it is met.
- Mini-flows carry only sourced steps; each outcome step can link to the section that treats it.
- Same reading-order self-test as Maps (visual-grammar §0).

**TB-5 — new subsection after "Mandatory format (other)":**

### Point-chips, editorial asides and author meta
- Every point-chip ("Why …", "Trap", "Concept insight", "Tie back", any tip) carries an Official or pack Big4 locator chip, or it is removed. No locator = invent.
- Never cite a framework outside the pack sources (e.g. US GAAP habits) as teaching.
- No author meta in teaching or Illus bodies: "keep this plate on Chapter N", "this plate does not invent…", "columns match …", "do not move", "EY places this … after …". Such notes go to NOTES / METHOD.

**TB-6 — Big4 pre-flight, add a third status beside path / `not on disk`:**

### Source on disk but not attached to this run
- METHOD records `on disk — not attached to run [date/agent]`.
- In that run: keep existing text and chips for that source unchanged; add **no** new substance or chips for it; never attribute reasoning to it; in a differ callout, restate only what is already on site under its existing chip.
- This is not a pre-flight PASS for that firm; the next run with the source attached must scan it.

**TB-7 — FAQ ≠ Illus chooser: append:**
- Demoted content goes to a numbered `h4` under its parent when the parent has no Illus left, or into a dense bullet when it is a rationale paragraph (BC). **Keep the old id** on the new `h4` / `li` so inbound Map and cross-chapter links survive.

**TB-8 — Container chooser: add a row:**

| **Sources-differ callout** | `aside.callout.differ` | Firms (or Official vs firm) treat the same point differently | Reconciling; ok/warn styling; repeating the difference elsewhere |

**TB-9 — Concept Map chrome (§9): add:**
- Cache keys move together: the visual's CSS link `?v=`, the chapter iframe `?v=`, and the page `draft.css?v=` when a body kit is added or changed. Re-shoot after the bump.

### 3C. `ifrs-teaching-body-qa`

**QA-1 — fix contradiction in C3:** "Peer column labels (Facts / Gate / Conclusion / Exception)" → "Peer column labels (Facts / Requirement / Assessment / Conclusion / Exception)".

**QA-2 — new section after F:**

### F2. Visual reading-order gate (Maps + body visuals) — BLOCKING when a visual was touched
1. Screenshot every touched board at the pack's viewports; crop bands; for body visuals, shoot every `.mini-flow`, `.worked-strip`, standalone `table` and `.callout.differ` as element shots on contact sheets.
2. Narrate each (visual-grammar *Reading-order self-test — procedure*); record verdict + one-line cause + what was rearranged.
3. FAIL classes: reverse/hunt walk; orphan node; decision without arms; question and outcomes in one box; continuing route on the right; stacked sum without operators; DOM order ≠ narration.
4. Fix = geometry + DOM. A colour-only change never clears a reading-order FAIL.
5. Regression set: re-shoot all previously locked boards and locked items (e.g. IAS 2 Ch1–6 Maps, Illus 6.2.1 differ callout) and compare with the last accepted shots.

**QA-3 — new section after F2:**

### F3. Pack Map mirror + drift log
1. For each chapter whose Map changed, extract the chip sequence of the chapter Map and of the matching pack band; they must match in order (pack may omit, never reorder).
2. Drift log row exists for every chip-order departure from section numbering.
3. If chip numbers jump on the pack Map, the reader note line is present.

**QA-4 — automated checks (extend `tools/pack_audit.py`; it currently scans only `ch*.html` `<article>`):**
```bash
# Reader-visible "gate" — word-bounded (plain `rg -i gate` matches "segregated")
rg -nwi 'gate|gates' ch*.html visuals/*.html index.html | rg -v 'sh-gate'
# HKAS/HKFRS and § in Maps too (§ allowed only as fb-num chrome, never in text or cites)
rg -n 'HKAS|HKFRS' visuals/*.html index.html
# CSS order faking reading order in visual CSS
rg -n '\border\s*:' visuals/*.css assets/draft.css
```
Python additions (prefer over rg):
- Resolve every `href="…#frag"` in `visuals/*.html` and `index.html` (Maps link with `../chNN.html#id` and `target="_parent"`).
- Count red leaves (`.leaf.stop`) per board; > 1 = review.
- Every `.st-fork` / `.mini-branch` has ≥ 2 arms and each arm has a non-empty label.
- Cache keys: CSS link `?v=` in each visual equals the `?v=` on the iframe that embeds it.
- Iframe fit: at each viewport, iframe height − body height ≤ 3px (Build regression check, not a design edit).
- Point-chips without a `.cite` inside = FAIL (TB-5).
- Each `.callout.differ` has ≥ 2 chips from different sources and the "not reconciled" line.

**QA-5 — H. Process gate: add:**
- One writer per file: never edit the same file in two parallel operations, and never run a command that reads a file in the same batch as the edit to it. After writing a long working-memory / NOTES file, check `git diff --stat` for unexpected deletions before committing. (IAS 2: an overlapping write wiped a 44-line checkpoint; restored from git.)
- Tarballs and commits exclude `uploads/` (copyrighted PDFs).

**QA-6 — Done when: add:**
- [ ] F2 reading-order gate green on every touched visual at the pack's viewports; narration recorded
- [ ] F3 pack band mirrors chapter Map; drift log current; reader note present if chips jump
- [ ] `gate` (word-bounded) absent from reader-visible HTML, aria-labels and comments
- [ ] Every differ callout flags both sources, unreconciled
- [ ] Regression shots of locked boards unchanged

**QA-7 — H6:** replace "Map (IAS 2 unlocked 2026-10-01): if chapter-top Maps or pack Map were edited, also verify…" with "If any Map or body visual was edited, run **F2** and, for Maps, **F3**."

---

## 4. IFRS 18 readiness — which advice matters most

IFRS 18 is presentation and disclosure throughout. That means statement schematics, categories, required subtotals, aggregation and disaggregation, management-defined performance measures, and long note packages. These are the patches that will carry the most weight, in priority order:

1. **VG-8 Pack Map / jump board + QA-3 mirror check.** IFRS 18 chapters interlock (classification feeds subtotals, subtotals feed MPMs and disclosure). With more chapters and denser Maps, the jump board will drift faster than it did on IAS 2. Make "pack band mirrors chapter Map" a blocking QA row from the first IFRS 18 chapter, not a final-wave fix.
2. **Group-by-destination rule (VG-8, §2.8).** IFRS 18 disclosure lists are far longer than IAS 2 para 36. Group by where the item lands: statement of profit or loss / the notes / MPM note / specified expenses by nature. Each group gets its technical name, story order inside each group, and a chip on every entry. A flat numeric list of note requirements will FAIL narration.
3. **Multi-column statements = statement schematic, not decision board.** The existing §3 IFRS 18 rows (subtotals as statement rules, double rule on the final total, overrides bracketed on exactly the peers they modify) are right. Add, for multi-column layouts:
   - Columns are categories, read L→R in the order the Standard presents them.
   - Rows are lines, read T→B down to each required subtotal.
   - The decision tree that *assigns* items to categories is a separate board or plate above the schematic, with the continuing route in column 1 (VG-3). It is never interleaved inside the schematic columns.
4. **Aggregation / disaggregation = containment.** A disaggregated line sits *inside* the line it disaggregates (part–whole), never as a sibling row below a total (§2 part–whole; the IFRS 18 Map row already says "nest analysis inside the parent category band"). Use the IAS 2 pattern: nested sub-cell inside the parent outcome (VG-8 nested parts).
5. **Fork grammar + "decision as question" (VG-4, VG-6).** IFRS 18 classification turns on entity-level assessments (e.g. main business activities) and line-level tests. Every one should be drawn as a question with labelled arms. Statements of the conclusion with no arms were the most common IAS 2 FAIL.
6. **Desktop-only viewport (VG-12)** with DOM order still enforced (VG-2). Wide statements will not survive a 420px restack, and Johnny has not asked for mobile. Do not burn effort on mobile layouts, but keep DOM order = narration so the boards stay accessible and future-proof.
7. **Equations (VG-7).** Subtotal identities (profit = sum of categories) read L→R with centred operators, or as statement rules with a rule line. Never a stacked list without operators, and never a waterfall (skill already bans "+" on skeleton bands).
8. **Sources differ (TB-2).** IFRS 18 is new; firm publications will differ on early interpretation. The differ callout lets the body show that honestly without forcing a view.
9. **Drift log (VG-9).** IFRS 18 body sections will follow the Standard's structure while the Maps follow the decision story. Expect more drift than IAS 2 and log it from day one.
10. **Vocabulary (VG-11, QA-1).** Fix the "gate" leak before the first IFRS 18 draft; the IFRS 18 rows in §3 use "gate spine" and "fail-outs" wording that will otherwise be copied into labels.

---

## 5. Anti-patterns to ban explicitly

Each line is suitable as a one-line FAIL in the skills.

1. **TOC order on visuals.** Reordering nodes to make chip numbers ascend when that breaks the decision story. Fix: keep story order, log drift, add the reader note.
2. **Colour-only fixes for a reading-order FAIL.** Recolouring, bolding or re-bordering a board that makes the eye reverse or hunt. Fix: move nodes (geometry + DOM).
3. **CSS-only reordering.** `order:` or out-of-source grid placement to make desktop look right while DOM order (mobile, screen reader) tells a different walk.
4. **Mobile-first design for desktop-only packs.** CF and IFRS 18 are desktop-only; do not restack statements or design around 420px for them. (IAS 2 is the exception: desktop + mobile both required.)
5. **Continuing route on the right** feeding a node that starts on the left.
6. **Decision as statement** — a test written as a heading with no yes/no arms.
7. **Question and outcomes in one box** (mini-flows and Maps alike).
8. **Orphan nodes** — any box with no incoming stem and no parent.
9. **Yes/no on the stem into a decision**, or one label serving two arms.
10. **Red on non-stops** — carve-outs, "not X", or "no further route" drawn red. Green fills as decoration.
11. **Stacked sums without operators**; equations drawn as a process strip.
12. **Pack Map re-teaching or reordering** a chapter Map's decisions; flat numeric lists of disclosures on a jump board.
13. **"Gate" in reader-visible text, labels, aria-labels or comments**; skill examples that model forbidden labels.
14. **Reconciling sources that differ**, or styling one firm's view as wrong.
15. **Unsourced point-chips and author meta** in teaching or Illus bodies.
16. **Inventing substance for a source not attached to the run**, including new chips placed on another source's text.
17. **Densify-down / thinning in a visual pass** — rearranging must keep every sourced item.
18. **Skill rules that point at live HTML ids or labels** as reference shapes; they go stale on the next amend. Describe shapes instead.
19. **Parallel edits to one file** (or reading a file in the same batch as editing it).
20. **Free ①②③ step prefixes** on mini-flow steps or Map nodes (chips carry section numbers, not sequence).

---

## Evidence index (screenshots, `/opt/cursor/artifacts/screenshots/`)

| Topic | Files |
|---|---|
| Fork labels mid-arm (Step A) | `map-yesno-ch0{1,2,3,4}-{desktop,mobile}.png` |
| Ch1–3 Maps after reading-order fix | `checkpoint-ch01-debt-concept-map-desktop.png`, `checkpoint-ch02-debt-concept-map-desktop.png`, `checkpoint-ch03-debt-concept-map-desktop.png` |
| Ch4 column swap + 4.7 decision; 4.5 / 4.6 branch kit | `checkpoint-ch04-ro-*` |
| Ch5 orphan 5.4 nested; 5.1 control question | `checkpoint-ch05-ro-*` |
| Ch6 column swap; 6.2.1 differ unchanged | `checkpoint-ch06-ro-*` |
| Sources-differ callout | `checkpoint-ch06-illus-6-2-1.png`, `checkpoint-ch06-mobile-illus-6-2-1-differ.png` |
| Pack Map before / final; band crops (scope, board, exit equation, disclosure groups) | `checkpoint-pack-map-final-*` |

Pack tarballs: `ias2-opus-ch1-3-debt-2026-10-01.tar.gz`, `ias2-opus-ch4-6-ro-2026-10-01.tar.gz`, `ias2-opus-pack-map-final-2026-10-02.tar.gz` (all under `/opt/cursor/artifacts/`).
