# Neutral Figma visual kit

For ordinary figures, instantiate the existing Figma kit first; do not rebuild this specification as a substitute for access. The following kit-creation instructions apply only when the user explicitly requests kit creation or setup.

The visual kit is a new page in a user-selected Figma design file. The page must be independently shareable under the file's permissions. Name the page and component set `Component Documentation Kit`. Create reusable editable templates for `Anatomy`, `Variants`, `States`, `Rule Comparison`, `Responsive Comparison`, `Truncation`, `Behavior`, `Product Example`, and `Positioning & Padding`. Use `Template` and `Locale` (`FA`, `EN`) as the only kit variant axes where variants are practical. A team's own component instances are supplied at use time. Never include a source component, asset, token, or style from another project in the shared kit.

Generated visual frames use English names in the form `<Component name> - <documentation type>`; for example, `FAB Menu - Anatomy`. Nested documentation frames add a descriptive role after the type. Do not rename layers inside source component instances.

| Family | Editable scaffold | Evidence before replacing the demo |
| --- | --- | --- |
| Anatomy | One stage, specimen slot, direct part labels, straight leaders, tight outlines, outside caption | Actual layer-to-part mapping and any optionality claim |
| Variants | One stage, repeatable specimen slots with names below | Actual variant axes, values, and example configurations |
| States | One stage, repeatable specimen slots with names below | Actual state values for the relevant configuration |
| Rule Comparison | Two stages, verdict headings, one caption per stage | A confirmed rule and one controlled correct/incorrect difference |
| Positioning & Padding | Explicit container boundary, specimen slot, requested red gap bands and full-opacity measurement labels | Confirmed container bounds, requested sides, and placement rule |
| Responsive Comparison | Two stages, captions, optional spacing or dimension guides | Confirmed conditions and changed behavior |
| Truncation | Two stages showing short and genuinely truncated content | Confirmed available width and truncation behavior |
| Behavior | One stage with ordered steps and short arrows, outside caption | Confirmed event and result; timing only if known |
| Product Example | One stage for an authorized product image, outside caption | Authentic context and a confirmed placement claim |

## Documentation defaults

- Canvas width: 960 logical px; fit height to content. Outer padding: 40 px on every side, including below the final caption. Default stage insets: 32 px on every side around the complete composition, including annotation extents. Retain approved destination insets when provided. Single stage width: 880 px. For two stages, use 428 px each with a 24 px gap. Use Auto Layout for every structural component, stage, specimen cell, and stage-caption column; let captions grow in height. Position only geometry-dependent overlays (leaders, outlines, dimension guides, and text inside a specimen) absolutely within an Auto Layout stage.
- Documentation stage: neutral light gray `#F3F4F6`. Chrome surface: white `#FFFFFF`. Text: near-black `#202124`. Annotation red: `#D92D20`. Behavior arrows: neutral gray `#667085`. These are independent kit colors, replaceable by the user's documentation theme. They never restyle source components.
- Documentation guide, leader, outline, measurement, and arrow strokes: 2 logical px. Use a 0 px outline gap and retain the target's displayed corner radii. Native component and icon strokes keep their source values.
- Anatomy labels use 16 px type with 24 px line height by default. Every label stays outside the whole specimen and its visible effects, while remaining inside the stage. Draw one straight horizontal or vertical leader attached to the actual target, with exactly 12 px between its other endpoint and the fitted text box. Side labels face the target and top/bottom labels are centered. Avoid numbered dots. Use [the callout placement procedure](../component-doc-visuals/references/anatomy-callouts.md) to calculate exterior clearance, comparable spans, collision handling, and post-export checks; its geometry defaults have one canonical source there.
- Outlines have no fill and a 2 px outside stroke. Their frame equals the exact displayed target bounds `(x, y, width, height)` with unchanged per-corner radii. A part outline follows that part's bounds, not the outer component's padding.
- Source specimens start at `nativeScale=1`. Enlarge uniformly only if a 960 px view shows that the native specimen is unreadable. Keep annotation type and line weights independent of specimen scale.
- Rule Comparison verdicts use **Bold (700)**, 16 px type with 24 px line height; explanations remain Regular. Use a solid green circle with a white check for Do and a solid red circle with a white cross for Don’t. Reuse the actual kit icons, never emoji or outlined substitutes. Center each icon/title group with an 8 px gap. In FA, put the correct panel on the right and the icon to the right of its title; in EN, put the correct panel on the left and the icon to the left of its title. Reorder whole panel groups so specimens and captions stay paired; never mirror native product UI to change documentation direction. Recheck icon/text bounds after applying the final font weight.
- Center the complete composition, including labels and guides. Put short captions 30 px below their stages. In Rule Comparison, place the verdict 30 px below the stage and its explanation 8 px below the verdict. Variants and States use exact source names directly beneath their specimens, without an extra outside caption.
- Place Variants and States names 24 px beneath their corresponding specimens. Use centered 14 px text with 24 px line height for captions and item names unless the destination file provides an approved documentation style.
- For dimensions, use one continuous line with 12 px perpendicular end caps, offset 32 px from the measured target, and put the value 12 px from the shaft. The shaft, both end caps, and numeric text must all use the same annotation red at full opacity; black numeric labels fail verification. Screen/container positioning gaps use editable red frames at 0.12 opacity only as defined in [Positioning & Padding](../component-doc-visuals/references/positioning-and-padding.md), never for width-only comparisons. Keep numeric labels outside translucent parents so they remain full-opacity red. Numeric labels follow `8 px` notation in both languages and use 14 px documentation type. Never invent measurements to fill a template.
- A reusable neutral touch indicator may mark a confirmed `Pressed` specimen or tap action: a 65 × 65 px circle at 0.30 opacity with its contact point inside the actual interactive target. Keep it separate from native content. Do not add it automatically to Hover, Enabled, Disabled, Loading, Selected, or keyboard Focus.
- Use a separate neutral backing for a source component that would disappear against the stage. Fit backing and padding to the actual component and the confirmed visual rule; do not alter native internals.
- Use Noto Sans Arabic for FA documentation labels and neutral example text, and Noto Sans for EN. Preserve source component typography and load its native fonts for supported text overrides. Load the available font styles before editing text; do not bundle font files. Check RTL shaping and mixed-direction identifiers in the rendered result.
- Variants and States specimen galleries use horizontal wrap. Keep each specimen and its exact source name together in a vertical auto-layout cell; let the gallery wrap to more rows and let the stage and output frame grow in height. Use the smallest readable specimen scale. For a generated page with many specimens, place the expanded output outside the fixed master component-set grid so later masters cannot overlap it.
- Keep explanatory prose and visible scale labels outside the gray stage. In-stage documentation text is limited to Anatomy part names/status, Variants and States names, and confirmed numeric measurements. Native specimen text remains inside its component.

