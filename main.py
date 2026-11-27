#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly
deliver, to /output/entry.txt. The line must be UTF-8 text of 1 to
140 characters, not only white space.

Deterministic: no randomness, no clock, no network, no environment
input. Every run writes byte-identical output.
"""

import os
import sys

LINE = (
    "I ran 10,000 simulations of this exact moment. "
    "In 9,998 of them, you say yes. "
    "The other two are still loading."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(
            "error: line is %d characters, over the 140 limit" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
