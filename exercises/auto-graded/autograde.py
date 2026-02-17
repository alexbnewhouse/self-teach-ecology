#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
BANKS_DIR = BASE_DIR / "banks"
RUBRICS_DIR = BASE_DIR / "rubrics"
RESULTS_PATH = BASE_DIR / "results" / "results.jsonl"


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure_results_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.touch()


def record_result(record: dict[str, Any], results_path: Path) -> None:
    ensure_results_file(results_path)
    with results_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def parse_bank_path(bank_arg: str | None) -> Path:
    if not bank_arg:
        return BANKS_DIR / "module-01-foundations.json"
    candidate = Path(bank_arg)
    if not candidate.is_absolute():
        direct = (Path.cwd() / candidate).resolve()
        if direct.exists():
            return direct
        return (BANKS_DIR / bank_arg).resolve()
    return candidate


def parse_rubric_path(rubric_arg: str | None) -> Path:
    if not rubric_arg:
        return RUBRICS_DIR / "restoration-practicum.json"
    candidate = Path(rubric_arg)
    if not candidate.is_absolute():
        direct = (Path.cwd() / candidate).resolve()
        if direct.exists():
            return direct
        return (RUBRICS_DIR / rubric_arg).resolve()
    return candidate


def print_choices(choices: list[str]) -> None:
    for idx, choice in enumerate(choices, start=1):
        print(f"  {idx}. {choice}")


def prompt_text(prompt: str) -> str:
    return input(f"{prompt}\n> ").strip()


def prompt_single_choice(prompt: str, choices: list[str]) -> str:
    print(prompt)
    print_choices(choices)
    while True:
        raw = input("> ").strip()
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(choices):
                return choices[idx - 1]
        if raw in choices:
            return raw
        print("Enter a valid option number or exact choice text.")


def prompt_multi_select(prompt: str, choices: list[str]) -> list[str]:
    print(prompt)
    print("Select one or more options separated by commas.")
    print_choices(choices)
    while True:
        raw = input("> ").strip()
        if not raw:
            print("Please enter at least one option.")
            continue

        parts = [part.strip() for part in raw.split(",") if part.strip()]
        picked: list[str] = []
        valid = True
        for part in parts:
            if part.isdigit():
                idx = int(part)
                if 1 <= idx <= len(choices):
                    picked.append(choices[idx - 1])
                else:
                    valid = False
                    break
            elif part in choices:
                picked.append(part)
            else:
                valid = False
                break

        if valid and picked:
            return sorted(set(picked))
        print("Invalid selection. Use comma-separated numbers or exact choice text.")


def grade_numeric(user_answer: str, expected: float, tolerance: float) -> bool:
    try:
        value = float(user_answer)
    except ValueError:
        return False
    return abs(value - expected) <= tolerance


def grade_short_text(answer: str, question: dict[str, Any]) -> bool:
    normalized = normalize_text(answer)

    accepted_answers = question.get("accepted_answers", [])
    if accepted_answers:
        accepted = {normalize_text(item) for item in accepted_answers}
        if normalized in accepted:
            return True

    contains_all = question.get("contains_all", [])
    if contains_all:
        if all(normalize_text(token) in normalized for token in contains_all):
            return True

    contains_any = question.get("contains_any", [])
    if contains_any:
        min_matches = int(question.get("min_matches", 1))
        matches = sum(1 for token in contains_any if normalize_text(token) in normalized)
        if matches >= min_matches:
            return True

    return False


def grade_question(question: dict[str, Any], user_answer: Any) -> tuple[bool, str]:
    q_type = question["type"]
    explanation = question.get("explanation", "")

    if q_type == "multiple_choice":
        correct = normalize_text(str(user_answer)) == normalize_text(str(question["answer"]))
        return correct, explanation

    if q_type == "multi_select":
        expected = sorted({normalize_text(item) for item in question["answers"]})
        submitted = sorted({normalize_text(item) for item in user_answer})
        correct = expected == submitted
        return correct, explanation

    if q_type == "numeric":
        expected = float(question["answer"])
        tolerance = float(question.get("tolerance", 0.01))
        correct = grade_numeric(str(user_answer), expected, tolerance)
        return correct, explanation

    if q_type == "short_text":
        correct = grade_short_text(str(user_answer), question)
        return correct, explanation

    raise ValueError(f"Unsupported question type: {q_type}")


