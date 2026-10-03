# Cursor Grok 4.7 — CF Ch1–7 EY advisory comments

**Job:** #4 CF Ch1–7 EY advisory (comments only).  
**Who:** Cursor Grok 4.7 (cloud). Not Grok Bot. Not Opus densify.  
**Date:** 2026-10-02.  
**HTML:** not edited.

## Sources used

| Source | This run |
|--------|----------|
| Official *Conceptual Framework for Financial Reporting* (2018) | Read (text extract) |
| EY *International GAAP* 2026 **Ch2** Conceptual Framework (by-chapter PDF) | Primary. Section text read for every locator behind a failed or firm-specific chip |
| EY iGAAP 2026 Ch1, Ch3 (IAS 1), Ch4 (IFRS 18), Ch5 | Attached. Used only where a Ch1–7 teaching claim points at presentation / status. No Ch5 (IFRS 5) hit in the EY chips |
| EY master PDF | **Not attached.** Not searched |
| PwC MOA | **Missing.** No PwC sentence was checked, added, or “corrected” |
| DTT / KPMG | Not this job. Existing chips left as they stand |

Pack under review: `ch01.html`–`ch07.html` (draft-v1-linked).  
EY chips found: **370**. **369** are `EY iGAAP 2026 Ch2 · section …`. **1** is `EY IFRS Developments 169 · May 2020` (not a book section; publication not attached).  
Zero `§` inside `.cite`. Official chips use `para`. Book chips use `section`. That hygiene holds except the Developments chip.

Method: unique EY locators were cut from the Ch2 extract and compared with the teaching sentence they sit on. Overlap misses and every firm-specific / historical sentence were read in the book. The other chips are Official restatements that sit on the matching EY section’s Framework extract. They are not re-listed one by one.

## Counts

| Severity | Count |
|----------|------:|
| **Blocker** | **1** |
| **Should-fix** | **14** |
| Note (no Opus rewrite required to clear the gate) | see chapter skims |

---

## Blocker

### B1 — Ch4 / `#s-4-ex-executory` / Illustration 4.7.1

- **Severity:** Blocker
- **Class:** EY-miss
- **Evidence:** Assessment peer: “a contract that is equally unperformed is typically **neither an asset nor a liability** in full — unless the terms are onerous / other Standards require recognition.” Title chips include `EY iGAAP 2026 Ch2 · section 7.1.2` and `CF 2018 · para 4.56–4.58`.
- **EY locator:** Ch2 **section 7.1.2** (CF 4.57): the combined right and obligation **constitute a single asset or liability**. Favourable terms → asset; unfavourable terms → liability. **Whether that asset or liability is included in the financial statements** depends on the recognition criteria and the measurement basis, including any onerous test.
- **Advice for Opus:** Rewrite that Assessment bullet so the definition (single asset or liability) and recognition (often not included; onerous test / Standards) are separate sentences, in the words of CF 4.57 / EY 7.1.2. Keep the plate — it is a named fact pattern, not a plain-paragraph Illus. Company C / pay **100** is **not** in EY 7.1.2 (KPMG Example 2 chip; KPMG not attached). Do not add or “complete” those facts. Do not call the plate invent. Do not reconcile the onerous-test point into a third view.

---

## Should-fix

### S1 — Ch2 / `#s-2-2` — nature-of-item list

- **Severity:** Should-fix
- **Class:** EY-miss
- **Evidence:** Nested list (related parties, profit-to-loss, consensus, covenants, fines, key suppliers/customers/employees) ends with `PwC MOA 2020 · FAQ 1.51.1` · `CF 2018 · para 2.11` · `EY iGAAP 2026 Ch2 · section 5.1.1`.
- **EY locator:** Section **5.1.1** quotes CF 2.6–2.11, including obscuring and “could reasonably be expected to influence”, and the ban on a uniform quantitative threshold. It does **not** contain that list. Those phrases are also absent from the Official CF extract.
- **Advice for Opus:** Take the EY chip and the Official chip off the FAQ list. If the lead “nature or magnitude, or both” stays, chip **that sentence only** to `CF 2018 · para 2.11` and `EY iGAAP 2026 Ch2 · section 5.1.1`. Do not invent an EY section for the list. PwC chip stays; PwC body not verified.

