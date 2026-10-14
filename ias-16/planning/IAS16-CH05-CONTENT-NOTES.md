# IAS 16 Ch5 Depreciation — Content NOTES (42g)

**Date:** 2026-10-07 (Asia/Shanghai, UTC+8)  
**Pack path:** `ias-16/draft-v1-linked/ch05.html` (box: `/workspace/ias16/draft-v1-linked/ch05.html`)  
**Status:** First HTML wave · Map parked · No PR  
**Cite house:** Official `IAS 16 · para …` · `PwC MOA 2020 Ch22 · …` · `DTT iGAAP 2022 A7 · …` · `EY iGAAP 2026 Ch19 · section …` · `KPMG Insights 2019/20 · 3.2 · …` · **no §**

---

## 1. Source inventory (Ch5 Depreciation / components)

| Source | Path on box | Depreciation / component locators scanned | Named examples / plates |
|--------|-------------|------------------------------|-------------------------------------|
| Official (via HKAS 16) | `/workspace/ias16/HKAS-16-PPE.pdf` · `hkas16-extract.txt` | **para 6** defs (dep / depreciable amount / residual / useful life) · **43–47** significant parts · **48–49** charge location · **50–54** depreciable amount / residual · **55** begin/cease · **56–59** UL factors / land·buildings · **60–62** methods · **62A** revenue-based ban · BC26–BC33E | No Official numeric IE for dep — firm Illus supply numbers |
| PwC MOA 2020 Ch22 | `/workspace/ias16/pwc-ch22-ias16.pdf` | **22.14** componentisation · FAQ **22.14.2** (deferred from Ch2) · **22.79–22.102** Depreciation cluster · FAQ **22.80.1 / 22.83.2 / 22.84.1–2 / 22.87.1 / 22.89.1–2 / 22.100.1–2 / 22.101.1** | FAQ 22.14.2 → Illus 5.2.1; 22.83.2 → 5.0.1; 22.80.1+22.87.1 → 5.3.1; 22.89.1 → 5.4.1; 22.84.2 → 5.7.1; 22.100.1 → 5.8.1; 22.101.1 → 5.8.3 |
| EY iGAAP 2026 Ch19 | `/workspace/ias16/ey-ch19-ppe.pdf` | **section 5** Cost model and depreciation · **5.2** components · **Illus 3-2** parts · **5.2.1** in-place leases · **5.3** residual · **5.4** UL · **5.5** start · **5.6** methods · **Illus 5-3 / 5-4 / 5-5** · Practical **5-1–5-5** FS plates | Illus 3-2 → 5.2.2; 5-3 → 5.5.1; 5-4 → 5.5.2; 5-5 → point-chip; Practical 5-1–5-5 → gap (image body) |
| DTT iGAAP 2022 A7 | `/workspace/ias16/dtt-a7-ppe.pdf` | **§7** Depreciation · **7.2 / 7.2-1…3** components · **7.3** residual · **7.4** UL · **7.4.3-1** mothball · **7.4.5-1** UL change · **7.5** methods · **7.5.3-1** increasing charge · **7.5.4** revenue · **7.5.5-1** method change · **7.6** classes | 7.2-2 → 5.2.3; 7.4.3-1 → 5.4.2; 7.4.5-1 → 5.8.1; 7.5.5-1 → 5.8.2; 7.5.3-1 / 7.6.2-1 / 7.6.5–7 teaching |
| KPMG Insights 2019/20 · 3.2 | `/workspace/ias16/kpmg-3.2-ppe-extract.txt` | **3.2.140** Depreciation · Ex **9** UL · **3.2.150** residual Ex **10A/10B/11** · **3.2.160–190** methods Ex **12A–12C** (tables blank) · **3.2.210** revenue ban · **3.2.220** begin · **3.2.230–280** Component · Ex **14A/14B** · **15A** (Ch2) · **15B–15D** (pulled here) | 9 → 5.8.1; 10A/10B → 5.1.1; 11 → 5.1.2; 14A → 5.2.4; 14B → 5.2.5; 15B→5.2.6; 15C→5.2.7; 15D→5.2.8; 12A–C tables blank → EY numbers used |

**Pre-flight:** All four Big4 + Official on disk and scanned for Depreciation / Component accounting.  
**Site labels:** IAS 16 / IFRS only (HKAS is Official study proxy).  
**Johnny HARD:** Models not re-dumped (Ch4 pointer only); component accounting is home here; KPMG 15B–15D + PwC FAQ 22.14.2 pulled from Ch2 NOTES gaps.

