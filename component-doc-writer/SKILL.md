---
name: component-doc-writer
description: Research and write evidence-based design-system component documentation through project setup, section selection, a focused gap interview, and Persian-first or bilingual Markdown drafts.
---

# Component Doc Writer

Document one component at a time. Execute the steps below in order, starting at the first unfinished step. Read [execution and handoff](../shared/execution-contract.md) and [setup and evidence](../shared/setup-and-evidence.md). Read [section choices](../shared/sections.md) when selecting or mapping sections. Before writing Persian drafts, captions, or alt text, read [the complete Persian guide](../shared/persian-writing.md).

## Ready-to-draft rule

When the request already provides a readable Figma component node link, selected sections, language(s), and a reference choice (including “none”), setup is settled. Inspect that source and draft its supported claims now. An empty foundations list does **not** block this path. The heading Implementation alone does not create a token dependency: authored properties, enum values, and example content can be documented from the component source. Ask for foundations only if a particular requested claim needs a missing token/foundation fact; name that exact claim and continue the independent supported content.

## 1. Recover the task

Read the request and existing component work record. Extract: component, Figma component node link, supplementary sources, selected sections, language(s), output location, and requested action (new draft or revision). Reuse explicit decisions. A request naming selected sections is already a selection; a request for both languages is already a bilingual choice.

**Checkpoint:** component and requested action are identifiable. If not, ask for the missing identity. Do not inspect unrelated components or draft a generic substitute.

## 2. Complete only missing setup

Read `component-docs.json` from the user's project; use [the example](../shared/project.example.json) only for structure. Follow the setup guide's missing-value rules. Require the component’s Figma node link, reusing a saved link when present; ask for it if absent. Ask for absent source access, language choices, and foundation/token context where relevant. Then settle external interview references: use a saved selection, accept an explicit “none,” or show the guide's shortlist and wait for a choice. Never silently turn an unconfirmed template's empty list into a decision.

Save resolved preferences in the project configuration, preserving unrelated fields. Do not put project URLs or identifiers in the skill folder. Do not reset saved choices to defaults on each invocation.

**Checkpoint:** available evidence and language choices are known; references are selected, declined, or awaiting a stated choice. Supported inspection may continue while setup questions wait. External comparison waits for reference selection.

## 3. Inspect, then settle sections

Inspect the linked Figma component and relevant supplementary component sources before the full interview. If Figma access is blocked, record that limitation and continue only claims supported by available evidence; do not claim live source inspection. Extract its purpose, named parts, property keys, axes/values, visual states, authored dimensions, behavior notes, and constraints relevant to the request. Preserve raw keys in working notes. Record inaccessible evidence precisely.

If sections are not already selected, show the readable choices from [sections.md](../shared/sections.md), with short purposes in the user's language. Wait for selection. If selected, echo the set briefly and proceed; do not require another “yes.” Do not silently add sections or discard a selected section that appears inapplicable.

**Checkpoint:** the selected set is explicit and recorded. No drafting before this checkpoint; inspection and gap identification are allowed.

## 4. Resolve selected-section gaps

Build the claim ledger from the execution contract. Work one selected section at a time:

1. Inventory the authored items relevant to each selected section before choosing prose: state/variant axes and values, exposed properties, supplied example content, and confirmed rules. Attach local evidence to each. Cover those relevant items unless the user asked to summarize or omit them. Record a scope-based reason for an exclusion; do not silently drop an item to shorten the draft or make a check pass.
2. Distinguish observed appearance from behavior, usage policy, and accessibility claims. Missing behavior stays unknown even when a state name sounds familiar.
3. Consult only chosen external references using compact reusable notes. Convert relevant differences into questions, not local rules.
4. Ask a small related batch of questions whose answers change the selected output. Show the observed fact and specific gap. Offer options only when meaningful; label recommendations as proposals.
5. Record answers and their scope. Recheck only affected claims. If the user defers a point, exclude that claim and log the gap; continue supported parts. If no grounded content remains for a selected section, ask whether to defer it rather than filling it with generic advice.

**Checkpoint:** each claim to be drafted is `confirmed`. Unresolved claims stay outside publication text. Lack of an unselected Accessibility or Behavior rule does not block an appearance-only States draft.

## 5. Draft from the ledger

Before drafting claims containing source identifiers, read [the identifier procedure](references/identifier-check.md), copy the raw keys, axis names, values, and supplied literal examples from that selected-section inventory into its input manifest, and generate the raw-to-public map. Do not normalize identifiers from memory.

For each selected section, write only its confirmed claims. Use current project terminology and the section's purpose; do not expand the outline to display everything inspected.

- In Persian drafts, use Persian section labels from [section choices](../shared/sections.md); stable English section names may follow in parentheses. These structural headings are not source identifiers. Transliterate the component name consistently; do not replace it with a related component name merely because its purpose is similar. For example, Toggle is تاگل, while Switch is سوییچ; a toggle is not renamed to Switch in Persian prose.
- Preserve authored property, variant, state, size, and configuration names and values, including capitalization and spaces. Remove only a terminal Figma API suffix matching `#<digits>:<digits>` from a public property key. Thus `Label#12:34` becomes `Label`; `Version#beta`, `#12:34 title`, and literal user content do not change. Keep the raw key only in working evidence. Even in Implementation, do not repeat it in a parenthetical or a sentence explaining how the public key was derived. Copy public names from the generated map; never split all names at `#`.
- Describe a state as appearance unless activation and behavior are separately confirmed. “Disabled uses opacity 0.40” does not imply “Disabled is skipped by keyboard focus.”
- For bilingual output, draft both files in this pass in primary-language order. Use the same selected sections, facts, conditions, numbers, and identifiers. Translate prose naturally; one language's approval is not a prerequisite for drafting the other.
- For a single language, produce only that language. Use requested paths; otherwise use component filenames ending in `.fa.md` and/or `.en.md` under the configured output directory.
- Keep evidence, research-system names, unresolved questions, and missing-asset notes in the work record. Do not insert `TBD`, empty headings, or references to undelivered figures unless the user requests placeholders.

**Checkpoint:** each draft is complete within the confirmed scope, with no claim added merely to sound more comprehensive.

## 6. Check, save, and hand off

Check the actual draft against the ledger:

1. Compare headings to the selected set: each once, no additions or silent omissions.
2. For every rule, number, condition, and identifier, locate supporting evidence. Remove or resolve unsupported claims.
3. For bilingual output, compare corresponding sections for equal meaning and identical configuration values; check the Persian guide, including opacity versus transparency.
4. Save Markdown and a compact work record. Run the [identifier checker](references/identifier-check.md) on the saved drafts when local Python execution is available. Fix every reported mismatch and rerun it; record the actual result or the unavailable-tool limitation. Read the saved files to catch missing content, broken formatting, raw property keys even in explanatory prose, and internal notes.
5. Mark newly written text as draft. Record user approval only when given, for the actual version and scope. When visuals are requested, create the section-level handoff in the execution contract; do not automatically run visuals for a text-only request.

**Done:** return saved draft paths, languages and selected sections, plus unresolved decisions if any. Assembly uses approved text and verified figures through `component-doc-assembler`.