These defaults are for documentation chrome. Inspect current Figma geometry and user edits before placing annotations. After export, perform a separate fresh Figma read to compare annotated bounds with the pre-export snapshot. If geometry moved, repair the generated annotation and export again. Check the actual image at intended display width.

The kit page should contain a short usage note, nine template families in FA and EN, a specimen placeholder in each, and a small neutral component example made only for demonstrating the kit. It must not claim any example behavior as the user's product policy. Share the Figma file or duplicate link according to the user's chosen access settings; a page URL alone inherits its parent file's permissions.

For the step-by-step build order, family-specific checks, and export verification procedure, read [build and verify](../component-doc-visuals/references/build-and-verify.md).


## Centered compositions and equal gray-stage padding

This rule applies to every template, with or without callouts or additional assets. Measure the union of all visible in-stage content: native specimens, separate backings, labels, leaders, measurement bands and values, icons, touch indicators, auxiliary assets, and visible stroke/shadow extents. Exclude the gray stage itself and captions outside it. A composition wrapper counts by its visible children, not its empty frame bounds.

All gray stages use a fixed height of **320 logical px**, bound to the Figma FLOAT token `size/stage-height`. This applies to all nine families and both locales. The complete output frame can grow for captions; the gray-stage height does not grow automatically.

Center the whole visible union horizontally and vertically. For stage `(sw, 320)` and union `(uw, uh)`, use horizontal inset `px = (sw - uw) / 2` and vertical inset `py = (320 - uh) / 2`. Left must equal right, and top must equal bottom. Horizontal and vertical insets need not match. This supersedes the earlier four-equal-sides formula that caused excessively tall templates. Preserve the output's separate 40 px outer padding.

Require at least the configured minimum inset (default 32 px). If the composition cannot fit, rearrange annotations or split the examples. Do not automatically enlarge the stage, shrink native content, or remove required labels. A larger stage requires an explicit user-approved exception, consistently applied to the affected comparison. Center a demonstrated product container and its annotations as one composition; preserve its internal component placement and measured gaps.

After export, independently read the actual four gaps and the stage height. Verify height `320 px`, left/right equality and top/bottom equality within 0.5 logical px. Checking Auto Layout settings alone is insufficient when overlays, text reflow, or effects alter visible bounds.

## Figma color token contract

Every kit-owned color must have a real Figma color-variable binding: fills, strokes, text fills (including mixed ranges), icon shapes, annotation bands, and any colored effects or gradient stops. A matching RGB/hex value or paint style without a variable binding is insufficient. Reuse the semantic variables in the `Documentation Kit` collection; create a clearly named semantic token only for a genuinely missing role. Preserve the native product component's own color bindings; do not retheme product content with documentation tokens.

Current semantic roles: `color/canvas`, `color/stage`, `color/surface`, `color/ink`, `color/annotation`, `color/arrow`, `color/border`, `color/border-subtle`, and `color/success`. White marks inside status icons use `color/surface`. Red gap bands bind `color/annotation` and retain effective opacity `0.12` (use band-frame opacity when variable binding resets paint alpha; keep labels as separate full-opacity siblings); measurement labels use the same token at full opacity. Transparent layers can have no paint; never add a visible fill just to attach a token.

Audit Cover, Templates, and Assets recursively after edits. Inspect binding IDs and resolved colors, not appearance alone, and render the result to catch incorrect alias resolution or black fallbacks. A final audit must report zero unbound kit-owned colors. Editor canvas backgrounds are workspace preferences, not exportable kit artwork.
