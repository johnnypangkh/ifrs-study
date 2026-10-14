# Build tools

From the repo root:

```bash
bash tools/build-all.sh
```

The script runs, in order:

1. `tools/build-map-includes.py` — splice IAS 16 chapter map sections into `ias-16/draft-v1-linked/visuals/master-concept-map.html`.
2. `tools/stamp-assets.py` — set every local `.css` / `.js` / `.html` `?v=` under `ias-16/draft-v1-linked/` to the first 12 hex digits of the SHA-256 of the target file.
3. `homepage/build-search-index.py` — rebuild `homepage/search-index.js` and its own `?v=` stamps.
4. `tools/build-last-update.py` — rebuild `_shared/last-update.js` and its own `?v=` stamps.

A second run rewrites nothing. CI runs this script and then `git diff --exit-code`.

`tools/check-duplicates.py` fails when a normalised `plate` or `disc-band` section appears twice outside a matching include, when an include body has drifted from its chapter `map-section`, when the during-use axis (`map-section:ch05-axis`) appears twice outside a matching include, or when a local IAS 16 `?v=` is not 12 hex. Whitespace between tags is ignored for the axis, so a pretty-printed copy still counts. A copy inside a matching include is the included axis, not a second source. There is no deferred plate.

## Map includes

The chapter visual owns the section:

```html
<!-- map-section:ch06:start -->
<section class="plate pack-exit">...</section>
<!-- map-section:ch06:end -->
```

The master reuses it inside a wrapper that keeps the phase and spine hooks. `inject-class` copies a master-only class onto the included root tag when a selector matches the plate itself (`.plate.ch06-map`). There is no runtime fetch and no iframe.

```html
<div class="map-include" data-phase-start data-phase-end>
  <!-- include:ch06-derecognition.html#ch06:start inject-class="ch06-map" -->
  ...
  <!-- include:ch06-derecognition.html#ch06:end -->
</div>
```

Whitespace, `data-phase-*` attributes, and `?v=` are ignored when the include is compared with its source. Classes and attributes named on the include comment are master-owned and are not required in the chapter file.

### Single-source

| Plate | Chapter visual | Master |
| --- | --- | --- |
| Derecognition | `visuals/ch06-derecognition.html` (`map-section:ch06`) | include `ch06-derecognition.html#ch06` |
| Depreciation | `visuals/ch05-depreciation.html` (`map-section:ch05-dep`) | include `ch05-depreciation.html#ch05-dep` |
| During-use axis | `visuals/ch05-depreciation.html` (`map-section:ch05-axis`) | included from Depreciation, and nested inside the Revaluation and Impairment sections |
| Revaluation | `visuals/ch04-models.html` (`map-section:ch04-reval`) | include `ch04-models.html#ch04-reval` |
| Impairment | `visuals/ch04-models.html` (`map-section:ch04-impair`) | include `ch04-models.html#ch04-impair` |
| Compensation for impairment | `visuals/ch04-models.html` (`map-section:ch04-comp`, inside Impairment) | included on the chapter 6 visual (`ch04-models.html#ch04-comp`); the master copy sits inside the Impairment include |

The Derecognition chapter section and the master copy matched after collapsing whitespace and ignoring `data-phase-*` and `?v=`. The only token the master added was the class `ch06-map`, which is the styling hook for that plate. It stays on the included root via `inject-class`. The wrapper carries `data-phase-start` and `data-phase-end`.

The Depreciation plate matches the same way. The chapter and the master differed by one sentence before the include: the master said “Leased assets: IFRS 16”; the chapter continued “— lessee right-of-use asset depreciation often uses IAS 16”. Both now say “Lessee right-of-use asset — depreciation applies IAS 16, subject to IFRS 16 (useful life / lease term)”. No class is injected. The master wrapper keeps `dep-port`, `data-phase-start`, and `data-phase-end`. It does not also take `map-include`: that class zeros padding, and `.dep-port` is a `.ppe` that keeps the pack's end padding. The during-use axis (`5.4` Begins/Ceases) is marked inside that plate. The Revaluation and Impairment date bands include the same `ch05-axis` block, so those master copies sit inside matching includes.

### Master-owned

These blocks stay in the master. They are not byte-for-byte the chapter section, or the chapter visual has no such plate. The build does not choose between the two copies.

- Scope decision stack (`data-phase="scope"`). `ch01-scope.html` has no `plate` / `disc-band` section.
- Recognition decision fork and the “Recognised as an asset” plate. The chapter plate differs.
- Cost plate. The chapter plate differs.
- Measurement-after-recognition plate. The chapter plate differs.
- Disclosure `disc-band`. The chapter band differs.
- Rails, pack-flow shafts, and the connector script. Those are the master spine.

## Cache stamps

`stamp-assets.py` rewrites an existing `?v=` only when the URL resolves to a file inside `ias-16/draft-v1-linked/` whose suffix is `.css`, `.js`, or `.html`. That includes the Map iframe `src` on `index.html`. It does not add `?v=` to fragment links that never had one, and it does not rewrite `_shared/` URLs.

`search-index.js` and `last-update.js` are skipped so this script does not fight `homepage/build-search-index.py` or `tools/build-last-update.py`. Those generators still run after the stamper and write their own 12-hex `?v=` values.

## Incremental teaching diff

`tools/check-incremental.py` compares visible teaching items on a pull request with the merge-base of `main`. CI runs it on `pull_request` after `build-all.sh`, `git diff --exit-code`, and `check-duplicates.py`. The checkout uses `fetch-depth: 0` so the base commit is in the clone. In CI the base ref is `GITHUB_BASE_REF`. Locally pass `--base`.