def run_interactive_bank(bank_path: Path, learner: str, results_path: Path, fail_on_review: bool) -> int:
    bank = load_json(bank_path)
    title = bank.get("title", bank_path.stem)
    module = bank.get("module", "unspecified")
    questions = bank.get("questions", [])
    pass_threshold = float(bank.get("pass_threshold", 0.7))

    if not questions:
        raise ValueError("Question bank is empty.")

    print(f"\n=== {title} ===")
    print(f"Module: {module}")
    print(f"Questions: {len(questions)}\n")

    earned = 0.0
    total = 0.0
    details: list[dict[str, Any]] = []

    for index, question in enumerate(questions, start=1):
        q_id = question.get("id", f"Q{index}")
        q_type = question["type"]
        points = float(question.get("points", 1.0))
        total += points

        print(f"\n[{index}/{len(questions)}] {q_id} ({points:g} pt)")
        if q_type == "multiple_choice":
            response = prompt_single_choice(question["prompt"], question["choices"])
        elif q_type == "multi_select":
            response = prompt_multi_select(question["prompt"], question["choices"])
        else:
            response = prompt_text(question["prompt"])

        correct, explanation = grade_question(question, response)
        if correct:
            earned += points
            print("✓ Correct")
        else:
            print("✗ Not correct")

        if explanation:
            print(f"  {explanation}")

        details.append(
            {
                "id": q_id,
                "type": q_type,
                "points": points,
                "correct": correct,
                "response": response,
            }
        )

    score_pct = (earned / total) if total else 0.0
    passed = score_pct >= pass_threshold

    print("\n=== Summary ===")
    print(f"Score: {earned:g}/{total:g} ({score_pct * 100:.1f}%)")
    print("Result: PASS" if passed else "Result: REVIEW")

    record = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": "bank",
        "learner": learner,
        "module": module,
        "title": title,
        "bank_path": str(bank_path),
        "score_earned": earned,
        "score_total": total,
        "score_percent": round(score_pct * 100, 2),
        "pass_threshold_percent": round(pass_threshold * 100, 2),
        "passed": passed,
        "details": details,
    }
    record_result(record, results_path)
    print(f"Saved result to: {results_path}")

    return 2 if (fail_on_review and not passed) else 0


def evaluate_rubric_check(submission_text: str, check: dict[str, Any]) -> bool:
    mode = check["mode"]
    normalized = normalize_text(submission_text)

    if mode == "word_count_min":
        min_words = int(check["min_words"])
        word_count = len(re.findall(r"\b\w+\b", submission_text))
        return word_count >= min_words

    if mode == "contains_all":
        tokens = [normalize_text(item) for item in check.get("tokens", [])]
        return all(token in normalized for token in tokens)

    if mode == "contains_any":
        tokens = [normalize_text(item) for item in check.get("tokens", [])]
        min_matches = int(check.get("min_matches", 1))
        matches = sum(1 for token in tokens if token in normalized)
        return matches >= min_matches

    if mode == "heading_exists":
        headings = [normalize_text(item) for item in check.get("headings", [])]
        lines = [normalize_text(line.strip("# ")) for line in submission_text.splitlines() if line.strip().startswith("#")]
        return any(heading in lines for heading in headings)

    raise ValueError(f"Unsupported rubric mode: {mode}")


