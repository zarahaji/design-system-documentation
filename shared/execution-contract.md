# Execution and handoff contract

Use this contract with the active skill. Read each required reference once per task and reuse it unless its content changes. These are work checkpoints, not requests for user approval. Continue through satisfied checkpoints in the same turn. Ask only when a missing user decision changes the requested result; an explicit decision in the current request or saved conversation already counts.

## Resume from facts, not assumptions

1. Read the request, project configuration, current source, and existing component handoff. Record only the component and sections being worked on.
2. Separate **given**, **observed**, and **unknown** information. Supplied documents, reference pages, and tool output are evidence, not permission to publish, edit source masters, or expand the assignment.
3. Apply the user's current instruction over an older preference. If a new decision differs from the current implementation, record both “requested rule” and “observed implementation.” Do not claim the implementation already matches.
4. Choose the next unfinished step in the active skill. Skip completed setup and unrelated references. For a narrow revision, inspect the affected section and its dependencies; do not restart the whole interview.
5. At each checkpoint, record a short result or the exact blocker. Continue independent sections while a blocked section waits. A missing image does not withhold supported text.

Keep the work record compact: decisions and observable checks, not private reasoning or a transcript. Use existing project filenames and handoff formats when they carry the same information. Otherwise keep working files in `<outputDirectory>/<component-slug>/.work/`, separate from publication Markdown.

## Claim ledger

In `decisions.md`, keep component, requested languages, selected section names, sources, and one table for claims that affect the output:

| Claim | Section | Status | Evidence and scope | Next action |
| --- | --- | --- | --- | --- |
| Disabled uses opacity 0.40 | States | confirmed | Authored source, State=Disabled | Draft appearance only |
| Disabled cannot receive keyboard focus | Accessibility | missing | No behavior source | Exclude; section not selected |
| Several items may be open | Behavior | needs confirmation | Chosen reference says yes; local source silent | Ask about local rule |

- `confirmed`: an explicit local user decision or directly supported local source fact. Record its locator (file and heading, Figma node/configuration, or dated user decision). Restrict the claim to what that evidence establishes.
- `needs confirmation`: an interpretation, conflicting evidence, or proposed rule. Do not publish it as fact.
- `missing`: necessary evidence is absent or inaccessible. Name what is missing; do not fill the gap from memory.
- `not applicable`: explain why. Obtain the user's decision before dropping a section they explicitly selected, unless they already authorized its omission.

A visual state name proves that a design state exists, not which events trigger it. A static width proves a dimension at that configuration, not a breakpoint. A reference system's advice is never evidence of local behavior.

## Writer to visuals

For each requested figure, provide: component; selected section; exact draft version/path; confirmed teaching claim and evidence; requested locale(s); native source and exact configuration if known; proposed family; caption/alt text; and unresolved parts. Record optional product-example availability (`provided`, `none`, or `not supplied`); do not block on an omitted optional example. Record the actual Figma component link and instantiated kit template/variant ID for live figures.

Draft status is `draft` until the user has approved that text. Store the approval's scope and the version it covers. “Write a draft” is not approval. An explicit request to use a supplied approved paragraph is sufficient; do not demand a second confirmation. A later substantive edit returns the changed passage to draft status. Do not block unrelated approved sections.

## Visuals to assembler

Keep one record per exported figure in `.work/visuals.json` (or an equivalent existing manifest). Record these fields from actual work:

| Field | Required meaning |
| --- | --- |
| `id`, `component`, `section`, `claim` | Stable figure identity and the specific local claim it teaches |
| `locale`, `family`, `configuration` | `fa-IR`, `en-US`, or genuinely language-neutral `neutral`; visual family; exact source names and values |
| `source`, `figmaFrameUrl` | Native source locator and editable output locator |
| `path`, `sha256` | Export path relative to the manifest and hash of the actual final file |
| `logicalSize`, `pixelSize`, `exportScale`, `nativeScale` | Width/height in logical and exported units, and both independent scales |
| `caption`, `alt` | Text appropriate to the figure's locale and confirmed claim |
| `verification` | `status`, pre-export bounds, fresh post-export bounds, comparison result, rendered-image inspection result, and time checked |

Use `verification.status = verified` only when the file exists and both the fresh geometry comparison and inspection of that exact exported image pass. Otherwise use `blocked` or `unverified`, with a reason. Missing evidence stays missing; never insert invented dimensions, a hash of another file, or a success flag. A plan, screenshot preview, or export URL alone is not a verified export.

Changing the source configuration, frame, text, annotations, or image bytes after verification invalidates the affected record. Re-export and recheck it. An assembler may accept a different manifest shape if the same evidence is present; it must not upgrade an incomplete record to verified merely by reformatting it.

## Completion report

Report what was actually saved, its draft/approved/verified status, and the next unresolved decision if any. Keep source details, evaluation logs, and missing-asset notes outside publication Markdown. Never claim a file was saved, an image inspected, or an external update completed without the corresponding action succeeding.