### S2 — Ch2 / `#s-2-2` — “Standards need not be applied to immaterial items”

- **Severity:** Should-fix
- **Class:** EY-miss
- **Evidence:** Bullet “Immaterial items — Standards need not be applied” cites `EY iGAAP 2026 Ch2 · section 5.1.1` (with KPMG and BC2.20A).
- **EY locator:** “need not be applied” does not occur in EY Ch2. The only “immaterial” hit in Ch2 is **section 4.1.2** (IAS 1.30A / IFRS 18.41(e) — obscuring material information), not 5.1.1. The **definition** sentence (obscuring + “reasonably be expected”) **is** in 5.1.1.
- **Advice for Opus:** Keep the EY 5.1.1 chip on the definition wording only. Remove it from the “need not be applied” clause. Do not move that clause onto 4.1.2 — 4.1.2 is the IAS 1/IFRS 18 obscuring rule, not an “IFRS need not be applied” rule.

### S3 — Ch2 / `#s-2-2` differ vs the same PwC locator

- **Severity:** Should-fix
- **Class:** differ
- **Evidence:** The materiality bullet quotes the **post-2018** definition and chips `PwC MOA 2020 · 1.32` and `PwC MOA 2020 · 1.51`. The callout “Sources differ — wording of the materiality definition” says PwC **1.51** and FAQ 1.51.2 quote the **earlier** wording (“could influence”, no “obscuring”). The callout has the “not reconciled” line and does not reconcile. EY is not in the callout.
- **EY locator:** Section **5.1.1** uses the **new** wording (obscuring + reasonably be expected). EY agrees with the Official row. It is not a third view.
- **Advice for Opus:** Do not pick a winner. PwC is not attached. Stop using locator **1.51** on both sides. Until PwC is attached, leave the differ as Official vs PwC and take `1.51` off the new-wording sentence (keep `1.32` only if a later PwC pass confirms it). Do not add EY to the PwC side. Do not rewrite either quotation from memory.

### S4 — Ch1 / `#s-1-3` — PwC user list under EY chips

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** “Not primary users” ends: Framework names regulators and members of the public; “PwC also lists employees, suppliers, customers, and governments and their agencies.” Chips: `CF 2018 · para 1.9–1.10` · PwC 1.18 · `EY iGAAP 2026 Ch2 · section 4.1.1` · `section 4.1.2`.
- **EY locator:** **4.1.1** names regulators and members of the public (CF 1.10) and adds EY’s own point that the objective leaves out corporation tax and distributable-profit uses. **4.1.2** says management need not rely on general purpose reports (CF 1.9). Neither section lists employees, suppliers, customers, or governments.
- **Advice for Opus:** Close the EY chips on the Framework sentence. Leave the extra list on the PwC chip only (unverified). Optional separate unit, EY only: section 4.1.1’s tax-and-distributions comment. Do not attribute that comment to the Official objective.

### S5 — Ch1 / `#s-1-4` — “more prominence” on section 4.1.1

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** Lead: the 2018 Framework “gives it more prominence”. Chips include `CF 2018 · para BC1.33` and `EY iGAAP 2026 Ch2 · section 4.1.1`.
- **EY locator:** **4.1.1** restates CF 1.3 (stewardship as one of the two assessments). “more prominence” / “reintroduced” does not appear in EY Ch2.
- **Advice for Opus:** Keep BC1.33 on the prominence sentence. Move the EY chip to the sentence that stewardship is one of the two assessments (4.1.1 / CF 1.3). Examples of management’s responsibilities stay on **section 4.2.3** (already used at 1.4’s later bullet — that one matches).

### S6 — Ch1 / `#s-1-2` — defined-term footnotes

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** Bullet lists the Framework footnotes (financial reports, entity, management, primary users) and chips `EY iGAAP 2026 Ch2 · section 4.1.1`.
- **EY locator:** **4.1.1** only has the shorthand “collectively, ‘users’ or ‘primary users’”. It does not reproduce the other footnotes.
- **Advice for Opus:** Drop the EY chip from the full footnote list, or narrow the EY-supported words to the primary-user shorthand.

