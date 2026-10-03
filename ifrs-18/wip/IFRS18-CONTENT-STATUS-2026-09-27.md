# IFRS 18 — Content STATUS

**Date:** 2026-09-27 ~22:45 (Asia/Shanghai)  
**Pack:** IFRS 18 Presentation and Disclosure  
**Agent:** Content — canon **2026.09.27-7** remap sync (MD twins · Design brief · teaching structure · stale HTML strings · LOCK-STAMP)  
**Locks:** VISUAL-TYPES / PRODUCT-SPEC / QC-CHECKLIST **2026.09.27-7** — page stamps **stale** pending QC (see LOCK-STAMP)

---

## 1. Remap sync note (2026.09.27-7)

- **Build** remapped draft HTML filenames/ids/sticky to **Map + ch01…ch08** (`#s-1-*`…`#s-8-*`).
- **Content** synced MD twins + Design brief + teaching structure + STATUS; fixed leftover student-facing old Ch-number strings in draft HTML (cross-refs only — no visual redraw).
- Sticky live: **Map · 1 What’s new · 2 PFS & aggregation · 3 P&L categories · 4 Totals & subtotals · 5 Operating expenses · 6 MPMs · 7 Other FS impacts · 8 Transition**.

### Files created / updated this sync

#### Subpages (`subpages/`)
| File | Status |
|------|--------|
| `INDEX.md` | **Rewritten** — Map + Ch1–8 |
| `01-whats-new-vs-ias1.md` | **Created** (was `02-…`) |
| `02-pfs-roles-aggregation.md` | **Created** (was `03-…`) |
| `03-pnl-categories.md` | **Created** (was `04-…`) |
| `04-totals-subtotals.md` | **Created** (was `05-…`) |
| `05-operating-expenses.md` | **Created** (was `06-…`) |
| `06-mpms.md` | **Created** (was `07-…`) |
| `07-other-fs-impacts.md` | **Created** (was `08-…`) |
| `08-transition.md` | **Created** (was `09-…`) |
| `02-….md` … `09-….md` (old numbers) | **Deleted** |

#### HTML (`draft-v1-linked/`) — Content touch (strings only)
| File | Status |
|------|--------|
| `ch01.html`, `ch03.html`, `ch04.html`, `ch06.html`, `ch07.html` | Stale cross-ref Ch numbers fixed to NEW |
| `visuals/ch06-mpms.html` | Stale “Ch5 matrix” → “Ch4 matrix” |
| `index.html` sticky/pillars | Already NEW (Build) — left as-is |
| Visual stub drawings | **Not redrawn** |

#### WIP / stamp
| File | Status |
|------|--------|
| `wip/IFRS18-CONTENT-DESIGN-BRIEF-2026-09-27.md` | **Updated** — TYPE map Ch1–8 · P0 Map/Ch2/Ch3/Ch4·Ch6 · stubs renamed |
| `wip/IFRS18-TEACHING-STRUCTURE-2026-09-27.md` | **Updated throughout** to Map·1…8 |
| `wip/IFRS18-CONTENT-STATUS-2026-09-27.md` | This file |
| `LOCK-STAMP.md` | Remapped page rows · Versions **2026.09.27-7** · status **stale** · pending QC |

### Not touched (by design)
- Homepage READY flag (PM owns)
- CF pack files
- Official / Big 4 PDFs
- Design drawings / visual layout (stubs remain stubs)

**Preview symlink:** `_review/ifrs-18/preview` → `refs/ifrs-18/draft-v1-linked` (edits apply).

---

## 2. Open assumptions (NEW numbers)

1. **Ch2 early — YES** (official + EY), not KPMG-late aggregation order.
2. **Banks/insurers — Map-only** dashed see-also in v1 (no competing Ch3 dashed chip).
3. **Colour — five category tokens** (`--cat-operating` … `--cat-discontinued`) **+** `--ifrs-subtotal` / `--mpm` contrast (do not collapse tax+discontinued).
4. Sticky tag short labels (`1 What’s new`, `2 PFS & aggregation`, …) — full titles in page H1.
5. Site labels **IFRS 18** only (official source text is HKFRS 18 — paraphrased; no dual UI code).
6. Ch7 stays thin consequential; no full IAS 7/33/34 courses.
7. Visual stubs are TYPE picks only — Design owns finished drawings.

---

## 3. Design unlock readiness (NEW chapter numbers)

| Page | Substantive body for Design? | Notes |
|------|------------------------------|-------|
| **Map** | **YES** | Pillars wired to Ch3–4 / Ch2 / Ch6; 1 Jan 2027 → Ch8; banks dashed see-also; all tags live |
| **Ch3** | **YES** | Five categories · operating default · investing/financing · main-business overview · traps |
| **Ch4** | **YES** | §69 anchors · §73 trap · required/§118/MPM matrix · token grammar |
| **Ch6** | **YES** | §117 gate · §118 exclusions · single note · reconciliation waterfall cues |
| Ch2 | Ready for P0 roles plate | Dual-role + aggregation checklist in body |
| Ch1 / Ch5 / Ch7 / Ch8 | Draft complete | P1/P2 visuals per Design brief |

**Confirmation:** Map + Ch3 + Ch4 + Ch6 bodies are substantive enough for Design unlock (P0). Prior QC under -6 on old Ch3/4/5/7 is **stale** under -7 — re-QC required.

---

## 4. PDF / extraction notes (non-blockers)

| Source | Use | Gap? |
|--------|-----|------|
| `official-hkfrs18-2026-06.pdf` | Primary § spine via `pdftotext` | None material — App B AG taught selectively (not full dump) |
| KPMG First Impressions | Visual/flow cross-check per structure | Not line-extracted this pass; structure brief already mapped FI → teaching order |
| EY closer look (MOA 2026) | Depth/FAQ nuance | Same — structure + known traps used; no long FAQ paste |
| Deloitte IAS 1 A4 | Bridge only | Intentionally not structural |

No PDF blocker stopped the draft. Deeper App B bank/insurer AG remains **out of v1** by brief.

---

## 5. Paths for parent

- Design brief: `refs/ifrs-18/wip/IFRS18-CONTENT-DESIGN-BRIEF-2026-09-27.md`
- This STATUS: `refs/ifrs-18/wip/IFRS18-CONTENT-STATUS-2026-09-27.md`
- Teaching structure: `refs/ifrs-18/wip/IFRS18-TEACHING-STRUCTURE-2026-09-27.md`
- LOCK-STAMP: `refs/ifrs-18/LOCK-STAMP.md`
- Openable Map: `refs/ifrs-18/draft-v1-linked/index.html`
