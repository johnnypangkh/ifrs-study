# 7B2 Map nodes — key changes (2026-10-03)

Attach checklist: Brief attached · maps-visuals.tgz attached · visual-grammar skill attached · Official/Big4 not needed.

Scope kept to Map node chrome. No new teaching claims. Skill MD, teaching-body `chNN.html`, jump chips (#7b1), point-chip wrap (#7b3), CF Ch7 leak (#7b4), section markers (#7b5), and Homepage were not edited.

Screenshots are 1280-wide, night. Ch9–Ch11 chapter CSS already paints a night page. The Ch5 shot sits the transparent embed (`body.embed { background: transparent }`) on a night canvas for the photo only; that file was not edited.

## Inventory

| Where | What the reader sees | Role | Call |
|---|---|---|---|
| `cf-2018/.../ch09-combined.html` 9.1 | `span.dec-tag` “Decision” before the question | Badge on a question that already forks Yes/No | **Drop** |
| same, 9.2 | same badge | same | **Drop** |
| `cf-2018/.../ch10-carve.html` 10.1 | same badge | same | **Drop** |
| same, 10.3 | same badge | same | **Drop** |
| `cf-2018/.../ch11-status.html` 11.2 | same badge | same | **Drop** |
| Ch9 / Ch10 / Ch11 zone heads (Label, Boundary, Portion, Status) | Uppercase plate name | Names which test the plate is | **Keep** |
| Ch9 / Ch10 / Ch11 `.mid` Yes / No | Arm label inside each outcome card | Tells the two arms apart | **Keep** |
| Ch9 / Ch10 / Ch11 `aria-label="Decision — …"` | Not visible | Names the plate for assistive tech | **Keep** |
| Ch9 / Ch10 / Ch11 continuing stems (“Yes continues…”, “No continues…”) | Rule between plates | Names which arm enters the next plate | **Keep** |
| `ifrs-18/.../ch03-classification-path.html` `.pc-gate` | Question box, no “Decision” or “Gate” text | The decision node itself | **Keep** |
| same, `.cp-kicker` | “Ordered classification tests…” | Board title | **Keep** |
| same, entry line “If yes, it must sit in one of the five categories.” | Muted line under the entry question | Entry rule, not a badge | **Keep** |
| same, “Answer no here if a specified main-business activity…” | Muted line on the investing and financing questions | Exception on the test it changes | **Keep** |
| same, category leaves | Operating / Investing / Financing / Income taxes / Discontinued colours | Destination category (same tokens as the P&L schematic) | **Keep** |
| `cf-2018/.../ch05-recognition-derecognition.html` | Questions + labelled stems; no Decision badge | Reference fork | **Keep** (unchanged) |
| IAS 2 maps (`ch01`–`ch06`, `map-formula-board.html`) | `aria-label="Decision: …"` only | Not a visible badge | **Keep** |

No other reader-visible “Decision” or “Gate” label turned up in the IFRS 18, CF 2018, or IAS 2 map HTML.

## Drop — five Decision pills

Each dropped pill sat in front of a question that already ends in “?”, with a Yes card and a No card under it and a stem that says which arm continues. The badge only renamed that structure. Ch5 already teaches the same fork with the question and the stems alone, and that board has no Decision pill.

Removed:

- The five `<span class="dec-tag">Decision</span>` nodes.
- The unused `.dec-tag` rules in `ch09-combined.css`, `ch10-carve.css`, and `ch11-status.css`.
- Cache-bust on those three stylesheets: `cf2018-ch09-map-20261003`, `cf2018-ch10-map-20261003`, `cf2018-ch11-map-20261003`.

Wording of the questions, outcomes, stems, and source-differ lines is unchanged.

## Light layout — Ch11 11.2 arms only

On 11.2 the next plate is the IAS 8 gap-fill, and the stem already said “No continues”. Yes (“Apply the Standard”) does not enter that plate. Before the edit, Yes sat on the left and No on the right, so the continuing arm was the right-hand card.

The two outcome cards were swapped. No is now the left card (the route into 11.3). Yes is the right card (apply the Standard and stop this spine). No sentences were added or rewritten.

Ch9 and Ch10 already put the continuing Yes arm on the left. Those arms were left as they were.

## Keep — IFRS 18 classification path

`.pc-gate` is the question box, not a Decision/Gate chip. Nothing on the board says “Decision” or “Gate”.

The walk is forced: entry question → “yes → test in order” → each later question sends **yes** right into a category leaf and **no** down the left spine → the last no lands on Operating, the residual default. Short questions stay in a shared left column so the yes stems line up; that empty interior is the aligned spine, not an orphan box.

Category colour names which leaf you landed on. It is not a green “continue” fill. Operating uses the operating category token.

The entry sentence, the two main-business exceptions, the kicker, and the 3.5 cue were left in place. Cutting them would drop teaching lines, not chrome.

## Keep — CF Ch5 and IAS 2

Ch5 is already the fork without a Decision badge: definition question, no-arm to “Not that element”, yes-stem into the usefulness plate, no-arm to “Do not recognise”, yes-stem into Recognise, later plate for derecognition. No Ch5 Decision box was still present. File untouched.

IAS 2 uses `aria-label="Decision: …"` on structure sections. Those labels are not painted. They were not removed.

## Reading order after the edit

- **Ch9:** 9.0 → 9.1 question → Yes (left, combined) beside No (right, consolidated / carve-out) → “Yes continues — boundary” → 9.2 → Yes beside No → “Yes continues — what binds the activities” → 9.5 peers → 9.6 → 9.7 → see also.
- **Ch10:** 10.0 → 10.1 question → Yes (left, carve-out) beside No → “Yes continues — boundary” → 10.3 → Yes beside No → “Yes continues — preparing the carve-out” → 10.4 ∥ 10.5 ∥ 10.6 → 10.7 ∥ 10.8 → see also.
- **Ch11:** 11.0 → 11.1 three uses → “Applying the Framework to a transaction” → 11.2 question → No (left) beside Yes (right, apply the Standard) → “No continues — IAS 8 gap-fill order” → 11.3 → 11.4 ∥ 11.5 → 11.6 ∥ 11.7 → see also.
- **I18 classification path (unchanged):** entry question → ordered tests down the left → yes exits right to a category → last no is Operating → 3.5 cue.
- **Ch5 (unchanged):** 5.1 → 5.2 → no exits right / yes down → usefulness → no exits right / yes down → Recognise → later → 5.6.

## Files touched

- `cf-2018/draft-v1-linked/visuals/ch09-combined.html`
- `cf-2018/draft-v1-linked/visuals/ch09-combined.css`
- `cf-2018/draft-v1-linked/visuals/ch10-carve.html`
- `cf-2018/draft-v1-linked/visuals/ch10-carve.css`
- `cf-2018/draft-v1-linked/visuals/ch11-status.html`
- `cf-2018/draft-v1-linked/visuals/ch11-status.css`
