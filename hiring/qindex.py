"""`hiring index` — build a token-efficient JSON index of the team question bank.

The agent reads the small index (categories + line ranges + tags) instead of the
whole question bank, then reads only the relevant sections.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
from pathlib import Path

from . import config as cfg

GREEN, YELLOW, RED = "\U0001F7E2", "\U0001F7E1", "\U0001F534"
_H2 = re.compile(r"^##\s+(?!#)(.+?)\s*$")
_H3 = re.compile(r"^###\s+")
_QUOTE_BULLET = re.compile(r'^\s*-\s+\*?"')
_TABLE_ROW = re.compile(r"^\|.*\|.*\|")


def _tags_for(name: str, tag_map: dict[str, list[str]]) -> list[str]:
    lowered = name.lower()
    for key, tags in tag_map.items():
        if key.lower() in lowered:
            return tags
    words = re.sub(r"[^a-z0-9\s]", "", lowered).split()
    return [w for w in words if len(w) > 2]


def _close(category: dict, end_line: int, out: list[dict]) -> None:
    if category:
        category["end_line"] = end_line
        out.append(category)


def build_index(bank_path: Path, tag_map: dict[str, list[str]]) -> dict:
    lines = bank_path.read_text(encoding="utf-8").splitlines()
    categories: list[dict] = []
    current: dict = {}

    for i, line in enumerate(lines):
        line_no = i + 1
        m = _H2.match(line)
        if m:
            heading = m.group(1).strip()
            if re.match(r"^(Index|Indice|Log|Changelog)", heading, re.IGNORECASE):
                continue
            _close(current, line_no - 1, categories)
            name = re.split(r"\s+[—-]\s+", heading)[0].strip()
            current = {
                "name": name,
                "start_line": line_no,
                "end_line": line_no,
                "question_count": 0,
                "exercise_count": 0,
                "levels": {"base": 0, "intermediate": 0, "advanced": 0},
                "has_subsections": False,
                "tags": _tags_for(name, tag_map),
            }
            continue
        if not current:
            continue
        if _H3.match(line):
            current["has_subsections"] = True
        has_level = False
        if GREEN in line:
            current["levels"]["base"] += 1
            has_level = True
        if YELLOW in line:
            current["levels"]["intermediate"] += 1
            has_level = True
        if RED in line:
            current["levels"]["advanced"] += 1
            has_level = True
        if has_level:
            current["question_count"] += (
                (GREEN in line) + (YELLOW in line) + (RED in line)
            )
        elif _QUOTE_BULLET.match(line):
            current["question_count"] += 1
        if _TABLE_ROW.match(line) and not line.lstrip().startswith("|--"):
            current["exercise_count"] += 1

    _close(current, len(lines), categories)

    return {
        "_meta": {
            "description": (
                "Structured index of the team question bank. Read this instead of "
                "the full file, then use start_line/end_line to read only relevant "
                "sections."
            ),
            "total_lines": len(lines),
            "generated_at": _dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "generator": "hiring index",
        },
        "categories": categories,
    }


def run(_args: argparse.Namespace) -> int:
    config = cfg.load_config()
    team = cfg.active_team(config)
    team_path = cfg.team_dir(team)

    bank_rel = team.get("question_bank", "question-bank.md")
    bank_path = team_path / bank_rel
    if not bank_path.is_file():
        raise FileNotFoundError(f"Question bank not found: {bank_path}")

    tag_map = team.get("question_tag_map", {})
    index = build_index(bank_path, tag_map)

    out_rel = team.get("question_bank_index", "question-bank-index.json")
    out_path = team_path / out_rel
    cfg.write_text_resilient(out_path, json.dumps(index, indent=2, ensure_ascii=False) + "\n")

    total_q = sum(c["question_count"] for c in index["categories"])
    total_e = sum(c["exercise_count"] for c in index["categories"])
    print(f"Question bank index generated: {out_path.relative_to(cfg.PROJECT_ROOT)}")
    print(f"  categories: {len(index['categories'])}")
    print(f"  questions:  {total_q}")
    print(f"  exercises:  {total_e}")
    return 0