### S7 — Ch3 / `#s-3-6` — IAS 27 “separate”

- **Severity:** Should-fix
- **Class:** EY-miss
- **Evidence:** “The Framework’s ‘unconsolidated’ is IAS 27’s ‘separate’.” Chips: `CF 2018 · para 3.11` · `DTT A2 2022 · 6.2` · `EY iGAAP 2026 Ch2 · section 6.2`.
- **EY locator:** EY Ch2 has **no** “IAS 27” and **no** “separate financial statements”. Section 6.2 / 6.2.1 use the Framework word “unconsolidated” only. The Official extract of para 3.11 likewise does not name IAS 27.
- **Advice for Opus:** Remove the EY chip from this bullet. Keep `para 3.11` for the word “unconsolidated” only. Do not invent an IAS 27 paragraph (IAS 27 is not attached). Leave the DTT chip unchanged.

### S8 — Ch3 / `#s-3-7` — combined financial statements and carve-out

- **Severity:** Should-fix
- **Class:** differ
- **Evidence:** Lead and first bullet: combined statements are acknowledged; the Framework does not say when or how. Chip `EY iGAAP 2026 Ch2 · section 6.2` sits on that Official/BC sentence. No differ callout.
- **EY locator:** Same section **6.2**, after CF 3.14, adds views that are not the BC sentence:
  1. EY reads the discussion as seeming to confirm that combined financial statements **can be said to comply with IFRS** (subject to the 3.14 bullets and IFRS compliance generally).
  2. EY then quotes the BC hesitancy (useful in some circumstances; Framework does not discuss when or how — BC3.21).
  3. EY says the Framework is silent on **carve-out** accounting.
  4. **How we see it:** considerations similar to those for combined financial statements should apply to carve-out financial statements.
- **Advice for Opus:** Add `aside.callout.differ`, title “Sources differ — combined financial statements and carve-out”. Official row: BC3.21 (acknowledges the concept; does not discuss when or how) with `CF 2018 · para BC3.21`. EY row: points 1 and 4 above, chip `EY iGAAP 2026 Ch2 · section 6.2`. Closing line: “Shown side by side and not reconciled.” Do not add a PwC row. Do not fold “in our view” into the silence sentence. Point the existing see-also (Ch9 / Ch10) at the callout id instead of repeating the difference.

### S9 — Ch4 / `#s-4-0` and `#s-4-1` — section 7 chips on BC-only sentences

- **Severity:** Should-fix
- **Class:** EY-miss
- **Evidence:**
  - `#s-4-0`: “lowers the existence hurdle” and “does not change the liability vs equity distinction” chips `EY iGAAP 2026 Ch2 · section 7` next to DTT and KPMG.
  - `#s-4-1`: “more effective, efficient and rigorous to define assets and liabilities first” chips `section 7` next to BC4.94.
  - `#s-4-0` contrast: “an entity considers the definitions and the recognition criteria at the same time” chips `section 7.2.2` and `section 7.3.2`.
- **EY locator:** Section **7** restates the five elements and EY’s “balance sheet approach” label, then points at sections 8–10. It does not use “existence hurdle”, “liability vs equity distinction”, or “effective, efficient and rigorous”. **7.2.2** says a low probability can still be an asset and that the probability affects recognition and measurement (CF 4.14–4.15). It does not say the entity applies definition and recognition “at the same time”.
- **Advice for Opus:** Remove those EY chips from the BC/DTT sentences. If an EY chip stays on the element chapter, put it on a sentence section 7 actually makes (elements linked to resources, claims and changes; performance derived from the movement in financial position — EY’s “balance sheet approach”). Low-probability-still-an-asset stays on **7.2.2** (and the liability twin on **7.3.2**), which other bullets already do correctly.

### S10 — Ch4 Illus 4.2.2 and 4.2.4; Ch5 Illus 5.2.1 — FAQ wording inside the Conclusion peer

