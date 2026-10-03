# Voice recordings — tracking your pronunciation

Short recordings of you speaking Russian, kept so you can **hear your own progress**: play today's recording next to one from three months ago.

## ⚠️ Privacy first

This repository is **public** on GitHub. Anything committed here — including audio — is visible to anyone, and stays in git history even if you delete it later. So:

* **Audio files are not committed unless you explicitly say so.** By default they stay in this folder locally (git ignores them).
* To keep them in git safely, first make the repository **private** (GitHub → repository **Settings → General → Danger Zone → Change visibility**), then ask your tutor to commit the recordings.
* Or keep the audio on your own device/cloud drive and only keep the *log below* in the repo.

## Naming

```
recordings/stage-<N>/YYYY-MM-DD_lesson-<NN>_<a|b|c…>_<short-slug>.m4a
```

Example: `recordings/stage-0/2026-10-03_lesson-01_a_read-words.m4a`

## Benchmarks (so recordings are comparable)

Record the **same prompts** at each milestone and compare:

| When | What to record |
|---|---|
| Lesson 1 *(baseline)* | **так · мак · акт · ток** · **Там ма́ма.** · **Кто там? — Ма́ма.** |
| Lesson 9 (Stage 0 checkpoint) | the same lines again + the Part B word list from the test |
| End of every later stage | the same lines + the dialogue from the stage's last lesson |

## How to self-check (your tutor can't hear audio)

Your tutor can store and organise recordings but **cannot listen to them in this environment** — so it won't pretend to judge your accent. To get real feedback:

1. Look up each word on [forvo.com](https://forvo.com), listen to 2–3 native speakers, then play your recording right after.
2. Check the specific points the lesson trains. **Stage 0 checklist:**
   - [ ] **к, т, п** — no puff of air (hold a hand in front of your mouth)
   - [ ] **т, д, н, л** — tongue touches the back of the upper teeth
   - [ ] **о** — short and pure (no *oh-w*); unstressed **о** sounds like **а**
   - [ ] **ма́ма** — stress on the *first* syllable, the second **а** weaker
   - [ ] **кто** — *k-to* with no vowel between
   - [ ] statements fall at the end; yes/no questions rise on the key word
3. Ask a native speaker or an online tutor (see `reference/resources.md`) to listen to a recording now and then.

## Log

| Date | Lesson | Prompt | File | Length | In git? |
|---|---|---|---|:-:|---|
| 2026-10-03 | 1 | Read aloud: **так, мак, акт, ток** | `stage-0/2026-10-03_lesson-01_a_read-words.m4a` | 0:21 | no — local only |
| 2026-10-03 | 1 | Say: **Там ма́ма.** ("Mom is there.") | `stage-0/2026-10-03_lesson-01_b_mom-is-there.m4a` | 0:03 | no — local only |
| 2026-10-03 | 1 | Say: **Кто там? — Ма́ма.** | `stage-0/2026-10-03_lesson-01_c_who-is-there.m4a` | 0:06 | no — local only |

*Self-assessment notes:* *(add your own observations after comparing with Forvo — e.g. "т too aspirated; stress on ма́ма OK")*
