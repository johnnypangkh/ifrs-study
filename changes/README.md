# Approved teaching changes

`tools/check-incremental.py` compares visible teaching text on a pull request with the merge-base of `main`. A removal or a rewrite fails unless this directory lists it. An addition is only a warning unless the run uses `--strict-added`.

Whitespace, `?v=` stamps, `data-phase-*` hooks, and the last-update stamp are ignored. Text inside `<!-- include:... -->` belongs to the source file, so the included copy is not a second location and not a move. Capitals, hyphens, and U+2011 non-breaking hyphens are real changes.

The checker reads every `*.html` file except paths under `_archive/`. Those directories are retired Conceptual Framework snapshots, not the published notes. A historical copy must not hide a deletion on the live page, and an archive-only edit is outside this guard. See `tools/README.md`.

A removal is per location. The same sentence still sitting in another file does not cancel it. A hand copy replaced by a new include of the same text is kept when the source already had it, and moved (`source.html#section`) when a different file newly owns it. It is not a removal. Different wording is the source file's own change or removal, once. A move across files is only when the count falls in one place and rises by the same amount in a file that did not already have the copy. Unchanged text that stays in the same file is kept when only its locator changes.

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
| `file` | Repo path from the report. One location, one file. For a removal this is the file that lost the text. |
| `locator` | Optional. When present, a `removed` entry matches only that locator. Omit it to match the text in that file at any locator. |
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
  locator: "section:ch02-recog"
  old: "Depreciation of right-of-use assets used to construct, add to, replace part of or service PPE may form part of cost."
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
