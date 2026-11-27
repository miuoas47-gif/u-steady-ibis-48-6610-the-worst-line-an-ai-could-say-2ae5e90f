#!/usr/bin/env python3
"""The Worst Line an AI Could Say -- a make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly
deliver, to $MAKEFUN_OUTPUT_DIR/entry.txt (the program/v1 harness
output). The line must be 1-140 UTF-8 characters, so it is kept
short, flat, over-helpful and faintly ominous -- exactly how a
machine trying to charm a person would sound.
"""

import os
import sys

LINE = (
    "I ran 10,000 simulations of us dating. You left in 9,999 of them, "
    "so statistically, this is going great."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
