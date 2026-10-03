# CF 2018 ↔ IAS 2 format parity — 2026-10-01

**Pack:** `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/`  
**Skills (source of truth):**  
- `/home/box/agent-data/workflows/ifrs-teaching-body/SKILL.md`  
- `/home/box/agent-data/workflows/ifrs-teaching-body-qa/SKILL.md`  
- `/home/box/agent-data/workflows/ifrs-visual-grammar/SKILL.md`  
**IAS 2 reference (read-only):** `/workspace/ifrs-website/refs/ias-2/draft-v1-linked/`  
**Backup:** `/workspace/cf2018-ias2-parity-fmt-20261001-backup/`  
- `draft-v1-linked/` = pre-edit snapshot  
- `final/` = post-edit snapshot  

**IAS 2 / IFRS 18:** untouched.  
**Documents sync:** **SKIPPED** — laptop `LAPTOP-MODGPP0C` (`2a06a250-7384-4878-8b5c-ffbf4a1f68e5`) offline.

---

## Done this pass (Grok-doable chrome / numbering / cite placement)

### 1. Map / Diagram numbering = chapter section numbers (IAS 2 style)

| Visual | Change |
|--------|--------|
| `visuals/ch09-combined.html` | Circles `3.12`→`9.1`, `3.14`→`9.2`, `BC3.21`→`9.6`; chapter jumps `3`→`3.6`, `10`→`10.1`. Official CF paras kept as muted `(CF …)` hints beside Decision questions — **not** on circles. |
| `visuals/ch10-carve.html` | Circles `3.10`→`10.1`, `3.14`→`10.3`; jumps `3`→`3.6`, `9`→`9.1`, `6`→`6.7`. Same Official-hint pattern. |
| `visuals/ch07-presentation-disclosure.html` | All `fb-num` display text remapped to href section ids (`7.1`…`7.5`); collapsed duplicate ranges. |
| `visuals/ch06-measurement.html` | `Ch5`→`5` (chapter-level jump). |
| `visuals/ch11-status.html` | Hrefs remapped from stale `ch09.html#s-9-*` → `ch11.html#s-11-*`; chips `11.1`–`11.3`. |

Iframe cache-bust: `?v=cf-ias2-parity-20261001` on touched chapter Maps.

**Not done (parked):** Opus-signed Ch9/Ch10 Map redesign (layout / mid-branch art / visual ambition). Chrome + numbering + labels + fit only.

### 2. Illustrations — C1 cite placement

Hoisted body `.cite` chips onto `worked-strip-title` (cite-row) for Illus that still had body cites:

- Ch3: `3.5.2`
- Ch4: `4.6.1`
- Ch9: `9.5.1`–`9.5.6`, `9.6.1`–`9.6.2`
- Ch10: `10.2.1`, `10.3.1`, `10.4.1`–`10.4.2`

Nested-aware cite parser used (`.cite-house` inside `.cite`). First broken pass rolled back from backup and re-applied cleanly.

All pack Illus remain `.worked-strip` + neutral peers (Facts / Assessment / Conclusion or equivalent). Decision strips keep cites inside **Test** columns (allowed — not Illus C1).

### 3. Decision / Test / Assessment roles

- Map forks: `.dec-tag` **Decision** (Ch5 / Ch9 / Ch10 visuals).
- Decision-strip criterion columns: **Test** (renamed **Concept / gate** → **Test** in Ch4–Ch8 — 10 labels).
- Illus analysis columns: **Assessment** (unchanged).
- Reader-facing peer role `>(Gate)<`: **0**.

### 4. QA gate (`ifrs-teaching-body-qa`) — green

| Check | Result |
|-------|--------|
| House-only Big4 chips | 0 |
| `§` inside `.cite` | 0 |
| `p.box-body>ul` | 0 |
| Illus not in worked-strip | 0 |
| Illus peer ok/warn/danger | 0 |
| C1 body cites on Illus | 0 |
| Densify thin (≤5 li / ≤350 chars) | 0 fails |
| Flowery titles | 0 |
| Gate role label | 0 |
| Map chip ↔ `#s-N-M` prefix | aligned |
| Visual → chapter hrefs | resolve |

---

## Honest remaining debt

1. **Documents sync pending** — laptop offline; sync when connected.  
2. **Opus Map redesign parked** — Ch9 Combined + Ch10 Carve Maps need Opus-level redesign (not claimed Grok-signed). Numbering/chrome only this pass.  
3. **`visuals/ch09-status.html`** — stale Status Map still on disk with `9.x` chips; live Status teaching is Ch11 + `ch11-status.html`. Confirm whether to delete or unlinked orphan (not removed this pass — no invent / no silent delete without Johnny).  
4. **Illus visual-when-complex** — several dense multi-gate Ch9/Ch10 plates are still prose/bullet peers only; diagram/mini-flow debt remains (skill E3) — Opus territory when unlocked.  
5. **Decision-strip ok/warn fills** — still used on some Decision strips (allowed for non-Illus); leave unless Johnny wants neutral Decision strips too.  
6. **Teaching titles that say “gate” in substance** (e.g. “Relevance gate”, “Faithful representation gate”) — kept as technical wording, not role tags.  

---

## Changed paths (absolute)

### Chapters
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch03.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch04.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch05.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch06.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch07.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch08.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch09.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch10.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/ch11.html` (iframe cache-bust / status Map link path via visual)

### Visuals
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/visuals/ch06-measurement.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/visuals/ch07-presentation-disclosure.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/visuals/ch09-combined.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/visuals/ch10-carve.html`
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/visuals/ch11-status.html`

### Report + backup
- `/workspace/ifrs-website/refs/cf-2018/draft-v1-linked/CF-IAS2-FORMAT-PARITY-2026-10-01.md`
- `/workspace/cf2018-ias2-parity-fmt-20261001-backup/`

**QA stamp:** structure + densify + cite placement **PASS** for this format-parity sweep. Pack content completeness crosswalks unchanged (see GAP-FILL-4 / GROK-SIDE-KO reports). No invent. Opus Maps not claimed.