---

## 2. Chapter outline (as drafted)

| id | Section | Teaching claim |
|----|---------|----------------|
| `s-5-0` | 5.0 What depreciation is | Para 6/50 def; allocation not valuation; both models; hotel-equip Illus |
| `s-5-1` | 5.1 Depreciable amount | Formula plate; residual current; review; zero when residual ≥ CA; two Illus |
| `s-5-2` | 5.2 Significant parts / component accounting | FULL home para 43–47; eight Illus incl. 15B–15D + FAQ 22.14.2 |
| `s-5-3` | 5.3 Useful life; land/buildings | Para 56–59; landfill Illus |
| `s-5-4` | 5.4 Begin and cease | Para 55; idle ≠ stop; IFRS 5 / Derecognition tips; ready + mothball Illus |
| `s-5-5` | 5.5 Methods | SL / diminishing / units; EY Illus 5-3/5-4 + 5-5 chip |
| `s-5-6` | 5.6 Revenue-based restriction | Para 62A hard ban; contrast-pair |
| `s-5-7` | 5.7 Charge location | Para 48–49; absorb Illus |
| `s-5-8` | 5.8 Change in estimate | Para 51/61 prospective; three Illus |
| `s-5-9` | 5.9 ROU tip | IFRS 16 see-also |
| `s-5-10` | 5.10 Bridge | Ch2 replacements/inspections; Ch4 models; Ch6 forward |
| `s-5-11` | 5.11 Checklist | Depreciation scan table |

**Chrome:** Match `ch04.html` (header, disclaimer bottom, footer-nav, CSS query strings, `data-ias2-pill-bar` + `ias16-pills.js`). **No Concept Map iframe.** `h1` id `chapter-title`; `a.sec-top` href `#chapter-title`. Local `draft.css` carries `.peer-row` + `.cost-sum` formula plate.

---

## 3. Illustrations (all worked-strip, neutral peers)

| id | Title | Source | Peers |
|----|-------|--------|-------|
| `s-5-ex-hotel-equip` | 5.0.1 Rolling hotel-equipment replacements ≠ depreciation | PwC FAQ 22.83.2 | Facts / Assessment / Conclusion |
| `s-5-ex-residual-market` | 5.1.1 Residual — second-hand vs scrap | KPMG Ex 10A + 10B | Facts / Assessment / Conclusion |
| `s-5-ex-residual-change` | 5.1.2 Change in residual — ship scrap steel | KPMG Ex 11 | Facts / Assessment / Conclusion |
| `s-5-ex-factory-roof` | 5.2.1 Factory roof component depreciation | PwC FAQ 22.14.2 | Facts / Assessment / Conclusion |
| `s-5-ex-ey-parts` | 5.2.2 Roof + partitioning components | EY Illus 3-2 | Facts / Assessment / Conclusion |
| `s-5-ex-dtt-drydock` | 5.2.3 Ship dry-dock overhaul component | DTT A7 · 7.2-2 | Facts / Assessment / Conclusion |
| `s-5-ex-kpmg-14a` | 5.2.4 Combining insignificant components | KPMG Ex 14A | Facts / Assessment / Conclusion |
| `s-5-ex-kpmg-14b` | 5.2.5 Stadium seating physical component | KPMG Ex 14B | Facts / Assessment / Conclusion |
| `s-5-ex-kpmg-15b` | 5.2.6 Overhaul internal vs external costs | KPMG Ex 15B | Facts / Assessment / Conclusion |
| `s-5-ex-kpmg-15c` | 5.2.7 Overhaul across physical components | KPMG Ex 15C | Facts / Assessment / Conclusion |
| `s-5-ex-kpmg-15d` | 5.2.8 Early dry-dock write-off via depreciation | KPMG Ex 15D | Facts / Assessment / Conclusion |
| `s-5-ex-landfill` | 5.3.1 Landfill land + restoration depreciated | PwC FAQ 22.80.1 + 22.87.1 | Facts / Assessment / Conclusion |
| `s-5-ex-ready` | 5.4.1 Begin when ready for use | PwC FAQ 22.89.1 | Facts / Assessment / Conclusion |
| `s-5-ex-mothball` | 5.4.2 Mothballed machinery — dep continues | DTT A7 · 7.4.3-1 | Facts / Assessment / Conclusion |
| `s-5-ex-sl` | 5.5.1 Straight-line | EY Illus 5-3 | Facts / Measure / Conclusion |
| `s-5-ex-db` | 5.5.2 Diminishing balance | EY Illus 5-4 | Facts / Measure / Conclusion |
| `s-5-ex-absorb` | 5.7.1 Factory dep absorbed into tools | PwC FAQ 22.84.2 | Facts / Assessment / Conclusion |
| `s-5-ex-ul-change` | 5.8.1 Change in useful life | KPMG Ex 9 + DTT 7.4.5-1 + PwC FAQ 22.100.1 | Facts / Assessment / Conclusion |
| `s-5-ex-method-change` | 5.8.2 Reducing-balance → straight-line | DTT A7 · 7.5.5-1 | Facts / Assessment / Conclusion |
| `s-5-ex-residual-zero` | 5.8.3 Revising residual / zero charge | PwC FAQ 22.101.1 | Facts / Assessment / Conclusion |

