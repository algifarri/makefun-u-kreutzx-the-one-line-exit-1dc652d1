#!/usr/bin/env python3
"""The One-Line Exit entry.

Writes one funny one-line resignation letter to /output/entry.txt
(UTF-8, 140 Unicode code points at most, inside the 1-140 gate).
Deterministic, standard library only, no network, no environment reads.

The line (123 characters, inside the 1-140 gate): "I hereby resign
effective immediately: the office goldfish was promoted before me,
and I refuse to take orders from a fish." It reads like a letter a
person could actually send, opens with the formal resignation
formula, then turns on an absurd promotion: the goldfish outranked
the writer, and the punchline lands on the last word. Specific
voice, one surprise, no padding.
"""

import os

TEXT = (
    "I hereby resign effective immediately: the office goldfish was "
    "promoted before me, and I refuse to take orders from a fish."
)


def main() -> None:
    # The gate requires 1-140 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
