#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "My earbuds case died before the earbuds did, so now I carry a tiny "
    "coffin for two perfectly healthy earbuds."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 characters, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
