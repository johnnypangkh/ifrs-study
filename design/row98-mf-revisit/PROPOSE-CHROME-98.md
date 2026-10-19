# PROPOSE — chrome inventory for Johnny to sign

**Status:** PROPOSE only · DRAFT-FOR-SIGN · No Build · signed BA not overwritten
**Sign against:** `mf-sec10-gate.html` (the page delta) and `MF-SEC10-FAIL-ADDENDUM-98.md`
**Do not merge** PR #163. This file does not edit it.

The signed inventory in §10.0 stays three patterns, one chrome family. Nothing below adds a kit ID, a token, or a fourth building block.

## Signed inventory (unchanged by this propose)

| # | Building block | Chrome |
|---|---|---|
| 1 | Primary left label | live `.inner-rail` + `.rail-name` |
| 2 | Phase + timeline | left `.inner-rail`; right kit 25 |
| 3 | Nested layers | nested `.inner-rail` / wrap-row |

`#27` thick-left stays the When-not footnote (IFRS 18 `.m-strip` / Rec mock-only).

## Asks

### P1 — Add the gate to the MF page

Put §10.10 on the Master formatting page, under the decision strip: the four FAIL tests and the abstract pass/fail minis on `mf-sec10-gate.html`.

This is new **page** copy on a signed BA. It is not a new map component.

**Recommend: sign.** Without it on the page, PM still has to leave MF to find the test.

### P2 — Replace two lines on the Phase card

On component 2 (Phase + kit 25), replace:

- “Not for: … YE legend dump” / “no YE markers on signed lock”
- recipe “rings ON axis · optional markers”

with the §10.10.3 sentences:

- Markers of this phase sit on the kit 25 axis (one mark, one label).
- A second band under that axis, inside the same pane, fails.
- Dep’s year-end review is its own rail (5.8), so Dep’s timeline has no year-end marks. That is the chapter lock, not a ban on markers.

**Recommend: sign with P1.** Those two lines are the sentences PM read two ways.

### P3 — Relabel the §9 timeline min

The signed min still prints chapter words: “Year-end” twice, span “Depreciate over useful life”. Kit 25 geometry (rings, leaders, Begins/Ceases) stays.

Propose the specimen labels become abstract, matching §10:

- tick labels → `marker`
- span → `span (Start→End)`
- one caption: “Second band under this axis = FAIL.”

**Recommend: sign.** Leaving “Year-end” on the min keeps the Dep-band reading alive. Until this is signed, §10.10.6 tells PM those words are a frozen specimen label, not the rule.

## Explicitly not inventory

| Idea | Verdict |
|---|---|
| A second-band component (keep `.lc-band` / `.reval-date-row` as kit) | **No.** It is the FAIL pattern, not a block. |
| An empty-rail or stub component | **No.** Those are missing or short instances of blocks 1–3. |
| New kit ID, new token, atlas edit | **No.** |
| Reval redraw (drop dates vs on-axis dates) | **Out of this page.** Timeline audit P1/P2. This propose only forbids the second band. |
| Dep chrome reopen | **No.** dep-v2 stays frozen. |
| Merge PR #163 | **No.** |

## Sign line

| Ask | Johnny |
|---|---|
| P1 Gate on the MF page | |
| P2 Phase-card sentences | |
| P3 §9 min labels → `marker` | |

Recommend **yes / yes / yes**. The three blocks and the tokens stay.
