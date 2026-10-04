# Testing and known limitations

## Observed evaluation scope

An evaluation on 2026-10-04 used isolated Codex CLI runs and synthetic component sources. Raw traces and private project references are intentionally not distributed in this repository.

| Area | Observation |
| --- | --- |
| Implicit selection | Three relevant requests selected the expected skill; two unrelated requests did not load these skills. |
| Repeated workflows | Four scenarios ran three times each. Eleven runs met the reviewed criteria; one bilingual run had ambiguous Persian opacity wording. |
| Multi-turn interview | A four-turn session persisted setup, collected selected sections, used Carbon to form questions, and preserved local rules that differed from the reference. |
| Missing assets | Unavailable native sources were not replaced with invented product visuals; missing image links were removed from publication Markdown and reported separately. |
| Package checker | A clean fixture and deliberately invalid fixtures exercised parsing, links, metadata, privacy-term matching, release requirements, and ignored repository artifacts. |

The opacity finding led to a narrow clarification in `shared/persian-writing.md`: full opacity is not full transparency. A fresh bilingual regression run after this clarification used «کدری کامل» for full opacity and preserved `opacity=0.40` correctly. All 13 portable checker tests also passed locally. Historical run counts describe the evaluated version; they are not a claim that all behavior has been re-evaluated after every documentation edit.

## What remains unverified

- Live Figma creation, source preservation during composition, complete property coverage, actual image exports, and a fresh post-export geometry comparison.
- Statistical reliability across models, environments, or a large prompt set. Three runs per scenario are a smoke test, not a benchmark.
- Public access to linked Figma files and rights to distribute external assets.

Human review of the traces and documents supplemented deterministic checks. A separate model-based judge was not used.

## Run the portable checks

```sh
python3 scripts/check_package.py . --release
python3 -m unittest discover -s tests -v
```

These checks need Python 3.10 or later and no third-party packages. They validate the repository, not component behavior.

## Reproduce a behavioral evaluation

Install the skills in an isolated project with a small authored component source. Capture a run using `codex exec --json`, then review both its actions and saved artifacts. Define expectations before running it: selected sections, exact identifiers, confirmed rules, missing-asset handling, and required evidence. Include requests that should not activate the skills.

For a visual evaluation, first confirm that the necessary Figma tools are available. Record native and annotation bounds after layout settles, export the actual image, then perform a separate fresh Figma read and compare those bounds. Inspect the exported image at its intended display width. Report unavailable tooling separately from a failed skill.