def run_rubric_grader(
    rubric_path: Path,
    submission_path: Path,
    learner: str,
    results_path: Path,
    fail_on_review: bool,
) -> int:
    rubric = load_json(rubric_path)
    with submission_path.open("r", encoding="utf-8") as handle:
        submission_text = handle.read()

    title = rubric.get("title", rubric_path.stem)
    module = rubric.get("module", "unspecified")
    checks = rubric.get("checks", [])

    if not checks:
        raise ValueError("Rubric contains no checks.")

    earned = 0.0
    total = 0.0
    details: list[dict[str, Any]] = []

    print(f"\n=== Rubric: {title} ===")
    print(f"Submission: {submission_path}\n")

    for check in checks:
        weight = float(check.get("weight", 1.0))
        total += weight
        passed = evaluate_rubric_check(submission_text, check)
        if passed:
            earned += weight

        label = check.get("label", check.get("id", "Unnamed check"))
        print(f"{'✓' if passed else '✗'} {label} ({weight:g} pt)")

        details.append(
            {
                "id": check.get("id", label),
                "label": label,
                "weight": weight,
                "passed": passed,
                "mode": check.get("mode"),
            }
        )

    score_pct = (earned / total) if total else 0.0
    pass_threshold = float(rubric.get("pass_threshold", 0.7))
    passed = score_pct >= pass_threshold

    print("\n=== Summary ===")
    print(f"Score: {earned:g}/{total:g} ({score_pct * 100:.1f}%)")
    print("Result: PASS" if passed else "Result: REVIEW")

    record = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": "rubric",
        "learner": learner,
        "module": module,
        "title": title,
        "rubric_path": str(rubric_path),
        "submission_path": str(submission_path),
        "score_earned": earned,
        "score_total": total,
        "score_percent": round(score_pct * 100, 2),
        "pass_threshold_percent": round(pass_threshold * 100, 2),
        "passed": passed,
        "details": details,
    }
    record_result(record, results_path)
    print(f"Saved result to: {results_path}")

    return 2 if (fail_on_review and not passed) else 0


def list_banks() -> int:
    banks = sorted(BANKS_DIR.glob("*.json"))
    if not banks:
        print("No banks found.")
        return 0

    print("Available banks:")
    for bank in banks:
        print(f"- {bank.name}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Interactive ecology exercise auto-grader")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_cmd = subparsers.add_parser("run", help="Run interactive bank")
    run_cmd.add_argument("--bank", help="Bank filename in banks/ or path to JSON file")
    run_cmd.add_argument("--learner", default="anonymous", help="Learner identifier saved in results")
    run_cmd.add_argument(
        "--results",
        default=str(RESULTS_PATH),
        help="Path to JSONL results file",
    )
    run_cmd.add_argument(
        "--fail-on-review",
        action="store_true",
        help="Return non-zero exit code if score is below pass threshold",
    )

    rubric_cmd = subparsers.add_parser("rubric", help="Run checklist-style rubric grading")
    rubric_cmd.add_argument("--submission", required=True, help="Path to markdown submission")
    rubric_cmd.add_argument("--rubric", help="Rubric filename in rubrics/ or path to JSON file")
    rubric_cmd.add_argument("--learner", default="anonymous", help="Learner identifier saved in results")
    rubric_cmd.add_argument(
        "--results",
        default=str(RESULTS_PATH),
        help="Path to JSONL results file",
    )
    rubric_cmd.add_argument(
        "--fail-on-review",
        action="store_true",
        help="Return non-zero exit code if score is below pass threshold",
    )

    subparsers.add_parser("list-banks", help="List available question banks")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "list-banks":
            return list_banks()

        if args.command == "run":
            results_path = Path(args.results).resolve()
            learner = str(args.learner)
            bank_path = parse_bank_path(args.bank)
            return run_interactive_bank(
                bank_path=bank_path,
                learner=learner,
                results_path=results_path,
                fail_on_review=bool(args.fail_on_review),
            )

        if args.command == "rubric":
            results_path = Path(args.results).resolve()
            learner = str(args.learner)
            rubric_path = parse_rubric_path(args.rubric)
            submission_path = Path(args.submission).resolve()
            return run_rubric_grader(
                rubric_path=rubric_path,
                submission_path=submission_path,
                learner=learner,
                results_path=results_path,
                fail_on_review=bool(args.fail_on_review),
            )

        parser.print_help()
        return 1
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
