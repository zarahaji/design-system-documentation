# Shared setup and evidence

Use one `component-docs.json` in the user's project. If not already loaded, read [execution and handoff](execution-contract.md) for resuming work, evidence status, and approval scope. Do not write private URLs or identifiers into this skill set. Start with a short intake for foundations or tokens, component sources, and primary language. Then ask about interview references as the final setup decision:

- Link or path for foundation and tokens; a readable reference is enough.
- Figma link to the specific component node, plus the component name. Reuse a previously supplied link. Code and authored specifications supplement the Figma source. For visual work, also require the paragraph to illustrate; a product example is optional unless a specific placement claim needs its container evidence.
- Primary language: Persian (`fa-IR`, default) or English (`en-US`). The default output is one Persian document. Ask whether each component should also receive an English document. Store the choice; do not ask again for every component unless the user changes it.
- Open design systems to consult during the interview. If the user has no preference, offer Material Design, Uber Base, IBM Carbon, and Microsoft Fluent as a short starting set and wait for their selection or confirmation. Do not treat the suggestions as preapproved.

Resolve what each supplied link permits. A link may be inaccessible; ask for the minimum missing evidence rather than guessing. User statements and component sources establish local behavior. External design systems help formulate interview questions and compare documentation approaches; they do not establish the user's product rules.

## Efficient reference use

For each selected reference system, look for the closest relevant component page and extract only the topics that could change the current interview. Keep a compact note with source URL, page title, date checked, and up to five useful questions or decision points. Reuse that note for subsequent sections or components while the source remains relevant. Read a full page only when a specific unresolved issue requires it. Do not quote large passages or fetch every reference for every question. If a reference cannot be read, continue with other evidence and mark that limitation.

During the component interview, make a compact evidence table with `confirmed`, `needs confirmation`, `missing`, or `not applicable`. Batch related missing questions. Cite the component source in working notes. Keep published prose self-contained and free of unsupported claims. Keep tool results and handoffs brief: summarize only decisions, source URLs, unresolved questions, and required identifiers; avoid copying full pages, large Figma node trees, or repeated conversation history.

## Missing values and prior decisions

- Read existing configuration and the current request before asking. A supplied source, selected sections, language choice, reference choice, or “no product screen” answer must not be requested again.
- A missing or null field is unknown. An explicitly confirmed empty list can mean “none”; do not conflate these states.
- New configurations use `interviewReferencesConfirmed`: `false` for an unanswered template and `true` after the user chooses systems or declines external references. Save an explicit decline as `interviewReferences: []` plus `interviewReferencesConfirmed: true`.
- For older saved configurations without this flag, preserve an existing reference choice, including an empty list, unless the record is known to be an unconfirmed example. Do not invalidate an existing project merely because this field is new. A newer explicit request overrides the saved choice.
- If primary language is unspecified, propose Persian as the default and ask once whether English is also needed. An explicit English-only or bilingual request settles the choice immediately.
- If foundations are unavailable, record the limitation and ask only when a selected claim depends on them. Supported component appearance can be documented without inventing tokens or blocking on unrelated foundation files.
- If output location is unspecified, use the configured location, or the example's default location when creating a configuration; report the chosen path. Do not add an approval round just for an ordinary local output path.
- A new local rule that contradicts an older source is a documented decision, not proof the source has been updated. Keep the distinction in working evidence and ask which description belongs in the selected document when the intended scope is unclear.
