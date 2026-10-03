# 7B3 point-chip wrap — key changes (2026-10-03)

Checklist: Brief attached · i18-css-html.tgz attached · Official/Big4 not needed.

## Choice

The wrap is a teaching override in `ifrs-18/draft-v1-linked/assets/draft.css`, scoped to `.teaching .point-chip`.

`assets/shared.css` keeps the densifier one-line chip (`inline-flex`, `white-space: nowrap`, `overflow: hidden`, `text-overflow: ellipsis`, pill radius `999px`). That rule is the kit comment “1-line tip”. Concept-map visuals are separate documents (`visuals/*.html` in each chapter iframe) and keep that clamp. `.meta-chip` nowrap in the same file is a different control and stays as it is. `shared.css` is byte-identical to the source archive.

Every chapter already loads `draft.css` after `shared.css`, and every tip already sits in `<article class="teaching">`. No HTML edit and no new class hook.

## CSS

```css
.teaching .point-chip {
  display: block;
  white-space: normal;
  overflow: visible;
  text-overflow: clip;
  overflow-wrap: break-word;
  border-radius: var(--card-radius, 8px);
  line-height: 1.45;
}
```

| Property | Shared one-line chip | Teaching override |
|---|---|---|
| display | `inline-flex` | `block` |
| white-space | `nowrap` | `normal` |
| overflow | `hidden` | `visible` |
| text-overflow | `ellipsis` | `clip` |
| border-radius | `999px` | `var(--card-radius, 8px)` |
| line-height | `1.3` | `1.45` |
| overflow-wrap | (initial) | `break-word` |

`display: block` plus `white-space: normal` is what lets the sentence wrap inside the column. `overflow: visible` and `text-overflow: clip` turn the ellipsis clamp off. A leftover pill radius of `999px` would still round into the corners of a wrapped line, so the teaching chip uses the pack card radius (fallback `8px`, same fallback the kit already uses). Horizontal padding stays `10px`, which clears an 8px corner. Line-height moves from the one-line `1.3` to `1.45` so wrapped lines do not collide. Type size stays `12px` and weight stays `600`. Warn and plain colours stay on `.point-chip.warn` / `.point-chip` in `shared.css`.

`display: block` uses the column measure (`948px` inside the `980px` page at a `1280` viewport). The Chapter 8 tip, which already fitted, is now that full measure too. Its sentence is still complete and still one line.

## Unchanged

- Tip wording. Word tokens of all 26 chips match the chapter HTML before and after.
- Chapter HTML, including `draft.css?v=ifrs18-skill-align-20261002b`. Bump that query when the file is published so a cached copy is replaced.
- `shared.css` (densifier chip, `.meta-chip`, other kit).
- Concept maps, citation apply for Q1–4, CF / IAS 2, and any other component.

Chapter 7 has no `.point-chip`.

## Verification

Chrome 148, CSS viewport **1280×800**, dark. `_shared/tokens.css` is not in this slice. Screenshots inject a night stand-in (`--card-radius: 8px` and the night palette). The clamp and the wrap come from the pack CSS. Segoe UI is not installed here; the declared stack falls through to the system UI font. The 25/26 clamp still reproduced on that font.

Page column `980px`. Chip measure before the wrap: `948×26` with `scrollWidth` past the box. Document `scrollWidth` stayed `1280` (no horizontal page scroll) before and after.

Before: **25 of 26** tips clipped (`scrollWidth − clientWidth` from 181px to 1673px). The one that fitted was Chapter 8 #1 (`135` characters, gap `0`, width `812px`).

After: **0 of 26** clipped (`scrollWidth` gap `0`, text rects inside the border box). Wrapped heights are `45px` (two lines) or `62px` (three lines). Chapter 8 stays one line at `27px`.

| Chip | Chars | Before overflow | Before height | After height | After overflow |
|---|---:|---:|---:|---:|---:|
| ch01 #1 warn | 189 | 181px | 26px | 45px | 0 |
| ch01 #2 plain | 281 | 725px | 26px | 45px | 0 |
| ch02 #1 warn | 272 | 704px | 26px | 45px | 0 |
| ch02 #2 plain | 289 | 814px | 26px | 45px | 0 |
| ch02 #3 warn | 240 | 463px | 26px | 45px | 0 |
| ch03 #1 warn | 331 | 1030px | 26px | 62px | 0 |
| ch03 #2 plain | 264 | 606px | 26px | 45px | 0 |
| ch03 #3 plain | 434 | 1595px | 26px | 62px | 0 |
| ch03 #4 plain | 214 | 350px | 26px | 45px | 0 |
| ch04 #1 warn | 216 | 372px | 26px | 45px | 0 |
| ch04 #2 plain | 436 | 1673px | 26px | 62px | 0 |
| ch04 #3 warn | 224 | 368px | 26px | 45px | 0 |
| ch04 #4 plain | 309 | 931px | 26px | 45px | 0 |
| ch04 #5 warn | 291 | 782px | 26px | 45px | 0 |
| ch05 #1 warn | 289 | 753px | 26px | 45px | 0 |
| ch05 #2 plain | 284 | 780px | 26px | 45px | 0 |
| ch05 #3 warn | 291 | 759px | 26px | 45px | 0 |
| ch05 #4 plain | 249 | 559px | 26px | 45px | 0 |
| ch05 #5 warn | 301 | 862px | 26px | 45px | 0 |
| ch06 #1 warn | 202 | 306px | 26px | 45px | 0 |
| ch06 #2 plain | 291 | 800px | 26px | 45px | 0 |
| ch06 #3 warn | 304 | 917px | 26px | 62px | 0 |
| ch06 #4 plain | 257 | 643px | 26px | 45px | 0 |
| ch06 #5 plain | 289 | 817px | 26px | 45px | 0 |
| ch06 #6 warn | 267 | 645px | 26px | 45px | 0 |
| ch08 #1 warn | 135 | 0px | 26px | 27px | 0 |

Screenshots are CSS viewport 1280. The page frames are 1280×800. The tip frames are 1280-wide crops of that same viewport, scrolled to the chip.

- `screenshot_1280_dark_ch02_page_before.png` / `_after.png` — Chapter 2 at 1280, dark.
- `screenshot_1280_dark_ch02_trap_before.png` / `_after.png` — the clamped trap. Before ends at “aggrega…”. After shows the rest of the sentence and both IFRS 18 cites.
- `screenshot_1280_dark_ch03_investing_before.png` / `_after.png` — longest plain tip (Chapter 3, 1595px overflow before, three lines after).
- `screenshot_1280_dark_ch08_short_before.png` / `_after.png` — the tip that already fitted. Still complete. The bar is now the column width.

## Files

- `assets/draft.css` — teaching override (this is the change).
- `assets/shared.css` — unchanged, included so the one-line rule can be read beside the override.
