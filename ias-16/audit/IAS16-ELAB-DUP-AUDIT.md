# IAS 16 — Layer-2 teaching-body audit (elaboration + duplication)

**Date:** 2026-10-10 (Asia/Shanghai, UTC+8)  
**Workbook:** #56 (under IAS 16 parent #42)  
**Auditor:** Grok, cloud agent  
**Base:** `main` @ `da186539` — *Densify five IAS 16 medium teaching gaps (#86)*  
**Surface:** `ias-16/draft-v1-linked/ch01.html`–`ch07.html`, `abbreviations.html`  
**Companion:** `ias-16/audit/IAS16-ELAB-DUP-SUMMARY.json`

**This job edits no teaching HTML.** Ranked briefs below are for a later densify / dedupe pass.

---

## 0. Question and method

Johnny’s two questions, applied to every section and every Illustration:

1. **Elaboration sufficient?** Exceptions, formulas, worked detail and firm locators are present where the pack Big4 text (as recorded in the chapter CONTENT-NOTES) has substance.
2. **No duplication?** The same point is not written twice unless the second unit has a distinct firm view, an extra test, or unique numbers. Agreeing firms belong in one dense unit with a chip each.

**Rules used:** teaching-body duplication HARD and detail-first (2026.10.10); acceptance cues §7.A.5 (duplicate plates) and §7.D (densify). Home-chapter rule: one plate, elsewhere a one-line pointer.

**Read, and not re-done:**

| Input | Use |
|---|---|
| `ifrs-teaching-body` + `ifrs-teaching-body-qa` | Scoring rules |
| Layer-1 refs audit + summary | Context only. Source stocktake not repeated. |
| CONTENT-NOTES ch01–ch07 (post-#86 notes for ch03, ch04, ch06, ch07) | Where a firm plate has substance, and which #55 gaps HTML now claims to hold |
| Live HTML on `da18653` | The scored text |

**Scores**

| Score | Meaning |
|---|---|
| **OK** | Enough sourced detail for that point, and the unit is not a repeat. |
| **DUP** | Overlapping prose, no distinct firm view, extra test, or unique numbers. |
| **THIN** | Pack substance (named example, exception, or formula in NOTES) is missing or reduced to a sentence that drops the test. |

Image-only Practical plates and blank KPMG journal tables are **not** scored THIN. Inventing them would break the no-invent rule. Deliberate see-also tips (IAS 20, IAS 23, IAS 36, IFRS 16 sale-and-leaseback) are OK when they state the IAS 16 limb and point onward.

**Mechanical density (context, not the verdict):** 76 Illustrations. Peer text is above the ~350-character densify floor on every plate. Structure density is not the failure mode. The failures are repeated points, and a few named DTT plates that never landed.

---

## 1. Verdict

**BOTH — needs dedupe and needs densify.**

The spine a learner actually studies (scope through disclosure, with worked numbers on revaluation, components, depreciation and derecognition) is in good shape. 145 of 154 walked units are OK. The #86 additions closed the Layer-1 *topic* gaps and, on several of them, also pasted the new section into an Illustration that adds no numbers.

| | Count |
|---|---:|
| Units walked (77 sections + 76 Illustrations + abbreviations) | 154 |
| OK | 145 |
| DUP units | 9 |
| THIN existing unit (one bullet inside an otherwise OK section) | 1 |
| THIN missing plates (no unit yet) | 4 |
| Critical issues | 1 |
| Medium issues | 9 |
| Nice backlog | 8 |

Illustrations on this SHA: ch01 5, ch02 10, ch03 16, ch04 12, ch05 20, ch06 7, ch07 6. Total **76** (Layer-1’s 66 plus the #86 additions).

---

## 2. Top 10

| # | Sev. | Kind | Where | What to do later |
|---|---|---|---|---|
| 1 | Critical | DUP | Illus **2.6.2** and **6.5.1** | One EY Illustration 3-3. Same machinery: CU10 million, ten years, replacement CU200,000, original pump ≈ CU170,000, remaining CA ≈ CU51,000. Ch6’s only addition is that the CU51,000 write-off is a para 68/71 loss. Keep one plate; add that loss sentence on the home; one-line pointer in the other chapter. Keep `s-6-ex-replace-pump`. |
| 2 | Medium | DUP | §**3.1A** and Illus **3.1A.1** | The strip repeats control, fair value, stand-alone selling price, and EY’s tooling / utility-connection / outsourcing examples already in the bullets. No currency. |
| 3 | Medium | DUP | §**3.7A** differ table and Illus **3.7A.1** | Cost accumulation versus financial-liability model is already side by side and not reconciled. The strip repeats both approaches with no currency. Illus **3.7A.2** is the subsequent-change test and stays; shorten the section’s subsequent-change bullet to a pointer. |
| 4 | Medium | DUP | h4 **s-4-0-policy-change** and Illus **4.0.1** | Direction rule (current-period revaluation versus retrospective return to cost), class limit, and repeat-change caution are already in the heading. The strip has no journal. |
| 5 | Medium | DUP | §**7.4** and Illus **7.4.1** | Para 74(a)–(c) and DTT’s cumulative-CIP reading are in the section. The strip says the sources state no amounts, then repeats the three limbs. |
| 6 | Medium | DUP | §**7.5** and Illus **7.5.2** | 74A(b) proceeds, cost, and line item are in the peer-row. The strip points at Illus 3.5.1 and adds no figure. Illus **7.5.1** stays: Company W’s PPE compensation is 800, not the 1,000 and not the 200 loss-of-profits piece. |
| 7 | Medium | DUP | §**6.0A** and Illus **6.0A.2** | Physical-part allocation (systematic CA, gain = proceeds − allocated CA, residual keeps the rest) is in the section. The strip states that no currency amount is given. Illus **6.0A.1** stays: 25% of the 100 acres leaves, 75% remains. |
| 8 | Medium | DUP | §**1.2** and §**1.4** | Para 5, fair-value investment property staying in IAS 40, and investment property under construction appear in both. §1.4 is the home. §1.2 should be one line. The single para 5 bullet in §4.0 is already the right pointer shape. |
| 9 | Medium | DUP | Illus **2.4.1** and **2.4.2** | Both are para 11: legally required equipment that does not earn benefits on its own is capitalised, then the combined carrying amount is reviewed under IAS 36. KPMG Example 16 (filters) has no numbers and no different conclusion. Multi-chip the filter facts onto 2.4.1. |
| 10 | Medium | THIN | ch03, DTT cost edges | Absent from HTML: DTT A7 **4.2.6** reimbursement, **4.2.7** broker rebate, **4.2.8** utility capacity fee, **4.2.9-2** occupation approval. **4.2.10-1** asbestos / new obligation (with KPMG Example 7 and PwC FAQ 22.28.2) is one sentence in §3.4 and drops the worked test. NOTES still list the first four as density candidates; a file search finds none of those locators. |

---

## 3. Chapter walk

OK units are one line. DUP and THIN units say why.

### Abbreviations — OK

One table (CU, FV, FVLCD, OCI, P&L, PPE, ROU, VIU) plus the para 6 term list. Chapters use the short forms and do not open a second glossary.

### Chapter 1 Scope — NEEDS DEDUPE

| Unit | Score |
|---|---|
| 1.0 Objective | OK |
| 1.1 Definition, including software-integral and collectibles | OK — each is one firm test with its chip |
| 1.2 When IAS 16 applies | **DUP** — para 5 block repeats §1.4 |
| 1.3 Exclusions + Illus 1.3.1 mineral rights | OK — factors plate is the DTT 2.1-1 case |
| 1.4 Cost-model IP bridge | OK — home of para 5 |
| 1.5 Bearer plants | OK |
| 1.6 lead-in | OK — the four plates carry the teaching |
| Illus 1.6.1 hotel / 1.6.2 base stock / 1.6.3 research / 1.6.4 gold | OK — four different classification tests |
| 1.7 Lessee ROU tip | OK |
| 1.8 Spare-parts pointer | OK — full plate is Ch2 |
| 1.9 Checklist | OK |

### Chapter 2 Recognition — NEEDS DEDUPE

| Unit | Score |
|---|---|
| 2.0 Recognition principle | OK |
| 2.1 Unit of measure | OK |
| 2.2 + Illus 2.2.1 stand-by + Illus 2.2.2 core stock | OK — inventory-versus-PPE is a different test from stand-by |
| 2.3 + Illus 2.3.1 supermarket remodel + Illus 2.3.2 hotel wing | OK — subsequent-benefit test. Ch3’s supermarket (FAQ 22.19.1) is a different test: which opening budget lines are directly attributable |
| 2.4 + Illus 2.4.1 chemical handling | OK — home of the para 11 test (Official, DTT, PwC, EY) |
| Illus 2.4.2 emissions filters | **DUP** of 2.4.1 |
| 2.5 + Illus 2.5.1 redecoration versus partitioning | OK |
| 2.6 + Illus 2.6.1 hotel refurbishment | OK |
| Illus 2.6.2 replacement pumps | OK as the **home** of EY Illustration 3-3. The duplicate is Ch6 |
| 2.7 + Illus 2.7.1 inspection / dry-dock (ship 400 / component 80) | OK — points to Ch5 for KPMG 15B–15D |
| 2.8 Component bridge + carbon-offset tip | OK — three-way classification (IAS 41 / bearer / PPE) is stated; IAS 41 depth stays out |
| 2.9 Checklist | OK |

### Chapter 3 Initial measurement — BOTH

| Unit | Score |
|---|---|
| 3.0 Measure at cost | OK |
| 3.1 Three limbs | OK |
| 3.1A Customer contributions | OK — home of the control / fair-value / stand-alone selling price rule |
| Illus 3.1A.1 | **DUP** of §3.1A |
| 3.2 + Illus 3.2.1 training, 3.2.2 engineer, 3.2.3 supermarket lines, 3.2.4 land clearing, 3.2.5 ROU during construction | OK — each line has its own include-or-expense result |
| 3.3 Exclusions, feasibility, general permits | OK |
| 3.4 Dismantling initial estimate + Illus 3.4.1 | OK on the initial provision. **THIN** bullet: new obligations / asbestos (DTT 4.2.10-1, KPMG Example 7) is one sentence |
| 3.5 + Illus 3.5.1 (20A) + Illus 3.5.2 incidental | OK — testing-output and car-park / sports rental are different buckets. Pre-amendment netting is warned, not taught as current |
| 3.6 + Illus 3.6.1 commissioning + Illus 3.6.2 demolition | OK — design-abandonment and cancellation-fee bullets carry KPMG 1E / 1F |
| 3.7 + Illus 3.7.1 deferred payment | OK |
| 3.7A + Sources differ table | OK — home of the two approaches and the IFRS IC “too broad” note |
| Illus 3.7A.1 | **DUP** of the differ table |
| Illus 3.7A.2 subsequent changes | OK — extra test (capitalise only when linked to the asset initially received). Shrink the matching section bullet to a pointer when deduping |
| 3.8 + Illus 3.8.1 commercial substance + Illus 3.8.2 no substance | OK |
| 3.9 Government grants tip | OK — deliberate IAS 20 pointer; presentation choice is named |
| 3.10 IAS 23 tip | OK — deliberate see-also |
| 3.11 Checklist | OK |
| DTT 4.2.6 / 4.2.7 / 4.2.8 / 4.2.9-2 | **THIN** — missing plates |

### Chapter 4 Models — NEEDS DEDUPE

| Unit | Score |
|---|---|
| 4.0 Choose a model | OK — para 5 appears as one lock-in bullet |
| h4 Changing between cost and revaluation | OK — home of KPMG 3.2.360 / IAS 8.17 |
| Illus 4.0.1 | **DUP** of that heading |
| 4.1 + Illus 4.1.1 office/industrial, 4.1.2 geography, 4.1.3 AUC | OK — three different class judgements |
| 4.2 Cost model / 4.3 Revaluation model | OK. Numbering 4.2/4.3 left untouched (out of scope) |
| 4.4 + Illus 4.4.1 three methods, CU10,000 gain + Illus 4.4.2 mid-life useful-life change | OK — different fact patterns |
| 4.5 + Illus 4.5.1 land CU125→150, 4.5.2 reverse CU15 then OCI CU10, 4.5.3 surplus CU10 then P&L CU5, 4.5.4 depreciation-adjusted reversal | OK — DTT 6.8.3-1 through 6.8.3-4, each with its own opening numbers. Shared words (“land”, “OCI”) are not duplication |
| 4.6 + Illus 4.6.1 surplus transfer | OK |
| 4.7 Optional 29A–29B | OK — election, separate class, and mismatch rationale are stated; outline locks this as a thin note |
| 4.8 IAS 36 pointer | OK |
| 4.9 IFRIC 1 rules + Illus 4.9.1 cost-model remeasurement (1,500 / 100 / 130) | OK. Revaluation-model journals stay in prose because KPMG 6B–6D tables are blank |
| 4.10 Compensation tip | OK as a pointer. A later edit can cut it to one line; it does not repeat Company W’s numbers |
| 4.11 Checklist | OK |

### Chapter 5 Depreciation — OK

| Unit | Score |
|---|---|
| 5.0 + Illus 5.0.1 hotel equipment | OK — replacements do not replace depreciation |
| 5.1 + Illus 5.1.1 second-hand versus scrap + Illus 5.1.2 ship scrap 4,000 / 500 → 260, charge 140 then 150 | OK |
| 5.2 + eight component Illustrations (5.2.1–5.2.8) | OK — roof factory (C1m / 30 years), EY property (CU4m, roof and partitions), ship dry-dock, combining insignificant parts, stadium seating, internal versus external (30), allocation across components, early dry-dock write-off. Each has its own numbers or its own allocation test. Ch2’s ship 80 is the recognition step; these are the depreciation steps |
| 5.3 + Illus 5.3.1 landfill | OK |
| 5.4 + Illus 5.4.1 ready for use + Illus 5.4.2 mothball | OK — begin versus idle-does-not-stop |
| 5.5 + Illus 5.5.1 straight-line CU12,000 + Illus 5.5.2 diminishing balance + sum-of-digits point-chip CU10,000 | OK — three methods, three number sets |
| 5.6 Revenue-based restriction | OK — hard ban, and units of production kept available |
| 5.7 + Illus 5.7.1 absorb into tools | OK |
| 5.8 + Illus 5.8.1 useful-life change, 5.8.2 method change, 5.8.3 residual to nil | OK — 5.8.3’s nil-charge path is a different test from 5.1.2’s scrap revision |
| 5.9 ROU tip / 5.10 bridge / 5.11 checklist | OK |

Units-of-production is named and contrasted with para 62A, and it has no output table. KPMG Examples 12A–12C are blank in the extract, so this is a Nice note, not a THIN fail.

### Chapter 6 Derecognition — NEEDS DEDUPE

| Unit | Score |
|---|---|
| 6.0 When to derecognise | OK |
| 6.0A Partial disposals (teaching) | OK — home of the EY 7.3 rule |
| Illus 6.0A.1 undivided 25% / 75% | OK — extra fraction test |
| Illus 6.0A.2 physical part | **DUP** of §6.0A |
| 6.1 Gain or loss, including KPMG net-proceeds view | OK — firm view Official does not define |
| 6.2 IFRS 15 consideration tip | OK |
| 6.3 + Illus 6.3.1 rental fleet | OK |
| 6.4 Sale-and-leaseback tip | OK — deliberate IFRS 16 pointer |
| 6.5 Replacement section | OK as the derecognition rule. The section tells the reader not to re-dump the capitalise decision, then the Illustration re-dumps the numbers |
| Illus 6.5.1 pumps | **DUP** of Illus 2.6.2 — Critical |
| 6.6 + Illus 6.6.1 fire (CA 600, insurance 1,000, rebuild 900) + Illus 6.6.2 new-for-old | OK — cash recovery versus non-cash replacement are different tests |
| 6.7 + Illus 6.7.1 in-period IFRS 5 | OK |
| 6.8 Checklist | OK |
| Farm-out / carried interest (EY 7.3.1–7.3.2) | Left as a see-also by the #55 brief. Scored OK as a pointer, not a missing IAS 16 plate |

### Chapter 7 Disclosure — NEEDS DEDUPE

| Unit | Score |
|---|---|
| 7.0 Objective / class, components ≠ classes | OK |
| 7.1 Policies, lives, IAS 8 estimates | OK |
| 7.2 Gross carrying amount and accumulated depreciation | OK |
| 7.3 Reconciliation limbs + KPMG additions-versus-business-combination split | OK |
| Illus 7.3.1 mapping known events onto 73(e) | OK — extra test. Entity A’s CU25 million is limb (iv); Company W’s 600 is limb (ii); the 800 compensation is not a 73(e) line; the 900 rebuild is limb (i); business-combination PPE is limb (iii) |
| 7.4 Restrictions, CIP, commitments, DTT cumulative reading | OK — home |
| Illus 7.4.1 | **DUP** of §7.4 |
| 7.5 74A peer-row | OK |
| Illus 7.5.1 compensation 800 | OK — extra disclosure test on the Ch6 facts |
| Illus 7.5.2 20A disclosure | **DUP** of §7.5 |
| 7.6 + Illus 7.6.1 cost-model comparative and borrowing costs | OK — Entity K / IU 05-14 |
| 7.7 + Illus 7.7.1 idle and postponed construction | OK — encouraged versus mandatory |
| 7.8 Package checklist | OK |

Checklist boilerplate that repeats the personal-study disclaimer across chapters is chrome, not a teaching duplicate.

---

## 4. Pairs checked and kept

These looked similar and are **not** duplicates, because the second unit has a different test or different numbers.

| Pair | Why it stays |
|---|---|
| Ch2 supermarket FAQ 22.62.2 and Ch3 supermarket FAQ 22.19.1 | Subsequent sales uplift versus which start-up budget lines enter cost |
| Ch4 4.5.1–4.5.4 | Four DTT land cases, four opening figures |
| Ch5 5.1.2 and 5.8.3 | Scrap revision versus residual rising through carrying amount to a nil charge |
| Ch5 5.2.1 and 5.2.2 | Different buildings and different component costs |
| Ch2 dry-dock 80 and Ch5 15B–15D | Recognition of the inspection component versus internal cost, allocation, and early write-off |
| Ch6 fire plate and Ch7 7.5.1 / 7.3.1 | Same sourced facts, new questions (which amount is 74A(a); which reconciliation limb) |
| Ch3 20A measurement and the disclosure pointer in §7.5 | Measurement home versus disclosure limb. The **Illustration** 7.5.2 is the duplicate; the section pointer is fine |
| Straight-line, diminishing balance, sum-of-digits | Three methods, three CU series |

---

## 5. Ranked remediation (briefs only)

### Critical

1. **Pump plate, one home.** Add the para 68/71 loss sentence to Illustration 2.6.2 (that is the distinct Ch6 test). Replace Illustration 6.5.1’s facts with a one-line pointer to 2.6.2. Keep id `s-6-ex-replace-pump` so links survive.

### Medium

2. **Drop or collapse restated #55 Illustrations** that have no unique numbers: 3.1A.1, 3.7A.1, 4.0.1, 6.0A.2, 7.4.1, 7.5.2. Leave every supporting chip on the surviving section. Keep 3.7A.2, 6.0A.1, 7.3.1 and 7.5.1.
3. **Paragraph 5.** §1.4 remains the home. §1.2 becomes one line plus the link.
4. **Safety / environmental.** One Illustration. Put KPMG Example 16’s filter facts on 2.4.1 and remove 2.4.2, or keep 2.4.2 only if a later read of the PDF shows a test 2.4.1 does not have. On the HTML as it stands, it does not.
5. **DTT initial-cost densify,** from extractable text only: reimbursement 4.2.6, broker rebate 4.2.7, utility capacity fee 4.2.8, occupation approval 4.2.9-2, and a real asbestos / new-obligation plate for 4.2.10-1 and KPMG Example 7. No invented CU.

### Nice

6. Cut §4.10 to one line pointing at §6.6.
7. Units-of-production worked plate only when a non-blank firm table is attached.
8. IFRIC 1 revaluation-model journals only when KPMG 6B–6D tables have body.
9. Optional tips already listed in NOTES and still absent as plates: EY 4.2.2 liquidated damages; EY 3.1.3 pre-permission expenditure; PwC FAQ 22.22.5 mobile-network start-up; PwC FAQ 22.71.2 business-combination rolling revaluation; EY section 6.5 ROU revaluation when the class is revalued.
10. Remove author-meta from the new strips (“the sources do not state currency amounts”, “this illustration does not reproduce a financial-statement image”, “do not re-dump”). Those sentences belong in NOTES.

**Do not densify from:** EY / DTT / PwC / KPMG Practical FS image plates (body unavailable); KPMG Example 8A (pre-20A, already warned); blank method and IFRIC 1 journal tables.

---

## 6. Out of scope (respected)

Chrome and Maps. Chapter 4 heading numbers 4.2 / 4.3. IAS 38 and IAS 40 packs. Merging. Invented financial-statement plates. A fresh PDF stocktake.

---

## 7. Proposed workbook #56 Remarks

Layer-2 body audit on main `da18653` (post #86). Verdict **BOTH**. Critical DUP: EY Illustration 3-3 pumps live as Illustration 2.6.2 and Illustration 6.5.1 with the same CU. Medium DUP: six #55-era Illustrations restate their own section with no unique numbers (3.1A.1, 3.7A.1, 4.0.1, 6.0A.2, 7.4.1, 7.5.2), paragraph 5 is in both 1.2 and 1.4, and safety Illustrations 2.4.1 and 2.4.2 are one test. Medium THIN: DTT 4.2.6–4.2.9-2 absent; asbestos / new-obligation is one sentence. 145 of 154 walked units are OK, including the distinct-number plates in Chapters 4 and 5 and the extra-test disclosure plates 7.3.1 and 7.5.1. Do not invent FS images or blank KPMG journals. HTML not edited in this workbook.

---

## 8. File index

| Path | Role |
|---|---|
| `ias-16/audit/IAS16-ELAB-DUP-AUDIT.md` | This audit |
| `ias-16/audit/IAS16-ELAB-DUP-SUMMARY.json` | Machine-readable verdict |
| `ias-16/audit/README.md` | Folder pointer |
