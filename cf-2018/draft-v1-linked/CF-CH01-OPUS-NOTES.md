# CF 2018 Ch1 Objective & users — storyline-first redraw (Opus)

**Scope.** `refs/cf-2018/draft-v1-linked/visuals/ch01-objective-users.html` + `.css` only.
- `ch01.html` was not uploaded. Suggested iframe cache-bust: `?v=cfch1-8` → `?v=cfch1-9`.
- `shared.css` is the uploaded CF copy, unchanged (`node tools/check-chapter.mjs cf1`).
- Baseline upload commit: `6f64148` (the local try, byte for byte).

## Story → picture

| Story beat | Drawn as | Visual type |
|---|---|---|
| 1. Primary users need information for resource-provision decisions | Users card with the three-party cast; the need is the card's last line | **Party cast** inside one actor card |
| 2. They cannot demand custom reports, so the entity provides GPFS | One left-to-right scene: **Primary users — rely on — GPFS — provided by — Reporting entity**. Under it, a muted direct path from the users card to the entity card, with the gap filled by "Tailored reports on demand — most users cannot require them" | **Relationship scene** with labelled stems, plus a **contrast path** (the route that doesn't exist) |
| 3. The objective of those GPFS | Inside the GPFS card, under a rule: "Objective — useful financial information … for those resource-provision decisions · not special-purpose reports" | **Containment**: the objective belongs to the object |
| 4. Which decisions | Three columns in one frame | **Peers** (same-format columns) |
| 5. Both assessments, for any decision | Two rows spanning all three decision columns; the stewardship tag sits on the accountability row | **Spanning bars** |
| 6. Accrual and cash flows are complementary | One frame split into two halves, with a shared foot row | **One object, two lenses** (split frame, not a "vs" pair) |

Accent means only "the GPFS route" (the GPFS card and its two stems). Everything else is neutral. Weight steps down by section: the scene has full cards, the decisions have 1px rules with a band on the spanning rows, and the lenses are a single 1px frame.

## Diagnosis of the local try → move

| Local try | Problem | Move |
|---|---|---|
| Six stacked cards of near-equal weight | Reads as a list the narrator walks through, so relationships aren't visible | Beats 1–3 become one scene, where the relationships are the stems |
| "Custom reports **vs** Entity provides GPFS" | "vs" suggests two options; the story is "can't, so" | The custom route is drawn as a muted direct path users → entity that doesn't deliver; the GPFS route is the accented one |
| GPFS card, then a separate "Objective of those GPFS" hub | One object drawn twice | Objective sits **inside** the GPFS card |
| Chip 1.2 on the objective **and** on "Which decisions" | Chip duplication | Each chip once: 1.3 users, 1.2 GPFS/objective, 1.5 and 1.4 on the assessment rows, 1.6 on the lenses |
| "Which assessments — both feed every decision type" + a bar "Users need both assessments for any of the decision types" | Said twice, and still not drawn | Assessment rows **span** the decision columns, so "both, for every decision" is the geometry; the label states it once |
| "CF WORDING" tip box under accountability | Layout-meta kicker, extra box | One inline tag: "CF term: *stewardship* · not a second objective" |
| Accrual ∥ Cash as two cards + "complementary" in the title + a bar repeating it | Two separate cards read as alternatives; the idea is stated three times | One frame, two halves; the foot row carries the one relationship (both inform prospects for future net cash inflows) |
| Every card in accent border | Colour with no meaning | Accent only on the GPFS route |

**Count.**
- Before: 18 boxes and 6 chips.
- After: 9 framed boxes (3 scene cards, 3 parties, decisions frame, lens frame, stewardship tag) and 5 chips.

**Narrow layout.**
- At ≤760px the scene stacks as Users, "rely on", GPFS, "provided by", Entity, with vertical stems that meet the card edges. The direct path becomes a muted ruled note under the entity.
- At ≤640px the decision columns and the two lenses stack.

## Method (principles PM can reuse)

1. **Write the story as sentences first, then find the nouns and the verbs.** Nouns become objects (users, GPFS, entity). Verbs that link two nouns become labelled stems ("rely on", "provided by"). Verbs that describe one noun stay inside it.
2. **One scene per causal beat, not one card per sentence.** If sentences 1–3 all describe the same three actors, draw the actors once and let the stems carry the sentences.
3. **Show a "cannot" as the missing route.** Draw the route that would exist (users → entity directly) muted and broken where it fails, beside the route that does exist. This beats a "vs" pair.
4. **Purpose lives inside its object.** An objective, definition or scope of X is containment in X, not a new box after it.
5. **"For every X" is a span.** When a rule applies to every member of a set, draw the set as columns and the rule as a row across them. Don't add a bar that says "for every".
6. **Complementary is one frame with two halves.** Alternatives are two frames; complements share an edge and a foot row.
7. **Stems only between objects that the story connects, with the verb on the stem, reading left to right.** No stems between sections; the section label names the link ("Those decisions …").
8. **Colour one route.** Here accent = how the information actually reaches users.
9. **Chip once, on the object the section is about.** Detail rows under a chipped object don't repeat its chip.

## Johnny to confirm

1. **Reporting entity as an actor.** The prior local round said the reporting entity is not an actor; this story needs the "provided by" end. It is drawn neutral and small. Confirm.
2. **Stem verbs.** "rely on" follows CF 1.5 ("must rely on general purpose financial reports"). "provided by" is my wording for the entity end.
3. **Wording carried or condensed.** The decision wording is condensed from CF 1.2(a)–(c). "Management accountability — how efficiently and effectively management has used the entity's resources" is condensed from CF 1.4(b).
4. **Lens bodies are my condensation.** Accrual: "Effects shown in the period they occur, even when cash moves in another period" (CF 1.17). Cash flows: "How the entity obtains and spends cash — liquidity, borrowing and investing" (CF 1.20). The foot row, "both inform prospects for future net cash inflows", is also my wording.
5. **"existing and potential"** added under Primary users (CF 1.2).
6. **Chip → anchor mapping** is kept from the local try (1.3 users, 1.2 objective, 1.5 cash inflows, 1.4 accountability, 1.6 lenses). `ch01.html` was not uploaded, so the ids `#s-1-2` … `#s-1-6` are unverified here.
7. **Party glyphs** (emoji) are kept from the shared `.party` kit.

## Known limits

- Preview uses shims for `assets/theme.js` (not uploaded), and the visual was shot standalone at 1280, 920 and 390. Re-check inside the real `ch01.html` fieldset. The empty space below the map in the local-try screenshot is the site-wide iframe-fit ratchet, which is out of scope.
- The direct-path text sits in the line's gap. If Johnny wants a stronger "blocked" cue, add end ticks at the gap; no glyphs.
- Subgrid (the direct path) needs a current browser. Older browsers fall back to a plain muted note row.
- LOCK-STAMP not restamped.
