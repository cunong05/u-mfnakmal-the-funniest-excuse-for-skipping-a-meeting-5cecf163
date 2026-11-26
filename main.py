#!/usr/bin/env python3
"""Write the funniest excuse for skipping a meeting to /output/entry.txt.

The entry is a single razor-sharp line (1-200 characters) that gets you out
of a pointless work meeting. The program validates the text against the
competition gate (1-200 characters, single line) before writing it, so what
lands in /output/entry.txt is always a valid entry.
"""

from pathlib import Path

# Gate limits from the competition rules: /output/entry.txt must hold
# UTF-8 text of 1 to 200 characters, on a single line.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200

ENTRY = (
    "Sorry, I can't make the meeting \u2014 my calendar and I are in a toxic "
    "relationship, and today it double-booked me with my own sanity."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY
    if not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
