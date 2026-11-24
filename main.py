#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes exactly one sentence to /output/entry.txt.
Deterministic: no input, no network, no randomness, no environment reads.
The same sentence is written on every run, so two runs are byte-identical.
The sentence is written verbatim, with no trailing newline, so the file
holds exactly the sentence and nothing else.
"""

import os

SENTENCE = (
    "A telephone that answers every spam call itself and keeps the caller "
    "talking for hours, so telemarketers spend their day pitching to a phone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
