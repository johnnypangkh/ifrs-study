# STANDARDISE — one job, one look

**Status:** proposals for Johnny’s sign-off. **Nothing here is applied.** Under owner rule 10, each item is first drawn on the Master formatting page, signed, and only then rolled out to chapters. Formatting only: no IFRS wording changes. Where an item would need new words, it says so and stops.

Each item gives:
- what differs today (with file, class and section);
- the one proposed standard and why;
- the map sections it affects;
- the before/after mock.

**Before** panels are real crops from the live maps (`evidence/`). **After** panels are drawn with the site’s dark tokens (`_shared/tokens-core.css`).

Order = how much each item helps the reader, highest first.

Part A is “same job, different markup”. Part B is “breaks an owner rule”.

---

## Part A — same job, different markup

### S1 · Group label on the left: one rail chrome
**Today.** One job (“everything to my right is this group”) is done four ways:

| where | markup | look (computed, dark 1280) |
|---|---|---|
| IAS 16 ch05 §5.1, Residual, §5.2, §5.3, §5.5 … | `.inner-rail` + `.rail-name` | boxed, `--band`, 1 px `--line`, 12 px / 700 |
| IAS 16 ch05 §5.4 *During use*; ch04 ×2 | `.lc-head-k` | **unboxed**, transparent, 12 px / 700 — sits in the same column as the boxed rails |
| IAS 16 master, all 9 phase rails (*Scope* … *Disclosure*) | `a.rail-link` | boxed, `--surface` (not `--band`), **14 px** / 700 |
| CF ch01–02, ch06–07, ch09–11; IFRS 18 ch01–08 | top kicker (B07): `.ou-label`, `.pa-label`, `.ts-label`, `.zone-head`, `.pd-kicker` … | no box; **three sizes**: 12 px/700, 11 px/400, 10 px/700 + 0.8 px tracking |

**Standard.**
- (a) A left rail is always `.inner-rail` + `.rail-name`, on the shared track. This is signed dep-v2 unify-A, and MF §10 (draft) generalises it.
- (b) The master phase rail keeps its own *level* but uses the same chrome family. A larger type step is allowed only because it is one level up; that is the documented deviation rule 2 allows.
- (c) A top kicker uses one recipe: T2-band, 12 px / 700, uppercase, `--muted`, 0.48 px tracking (today’s `.ou-label` / `.pa-label` / `.ts-label`).

**Why.** Owner rule 2: same-level rails align in style. The live ch05 *During use* rail is the exact case Johnny already signed (unify-A) but which exists only in `dep-v2.html`.
**Affects.**
- IAS 16 ch04 *Life cycle axis shared by both events* and *During use, with the impairment date*; ch05 §5.4; master rails.
- CF ch06 `.mx-kicker`, ch07 `.pd-kicker`, ch09–11 `.zone-head`.
**Mock.** `mocks/S01-rail-chrome.png`.
**Not proposed here.** Turning CF/IFRS 18 top kickers into left rails is a bigger change, so it is ENHANCE E1.

### S2 · “All must hold” connector: AND, not +
**Today.** Five forms. The worst problem: the AND criteria use the **same** `+` (accent 15 px / 700) as arithmetic plus in formulas. On IAS 16 ch01 §1.1, *Tangible + Held for use + More than one period* is drawn exactly like *Cost = Purchase price + Directly attributable costs* (ch03 §3.1).

| map · section | between criteria | junction | crop |
|---|---|---|---|
| IAS 16 ch01 §1.1 *Is it PPE in IAS 16?* | `span.crit-op` “+” | none | `evidence/C-and-gate-ias16.png` |
| IAS 16 ch02 §2.0 *Capitalise as PPE?* (+ master splice) | `span.crit-op` “+” | none | — |
| IAS 2 ch02 §2.2 *Three criteria, all required* | `span.or` “and” (class is *or*) | question text | `evidence/C-and-gate-ias2.png` |
| IAS 2 ch01 §1.1 *Definition of inventories* | `div.st-plus` “+” | none | `evidence/C-fork-ias2.png` |
| CF ch02 §2.5 *Fundamental — both required* | `.qc-op` “+” | kicker text | `evidence/C-and-gate-cf02.png` |
| CF ch05 §5.3 *Usefulness tests* | `.rc-op` “+” | `.rc-bar` | `evidence/C-and-gate-cf05.png` |

