# Build and verify one documentation figure

Read after selecting a confirmed claim and before planning live geometry or writing Figma. Numeric defaults live in [the kit specification](../../shared/visual-kit-spec.md); read its current values rather than copying an old example's coordinates. Explicit user decisions and approved destination styles override neutral defaults for documentation chrome, never the native product source.

## Route the claim

| What must the reader learn? | Family | Required evidence | Do not substitute |
| --- | --- | --- | --- |
| Name and location of parts | Anatomy | Actual target layers and part mapping | Imagined internals or a raw property key as the primary FA label |
| Available configurations | Variants | Live axes, values, valid configurations | A single baseline called complete coverage |
| State appearance | States | Actual states for the chosen configuration | Invented triggers or focus behavior |
| One correct/incorrect distinction | Rule Comparison | A confirmed rule and one controlled difference | Multiple differences that obscure the lesson |
| What changes under a condition | Responsive Comparison | Confirmed condition and behavior | Invented breakpoints from static widths |
| Gaps to screen/container edges | Positioning & Padding | Confirmed container bounds, requested sides, and placement rule | Width-only comparison with decorative gap bands |
| Where and how content shortens | Truncation | Confirmed text behavior and available width | Manually typed ellipsis as proof of truncation |
| Event followed by a result | Behavior | Confirmed event and resulting state | Timing or gestures inferred from state names |
| Placement in a real product | Product Example | Authorized context and confirmed placement | A screenshot passed off as editable reconstruction |

If several claims need different families, split them into separate figures. If the required evidence is missing, ask only for that evidence or report the blocked family; continue other grounded figures.

## Construct in this order

1. **Inspect existing output.** Read the destination, matching frames, and recent user edits. Reuse the approved kit and known output frame where appropriate. Make one authorized figure, not duplicate pages every run.
2. **Instantiate.** Instantiate the actual kit component/variant for the family and locale, then the native component. Record the source template identity and generated instance ID. Do not redraw a template from scratch. Only the generated documentation wrapper may be detached for adaptation; the native specimen stays an instance. Set each property with the exact source key/value; read back the resulting configuration. Keep a baseline of native size, styling, and relevant child structure for later comparison.
3. **Set content and fonts.** Load available fonts before editing documentation text. Use the kit's locale fonts for documentation labels and neutral example text; preserve native typography unless editing a supported text property requires its source font. Never silently replace a missing native font. Use only supported instance overrides; do not restyle or detach native parts.
4. **Lay out cells.** Give each specimen and exact source name its own vertical Auto Layout cell. Measure both before calculating cell width. Keep their canonical gap, center alignment, and non-truncated names. Wrap the gallery when the next cell plus gap exceeds usable stage width. Grow the stage and output height rather than compressing specimens or names.
5. **Place overlays last.** Wait for native layout to settle and read actual displayed target bounds. Convert all bounds to the stage's coordinate system before using them. Use displayed geometry, not source-master coordinates or the last component's numbers. An outline's frame equals the target bounds; its stroke lies outside. Preserve per-corner radii and account for outside stroke/effects when checking containment. Leaders attach to the intended part without crossing content; keep text boxes clear.
6. **Center the whole composition.** Compute the union of specimen, labels, leaders, outlines, measurement guides, and effects. Center that union in the stage. Use equal stage insets and the canonical output padding; let the stage grow vertically if the union does not fit. A caption remains outside the stage with its full measured text height plus bottom padding. Centering only the specimen while labels hang off one side fails this step.
7. **Read back.** Check the actual resulting frame tree, Auto Layout settings, native configuration, and bounds. Keep structural frames in Auto Layout. Absolute positioning is reserved for geometry-dependent overlays and specimen text, not whole layout columns.

For axis-aligned stage coordinates: `localX = displayedX - stageX` and `localY = displayedY - stageY`. For a scaled or rotated ancestor, use the inverse stage transform; do not subtract absolute coordinates as though scale were one. Compare pre/post bounds in the same coordinate system.

If content does not fit horizontally, first move annotation labels, wrap cells, or split figures while retaining the claim. Do not shrink a native component or delete labels to conceal overflow. If no compliant layout fits the canonical width, explain the conflict and settle a wider-format exception with the user.

## Family-specific checks

- **Anatomy:** follow [callout placement](anatomy-callouts.md), including its measurement record and fresh-read checks. Every label maps to a real part ID and stays outside the whole component; FA primary labels are semantic Persian. Leaders attach to targets, maintain a 12 px text gap, and use comparable spans with measured exterior clearance. Outline bounds and radii match the exact recorded target.
- **Variants / States:** each requested value is represented in the coverage map; each name belongs to the immediately paired specimen; long names wrap without truncation. Keep native styling and the canonical specimen/name gap.
- **Rule Comparison:** verify the kit’s solid verdict icons, Bold headings, locale-specific icon order and panel order; see the canonical kit specification. Check for reflow or icon/text overlap after setting the font weight. Both sides share configuration and content except the confirmed controlled difference. State the rule in outside captions. Use a supported instance change or separate documentation overlay; if the wrong example requires forbidden native edits, report that limitation.
- **Positioning & Padding:** execute [the gap-band procedure](positioning-and-padding.md). Check requested sides, container reference, frame geometry, 0.12 fill opacity, and full-red numeric siblings.
- **Responsive / Truncation:** record the actual width/configuration for each side and compare it to the confirmed behavior. The example must demonstrate the claim, not just label it. Every dimension shaft, end cap, and numeric label is full-opacity annotation red. Read back both stroke and text fills after export. Width-only responsive comparisons contain no positioning bands.
- **Behavior:** sequence order and arrows match the confirmed event/result. Add a touch marker only for confirmed tap actions or Pressed examples, with its hotspot inside the interactive target.
- **Product Example:** preserve the difference between a permitted contextual screenshot and an editable example. Rebuild only the requested editable part; never embed a screenshot as a substitute for it.

## Verification sequence — repeat after a repair

1. **Snapshot before export:** record output logical dimensions, native configuration, subject bounds, target part IDs/bounds, annotation bounds, corner radii, and relevant native styling. Check all visual extents stay within their intended frames, including strokes, shadows, text, and captions.
2. **Export:** export the entire composed output frame. Save the actual image and record export scale. Do not substitute a native-component-only export or an editor screenshot.
3. **Fresh read after export:** make a new Figma read in a separate call after export completes. Re-read the same node IDs and configurations. Reusing the earlier response is not a new read.
4. **Compare:** use the same units and coordinate system. Subject and target bounds must match within 0.5 logical px of numeric rounding; configuration, native styling, part identity, and corner treatment must be unchanged. This tolerance does not permit visible misalignment, clipping, or an outline gap. If geometry drifted, reposition generated annotations from the new bounds and restart at step 1.
5. **Inspect the exported file:** open the actual image at intended Markdown width (normally the canonical canvas width). Check text readability and RTL shaping, exact names, line breaks, contrast, pairing, clipping, consistent padding, caption clearance, and annotation alignment. If it cannot be opened, mark it unverified. Reading SVG/XML or a success response alone is not visual inspection.
6. **Record:** measure actual pixel width/height, compare to logical size × export scale allowing raster rounding, hash the saved bytes, and write both check results into the handoff. The final hash identifies the inspected image. Any later edit invalidates this verification.

Repair only the failing generated figure; preserve unrelated user edits and native masters. Stop after two repair passes for the same defect and report the evidence needed to proceed. A dry-run plan can exercise routing and stop conditions but never proves live Figma creation or export quality.
