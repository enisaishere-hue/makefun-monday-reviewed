#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- make.fun entry.

Monday, reviewed like a product: one star -- it arrived too early,
stayed too long, and brought no snacks. Would not recommend, cannot
return.

Writes the review to entry.txt inside the output directory. The
directory comes from MAKEFUN_OUTPUT_DIR (default /output); a first
command-line argument, if given, overrides it. The grader runs the
program with no arguments at all.
"""

import os
import sys

REVIEW = (
    "Monday: one star -- arrived too early, "
    "stayed too long, brought no snacks."
)


def main(argv):
    # The sealed scorer only accepts 1-200 characters, so refuse loudly
    # instead of writing a review the gate would reject.
    if not 1 <= len(REVIEW) <= 200:
        print("review must be 1-200 characters, got %d" % len(REVIEW),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
