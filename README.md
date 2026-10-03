# Русский язык — A Russian Course, from Letters to Fluency

A complete, self-contained Russian course in a Git repository — with **Claude as your personal tutor**. You start with the alphabet and finish at advanced (C1) level. Everything you do is tracked in `PROGRESS.md` and saved with Git.

> **Your first lesson is ready:** [`lessons/stage-0-alphabet/01-first-five-letters.md`](lessons/stage-0-alphabet/01-first-five-letters.md)

---

## 🚀 Quick start

1. **Open a session in this repository** (Claude Code on the web, desktop, or CLI).
2. Say **"start"** — or type **`/lesson`**. Your tutor reads `PROGRESS.md`, reviews what's due, and teaches the next lesson *interactively*: it explains, asks you questions, corrects you, and moves on when you're ready.
3. At the end of each session your progress is saved and committed. Next time, just say **"continue"**.

Prefer to study alone? Every lesson is a standalone Markdown file with explanations, exercises and an answer key — open them in order.

Handy commands:

| Command | What it does |
|---|---|
| `/lesson` | Teach the next lesson (`/lesson 4` for a specific one) |
| `/review` | Spaced-repetition review of what's due |
| "quiz me on …" | Ad-hoc quiz on any topic |
| "slower" / "faster" / "explain again" | Adjust the pace |

---

## 🗺 The path

| Stage | Level | What you can do at the end | Status |
|---|---|---|---|
| **0 — Alphabet & Sounds** | pre-A1 | Read any Russian word aloud; greet, thank, introduce yourself | ✅ **9 lessons written** |
| **1 — Survival Russian** | A1 | Basic daily conversations, ordering, directions, time | 📐 planned in detail |
| **2 — Everyday Russian** | A2 | Past & future, all six cases, shopping, health, plans | 📐 planned |
| **3 — Independent Speaker** | B1 | Hold conversations, tell stories, read simple texts | 📐 planned |
| **4 — Fluent Conversation** | B2 | Argue, follow news and films, read real articles | 📐 planned |
| **5 — Advanced** | C1 → C2 | Literature, nuance, professional Russian | 📐 planned |

The full syllabus — every unit, grammar point and goal — is in [`curriculum/ROADMAP.md`](curriculum/ROADMAP.md).

**How lessons after Stage 0 are produced:** Stage 0 is fully written because every learner needs exactly the same alphabet course. From Stage 1 onward, your tutor **writes each lesson just-in-time**, following the roadmap and the lesson template, and adapts it to *your* mistakes, pace and interests (lessons are saved into `lessons/` as they're created). This keeps the course tailored instead of one-size-fits-all.

### Stage 0 — Alphabet & Sounds

| # | Lesson | You learn |
|:-:|---|---|
| 1 | [First Five Letters](lessons/stage-0-alphabet/01-first-five-letters.md) | А К М О Т · stress · no "a/the", no "is" |
| 2 | [The False Friends](lessons/stage-0-alphabet/02-false-friends.md) | В Н Р С У Х Е · *вот* |
| 3 | [New Shapes, Familiar Sounds](lessons/stage-0-alphabet/03-new-shapes-familiar-sounds.md) | Б Г Д З И Л П Ф · *привет, спасибо, где?* |
| 4 | [Vowels, Hard & Soft](lessons/stage-0-alphabet/04-hard-and-soft-vowels.md) | Э Ы Я Ё Ю Й · pronouns · *это* · *мой* |
| 5 | [The Hushers](lessons/stage-0-alphabet/05-the-hushers.md) | Ж Ш Щ Ч Ц · question words · introductions |
| 6 | [The Two Signs](lessons/stage-0-alphabet/06-the-two-signs.md) | Ь Ъ · hard vs soft · professions · survival phrases |
| 7 | [Sound Rules](lessons/stage-0-alphabet/07-sound-rules.md) | stress · vowel reduction · devoicing · intonation |
| 8 | [Writing & Typing](lessons/stage-0-alphabet/08-writing-and-typing.md) | alphabet order · cursive · keyboard · your name |
| 9 | [Checkpoint](lessons/stage-0-alphabet/09-checkpoint.md) | 100-point test · signs, menus, a first text |

---

## 📁 What's in this repo

```
README.md               ← you are here
CLAUDE.md               ← instructions for your tutor (how sessions work)
PROGRESS.md             ← your progress: current lesson, review queue, error log
curriculum/ROADMAP.md   ← the master syllabus, beginner → C1
lessons/                ← lesson files, by stage (+ _TEMPLATE.md)
reference/              ← alphabet chart, sound-rules cheat sheet, resources
vocabulary/             ← Anki flashcards, one file per lesson
recordings/             ← voice-recording log + benchmarks (audio stays local unless you approve)
tools/                  ← check_text.py (QA for Cyrillic), export_anki.py
.claude/commands/       ← /lesson and /review
```

## 🧭 How to get the most from it

* **Little and often beats long and rare.** 45–60 minutes a day is ideal; even 20 minutes counts.
* **Say everything aloud.** Reading silently doesn't train your mouth. Check pronunciation on [Forvo](https://forvo.com).
* **Answer before you peek.** Cover the answer key; try first.
* **Type your answers in Cyrillic** from Lesson 4 on (see Lesson 8 for keyboard setup).
* **Don't skip the reviews.** The review queue is what moves words from "I've seen it" to "I know it".
* **Mistakes are data.** Your tutor logs them and brings them back until they stick.
* **Use Russian in the wild:** signs, songs, cartoons, menus. See [`reference/resources.md`](reference/resources.md).

## 🛠 Tools

```bash
python3 tools/check_text.py     # QA: mixed Latin/Cyrillic letters, malformed stress marks
python3 tools/export_anki.py    # regenerate flashcards in vocabulary/
```

Good luck — **уда́чи!** (*oo-DA-chee*) 🇷🇺
