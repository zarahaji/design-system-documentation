---
name: component-doc-writer
description: Research and write evidence-based design-system component documentation through a short setup, reference-informed gap interview, section checklist, and Persian-first or bilingual Markdown drafts.
---

# Component Doc Writer

Write documentation for one component at a time. Read [shared setup and evidence](../shared/setup-and-evidence.md) and [section choices](../shared/sections.md). For Persian output, read [the full Persian guide](../shared/persian-writing.md) before drafting.

## Setup once per project

Find `component-docs.json` in the user's project. If it is absent or incomplete, ask for foundation/token sources, component sources, primary language, and whether every component needs both Persian and English documents. Then ask which open design systems to use during the interview. Use [the example configuration](../shared/project.example.json) as a shape, not as evidence. If references are unspecified, offer the shortlist in the shared setup guide and wait for a selection or confirmation before using them in the interview. Ask again only when the project preference changes.

## Scope before interview

Inspect available component source first. Show the user [the section choices](../shared/sections.md), each with its short purpose, and let them choose which sections to document. If the conversation supports a real multi-select control, use it; otherwise show a readable multiline list and ask for section names. Never use Markdown task-list marks as if they were clickable controls, and never squeeze the choices into one form question or paragraph. Confirm the selected set before drafting. If a selected section appears inapplicable, say why and let the user decide. Keep this step compact; do not conduct the full interview yet.

## Evidence and interview

Inspect the component's authored properties, variants, states, anatomy, layout, and existing usage notes. Separate observed design facts, confirmed behavior, and unknown rules. Compare only the user's chosen reference systems through compact, reusable notes as described in the shared setup guide. Ask questions only about relevant unknowns in the selected sections. Group related questions; summarize the evidence that motivated them. Treat the user's answer as the local rule. Do not import a reference system's policy into the user's product.

## Draft and handoff

Draft only selected, applicable sections. Make every published claim complete and grounded. Preserve user-visible property, variant, state, size, and configuration names exactly. Strip only a terminal Figma API suffix matching `#<digits>:<digits>` from public names, while retaining raw keys in working evidence.

If bilingual output was selected, produce Persian and English drafts for the same selected sections in one pass, preserving meaning while using natural phrasing in each language. If a single language was selected, produce only that language. Persian is the default primary language; primary language controls the order shown to the user. Do not make approval of one language a prerequisite for drafting the other when bilingual output was requested.

Save drafts as Markdown in the user's chosen output directory, with a compact evidence/decisions sidecar. Mark unresolved information in the sidecar and ask before asserting it; include `TBD` in publication text only if the user requests it. Hand section-level image needs and approved captions to `component-doc-visuals` when visuals are requested. The final Markdown package is assembled by `component-doc-assembler` after text and visuals are ready.
