# IAS 2 Inventories — Opus amend pass (layout · numbering · links)

**Date:** 2026-09-30  
**For:** Johnny Pang  
**Pack:** `refs/ias-2/draft-v1-linked/` (unpacked from `ias2-draft-v1-linked.tgz`)  
**Skills followed:** IFRS visual grammar 2026.09.30-16 · IFRS teaching body · `IAS2-CONTENT-REWRITE-METHOD.md` · `IAS2-MAP-STORY-2026-09-30.md`  
**Pass type:** typesetting / formatting / layout / numbering / sectioning / deep-links. **No teaching substance rewritten** (no quote, Standard extract, Big4 support, or line-box figure changed). No new term, example, illustration or fact pattern.

## Order of work

1. Read the whole pack first: Map + `map-formula-board.html`, Ch1–Ch6 bodies, all six chapter visuals, `ias2.css`, `assets/*.css`, `theme.js`, `iframe-fit.js`, CH0N NOTES, METHOD, MAP-STORY, both skills. Official / DTT / PwC PDFs extracted to text to check the order of paragraph headings (§17–§27, §36–§39).
2. Fixed Ch1 → Ch6 (bodies + chapter visuals), committed.
3. Only then amended the Map against the final chapter anchors, committed.

---

## Site-wide body typesetting (`assets/draft.css`, scoped to `.teaching`)

| Problem found | Fix |
|---|---|
| `aside.point-chip` tips (Trap / Why / Concept insight / Tie back) inherited the shared one-line pill (`nowrap` + `overflow:hidden` + ellipsis) → every multi-sentence tip was **cut off after one line** | Body tips render as wrapped block tips; `warn` keeps the warn colour on the lead label only |
| Stacked single `.box` line boxes had **0 gap** between them (e.g. Ch1 crypto → spare parts; Ch4 post-period boxes) | `.teaching > .box` margin 14/18px, same rhythm as `.worked-strip` |
| Single-box `.box-title` is a flex row with `gap:0` → title and cite chips **ran together** | Body box title = text line with inline chips (like `.worked-strip-title`); box body 13px ink (matches worked-strip) |
| Section rhythm tight | `h3` after the first: 26px top margin |
| Table-cell nested bullets had extra bottom margin | Tightened |

**Cite-chip chrome:** removed the stray ` · ` text separators between adjacent chips (59 places across Ch1–Ch6). Chips now separated by a space everywhere, as the Official chips already were. The ` · ` **inside** chip labels (`PwC MOA 2020 Ch25 · 25.2`) is unchanged.

---

## Chapters

### Ch1 Scope
- Removed the duplicate `point-chip` “Why the definition is drawn this way” in 1.1. It repeated the bullet directly above word-for-word in substance (Big4-dedupe rule). The bullet is kept.
- 1.2 IAS 41 see-also → links to **Ch3 · 3.8** (deemed cost at harvest, §20).
- FAQ 25.8.1 box → links to **Ch4 · 4.2**.
- 1.5 handoff: chapter mentions are now links. Added the **Chapter 2** pointer (“confirms when the item enters as an inventory asset”, which is the 2.1 heading) so the pack path Ch1 → Ch2 → Ch3 → Ch4 is continuous. Carve-out bullet → **Ch6 · 6.3**.
- Visual: unchanged except cache-bust.

### Ch2 Recognition (kept light)
- Contrast pair Inventory ∥ Not-this-chapter’s-asset: dropped the `dense` variant. Its 3-line clamp was **hiding the body text and cite chips**.
- Links: pipeline cue → Ch1 box `#s-1-ex-pipeline`; expense exits → Ch5; handoff + property transfers → Ch3.
- Visual: “expense exits in Chapter 5” is now a link (`#s-5-0`).

### Ch3 Initial measurement — **renumbered**
The `3.7a` sub-letter broke the sequence. The Official Standard has three separate headed blocks here, so the sections now follow them:

