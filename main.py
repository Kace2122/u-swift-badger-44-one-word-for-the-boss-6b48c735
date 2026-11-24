#!/usr/bin/env python3
"""One Word for the Boss — entry program.

Writes the single word "Swoopervisor" to /output/entry.txt:
a supervisor who swoops in, drops chaos, and leaves.
The gate requires UTF-8 text of 1-30 characters, not only whitespace,
so the word is written with no trailing newline.
"""

import os

WORD = "Swoopervisor"


def main() -> None:
    # Gate check: 1-30 characters, a single word, not only whitespace.
    if not (1 <= len(WORD) <= 30 and WORD.split() == [WORD]):
        raise ValueError(f"word fails the gate: {WORD!r}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
