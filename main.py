#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes a single line of out-of-office auto-reply to /output/entry.txt.
Deterministic: every run writes the exact same bytes.
"""

import os

LINE = "I'm out of office until Monday. My inbox is guarded by a goldfish with no memory and full admin rights."


def main():
    # Gate check, mirroring the competition rules: 1-140 UTF-8 characters,
    # not only whitespace, exactly one line, no trailing newline.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # no trailing newline: the file is exactly the line


if __name__ == "__main__":
    main()