**Not Illus (teaching / see-also / other chapter):** EY Practical FS 5-1–5-5 (Skanska / easyJet / ArcelorMittal / Mærsk / National Grid) — extract body image/thin; EY Illus 5-1 in-place leases (IFRS 16/IAS 40 adjacent — point-chip); EY Illus 5-2 leasehold improvements (IFRS 16 tip); EY Illus 5-5 sum-of-digits → point-chip densify; KPMG Ex 12A–12C method tables blank in extract (EY 5-3/5-4 numbers used); KPMG Ex 15A already in Ch2; DTT 7.5.3-1 increasing-charge reject teaching; DTT 7.6.2-1 historic buildings teaching; PwC FAQ 22.84.1 / 22.89.2 / 22.100.2 densified into teaching or adjacent Illus; Models re-dump forbidden.

---

## 4. Crosswalk A — Official → Big4 (Depreciation)

| Official | PwC | DTT | EY | KPMG |
|----------|-----|-----|----|------|
| para 6 defs | 22.82 · 22.91 | 7.1 · 7.3 · 7.4.1 | 5.1 · 5.3 · 5.4 | 3.2.140 · 3.2.150 |
| para 43–47 components | 22.14 · 22.85 · FAQ 22.14.2 | **7.2 · 7.2-1…3** | **5.2 · Illus 3-2** | **3.2.230–280 · Ex 14A/B · 15B–D** |
| para 48–49 charge location | 22.84 · FAQ 22.84.x | 7.1 | 5.1 | 3.2.140.50 |
| para 50–54 depreciable / residual | 22.91–22.92 · FAQ 22.101.1 | 7.3 | 5.3 | 3.2.150 · Ex 10A/B · 11 |
| para 55 begin/cease | 22.90 · FAQ 22.89.1 | 7.4.2–7.4.3 · 7.4.3-1 | 5.5 | 3.2.220 |
| para 56–57 UL factors | 22.98 | 7.4.4 | 5.4 | (via 3.2.140 / 160) |
| para 58–59 land/buildings | 22.87 · FAQ 22.80.1/22.87.1 | 7.6.1–7.6.2 | 5.4.2 | 3.2.140.10 tip |
| para 60–62 methods | 22.93–22.96 | 7.5 · 7.5.5-1 | **5.6 · Illus 5-3–5-5** | 3.2.160–190 · Ex 12A–C |
| para 62A revenue ban | 22.98 | **7.5.4** | 5.6 | 3.2.210 |
| para 51 / 61 estimate change | 22.100–22.102 · FAQ 22.100.1 | 7.4.5 · 7.5.5 | 5.6 | 3.2.140.20 · Ex 9 |

---

## 5. Crosswalk B — Big4 → Official (Depreciation plates)