**Standard.** The signed MF §9 recognition pattern:
- an **AND pill** (T3, 700, `--accent` text, 1 px `--line`, `--radius-pill`) between criteria;
- a **junction bar** under the row, with one arrow down to the outcome.
- `+` is kept for arithmetic only.
- The junction carries words only where the map already has them (“both required”, “Are all three criteria met?”). Adding “Both required” elsewhere is new wording and needs Johnny’s OK.

**Why.** Owner rule 4: an explicit AND when all conditions must hold. And a reader should never mistake a test for a sum.
**Affects.** The six sections above. CF ch03 §3.2 *re-dual-and* sits inside a sentence and stays prose.
**Mock.** `mocks/S02-and-connector.png`.

### S3 · Yes / No on arrows: one label
**Today.** Six styles (computed):

| style | maps |
|---|---|
| “Yes” / “No”, ink, 10 px / 600 | IAS 16 `.arm-label`; CF index `.arm-label` |
| “yes” / “no”, muted, 11 px / 700 | IAS 2 `.stem-label` (ch01–06, master) |
| outlined pill “Yes” / “No”, 11 px / 700 | CF ch09–11 `.mid` |
| “no”, muted, 11 px / 600 | CF ch05 `.rc-link-label` |
| “no”, muted, 11 px / 700 | IFRS 18 ch06 `.gt-ans` |
| UPPERCASE via CSS, 10 px | IFRS 18 ch03 `.pc-stem-label`, `.pc-yes-label` (“YES → TEST IN ORDER”) |

**Standard.**
- T3 (10 px), 700, `--muted`, no border, knocked out on `--bg`, centred mid-arm.
- First letter capital via CSS (`::first-letter`), so no source text is edited.
- IFRS 18 ch03 drops `text-transform: uppercase`.

**Why.** Rule 6, same logic = same format. Grammar skill §3: one label per arm, centred mid-arm, same height.
**Affects.** Every fork and ladder: IAS 16 ch01, ch02, master; IAS 2 ch01–06, master; CF ch05, ch06, ch09–11, index; IFRS 18 ch03, ch05, ch06.
**Mock.** `mocks/S03-yes-no-label.png`.

### S4 · Timeline: one shared component (kit 25)
**Today.** Four markups:
- IAS 16 `.lc-head` (ch04 ×2, ch05 §5.4, master ×3);
- IAS 16 ch03 `.ready-axis`;
- CF ch03 §3.2 `.re-axis`;
- IFRS 18 `ol.wn-tl` (ch01) and `ol.tr-tl` (ch08).

Across them:
- **Markers to labels:**
  - IAS 16 cards float above the end rings, with no leader to the ring.
  - CF ch03 puts labels under the rings.
  - IFRS 18 puts dates above and cards below.
- **Between-marker note:** only IFRS 18 ch08 §8.2 *Retrospective* (`p.tr-span`).
- **Live ch05 §5.4** still shows 4 “Year-end” ticks plus a “Year-end” key. The signed Dep lock removed them (kit 25: “no YE markers”), but only in `dep-v2.html`.

**Standard.** Signed kit 25:
- the axis is `--stroke-1 --accent`, with rings **on** the axis;
- each marker has a leader to its label card;
- one **span caption** sits between markers (dashed line + T3 muted).
- The **same component** is used on all 7 timeline maps. Chapter CSS only sets how many markers.

**Words.** A span caption uses only text already on the map, e.g. IFRS 18 ch08 *Retrospective*, IAS 16 *Depreciate over useful life* (signed). Where a map has no between-text today (CF ch03, IFRS 18 ch01), the span stays empty until Johnny supplies the words.
**Why.** Owner rules 5 and 6.
**Affects.**
- IAS 16 ch03 §3.5; ch04 §4.5 and impairment; ch05 §5.4; master.
- CF ch03 §3.2.
- IFRS 18 ch01 *Effective date timeline*; ch08 §8.1–8.2.
**Mock.** `mocks/S04-timeline.png`.

### S5 · See-also: one dashed pointer
**Today.** Four looks (computed):

