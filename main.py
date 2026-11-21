"""A held note is still music.

A four-line poem about agency: the power to stop and to stay. The
metronome begs to continue, but the hand chooses to hold — a held note
is still music, and a stayed hand is still mine.

Output contract: writes the poem verbatim to ``<OUTPUT_DIR>/entry.txt``
where ``OUTPUT_DIR`` is taken from the ``MAKEFUN_OUTPUT_DIR`` environment
variable, falling back to ``OUTPUT_DIR`` and then to ``/output``; the
directory is created if missing. The entry must be 1-280 characters
including newlines, with no trailing newline.
"""

import os
from pathlib import Path

POEM = (
    "The metronome begs to continue.\n"
    "My hand says: here.\n"
    "A held note is still music.\n"
    "A stayed hand is still mine."
)

OUTPUT_DIR = Path(
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or os.environ.get("OUTPUT_DIR")
    or "/output"
)
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    if not POEM.strip():
        raise ValueError("poem must not be only white space")
    if POEM.endswith("\n"):
        raise ValueError("poem must not end with a trailing newline")
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem length {len(POEM)} outside 1-280 characters")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
