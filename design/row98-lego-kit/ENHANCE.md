# ENHANCE — optional proposals

**Status:** every item is a **PROPOSAL** for Johnny. None is applied, and none is needed to finish STANDARDISE.

Each item gives:
- one line on why;
- what changes (file, class, section);
- what it does to wording;
- the mock.

Rule 10 still holds: each item is drawn on the Master formatting page first, signed, then rolled out.

Each item is small and can be undone on its own: it touches one section of one map first, and you can stop there.

In the mocks:
- **Before** panes are live crops.
- **After** panes are the same live map with the proposal CSS injected at render time (`tools/before_after.py`). E7 also moves the live words into child cells at render time, with nothing added. E5 is the exception: it is drawn with tokens only (`tools/build_ba_pages.py`).

---

### E1 · PROPOSAL — stacked groups get a left rail, not a top kicker
- **Why.** Rules 2–3: a group label on the left and only that group's content on a grid to its right. Then every group on a map sits on one rail track and new items can be added to the grid.
- **What.** CF ch01 `.ou-sec` becomes a 2-column grid (shared rail track `calc(5*var(--space-6)+var(--space-2)+var(--stroke-1))`, as signed in unify-A). `.ou-label` takes the `.inner-rail` chrome. Its content (`.ou-scene` / `.ou-grid` / `.ou-lenses`) moves to column 2, unchanged.
- **Where next, if signed.** Other CF / IFRS 18 maps that stack labelled groups with a top kicker (`.pa-label`, `.ts-label`, `.zone-head`, `.pd-kicker`; list in `CENSUS.md` §2). Each one is a separate sign-off.
- **Wording.** None changed. The label keeps its text; only the CSS uppercase is dropped, so it reads like other rails.
- **Mock.** `mocks/E01-kicker-to-rail.png`

### E2 · PROPOSAL — show “Asset AND (one of three)” on IAS 2 ch01 §1.1
- **Why.** Rule 4: the definition is an AND of an OR-set. Today a lone `+` (`div.st-plus`) sits between *Asset* and the three cases, and nothing groups the three.
- **What.**
  - `div.st-plus` shows the signed AND pill (MF §9) in place of `+`.
  - `div.classes` gets an open bracket (solid 1 px `--line`, top and sides, no bottom). A bracket, not a box, because it groups the three cases rather than holding them as one idea.
  - `span.or` becomes a small OR pill.
- **Wording.** None. “AND” replaces a glyph, as in STANDARDISE S2.
- **Mock.** `mocks/E02-and-of-or.png`

### E3 · PROPOSAL — each IAS 16 exclusion shown once (ch01 §1.3)
- **Why.** Rule 7: *Excluded from IAS 16?* lists the four exclusions in `.q .item-rows`. The *IAS 16 does not apply* branch then shows the same four as `.carve` cards, each with its See-also (IFRS 5, IAS 41, IFRS 6).
- **What.** Hide the `.item-rows` inside the question; the cards stay.
- **Wording.** Changes what is shown: the question loses its list. The cards drop the bracketed standard after each item (“(IFRS 5)”), but each card's See-also already names that standard, so nothing is lost. That is why this is a proposal, not a formatting fix.
- **Mock.** `mocks/E03-exclusions-once.png`

### E4 · PROPOSAL — peers share one row grid (reads as a matrix, no new words)
- **Why.** Rule 1: prefer pivot / matrix. IFRS 18 ch05 §5.1 *How the face can present OpEx* has three peers (`.oe-opt`: *Nature*, *Function*, *Mixed*), each with the same three rows: head, body, example. Today each card has its own heights, so the rows don't line up across.
- **What.**
  - `.oe-options` gets `grid-template-rows`.
  - Each `.oe-opt` spans 3 rows with `grid-template-rows: subgrid`, plus a hairline between rows.
  - The cards stay; the head, body and example rows now line up across all three.
- **Where next, if signed.** Other peer sets whose cells repeat the same inner rows. Each needs checking first. IAS 16 ch05 `.method-set` already equalises its cells (`data-eq`), and the CF ch02 §2.5 peers have inner rows that ask different questions, so neither is proposed.
- **Wording.** None.
- **Mock.** `mocks/E04-shared-row-grid.png`

### E5 · PROPOSAL — the echo bar on IAS 2 chapters
- **Why.** Rule 6: IAS 2 ch01–ch06 walk a life cycle just as IAS 16 does. IAS 16 ch04, ch05 and ch06 show the reader where they are on it (`nav.master-echo`); IAS 2 shows nothing.
- **What.**
  - Reuse the IAS 16 echo recipe: kicker, step pills, current step in accent, later steps faded.
  - The steps are the six IAS 2 chapter titles (`ias-2/draft-v1-linked/ch01–ch06.html` `<title>`).
  - Standardise first: today the echo CSS is written three times, once per map, in `ias16.css` (`.ppe.dep-map.ch05-map .echo-*` from L5979, `.ppe.models.ch04-map .echo-*` from L6215, `.ch06-map .echo-*` from L6472). It would move to one shared rule before reuse.
