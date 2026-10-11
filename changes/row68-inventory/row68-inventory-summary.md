# Row 68 phase 1 — OCI / P&L / FV inventory

Phase 1 only. No teaching HTML was edited. Head is `ee89185c0073bdab81a74c2dda606364b8272da9` (PR #108 squash, IAS 16 right-of-use depreciation).

Scope is every `*.html` file `tools/check-incremental.py` treats as teaching text (`in_scope`: all HTML except a path segment `_archive/`). Also excluded, as already converted in #106: the IAS 16 map-section regions `ch04-reval` and `ch04-impair`, including their `include:` copies. Those regions contain **0** remaining hits of the three phrases.

Search is case-insensitive and includes plurals (`fair values`, `profits or losses`, `other comprehensive incomes`), possessives (`'s` / `’s`), and hyphenated joins (`fair-value`, `profit-or-loss`, `other-comprehensive-income`, `statement-of-profit-or-loss`). **810** hits: P&L 420, FV 338, OCI 52.

## Counts by class × pack

| Class | cf-2018 | homepage | ias-16 | ias-2 | ifrs-18 | Total |
|---|---:|---:|---:|---:|---:|---:|
| SWAP | 109 | 0 | 213 | 107 | 82 | 511 |
| KEEP-OFFICIAL | 2 | 0 | 0 | 7 | 16 | 25 |
| KEEP-TITLE | 21 | 4 | 13 | 0 | 136 | 174 |
| KEEP-CITE | 0 | 0 | 1 | 1 | 0 | 2 |
| KEEP-ABBREV | 0 | 0 | 4 | 2 | 6 | 12 |
| COMPOUND | 0 | 0 | 3 | 64 | 19 | 86 |
| UNSURE | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 132 | 4 | 234 | 181 | 259 | 810 |

## Abbreviations pages

A “yes” means the Abbreviations table has a short-form cell that is exactly that token. `FVTPL`, `FVPL`, and `FVLCD` are different rows and do not count as FV, OCI, or P&L.

| Pack | Abbreviations page | FV | OCI | P&L |
|---|---|---|---|---|
| cf-2018 | No Abbreviations page | — | — | — |
| homepage | No Abbreviations page | — | — | — |
| ias-16 | `ias-16/draft-v1-linked/abbreviations.html` | yes | yes | yes |
| ias-2 | `ias-2/draft-v1-linked/abbreviations.html` | no | no | no |
| ifrs-18 | `ifrs-18/draft-v1-linked/abbreviations.html` | yes | yes | yes |

IAS 2’s page defines `fair value through profit or loss` as **FVPL**, and not FV, OCI, or P&L. IFRS 18 also defines **FVTPL**. IAS 16 defines `fair value less costs of disposal` as **FVLCD** in addition to FV, OCI, and P&L.

## How to read the CSV

Columns: `pack`, `file`, `line`, `locator`, `term`, `matched`, `context`, `class`, `reason`, `proposed_new_text`, `sentence_start`, `include_of`.

`context` is collapsed whitespace, up to 40 characters each side, with the hit wrapped in `[[ ]]`. `locator` is the nearest id, otherwise the heading id, otherwise `section:` plus the map section. `proposed_new_text` is filled for SWAP, COMPOUND, and UNSURE only, and uses exactly **OCI**, **P&L**, and **FV**. For a compound, that cell is the whole compound rewritten once (`FV through P&L`, `FV through OCI`, `FV less costs to sell`, `FV less costs of disposal`); the reason names which token the row is, so the pair is not applied twice. `sentence_start` is `yes` when a swap of that hit would open a sentence, heading, or label (after a section number such as `7.5`). `include_of` is set on the **34** rows that sit in an `<!-- include: -->` copy; `tools/check-incremental.py` treats the source file as the owner of that text.

`sentence_start=yes` on **124** rows, of which **89** are SWAP or COMPOUND (the rows a later swap would actually change).

## Class rules applied

- **SWAP** — teaching prose, labels, headings, tips, cards, and aria-labels written by Content. Proposed text is OCI, P&L, or FV for that token.
- **KEEP-OFFICIAL** — inside `<q>` or `<blockquote>`, or a passage in curly quotes (including a firm extract in a Sources-differ cell). A compound inside a quotation stays KEEP-OFFICIAL.
- **KEEP-TITLE** — statement names (including `statement of profit or loss and other comprehensive income` and the hyphenated `statement-of-profit-or-loss`), IFRS 18 subtotals and paragraph 118 line items (`operating profit or loss`, `profit or loss before financing and income taxes`, `gross profit or loss`, `profit or loss before income taxes`, `profit or loss from continuing operations`, `total other comprehensive income`), the IFRS 13 title Fair Value Measurement, the fair value hierarchy, and the IAS 40 fair value model. A bare `Profit or loss` cell is KEEP-TITLE only in an IFRS 18 statement schematic; elsewhere it is a Content label (SWAP).
- **KEEP-CITE** — cite chips and References page rows. The two hits are `IFRS 13 Fair Value Measurement` on the IAS 16 and IAS 2 References pages.
- **KEEP-ABBREV** — the full-form cell of an Abbreviations table. The IAS 16 paragraph 6 term list under that table is KEEP-TITLE, not a second abbreviation row.
- **COMPOUND** — `fair value through profit or loss`, `fair value through OCI`, `fair value less costs to sell`, `fair value less costs of disposal`. Counts of rows (each token is its own row): FV less costs to sell 63, FV through P&L 20, FV less costs of disposal 2, FV through OCI 1.
- **UNSURE** — none left. The close calls below were given a class anyway.

Plurals (13 rows) and possessives are proposed as the singular abbreviation, not `FVs`. Hyphenated joins (22 rows) are included; replacing `fair-value-measured` in place reads `FV-measured`.

## Classifications that were close

No row is classed UNSURE. These are the calls a reviewer is most likely to reverse:

1. **Content headings that also name the topic were SWAP**, because the brief puts Content headings in SWAP. Examples: `cf-2018/draft-v1-linked/ch07.html` `#s-7-5` “Profit or loss and other comprehensive income” (sentence-start on P&L); the same words on the CF index and chapter visuals; `ias-16/draft-v1-linked/ch02.html` `#s-2-5` “Day-to-day servicing → profit or loss”; `ias-2/draft-v1-linked/ch04.html` `#s-4-2` “Net realisable value and fair value”; `ias-2/draft-v1-linked/ch06.html` `#s-6-4` “Amounts recognised in profit or loss”. Keeping the official words in the heading would move these to KEEP-TITLE.
2. **IFRS 18 defined subtotals and line items were KEEP-TITLE**, not shortened to P&L. That includes `operating profit or loss` (36 tokens inside that name) and the paragraph 118 names. A ruling that the sweep may shorten those tokens would reclass them as SWAP, proposed `P&L`, and would change a large block of `ifrs-18`.
3. **Compound proposals do not use FVTPL, FVPL, FVOCI, or FVLCD.** They use FV, OCI, and P&L inside the compound (`FV through P&L`, and so on). IFRS 18 already maps the through-profit-or-loss compound to FVTPL, IAS 2 maps it to FVPL, and IAS 16 maps fair value less costs of disposal to FVLCD. Phase 2 should not invent those shorter forms unless the ruling says so.
4. **`fair value model` (IAS 40) and `fair value hierarchy` (IFRS 13) are KEEP-TITLE**, including hyphenated `fair-value hierarchy`. They are named bases, not ordinary uses of “fair value”.
5. **Curly quotes.** A passage in curly quotes is KEEP-OFFICIAL even when the speaker is DTT or PwC in a Sources-differ cell, not only when it is the Standard. A short quoted term (“Other comprehensive income”, “total for profit or loss”) is KEEP-TITLE. The scare quote “not fair value only” in `cf-2018/draft-v1-linked/visuals/ch06-measurement.html` is SWAP.
6. **Definitional prose is SWAP**, with `sentence_start=yes`, for sentences such as “Fair value is the price…”. Only a definition list is KEEP-TITLE. The one list hit is the paragraph 6 term roll on the IAS 16 Abbreviations page (`fair value` among the terms “used in full”).
7. **cf-2018 has no Abbreviations page, and IAS 2’s page has no FV, OCI, or P&L rows.** The SWAP proposals in those packs still say FV, OCI, and P&L. Applying them in phase 2 needs new abbreviation rows first, or readers have no expansion.
8. **Homepage cards** `Fair value measurement` under the code IFRS 13 (four wireframe/demo copies) are KEEP-TITLE, the standard’s name in sentence case, not a teaching swap.
9. **Include copies are separate rows** (34), almost all the IAS 16 master map repeating a chapter visual. `include_of` names the source. Editing only the source would leave the copy stale, and the checker does not count the copy as a second owned item.
