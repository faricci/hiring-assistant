"""`hiring scorecard` — init / summary / compare candidate scorecards.

Scoring is data-driven: the categories, dimensions and weights come from the
active team's ``score_model`` in team.json, so a different team can score on
different axes without changing this code.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
from pathlib import Path
from typing import Any

from . import config as cfg

DEFAULT_THRESHOLDS = {
    "strong": 4.0,
    "recommend": 3.5,
    "weak": 3.0,
    "behaviour_floor": 3.0,
}


def _scorecards_dir(config: dict[str, Any]) -> Path:
    path = cfg.candidates_dir(config) / "scorecards"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _file_token(name: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in name.strip())


def _weighted(scorecard: dict, score_model: dict) -> dict:
    result: dict[str, float] = {}
    total = 0.0
    for category, spec in score_model.items():
        dims = spec["dimensions"]
        values = scorecard.get("scores", {}).get(category, {})
        avg = round(sum(values.get(d, 0) for d in dims) / len(dims), 2) if dims else 0.0
        result[f"{category}_avg"] = avg
        total += avg * spec["weight"]
    result["weighted_total"] = round(total, 2)
    return result


def _recommend(weighted: float, behaviour_avg: float, thr: dict) -> str:
    if behaviour_avg < thr["behaviour_floor"]:
        return "behaviour_review_required"
    if weighted >= thr["strong"]:
        return "strong_recommendation"
    if weighted >= thr["recommend"]:
        return "recommendation"
    if weighted >= thr["weak"]:
        return "not_brilliant"
    return "not_proceeding"


def _behaviour_category(score_model: dict) -> str:
    for name in score_model:
        if name in ("behaviour", "behavior"):
            return name
    return next(iter(score_model))


# --- init -----------------------------------------------------------------
def _init(args: argparse.Namespace, config: dict, team: dict) -> int:
    if not args.name:
        raise cfg.ConfigError("--name is required for 'scorecard init'.")
    score_model = team["score_model"]
    directory = _scorecards_dir(config)
    path = directory / f"{_file_token(args.name)}_round{args.round}.json"
    if path.exists():
        print(f"Scorecard already exists: {path.relative_to(cfg.PROJECT_ROOT)}")
        return 1

    scores = {
        category: {dim: 0 for dim in spec["dimensions"]}
        for category, spec in score_model.items()
    }
    scorecard = {
        "candidate": args.name.strip(),
        "round": args.round,
        "date": _dt.date.today().isoformat(),
        "status": "pending",
        "contribution_archetype": "unclear",
        "scores": scores,
        "weighted_score": 0,
        "recommendation": "pending",
        "strengths": [],
        "concerns": [],
        "narrative": {category: "" for category in score_model} | {"overall": ""},
        "holistic_axes": {axis: 0 for axis in team.get("holistic_axes", [])},
        "evidence": {
            phase: {"status": "not_started", "summary": ""}
            for phase in ("cv_screening", "career_path_review",
                          "structured_interview", "work_sample", "evidence_review")
        },
        "pre_employment_checks": {
            "reference_check": {"owner": "HR", "status": "not_started", "note": ""},
            "background_check": {"owner": "HR/provider", "status": "not_started", "note": ""},
        },
    }
    cfg.write_text_resilient(path, json.dumps(scorecard, indent=2, ensure_ascii=False) + "\n")
    print(f"Scorecard created: {path.relative_to(cfg.PROJECT_ROOT)}")
    return 0


# --- summary --------------------------------------------------------------
def _load_latest(directory: Path, name: str) -> dict | None:
    token = _file_token(name)
    files = sorted(directory.glob(f"{token}_round*.json"), reverse=True)
    if not files:
        return None
    return json.loads(files[0].read_text(encoding="utf-8"))


def _summary(args: argparse.Namespace, config: dict, team: dict) -> int:
    if not args.name:
        raise cfg.ConfigError("--name is required for 'scorecard summary'.")
    data = _load_latest(_scorecards_dir(config), args.name)
    if data is None:
        print(f"No scorecards found for: {args.name}")
        return 1
    score_model = team["score_model"]
    calc = _weighted(data, score_model)
    print(f"\n=== {data['candidate']} — Round {data['round']} ({data['date']}) ===")
    for category, spec in score_model.items():
        pct = int(spec["weight"] * 100)
        print(f"{category.capitalize()} ({pct}%) avg: {calc[f'{category}_avg']} / 5")
    print(f"Weighted total:            {calc['weighted_total']} / 5")
    print(f"Recommendation (provisional): {data.get('recommendation', 'pending')}")
    print(f"Contribution archetype:    {data.get('contribution_archetype', 'unclear')}")
    checks = data.get("pre_employment_checks", {})
    print(f"Reference check (HR, not scored):  "
          f"{checks.get('reference_check', {}).get('status', 'n/a')}")
    print(f"Background check (HR, not scored):  "
          f"{checks.get('background_check', {}).get('status', 'n/a')}")
    for label, key in (("Strengths", "strengths"), ("Concerns", "concerns")):
        items = [x for x in data.get(key, []) if x]
        if items:
            print(f"\n{label}:")
            for item in items:
                print(f"  - {item}")
    return 0


# --- compare --------------------------------------------------------------
def _compare(_args: argparse.Namespace, config: dict, team: dict) -> int:
    directory = _scorecards_dir(config)
    files = sorted(directory.glob("*.json"))
    if not files:
        print(f"No scorecards found in: {directory.relative_to(cfg.PROJECT_ROOT)}")
        return 1

    latest: dict[str, dict] = {}
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        name = data["candidate"]
        if name not in latest or data["round"] > latest[name]["round"]:
            latest[name] = data

    score_model = team["score_model"]
    thresholds = team.get("recommendation_thresholds", DEFAULT_THRESHOLDS)
    names = sorted(latest)
    rows: list[str] = [f"## Candidate Comparison — {_dt.date.today().isoformat()}", ""]
    rows.append("| Axis | " + " | ".join(names) + " |")
    rows.append("|------|" + "|".join(["------"] * len(names)) + "|")

    for axis in team.get("holistic_axes", []):
        cells = [str(latest[n].get("holistic_axes", {}).get(axis, "-")) for n in names]
        rows.append(f"| {axis.replace('_', ' ').title()} | " + " | ".join(cells) + " |")

    rows.append("|------|" + "|".join(["------"] * len(names)) + "|")
    calcs = {n: _weighted(latest[n], score_model) for n in names}
    for category, spec in score_model.items():
        pct = int(spec["weight"] * 100)
        cells = [str(calcs[n][f"{category}_avg"]) for n in names]
        rows.append(f"| {category.capitalize()} ({pct}%) | " + " | ".join(cells) + " |")
    weighted_cells = [f"**{calcs[n]['weighted_total']}**" for n in names]
    rows.append("| **Weighted Score** | " + " | ".join(weighted_cells) + " |")

    behaviour = _behaviour_category(score_model)
    for n in names:
        calcs[n]["recommendation"] = latest[n].get("recommendation") or _recommend(
            calcs[n]["weighted_total"], calcs[n][f"{behaviour}_avg"], thresholds
        )
    rows.append("| Provisional recommendation | "
                + " | ".join(calcs[n]["recommendation"] for n in names) + " |")
    rows.append("| Contribution archetype | "
                + " | ".join(latest[n].get("contribution_archetype", "unclear") for n in names)
                + " |")
    for label, key in (("Reference check (HR)", "reference_check"),
                       ("Background check (HR)", "background_check")):
        cells = [latest[n].get("pre_employment_checks", {}).get(key, {}).get("status", "n/a")
                 for n in names]
        rows.append(f"| {label} | " + " | ".join(cells) + " |")

    output = "\n".join(rows) + "\n"
    out_path = directory / "_comparison.md"
    cfg.write_text_resilient(out_path, output)
    print(output)
    print(f"Comparison written to: {out_path.relative_to(cfg.PROJECT_ROOT)}")
    return 0


def run(args: argparse.Namespace) -> int:
    config = cfg.load_config()
    team = cfg.active_team(config)
    return {"init": _init, "summary": _summary, "compare": _compare}[args.mode](
        args, config, team
    )
