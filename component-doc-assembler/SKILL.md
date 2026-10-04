---
name: component-doc-assembler
description: Combine approved component documentation text and verified visual exports into complete Persian, English, or bilingual Markdown deliverables with working image links.
---

# Component Doc Assembler

Execute these steps in order. Read [execution and handoff](../shared/execution-contract.md) and [setup and evidence](../shared/setup-and-evidence.md). Before editing Persian text, captions, or alt text, read [the complete Persian guide](../shared/persian-writing.md). Assemble the user's selected sections; do not add policy during a merge.

## 1. Inventory the inputs

Read the request, configuration, approved drafts, and available visual handoff. Build a small working table: selected section × requested language, text path and approval scope, matching figure IDs, and blockers.

Reuse explicit choices and approval already in the conversation. A filename containing “approved” is not sufficient by itself, but the user's statement that the supplied text is approved is sufficient. If a draft is not approved, ask for approval of that text; you may prepare a clearly labeled assembly draft without calling it final.

**Checkpoint:** selected sections, requested languages, approved text versions, and requested output format are known. Do not ask writer setup questions irrelevant to assembly.

## 2. Admit only matching, verified figures

For each candidate image, check all of the following:

1. Its component, section, claim, and configuration match the text it would accompany.
2. Its locale matches the publication language. A `neutral` figure is reusable only if its visible labels and content truly suit both languages; do not pair English captions with a Persian-labeled figure.
3. Its export exists and is readable. Resolve its path relative to the manifest, not the shell's current directory.
4. Its actual file hash matches the verification record. A changed file needs fresh verification; do not copy an old `verified` label.
5. Its recorded dimensions, fresh post-export bounds comparison, and actual rendered-image inspection satisfy the execution contract. The word `verified` without evidence does not pass.

Accept an equivalent older handoff format when it contains the same evidence; do not demand a format conversion for its own sake. If a check fails, exclude that figure from publication and record the exact reason in a separate missing-assets note. Continue supported text and other valid figures. Do not manufacture a substitute image or invent a passed check.

**Checkpoint:** every included figure is matched and verified; every excluded figure has an explicit reason.

## 3. Assemble without changing the rules

Use the requested file paths and preserve section order from the approved draft or explicit user choice. Include each selected section once. A selected but missing text section is a reported gap, not permission to invent prose or publish an empty heading.

For full documentation:
- Place each figure beside the paragraph making its claim.
- Preserve approved meaning, conditions, numeric values, and exact property/variant identifiers. Limit edits to assembly and minor formatting; substantive changes return the affected passage for approval.
- Create separate `.fa.md` and `.en.md` files for bilingual output, with corresponding sections and locale-appropriate figures. Produce only requested languages.
- Put packaged images in the chosen image directory. Compute relative Markdown paths from **each output Markdown file's parent directory**, including when it is nested. Encode path spaces as `%20` where needed; verify the decoded path resolves.
- Keep captions and alt text truthful to the visible image. Use approved captions when supplied.

For visual-only output, use one `## <Component name>` section per component containing only verified image embeds. Put no captions, prose, lists, metadata, or extra headings inside it.

**Checkpoint:** files contain only approved scoped text and admissible figures. Missing-asset notes, source ledgers, and verification metadata stay outside publication Markdown.

## 4. Check the saved result

Read the actual saved Markdown and image files, then:

1. Compare the section/language inventory against the request. Detect omissions, duplicates, extra sections, and mismatched bilingual facts.
2. Resolve every Markdown image embed, including any inherited from the supplied draft. Existence alone is insufficient: each must also have passed step 2. Remove broken, stale, wrong-locale, and unverified embeds and any prose referring to those missing figures.
3. Check captions/alt text against the corresponding visible figure; verify dimensions and hashes still match the admitted exports.
4. Look for empty headings, unrequested placeholders, internal evidence notes, and leaked terminal Figma binding suffixes on property identifiers. Preserve literal user content containing `#`; do not run a broad replacement over the document.
5. Confirm that text remains complete when a figure is omitted. Report missing selected text or images in the sidecar and final response, not as unexplained publication gaps.

**Done:** return the actual Markdown paths, image directory when present, editable Figma links when available, and concise completeness status. If all text is ready but an image is blocked, deliver the text and the separate missing-asset note. Do not describe a partial package as fully verified.