| Old | New | Official heading |
|---|---|---|
| `#s-3-7a` 3.7a Deemed cost at harvest | `#s-3-8` **3.8** | Cost of agricultural produce harvested from biological assets (§20) |
| `#s-3-8` 3.8 Techniques that only approximate cost | `#s-3-9` **3.9** | Techniques for the measurement of cost (§21–22) |
| `#s-3-9` 3.9 Cost formulas | `#s-3-10` **3.10** | Cost formulas (§23–27) |

No section split or merged. All example-box ids (`#s-3-ex-*`, incl. `#s-3-ex-b`, `#s-3-ex-c`, `#s-3-ex-lifo`) preserved. Every inbound link updated (Ch3 visual, Ch4 visual, Map).
- Links: 3.0 → Ch4 (twice); 3.5 “see exclusions” → 3.6.
- Visual: § chips added on the cost cells (11 · 12–13 · 15) and formula cells (23 · 25–27), matching the Map’s cost arm. Cells became `div` so a chip link does not sit inside another link. The duplicate 23–27 on the formula plate title was dropped (chip once). The LIFO missing route links to `#s-3-ex-lifo`. “Deferred settlement” / “Standard cost and the retail method” in the thin line link to 3.7 / 3.9.

### Ch4 Subsequent measurement
- Links: 4.1 → Ch3; 4.2 mineral example → Ch1 box `#s-1-ex-nrv-fv`; `#s-4-ex-a` conclusion → Ch5 · 5.2.
- Visual: § chips added (NOTES (g) request): 16 Already excluded · 23–27 Already assigned (→ 3.10) · 29 item by item · 33 reversal capped · 32 materials · 30–31 contracts and evidence. The NRV arm title is now the 6–7 range, same as the Map. Iframe was on `ias2-v2`; now `ias2-v4`.

### Ch5 Derecognition
- Moved the “Year 2 of the capped Ch4 example” line up under the 5.3 bullets (it had been stranded after the PwC box and the tip). The Chapter 6 bridge tip is now last before 5.4.
- Links: consignment → Ch2 `#s-2-ex-consign`; SKU strip → `#s-4-ex-a`; capped example → `#s-4-ex-d`; Disclosure → Ch6 · 6.4.

### Ch6 Disclosure
- The §36 (a)–(h) overview table was filed under 6.4, which only covers (d)–(h). It now sits in **6.0** as the package overview before the detail sections. Each row label links to its section (6.1 / 6.2 / 6.3 / 6.4).
- Links: tie-back tip → `#s-4-ex-a` / `#s-4-ex-d`; crypto tip → Ch1 `#s-1-ex-crypto`.
- Visual: unchanged except cache-bust (its 36→6.1 / 39→6.5 chips were already correct).

### Chapter visuals CSS (`visuals/ias2.css`)
- In-text links inside `.bar` / `.thin` now show a quiet underline (they inherited `text-decoration:none` and were invisible as links).
- `.missing` renders as a block (it is now also used on an `<a>`); `a.ias2-mute-chip` hover state added.
- `.cells.g4` (2 columns at ≤800px) for the Map disclosure plate.

**Cache-bust:** all six chapter iframes and their `ias2.css` links `→ ?v=ias2-v4`.

---

## Map (done last)

`index.html` iframe + `map-formula-board.html` `ias2.css` link `→ ?v=ias2-map5`.

| Map node | Before | After |
|---|---|---|
| Specific identification 23 · FIFO ∥ WA 25–27 | `ch03#s-3-9` (would now land on Techniques) | `ch03#s-3-10` Cost formulas |
| LIFO `IN13` muted chip | not a link | links to `ch03#s-3-ex-lifo` (still muted chrome, not a peer chip) |
| Disclosure range 36–39 | 39 → `#s-6-4` | 39 → `#s-6-5` (nature-of-expense, §39) |
| Disclosure cells | 3 cells mixing sections (“Balances, expense, write-downs” → 6.4 but included 6.2; “Pledges and fair-value carve-out” → 6.4 but included 6.3) | 4 cells, one per Ch6 section: Policies and formula → 6.1 · Balances and classifications → 6.2 · Fair-value carve-out → 6.3 · Expense, write-downs, pledges → 6.4. Wording reused from the old Map cells and the Ch6 visual |
| Ch2 Recognition | no Map entry → orphan chapter | thin pointer inside the GO card: “Recognised when the entity controls that asset — Chapter 2” (Ch2 visual wording) → `ch02#s-2-1`. Not a new route; the stem still leaves only from GO |
| Inline styles | `style="margin:0"` / `style="margin-right:6px"` | removed (already set by `.gate-body` / `a.fb-num`) |

