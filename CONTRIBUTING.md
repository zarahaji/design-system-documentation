# Contributing

This repository contains three runtime skills and their shared references. Keep component rules grounded in the user's project, preserve exact authored identifiers, and keep working evidence separate from published prose.

## Local checks

From the repository root:

```sh
python3 scripts/check_package.py . --release
python3 -m unittest discover -s tests -v
```

The checker verifies required skill metadata, local links, JSON and SVG syntax, and basic release-license requirements. It skips `.git` and Python bytecode caches. It does not inspect Git history, validate live Figma output, or prove legal ownership. Add project-specific text checks with repeated `--forbid` arguments when relevant.

The GitHub Actions workflow runs these same commands. It requires no API credentials and does not invoke a paid model or modify Figma.

## Behavior changes

Use isolated test projects. Exercise explicit and implicit invocation, unrelated requests, missing configuration, bilingual drafting, unresolved rules, unavailable images, and a multi-turn interview. Compare outputs with the authored facts and selected scope, rather than requiring identical wording. When testing visuals, use an authorized test destination and preserve source masters.

See [testing and limitations](docs/testing.md). Keep raw model traces, private project configuration, source files, and generated client documentation out of this repository.

## Before publishing

- Inspect the actual staged files and any Git history for private URLs, credentials, local paths, internal names, and product-specific assets. Check binary content and metadata separately.
- Run the checks above. If Codex's full skill validator is available, run it on each skill as well; the package checker only checks a subset of metadata rules.
- Verify that all runtime references ship with the four installable folders and that the skills work without access to the original author's organization.
- Confirm rights to distribute the instructions and assets, and verify the copyright holder and year in `LICENSE`.
- Check linked Figma files' permissions and distribution rights separately. A valid URL does not establish access or permission to redistribute.

Publication checks are maintenance work, not steps in the component-documentation workflow.
