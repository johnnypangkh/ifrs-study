# CF 2018 — IAS 2 parity wave (2026-10-01 Asia/Shanghai)

**Owner:** Content implement (Grok executor)  
**Reviewer:** Johnny Pang  
**Pack:** `refs/cf-2018/draft-v1-linked/`  
**Skills:** ifrs-teaching-body · ifrs-teaching-body-qa · ifrs-visual-grammar  
**Prior note corrected:** `CF-FULL-PASS-2026-10-01.md` wrongly marked EY/KPMG **not on disk** — **FIXED** this wave.

## Pack path

`/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/` — now **ch01–ch11** + `index.html` Map  
Backup: `/workspace/cf2018-ias2-parity-20261001-194755+0800/`

## Big4 pre-flight (HARD — corrected)

| Layer | Firm / source | Path | Status |
|-------|---------------|------|--------|
| 1 | Official CF 2018 (2026 stamp) | `inputs/cf-2018/official-conceptual-framework-2026.pdf` (+ HTML/HK) | Scanned |
| 2 | DTT A2 2022 | `inputs/cf-2018/dtt-2022-conceptual-framework-moa.pdf` | Scanned |
| 2 | PwC MOA 2020 intro | `inputs/pwc-2020-moa/01-conceptual-framework-intro.pdf` | Scanned |
| 2 | PwC MOA 2020 Appendix 2 Combined/Carve | `inputs/pwc-2020-moa/appendix-2-combined-carve-out.pdf` | Scanned |
| 2 | **EY IGAAP 2026 Ch2** | `inputs/ey-international-gaap-2026/International-GAAP-2026-part1.pdf` (~pp 46–103) | **Scanned** (was wrongly “missing”) |
| 2 | **KPMG Insights 2019/20 · 1.2** (=2018 CF) | `inputs/kpmg-2019-2020/part1-non-fi.pdf` | **Scanned** (was wrongly “missing”) |
| 3 | KPMG Combined/Carve Feb 2022 | `inputs/cf-2018/kpmg-public/kpmg-combined-and-carve-out-financial-statements.pdf` | Scanned → Ch9/Ch10 |
| 3 | KPMG flyer Apr 2018 | `inputs/cf-2018/kpmg-public/kpmg-2018-04-conceptual-framework-print-friendly.pdf` | Background |
| 3 | EY IFRS Dev 169 | `inputs/cf-2018/ey-public/ey-devel169-ifrs-3-conceptual-frwk-may-2020.pdf` | Ch5 see-also |
| — | ACCA SBR storyline | `inputs/cf-2018/acca/ACCA-SBR-CF-storyline-NOTE.md` | **Visit path only — no cite** |

**Inventories:** `CF-EY-CH2-INVENTORY-2026-10-01.md`, `CF-KPMG-1.2-INVENTORY-2026-10-01.md`  
**Crosswalks:** `CF-XREF-OFFICIAL-TO-BIG4-2026-10-01.md` (A), `CF-XREF-BIG4-TO-OFFICIAL-2026-10-01.md` (B) — **started / locator-level / gap-honest**; not yet pack-complete claim.

## What changed

### 1. Pre-flight FIX
METHOD + inventories + Crosswalk A/B record EY Ch2 + KPMG 1.2 on disk. Prior “No EY/KPMG invent because missing” lines removed.

### 2. Chapter renumber / new apps
| Was | Now |
|-----|-----|
| Ch9 Status | **Ch11 Status** (`ch11.html`; anchors `s-11-*`; visual `ch11-status.html`) |
| — | **Ch9 Combined FS** (`ch09.html`) — CF 3.10–3.14 + KPMG Combined/Carve 2022 + PwC A2 |
| — | **Ch10 Carve-out** (`ch10.html`) — portion-of-entity app |

Chrome tags + footers updated pack-wide (Map · 1…8 · 9 Combined · 10 Carve-out · 11 Status).

### 3. Enrich Ch1–8 (+ Ch11) from EY + KPMG
- Multi-firm write-once chips: `EY IGAAP 2026 · Ch2 · section …`, `KPMG Insights 2019/20 · 1.2…` alongside DTT/PwC/Official.
- **New Illus (worked-strip, neutral peers):**
  - 3.5.2 KPMG Ex1 GC liquidation / IFRS 9 liability
  - 4.6.1 KPMG Ex2 executory contract
  - 6.7.1 KPMG Ex3 shareholder inventory (FV / free / above FV)
  - 9.5.1 KPMG Ex 1B Combined three LLCs
  - 9.5.2 KPMG Ex 1D Combined and carve-out clothing IPO
  - 10.2.1 KPMG Ex 1C Carve-out cable division
- Ch3 boundary bullets link to Ch9/Ch10.
- Ch5 see-also EY Dev 169 (IFRS 3 ↔ CF).

