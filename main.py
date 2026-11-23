#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Stdlib only, no network. The line is a single sentence of 118
characters, written with no trailing newline.
"""

import os

LINE = "The elevator stopped on every floor except mine, like it was introducing me to neighbors I have spent years avoiding."


def main() -> None:
    # Guard: the entry must be a single sentence of 1-200 characters
    # with no newline, per the competition gate.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must have no newline"
    assert LINE.strip() == LINE and LINE, "line must not be only whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verify: what landed on disk must be byte-identical.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
