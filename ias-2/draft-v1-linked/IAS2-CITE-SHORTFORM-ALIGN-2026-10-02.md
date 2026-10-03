# IAS 2 cite short-form alignment — 2026-10-02

## Result

Aligned the IAS 2 draft-v1-linked Big4 cite-chip work-title prefixes and the corresponding Short form documentation. Full-name cells on `references.html` were left unchanged. Official cite chips, firm colours, and chip CSS classes were not changed. No CSS/cache bump was needed.

## Visible cite-chip counts aligned

Counts below are the visible Big4 cite chips verified after replacement, and represent the old-prefix chips aligned in this pass:

| Firm | ch01 | ch02 | ch03 | ch04 | ch05 | ch06 | references.html | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PwC | 17 | 21 | 72 | 38 | 22 | 11 | 2 | 183 |
| DTT | 14 | 5 | 70 | 35 | 12 | 29 | 2 | 167 |
| EY | 11 | 2 | 21 | 9 | 3 | 9 | 2 | 57 |
| KPMG | 26 | 21 | 107 | 53 | 21 | 22 | 2 | 252 |

Pack METHOD/NOTES/XREF/preflight/reference MD was normalized to the same four target work-title forms, including locator-preserving forms. References full-name cells remain long titles.

## Validation

- Old-only prefix scan across IAS 2 HTML/MD and both workflow skills: **0 hits**.
- Old DTT A11/year-order variants: **0 hits**.
- All 659 extracted Big4 cite chips have the target firm prefix; no bad-prefix chips found.
- Official cite-chip classes/text and firm colour/CSS classes were not edited.
- Skill files updated: **yes** — `ifrs-teaching-body/SKILL.md` and `ifrs-teaching-body-qa/SKILL.md`; examples and 2026.10.02 changelog notes updated.
- `tools/pack_audit.py` was not runnable in the box because the optional `bs4` module is unavailable; custom HTML span parsing supplied the structural chip validation above.
- Documents sync: **not performed**.