```bash
python3 tools/check-incremental.py --base main
python3 -m unittest discover -s tools/tests -v
```

Scope is every `*.html` file in the repo: chapter pages, visuals, other packs, `homepage/`, and `_shared/`. `cf-2018/chapter-visuals/` was an offline twin of `draft-v1-linked/visuals/` and was deleted in PR7, together with the listed `_archive` duplicates (restore from `design/archive/cf2018-pr7-2026-10-14/`). The only exclusion is a path segment `_archive` (`cf-2018/draft-v1-linked/_archive/`). Those trees are retired snapshots of the old Conceptual Framework overview. They are not the published notes. Counting them would treat a historical copy as a second live location, so deleting the live sentence could look like a move into the archive. A live removal is still a removal. An edit that touches only the archive is outside this guard. `_archive-index-stub.html` was not under `_archive/`; it was deleted in PR7 with the other archive duplicates.

Items, one record each (`kind`, text, file, locator):

- headings `h1`–`h6`
- `li` bullets
- `p` text, and the inline text of a `div` (a wrapper whose children are blocks does not repeat them). Plate, card, and tip copy is read this way, and so is the same run outside those containers, so moving a rail into a plate is not a second item
- `.cite` chips, full label
- See also chips, and links as the label plus the href target id
- `aria-label` and `title` attributes
- table cells

The locator is the nearest element id, else the id of the current section heading, else a `data-section` attribute or a `map-section` comment, else the heading path.

Normalisation collapses whitespace and drops `?v=` stamps, `data-phase-*` attributes, and the last-update stamp (`Last update · YYYY-MM-DD HH:MM HKT`). Other characters stay, including capitals and U+2011 versus `-`. Text inside `<!-- include:... -->` … `<!-- include:...:end -->` is owned by the source file, so the pasted body is not a second copy.

The diff counts each `(kind, normalised text)` at each `(file, locator)`. A copy that survives in another file does not cancel a removal. A hand copy that the head replaces with a new include is compared to the multiset of items that section renders: the text between its `map-section` start and end markers, and only the hand-copy region that include replaced. A line elsewhere in the source file does not cover the including file.

- the same normalised text, and the source already had it: kept
- the same text, and a different file newly owns it: moved, with `moved_from` the hand-copy place and `moved_to` `source.html#section`
- different text: the source's own change or removal, reported once. A hand copy of wording the source itself dropped is kept when it sits in that replaced region, so the source row is not repeated

An include that was already in the base does not absorb a hand copy deleted somewhere else. Unchanged text that stays in the same file is kept when a new `map-section` wrapper is the only locator change.

The books have to balance. At each location the base count equals kept plus moved out plus removed plus the old side of a change. Across the run, base items equal kept plus moved plus changed plus removed, and head items equal kept plus moved plus changed plus added. Head items include one counterpart for each hand copy a new include still shows. If an equation fails, the check exits non-zero and prints a `reconciliation error` naming the items. Nothing can disappear without a row.

| Result | Meaning | Approval |
| --- | --- | --- |
| kept | The count at that location did not fall, or an equivalent include or same-file locator wrapper still shows the text | none |
| moved | The count fell at one location and rose by the same amount at another file that did not already hold the copy, including a new include source | none |
| removed | The count fell at that location, nothing there renders it, and no other file took the same text | required |
| added | The count rose at that location, and it was not the destination of a move | warning, or a failure with `--strict-added` |
| changed | A removal paired with an addition of the same kind in the same file that share a locator, or whose text is at least 0.6 similar. Similar text in two files is not a change | required |

A removal and an addition that pair are not also listed as removed and added. Deleting text from the source file is a removal even when a stale include body still contains the words.

Approval is `changes/<pr-number>.yml`, or `changes/<branch-name>.yml` when there is no pull-request number (`cursor/example` → `changes/cursor/example.yml`). The format, the `source` forms, and a template are in `changes/README.md`. A `removed` entry matches normalised text and `file`. `locator` is optional; when it is present it must match that row. The check fails when:

- a removal or a change has no matching entry, or an entry has an empty `source`
- an entry matches nothing (stale text, stale file, stale locator, or a typo)
- the YAML file is missing while the diff has a removal or a change

## Type literals

`tools/check-type-literals.py` fails when a served stylesheet or HTML `<style>` / `style=""` uses a `font-weight` or `line-height` value that is not `var(...)`, a `calc()` of variables only, or `inherit` / `normal` / `initial` / `unset`. Comments are ignored. The scan covers `_shared` (except `tokens.css` and `tokens-core.css`), each pack's `draft-v1-linked` tree, `homepage/*.html`, and `site`. `design/archive/` is skipped.

Hits are keyed by path, normalised selector, property, value, and occurrence, not by line number. `tools/type-literals-baseline.tsv` lists the current hits with class `DRIFT`, `GAP`, or `EXCEPTION`. A hit missing from that file fails. A `DRIFT` or `GAP` row that no longer matches also fails, so a fixed literal has to be deleted from the baseline and the allowlist only shrinks. `EXCEPTION` rows may stay. `--report` prints counts per pack. `--write-baseline` rewrites the file from the tree and keeps the class of every key that is still present; a new key is `DRIFT`.

Stdout and `$GITHUB_STEP_SUMMARY` get a Markdown table: the five counts, then each moved, changed, removed, and added row with old text, new text, file, locator, `approved: <source>` or `UNAPPROVED`, and `moved_from` / `moved_to` for a move. The same rows are written to `incremental-report.csv`. CI uploads that file as an artifact. Publish checks run on every pull request, with no path filter. A passing run with no such rows prints the counts and exits 0 without a YAML file.
