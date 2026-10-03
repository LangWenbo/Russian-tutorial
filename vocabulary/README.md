# Vocabulary flashcards

One tab-separated file per lesson, generated from the vocabulary tables in the lessons. Import each file **after you finish that lesson** — that way you only ever review words you've actually met.

```
vocabulary/
  stage-0/
    01-first-five-letters.tsv
    02-false-friends.tsv
    …
```

## Import into Anki

1. Install [Anki](https://apps.ankiweb.net) (free on desktop and Android; AnkiMobile on iOS is paid).
2. **File → Import** and pick the `.tsv` for the lesson you just finished.
3. Set **Note type** to **Basic (and reversed card)** — this gives you both *Russian → English* and *English → Russian* cards.
4. Check the field mapping: *Field 1 → Front* (Russian), *Field 2 → Back* (English + pronunciation help), and the third column → **Tags**.
5. Import. Re-importing a file is safe: Anki recognises duplicates by the first field.

## Tips

* **Do both directions.** Recognising a word is easy; recalling it is what makes you fluent.
* **Say every word aloud** when you review. Check difficult ones at [forvo.com](https://forvo.com).
* **Cap new cards at ~10–15 per day.** The reviews will pile up faster than you expect.
* Add your own cards (sentences from the lessons make the best cards).

## Regenerating

If the lesson tables change, rebuild the files with:

```bash
python3 tools/export_anki.py
```

A row becomes a card when it sits in a table whose header starts with **Russian** (or *Spelling*) and has an **English/Meaning** column, and the first cell is a single bold Russian word or phrase.
