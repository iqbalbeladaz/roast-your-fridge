#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge entry.

Writes one roast of the fridge to /output/entry.txt. The roast is a
fixed, deterministic string: every run produces byte-identical output.
"""

import os

ROAST = (
    "My fridge is the only roommate who eats nothing, makes noise "
    "all night, and still expects me to pay the electricity bill."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "roast violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
