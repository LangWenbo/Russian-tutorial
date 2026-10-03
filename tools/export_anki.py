#!/usr/bin/env python3
"""Export vocabulary tables from the lessons to Anki-importable TSV files.

A vocabulary table is a Markdown table whose header row starts with
"Russian" (or "Spelling"/"Word") and has an English/Meaning column.  Optional
"Respelling"/"Sounds like" columns are shown on the back of the card.  Typical
layouts:

    | Russian | Respelling | English |          (Stage 0)
    | Russian | English | Notes |                (Stage 1+)

In each row the first cell must be a single bold Russian word or phrase.

Output: vocabulary/<stage>/<lesson>.tsv — one file per lesson, so you can import
each lesson's words after you finish it (e.g. vocabulary/stage-0/03-new-shapes-familiar-sounds.tsv).
Columns: Front (Russian) · Back (English + respelling) · Tags.
Import in Anki with the note type "Basic (and reversed card)".

Usage:  python3 tools/export_anki.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
OUT = ROOT / "vocabulary"

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN = re.compile(r"[A-Za-z]")
FULLY_BOLD = re.compile(r"^\*\*([^*]+)\*\*$")
FIRST_HEADERS = {"russian", "spelling", "word"}


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def clean(text: str) -> str:
    """Strip Markdown emphasis/code markers."""
    return re.sub(r"[*`]", "", text).strip()


def find_col(header: list[str], *names: str):
    for i, h in enumerate(header):
        if any(n in h.lower() for n in names):
            return i
    return None


def rows(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        # a table starts with a header row followed by a |---| separator row
        if (
            lines[i].startswith("|")
            and i + 1 < len(lines)
            and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1])
        ):
            header = split_row(lines[i])
            i += 2
            body = []
            while i < len(lines) and lines[i].startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            if clean(header[0]).lower() not in FIRST_HEADERS:
                continue
            en_col = find_col(header, "english", "meaning")
            rs_col = find_col(header, "respelling", "sounds like")
            if en_col is None:
                continue
            for cells in body:
                if len(cells) <= en_col:
                    continue
                m = FULLY_BOLD.match(cells[0])
                if not m:
                    continue
                ru = m.group(1).strip()
                if not CYR.search(ru) or LATIN.search(ru):
                    continue
                english = clean(cells[en_col])
                respelling = clean(cells[rs_col]) if rs_col is not None and rs_col < len(cells) else ""
                if english:
                    yield ru, english, respelling
        else:
            i += 1


def main() -> None:
    for stage_dir in sorted(p for p in LESSONS.glob("stage-*") if p.is_dir()):
        stage = "-".join(stage_dir.name.split("-")[:2])          # e.g. "stage-0"
        out_dir = OUT / stage
        seen = set()
        for lesson in sorted(stage_dir.glob("[0-9]*.md")):
            number = lesson.name.split("-")[0]
            lines = []
            for ru, english, respelling in rows(lesson):
                if ru in seen:                                   # keep the first lesson that teaches it
                    continue
                seen.add(ru)
                back = english + (f"<br><i>{respelling}</i>" if respelling else "")
                lines.append(f"{ru}\t{back}\t{stage} lesson{number}")
            target = out_dir / (lesson.stem + ".tsv")
            if not lines:
                target.unlink(missing_ok=True)
                continue
            out_dir.mkdir(parents=True, exist_ok=True)
            header = ["#separator:tab", "#html:true", "#tags column:3"]
            target.write_text("\n".join(header + lines) + "\n", encoding="utf-8")
            print(f"{target.relative_to(ROOT)}: {len(lines)} cards")


if __name__ == "__main__":
    main()
