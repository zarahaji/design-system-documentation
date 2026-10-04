# Design System Documentation

Research, write, illustrate, and assemble design-system component documentation with three Codex skills. Persian-first, with optional English output and editable Figma visuals.

![Eight component documentation visual families](assets/kit-overview.svg)

## What is included

| Skill | What it does |
| --- | --- |
| [`component-doc-writer`](component-doc-writer/SKILL.md) | Reads your sources, asks about missing rules, and drafts the sections you choose. |
| [`component-doc-visuals`](component-doc-visuals/SKILL.md) | Builds editable Figma illustrations and checks their geometry and exported images. |
| [`component-doc-assembler`](component-doc-assembler/SKILL.md) | Combines approved text and verified images into a Markdown package. |

Your component sources and confirmed decisions establish the rules. External design systems help identify questions; their policies are never automatically adopted.

## Requirements

- Codex with local skill support and access to the project files.
- Readable component sources: design files, code, or authored specifications.
- For visuals: an available Figma connection capable of inspecting and editing nodes and exporting images, an editable destination, and the required `figma-use` skill. Its prerequisites must also be available for the operations you request. Having a Figma browser tab open does not make these tools available to Codex.
- For package checks: Python 3.10 or later. The bundled checker and tests use the standard library.

Text-only writing and Markdown assembly do not require a Figma connection.

## Install

Download or clone this repository, then copy these four folders together into your target project's `.agents/skills/` directory:

```text
.agents/skills/
├── component-doc-writer/
├── component-doc-visuals/
├── component-doc-assembler/
└── shared/
```

Keep `shared` beside all three skill folders: their relative references depend on this layout. If the destination already has a `shared` folder, check for conflicting filenames before merging. Only these four folders are needed at runtime; repository maintenance files are not skill instructions.

Copy [`shared/project.example.json`](shared/project.example.json) to `component-docs.json` in the target project, or let the writer create it during setup. Save real source URLs, identifiers, language preferences, and the output directory there. Keep that configuration outside this public repository.

## Start with a component

```text
Use $component-doc-writer to document our Accordion.
The component source is in source.md. Help me choose the sections first.
```

The writer first settles the sources, language, optional bilingual output, and interview references. It then shows a section list, investigates the selected sections, and asks only about relevant unknowns. Drafts and working evidence are saved separately.

When you have confirmed text and want illustrations:

```text
Use $component-doc-visuals to illustrate the confirmed Anatomy section.
Use the native component and the destination linked in component-docs.json.
```

The visual skill asks once about a product-screen reference, preserves native component styling, and checks exported images. It supports Anatomy, Variants, States, Rule Comparison, Responsive Comparison, Truncation, Behavior, and Product Example.

To assemble the final package:

```text
Use $component-doc-assembler to combine the approved drafts and verified
images into the selected Persian and English Markdown documents.
```

If an image is unavailable, the assembler delivers the text and a separate missing-asset note without leaving a broken image link.

## Visual kit

The [kit specification](shared/visual-kit-spec.md) defines editable documentation templates at 960 logical px wide, with FA and EN layouts. It controls annotations and framing, while product components retain their native appearance.

An [editable Figma kit](https://www.figma.com/design/vuz0Ey8cw38miujLZ3kP1d/Untitled?node-id=3-2) is available subject to the file's sharing permissions. Set `visualKit.pageUrl` to your project's copy. If the link is unavailable, the visual skill can build the templates from the specification in your chosen editable file; working Figma tools are still required. Font files are not bundled.

## Output

- Selected sections as Markdown, in Persian, English, or separate files for both.
- A separate evidence and decisions note.
- When requested and verified: image exports, an editable Figma reference, and a visual handoff with configuration and verification details.

Visual-only delivery uses one section per component containing image embeds. Full documentation places figures alongside their corresponding text.

## Validation status

Local evaluations cover skill selection, a four-turn interview, bilingual writing, missing-source handling, and Markdown assembly. Repeated runs exposed a Persian opacity wording issue; the writing guide now distinguishes opacity from transparency, and a fresh bilingual regression run passed. Live Figma creation, export, and post-export geometry verification remain unverified in this evaluation environment.

See [testing and limitations](docs/testing.md) for scope and commands. Package checks are not proof of visual correctness or publication rights.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance and release checks. Instructions and repository assets are distributed under the [MIT license](LICENSE). Linked Figma files, fonts, and user-supplied product assets require their own permission review.
