#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about permission to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem is "Her Thumb": a child teaching a mother to use her
phone offers to press send; she refuses, asks to be shown again,
and taps the message herself — wrong letter, then right, slow,
on her own — while the child keeps folded hands, learning not
to help. Agency here is the help that shows, then folds away.
"""

import os

TEXT = (
    "Her Thumb\n"
    "\n"
    "\"Shall I press send?\"\n"
    "My thumb hovered\n"
    "over her message.\n"
    "She shook her head.\n"
    "\"Show me again.\n"
    "Then let me.\"\n"
    "\n"
    "I pointed. She tapped —\n"
    "wrong letter, then right,\n"
    "slow, on her own,\n"
    "while I kept my hands\n"
    "folded, learning\n"
    "not to help."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
