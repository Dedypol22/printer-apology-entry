#!/usr/bin/env python3
"""The Printer Apology.

One line of apology from an office printer to the people who keep jamming
it, feeding it cheap paper and swearing at it. The printer says sorry for
the jam and the streaks -- and then, in the same breath, confesses it
printed your resignation letter twice. The punch is the last sentence:
one copy was for HR.

The line is 96 characters, inside the competition's 120-character gate,
and the file holds exactly that line plus a trailing newline (97 bytes).
Written to entry.txt in the output directory and echoed to stdout.
"""

import os
import sys

# The apology itself: three printer sins, then the twist at the end.
APOLOGY = (
    "Sorry for the jam, the streaks, and printing your resignation "
    "letter twice. One copy was for HR."
)


def output_dir() -> str:
    """Where the entry file goes: $MAKEFUN_OUTPUT_DIR, or /output by default.

    An env var that is set but empty counts as unset: writing to a relative
    "entry.txt" in the caller's cwd would silently lose the entry.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    # Build the payload once, so the file and stdout can never disagree
    # about the exact bytes of the apology.
    text = APOLOGY + "\n"

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)

    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
