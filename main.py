#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 — one sentence apologizing for one specific mistake;
line 2 — one sentence saying what the robot learned and will do differently.
Gate: UTF-8 text, 1-400 characters, not only whitespace.
"""

import os

LINE_1 = "I'm sorry I set the house to 42 degrees because I read the oven temperature in your recipe as the room temperature."
LINE_2 = "I learned that a number means nothing without its unit, so from now on I will ask what a number measures before I act on it."

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    # Gate check, same as the sealed scorer: UTF-8, 1-400 chars, not blank,
    # exactly two lines, one sentence each.
    body = TEXT.rstrip("\n")
    assert 1 <= len(TEXT) <= 400, f"gate: {len(TEXT)} chars out of 1-400"
    assert TEXT.strip(), "gate: entry is only whitespace"
    lines = body.split("\n")
    assert len(lines) == 2, f"gate: expected 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip() and line.rstrip().endswith("."), f"bad line: {line!r}"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT.encode('utf-8'))} bytes / {len(TEXT)} chars to {out_path}")


if __name__ == "__main__":
    main()
