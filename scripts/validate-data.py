#!/usr/bin/env python3
"""
Validation for data/ai-design-systems.json

Checks:
- Required keys present and correct types
- No duplicate names/URLs (case-insensitive for names)
- Tags are lowercase, hyphenated, ASCII, and reasonably short
- License is non-empty (or 'Unknown')
- Type matches known taxonomy
- Name is ASCII (warn if not strictly ASCII)
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any

DATA_PATH = Path("data/ai-design-systems.json")

REQUIRED_KEYS = [
    "name",
    "org",
    "url",
    "license",
    "ai_features",
    "integrations",
    "maturity",
    "type",
    "tags",
    "evidence",
    "notes",
]

KNOWN_TYPES = {
    "AI-Driven Component Generation",
    "AI Chat / Agent UI Systems",
    "AI UI Component Libraries",
    "Copilot / Assistant Integration Systems",
    "Prompt-First / Prompt-Component Systems",
    "Schema-to-UI Kits",
    "Agent/UI Protocols",
}


def is_ascii(s: str) -> bool:
    try:
        s.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def validate_tags(tags: List[str], name: str) -> List[str]:
    errors: List[str] = []
    for t in tags:
        if not isinstance(t, str):
            errors.append(f"Tags must be strings: {name}")
            continue
        if t != t.lower():
            errors.append(f"Tag not lowercase '{t}' in {name}")
        if any(ch.isspace() for ch in t):
            errors.append(f"Tag contains spaces '{t}' in {name}")
        # allow letters, digits, and hyphens only
        if not all(ch.isalnum() or ch == '-' for ch in t):
            errors.append(f"Tag contains invalid chars '{t}' in {name}")
        if len(t) > 24:
            errors.append(f"Tag too long (>24) '{t}' in {name}")
    return errors


def main() -> None:
    if not DATA_PATH.exists():
        print(f"Missing dataset at {DATA_PATH}")
        sys.exit(1)

    try:
        entries: List[Dict[str, Any]] = json.loads(DATA_PATH.read_text())
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        sys.exit(1)

    errors: List[str] = []

    seen_names = set()
    seen_urls = set()

    for i, entry in enumerate(entries):
        # Required keys and types
        missing = [k for k in REQUIRED_KEYS if k not in entry]
        if missing:
            errors.append(f"Entry {i} '{entry.get('name','unknown')}' missing keys: {missing}")
            continue

        if not isinstance(entry["tags"], list):
            errors.append(f"Tags must be a list in '{entry['name']}'")

        # Duplicates
        nm = entry["name"].strip().lower()
        url = entry["url"].strip()
        if nm in seen_names:
            errors.append(f"Duplicate name: '{entry['name']}'")
        else:
            seen_names.add(nm)
        if url in seen_urls:
            errors.append(f"Duplicate URL: '{url}'")
        else:
            seen_urls.add(url)

        # License
        lic = (entry["license"] or "").strip()
        if not lic:
            errors.append(f"Empty license in '{entry['name']}' (use 'Unknown' if unclear)")

        # Type
        typ = entry["type"].strip()
        if typ not in KNOWN_TYPES:
            errors.append(
                f"Unknown type '{typ}' in '{entry['name']}'. See docs/taxonomy.md for allowed types."
            )

        # ASCII name check (warn only)
        if not is_ascii(entry["name"]):
            errors.append(
                f"Non-ASCII name in '{entry['name']}'. Prefer ASCII unless the project requires otherwise."
            )

        # Evidence non-empty
        if not str(entry["evidence"]).strip():
            errors.append(f"Missing evidence in '{entry['name']}'")

        # Tag shape
        errors.extend(validate_tags(entry["tags"], entry["name"]))

    if errors:
        print("Validation failed:\n" + "\n".join(f"- {e}" for e in errors))
        sys.exit(1)

    print(f"OK: {len(entries)} entries validated with no issues.")


if __name__ == "__main__":
    main()