- **Wording.** The step names are existing titles. The kicker “Master path” is IAS 16's label, so using it on IAS 2 is new text on a map and needs Johnny's OK.
- **Mock.** `mocks/E05-echo-bar-ias2.png`

### E6 · PROPOSAL — put the Master formatting page in the repo
- **Why.** Rule 10 says formatting is defined on Master formatting and signed first. But the repo has no such page on any branch.
  - The latest draft, `mf-master-revise.html` (upload), is marked “DRAFT-FOR-SIGN HOLD”.
  - The signed kits live only in `/cursor/stores/bot/row98-handover/` and `dep-v2.html`.
- **What.** One page under `design/` (not linked from the site) that draws each brick and component in `LEGO-BRICKS.md` / `LEGO-LOGIC.md`, with a “signed / not signed” stamp per item. Every STANDARDISE and ENHANCE item is drawn there before it reaches a chapter.
- **Wording.** None (process).
- **Mock.** None. `lego-sheet.png` and `lego-combos.png` are the starting content.

### E7 · PROPOSAL — a text-dump cell is a cue to go one layer deeper
- **Why.** Owner heuristic (2026-10-19), with the signed rules “add layers, never fold”, “prefer pivot / matrix” and “wrap rows across”. When a cell runs a list as one line of prose, the reader has to parse it; one more grid layer lets them see the items. There is no depth cap (`LEGO-LOGIC.md` snap rule 1), and S13 depth-cut is on HOLD.
- **Rule.** `LEGO-LOGIC.md` snap rule 9 says when to go deeper, which component to build inside the cell, and where to stop (one idea per cell).
- **What (two live examples, mocked):**
  - **IAS 2 ch02 §2.2 *Indicators that control has passed*** (`.st-list .cell > span.cell-body`). Today it is one line: “Present obligation to pay; physical possession; legal title; risks and rewards of ownership; acceptance — evaluated together under IFRS 15, none individually determinative”.
    - After: five peer cells, wrapping across, and a junction bracket under them carrying “evaluated together under IFRS 15, none individually determinative”.
    - It is *not* an AND-gate: the map says the indicators are weighed together and none decides alone. So there is no AND pill, just peers plus a bracket (K1 + B13).
  - **IAS 2 master §3.6 *Not included in the cost of inventories*** (`.m-sum > p.m-out`). Today it is one line after the title: four items, then “Recognised as expenses in the period incurred.”
    - After: chip + title, then a wrapped 2 × 2 grid of the four items, then the consequence as a Note.
    - This adds one bordered layer inside the *Cost of inventories* plate, which is the point under the new rule.
- **Wording.** No word added, removed or reordered. Only separators change role:
  - `; ` becomes a cell boundary;
  - “ — ” becomes the bracket;
  - the full stop before “Recognised …” becomes the Note break.
  
  First letters are capitalised by CSS (`::first-letter`), as in S3. The mocks build this at render time (`tools/before_after.py`, jobs `E07-*`). The live files are untouched.
- **Where next, if signed.** `TEXT-DUMPS.md` (generated by `tools/text_dumps.py`) lists 13 strict candidates on 9 maps, each an inline run of ≥ 150 characters with ≥ 2 `;` / `·` separators. For example:
  - IAS 2 ch03 `.leaf-note` (same §3.6 list);
  - IAS 2 master *Measure NRV* §4.5–4.6 *Estimates of NRV*;
  - IFRS 18 ch04 `.ts-regime-eg` *Listed IFRS subtotals*;
  - IFRS 18 ch02 *Rules shared by both roles* §2.2;
  - CF ch09 / ch10 / ch11 header lines (“·”-joined).

  Looser candidates that suit other components are named in `LEGO-LOGIC.md`:
  - K2: IFRS 18 index *Other FS impacts*;
  - K3: the IAS 16 ch04 impairment-reversal tip;
  - K10: IAS 2 ch04 §4.5 *Purpose for which the inventory is held*.

  Each one is its own sign-off.
- **Mock.** `mocks/E07-text-dump-deeper.png`

---

## Sign-off order (if any are wanted)
1. **E6**: it is where the others get signed.
2. **E7, E2, E4**: one section each; E7 sets the rule the later candidates follow.
3. **E1**: one map first (CF ch01).
4. **E5**: after the echo CSS is made shared.
5. **E3**: content-visible; last.