**Unchanged and confirmed against the frozen story:** formula-board spine (§9 → `#s-4-1`); Cost ∥ NRV same-format peer arms under “lower of”; the scope stem leaves the **GO card only**; the stop exits are in a side rail and do not feed the board. On narrow screens they fall **after** the board. Biological assets / produce at harvest (full exclusion, IAS 41 see-also) and commodity broker-traders at fair value less costs to sell (measurement-only stop) are explicit on the stops. LIFO stays a muted missing route. Expense exit and disclosure are lighter secondaries. Site labels are IAS 2 / IFRS only (no HKAS on any page).

**Visit-path check (Map → body):** enter at GO §6 → Ch1 1.1 · stops §2 / §3 → 1.2 / 1.3 · (Recognition pointer → 2.1) · board §9 → 4.1 · Cost §10–16 → 3.1–3.6, IAS 23 → 3.7 · formulas §23 / §25–27 → 3.10, LIFO → 3.10 box · NRV §6–7 / 28 / 29 / 33 → 4.2 / 4.3 / 4.4 / 4.7 · exit §34–35 → 5.1–5.4 · disclosure §36–39 → 6.1–6.5. Link checker: **0 broken** anchors across all 13 HTML files.

---

## Left for Johnny (not changed — content or Build decisions)

1. **Iframe dead space.** Short visuals (Ch2, Ch6, and partly Ch3/Ch4) show empty space under the Concept Map. `theme.js` embed `notify()` still includes `documentElement.scrollHeight`, which never shrinks below the iframe’s own height, plus the 260px CSS floor. The skill says Build should measure `body` only. Preserved per brief; this needs a Build fix.
2. **Teaching-arithmetic strips not from a source:** `#s-4-ex-a` (SKU 40/30/20) and `#s-4-ex-d` (100/70/90/110; materials 50/30) are existing teaching numbers (NOTES (f) already flags them). The Ch5 illustrative journals (“80 of carrying amount”; Dr PPE / Cr inventories) are loose `<p>` lines, also not from a source. Kept as-is. Decide whether to keep them, retitle them “Teaching strip”, or replace them with DTT/PwC figures.
3. **Ch5 visual chrome:** the flow label “three routes, not a sequence” restates peer rank that the same-format cells already show (skill §1.6). The hub → exits pair also has no labelled stem. Left because it is a visual redesign, not a numbering fix.
4. **§9 chip target.** The Map, Ch4 visual and Ch5 visual send §9 to **4.1 The lower-of rule**. The §9 Official quote itself sits in **4.0**. I kept 4.1, which is consistent everywhere; switch all three to `#s-4-0` if you prefer the quote.
5. **Measurement-only stop chip.** The Map shows `3`, while the Ch1 visual shows `3–5` for the same node (the story table lists §2 · §3). Left as-is on the Map.
6. **Cross-Standard chip** `Official · IAS 16 §8` (Ch1 spare-parts box) cites a Standard outside this pack’s Official PDF. Relabel or keep?
7. **PwC FAQ 25.10.1** appears as a box in both Ch1 and Ch2 (the METHOD maps it to both). Consider keeping one full box and a pointer in the other.
8. `assets/draft.css` has no `?v=` on the chapter pages (site convention only busts iframes). Hard-refresh if the tip / box spacing looks unchanged.
9. The Map label “Disclosure — secondary” is existing chrome that states rank already shown by the lighter frame. Left.
10. CH0N NOTES were not rewritten (content-pass records). The Ch3 renumber is recorded here only.