- **Severity:** Should-fix
- **Class:** differ
- **Evidence:** The plates are named entity facts (not plain-paragraph Illus). Conclusion peers state the pre-2018 test as the outcome:
  - **4.2.2:** “sufficient **expectation** or control of any economic benefits”.
  - **4.2.4:** benefits “**expected to flow**”; value “**reliably measured**”.
  - **5.2.1:** acquired brands recognised if control and “the **probable flow** of future economic benefits” are met; cost “**reliably measured**”.
  Each page already has a differ callout that places those phrases on the PwC FAQ side and the 2018 definition/recognition test on the Official side, with “Shown side by side and not reconciled.”
- **EY locator:** Not an EY plate. EY 7.2.2 is the 2018 potential test (one circumstance is enough; low probability can still be an asset), which is the Official side of the existing differ.
- **Advice for Opus:** Do not demote the plates and do not delete the entity facts (PwC not attached — do not verify, extend, or invent). In the Conclusion peer, mark the expectation / probable-flow / reliable-measurement sentences as the **FAQ outcome**, so they do not read as the 2018 definition. Leave the differ. Do not reconcile. Do not add an EY chip to the FAQ outcome.

### S11 — Ch5 / `#s-5-2-ex` — IFRS Developments 169

- **Severity:** Should-fix
- **Class:** cite
- **Evidence:** See-also: “Amendments update IFRS 3’s Conceptual Framework reference and add an IAS 37 / **IFRIC 21** recognition exception to avoid **day-2** gains/losses.” Chip: `EY IFRS Developments 169 · May 2020` plus `CF 2018 · para SP1.2`. The alert is **not attached**. The chip is not `EY iGAAP 2026 Ch2 · section …`.
- **EY locator:** The attached book covers this in **section 2** (footnote 7: *Reference to the Conceptual Framework, Amendments to IFRS 3*, para 64Q, May 2020). IFRS 3 kept the 2010 Framework until periods beginning on or after 1 January 2022; an exception makes IFRS 3 refer to **IAS 37** rather than the Framework in certain circumstances, so an acquirer does not recognise liabilities it would not recognise otherwise and then derecognise them for a gain the Board did not consider an economic gain. The exception is expected to remain while IAS 37’s liability definition differs. Section 2 does **not** name IFRIC 21, “day-2”, or “IFRS Developments 169”.
- **Advice for Opus:** Replace the Developments chip with `EY iGAAP 2026 Ch2 · section 2`. Rewrite the callout to those section 2 sentences. Drop “IFRIC 21” and “day-2” unless the alert is later attached and those words are in it. Keep `CF 2018 · para SP1.2`. Do not expand the alert from memory.

### S12 — Parent section cited where EY has a lettered subsection

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** The parent heading exists, so the cite is not “not found”. The sentences live in the lettered child. Pattern (retarget, do not rewrite the teaching):

| Teaching home | Chip now | Retarget |
|---------------|----------|----------|
| Ch5 `#s-5-5` exceptionally wide range / sensitivity / difficult allocations (CF 5.20) | `section 8.2.2` | **`8.2.2.A`** Measurement uncertainty |
| Ch5 `#s-5-5` explanatory information about existence, measurement, or outcome (CF 5.21–5.23) | `section 8.2.2` | **`8.2.2.B`** Other factors |
| Ch6 `#s-6-3` fair value (CF 6.12–6.16) | `section 9.1.2` | **`9.1.2.A`** |
| Ch6 `#s-6-3` value in use / fulfilment value | `section 9.1.2` | **`9.1.2.B`** |
| Ch6 `#s-6-3` current cost (CF 6.21–6.22 only — see S13) | `section 9.1.2` | **`9.1.2.C`** |
| Ch6 `#s-6-5` characteristics / market-sensitive items (CF 6.49–6.53) | `section 9.3.1` | **`9.3.1.A`** |
| Ch6 `#s-6-5` contribution to cash flows (CF 6.54–6.57) | `section 9.3.1` | **`9.3.1.B`** |
| Ch7 `#s-7-3` offsetting (CF 7.10–7.11) | `section 10.2.1` | **`10.2.1.A`** (keep `7.1.1` for the unit-of-account contrast — EY states that cross-reference) |
| Ch7 `#s-7-5` profit or loss, OCI, recycling (CF 7.15–7.19) | `section 10.2.3` | **`10.2.3.A`** |

