# 7B1 — Map jump links → rounded chip (2026-10-03)

Chrome-only pass. Cross-chapter and section jumps on Concept Maps now use the same `a.fb-num` chip as the existing `1.2` / `4.2` markers. Destinations are unchanged. No teaching sentences were added or rewritten. Skill MD and teaching-body `chNN.html` were not edited.

## Attach checklist

- Brief attached
- maps-visuals.tgz attached
- visual-grammar skill attached
- Official/Big4 not needed

## What changed

Bare jump anchors — visible label is only `ChN`, `Chapter N`, or a section number such as `4.2` / `1.1.3` — gained `class="fb-num"`. `thin-link` was removed from those anchors so the underline does not sit on the chip. `·` separators between peer chips were left in place.

`a.fb-num` was already in each pack’s `shared.css` (28px circle, formula border, accent-soft fill). No second chip style was added.

IAS 2 `ias2.css` lets that same chip grow only when the label is wider than 28px. Measured result:

| Label | Box | Shape |
|---|---|---|
| `Ch2` `Ch3` `Ch4` `Ch6` `1.2` `1.4` `1.1.3` `1.1.4` `2.2` `2.3` `3.4` `3.7` `4.2` | 28×28 | circle, no overflow |
| `Chapter 2` `Chapter 3` `Chapter 4` `Chapter 5` | 52×28 | same border, fill, and type; stadium because the words do not fit a circle |

Inline chips inside a sentence use a 2px side margin so they sit in the line. Title chips keep the existing 6px gap.

IFRS 18 `.wn-set-ptr a.fb-num:hover` no longer inherits the bare-link underline.

## Inventory — before → after

22 anchors. Href unchanged on every row.

### IFRS 18 `visuals/ch01-whats-new.html` (§1.2 cards)

| Line | Before | Href |
|---|---|---|
| 46 | `<a>` `Ch3` | `../ch03.html#s-3-1` |
| 46 | `<a>` `Ch4` | `../ch04.html#s-4-1` |
| 52 | `<a>` `Ch2` | `../ch02.html#s-2-1` |
| 57 | `<a>` `Ch6` | `../ch06.html#s-6-1` |

After: `class="fb-num"` on each. The peer `4.2` chip on line 46 was already `fb-num` and was not retargeted.

### IAS 2 `visuals/ch01-scope.html`

| Line | Before | Href |
|---|---|---|
| 68 | `thin-link` `1.1.3` | `../ch01.html#s-1-ex-spare` |
| 68 | `thin-link` `1.1.4` | `../ch01.html#s-1-ex-kpmg-bottles` |
| 68 | `thin-link` `1.4` | `../ch01.html#s-1-ex-kpmg-samples` |
| 131 | `thin-link` `Chapter 3` | `../ch03.html#s-3-1` |
| 131 | `thin-link` `Chapter 4` | `../ch04.html#s-4-1` |

### IAS 2 `visuals/ch02-recognition.html`

| Line | Before | Href |
|---|---|---|
| 22 | `thin-link` `2.2` | `../ch02.html#s-2-2` |
| 75 | `thin-link` `2.3` | `../ch02.html#s-2-3` |
| 75 | `thin-link` `2.2` | `../ch02.html#s-2-2` |
| 87 | `thin-link` `Chapter 3` | `../ch03.html#s-3-1` |
| 87 | `thin-link` `Chapter 4` | `../ch04.html#s-4-1` |
| 98 | `thin-link` `Chapter 5` | `../ch05.html#s-5-0` |

### IAS 2 `visuals/ch03-initial.html`

| Line | Before | Href |
|---|---|---|
| 16 | `<a>` (no class) `Chapter 4` | `../ch04.html#s-4-1` |
| 29 | `thin-link` `3.4` | `../ch03.html#s-3-4` |
| 40 | `thin-link` `3.7` | `../ch03.html#s-3-7-deferred` |

### IAS 2 `visuals/ch05-derecognition.html`

| Line | Before | Href |
|---|---|---|
| 45 | `thin-link` `Chapter 2` | `../ch02.html#s-2-3` |

### IAS 2 `visuals/map-formula-board.html`

| Line | Before | Href |
|---|---|---|
| 48 | `thin-link` `2.2` | `../ch02.html#s-2-2` |
| 53 | `thin-link` `2.3` | `../ch02.html#s-2-3` |
| 92 | `thin-link` `3.4` | `../ch03.html#s-3-4` |

### CF 2018 Maps

Scanned every `cf-2018/draft-v1-linked/visuals/*.html` (ch01–ch11). Every anchor whose visible label is a section number already had `class="fb-num"`. No bare `ChN` / `Chapter N` jump. No file edited.

## Reviewed and left alone

These mention a chapter but the anchor’s visible label is a sentence (or the chapter token is not a link). They are not bare jumps.

| File | Why left |
|---|---|
| IFRS 18 `ch01-whats-new.html` see-also | Whole sentence, dashed `wn-see`. “→ Ch3” is inside that sentence. |
| IFRS 18 `ch01-whats-new.html` timeline | “Transition detail → Ch8” is text after the `8.1` chip. `Ch8` is not its own link. |
| IFRS 18 `ch03-pnl-categories.html` | “Ch4” is prose beside the existing `4.1` chip. |
| IFRS 18 `map-jumpboard.html` tip | One see-also link; “Ch3 3.5” sits in the sentence. Chapter numbers on the board are already `<span class="fb-num">`. |
| IAS 2 `ch02-recognition.html` see-also | “See also — Chapter 1. …” is the whole label. |
| IAS 2 `ch04-subsequent.html` | “Chapter 5” is inside the leaf sentence; the link is the whole outcome card, which already carries its section chip. |
| IAS 2 `ch05-derecognition.html` see-also | “See also — … Chapter 2” is the whole label. The separate `Chapter 2` thin-link on the leaf was chipped. |

`span.fb-num` inside a parent link (IAS 2 ch04–ch06 and the pack Map disclosure rows) is already the circle. An `<a class="fb-num">` cannot be nested inside that parent link.

## Files touched

- `ifrs-18/draft-v1-linked/visuals/ch01-whats-new.html`
- `ifrs-18/draft-v1-linked/visuals/ch01-whats-new.css`
- `ias-2/draft-v1-linked/visuals/ias2.css`
- `ias-2/draft-v1-linked/visuals/ch01-scope.html`
- `ias-2/draft-v1-linked/visuals/ch02-recognition.html`
- `ias-2/draft-v1-linked/visuals/ch03-initial.html`
- `ias-2/draft-v1-linked/visuals/ch05-derecognition.html`
- `ias-2/draft-v1-linked/visuals/map-formula-board.html`

## Screenshots (1280, dark)

Night via `prefers-color-scheme: dark`. Chip colour `rgb(123, 163, 201)` on `rgb(30, 42, 56)`.

- `i18-ch01-s12-cards-1280-dark.png` — primary: §1.2 cards, `Ch3` · `Ch4` · `4.2`, `Ch2`, `Ch6`
- `i18-ch01-whats-new-1280-dark.png` — full Ch1 board
- `ias2-ch01-scope-1280-dark.png` — `1.1.3` / `1.1.4` / `1.4` and `Chapter 3` / `Chapter 4`
- `ias2-ch03-initial-1280-dark.png` — `Chapter 4`, `3.4`, `3.7`
- `ias2-map-3-4-band-1280-dark.png` — pack Map `3.4` beside the existing `3.3` circle
- `ias2-ch02-chapter5-1280-dark.png` — `Chapter 5`
- `ias2-map-formula-board-1280-dark.png` — full pack Map
