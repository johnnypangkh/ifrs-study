# §10.10 Gate — FAIL rules (addendum)

**Status:** SIGNED text · **applied** on the MF page · page render still **DRAFT-FOR-SIGN** (verification) · **No Build**
**Insert:** §10.10, after §10.9a, in `MAP-MASTER-FORMATTING-PAGE-98.md`.
**Page:** `mf-master-revise.html` and `mf-sec10-gate.html`.
**Does not replace** SIGNED `ba-mf-master-revise.png` (~11:07 HKT). That file stays the chrome lock.
**Cite only:** visual-grammar § Grid conditions 3–4 (Alignment, Layers & hierarchy) · Rail-cell · §6 Timelines. Atlas kits 1–23 stay FROZEN. Kit 25 stays the one timeline. `#27` thick-left stays When-not for Dep.

Essence templates stay. This addendum adds the tests. It does not add chapter Content, and it does not add a fourth building block.

---

## How to measure

Night 1280. Use each box’s border box (`getBoundingClientRect`).

- A difference **greater than 2px** fails.
- **2px or under** passes.
- Compare the two border boxes of a pair. **Do not subtract padding.** Padding and `--space-cell` sit inside the parent.

## What “L1” means here

**L1** in this addendum is the **outer left rail of a beat**: the phase rail, or the first-column section rail.

It is **not** atlas kit **#4 `.m-l1`** (the plate). “L1 never transparent” stays the plate rule. Do not mix the two tests.

## What “needs a rail” means

A right-hand beat needs its own left-rail cell when the reader has to know its name. That is the three signed patterns:

| Pattern | Beat | Rail |
|---|---|---|
| Left label | each named peer or section | one `.inner-rail` on that row |
| Phase + kit 25 | the phase (one timeline pane) | one `.inner-rail`. The phase name **is** that rail |
| Nested layers | each named depth (Outer, Inner, Group, each Peer) | one `.inner-rail` per named row. Add a layer. Do not fold |

These do **not** need their own rail. They sit inside the pane the phase rail already covers:

- kit 25 rings, on-axis markers, the span, Begins / Ceases cards
- a See-also chip on the card it qualifies
- formula terms and unboxed operators
- fork arms and outcomes

---

## 10.10.1 Missing grid — FAIL

**FAIL** when a beat that needs a rail is drawn and any of these is true:

1. The row has a detail and no left-rail cell.
2. The left cell is in the grid and empty (no name).
3. The rail column is collapsed, or the detail spans the full width, while other rows on the same board are rail | detail.
4. Two named beats share one rail (folded into one column).

**PASS** when every such beat has its own named `.inner-rail` on its row. During use is one rail for the whole kit 25 pane. Dep’s signed plate is the control: every named row is rail | detail.

**Exception:** only when Johnny writes one sentence on that mock naming the special logic or story. PM and MD do not write “missing rail OK”, “the head label counts as the rail”, or “a short Dep label covers the rows under it”. An unsigned mock has no exception.

## 10.10.2 Equal height, and the parent covers the children — FAIL

**Row.** The left-rail border box and its detail border box share a top and a bottom.

**FAIL** when `|Δtop|`, `|Δbottom|`, or `|Δheight|` is greater than 2px.

**Parent.** The outer rail and the board that holds its children are that same pair. The rail covers the child board when the row test passes.

**FAIL** when:

- the parent rail is only as tall as its label and the children continue below it
- a child sticks out past the parent board by more than 2px
- the parent is taller than the children by more than its own padding (it claims cover it does not have)

**PASS** on signed Dep: During use `.inner-rail` matches `.tl-pane`; Useful life matches its nest board. The align punch already recorded rail | detail ≤2px as pass. This section puts that test on the MF page.

Words may sit **centered** inside a rail that already stretches. Signed Dep centers `.rail-name`. This gate scores the **boxes**. It does not reopen centering.

Cite: visual-grammar Alignment — “Rail and its detail: equal height, same top and bottom (≤2px)”. Layers — “Parent is exactly as tall/wide as the children it covers.”

## 10.10.3 Phase + kit 25 — markers on the axis; second band = FAIL

One phase pane has **one** kit 25 axis, from Begins to Ceases.

**PASS — on that axis**

- rings at the two ends
- the span between them
- an event of **this** phase drawn on the line (one mark, one leader, one label)
- Begins / Ceases as the end cards of this same axis

