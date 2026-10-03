# IAS 2 — Two-way XREF summary

**Date:** 2026-10-01 (Asia/Shanghai, UTC+8)  
**Refresh:** EY Official→Ch23 map densify — 43 genuine XREF rows densified; 38 new cite-only chips added; residual maps kept honest; cite QA green

## Deliverables

1. `IAS2-XREF-OFFICIAL-TO-BIG4-2026-10-01.md` — Crosswalk A
2. `IAS2-XREF-BIG4-TO-OFFICIAL-2026-10-01.md` — Crosswalk B
3. this summary
4. `IAS2-EY-FS-UNLOCK-2026-10-01.md` — EY FS ×4 unlock
5. `IAS2-COMPLETENESS-RESWEEP-2026-10-01.md` — claim gate re-sweep

Locations: `refs/ias-2/draft-v1-linked/` **and** `/workspace/ias2-content-extract/`.

## Counts

| Direction | Rows / population | Site-chip / on-site | GAPs |
|-----------|-------------------|---------------------|------|
| A Official→Big4 | 70 material Official rows (+ 4 IE-equivalent rows) | **70** with Official cite chip; **43** EY Ch23 rows co-cited; **38** new chips | **0** site-chip GAPs; 2 EY maps honestly retained |
| B Big4→Official | DTT 27; PwC 25; EY **11**; KPMG Ex 23 + 25 sections | All named plates on site | **0** design GAPs |
| HTML | **80** Illus · **~526** cite chips | densify HARD **0** FAIL | — |

## GAP list (combined short)

- ~~B: EY Practical example 3-1 / 3-2 / 6-1 / 6-2~~ — **CLOSED**
- ~~A: BC4–BC5 / BC21 / BC22–BC23~~ — **CLOSED**
- ~~B: DTT 2.1-4 / 2.1-5; KPMG 3.8.215~~ — **CLOSED**
- ~~Densify thin: storage / dtt-xfer / kpmg-retail / kpmg-fifo-wa~~ — **CLOSED** 2026-10-01 re-sweep
- ~~Optional EY Official→Ch23 map densify~~ — **CLOSED for 43 genuine rows**; 2 honest maps retained (IN10 FX; BC22–BC23 Board history)

## Completeness claim status

**Crosswalk-complete: YES** (named-plate inventory; Official cite chips). EY FS ×4 on site (personal-study unlock + `#pack-disclaimer`).  
**EY map densify:** 43 genuine Ch23 locator rows are now co-cited; 38 new chips were needed because shared teaching units were deduplicated; 2 `_(map)_` rows remain parked honestly where Ch23 does not provide a matching locator.  
**Laptop Documents sync:** pending while LAPTOP-MODGPP0C is offline.

## QA gate I

- [x] Both inventory files exist (pack + `ias2-content-extract/`)
- [x] Locator-level rows (Official para / firm FAQ / Ex / section ids)
- [x] GAP-honest (design GAPs closed; Map parked called out)
- [x] Pack completeness claim — **assertable** for crosswalk / named plates (`IAS2-COMPLETENESS-RESWEEP-2026-10-01.md`)
- [x] EY cite QA — 38 new `cite-ey` chips use `EY iGAAP 2026 Ch23 · section …` with no `§`; no duplicate prose/illustration rewrites