| look | where |
|---|---|
| dashed 1 px `--see` purple, “See also” in `--see` | IAS 16 `p.see` (12 px / 700, chip width); IAS 2 `.see` (11 px / 400, full width) |
| dashed 1 px `--dash` grey, muted text | CF ch03 `.re-see`, ch06 `.mx-see`, ch07 `.pd-see`; IFRS 18 ch01 `.wn-see` |
| no border, muted line | `.see-also-strip`: CF ch05–08, IFRS 18 ch08 |
| **solid** 1 px `--line` frame of muted cards | CF ch09–11 `aside.sec` “See also” |

There is also a misuse: dashed borders are put on **content** boxes, so content looks like a pointer. This breaks the shared grammar, which `_shared/visuals.css` states in its header: “solid = peer / containment; dashed = see-also (or matrix N/A) only”.
- IAS 16 ch04 §4.5 *Revalued asset* (`.impair-formula-contrast-cell.m-see`, `evidence/S-m-see-on-content-ias16-ch04.png`);
- IAS 16 ch04/ch06 §6.6 *Compensation for impairment*: rule text with cite chips (`.impair-comp.m-see`, `.comp-nest.m-see`);
- IFRS 18 ch06 §6.4 *Reconciling items* (`.rc-step--mid`, dashed `--line`; `evidence/C-formula-ifrs18-ch06.png`).

**Standard.**
- One brick, `.m-see` (`map-box.css` L89–103): dashed 1 px `--see`, label “See also” in `--see`, T3, transparent.
- It has two sizes: chip (inline) and strip (one line under a plate).
- CF ch09–11 zones become a dashed `--see` frame.
- Content boxes drop `.m-see` and become plain Cells.

**Why.** A reader must be able to tell “go elsewhere” from “this is the rule” at a glance.
**Affects.** IAS 2 ch01–05 + master; CF ch03, ch05–11, index; IFRS 18 ch01, ch06 §6.4, ch07, ch08; the IAS 16 content misuses in ch04, ch06 and the master.
**Mock.** `mocks/S05-see-also.png`.

### S6 · Thick-left strip: financial-statement lines only
**Today.** 38 strips, all IFRS 18 (computed: left border ≥ 3 px; `CENSUS.md` §4). That confirms the handover fact that the strip is IFRS 18 only. But the strip is **not** only on FS lines:

| kind | elements | sections |
|---|---|---|
| FS line / category band (correct) | `.pc-band` ×5, `.ts-band` ×5, `.mini-pnl-band` ×10, `.oe-row--face` ×3, `.ofs-line--start` | ch03 pnl, ch04 §4.1, ch05 §5.3, ch07 §7.4, index, jumpboard |
| category landing (borderline) | `.pc-leaf` ×5, `.pc-mba` | ch03 *Classification decision tree*, §3.5 |
| **not a line** | `.pa-trap` (ch02 *Trap*), `.ts-trap` (ch04 §4.2 *Exception*), `.ts-regime` ×3 (ch04 §4.4, §6.1), `.rc-step` ×3 (ch06 §6.4 bridge) | — |

Outside IFRS 18 the nearest thing is CF ch03 `.re-obj`, a 2 px accent-mix left border (below the 3 px threshold).

**Standard.**
- The strip lives only in K11 Statement (MF §10 audit: “thick-left ≈ IFRS 18 FS `.m-strip`”).
- Traps and exceptions become full-border **Tone warn** (`.m-warn`).
- Regimes and reconciliation steps become plain Cells; the MPM step keeps `--mpm` as a full border.
- Category landings keep the strip, because they *are* the category; to be confirmed by Johnny.

**Why.** One meaning per paint. Once the bar also means “trap”, it stops meaning “line on the statement”.
**Affects.** IFRS 18 ch02 §2.3; ch04 §4.2, §4.4; ch06 §6.4.
**Mock.** `mocks/S06-strip-scope.png`.

