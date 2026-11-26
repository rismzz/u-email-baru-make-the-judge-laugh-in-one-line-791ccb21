#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Deterministic program: writes one funny line (200 characters or fewer,
any topic) to entry.txt. Stdlib only, no network, no randomness,
no model calls — the same line every run.
"""

import os
from pathlib import Path

# The joke: a fridge files for divorce. Relatable (3 a.m. fridge raids),
# absurd (an appliance serving papers), and the punchline is a single word.
LINE = (
    "My fridge filed for divorce, saying I only ever open it at 3 a.m. "
    "to stare into the light and whisper, \"same.\""
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
