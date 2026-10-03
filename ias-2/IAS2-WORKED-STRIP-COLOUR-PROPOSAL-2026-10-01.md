# IAS 2 — Worked-strip colour proposal (2026-10-01)

> **STATUS 2026-10-01 (CST):** Johnny LOCK OVERRIDE applied — full Illus-peer neutral (no ok/warn fills, no include/exclude colour). See `IAS2-WORKED-STRIP-COLOUR-SAVE-2026-10-01.md`. Option A carve-out superseded.

**Owner:** Design (propose) · Johnny decides · PM locks  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Trigger:** Johnny dislikes worked-strip rainbow (ok green / warn yellow on most Conclusion/Exception columns + band beige). QC asked Design propose quieter strip colour. **No lock until Johnny picks.**

## Audit (draft-v1-linked)

| Class | Approx count ch01–05 | Typical role today |
|-------|---------------------:|--------------------|
| `.box.ok` | ~34 | Almost every **Conclusion** |
| `.box.warn` | ~23 | Almost every **Exception** (+ some Facts) |
| Strip shell | all strips | `.worked-strip` uses `--band` beige / night band |

True **include vs exclude** teaching pairs are rare (e.g. storage Ill. with “Include in inventory”). Most ok/warn is decorative peer paint, not colour-with-meaning.

## Design recommendation (Option A)

**Inside `.worked-strip` only:** neutral peer fills for all columns (Facts / Usual gate / Conclusion / Exception).  
**Reserve** `.box.ok` / `.box.warn` for true include/exclude (or YES/NO) contrast — preferably via explicit classes or only when Content labels Include/Exclude.

### CSS sketch (not applied)

```css
/* Quieter strip shell — optional */
.worked-strip {
  background: var(--surface);          /* was --band */
  border-color: var(--line);
}

/* Neutralize decorative ok/warn INSIDE strips */
.worked-strip .box.ok,
.worked-strip .box.warn {
  background: var(--surface);
  border-color: var(--line);
  color: inherit;
}
.worked-strip .box.ok .box-title,
.worked-strip .box.warn .box-title {
  color: var(--muted);                 /* same as peer column titles */
}

/* Keep true contrast when Content marks include/exclude */
.worked-strip .box.include,
.worked-strip .box.ok.include { /* ok-soft + ok border */ }
.worked-strip .box.exclude,
.worked-strip .box.warn.exclude { /* warn-soft + warn border */ }
```

HTML follow-up (Content or Design after lock): strip bare `ok`/`warn` from Conclusion/Exception **or** add `.include` / `.exclude` where meaning is real. Outside worked-strips (contrast-pair, decision branches) keep current ok/warn.

## Options for Johnny

| Option | Strip shell | Conclusion / Exception | Include vs Exclude |
|--------|-------------|------------------------|--------------------|
| **A (rec)** | surface (no beige) | neutral peers | ok/warn only with `.include`/`.exclude` |
| **B** | keep band | neutralize ok/warn inside strip | same as A |
| **C** | surface | keep ok/warn classes but muted (lower chroma softs for strip only) | same classes, quieter paint |
| **Hold** | no change | — | — |

## Out of scope until lock

- Applying CSS / HTML mass edit  
- Changing CF / IFRS 18 packs  
- Inventing site-wide colour lock beyond IAS 2 trial unless Johnny says pack-wide