- **Advice for Opus:** Retarget those chips. Do not retarget a genuine chapter-scope sentence (for example Ch1 `#s-1-0` “flow from the objective”, which is the opening of EY **section 4**).

### S13 — Ch6 / `#s-6-3` — academic-literature sentence under the current-cost EY chip

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** Current-cost paragraph ends “a significant body of academic literature advocates it, though it is not widely used in IFRS Standards” and chips `CF 2018 · para BC6.28` together with `EY iGAAP 2026 Ch2 · section 9.1.2`.
- **EY locator:** **9.1.2.C** stops at CF 6.21–6.22 (entry value; used asset estimated from a new-asset price). “not widely” does not appear in EY Ch2. BC6.28 in the Official PDF is the academic-literature sentence — that half is Official, not invent.
- **Advice for Opus:** Split the paragraph. EY chip on the CF 6.21–6.22 sentences only, retargeted to **`section 9.1.2.C`**. BC6.28 stays Official-only.

### S14 — Ch7 / `#s-7-5` — one statement or two

- **Severity:** Should-fix
- **Class:** EY-soft
- **Evidence:** “One statement or two is a Standards decision… Since 2007 that decision has been set out in IAS 1.” Chips include `CF 2018 · para 7.15 fn11`, `BC7.11`, and `EY iGAAP 2026 Ch2 · section 10.2.3`.
- **EY locator:** The “does not specify single statement or two” sentence is **footnote 9 under section 6.1.1**, not section 10.2.3. EY Ch2’s presentation sections do not say the choice has been in IAS 1 since 2007.
- **Advice for Opus:** Move the EY chip to `EY iGAAP 2026 Ch2 · section 6.1.1` and attach it only to “the Framework does not specify one statement or two”. Leave the 2007 / IAS 1 history on the Official footnote and BC7.11.

---

## Chapter skim (Ch1–Ch7)

### Ch1 — Objective — skim: pass with S4–S6

EY sections **4, 4.1.1, 4.1.2, 4.2.1, 4.2.2, 4.2.3, 8.1** match the objective, users, limitations, resources/claims, accrual, and the CF 5.5 matching sentence (sale of goods for cash; matching is not an objective). `#s-1-6` “balance sheet” in the matching bullet is the pack’s word; EY 8.1 says “statement of financial position”. Not an EY-miss of the rule.

**Note (densify, not a wrong cite):** EY **4.1.1** adds that limiting the objective to resource providers leaves out corporation tax and restrictions on distributions. EY **4.1.2** adds IAS 1.30A and IFRS 18.41(e) / B3 (do not obscure material information), and points IAS 1/IAS 8 to EY Chapter 3 and IFRS 18 to EY Chapter 4. Neither comment is in Ch1. If Opus adds them, they are EY-only units with those locators — not Official paras.

No Illustration. No differ. Body peer-rows and mini-flow read Test → outcomes, question not in the outcome box.

### Ch2 — Qualitative characteristics — skim: fail until S1–S3

Sections **5.1.1, 5.1.2, 5.1.3, 5.2.x, 5.3** support relevance, faithful representation (substance, prudence both ways, no systematic asymmetry), the fundamental process, enhancing characteristics, and the cost constraint. The materiality **differ** is shaped correctly (table, both sides, “not reconciled”) except the locator clash in S3. EY uses the **new** materiality wording; do not put EY on the PwC side.

No Illustration (the materiality unit is an Assessment mini-flow, not an Illus — correct). Prudence contrast is a non-Illus `.contrast-pair` (ok/warn allowed there).

### Ch3 — Financial statements and the reporting entity — skim: fail until S7–S8

Sections **6.1.1–6.1.4, 6.2, 6.2.1** support objective and scope, reporting period and comparatives, perspective, going concern, the reporting-entity definition, and consolidated vs unconsolidated. `#s-3-5` “branch or defined region” is on `section 6` with a DTT chip; EY 6.2 says “a portion of an entity” and later “part of a legal entity” for carve-out, but does not say “branch”. Soft only — do not invent a tighter EY locator.

