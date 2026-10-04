# Preserve source identifiers mechanically

Read when selected draft claims contain source properties, variants, states, configuration values, or literal example content. This check supports the claim ledger; it does not prove the source facts or behavior.

## Before drafting

1. From the actual source, copy all identifiers and supplied example literals in the selected-section inventory into `.work/identifiers.json`. Do not normalize them in your head. Keep raw property keys in `properties`; put exact variant/state/configuration identifiers in `exact`; put literal example content in `literals`. All listed items must be used in each corresponding draft. Build this inventory from the source before the draft, not from whichever items happened to survive in your draft. Include an authored example literal when its associated property is part of the selected Implementation content; keep its exact bytes. Exclude items only for a recorded scope reason, such as an unselected section or an explicit request to omit examples.
2. For example, a source with two properties and one literal may produce:

```json
{
  "properties": ["Label#12:34", "Version#beta"],
  "exact": ["Enabled", "Disabled", "Stable"],
  "literals": ["Ticket#12:34"]
}
```

3. Resolve the helper relative to this skill's installed folder. With Python 3 available, run:

```sh
python3 <skill-folder>/scripts/check_identifiers.py <work-dir>/identifiers.json --map-only
```

The map is `Label#12:34 → Label` and `Version#beta → Version#beta`. Only a terminal numeric binding suffix is removed. Never split every name at `#`.

## While drafting

Copy only the map's **public** property names into Markdown code spans. Write exact identifiers/configurations in code spans as well; preserve literal text exactly. Raw binding keys and explanations of the cleanup belong in working evidence, even when the selected section is Implementation.

Correct publication: “The string property `Label` is available.”

Incorrect publication: “The public property `Label` has raw key `Label#12:34`.”

Do not add the raw key as a parenthetical, source note, table column, or explanatory sentence. The user may explicitly request API binding documentation; record that exception and retain the requested keys rather than applying this publication cleanup blindly.

## Check the saved drafts

Run the helper on the actual saved draft files, for example:

```sh
python3 <skill-folder>/scripts/check_identifiers.py <work-dir>/identifiers.json <draft.fa.md> <draft.en.md>
```

An exit code of 0 passes the mechanical check. Any reported missing public name, changed exact identifier, changed literal, or leaked raw key must be corrected in all affected languages; rerun the check before handoff. Never remove an item from the input manifest just to make a failed check pass. Change that manifest only when the selected claims or source actually change.

For language-specific examples, keep separate manifests for the actual intended content. If Python or shell execution is unavailable, compare the same raw/public table manually against saved drafts and report that the mechanical check was unavailable. Do not block supported drafting on installing a dependency or claim that a manual comparison was a script pass. The helper needs only Python's standard library.
