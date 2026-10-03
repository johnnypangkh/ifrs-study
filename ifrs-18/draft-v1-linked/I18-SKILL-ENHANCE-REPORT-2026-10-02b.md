# I18 skill-enhance report — 2026-10-02b

**Job:** #7 skill-align / chrome / structure. Not the Official + Big4 densify wave (that is Opus #8).  
**Runner:** Grok 4.7. No CF. No IAS 2.  
**Pack edited:** `refs/ifrs-18/draft-v1-linked/` (extracted from the attached live tarball).  
**Stamp:** `Last update · 2026-10-02 16:20 HKT` on every pack page (was `2026-10-02 01:48 HKT`).  
**Status:** HTML edited. Densify not started.

Shared CSS links re-verified on every page before the edit: `../../_shared/tokens.css`, `chrome.css`, `cite.css`, then `assets/shared.css` and `assets/draft.css` (`map.css` on the Map). Cache key on those links was `ifrs18-chrome-phase2-20261002f`. The `_shared` files are not inside this pack tarball (they live at the site root). They were not invented.

`assets/draft.css` gained one rule, `.teaching h4`, so the demoted headings match the teaching kit. Only the `draft.css` query was bumped, to `ifrs18-skill-align-20261002b`.

---

## 1. DIFF — what changed

### A. Nine wrong-shape matrix titles demoted (not invent)

Each plate kept its `id`. `Illustration:` and the italic “(section matrix — not an Illustration)” note were removed. The `.worked-strip` wrapper came off. Shape is now `h4` + the existing list + the existing table (1.5.1 is lists only) + cite chips in a paragraph at the end of the unit.

| Plate | id | File |
|---|---|---|
| 1.5.1 — IE pack map (IE1–IE3 orientation) | `s-1-5-ex` | `ch01.html` |
| 2.4.1 — Informative labels for aggregated items | `s-2-4-fig7` | `ch02.html` |
| 3.1.1 — Categories without specified MBA | `s-3-1-fig2` | `ch03.html` |
| 3.4.1 — Hybrid contracts with host liabilities | `s-3-4-fig4` | `ch03.html` |
| 3.5.1 — Investing MBA classification | `s-3-5-fig31` | `ch03.html` |
| 3.5.2 — Financing-to-customers MBA classification | `s-3-5-fig32` | `ch03.html` |
| 3.5.3 — Cash and cash equivalents with specified MBA | `s-3-5-fig33` | `ch03.html` |
| 3.4.2 — Gains and losses on derivatives | `s-3-5-fig5` | `ch03.html` (left where it already sat, after 3.5.3) |
| 6.1.1 — Identifying MPMs | `s-6-1-fig6` | `ch06.html` |

Facts / Assessment labels were the wrong shape and were dropped. The sentences in those columns were kept. Part I / II / III labels on 1.5.1 were kept because they are the matrix, not a Facts/Assessment costume.

**Representative before → after (1.5.1):**

```html
<!-- before -->
<div class="worked-strip" id="s-1-5-ex">
  <p class="worked-strip-title"><strong>Illustration: 1.5.1 — IE pack map (IE1–IE3 orientation)</strong>
    <em>(section matrix — not an Illustration)</em> …cites…</p>
  <div class="worked-strip-grid">…Part I / II / III boxes…</div>
</div>

<!-- after -->
<h4 id="s-1-5-ex"><strong>1.5.1 — IE pack map (IE1–IE3 orientation)</strong></h4>
<ul>…same Part I / II / III items…</ul>
<p>…same cite chips…</p>
```

**Author-meta taken off the reader page** (recorded in `OPUS-WORKING-MEMORY.md`, not treated as lost teaching):

- Four bullets: `No invent: do not add entity facts beyond the cited IE / firm plate.`
- Four bullets that told the reader to “read peers with the table” after the peer grid was removed.
- Two empty “See supporting table/figure below” Facts lines on 3.5.3 and 3.4.2.

The figure tables and the Official path sentences stay. The bullet list still repeats the table on the figure plates. That overlap is left for Opus write-once. Do not drop the Fig 2 FX footnote, the Fig 6 §119 presumption footnote, or the Fig 7 “other is a last resort” line — those are not in the tables.

### B. Case-study Illustrations — structure already present

The 24 kept plates were already `.worked-strip` + `.worked-strip-grid`, with neutral peers and `<div class="box-body"><ul>`. No `.ok` / `.warn` / `.danger` on those peers. No `<p class="box-body"><ul>`.

No bullets, entities, or CU amounts were added. A thin plate was not padded to clear a count.

Bullet-text floor (≤5 list items or ≲350 characters) is clear on all 24. That is a structure observation only. It is not a densify pass.

### C. Ch3 narrative Gate → Decision / Test / Assessment

15 hits in `ch03.html` (inventory ~12). Questions unchanged. Word-bounded `gate` / `gates` in `ch03.html` is now 0.

| From | To | n |
|---|---|---|
| next gate | next test | 6 |
| gate labels | test labels | 4 |
| Investing / Financing gates | Investing / Financing tests | 2 |
| ordered category gates | ordered category tests | 1 |
| overview gate | overview decision | 1 |
| at that gate | at that test | 1 |

Example: `Decision strip — ordered category gates` → `Decision strip — ordered category tests`. The parenthetical “no invented entity facts” on that title was already there and was left.