### S7 · Formula: one row recipe, one ledger recipe
**Today.**
- IAS 16 uses `.cost-eq` / `.cost-identity` / `.mini-formula` and the ledger `.vledger`.
- IAS 2 ch05 uses `.exp-f`.
- The **IAS 2 master alone** uses three: `.m-sum` (vertical, `+` between `.m-row` boxes, *Cost of inventories*), `.m-formula` (unboxed terms, *Measure NRV*), and `.m-eqn` (boxed cells, *Inventories sold …*). Plus `p.m-op` “lower of”.
- CF ch04 uses `.el-eq`. IFRS 18 ch06 uses `.rc-bridge`, whose `±` is the only muted, 18 px operator (all others are accent 15 px).
- **Result side.** IAS 16 puts the result first (`X = a − b`). IAS 2 ch05, CF ch04 and IFRS 18 ch06 put it last. This follows a real rule, so it is **not** an inconsistency:
  - **define** a term → result first;
  - **compute** a flow or reconciliation → result last.
  - Write the rule down; change nothing.

**Standard.**
- **Formula row** (K8): Cells with T2 titles, operators unboxed `--accent` 15 px / 700 centred on the row midline, result cell `.m-result`.
- **Ledger** (K9): the IAS 16 `.vledger` recipe; single rule = subtotal, double rule = total.
- The IAS 2 master `.m-sum` becomes a ledger, and `.m-formula` / `.m-eqn` become one formula row.

**Why.** Rule 6; grammar skill *Equations* (operators unboxed, centred).
**Affects.** IAS 2 master (*Cost of inventories*, *Measure NRV*, *Inventories sold …*); IFRS 18 ch06 §6.4 operator colour.
**Mock.** `mocks/S07-formula.png`.

### S8 · Matrix: one table recipe
**Today.** Three chromes for “same questions × several items”:
- every cell boxed: CF ch06 §6.4 `.mx-cell`, IFRS 18 ch02 §2.3 `.matrix-cell`;
- one frame with hairline row rules: CF ch08 §8.1 `.cap-matrix`, IFRS 18 ch08 `.tr-mx`;
- boxed rows holding ledgers: IAS 16 ch04 `.lens-row`.

The stub column is UPPERCASE on CF ch06, IFRS 18 ch02 and IFRS 18 ch08, but sentence case on CF ch08 and IAS 16 ch04.

**Standard.**
- One frame (L3), hairline row and column rules (`--stroke-1 --line`).
- Stub column on `--band`, header row T2-band, stub labels in sentence case bold (no CSS uppercase).
- Cells are unboxed unless they hold a formula or ledger (the allowed 3rd level).

**Why.**
- An all-boxed grid adds a border level for no meaning (grammar skill §4: max 2).
- Ruled rows read straight across (grammar skill: “one shared row grid”).

**Affects.** CF ch06 §6.4; IFRS 18 ch02 §2.3; stub case on IFRS 18 ch08.
**Mock.** `mocks/S08-matrix.png`.

### S9 · One class, one job
- **`a.rail-link`** is both the master phase rail (9 on the master) and the chapter-end hand-off (`a.rail-link.handoff`, IAS 16 ch02–ch05). Split it: rail chrome per S1; `.handoff` keeps the K12 Hand-off look.
- **`.sec`** is both the CF index section chip (`a.sec` ×64, `a.sec-sm` ×8) and the CF ch09–11 “See also” zone (`aside.sec`). Use `.fb-num` for the chip (it already measures identical: 11 px / 700, 46×22) and `.m-see` for the zone (S5).
- **`span.or`** holds “and” on IAS 2 ch02 and “or” on IAS 2 ch01. The AND case moves to the S2 pill.

**Why.** When the class says one thing and does another, the next restyle breaks the other job.
**Mock.** none (markup only; no visual change).

---

## Part B — breaks an owner rule

