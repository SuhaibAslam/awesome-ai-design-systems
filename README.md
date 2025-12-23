# Awesome AI-Native Design Systems [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated, research-grade index of AI-native, AI-first, and AI-focused design systems, UI frameworks, and component platforms, where AI is treated as a core design material, not an add-on.

## Contents

- Motivation
- Scope and principles
- Taxonomy
- Highlights
- Dataset and table
- Contributing
- Roadmap
- License

## Motivation

Traditional design systems assume deterministic components, static states, human-authored flows, and predictable inputs. AI-native products violate those assumptions with probabilistic outputs, non-deterministic flows, tool-calling, emergent UI states, prompt-driven structure, and runtime UI synthesis. This repository documents and structures the emerging ecosystem of design systems built for AI-native products.

## Scope and principles

This repo is:
- A map of the AI-native design systems landscape
- A taxonomy of AI-first UI paradigms
- A reference dataset for researchers, designers, and engineers
- A starter kit for prototyping AI-native interfaces
- A living index that evolves with the ecosystem

This repo is not:
- A generic UI kit list
- A "best React components" roundup
- A marketing catalog
- A no-code tool directory
- Primarily a list of traditional design systems with superficial AI add-ons; where such projects appear, they must demonstrate AI-specific patterns with evidence

## Taxonomy

Each entry is classified by AI design system type. See `docs/taxonomy.md` for definitions.

- AI-Driven Component Generation
- AI Chat / Agent UI Systems
- AI UI Component Libraries
- Copilot / Assistant Integration Systems
- Prompt-First / Prompt-Component Systems
- Schema-to-UI Kits
- Agent/UI Protocols

## Highlights

If you are new to this space, start with these:
- 21st.dev (component generation)
- OpenAI ChatKit, assistant-ui, ChatUI (chat and agent UX)
- CopilotKit (copilot integration)
- Lobe UI, LangUI, Ant Design X (AI UI component libraries)

## Dataset and table

- Source of truth: `data/ai-design-systems.json`
- Generated table: `TABLE.md`
- Validate the dataset with `python scripts/validate-data.py` (or `make validate`)
- Regenerate the table with `python scripts/generate-table.py` (or `make table`)

## Contributing

Read `CONTRIBUTING.md` and `docs/inclusion-criteria.md`. Add entries to `data/ai-design-systems.json`, validate with `make validate`, then regenerate with `make table`.

Optional: enable pre-commit hooks to auto-validate on commit.

## Scope Notes

This list prioritizes AI-native systems, but may include transitional projects that are evolving toward AI-first patterns. Inclusion requires clear, cited evidence of AI-specific primitives, patterns, or protocols, even if the broader project is not fully AI-native yet.

## Roadmap

See `docs/roadmap.md` for planned improvements and research directions.

## License

This list is licensed under CC0 1.0. See `LICENSE`.