**Illustration 3.4.1** is a KPMG fact pattern (liquidation / IFRS 9), not an EY plate. No EY chip. KPMG not attached: do not verify or extend the “Insights 1.2.70.50–60” cases. The CF 3.9 / SP1.2 / IFRS 9 split (going concern does not rewrite derecognition) is the Official point and is not an EY-miss.

### Ch4 — Elements — skim: fail (B1, S9, S10)

Asset / liability / equity / income / executory / substance sections **7.2.1–7.2.3, 7.3.1–7.3.3, 7.4, 7.5, 7.1.1–7.1.3** match the definition bullets that quote CF 4.x (rights, potential, control, no practical ability to avoid, unit of account, substance). Those chips can stay.

**Illus 4.2.1–4.2.4 and 4.5.1** are PwC FAQ fact patterns (entities, and in 4.5.1 the amount C500,000). They are Illustrations, not plain-paragraph wrong-shape. PwC not attached: **do not confirm, delete, or add facts**. 4.2.1’s “balance sheet” / “criteria of an asset” is FAQ wording; the differ already covers the expectation test for 4.2.2 and 4.2.4 (S10). 4.5.1’s “income statement” / “balance sheet” is not EY’s label; there is no EY chip on that plate.

**Illus 4.7.1** is B1. EY 7.1.2 supports the principle, not Company C or the amount 100.

Existence-uncertainty differ (Official 4.13 / 5.14 / 6.61–6.62 vs PwC 1.65) is tabled and not reconciled. EY **9.3.2** distinguishes existence uncertainty from measurement uncertainty (same direction as Official). Do not add an EY row that restates Official as if it were a firm difference. PwC side unverified.

Income/expense “recognition criterion” differ (Official definitions 4.68–4.69 vs PwC label) is tabled and not reconciled. EY **7.5** states the definitions, not PwC’s “recognition criterion” label. Same advice: do not force EY onto that differ.

### Ch5 — Recognition and derecognition — skim: fail until S11 (and S10, S12)

Sections **8.1, 8.2, 8.2.1, 8.2.2, 8.3** support the recognition process, relevance (existence uncertainty, low probability), faithful representation, and derecognition (transferred component, retained component, continued recognition of the transferred component as the case where derecognition is not enough). Letter-level retarget is S12.

**Illustration 5.2.1** is a PwC FAQ (Entity F, beverage brand). Differ on probable-flow / reliable-measurement is correctly not reconciled (S10). No EY chip on the plate. Do not invent an EY brand example — EY Ch2 has none.

Derecognition differ (Official BC5.28–BC5.29 vs DTT “akin to control / risks-and-rewards” vs KPMG “control-based”) is tabled and not reconciled. EY **8.3** restates CF 5.26–5.33 and does **not** use “control approach” or “risks and rewards”. Do not add an EY row that invents those labels. If a row is added later, it may only repeat section 8.3’s two aims and the last-resort continued recognition, side by side, not reconciled.

### Ch6 — Measurement — skim: pass after S12–S13

Sections **9.1.1, 9.1.2.A–C, 9.2, 9.2.1, 9.2.2.A–C, 9.3–9.3.5, 9.4, 9.5** support historical cost, the three current values, information in both statements, selection factors, initial measurement (market terms, deemed cost, CF 6.80(a)–(d)), equity as a residual, and cash-flow-based techniques. “long-term investment” / “business activities are a fact” is Official BC6.40–BC6.42 only (no EY chip on that bullet — correct; those words are not in EY Ch2).

Outcome-uncertainty differ (Official 6.58–6.62 vs PwC 1.86) is tabled and not reconciled. EY **9.3.2** matches the Official distinction (outcome uncertainty and existence uncertainty may contribute to measurement uncertainty and need not). Do not put EY on the PwC side. PwC side unverified.

**Illustration 6.7.1** is KPMG Example 3 (inventory to a shareholder; fair value / free / above fair value). No EY chip. KPMG not attached: do not verify the three variants or add numbers.

### Ch7 — Presentation and disclosure — skim: pass after S12 and S14

