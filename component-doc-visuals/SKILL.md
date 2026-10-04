---
name: component-doc-visuals
description: Create editable, source-faithful Figma visuals for confirmed component documentation sections using a neutral visual kit, then verify geometry and image exports.
---

# Component Doc Visuals

Execute the steps in order, resuming completed work. Read [execution and handoff](../shared/execution-contract.md), [setup and evidence](../shared/setup-and-evidence.md), and [the neutral kit specification](../shared/visual-kit-spec.md). Before Persian captions, labels, or alt text, read [the complete Persian guide](../shared/persian-writing.md). Read [build and verification procedures](references/build-and-verify.md) before planning live geometry or editing Figma.

## 1. Establish the exact teaching claim

Read the user-supplied paragraph or confirmed section, required Figma component node link, requested locales, and requested output (one figure, complete coverage, or visual-only). Reuse the writer handoff if present. A paragraph supplied for illustration authorizes that scope; do not ask for blanket reconfirmation. Ask only about a specific unsupported or contradictory claim; do not invent a rule to illustrate.

Use a product example if supplied. If omitted, record “not supplied” and continue with native sources and neutral content. Ask for screen/container evidence only when a requested placement or padding claim cannot be established without it. A supplied screen helps with context and content, but cannot override native geometry or establish behavior by itself.

**Checkpoint:** a confirmed claim and scope, requested locales, and optional product-example availability are recorded.

## 2. Check source and tools before construction

Read the project configuration. Identify the native component, editable destination, and configured kit. Load `figma-use` and any other Figma skill required for the operation before a `use_figma` call. Check that source inspection, editable construction, export, and a fresh read are actually available.

Read the live source and destination before writing. Record native component identity, raw property keys, axes/values, exact chosen configuration, dimensions, and existing user edits. Never edit a source master, detach an instance, or replace it with drawn rectangles merely to finish the example.

Start from the actual Figma kit component: instantiate the chosen template and locale, and record its file, component/variant ID, and generated instance ID. A fresh reconstruction from rectangles is not a kit instance. Detach only the generated documentation wrapper if needed; preserve native product instances. If the kit is inaccessible or absent, request an accessible kit copy/link and mark construction blocked. Creating a kit from the specification is a separate explicitly requested setup task. Reuse the supplied destination; ask only if missing. If tools, source, or destination prevent the requested work, record the precise blocker and provide only a clearly labeled plan; do not claim to have created or verified a figure.

Before returning from a blocked construction step, save both the reason in the work record and a minimal `.work/visuals.json` entry. Use the actual component/section values with this shape: `{"figures":[{"id":"states-fa","component":"<component>","section":"States","locale":"fa-IR","verification":{"status":"blocked","reason":"<actual missing source, destination, or tool>"}}]}`. Omit unknown paths, hashes, dimensions, and bounds; do not fill them with guessed or verified values. This blocked record is a handoff, not an exported figure.

**Checkpoint:** native source, actual kit template, and authorized output location are readable, and necessary tools are available.

## 3. Make a small build plan

Select one family per main claim using the procedure's routing table. Record family, exact configurations, locales, target part IDs, caption, and expected comparison. Match the family to the evidence: a frame width is not a responsive breakpoint; a state name is not an interaction specification.

For complete coverage, inventory all actual axes and values, including relevant exposed boolean and swap properties. Map each value to a valid inspected configuration and planned figure. Do not infer missing values from naming conventions. Show dependent combinations in configurations where they exist; do not manufacture invalid combinations. Cover all combinations only when requested or when their interaction changes the documented rule. Track any intentionally omitted item and its reason; do not call partial coverage complete.

**Checkpoint:** each planned figure teaches a confirmed claim, each specimen has a real configuration, and requested coverage is traceable.

## 4. Build one figure, then repeat

Follow [build and verification procedures](references/build-and-verify.md). Use editable kit templates and actual native instances. Apply the kit's colors, layout, and fonts only to documentation elements. All kit-owned colors must bind to Figma color tokens. Center the complete visible composition, including every callout and auxiliary asset, with equal padding on all four sides of the gray stage; follow the kit specification’s geometry and post-export checks.

For Anatomy, read and execute [callout placement](references/anatomy-callouts.md) before positioning labels. Every title stays outside the whole native component, with a 12 px text-to-leader gap. Fit text boxes, select unobstructed exit sides, calculate comparable leader spans and exterior clearance, then verify the measured result after export. Never copy an earlier example's coordinates as a placement rule.

For dimensions, both the line (including end caps) and numeric text must use full-opacity annotation red. For placement or padding relative to screen/container edges, read [Positioning & Padding](references/positioning-and-padding.md): use 0.12-opacity red gap frames only on the requested sides. Never add these bands merely to compare component widths.

Name generated frames `<Component name> - <documentation type>` in English, with spaces around a plain hyphen; append role suffixes to nested documentation frames. Preserve names inside native instances. Keep exact variant/state names under specimens; use Persian semantic part names as primary Anatomy labels in FA. Never translate configuration identifiers.

Build and verify one figure before multiplying a layout across configurations or locales. If a small component is readable at native size, preserve whitespace; do not enlarge it to fill the stage. Keep newer destination edits and place expanded outputs outside the fixed master grid.

**Checkpoint:** live layout has no clipping, overlap, drifting guides, mismatched configuration, or unsupported specimen edits.

## 5. Export, re-read, and inspect

Use the procedure's ordered verification steps. Capture settled pre-export bounds, export the composed figure, then perform a **separate fresh Figma read**. Compare subject and annotation-target geometry; inspect the actual exported image at the intended Markdown display width. A tool success response alone does not pass this checkpoint.

Repair the specific defect and repeat export plus both checks. After two repair passes for the same unresolved defect, stop retrying that figure, record the blocker, and continue independent figures. Never lower the verification standard to finish a batch.

**Checkpoint:** the exact exported file passes both geometry comparison and image inspection. Otherwise it is blocked or unverified.

## 6. Deliver the requested format

Write the visual manifest described in [execution and handoff](../shared/execution-contract.md), including actual dimensions, configuration, file hash, and check evidence. Put source URLs, editable frame URLs, captions for full documentation, scale, and verification notes in the handoff.

For **visual-only** delivery:
- In Figma, create a `SECTION` named exactly after the component and put only that component's visual frames inside it.
- In Markdown, use `## <Component name>` followed only by verified image embeds with concise alt text. No prose, captions, lists, metadata, or extra subsection headings inside the section.
- Make one such section per component. Keep blocked-figure notes in a separate work file.

For full documentation, hand verified figures and their section/claim mapping to `component-doc-assembler`. Report missing sources or inaccessible files accurately and identify any unfinished coverage. Exporting figures does not authorize publishing a repository or changing Figma sharing permissions.
