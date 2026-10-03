---
description: Teach the next Russian lesson (or a specific one) interactively
argument-hint: [lesson number or topic — blank = next lesson]
---

Run a tutoring session following `CLAUDE.md`.

1. Read `PROGRESS.md`. Target lesson: `$ARGUMENTS` if given, otherwise the current/next lesson in "Where I am now".
2. Warm-up: quiz the learner on 4–6 items due in the review queue (skip if the queue is empty).
3. Open the lesson file and teach it **interactively** — one concept at a time, with questions, waiting for the learner's answers and correcting them. Don't paste the whole file.
   - If the lesson file doesn't exist yet, write it first (see CLAUDE.md §5 and `lessons/_TEMPLATE.md`) from the unit in `curriculum/ROADMAP.md`, run `python3 tools/check_text.py` and `python3 tools/export_anki.py`, then teach it.
4. Finish by summarising, assigning the spaced review, and updating `PROGRESS.md` (lesson log, review queue, error log, current position).
5. Commit and push to the working branch.
