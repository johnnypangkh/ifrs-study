# Citation chips — Design chrome (IAS 2 trial grammar — 2026-10-01)

**Status:** Tokens + classes shipped. Cite **label grammar** locked to [IFRS teaching body](sand-workflow:ifrs-teaching-body): `CF 2018 · para …`; firm+work+locator; **zero `§`** inside `.cite`. Colour samples live **only in this note** — never on chapter visuals Johnny opens.

## Tokens (`:root`)

| Token | Role |
|-------|------|
| `--cite-official` / `--cite-official-soft` | CF / IFRS / IAS para · SP · BC |
| `--cite-pwc` / `--cite-pwc-soft` | PwC house |
| `--cite-dtt` / `--cite-dtt-soft` | Deloitte / DTT house |
| `--cite-kpmg` / `--cite-kpmg-soft` | KPMG house |
| `--cite-ey` / `--cite-ey-soft` | EY house |

## Classes

- `.cite.cite-official` — official paragraph / SP / BC tag
- `.cite.cite-pwc` · `.cite.cite-dtt` · `.cite.cite-kpmg` · `.cite.cite-ey` — Big 4
- `.cite-house` — house label inside a Big 4 chip (inherits size/weight from `.cite`)
- `.cite-extract` — optional one-line italic extract beside a chip (not a quote block)
- `.cite-row` — wrap a row of chips

## Markup (locked labels)

```html
<span class="cite cite-official">CF 2018 · para 4.26</span>
<span class="cite cite-official">CF 2018 · para SP1.2</span>
<span class="cite cite-official">CF 2018 · para BC4.53</span>
<span class="cite cite-official">IAS 8 · para 11</span>
<span class="cite cite-dtt"><span class="cite-house">DTT</span> A2 2022 · 5</span>
<span class="cite cite-pwc"><span class="cite-house">PwC</span> MOA 2020 · 1.19</span>
<span class="cite-extract">low probability can still meet the definition</span>
```

## Typography (cite chips only)

| Property | Value |
|----------|-------|
| `font-family` | `"Calibri Light", Calibri, "Segoe UI", sans-serif` |
| `font-size` | `11px` |
| `font-weight` | `300` (house inherits — never 700/800) |
| `letter-spacing` | `.02em` |

## Where CSS lives

- `draft-v1-linked/assets/shared.css` — tokens
- `draft-v1-linked/assets/draft.css` — chip classes (chapter pages)
- `chapter-visuals/shared.css` + `draft-v1-linked/visuals/shared.css` — tokens + classes (iframe visuals)

## Rules

- Colour = **source class**, not decoration
- Big 4 chip must include **firm + work + locator** (never house-only)
- **No `§` inside any `.cite`** — Official uses `para`; firm locators use numeric path / FAQ id
- Chip + optional one-line extract only — **no long quote UI**
- **Placement:** Illus title chips only; teaching paras/lis chips at end of unit. Do **not** put decorative PwC/KPMG/EY sample rows on iframe visuals / review surfaces.
