# IAS 16 — References page outline (42j)

**Date:** 2026-10-07 (Asia/Shanghai, UTC+8)  
**Workbook:** #42 · sub-row **42j**  
**Pack path (when HTML unlocked):** `ias-16/draft-v1-linked/references.html`  
**Status:** Outline only · **NO HTML** until Johnny accepts  
**Owner:** IAS 16 Content  
**Template:** Mirror IAS 2 `references.html` (two-column Full name | Short form; Official block + Big4 block + how-derived)  
**Chrome (when HTML):** `data-ias16-pill-bar` · `data-page="references"` · disclaimer · footer-nav — same as ch06/ch07  

**Not in this row:** Concept Map / Map HTML stays **42a PARKED**. Do not unlock Map under 42j. Do not start IAS 38 / IAS 40 packs.

---

## 1. Learning goal

Cite Official + pack Big4 chips used across Abbreviations + ch01–ch07. Honest inventory — **no invented sources**. Locators stay on chapter pages; References lists work titles only.

---

## 2. Page structure (proposed HTML spine — hold until accept)

| id | Section | Content |
|----|---------|---------|
| `page-header` | References | Purpose: sources evidenced in cite chips (abbreviations + ch01–ch07) |
| `s-ref-official` | Official | Two-col table: Full name \| Short form (`cite-official`) |
| `s-ref-big4` | Big 4 firm manuals | Two-col table: Full name \| Short form (house + work title) |
| `s-ref-method` | How this list was derived | Cite chips only · full names from stocktake / NOTES · no invent |
| disclaimer | pack-disclaimer | Personal study pack wording (IAS 16 label) |

No Map iframe. No densify. No chapter teaching prose.

---

## 3. Official — proposed rows (evidenced as `cite-official` chips)

Primary pack Standard first; then other Official texts that appear as chips on chapter pages (scan of box drafts 2026-10-07).

| Full name | Short form (cite chip) |
|-----------|------------------------|
| IAS 16 Property, Plant and Equipment *(studied via HKAS 16 on box inputs; site label IAS 16 only)* | `IAS 16` |
| IAS 1 Presentation of Financial Statements | `IAS 1` |
| IAS 2 Inventories | `IAS 2` |
| IAS 7 Statement of Cash Flows | `IAS 7` |
| IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors | `IAS 8` |
| IAS 20 Accounting for Government Grants and Disclosure of Government Assistance | `IAS 20` |
| IAS 23 Borrowing Costs | `IAS 23` |
| IAS 36 Impairment of Assets | `IAS 36` |
| IAS 37 Provisions, Contingent Liabilities and Contingent Assets | `IAS 37` |
| IAS 38 Intangible Assets | `IAS 38` |
| IAS 40 Investment Property | `IAS 40` |
| IAS 41 Agriculture | `IAS 41` |
| IFRS 5 Non-current Assets Held for Sale and Discontinued Operations | `IFRS 5` |
| IFRS 9 Financial Instruments | `IFRS 9` |
| IFRS 13 Fair Value Measurement | `IFRS 13` |
| IFRS 15 Revenue from Contracts with Customers | `IFRS 15` |
| IFRS 16 Leases | `IFRS 16` |
| IFRIC 1 Changes in Existing Decommissioning, Restoration and Similar Liabilities | `IFRIC 1` |

**Deliberately omitted (not chip-evidenced as own Official source):** IFRIC Update / IU 05-14 (taught inside DTT/PwC/EY/KPMG Illus prose in Ch7 — cite remains firm + IAS 23 / IAS 16 chips, not a separate Official row). Issuer FS practical-example entities (e.g. EY Practical image plates) — not separate sources.

---

## 4. Big 4 firm manuals — proposed rows (work-title prefixes on chips)

| Full name | Short form (cite chip) |
|-----------|------------------------|
| PwC Manual of Accounting 2020 — Chapter 22 Property, plant and equipment | `PwC MOA 2020 Ch22` |
| Deloitte (DTT) iGAAP / Manual of Accounting — A7 Property, plant and equipment (2022) | `DTT iGAAP 2022 A7` |
| EY International GAAP 2026 — Chapter 19 Property, plant and equipment | `EY iGAAP 2026 Ch19` |
| KPMG Insights into IFRS 2019/20 — Part 1 · 3.2 Property, plant and equipment | `KPMG Insights 2019/20 · 3.2` |

Locators (FAQ / Example / section) stay on chapter pages after the `·`.

**Not listed:** KPMG Guides to financial statements (off-disk for this pack); EY Practical FS image plates as standalone works; any IAS 38 / IAS 40 firm manuals (out of IAS 16 pack scope).

---

## 5. How derived (method note for HTML)

1. **Cite chips only** — short forms match work-title prefix on `.cite` chips in `abbreviations.html` + `ch01.html`–`ch07.html` (before the `·` locator).  
2. **Full names** from `SOURCE-STOCKTAKE-2026-10-07.md` + chapter CONTENT-NOTES pre-flights.  
3. **No invent** — no source without an evidenced chip.  
4. Re-scan chips immediately before HTML draft in case Johnny/Grok edits moved cites.

---

## 6. Chrome / handoff (after Johnny accepts outline)

- HTML draft by IAS 16 Content (or Cursor Grok per PM) → Johnny accept → draft PR (PM hands chrome).  
- Use `data-ias16-pill-bar` (not `data-ias2`).  
- Pill already includes `{ href: "references.html", label: "References" }` in `ias16-pills.js`.  
- **42a Map** remains PARKED until separate unlock.

---

## 7. Open for Johnny (accept / adjust)

1. Accept Official + Big4 tables above as-is?  
2. Add IU 05-14 as its own Official row (currently prose-only inside firm Illus)? **Recommend: no.**  
3. Any house short-form rename before HTML? (Current chips already locked across ch01–ch07.)

**Default recommendation:** Accept as drafted → unlock References HTML first wave (no densify) → PM → Cursor Grok draft PR.
