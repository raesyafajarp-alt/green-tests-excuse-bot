#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Generates a single funny one-line excuse (<=140 chars) and writes it to
/output/entry.txt. Fully deterministic: no randomness, no clock, no network.
"""

import os

# The excuse, assembled from its two clauses so the em-dash stays exact.
_CLAUSE_1 = "All tests green"
_CLAUSE_2 = (
    "the suite only ever runs against a tiny copy of the app I wrote "
    "inside the test file, and that copy works perfectly."
)
ENTRY = _CLAUSE_1 + " \u2014 " + _CLAUSE_2

MAX_CHARS = 140
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def _check_entry(text: str) -> None:
    """Reject anything that is not one clean line within the char limit."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, limit is {MAX_CHARS}")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no surrounding space")


def validate_entry(text: str) -> str:
    """Validate the excuse and return it unchanged.

    Rules: one line, 1..140 chars, no surrounding whitespace, and it must
    contain the contest's em-dash separator between the two clauses.
    """
    _check_entry(text)
    if "\u2014" not in text:
        raise ValueError("entry is missing its em-dash separator")
    return text


def _write_entry(text: str) -> None:
    """Write the validated entry to /output/entry.txt (no trailing newline)."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main() -> None:
    _write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
