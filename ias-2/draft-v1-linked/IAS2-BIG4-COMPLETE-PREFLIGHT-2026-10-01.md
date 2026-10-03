# IAS 2 — Big4 completeness pre-flight

**Date:** 2026-10-01 (Asia/Shanghai, UTC+8)  
**For:** IFRS Website PM (Johnny Pang)  
**Trigger:** HARD process gate — never wait for Johnny to name a missing Big4; scan PwC + DTT + EY + KPMG + Official before write/enrich.  
**Pack:** `refs/ias-2/draft-v1-linked/`  
**Skills locked:** [IFRS teaching body](sand-workflow:ifrs-teaching-body) · [IFRS teaching body QA](sand-workflow:ifrs-teaching-body-qa) §I  

---

## 1. Box inputs inventory (firm manuals)

| Firm | Expected work | On disk | Path(s) | Size / notes |
|------|---------------|---------|---------|--------------|
| **Official** | HKAS 2 Inventories (= IAS 2 on site) | **YES** | `inputs/hkas/hkas-2-inventories.pdf` | 404 344 B |
| Official alias | same | **YES** | `inputs/ias-2/official-hkas-2-inventories.pdf` → hkas | symlink |
| **PwC** | MOA 2020 **Ch25** IAS 2 Inventories | **YES** | `inputs/pwc-2020-moa/chapters/25-ias2-inventories.pdf` | 278 826 B |
| PwC alias | same | **YES** | `inputs/ias-2/pwc-2020-moa-25-ias2-inventories.pdf` → chapters/25 | symlink |
| **DTT** | **A11** 2022 Inventories | **YES** | `inputs/dtt-moa-2022-june21/dtt-2022-a11.pdf` | 917 776 B |
| DTT alias | same | **YES** | `inputs/ias-2/dtt-2022-a11-inventories.pdf` → a11 | symlink |
| **EY** | International GAAP® 2026 **Ch23** Inventories | **YES** | `inputs/ey-international-gaap-2026/International-GAAP-2026-part1.pdf` (Ch23 ~book pp 1692–1723) | 86 654 918 B |
| EY part2 | remainder of book | **YES** | `…/International-GAAP-2026-part2.pdf` | 97 193 113 B |
| EY alias under `inputs/ias-2/` | — | **no symlink** | — | optional gap only |
| **KPMG** | Insights into IFRS **2019/20** Part 1 · **3.8** Inventories | **YES** | `inputs/kpmg-2019-2020/part1-non-fi.pdf` | 39 287 423 B |
| KPMG other parts | 2–4 (not IAS 2 3.8) | YES (N/A for IAS 2 body) | `part2-ifrs9.pdf` … `part4-insurance.pdf` | on disk |
| KPMG alias under `inputs/ias-2/` | — | **no symlink** | — | optional gap only |

**None of the four firms is `not on disk` for IAS 2.** Official + all Big4 manuals are available under box `inputs/`.

---

## 2. Extracts / inventory cited

| Firm | Extract / inventory on disk | Extracted? | Cited in pack HTML? |
|------|----------------------------|------------|---------------------|
| Official | `ias2-content-extract/hkas2-extract.txt` (826 lines) | **Yes** | **Yes** — `cite-official` pack-wide (~163 chips) |
| PwC Ch25 | `ias2-content-extract/pwc-ias2-extract.txt` (1234 lines) | **Yes** | **Yes** — FAQ-with-body set complete per `IAS2-BIG4-EXAMPLES-GAP-2026-10-01.md`; `cite-pwc` (~66) |
| DTT iGAAP 2022 A11 | `ias2-content-extract/dtt-a11-extract.txt` (1223 lines) | **Yes** | **Yes** — numbered examples filled (incl. priority + deferred plates); `cite-dtt` (~59) |
| EY Ch23 | `ias2-content-extract/ey-ch23-inventories-raw.txt` (1622 lines) + `EY-IGAAP-2026-IAS2-HITS.md` | **Yes** | **Yes** — teaching-critical Scope/broker/emission/crypto/forward cites; `cite-ey` (~7). FS “Practical example” 3-1/3-2/6-1/6-2 = NOTES-only (copyright) |
| KPMG 3.8 | `IAS2-KPMG-3.8-INVENTORY-2026-10-01.md` + enrich note; body text in `/tmp/kpmg-*` | **Yes (inventory + enrich)**; durable `kpmg-3.8-extract.txt` under extract folder **not yet persisted** | **Yes** — Ex 1–17 enrich pass; `cite-kpmg` (~48). Some table-image Ex deferred (no invent) |

---

## 3. Documents-synced refs

| Item | Status |
|------|--------|
| Laptop Documents bridge | Machine `2a06a250-7384-4878-8b5c-ffbf4a1f68e5` (`LAPTOP-MODGPP0C`) **disconnected** at pre-flight |
| Box vs Documents | Box `inputs/` + `refs/ias-2/draft-v1-linked/` = working source of truth |
| Pending CopyFromBox | See `IAS2-SYNC-PENDING-2026-10-01.md` / KPMG enrich note (METHOD, NOTES, ch01–ch06, KPMG inventory files) |

Could **not** re-verify Documents copies while offline; no evidence the four firm PDFs are missing on box.

---

## 4. Per-firm verdict

| Firm | Pre-flight | Content extract | Cite in HTML | Blocking? |
|------|------------|-----------------|--------------|-----------|
| Official | PASS | PASS | PASS | No |
| PwC Ch25 | PASS | PASS | PASS | No |
| DTT iGAAP 2022 A11 | PASS | PASS | PASS | No |
| EY Ch23 | PASS | PASS | PASS (teaching set; FS Practical skipped by rule) | No |
| KPMG 3.8 | PASS (PDF on disk) | PASS inventory/enrich; **durable extract.txt gap** | PASS | No (gap = hygiene, not missing firm) |

**Overall:** Four-firm + Official pre-flight **GREEN** for IAS 2. Ready for further write/enrich under existing copyright + densify gates.

---

## 5. Remaining gaps (non-blocking hygiene)

1. **Persist** `/tmp/kpmg-3.8-body.txt` (or re-extract from `part1-non-fi.pdf`) → `ias2-content-extract/kpmg-3.8-extract.txt` so future agents do not depend on `/tmp`.
2. Optional **symlinks** under `inputs/ias-2/` for EY Ch23 pointer + KPMG part1 (parity with Official/PwC/DTT aliases).
3. **Stale text to clean when touched:** `inputs/DISTRIBUTION.md` still says “EY GAAP 2026: not on box” (false as of 2026-10-01); `IAS2-CONTENT-AUDIT-2026-10-01.md` still has “No KPMG/EY” honest-gap line (superseded by EY unlock + KPMG enrich).
4. Content-level leftovers already tracked elsewhere (EY FS Practical skip; KPMG Ex 7A/7C table images; learning-curve defer) — **not** pre-flight firm-missing issues.

---

## 6. Skill / METHOD locks this pass

- `workflows/ifrs-teaching-body/SKILL.md` — HARD **Big4 completeness pre-flight** gate + workflow step 0 + Done/QA items (**file not truncated**).
- `workflows/ifrs-teaching-body-qa/SKILL.md` — QA section **I**; “No KPMG invent”-style skipped-firm lines = **FAIL**.
- `refs/ias-2/draft-v1-linked/IAS2-CONTENT-REWRITE-METHOD.md` — four-firm pre-flight rule + current status table.

---

## 7. This file

`/workspace/ias2-content-extract/IAS2-BIG4-COMPLETE-PREFLIGHT-2026-10-01.md`