---

# Map redraw — `ias2-map6` (Johnny correction, 2026-09-30)

The `map5` pass only relinked the Map; its layout was almost unchanged. This pass **redraws the Map composition**, then re-checks every link against the current chapter HTML. Chapter bodies and chapter visuals are untouched.

**Files:** `visuals/map-formula-board.html` (rewritten), `visuals/ias2.css` (new namespaced `.m-*` Map rules; removed the Map-only `.gate*` / `.ias2-kicker` / `.exit-stem` / `.exit` rules, which no chapter visual uses; `.gate-body` kept for Ch5), `index.html` (iframe `?v=ias2-map6`).

## Story and visit path (skill §0, unchanged story)

Scope question → in-scope outcome (stops branch right as dead ends) → stem → **§9 board** → Cost arm (build, then assign; LIFO muted) ∥ NRV arm (measure, then “if NRV < cost”) → exit stem → expense exit → disclosure (lightest).

## What changed visually vs `map5`

| Mistake class in `map5` | Redraw move |
|---|---|
| No gate/outcome split: the GO card was simply the top-left box | **Gate question header** (“Scope — is this an inventory asset in IAS 2?”, the Map-story wording, linked to Ch1 1.0) with **three outcome cards hanging from it** in one row: in scope (accent, wider) · full exclusion · measurement only |
| The stem floated in a void, because the stop column was taller than the GO card | All three outcomes share one row height; the stem leaves the **GO bottom edge** and its arrow meets the **board top edge** |
| The stops sat directly above the board and read as feeding it | Each stop ends in a **muted dead-end cap** (short shaft + bar, no arrowhead): “stop — no IAS 2 carrying amount” / “stop — lower of not applied” (Ch1 1.5 wording). Only GO has an accent stem |
| Cost was an 11-item stack against 3 NRV cells, so the peers had unequal rank | **Same-format arms**: each has a head + chip, a one-line definition, then two titled inner plates. Cost = **Build** (Purchase / Conversion / Other as compact label-and-body rows, IAS 23 tip beside Other, §16 “Not in cost” as the plate’s boundary line) + **Assign — cost formulas**. NRV = **Measure** + **If NRV < cost** (Write-down 28–29 / Reversal capped 33). Equal width, equal height. The NRV see-also is pinned to the arm foot |
| NRV had no formula on a formula board | **Measure** shows NRV as a term strip: Estimated selling price − Estimated costs of completion − Estimated costs necessary to make the sale, “in the ordinary course of business” (Official §6 wording). The third term deep-links to the DTT costs-to-sell box `#s-4-ex-costs-sell` |
| The expense exit was **nested inside** the board, as if part of the identity | The exit is now a **separate lighter plate** after a labelled stem (“carrying amount leaves inventory”). Its three routes are peer cells; the thin route to PPE / intangibles is a lighter footer line with the IAS 16 / 38 see-also beside it |
| Disclosure had equal-weight cells, and the “— secondary” label restated rank (AMEND item 9) | **Lightest plate**: no fill, reduced opacity, a ruled 5-column list instead of boxed cells. The label is just “Disclosure”. A fifth entry for §39 nature-of-expense (Ch6 visual wording) → 6.5, so all five Ch6 sections are reachable |
| LIFO looked like a small card | Muted missing-route strip under the FIFO ∥ WA peers: dimmed, with **“LIFO” struck through** and the IN13 mute chip left unstruck. It links to `#s-3-ex-lifo` |
| Board title the same weight as the arms | Hub title 15px with an accented “=”; board frame 1.5px accent; arms sit on a darker ground inside it; “lower of” operator enlarged between the arms |

**Narrow screens:** at ≤800px the arms stack with a horizontal “lower of” between them, the stops move after the exit (never onto the stem), and disclosure goes to 2 columns. At ≤520px everything is a single column and the NRV terms stack.

