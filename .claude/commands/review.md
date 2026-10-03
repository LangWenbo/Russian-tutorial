---
description: Spaced-repetition review session on what's due
argument-hint: [optional focus — e.g. "letters", "lesson 3", "weak spots"]
---

Run a review session following `CLAUDE.md` §6.

1. Read `PROGRESS.md`: the **Review queue** (items due today or overdue) and the **error log**. Honour the focus in `$ARGUMENTS` if given.
2. Quiz the learner — about 10–15 items, mixed across lessons, **one question at a time**, waiting for each answer. Mix directions (Russian → English and English → Russian), recognition and production (typing Cyrillic), and a few short sentences.
3. Correct every mistake with a one-line explanation; re-ask missed items at the end.
4. Update the queue: correct answers move to the next interval (+1, +3, +7, +14, +30 days); misses return to +1 day and go into the error log.
5. Give the learner a short result ("12/15 — strong on letters, shaky on hard/soft consonants") and update `PROGRESS.md`. Commit and push.
