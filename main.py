#!/usr/bin/env python3
"""Roast the Gadget You Use Every Day: One Line.

Writes a single-line roast (1-200 characters) of the wireless earbuds to
/output/entry.txt. Standard library only, no network, deterministic.

The angle: not the stock "phone battery dies" joke. This one roasts a real
behaviour — wireless earbuds always lose one side first, right in the middle
of a song — and lands the sting on the price: you paid for stereo sound and
ended up with a one-ear monologue.
"""
import os

ROAST = "My earbuds die one at a time, taking turns ghosting me mid-song \u2014 I paid for stereo and got a one-ear monologue."


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} characters"
    assert "\n" not in text, "roast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
