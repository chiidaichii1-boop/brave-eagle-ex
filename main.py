#!/usr/bin/env python3
"""One Word From Your Ex: the single word my ex would use to describe me.

The entry is one word: "placeholder" — the person who was never the plan,
just the warm body keeping the seat warm until the real thing showed up.
It stings because it is true, and it is funny for exactly the same reason.
"""
import os

# Verified: entry is "placeholder", 11 characters, within the 1-24 gate.
ENTRY = "placeholder"

# Gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters.
assert 1 <= len(ENTRY) <= 24, "entry out of gate"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