Those end cards are kit 25. They are not a second band. A tick whose mark sits on the line is still one axis, including when the leader runs above or below the line (visual-grammar §6 “ticks below” means ticks of this axis).

**FAIL — second band**

A further legend plus a tick row, in its own box, **under** the kit 25 ends, inside the same phase pane. The pane then holds two timelines.

| Instance | What it is | Gate |
|---|---|---|
| Reval after | `.reval-date-row` under `.m-tl`: legend 「Revaluation date」 and two ◆ labels (three copies). The marks are not on the kit 25 axis | **FAIL pattern** |
| Dep before | `.lc-band` Year-end legend + four ticks under the live axis | **FAIL class.** Signed Dep **dropped** it. Putting it back under kit 25 fails |
| Live Reval and Impairment heads | `.lc-head` row 2 = `.lc-band-k` + `.lc-band` under the axis row | **same FAIL class** |

**PASS instead of a second band**

1. Put the event on the kit 25 axis. On the MF template the label is `marker`.
2. A different concept, not a mark on this span, gets **its own rail row** (visual-grammar §6). Dep control: year-end review is the **5.8** peer rail, so Dep’s timeline has no year-end marks.
3. A See-also chip stays on the card it qualifies.

**Still Johnny’s pick, not this page’s:** whether Reval keeps the dates. Dropping them, or drawing them as on-axis markers, both pass this rule. A second band fails either way. `TIMELINE-AUDIT-98.md` P1 and P2 stay open. This addendum does not redraw Reval or Dep.

**Dep chapter lock, separate from the template:** signed Dep During use has no year-end marks on the timeline. Do not read the §9 min’s “Year-end” labels as an order to put them back.

## 10.10.4 L1 short stub against its beat — FAIL

**Yes. FAIL.**

A short outer rail or phase rail whose border box does not cover its beat fails rule 10.10.2. Called out on its own so a one-line phase label is not treated as a special case.

**FAIL**

- Phase name as a text-height label beside a tall kit 25 pane. Live `.lc-head-k` uses `align-self: end` and does this. Signed Dep does not. Do not copy the stub back.
- Outer section rail one line tall beside a nest that continues below it.

**PASS**

- The rail border covers the beat. Dep During use `.inner-rail` | `.tl-pane` (`align-items: stretch`) is the control.
- Reval punch3 **L1 stretch** is this same rule. A later mock that shrinks that rail fails.
- A nested peer rail that is short because **its own** detail is one line, and the two boxes still match within 2px.
- A dropped plate title. Dep and Reval dropped the plate title on purpose. Absence of a title is not a stub. Do not add a title to fill the rail.

## 10.10.5 PM checklist

On the mock, night 1280, for each beat that §10.10.1 says needs a rail:

1. The rail cell is present and named. Otherwise FAIL, unless Johnny’s sentence is on the mock.
2. `|Δtop|`, `|Δbottom|`, and `|Δheight|` against the detail are 2px or under.
3. The parent rail covers the child board by that same test.
4. On a phase timeline, events of that phase sit on the kit 25 axis. A `.lc-band`, `.reval-date-row`, or legend row under the ends is FAIL.
5. The outer / phase rail is not a short stub (§10.10.4).

Essence check on the MF page itself: labels stay `Phase` / `Peer` / `Outer` / `Start` / `End` / `marker`. Chapter sentences stay off the template cards.

## 10.10.6 Lines replaced on the applied page (P2, P3)

The applied HTML no longer uses the old sentences. The frozen PNG still shows them. Gate from the applied page, not from those PNG pixels.

| Old line on the PNG | Applied reading |
|---|---|
| Phase card: “no YE markers on signed lock” | Replaced. Dep’s year-end review is rail 5.8. That chapter lock is not a ban on on-axis markers, and it does not allow a second band. |
| Phase recipe: “optional markers” | Replaced. Markers of this phase sit on the kit 25 axis. A second band fails. |
| §9 min “Year-end” and “Depreciate over useful life” | Replaced with `marker` and `span (Start→End)`, plus the second-band caption. |

## 10.10.7 Stays as signed

- `ba-mf-master-revise.png` (~11:07) — three patterns, `.inner-rail`, kit 25, nest. File unchanged.
- The three building blocks in §10.0. This gate is not a fourth component.
- dep-v2 unify-A freeze. This note does not reopen Dep chrome.
- Atlas 1–23. No new kit ID. No new token.
- `#27` When-not footnote.
- PR **#163** is a different job. Do not merge it from this work.