### 4. Map enhance
- Pack Map: Status chip → **11**; dashed Combined (9) ∥ Carve-out (10) under Reporting entity boundary.
- Story + **ACCA visit path** documented in HTML comment (ACCA = narrative only).
- Cache-bust `map.css?v=cf-parity-20261001`.
- Minimal chapter-top visuals for Ch9/Ch10 (`visuals/ch09-combined.html`, `ch10-carve.html`).

### 5. Decision strips
Left `.ok` / `.warn` on **main-body decision strips** (Johnny deferred). **No** new ok/warn on Illus peers (neutral).

## QA table (ifrs-teaching-body-qa)

| Gate | Result |
|------|--------|
| A Cite — house-only / `§` / Official=`CF 2018 · para…` | **PASS** |
| A Big4 firm+work+locator (EY/KPMG forms) | **PASS** |
| B Illus = worked-strip-grid | **PASS** (all Illus titles inside strips) |
| B Illus peers neutral | **PASS** (ok/warn only on Decision strips — deferred) |
| C `p.box-body>ul` | **PASS** |
| D Densify quantitative (Illus) | **PASS** — see list below |
| E Title essence | **PASS** (fixed bare PwC./KPMG. leads on Ch10) |
| E2 Technical-strict titles | **PASS** |
| E3 Visual-when-complex | **Partial** — peer grids dense; Ch9/10 Maps are thin jump boards (debt if Johnny wants Opus redraw) |
| F Hyperlink | Ch3↔Ch9/Ch10 links added; Status Map links → Ch11; no Illus id renumber of prior plates |
| I Big4 pre-flight | **PASS** — all four firms + Official paths; EY/KPMG fixed |
| I Crosswalk A+B | **Partial** — both files non-empty locator-level; BC full sweep + KPMG Combined Ex 2–4 plate wrap still **debt** → **no pack-complete claim** |
| Map | Pack Map + ACCA visit path + Ch9/10 cells; Illus peers still neutral |

### Illus densify snapshot
- `ch03.html` · 3.5.1 — Going concern assumption · li=10 chars=1452 → **PASS**
- `ch03.html` · 3.5.2 — Going concern broken — IFRS 9 liability still r · li=16 chars=3265 → **PASS**
- `ch04.html` · 4.4.1 — Claim that fails liability → equity · li=14 chars=3467 → **PASS**
- `ch04.html` · 4.5.1 — Owner cash contribution vs inventory sale · li=18 chars=5876 → **PASS**
- `ch04.html` · 4.6.1 — Executory contract to buy equipment · li=8 chars=917 → **PASS**
- `ch05.html` · 5.5.1 — Not recognising an acquired resource distorts p · li=15 chars=5522 → **PASS**
- `ch06.html` · 6.6.1 — Day-2 P&amp;L from basis flip / deemed cost · li=19 chars=4983 → **PASS**
- `ch06.html` · 6.7.1 — Inventory sold to a shareholder (FV / free / ab · li=10 chars=1057 → **PASS**
- `ch08.html` · 8.4.1 — Three-way landing of the same CU15 · li=20 chars=3856 → **PASS**
- `ch09.html` · 9.5.1 — Combined financial statements (three LLCs under · li=10 chars=1299 → **PASS**
- `ch09.html` · 9.5.2 — Combined and carve-out (clothing IPO across sub · li=18 chars=2536 → **PASS**
- `ch10.html` · 10.2.1 — Carve-out of a cable division from one legal e · li=14 chars=2097 → **PASS**

## Open gaps / debt (honest)

1. **Crosswalk A/B** — started; full BC paragraph inventory + every KPMG Combined/Carve Ex 2A–4H wrap still open before pack-complete.
2. **EY Ch2 measurement tables / Figure 5-1** — section cites present; full matrix plates not yet mirrored as Ch2/Ch6 section tables (debt densify).
3. **Ch9/Ch10 Map visuals** — functional stubs; not Johnny-signed Opus redraws.
4. **Decision-strip `.ok` peers** — left per Johnny deferral.
5. **Body prose `§`** — chips clean; running text may still say “Teaching §§” in places.
6. **PwC A2 full step 1–5 narrative** — spine cited; not every A2.nn FAQ body wrapped.
7. **ACCA** — visit path only; never cite authority.

## Sync status

Laptop `LAPTOP-MODGPP0C` (`2a06a250-…`) **connected: true**. **Documents sync: OK** (~20:15 Asia/Shanghai) — report, Crosswalk A/B, METHOD, index, ch01–ch11.html, Ch9/10/11 visuals, EY/KPMG inventories → `C:\Users\johnny\Documents\ifrs-website-refs\refs\cf-2018\…`.

## Completeness claim

**IAS 2 parity progress: YES** (EY/KPMG unlocked, Ch9/Ch10 apps live, Crosswalk started, QA A–E green on touched Illus).  
**Pack-complete / Crosswalk-complete: NO** — remaining Crosswalk debt + Combined/Carve Ex plate backlog.
