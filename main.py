#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one funny one-line excuse (<=140 chars) to /output/entry.txt.
Deterministic: no randomness, no time, no network.
"""

import os

ENTRY = (
    "All tests green \u2014 the suite only ever runs against a tiny copy of "
    "the app I wrote inside the test file, and that copy works perfectly."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