### S10 · Graph paper is still painted (rule 9)
- `_shared/modules/visuals/map-box.css` L22–37: `.m-l0 { background-image: linear-gradient(...) }` (“#89 field”).
- Visible on 4 maps: IAS 16 master, IAS 2 master, CF index `#conceptMap`, IFRS 18 index `#conceptMap` (computed `background-image` contains a gradient).
- Signed GB-SOLID and MF §9 (“kit 2 STRUCK — solid background = `var(--bg)` only”) both say it should be gone.
- **Standard:** `.m-l0 { background: var(--bg); }`. This is one shared-CSS change and needs no chapter edits.
- **Mock:** `mocks/S10-solid-bg.png`.

### S11 · Paragraph cite chips on IAS 16 maps (rule 8)
- **40 `.cite` chips:**
  - ch04 ×17, e.g. *Revaluation (revaluation model only)* “IAS 16 · para 41”, *Revaluation increase or decrease* “IAS 16 · para 30”, plus EY chips;
  - ch06 ×2, §6.6 *Compensation for impairment* “para 65 / 66”;
  - ch07 ×2, *Disclosure* “para 73(e)” + KPMG;
  - master ×19 (spliced copies).
- The 2026-10-03 strip pass (`_shared/MAP-STRIP-PARA-CHIPS-KEY-CHANGES-2026-10-03.md`) cleared IFRS 18, CF and IAS 2 but never covered IAS 16.
- Also chip-styled: IAS 2 master `.ias2-mute-chip` “IN13”.
- **Standard:**
  - No `.cite` markup inside `body.embed`. Remove the chip markup only, as the 2026-10-03 pass did.
  - Before removing, check that each reference already exists in the chapter body text. That check is content, not formatting, and is listed for Johnny.
  - Plain-prose references (“Para IN13; BC9–BC21”, “IFRS 1 D16(a)”, “IFRS 18 App D”) are wording and stay.
- **Mock:** `mocks/S11-cite-chip.png`.

### S12 · Same thing drawn twice on one map (rule 7)
- **IAS 16 master During-use timeline ×3.** `tools/build-map-includes.py` splices section `ch05-axis` into *ch04-reval* and *ch04-impair*, so the master shows the same Begins / Ceases axis three times (`.lc-head` ×3; `evidence/S-master-timeline-repeat.png`). Chapter ch04 itself shows it twice.
  - **Standard:** draw the axis once per map. Revaluation dates (`.lc-dia`) and the impairment date become **event lanes** under that one axis, using kit 25’s “optional markers” lane.
  - This is direction only: the splice markers decide what is copied, so the build tool and the master change together, after sign-off.
- **IAS 16 ch01 §1.3 *Excluded from IAS 16?*** lists the four exclusions as `.item-rows` inside the question. It then repeats the same four as cells under *IAS 16 does not apply*, each with its See-also. **Standard:** show each exclusion once. See ENHANCE E3 (it touches what is shown, so it is a proposal).
- **Mock:** `mocks/S12-draw-once.png`.

### S13 · Red stops and box depth (grammar skill §3, §4)
- **Red stops.** The CF index has **2** red `.m-stop` leaves: *Not that element* and *Do not recognise*. The skill says “≤ 1 per board, justify a second”. Every other board has ≤ 1. **Standard:** keep *Do not recognise* red (the true hard stop); *Not that element* becomes a muted dead-end (`.m-flow.mute` + plain Cell). Johnny to confirm which is the true stop.
- **Box depth.** Measured nesting of bordered, non-pill boxes, from `CENSUS.md` §3:
  - 5 levels: IAS 16 ch06, IAS 16 master, IAS 2 master, CF index;
  - 4 levels: IAS 16 ch03 / ch04 / ch05, CF ch07, IFRS 18 ch03-mba-nest / ch05 / jumpboard / index.
  - The cap is 2, with a 3rd only for formula, ledger and see-also. **Standard:** the innermost `.item-rows` / `.inner-detail` box goes unboxed (a Note-weight list) when it sits inside a rail detail. A formula or ledger may keep its box.
- **Mock:** `mocks/S13-stop-and-depth.png`.

---

## Sign-off order (smallest first, each one reversible)

1. **S10 solid background.** One shared rule; already signed in principle.
2. **S3 Yes/No labels.** CSS only.
3. **S5 See-also.** CSS only, plus 3 class removals.
4. **S2 AND pill.** A glyph swap plus a junction bar.
5. **S1 rail chrome.** Applies the already-signed unify-A to live ch04 and ch05.
6. **S6 strip scope.**
7. **S8 matrix.**
8. **S7 formula.**
9. **S4 timeline.** Shared component; biggest; after S1.
10. **S12 draw once.** Needs the splice tool; after S4.
11. **S11 cites.** Needs the body-text check first.
12. **S13 depth.**
13. **S9 markup.** Invisible; do it with whichever item touches the file.
