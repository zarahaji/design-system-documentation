# Positioning & Padding

Read when the supplied paragraph or product example teaches a component's placement or padding relative to screen/container edges. Use the dedicated `Template=Positioning & Padding` variant with the requested `Locale=FA` or `Locale=EN`. This ninth family is separate from Responsive Comparison.

## Choose the measurement

- Component width/height or responsive size comparison only: use capped dimension lines and numeric text, both full-opacity annotation red. Do not add red area bands.
- Placement or padding to screen/container edges: use editable low-opacity red gap frames for the requested sides only.
- Both claims: record separate dimension and positioning measurements. Include both only when each teaches a supplied claim; split figures if their annotations collide.

## Build in order

1. Inspect the live native component and the supplied screen/container evidence. Record the intended reference edge: viewport, content area, safe area, or another explicitly named boundary. Never treat the gray documentation stage as a product screen. Ask for missing boundary evidence rather than inventing padding or breakpoints.
2. Instantiate `Template=Positioning & Padding` with the requested locale from the actual Figma kit. The template includes horizontal-only and four-side demonstrations. Keep only the example and sides required by the claim; the demo’s 48 px values are not product rules. If this variant is missing in an older project copy, request an updated kit rather than silently routing to Responsive Comparison. Record the template and instance IDs. Adapt only the generated documentation wrapper, preserving native instances and masters. Name the output `<Component name> - Positioning & Padding`.
3. Record which sides the paragraph requests: left, right, top, bottom, or an explicit combination. Convert logical start/end to physical sides using the actual UI direction. Do not automatically shade all four sides.
4. Set the supported native configuration and let layout/reflow settle. Read the component and confirmed container bounds in the same logical coordinate system. Measurements describe actual displayed geometry, not old master coordinates.
5. Calculate the rectangles below. Create a separate editable `FRAME` per requested positive gap. Use the kit's annotation-red fill with effective opacity exactly `0.12`, no stroke, and no native-component restyling. For example, use frame opacity `1` and fill opacity `0.12`. Keep any numeric label as a separate sibling with full-opacity annotation-red text. Do not put it beneath a translucent ancestor.
6. Set each label from the measured gap using English digits and `px`, including in Persian figures. Keep labels readable without covering native content. If a gap is too narrow for its label, put the measurement label outside the band with a clear association; do not enlarge the band or fake its value. Explanatory prose belongs in the outside caption.
7. Export, make a separate fresh Figma read, and inspect the actual exported file following [build and verify](build-and-verify.md). If native layout changes, recompute all affected bands and labels before exporting again.

## Exact band geometry

Let the component bounds be `(sx, sy, sw, sh)` and the confirmed container bounds be `(cx, cy, cw, ch)`. These must be axis-aligned in the same coordinate system. For transformed nodes, first convert to the relevant container coordinates; do not apply these formulas to unrelated coordinate spaces.

| Requested side | Frame x | Frame y | Frame width | Frame height |
| --- | --- | --- | --- | --- |
| Left | `cx` | `sy` | `sx - cx` | `sh` |
| Right | `sx + sw` | `sy` | `cx + cw - (sx + sw)` | `sh` |
| Top | `sx` | `cy` | `sw` | `sy - cy` |
| Bottom | `sx` | `sy + sh` | `sw` | `cy + ch - (sy + sh)` |

Left/right bands have exactly the component's displayed height. Top/bottom bands have exactly its displayed width. They fill only the measured gap: no screen-wide shading, corner fill, inset into the specimen, or decorative extension. A zero gap has no filled rectangle; a negative gap indicates overlap or an incorrect reference, not padding. Resolve it rather than taking an absolute value.

Example: a 280 × 240 component at `(40, 120)` inside a 360 × 640 screen at `(0, 0)` has left/right bands 40 × 240, top band 280 × 120, and bottom band 280 × 280. If only horizontal padding is requested, create only the two 40 × 240 bands and `40 px` labels. This example illustrates arithmetic; it does not establish a product spacing rule.

## Verification record

Save the claim, container identity/reference edge, requested sides, component/container bounds, and each band/label ID. For each band, record the calculated rectangle, actual rectangle, gap value, color, and effective opacity. For dimensions, record shaft/end-cap colors and text color separately. After export, verify:

- Requested sides exactly match the created bands; width-only comparisons have none.
- Actual bands match the formula within 0.5 logical px rounding and meet the component edges without overlap.
- Component configuration and native appearance are preserved.
- Band opacity is `0.12`; labels and dimension lines/caps use the same annotation red at effective opacity `1`.
- Labels match measured gaps and remain legible in the final image.

A red line with black text fails. A red band with translucent numeric text also fails. Fix generated annotations and repeat export plus fresh-read checks; do not change the source component to make the annotation fit.