**New words on the Map:** plate labels “Build”, “Assign — cost formulas”, “Measure”, “If NRV < cost” come from the Map story (“cost builds…”, “cost formulas assign that pool”) and Ch3/Ch4 existing text (“Assignment — cost formulas”, Ch4 4.1 “If NRV < cost”). The NRV terms are Official §6. The stop-cap labels are Ch1 1.5. No new accounting term, example or illustration.

## Locks preserved

1. §9 lower of cost and NRV is the hub title of the only accent plate.
2. Cost ∥ NRV are same-format, equal-rank arms either side of an unboxed “lower of”, with no stem between them.
3. The stem leaves the GO card only. The stops are capped dead ends and never touch the board.
4. LIFO is a muted, struck, missing route (IN13), not a peer.
5. Expense exit and disclosure are lighter secondaries (no accent, no fill; disclosure lightest).
6. Explicit stops: biological assets and agricultural produce at the point of harvest (IAS 41 see-also), and commodity broker-traders at fair value less costs to sell.
7. Chapter 2 stays a thin text pointer inside the GO card.
8. IAS 2 / IFRS labels only (no HKAS on any page).

## Final Map link table (checked against the current chapter HTML)

| Map node | Target |
|---|---|
| Scope question | `ch01#s-1-0` |
| In scope §6 · IFRS 15 see-also · Ch2 pointer | `ch01#s-1-1` · `ch01#s-1-4` · `ch02#s-2-1` |
| Full exclusion §2 (+ IAS 41 see-also) | `ch01#s-1-2` |
| Measurement only §3 | `ch01#s-1-3` |
| Board §9 | `ch04#s-4-1` |
| Cost §10 · Purchase §11 · Conversion §12–13 · Other §15 | `ch03#s-3-1` · `#s-3-2` · `#s-3-3` · `#s-3-5` |
| IAS 23 see-also · Not in cost §16 | `ch03#s-3-7` · `#s-3-6` |
| Specific identification §23 · FIFO ∥ WA §25–27 | `ch03#s-3-10` |
| LIFO (IN13) | `ch03#s-3-ex-lifo` |
| NRV §6–7 · selling price / costs of completion · CF see-also | `ch04#s-4-2` |
| Costs necessary to make the sale | `ch04#s-4-ex-costs-sell` |
| Write-down §28 – §29 · Reversal §33 | `ch04#s-4-3` – `#s-4-4` · `#s-4-7` |
| Expense exit §34 – §35 · Sold · Write-down or loss · Reversal | `ch05#s-5-1` – `#s-5-4` · `#s-5-1` · `#s-5-2` · `#s-5-3` |
| Thin route · IAS 16 / 38 see-also | `ch05#s-5-4` |
| Disclosure §36 – §39 | `ch06#s-6-1` – `#s-6-5` |
| Policies · Balances · FV carve-out · Expense/write-downs/pledges · Nature of expense | `ch06#s-6-1` · `#s-6-2` · `#s-6-3` · `#s-6-4` · `#s-6-5` |

Link checker: **0 broken** across all 13 pages (42 Map links, 29 distinct targets).

**Cache-bust:** Map = `ias2-map6` (`index.html` iframe + Map `ias2.css` link). Chapter visuals stay on `ias2-v4`. Their rules in `ias2.css` are unchanged, apart from deleting Map-only selectors they never used.

## Left for Johnny (Map)

- **Whitespace under the NRV arm.** The Cost arm genuinely carries more content (build + assign + LIFO). The arms are kept equal height for peer rank, so there is empty space above the pinned NRV see-also. The alternative is uneven arm heights.
- **Iframe dead space** below the Map inside the fieldset is still the `theme.js` height-measure issue (earlier item 1; Build).
- **Measurement-only stop chip** stays `3` (the story table says §2 · §3); the Ch1 visual shows `3–5`.
- **§9 chip** still targets 4.1 (earlier item 4).
