# Concept Map — orphan Standard “para NN” prose (2026-10-03)

Global pass on every IFRS 18 Concept Map (`ifrs-18/draft-v1-linked/visuals/*.html`, Ch1–Ch8 plus `map-jumpboard.html`). After the cite-chip strip, map prose still named Standard paragraphs. Those numbers had nothing on the board to point at. Labels are now teaching words, and a pack section jump (`a.fb-num`) only where that rule lives in a chapter section.

No cite chips were added. IAS 2 was not edited. Teaching `chNN.html` bodies are not in this tree. Skill markdown was not edited. Parent iframe `?v=` was not bumped.

## Gate

Case-insensitive scan of `ifrs-18/draft-v1-linked/visuals/` (HTML and CSS, including `title` and `aria-label`):

- `\bpara(graph)?\s+[0-9]`
- `\bparagraph\s+[0-9]`

Result: **zero matches**. No intentional exception.

The same two patterns are also zero in `cf-2018/draft-v1-linked/visuals/`. Visible “CF x.y” and “IAS 8.11” map labels that were the same class of orphan locator were rewritten. HTML comments were not (see below).

`para C3` does not match `\bpara\s+[0-9]` because of the letter. Those appendix locators were rewritten anyway.

## IFRS 18 — before / after

### `ch01-whats-new.html`

| Before | After |
|---|---|
| subject to paragraph 73 | unless the financing exception applies |
| pointer row `Ch3 · Ch4` | `Ch3 · Ch4` kept, plus `a.fb-num` **4.2** → `ch04.html#s-4-2` |
| Retrospective · annual para C3 · first-year interim para C4–C5 | Retrospective · **8.3** annual reconciliation · **8.4** first-year interims |

Existing chips 1.1, 1.2, 1.4, and 8.1 were not retargeted.

### `ch02-pfs-aggregation.html`

| Before | After |
|---|---|
| aria-label “Paragraph 41 aggregation checklist” | “Aggregation test checklist” |
| column head “Para 41 test” | “Aggregation test” |
| apply paragraph 41 through shared characteristics, roles and no obscuring | apply it through shared characteristics, roles and no obscuring |
| labelling tip ending `· B16–B26` | ending at “no unexplained leftover bucket” |

The 2.3 chip already titles this block. The 2.4 chip already jumps to the labelling section, so the bare appendix range was not left as a second locator. CSS was not changed.

### `ch03-classification-path.html`

| Before | After |
|---|---|
| kicker ending `(para 47–68)` | Ordered classification tests — income and expenses into categories |

No new chip. The maps do not already use one section id for that whole range, so none was invented.

### `ch03-mba-nest.html` and `ch03-pnl-categories.html`

Scanned. No `para` / `paragraph` + number. Not edited.

### `ch04-totals-subtotals.html`

| Before | After |
|---|---|
| aria-label “Paragraph 73 exception to this subtotal” | “Exception — financing amounts in Operating” |
| Para 73 exception | Exception — financing amounts in Operating (chip **4.2** kept) |
| the paragraph 65(a)(ii) policy choice classifies raising-finance amounts in Operating | a policy choice puts raising-finance amounts in Operating |
| aria-label “Required versus section 118 listed versus MPM” | “Required versus IFRS-listed versus MPM” |
| Required vs para 118-listed vs MPM | Required vs IFRS-listed vs MPM (chip **4.4** kept) |
| IFRS subtotal (required or para 118) | IFRS subtotal (required or IFRS-listed) |
| paragraph 73 can remove the middle one | the middle one drops if raising-finance amounts sit in Operating |
| aria-label “Subtotals listed in section 118” | “Listed IFRS subtotals” |
| Listed in para 118 | Listed IFRS subtotals |
| paragraph 118(a) lists it | the IFRS list includes it |
| MPM · Ch6 | chip **6.1** → `ch06.html#s-6-1`, name “MPM” |
| Meets paragraph 117 | Meets the MPM tests |

### `ch05-operating-expenses.html`

| Before | After |
|---|---|
| Para 83 note not required | Nature totals note not required |
| aria-label “One section 83 note — specified nature totals” | “One nature totals note — specified nature totals” |
| One para 83 note — specified totals | Specified nature totals |
| **Paragraph 84** gives narrow relief inside the paragraph 83 note. It does not skip **paragraph 41** material disaggregation. | **Narrow relief** inside the nature totals note. It does not skip material disaggregation, plus chip **2.3** → `ch02.html#s-2-3` |
| require the paragraph 83 note | require the nature totals note |

