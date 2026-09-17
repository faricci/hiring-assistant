"""`hiring prep` — generate a pre-filled interview prep file from the team template.

Deterministic step: copy the template verbatim, substitute candidate name/date and
the seniority calibration note, and leave ``<!-- AGENT-FILL: key | instructions -->``
markers for the LLM agent to complete from the candidate's CV. This keeps the
agent's job to a few hundred lines instead of regenerating the whole document.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
from pathlib import Path

from . import config as cfg

CALIBRATION = {
    "senior": (
        "Senior (5+ years)",
        "ownership, decision making, architecture, trade-offs, technical leadership; "
        "questions target depth, design and measured impact.",
    ),
    "mid": (
        "Mid-level (3-5 years)",
        "a mix of technical and behavioural; more technical than junior, "
        "less architectural than senior.",
    ),
    "junior": (
        "Junior (< 3 years)",
        "mindset, learning speed, potential and ownership; attitude and curiosity "
        "weigh more than technical depth.",
    ),
}

_MARKER = re.compile(r"<!--\s*AGENT-FILL:")


def run(args: argparse.Namespace) -> int:
    config = cfg.load_config()
    team = cfg.active_team(config)
    language = args.language or config.get("language", team.get("default_language", "en"))

    templates = team.get("templates", {})
    if language not in templates:
        raise cfg.ConfigError(
            f"Team '{team['id']}' has no template for language '{language}'."
        )
    template_path = cfg.team_dir(team) / templates[language]
    if not template_path.is_file():
        raise FileNotFoundError(f"Template not found: {template_path}")

    label, focus = CALIBRATION[args.seniority]
    name = args.name.strip()
    today = _dt.date.today().isoformat()

    text = template_path.read_text(encoding="utf-8")
    text = (
        text.replace("{{CANDIDATE_NAME}}", name)
        .replace("{{DATE}}", today)
        .replace("{{SENIORITY_LABEL}}", label)
        .replace("{{SENIORITY_FOCUS}}", focus)
    )

    out_dir = cfg.candidates_dir(config) / "preparation_md"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{cfg.safe_name(name)}_interview_prep.md"

    if out_path.exists() and not args.force:
        print(f"error: file already exists: {out_path} (use --force to overwrite)")
        return 1

    cfg.write_text_resilient(out_path, text)
    markers = sum(1 for line in text.splitlines() if _MARKER.search(line))

    rel = out_path.relative_to(cfg.PROJECT_ROOT)
    print(f"Created: {rel}")
    print(f"  language: {language}  seniority: {args.seniority}")
    print(f"  AGENT-FILL markers to complete: {markers}")
    return 0