| Firm plate | → Official |
|------------|------------|
| PwC FAQ 22.14.2 factory roof | para 43 |
| PwC FAQ 22.83.2 hotel equipment | para 52 |
| PwC FAQ 22.80.1 / 22.87.1 landfill | para 58–59 |
| PwC FAQ 22.89.1 ready for use | para 55 |
| PwC FAQ 22.84.2 absorb into tools | para 49 |
| PwC FAQ 22.100.1 UL change | para 51 |
| PwC FAQ 22.101.1 residual revise | para 51 · 54 |
| DTT 7.2-2 ship dry-dock | para 44 · 14 |
| DTT 7.2-3 missed component | para 14 |
| DTT 7.4.3-1 mothball | para 55 · 57 |
| DTT 7.4.5-1 UL change | para 51 |
| DTT 7.5.5-1 method change | para 61 |
| DTT 7.5.3-1 increasing charge | para 60 (reject) |
| EY Illus 3-2 roof/partition | para 43–44 |
| EY Illus 5-3 / 5-4 / 5-5 methods | para 62 |
| EY section 5.2.1 in-place leases | para 44 |
| KPMG Ex 9 UL change | para 51 |
| KPMG Ex 10A / 10B residual | para 6 · 53 |
| KPMG Ex 11 residual change | para 51 · 54 |
| KPMG Ex 14A / 14B components | para 43 · 46 |
| KPMG Ex 15B / 15C / 15D overhaul | para 14 · 13 |
| KPMG Ex 12A–12C methods | para 62 — **tables blank; EY numbers used** |
| EY Practical 5-1–5-5 FS | — **orphan / body unavailable** |

---

## 6. Gaps / open questions

1. **EY Practical examples 5-1–5-5** (Skanska component policy, easyJet residual, ArcelorMittal units, Mærsk climate UL, National Grid UL change) — pdftotext body empty (image/scan plates). Not paraphrased without body.  
2. **KPMG Examples 12A–12C** method journal tables blank in text extract — SL/diminishing numbers taken from EY Illus 5-3 / 5-4; units-of-production taught as method prose only.  
3. **EY Illustration 5-1** in-place lease components and **5-2** leasehold-improvement period — IFRS 16 / IAS 40 adjacent; point-chip / tip only, not full Illus.  
4. **PwC FAQ 22.89.2** held-for-sale then recommission — densified into 5.4 teaching (IFRS 5 cease + reverse impairment path); not a separate Illus.  
5. **Map HTML** still parked — no iframe / no chapter-top map.  
6. **Models** deliberately not re-dumped (Johnny HARD).  
7. **Pill bar** still uses `data-ias2-pill-bar` + `assets/ias16-pills.js`.

---

## 7. QA self-run (2026-10-07)

| Check | Result |
|-------|--------|
| Ends with `</html>` | PASS |
| Chrome matches ch04 | PASS |
| Zero `§` inside `.cite` / file | PASS |
| Zero house-only Big4 chips | PASS |
| All Illus = `.worked-strip` | PASS (20) |
| Illus peers neutral | PASS |
| Densify gate (all Illus >5 bullets / >350 chars) | PASS |
| No Concept Map iframe | PASS |
| No invent entity CU / fake company | PASS (sourced plates only) |
| `a.sec-top` href `#chapter-title` | PASS |
| Formula plate `.cost-sum` | PASS |
| Models re-dump absent | PASS |
| KPMG 15B–15D + PwC FAQ 22.14.2 present | PASS |
| Revenue-based 62A taught clearly | PASS |
| Internal `#frag` resolve | PASS |
| Map lecture note absent | PASS |

---

## 8. #60 Wave A impairment mechanical densify (2026-10-10)

**CLOSED 2026-10-10 · #60 Wave A (body)** — HTML on Draft PR #94 head `ae56513` (rebase-ready local `1d50036` on main@`f11c02d`).

| ID | Placement | Delivered |
|----|-----------|-----------|
| I2 | `h4#s-5-1-post-impair` after residual bullets, before Illus 5.1.1 | Impaired CA − residual over remaining UL; estimate path → 5.8; measurement → `ch04#s-4-8` |
| I4 | Cross-link only inside I2 | One bullet → existing residual≥CA teaching + Illus `s-5-ex-residual-zero` (5.8.3); no new worked-strip / multi-bullet re-teach |
| Cross-link | `s-5-8` indicator bullet | One sentence → `#s-5-1-post-impair` |
| Checklist | `s-5-11` | After cost-model impairment → impaired CA − residual over remaining UL |
| I5 | Pack-wide | No invented CU Illus; IAS 36 measurement stays see-also |

Cite house: `IAS 16 · para 6/30/50/51/54/63` · `IAS 8 · para 36` · `DTT · 7.4.5` · `KPMG · 3.2.140.35`. Zero `§` in `.cite`. Wave B map tip parked.
