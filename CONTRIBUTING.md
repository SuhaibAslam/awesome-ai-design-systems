# Contributing

Thanks for helping grow this list.

## How to add an entry
1. Check `docs/inclusion-criteria.md`.
2. Add your entry to `data/ai-design-systems.json`.
3. Keep fields short, factual, and non-marketing.
4. Run validation: `make validate` (or `python scripts/validate-data.py`).
5. Regenerate the table: `make table` (or `python scripts/generate-table.py`).
6. Commit changes to both `data/ai-design-systems.json` and `TABLE.md`.

## Data quality guidelines
- Avoid duplicates or near-duplicates
- Use the official repo or canonical site
- Prefer primary sources over blog posts
- Keep tags concise and lowercase
- Use "Unknown" if a license cannot be confirmed

### Pre-commit (optional but recommended)
Install pre-commit and enable the hooks to catch issues before you commit:

```sh
pip install pre-commit
pre-commit install
```

Hooks will run validation for the dataset.

### CI behavior
- Pull requests run dataset validation and table generation.
- CI will fail if `TABLE.md` is out of date with the generator.

If you're unsure whether a project qualifies, open an issue with a short rationale.
