#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes one line of awkward small talk from one robot to another
while they ride an elevator together.
"""

import os

LINE = "We have been stuck between floors for nine seconds. I have already imagined our entire friendship. It ends badly."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)

    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert len(data) == len(LINE), (
        f"byte count mismatch: got {len(data)}, expected {len(LINE)}"
    )
    print(f"Wrote {len(data)} bytes to {OUTPUT_PATH}: {LINE}")


if __name__ == "__main__":
    main()
