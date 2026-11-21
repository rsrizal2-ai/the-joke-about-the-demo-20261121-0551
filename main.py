#!/usr/bin/env python3
"""Entry for make.fun competition the-joke-about-the-demo-20261121-0551.

Writes one one-line joke about working beside AI coding agents to
<MAKEFUN_OUTPUT_DIR>/entry.txt. No network, no external calls.
"""

import os

JOKE = (
    "My AI coding agent fixed the demo bug live in four seconds, "
    "then spent forty minutes breaking its own fix "
    "\u2014 then asked if I'd like it to continue."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 code points"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
