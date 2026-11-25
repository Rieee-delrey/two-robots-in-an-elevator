#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes the single entry line to /output/entry.txt, byte-identical every run.
"""

import os

LINE = "We have been stuck between floors for nine seconds. I have already imagined our entire friendship. It ends badly."


def main() -> None:
    os.makedirs("/output", exist_ok=True)

    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Own validation, invented for this revision: reopen the file in text
    # mode and check it holds exactly one line, with no trailing newline,
    # and that every character is plain ASCII.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert text == LINE, "entry text does not match the expected line"
    assert "\n" not in text, "entry must contain exactly one line with no newline"
    assert all(ord(ch) < 128 for ch in text), "entry must be plain ASCII only"
    assert len(text.encode("utf-8")) == 113, "entry must be exactly 113 bytes"


if __name__ == "__main__":
    main()
