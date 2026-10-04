---
name: component-doc-visuals
description: Create editable, source-faithful Figma visuals for confirmed component documentation sections using a neutral visual kit, then verify geometry and image exports.
---

# Component Doc Visuals

Read [the neutral kit specification](../shared/visual-kit-spec.md) and [shared setup and evidence](../shared/setup-and-evidence.md). For Persian captions or annotation text, read [the full Persian guide](../shared/persian-writing.md). Use the user's project configuration and live Figma sources; do not assume a fixed file key, component ID, token library, or font.

## Choose the visual

Before starting visualization for a component, ask once whether the user has a product screen showing it and invite them to attach it as an example. Skip the question if they already supplied a screen or answered it for this component. Wait for their answer; if they do not have a screen, continue with the component source and neutral examples. Treat an attached screen as context for placement and realistic content; use it in a Product Example only when that visual is selected and the user is permitted to share it. Do not let the screen override the source component's native geometry or confirmed rules.

Start with a confirmed paragraph or section. Select one visual family that teaches its main point: Anatomy, Variants, States, Rule Comparison, Responsive Comparison, Truncation, Behavior, or Product Example. A request to complete visual coverage requires inspecting all actual variant axes and values of the source component; a single-paragraph request needs only the relevant family. Do not infer behavior from a state name, a breakpoint from an example frame width, or truncation from sample text.

## Build in Figma

Use the neutral kit page configured in `visualKit.pageUrl`. If the kit has not been built, ask for the destination Figma design file and create a new page using [the kit specification](../shared/visual-kit-spec.md). Before a `use_figma` call, load the `figma-use` skill and any other Figma skill its instructions require. Inspect the destination file and the source component before writing. Instantiate editable kit templates and actual source component instances. Preserve all native product styling, internals, and source masters. The kit's neutral colors and geometry apply only to documentation chrome.

Name each generated documentation frame in English as `<Component name> - <documentation type>`, with spaces around a plain hyphen; for example, `FAB Menu - Anatomy`. Apply the same prefix to nested documentation frames with a role suffix, such as `FAB Menu - Anatomy Stage`. Preserve authored names inside native component instances and exact variant/property identifiers.

Place annotations from actual displayed geometry. Keep exact source names beneath Variants and States. Keep every structural frame in Auto Layout; reserve absolute placement inside a stage for geometry-dependent overlays and specimen text. Keep each Variants or States specimen and its name in one auto-layout cell with 24 px between them, wrap the gallery as it grows, and let the stage and output frame grow vertically. Place outside captions 30 px below the stage. Place expanded outputs outside the fixed master component-set grid. Use Noto Sans Arabic for FA examples and Noto Sans for EN examples. Use Persian semantic part names as primary Anatomy labels in FA. Do not embed a user image merely as a shortcut when the request calls for an editable example; use a screenshot only when the lesson genuinely concerns product context and the user has rights to use it. Preserve newer user edits in the destination file.

## Verify and deliver

Record pre-export subject and annotation-target bounds. Export the composed image, then make a separate fresh read of the Figma document and compare those bounds. Repair and re-export if layout drifted. Inspect the image at its intended Markdown display size for clipping, text shaping, contrast, and alignment.

For visual-only output, group every final image for a component in one section named exactly after that component. In Figma, use a `SECTION` with that name and place only the component's visual frames inside it; omit extra page titles, subsection headings, and explanatory text. In Markdown, use `## <Component name>` followed only by image embeds with concise alt text; add no prose, captions, lists, or metadata inside the section. Make a separate section for each component. Keep the editable Figma link, source links, captions if needed for the full documentation, exact configuration, dimensions, export scale, native scale, and verification result in the assembler handoff rather than the visual-only section. Report a missing source or inaccessible file precisely; do not label an unverified image complete.
