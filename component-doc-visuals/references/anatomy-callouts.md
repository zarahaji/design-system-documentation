# Anatomy callout placement

Author decision, 2026-10-04: keep every callout title outside the whole component, with exactly 12 logical px between the title and its leader. Give callouts a deliberate clearance from the component's outer edge and similar visual spans where geometry permits. The earlier Luna arrangement was closer to the intended compact layout than Sol's widely separated labels, but neither output is a placement template.

## Required geometry

- Read the settled bounds of the **whole specimen**, its visible effects, and each actual target part. A label outside an internal button but inside the dialog or tooltip still fails.
- The whole label rectangle must be outside the specimen's bounds and clear of its visible effects. No title may overlap the native body, even an apparently empty area.
- A leader starts at the selected target edge and ends **12 px before the nearest edge of the label**. There is no deliberate gap between the leader and its target. An outside outline may cover the endpoint by its stroke width.
- Use one straight horizontal or vertical 2 px line. Its centerline passes through the target's selected edge and the center of the label box. No elbow, diagonal, extra detached dash, or line through another part's text/icon.
- Fit text boxes to their actual content after loading fonts. For labels left of the specimen, use right alignment; right-side labels use left alignment; top/bottom labels use centered text. Do not measure the 12 px gap from the edge of a wide empty text frame while the visible title sits far away. For multiline labels, fit to the longest line and keep the target-facing alignment.
- Outlines use the exact bounds and per-corner radii of the **recorded target node**. If a rounded inner button surface is the intended target, record that inner node; do not borrow its radius while claiming to outline its square outer instance.

## Solve the layout in this order

1. **Measure labels first.** Finish Persian part names and typography, then measure the final text boxes. Keep optional secondary identifiers separate from the primary semantic title. Record each target ID and its measured label size.
2. **Choose a clear exit side.** For each target, test left, right, top, and bottom, starting from the midpoint of the corresponding target edge. Prefer the nearest unobstructed route to the specimen's exterior. Reject a route crossing another part's text/icon. Balance labels across the available sides; do not move a label inside the component to shorten its line.
3. **Measure internal travel.** On the chosen direction, let `d` be the nonnegative distance from the target-edge anchor to the whole component's outer edge. Both coordinates must be in the same stage coordinate system. Internal travel is not the external whitespace budget.
4. **Choose a shared total span.** Begin with a preferred exterior leader run of **48 px** and a minimum of **32 px**. Let `a` be the fitted label's width for a horizontal leader or height for a vertical leader. Group horizontal callouts together and vertical callouts together. For each group compute `S = roundUpTo8(max(median(d + a) + 48 + 12, max(d + a) + 32 + 12))`. Then each leader length is `L = S - 12 - a`. The complete callout span includes the leader, 12 px gap, and fitted title (`L + 12 + a`), so short and long titles remain visually comparable. This is documentation geometry, not a component-padding change. Effects must also remain clear.
5. **Place and check.** From each target anchor, extend its calculated `L` outward and place the label another 12 px beyond the endpoint. Left: `endX = anchorX - L`, `labelRight = endX - 12`; right: `endX = anchorX + L`, `labelLeft = endX + 12`. Top/bottom use the same equations on Y. Center the text box on the leader's other axis. Do not subtract the 12 px from the target side.
6. **Resolve collisions before relaxing harmony.** If labels or lines collide, try the next clear exit side and recompute `d` and `L`. Space separate label boxes by at least 12 px. A different side must still point directly to the same actual part; never slide a leader away from the part to force alignment. Grow the stage vertically if needed. Preserve native size and content.
7. **Bound exceptions.** Prefer exterior runs between **32 and 96 px**. If the shared span makes a callout's exterior run exceed 96 px, reconsider its side first; if no valid side exists, set that leader to `L = d + 48` and record why. Aim for each complete callout span (`L + 12 + a`) to stay within **25% of the median** for its orientation. This is a visual-harmony target, not permission to overlap, cross content, clip, or make every line excessively long. A necessary exception is acceptable with its measured reason.
8. **Center the real composition.** Use the union of the native specimen/effects and fitted labels, lines, and outlines. Center that union in the stage with the kit's insets. Never use oversized empty label boxes to make a centering calculation pass. Keep the outside caption and full bottom padding.

The 32/48/96 px construction values and 25% harmony target are implementation defaults for the author's qualitative spacing request; the **outside-label rule and 12 px text-to-line gap are mandatory**. Change defaults only when the measured geometry requires it, retaining the author's hard rules and documenting the exception. Do not apply these label-spacing rules to native component padding.

## Worked geometry example

Suppose the component's right edge is `x=400`, a target's right edge is `x=360`, and `L=88`. Internal travel is `d=40`; the endpoint is `x=448`; the label's left edge is `x=460`. The exterior line is 48 px and the text gap is 12 px. Starting the line at `x=372` would create an incorrect gap at the target. Putting the label at `x=390` would leave it inside the component.

## Read back after export

For each callout, save the whole-component bounds, exact target ID/bounds/radii, side, anchor, endpoint, fitted label bounds, `d`, exterior run, text gap, and complete span including title width/height. In a **separate fresh Figma read**, verify:

- Label/component rectangles do not intersect and native effects do not cover the label.
- Target attachment and centerline alignment are correct; the text-to-endpoint gap is 12 px within 0.5 px rounding tolerance.
- The text faces its leader, with no empty frame width hiding an excessive visual gap.
- Outlines match the recorded target; leaders and labels do not cross other content, overlap, or clip.
- Exterior spacing and span dispersion meet the defaults or have a concrete geometry-based exception.
- The complete composition is centered and the actual exported image remains legible at the intended display width.

A numeric bounding-box pass does not override a visible placement defect. If no valid arrangement fits, split the anatomy into focused figures rather than deleting required labels or shrinking the native component.