Visual class names `pc-gate`, `oe-gate`, `gt-gate`, and the Ch5 map `aria-label="Gate — …"`, were not renamed. That is a visual CSS edit, not the Ch3 narrative sweep.

Four METHOD lines that instructed the next writer to put “Gate” on the page now say Decision / Test.

### D. Map

No “Section chips follow the order of the decisions…” note. None added. DOM was not reordered. No pillar redraw.

Desktop reading-order narration from source order: **PASS**. Start at chip 1 (What’s new), then the three requirement-set pillars L→R (Structured P&L 3/4 with operating expenses 5 nested inside Operating, then Grouping 2, then MPM 6), then the visit strip 1→8, then close row 7 | 8. Chip jumps on the pillars follow the three-set story, not chapter numbers. Drift-log row is in `OPUS-WORKING-MEMORY.md` (agents only).

### E. Not done, on purpose

| Item | What happened |
|---|---|
| `.callout.differ` | Still zero. None invented. |
| `IFRS 18 · para B… returns test` (Ch3 Entity C, EY Ill 3-1) | Left. Ask below. |
| Body-prose `§` → `para` | Not started. |
| Crosswalk A/B, thin bridges, IE/firm densify | Listed in §3. Not filled. |
| CF / IAS 2 | Not in this tree. Not edited. |
| PwC chips | Not added. PwC remains not on disk. |

### F. Chrome

- Last update is the same string on `index.html`, `ch01.html`–`ch08.html`, and `references.html`.
- Disclaimer stays at the bottom, immediately before `footer-nav`.
- References stays after Ch8. No sources added.
- Homepage links `../../homepage/homepage-wireframe-v0.1.html` are the pre-existing chrome and are outside this pack. Not invented.

---

## 2. ASK

**Ch3 Entity C (EY Ill 3-1, inside `#s-3-9-ey`).** The Official chip is truncated:

`IFRS 18 · para B… returns test`

Proposed replacement has to come from the Official text (the returns test for an asset that generates a return individually and largely independently — the page already cites `IFRS 18 · para 53–58` beside it). Do not guess the B paragraph. Reply with the locator and the next run can replace that one chip.

---

## 3. READY-FOR-OPUS — do not densify here

| Item | Why it waits |
|---|---|
| **Crosswalk A — Official → Big4** and **Crosswalk B — Big4 → Official** | METHOD still says both locator tables are open. Pack-complete stays blocked. Writing rows needs the PDFs. |
| **Thin bridges** | Ch1 carry / IAS 1 move; Ch2 §2.5 offsetting; Ch3 FX overview (§48 / B65–B76); Ch4 and Ch6 OPDAI vs EBITDA; Ch7 banks/insurers SCF and capital; Ch8 §8.5 optional IAS 28 election. Intentional bridge vs missing body is a source decision. |
| **24 case-study plates vs the PDFs** | Re-classify wrong-shape vs true invent vs keep. This run found named entities already on the page and did not relabel Official restatement as invent. |
| **Quantitative / source densify** | Structure floor is clear. Several plates are a short Facts/Assessment list plus a face table (thinnest bullet text: 3.8.2, 6 items / ~524 characters, with an IE11 table under it). Opus adds Official + KPMG FI + EY Closer look substance. Do not cut unique detail. Do not pad with empty bullets. |
| **EY Ill 3-1–3-12 index (`#s-3-9-ey`)** | One grid of one-paragraph sketches, not separate `Illustration:` plates. The lead already says the worksheets stay in the EY PDF. Densify from that PDF. Includes the broken `para B…` chip. |
| **Demoted-matrix overlap** | List and table repeat on Fig 2, 3.1, 3.2, 3.3, 4, 5, 6, and 7. Collapse to one unit only when doing write-once, and keep the unique lines named in the working memory. |
| **Real firm differences → `.callout.differ`** | Only after the PDFs show a difference. State both. Never reconcile. |
| **CONTENT-NOTES** | Still dated 2026-09-30. Refresh after the densify gates, not before. |
| **Visual Gate chrome** | `pc-gate` / `oe-gate` / `gt-gate` and the Ch5 aria label. Class rename plus the column-1 / leaf-colour check is the visual pass. This sweep’s map narration did not fail, so the pillars were not redrawn. |
| **Ch8 `s-8-3-appc` and `s-8-4-kpmg`** | Single-column `.worked-strip`, not Illustrations. Leave or convert to a plain section in a later structure pass. Not given a fake second column. |
| **Body `§` outside chips** | Optional later `para` pass. Chips already use `para` / `section`. |
| **PwC** | Not on disk. No PwC densify. |

---

## 4. Checks run on the edited pack

| Check | Result |
|---|---|
| `Illustration:` count | 24 (the kept case studies only) |
| “not an Illustration” residue | 0 |
| Ch3 word-bounded gate | 0 |
| `§` inside `.cite` | 0 |
| House-only Big4 chip | 0 |
| `<p class="box-body"><ul>` | 0 |
| `.ok` / `.warn` / `.danger` inside a worked-strip | 0 |
| `<div>` balance on edited HTML | balanced |
| `href` fragments inside the pack | resolve (homepage wireframe is outside the pack) |
| Map chip-order lecture | absent |
| Disclaimer before footer-nav | yes, every page |
| Same Last update string | yes |

---

## 5. Tarball

`ifrs18-draft-v1-linked-2026-10-02b.tar.gz` at the repo root. Contents: updated `ifrs-18/draft-v1-linked/` for Bot → Documents. `uploads/` is not in the tarball.
