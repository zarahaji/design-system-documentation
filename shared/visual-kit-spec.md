# Neutral Figma visual kit

The visual kit is a new page in a user-selected Figma design file. The page must be independently shareable under the file's permissions. Name the page and component set `Component Documentation Kit`. Create reusable editable templates for `Anatomy`, `Variants`, `States`, `Rule Comparison`, `Responsive Comparison`, `Truncation`, `Behavior`, and `Product Example`. Use `Template` and `Locale` (`FA`, `EN`) as the only kit variant axes where variants are practical. A team's own component instances are supplied at use time. Never include a source component, asset, token, or style from another project in the shared kit.

Generated visual frames use English names in the form `<Component name> - <documentation type>`; for example, `FAB Menu - Anatomy`. Nested documentation frames add a descriptive role after the type. Do not rename layers inside source component instances.

| Family | Editable scaffold | Evidence before replacing the demo |
| --- | --- | --- |
| Anatomy | One stage, specimen slot, direct part labels, straight leaders, tight outlines, outside caption | Actual layer-to-part mapping and any optionality claim |
| Variants | One stage, repeatable specimen slots with names below | Actual variant axes, values, and example configurations |
| States | One stage, repeatable specimen slots with names below | Actual state values for the relevant configuration |
| Rule Comparison | Two stages, verdict headings, one caption per stage | A confirmed rule and one controlled correct/incorrect difference |
| Responsive Comparison | Two stages, captions, optional spacing or dimension guides | Confirmed conditions and changed behavior |
| Truncation | Two stages showing short and genuinely truncated content | Confirmed available width and truncation behavior |
| Behavior | One stage with ordered steps and short arrows, outside caption | Confirmed event and result; timing only if known |
| Product Example | One stage for an authorized product image, outside caption | Authentic context and a confirmed placement claim |

## Documentation defaults

- Canvas width: 960 logical px; fit height to content. Outer padding: 40 px. Single stage width: 880 px. For two stages, use 428 px each with a 24 px gap. Use Auto Layout for every structural component, stage, specimen cell, and stage-caption column; let captions grow in height. Position only geometry-dependent overlays (leaders, outlines, dimension guides, and text inside a specimen) absolutely within an Auto Layout stage.
- Documentation stage: neutral light gray `#F3F4F6`. Chrome surface: white `#FFFFFF`. Text: near-black `#202124`. Annotation red: `#D92D20`. Behavior arrows: neutral gray `#667085`. These are independent kit colors, replaceable by the user's documentation theme. They never restyle source components.
- Documentation guide, leader, outline, measurement, and arrow strokes: 2 logical px. Use a 0 px outline gap and retain the target's displayed corner radii. Native component and icon strokes keep their source values.
- Anatomy labels use 16 px type with 24 px line height by default. Draw a single straight horizontal or vertical leader for each label; leave 12 px between the text box and the line. Side labels face the target and top/bottom labels are centered. Avoid numbered dots. Align the whole label box to the leader axis, and keep every annotation inside the stage.
- Outlines have no fill and a 2 px outside stroke. Their frame equals the exact displayed target bounds `(x, y, width, height)` with unchanged per-corner radii. A part outline follows that part's bounds, not the outer component's padding.
- Source specimens start at `nativeScale=1`. Enlarge uniformly only if a 960 px view shows that the native specimen is unreadable. Keep annotation type and line weights independent of specimen scale.
- Center the complete composition, including labels and guides. Put short captions 30 px below their stages. In Rule Comparison, place the verdict 30 px below the stage and its explanation 8 px below the verdict. Variants and States use exact source names directly beneath their specimens, without an extra outside caption.
- Place Variants and States names 24 px beneath their corresponding specimens. Use centered 14 px text with 24 px line height for captions and item names unless the destination file provides an approved documentation style.
- For dimensions, use one continuous line with 12 px perpendicular end caps, offset 32 px from the measured target, and put the value 12 px from the shaft. For spacing, use the annotation red at 0.12 opacity as an area. Numeric labels follow `8 px` notation in both languages and use 14 px documentation type. Never invent measurements to fill a template.
- A reusable neutral touch indicator may mark a confirmed `Pressed` specimen or tap action: a 65 × 65 px circle at 0.30 opacity with its contact point inside the actual interactive target. Keep it separate from native content. Do not add it automatically to Hover, Enabled, Disabled, Loading, Selected, or keyboard Focus.
- Use a separate neutral backing for a source component that would disappear against the stage. Fit backing and padding to the actual component and the confirmed visual rule; do not alter native internals.
- Use Noto Sans Arabic for FA examples and Noto Sans for EN examples. Load the available font styles before editing text; do not bundle font files. Check RTL shaping and mixed-direction identifiers in the rendered result.
- Variants and States specimen galleries use horizontal wrap. Keep each specimen and its exact source name together in a vertical auto-layout cell; let the gallery wrap to more rows and let the stage and output frame grow in height. Use the smallest readable specimen scale. For a generated page with many specimens, place the expanded output outside the fixed master component-set grid so later masters cannot overlap it.
- Keep explanatory prose and visible scale labels outside the gray stage. In-stage documentation text is limited to Anatomy part names/status, Variants and States names, and confirmed numeric measurements. Native specimen text remains inside its component.

These defaults are for documentation chrome. Inspect current Figma geometry and user edits before placing annotations. After export, perform a separate fresh Figma read to compare annotated bounds with the pre-export snapshot. If geometry moved, repair the generated annotation and export again. Check the actual image at intended display width.

The kit page should contain a short usage note, eight template families in FA and EN, a specimen placeholder in each, and a small neutral component example made only for demonstrating the kit. It must not claim any example behavior as the user's product policy. Share the Figma file or duplicate link according to the user's chosen access settings; a page URL alone inherits its parent file's permissions.