Sections **10, 10.1, 10.2, 10.2.1.A, 10.2.2, 10.2.3.A, 10.3** support communication, objectives and principles (entity-specific vs boilerplate, duplication), classification, offsetting, equity classification, profit or loss as the **primary source** (CF 7.16 — EY’s words, not “primary performance indicator”), default location, exceptional OCI, historical-cost components in profit or loss, recycling when there is a clear basis, and aggregation. The two differs (primary-source wording; recycling) are tabled and not reconciled. EY **10.2.3.A** tracks the Official “primary source” wording, so it is not a third label next to PwC “primary performance indicator” or DTT “primary measure”. Do not add EY as a reconciled middle.

**Note (densify):** EY **10.2.3.A** also (a) quotes the IFRS 18 Appendix A definition of other comprehensive income, (b) remarks that IFRS 18.B87 says the components “include” rather than “comprise”, and (c) quotes BC7.24 (default location) and BC7.29 (permanent exclusion only for a compelling reason — the compelling-reason point is already in the teaching). The IFRS 18 definition and the include/comprise remark are not in Ch7. If Opus adds them, chip `EY iGAAP 2026 Ch2 · section 10.2.3.A` only. EY **Chapter 4** is the IFRS 18 manual; the Ch7 see-also has no EY chip. Do not invent a Ch4 section number for that see-also. Operational categories, MPMs, and subtotals stay in EY Ch4, not in this CF chapter.

No Illustration in Ch7. Mini-flows: question on the left, arms on the right, outcomes not in the question box. Aggregation’s first arm is “No” and the second is “Yes”; both are terminal outcomes of one question, so that order is not a reverse walk.

---

## Reading order, Illus shape, cite hygiene (pack-level)

- **Reading order:** Body mini-flows are DOM-ordered question → branch → arms, L→R then T→B inside the arms. A question does not share a box with its outcomes. Peer rows in Ch1–Ch2 follow the section story left to right. **No screenshot narration** (comments-only; CF desktop). Chapter Maps were not redrawn and were not failed from a crop. No “Section chips follow the order of the decisions” lecture note in the pack HTML.
- **Illus vs FAQ:** The eight Illustrations are worked-strips with entity facts. They are not plain-paragraph or checklist Illus. S10 is a Conclusion-wording differ, not a demotion. B1 is a wrong statement of CF 4.57, not a wrong-shape classification.
- **Invent:** Nothing in the attached Official CF or EY Ch2 was found to be a fake company invented by the pack **and** attributed to those two sources. Firm plates (PwC FAQ, KPMG examples) cannot be confirmed. That is a **hold**, not an invent finding. Do not label Official restatement as invent.
- **Cite hygiene:** Pass, except S11 (Developments 169) and S12 (parent vs letter). No house-only EY chip. No `§` in chips.

---

## Priority for Johnny — Continue / Hold

**Continue (Opus can fix from the attached Official CF and EY Ch2 only):**

1. **B1** — Illustration 4.7.1 Assessment (definition vs recognition).
2. **S1, S2, S4, S5, S6, S7, S9, S11, S12, S13, S14** — move or drop EY chips; retarget lettered sections; replace Developments 169 with section 2.
3. **S8** — add the combined / carve-out differ from EY section 6.2. Do not reconcile.
4. **S10** — label FAQ wording inside the Conclusion peers. Do not rewrite the facts.

**Hold:**

1. **S3** and every PwC FAQ body (Ch2 materiality list and old/new definition, Illus 4.2.1–4.2.4, 4.5.1, 5.2.1) until PwC MOA is attached. Do not invent PwC. Do not delete those plates on this pass.
2. KPMG plates (Illus 3.4.1, 4.7.1 facts, 6.7.1) and DTT chips — not this job. Do not extend them.
3. EY master PDF — not used. Do not treat this note as a master-book search.
4. Ch8–Ch11 — out of scope. Ch3 links to `ch09.html` / `ch10.html` were not opened.

**Do not reconcile** any differ already on the page (materiality wording, existence uncertainty, asset-test FAQs, income “recognition criterion”, brand FAQ, derecognition approach, outcome uncertainty, profit-or-loss label, recycling).