The gate chip **5.3** and the relief chip **5.4** were already the Ch5 jumps. They were not duplicated onto the leaves.

### `ch06-mpms.html`

| Before | After |
|---|---|
| the para 117 tests, in order | the MPM tests, in order (chip **6.1** kept) |
| Listed in para 118, or required by IFRS Accounting Standards? | IFRS-listed, or required by IFRS Accounting Standards? (chip **6.3** kept) |
| paragraph 118-listed or IFRS-required subtotal | IFRS-listed or IFRS-required subtotal |

### `ch07-other-fs.html`

Scanned. No `para` / `paragraph` + number. Not edited. `IFRS 18 App D` stays: it is the appendix name on the EPS pointer (`span.ofs-cite-text`), not a paragraph-number label. The prior chip-strip kept it.

### `ch08-transition.html`

| Before | After |
|---|---|
| the paragraph 69–74 subtotals, despite IAS 34 paragraph 10 relief | the **4.1** required subtotals, despite IAS 34 condensed-statement relief |

Chip **4.1** → `ch04.html#s-4-1` is new. Chips 8.1–8.5 were not retargeted.

### `map-jumpboard.html`

| Before | After |
|---|---|
| (para 114) | dropped; the cell already links to `s-2-1-4` |
| para 118 subtotals are not MPMs | IFRS-listed subtotals are not MPMs |
| para 118 or IFRS subtotal | IFRS-listed or required subtotal |
| Para 126–129 carried forward · IE Part III examples | Capital disclosures carried forward · IE Part III examples |
| no para 28(f) amounts | no line-item adjustment amounts |
| (para C3) | dropped; the cell already links to `s-8-3` |
| (para C4–C5) | dropped; the cell already links to `s-8-4` |
| (para C7) | dropped; the cell already links to `s-8-5` |

`IE Part III` stays. It names the illustrative-examples part, not a paragraph.

## CSS

Only where a new chip or a longer label needed the existing row to hold it. No new colours, no denser type.

| File | Change |
|---|---|
| `ch01-whats-new.css` | Pointer row is a wrapping flex line so chip 4.2 sits with the Ch3 / Ch4 links. Timeline chips 8.3 and 8.4 keep the circle metrics. |
| `ch04-totals-subtotals.css` | Trap title may wrap inside the side rail. Regime-head chip 6.1 uses the same circle, without an extra right margin. |
| `ch05-operating-expenses.css` | Inline chip 2.3 has side margin. `html { background }` paints the night canvas, matching Ch4 and Ch6, so the iframe does not show a white backdrop beside the 780px board. |
| `ch08-transition.css` | Inline chip 4.1 has side margin inside the duty cell. |

## CF 2018 — map labels only

| File | Before | After |
|---|---|---|
| `ch10-carve.html` | Boundary description (CF 3.14) | Boundary description |
| `ch11-status.html` | A few decisions only the Board can take (OCI, CF 7.17) | A few decisions only the Board can take (when to use OCI) |
| `ch11-status.html` | No continues — IAS 8.11 order | No continues — IAS 8 gap-fill order |

Ch1–Ch8 and `ch09-combined.html` had no visible map label of this class. Not edited.

Left in HTML comments (not rendered, not map labels), same as the chip-strip pass:

- `ch09-combined.html` teaching-arc note: CF 3.12, CF 3.13–3.14, BC3.21
- `ch10-carve.html` teaching-arc note: CF 3.10, CF 3.13–3.14, BC3.17–BC3.18
- `ch11-status.html` teaching-arc note: SP1.1–SP1.5, IAS 8.11, BC0.26–BC0.28

## New section jumps

These `a.fb-num` links were added. None of the chips that were already on the boards were removed or retargeted.

| Chip | From | To |
|---|---|---|
| 4.2 | Ch1 structured P&L card | `ch04.html#s-4-2` |
| 8.3 | Ch1 first-year card | `ch08.html#s-8-3` |
| 8.4 | Ch1 first-year card | `ch08.html#s-8-4` |
| 6.1 | Ch4 MPM regime card | `ch06.html#s-6-1` |
| 2.3 | Ch5 narrow-relief line | `ch02.html#s-2-3` |
| 4.1 | Ch8 interim duty | `ch04.html#s-4-1` |

## Out of scope

- IAS 2 maps
- Teaching chapter bodies and iframe `?v=`
- Skill markdown
- New cite chips
