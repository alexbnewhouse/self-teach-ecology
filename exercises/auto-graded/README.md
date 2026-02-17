# Auto-Graded Interactive Exercises (MVP)

This folder provides a lightweight Python auto-grading system for interactive exercises.

## What It Supports

- Interactive question banks (`multiple_choice`, `multi_select`, `numeric`, `short_text`)
- Checklist-style rubric grading for structured written drafts
- JSONL result logging for progress tracking

## Quick Start

From the repository root:

```bash
python3 exercises/auto-graded/autograde.py list-banks
python3 exercises/auto-graded/autograde.py run --bank module-01-foundations.json --learner alex
```

Run the restoration practicum rubric checker against a draft Markdown file:

```bash
python3 exercises/auto-graded/autograde.py rubric \
  --rubric restoration-practicum.json \
  --submission exercises/restoration-practicum.md \
  --learner alex
```

Results are appended to:

- `exercises/auto-graded/results/results.jsonl`

## File Layout

- `autograde.py` – CLI runner and grader
- `banks/` – interactive objective question banks
- `rubrics/` – rule-based rubric checks for written submissions
- `results/` – persistent run logs

Current bank coverage includes:

- Core modules: 00, 01, 02, 03, 04, 05, 06, 07, 08
- Specialization tracks: computational ecology, restoration ecology (advanced), systems ecology & complexity

## Notes

- The rubric checker is a **first-pass heuristic**, not a replacement for qualitative expert feedback.
- You can add new banks/rubrics by copying existing JSON files and adjusting fields.
