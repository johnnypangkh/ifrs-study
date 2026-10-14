# CF Ch3 Concept Map — bold grammar (2026-10-03)

Checklist: Brief attached · Ch3 map tgz attached · visual-grammar skill attached · Official/Big4 not needed.

Viewport: CF 2018 desktop only, **1280**, dark. No mobile pass.

Files: `cf-2018/draft-v1-linked/visuals/ch03-reporting-entity.html` and `ch03-reporting-entity.css`. `shared.css` was read and not edited. The skill file was not edited. No wording was added or removed. Layout, chips, and structure colours are unchanged.

The tarball did not include the Ch1, Ch2, or Ch4 maps. Role weights were checked against `shared.css` (landmark names 700, body muted and regular, see-also note regular).

Screenshots:

- Before, full map: `screenshots/ch03-map-1280-before.png`
- After, full map: `screenshots/ch03-map-1280-after.png`

## Story and visit (unchanged)

This was a weight pass, not a redraw. The story on the board is still the one in the file header.

Financial statements are one particular form of general purpose financial report. They carry an objective (the elements; future net cash inflows and stewardship), the places that information appears, and the reporting period they are prepared for. Entity perspective and going concern are two readings of those statements, same rank, and they stop there. The statements are about a reporting entity. Inside that plate: the usual parent–subsidiary boundary beside the consolidated and unconsolidated readings, a lighter harder-boundary rail, and combined statements as a one-line acknowledgement.

Visit, unchanged: title → objective and the two uses → three places → period axis → perspective ∥ going concern → stem “are about” → reporting entity → consol plate beside the two readings → harder rail → combined note.

## Bold grammar

Three weights. Meaning uses `<strong>`. Role uses CSS. They are not mixed inside one sentence.

| Weight | Colour | Use |
|---|---|---|
| **700** | accent | Landmark titles: Financial statements, Objective, Reporting period, Entity perspective, Going concern, Reporting entity |
| **700** | ink (flank ticks stay muted) | Names of primary objects: the three places, the three period ticks, the two captions, Parent / Subsidiary A / B, Consolidated / Unconsolidated |
| **600** | ink | Lock words only, via `<strong>` |
| **600** | ink | Decision questions (“How is the whole viewed?”, “Will it keep operating?”) |
| **600** | accent | The relationship stem “are about” |
| **600** | muted | Short relationship word “controls”; the secondary rail heading “Harder boundary” |
| **400** | muted | Prose, connectives, examples, see-also chips, the three criterion chips, the inline combined label |

Rules for `<strong>`:

- Bold the word the learner must lock: a concept, a gate, or an outcome.
- A joining **and** / **or** stays regular. The “and” inside the element list stays inside that one `<strong>`, because the five elements are one lock, not two gates.
- A prohibition keeps its “not” inside the `<strong>` (`not a substitute`, `not necessarily`, `Not a legal entity`, `not elements`, `does not say when or how`). Bolding only the noun under a “not” would lock the wrong idea.
- Examples and restatements stay regular.

`<strong>` is always 600 and ink, in every plate. It does not climb to 700, so a lock word cannot equal a title.

## What was wrong (before)

Measured in the browser, not from the stylesheet alone.

**1. Plate titles were regular.** `.re-map h2, .re-map h3 { font: inherit }` has specificity (0, 1, 1). `.re-name`, `.re-period-name`, and `.re-hard-name` are (0, 1, 0), so the shorthand won and wiped the authored size and weight.

| Title | Authored | Rendered before |
|---|---|---|
| Financial statements | 15px / 700 | 14px / 400 |
| Objective | 15px / 700 | 15px / 400 (a later rule saved the size only) |
| Reporting period | 15px / 700 | 14px / 400 |
| Reporting entity | 15px / 700 | 14px / 400 |
| Harder boundary | 13px / 700 | 14px / 400 |
| Entity perspective, Going concern (spans, so the reset missed them) | 15px / 700 | 15px / 700 |
| Combined financial statements (span) | 12px / 700 | 12px / 700 |

The same role did not share a weight. The secondary combined label was heavier than the plate title above it.

**2. The two usefulness locks were the wrong weight and the wrong colour.** `future net cash inflows` and `stewardship` sit in `.re-dual`, outside the old `strong` list, so they fell through to user-agent bold: **700 and muted**. The joining “and” was a class at **600 and ink**. The connective was brighter than the two gates.

**3. Two other “and”s were the only `<strong>` in their sentence.** Forward-looking information, and the harder-boundary test. The gates around those conjunctions were regular.

**4. The cash-flows row lifted the whole line to ink** (`.re-ink`), including the connective “important”. `not elements` was not a lock.

**5. See-also chips were 600**, the same tier as lock words and the stem “are about”.

## Before / after

Wording is identical. Only weight moved.

**Usefulness.** Before: `future net cash inflows` and `stewardship` were 700 muted; **and** was 600 ink. After: the two gates are 600 ink; **and** is 400 muted.

**Forward-looking.** Before: only **and** was bold. After: **relates to those elements** and **is useful**. The example, and “Not management’s expectations and strategies”, stay regular.

**Cash flows.** Before: the whole row was ink, and only **Cash flows** was semibold. After: **Cash flows** and **not elements**. “important” stays regular.

**Harder boundary.** Before: only **and** was bold, and the heading did not receive its authored weight. After: the heading is 13px / 600 muted (a secondary rail name, not a landmark 700). The two conditions are **Not a legal entity** and **not only legal entities linked as parent–subsidiary**. **primary users’ needs** stays the lock on the next line. The three criterion chips stay 400; the border already marks them, and bolding the chips would turn the secondary rail into a second bold column.

**Opening line.** After: **particular form**. The rest of that sentence stays regular. The plate title is now actually 700, so the line does not need a second landmark.

**Combined.** Before: the name was 700 and the point was regular, so the acknowledgement looked like another title and the outcome did not. After: the name is 400 (inline secondary label). The lock is **does not say when or how**.

**See IFRS 10 / See IAS 27.** 600 → 400. The dashed chip still marks them as see-also. The gloss (“control”, “label only”) stays 400 and quieter by colour.

**Titles that were already right, and now match the headings.** Place names, tick names, captions, Parent / subsidiaries, Consolidated / Unconsolidated stay 700. Questions stay 600. “are about” and “controls” stay 600. Locks that were already on the right words stay, and now share one rule: **as a whole**, **continues in operation**, **different basis**, **not necessarily**, **one**, **alone**, **not a substitute**.

## Left regular on purpose

Not densified, and not new claims:

- Place lines (“Recognised assets, liabilities and equity.” / “Recognised income and expenses.”)
- Tick explanations, including the brighter “This period” card (colour and fill already mark that tick; the words stay 400)
- “separate from its capital providers” (restates **as a whole**)
- “Non-controlling interests are equity of that whole.”
- “and they describe that basis”
- “A parent may still prepare them in addition.”
- “required, or chooses” (the plate title carries Reporting entity; the non-obvious gate remains **not necessarily**)
- The org-chart note, “A legal entity, or legal entities linked by control, is the usual boundary.”
- The three faithful-representation chips

## CSS mechanism

- Heading reset is `margin: 0` only. A `font` shorthand on `h2` / `h3` must not come back; it outranks a single-class role.
- Title roles are scoped `.re-map .re-name`, `.re-map .re-period-name`, `.re-map .re-hard-name`.
- One rule, `.re-map strong`, sets every lock to 600 / ink so a container cannot miss the list again.
- Iframe cache query: `?v=cf2018-ch03-map-20261003-bold`.
