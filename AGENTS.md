# Agent Instructions

## Overview
This repository is an awesome-style, curated index of AI-native design systems and UI frameworks. The goal is high-signal, non-duplicative entries with clear AI relevance.

## Source of truth
- Dataset: `data/ai-design-systems.json`
- Generated table: `TABLE.md`
- Regenerate the table with: `python scripts/generate-table.py`

## Editing rules
- Keep entries consolidated; do not split a project into docs, demos, or templates.
- Use official repos or canonical product pages.
- Prefer factual, compact descriptions; avoid marketing language.
- Use "Unknown" if the license is not confirmed.
- Keep tags lowercase and short.
- Stay within ASCII unless a project name requires otherwise.

## Quality checks
- No duplicates or near-duplicates.
- Every entry must fit the inclusion criteria in `docs/inclusion-criteria.md`.
- Run the table generator after dataset changes.
