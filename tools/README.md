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

`tools/check-duplicates.py` fails when a normalised `plate` or `disc-band` section appears twice outside a matching include, when an include body has drifted from its chapter `map-section`, when the during-use axis (`map-section:ch05-axis`) appears twice outside a matching include, or when a local IAS 16 `?v=` is not 12 hex. Whitespace between tags is ignored for the axis, so a pretty-printed copy still counts. A copy inside `.reval-plate` or `.impair-plate` is deferred until those plates move: it must still match the chapter axis, and it is reported rather than failed.

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
| During-use axis | `visuals/ch05-depreciation.html` (`map-section:ch05-axis`) | once, inside the Depreciation include |

The Derecognition chapter section and the master copy matched after collapsing whitespace and ignoring `data-phase-*` and `?v=`. The only token the master added was the class `ch06-map`, which is the styling hook for that plate. It stays on the included root via `inject-class`. The wrapper carries `data-phase-start` and `data-phase-end`.

The Depreciation plate matches the same way. The chapter and the master differed by one sentence before the include: the master said “Leased assets: IFRS 16”; the chapter continued “— lessee right-of-use asset depreciation often uses IAS 16”. Both now say “Lessee right-of-use asset — depreciation applies IAS 16, subject to IFRS 16 (useful life / lease term)”. No class is injected. The master wrapper keeps `dep-port`, `data-phase-start`, and `data-phase-end`. It does not also take `map-include`: that class zeros padding, and `.dep-port` is a `.ppe` that keeps the pack's end padding. The during-use axis (`5.4` Begins/Ceases) is marked inside that plate, so the Depreciation include is the one master copy.

### Master-owned

These blocks stay in the master. They are not byte-for-byte the chapter section, or the chapter visual has no such plate. The build does not choose between the two copies.

- Scope decision stack (`data-phase="scope"`). `ch01-scope.html` has no `plate` / `disc-band` section.
- Recognition decision fork and the “Recognised as an asset” plate. The chapter plate differs.
- Cost plate. The chapter plate differs.
- Measurement-after-recognition plate. The chapter plate differs.
- Revaluation plate. No chapter plate with that label. It still contains a hand copy of the during-use axis so the revaluation-date band keeps the Begins/Ceases scale. That copy is deferred to the pass that moves this plate.
- Impairment plate. No chapter plate with that label. It still contains the same deferred axis copy, for the impairment-date band.
- Disclosure `disc-band`. The chapter band differs.
- Rails, pack-flow shafts, and the connector script. Those are the master spine.

## Cache stamps

`stamp-assets.py` rewrites an existing `?v=` only when the URL resolves to a file inside `ias-16/draft-v1-linked/` whose suffix is `.css`, `.js`, or `.html`. That includes the Map iframe `src` on `index.html`. It does not add `?v=` to fragment links that never had one, and it does not rewrite `_shared/` URLs.

`search-index.js` and `last-update.js` are skipped so this script does not fight `homepage/build-search-index.py` or `tools/build-last-update.py`. Those generators still run after the stamper and write their own 12-hex `?v=` values.
