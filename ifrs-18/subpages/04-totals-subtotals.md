# Chapter 4 — Totals & subtotals

## Purpose
*(HTML page shows **title only** — no purpose blurb, matching CF Ch2 exemplar. Teaching insight stays in body §§4.0+.)*

Required operating profit, profit before financing & tax (§73 awareness), profit or loss; distinguish §118-listed from MPMs.

## Map anchors
- **Required §69** → `#s-4-1`\n- **§73 trap** → `#s-4-2`\n- **Required / §118 / MPM matrix** → `#s-4-4`

## Visual plan
| Type | Artifact |
|------|----------|
| Statement layout (brackets) + matrix (required vs §118 vs MPM) | [`../draft-v1-linked/visuals/ch04-totals-subtotals.html`](../draft-v1-linked/visuals/ch04-totals-subtotals.html) — Design drawn · QC PASS 2026.09.27-7 |
| Linked chapter HTML | [`../draft-v1-linked/ch04.html`](../draft-v1-linked/ch04.html) |

## Teaching sections

### 4.0 Scope of this chapter `{#s-4-0}`

Once categories exist, lock the required totals/subtotals on the statement of profit or loss and separate them from §118-listed (non-MPM) subtotals and from MPMs (Ch6). Colour grammar: --ifrs-subtotal vs --mpm — two tokens only. **§69–74**, **§118**

> **Pitfall:** Equating “gross profit” with an MPM. Gross profit (and similar) is listed in §118 — not an MPM. **§118(a)**

### 4.1 Required presentation — three anchors `{#s-4-1}`

Present totals/subtotals in P&L for: **§69**

| Required measure | Composition (teaching) | Cite |
|---|---|---|
| Operating profit or loss | All income and expenses classified in the operating category | **§69(a)**, **§70** |
| Profit or loss before financing and income taxes | Operating profit plus all investing-category income/expenses — subject to §73 | **§69(b)**, **§71** |
| Profit or loss | Total of income less expenses in P&L — all categories | **§69(c)**, **§72** |

> **Concept insight:** Design brackets sit on the same category-band skeleton as Ch3: operating profit closes the operating band; “before financing & tax” closes operating+investing; profit or loss closes the statement. **§69–72**

### 4.2 The §73 policy-exception trap `{#s-4-2}`

Do not present the §69(b) “profit or loss before financing and income taxes” subtotal if the entity applies the §65(a)(ii) policy of classifying in operating the income/expenses from raising-finance liabilities that do not relate to providing financing to customers. **§73**

Such an entity still uses §24 to decide whether an additional subtotal after operating profit (and before financing) is needed for a useful structured summary — e.g. operating profit plus equity-method investment results. Do not label that extra subtotal as if it excludes financing (avoid “profit before financing” wording when financing amounts remain inside). **§73–74**, **§43**

**Contrast**

| Main path — present §69(b) | Special-entity path — §73 |
|---|---|
| Most entities: operating profit → + investing → “profit before financing and income taxes” → financing → tax → discontinued → profit or loss. **§69–72** | Policy under §65(a)(ii) moves some raising-finance amounts into operating → skip §69(b); any extra subtotal must be faithfully labelled (no fake “before financing”). **§73–74** |

### 4.3 Line items — thin pointer `{#s-4-3}`

§75 lists amounts to present in P&L (or disclose in notes), including revenue, operating expenses (as shaped by §78/§82), equity-method share of profit/loss, income tax, discontinued-operations total, and specified IFRS 9 amounts. Attribution of profit or loss to NCI and owners of the parent is presented outside the five categories. **§75–76**

### 4.4 Required vs §118-listed vs MPM — the three-column matrix `{#s-4-4}`

Not every useful subtotal is an MPM. §118 lists subtotals of income and expenses that are not management-defined performance measures: **§118**

- gross profit or loss (revenue − cost of sales) and similar subtotals;

- operating profit before depreciation, amortisation and IAS 36 impairments;

- operating profit and income/expenses from all equity-method investments;

- for a §73 entity: operating profit plus all investing-category amounts;

- profit or loss before income taxes;

- profit or loss from continuing operations.

| Column | What it is | Token | Cite |
|---|---|---|---|
| Required (§69) | Must present (subject to §73 for the middle subtotal) | --ifrs-subtotal + bracket weight | **§69–72** |
| Listed §118 | IFRS-recognised subtotals — not MPMs; may still be presented/used | --ifrs-subtotal | **§118** |
| MPM | Meets §117 definition → single-note reconciliation regime | --mpm | **§117**, **§122–123** → Ch6 |

> **Concept insight:** Same colour family for required and §118 (IFRS measure space); different token for MPM (different disclosure regime) — not “more important rainbow.” **§69**, **§118**, **§117**

#### Worked example — gross profit vs “adjusted operating profit”

- **Facts:** Entity publishes (A) gross profit on P&L and (B) “adjusted operating profit” excluding restructuring in the earnings release.
- **Concept / gate:** (A) §118(a) → not MPM. (B) subtotal of income/expenses · public communications · management view · not §118/required → gate to MPM (Ch6). **§118**, **§117**
- **Conclusion:** Listed ≠ MPM. Run the §117 gate before forcing every non-GAAP label into the MPM note.

### 4.5 Additional subtotals (compatibility) `{#s-4-5}`

Additional subtotals on PFS must remain compatible with the category structure and required totals — faithfully labelled (§24 / §43). They do not replace the §69 anchors. **§24**

## Key terms

- operating profit or loss
- profit or loss before financing and income taxes
- profit or loss
- §73 policy exception
- §118-listed subtotals (non-MPM)
- MPM (bridge to Ch6)
- --ifrs-subtotal / --mpm


## Refs used
- Official IFRS 18 (HKFRS 18 text): `§69–74 · §75–76 · §118 · §24` — paraphrase only
- KPMG First Impressions — visual/flow cross-check
- EY Applying IFRS closer look (MOA 2026) — depth/FAQ cross-check
- Deloitte IAS 1 A4 — bridge only (not structural)
