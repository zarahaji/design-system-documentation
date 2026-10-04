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

- Broad component/property coverage and live regression testing of the latest callout, color, positioning-band, and kit-first instructions. The limited completed live evaluation is recorded below.
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

## Historical first step-by-step revision — 2026-10-04

The three skills now define ordered steps, inputs, observable completion checks, and precise blocked-work behavior. Their [execution contract](../shared/execution-contract.md) separates claim evidence, draft approval, and image verification. The visual skill has a separate [build and verification procedure](../component-doc-visuals/references/build-and-verify.md) so live geometry instructions are loaded when needed.

Four synthetic scenarios were run once against the previous package and once against this revision, in separate temporary projects. Each run explicitly requested `model_reasoning_effort="low"` on the configured `gpt-6-astra` model. Both versions satisfied the reviewed criteria in all four scenarios:

| Scenario | Reviewed behavior |
| --- | --- |
| Ready bilingual draft | Both languages saved; only selected sections; exact identifiers and opacity retained; no redundant setup or invented focus behavior |
| Behavior gap interview | Selected reference used to ask local questions; reference defaults not published as local rules |
| Mixed image handoff | Valid neutral figure retained; stale hash, wrong locale, and missing file excluded; nested relative path resolves; approved text delivered |
| Missing native visual source | No substitute product visual, fake verification, or repeated product-screen question; blocker recorded accurately |

The comparison includes manual review of saved text, sidecars, final responses, and actions, plus 15 deterministic artifact assertions per version. All 13 package-checker tests and the skill validator for all three entrypoints passed. Raw traces, fixtures, and project paths are kept outside the distributed package.

This is a smoke test of local file workflows, not proof that the revision improves success rates. One run per scenario on one model does not establish reliability across models or repeated runs. The CLI emitted fallback model-metadata and skill-description-budget warnings; effort was explicitly requested, not independently measured at the service. Global skill discovery and plugin startup were present. No live Figma operation was used, so the new layout and verification procedure still needs a live visual evaluation before claiming visual-quality coverage.

To repeat the comparison, use identical synthetic source facts and prompts in fresh workspaces, copy only the three skill folders plus `shared` into each project's `.agents/skills/`, and explicitly set `-c 'model_reasoning_effort="low"'` in the `codex exec` invocation. Establish the expected behavior before running, inspect artifacts as well as the final response, and keep incomplete or tool-blocked cases distinct from successful live work. Do not run model evaluations automatically in repository CI.

## Cross-model follow-up — 2026-10-04

Nineteen additional isolated CLI runs explicitly selected a model with `--model` and requested `model_reasoning_effort="low"`: nine on `gpt-6-luna`, eight on `gpt-6-sol`, and two on `gpt-6-astra`. Each run retained its source snapshot, trace, final reply, and saved artifacts outside the distributed package. Failed attempts were retained. All CLI processes exited successfully; that did not mean the generated content passed review.

Luna and Sol each ran the four scenarios above. Both passed the original core criteria for the behavior interview, mixed-image assembly, and unavailable visual source. The first blocked-visual runs omitted a machine-readable blocked manifest; after making that handoff explicit, both models saved it correctly in a second run. No live Figma construction was attempted.

| Model | Writing observations across revisions |
| --- | --- |
| GPT-6 Luna | First run leaked the raw API key `Label#12:34`. After the first fix, it omitted `State` and the literal `Ticket#12:34`; another attempt unnecessarily blocked on missing foundations and saved no drafts. On the final instructions, one of two runs passed; the other still omitted the `State` axis. Low-effort writing remains inconsistent. |
| GPT-6 Sol | First run incorrectly shortened `Version#beta` to `Version`. Three subsequent writing runs passed after the first identifier fix, including one on the final instructions. |
| GPT-6 Astra | Two additional writing regression runs passed, including one on the final instructions. The earlier four-case comparison remains historical evidence for its earlier revision. |

The resulting fixes add an [identifier inventory and checker procedure](../component-doc-writer/references/identifier-check.md), require coverage of source items relevant to selected sections, preserve component identity in Persian, and clarify when available sources are sufficient to draft. Only a terminal numeric API suffix matching `#[0-9]+:[0-9]+$` is removed from a property key. Meaningful names such as `Version#beta` and literal content such as `Ticket#12:34` remain intact. Missing foundations do not block documenting authored properties and examples that do not depend on foundation tokens.

The runtime checker only validates the inventory it receives. It cannot discover source facts omitted while building that inventory. This limitation appeared in Luna's tests: an incomplete self-authored inventory passed its local check while the external fixture-based review detected omissions. The test reviewer used an independent expected inventory containing both properties, `State`, its two values, `Stable`, and the supplied literal.

Eight identifier-checker tests were added to the original 13 package tests; all 21 portable tests passed. The release package checker and official skill validator passed for all three entrypoints after the runtime changes. Saved text, evidence records, responses, and relevant actions were reviewed by the parent agent alongside deterministic artifact assertions; no independent model judge was used.

These results cover a small synthetic prompt set and successive instruction revisions. The three successful Sol runs are not three repetitions of an identical final version, and the counts do not establish statistical reliability. CLI warnings reported fallback model metadata and shortened global skill descriptions. Low effort was explicitly requested, not independently measured at the service. At that stage, live visual quality and geometry were unverified; the later limited live evaluation below adds evidence without establishing broad source-extraction completeness.


## Live Figma follow-up — 2026-10-04

GPT-6 Luna and Sol each ran with explicitly requested low effort to build Anatomy and Variants figures from one native component, then a Responsive Comparison from a native dialog. Six completed figures were reviewed. Earlier tool/quota-blocked attempts were kept separately and do not count as completed figures. Private source links, images, and raw traces remain outside the distributed package.

The parent agent inspected the exact final exports and performed independent Figma geometry reads. Native instances, the source masters, existing kit templates, and unrelated earlier examples were preserved in the inspected runs. Both models represented the four tested Boolean configurations. This is coverage of those fixtures only.

| Output | Observations |
| --- | --- |
| Anatomy | Luna placed one label inside the whole component and detached a leader from its target. Sol used unsuitable left-label alignment and excessive gaps. Both had target/outline radius mismatches. These findings informed the explicit callout geometry procedure. |
| Variants | Both outputs were readable and preserved the tested configurations. |
| Responsive | Both compared native dialog widths of 280 and 360 logical px with the same content. Luna used black dimension labels, inward-shifted caps, and uneven vertical clearance. Sol used red dimension lines and text with more balanced spacing. |

The model runs could not independently download the final exports because of local network limitations; their manifests retained the blocker. The parent agent retrieved and reviewed the exact images separately. This verifies the reviewed outputs through a supplemented workflow, not autonomous end-to-end model success.

The latest revision requires outside Anatomy labels with a 12 px text-to-leader gap, measured comparable callout spans, full-red dimension lines and text, and purpose-specific positioning bands. It also requires actual kit instantiation and a Figma component link in the input format. These subsequent instruction changes have passed package validation but have not yet been behaviorally rerun. Historical writing tests used synthetic local sources and therefore do not validate the new Figma-link intake requirement. No claim of guaranteed quality across models or reasoning levels is made.
