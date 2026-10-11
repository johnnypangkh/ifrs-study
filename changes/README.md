# Approved teaching changes

`tools/check-incremental.py` compares visible teaching text on a pull request with the merge-base of `main`. A removal or a rewrite fails unless this directory lists it. An addition is only a warning unless the run uses `--strict-added`.

Whitespace, `?v=` stamps, `data-phase-*` hooks, and the last-update stamp are ignored. Text inside `<!-- include:... -->` belongs to the source file, so the included copy is not a second item and not a move. Capitals, hyphens, and U+2011 non-breaking hyphens are real changes.

No file is required when the pull request does not remove or rewrite teaching text.

## Which file

| Run | File |
| --- | --- |
| Pull request (CI sets `GITHUB_REF` or the event payload) | `changes/<pr-number>.yml` |
| Local branch with no pull-request number | `changes/<branch-name>.yml` |

A branch named `cursor/example` uses `changes/cursor/example.yml`. Pass `--approval path` or `--pr 106` to point at a different file.

## Entries

The file is a list. Matching uses normalised text (collapsed whitespace, stamps removed) and the `file` value the report prints.

| Field | When |
| --- | --- |
| `action` | `removed`, `changed`, or `added` |
| `file` | Repo path from the report. For a change or an addition this is the head file. For a removal it is the base file. Several files are joined with `, `. |
| `old` | Exact old text for `removed` and `changed` |
| `new` | Exact new text for `changed` and `added` |
| `source` | Required. Empty fails the check. |

`source` names why the edit is allowed. Use one of these:

- `markup <ref>` — the wording follows the cited standard or manual
- `QC FAIL <PR rN item n>` — a numbered QC failure on a pull request
- `Content item <n>` — a numbered content-pass item
- `brief item <n>` — a numbered brief item
- `ruling <name>` — a named ruling

An entry that matches nothing (wrong text, wrong file, or a change that is no longer in the diff) fails as stale.

## Template

```yaml
- action: changed
  file: ias-16/draft-v1-linked/visuals/ch07-disclosure.html
  old: "Split additions · present disposals as a single line when useful for users."
  new: "Show additions and acquisitions through business combinations as separate lines; show all disposals as one line."
  source: "Content item 1"

- action: removed
  file: ias-16/draft-v1-linked/visuals/ch02-recognition.html
  old: "Sentence that was deleted."
  source: "QC FAIL PR r1 item 2"

- action: added
  file: ias-16/draft-v1-linked/visuals/ch07-disclosure.html
  new: "IAS 16 · para 73(e)"
  source: "markup IAS 16 para 73(e)"
```

Quote text that contains a colon. The checker also accepts `|` block scalars.

Generate a first draft from a diff. Every `source` is the placeholder `TODO`:

```bash
python3 tools/check-incremental.py --base <merge-base> --head HEAD --emit-draft changes/<pr-number>.yml
```

Replace each `TODO` with one of the source forms above before committing the file. The checker rejects a blank `source`. It does not treat the word `TODO` as blank, so a committed placeholder would satisfy that check without naming a real authority.
