# 7F top pill — pilot (2026-10-03)

IFRS 18 Chapter 3 only. No other page.

## What was added

Selector: `article.teaching > h3 > a.sec-top`

Href: `#page-map`

The first `fieldset.visual-fieldset` whose legend is Concept Map now has `id="page-map"`. Each teaching `h3` (3.0 through 3.9, ten titles) has a stadium pill on the right labelled `top`. The pill uses the chapter-tag family: `border-radius: 999px`, min 46×26, not a circle. Clicking it scrolls to that map; `scroll-margin-top: 112px` clears the sticky chapter bar.

Styles live in `_shared/chrome.css`. Only this page’s chrome query was bumped: `chrome.css?v=7f-top-pill-20261003`.

## Not touched

- Concept Map legend (no pill on it).
- `h4` subsections, the Key terms heading, chapter tags, cites, maps, and the rest of the chrome.
- Index, References, and every other chapter.
- Teaching sentences. The page base is the attached ch03; citation chips already in that file were left as attached.
