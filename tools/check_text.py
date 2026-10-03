#!/usr/bin/env python3
"""QA for Russian lesson text.

Checks every Markdown file in the repository for:
  1. Mixed-script words  — a token containing both Latin and Cyrillic letters
     (almost always a look-alike typo, e.g. Latin "a" inside a Russian word).
  2. Malformed stress marks — an acute accent (U+0301) that is not on a
     Cyrillic vowel, on "ё" (always stressed, never marked), on a one-syllable
     word, or a second accent in the same word.

Usage:  python3 tools/check_text.py [path ...]
Exit status is 1 if any problem is found.
"""
import re
import sys
from pathlib import Path

ACUTE = "\u0301"
CYR_VOWELS = set("аеиоуыэюяАЕИОУЫЭЮЯ")
LATIN = re.compile(r"[A-Za-z]")
CYR = re.compile(r"[\u0400-\u04FF]")
# A "word": letters (Latin or Cyrillic), the acute accent, and "_" (fill-in-the-blank gaps).
TOKEN = re.compile(r"[A-Za-z\u0400-\u04FF\u0301_]+")


def check_file(path: Path) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), 1):
        for m in TOKEN.finditer(line):
            tok = m.group()
            has_lat, has_cyr = bool(LATIN.search(tok)), bool(CYR.search(tok))
            if has_lat and has_cyr:
                problems.append(f"{path}:{lineno}: mixed Latin/Cyrillic word: {tok!r}")
                continue
            if ACUTE not in tok or not has_cyr:
                continue
            if tok.count(ACUTE) > 1:
                problems.append(f"{path}:{lineno}: more than one stress mark: {tok!r}")
            for i, ch in enumerate(tok):
                if ch == ACUTE and (i == 0 or tok[i - 1] not in CYR_VOWELS):
                    problems.append(f"{path}:{lineno}: stress mark not on a Cyrillic vowel (or on ё): {tok!r}")
            vowels = sum(1 for ch in tok if ch in CYR_VOWELS or ch in "ёЁ")
            if vowels < 2:
                problems.append(f"{path}:{lineno}: stress mark on a one-syllable word: {tok!r}")
    return problems


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    paths = [Path(a) for a in argv] or sorted(
        p for p in root.rglob("*.md") if ".git" not in p.parts
    )
    problems = []
    for p in paths:
        problems.extend(check_file(p))
    for line in problems:
        print(line)
    print(f"checked {len(paths)} file(s): {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
