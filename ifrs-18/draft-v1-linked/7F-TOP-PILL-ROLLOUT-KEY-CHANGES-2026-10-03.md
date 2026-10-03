# 7F top pill — rollout (2026-10-03)

Same pill as the IFRS 18 Chapter 3 pilot. Chapter pages only.

Selector stays `article.teaching > h3 > a.sec-top`. Href `#page-map`. The first Concept Map fieldset on each page has `id="page-map"`. `scroll-margin-top: 112px` is unchanged. Chrome query on every edited page: `chrome.css?v=7f-top-pill-20261003`.

All three packs use `h3` for the numbered section. No second pill style.

- IFRS 18: `h3 > strong`, as in the pilot.
- CF: `h3` holds `.sec-no` and `.sec-title`. The same rule now also lets `.sec-title` grow, so the pill sits on the right. The number’s own margin is unchanged.
- IAS 2: the section words are text in the `h3`, and the same `a.sec-top` is the last child. `margin-left: auto` pins it to the right.

## Pill counts

| Page | Pills |
| --- | ---: |
| cf-2018 ch01 | 9 |
| cf-2018 ch02 | 8 |
| cf-2018 ch03 | 8 |
| cf-2018 ch04 | 11 |
| cf-2018 ch05 | 8 |
| cf-2018 ch06 | 10 |
| cf-2018 ch07 | 7 |
| cf-2018 ch08 | 6 |
| cf-2018 ch09 | 8 |
| cf-2018 ch10 | 9 |
| cf-2018 ch11 | 8 |
| ifrs-18 ch01 | 6 |
| ifrs-18 ch02 | 6 |
| ifrs-18 ch03 | 10 (already present; not edited) |
| ifrs-18 ch04 | 6 |
| ifrs-18 ch05 | 5 |
| ifrs-18 ch06 | 7 |
| ifrs-18 ch07 | 6 |
| ifrs-18 ch08 | 7 |
| ias-2 ch01 | 6 |
| ias-2 ch02 | 5 |
| ias-2 ch03 | 11 |
| ias-2 ch04 | 8 |
| ias-2 ch05 | 5 |
| ias-2 ch06 | 7 |

187 pills. Every `h3` on these pages has one. None were skipped for a missing Concept Map.

## Not touched

- Pack Map / index pages and References (not in the bundle; no pill added).
- Concept Map legends, `h4` subsections, Key terms, chapter `h1`.
- Teaching sentences, cites, chapter tags, and the maps.
- IFRS 18 ch03, which already had its 10 pilot pills.
