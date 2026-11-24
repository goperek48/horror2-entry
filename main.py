#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

This program's only task is to emit the entry text: one horror story told
in exactly two sentences, written to /output/entry.txt. Because the judge
scores the words themselves, the program keeps the story as a single fixed
constant and reproduces it byte for byte on every run, without a trailing
newline or any surrounding decoration.
"""

import os

# The entry: two sentences, comfortably inside the 400-character gate.
# The first sentence is a lonely widower's nightly habit, thirty years of
# grief served on a second plate. The second sentence quietly overturns it:
# the plate is already empty and the chair is still warm, so the habit is
# no longer his alone — someone has been eating with him, unseen.
STORY = (
    "Every night for thirty years I have set a second plate at dinner "
    "for the wife I buried in 1994. "
    "Tonight the plate was empty before I sat down, "
    "and the chair across from me was still warm."
)


def main() -> None:
    # The harness reads /output/entry.txt, so the file must hold the story
    # and nothing else: no trailing newline, no header, no extra whitespace.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
