"""Shared pytest fixtures.

Every fixture here isolates a test from the developer's real
``config/hiring.config.json`` and the real ``teams/`` content by monkeypatching
the ``hiring.config`` module's path constants to point into a throwaway
``tmp_path``. No test in this suite touches the real config file or writes
into the real ``candidates/`` workspace.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# hiring/ is a plain package with no packaging metadata (see hiring.py's own
# sys.path bootstrap) -- mirror that here so `import hiring` works whether the
# suite is invoked as `pytest` or `python -m pytest`, from any cwd.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hiring import config as cfg  # noqa: E402


@pytest.fixture
def tmp_project(tmp_path, monkeypatch):
    """An isolated fake project root with one minimal, synthetic team pack.

    Deliberately not the real 'devops-platform' pack: this keeps core-logic
    tests fast and immune to future edits of that pack's content. Returns the
    fake project root (== tmp_path).
    """
    teams_dir = tmp_path / "teams" / "acme"
    (teams_dir / "templates").mkdir(parents=True)
    (tmp_path / "config").mkdir()

    team_json = {
        "id": "acme",
        "display_name": "Acme Team",
        "default_language": "en",
        "score_model": {
            "behaviour": {"weight": 0.4, "dimensions": ["energy", "communication"]},
            "skills": {"weight": 0.35, "dimensions": ["coding", "debugging"]},
            "knowledge": {"weight": 0.25, "dimensions": ["fundamentals"]},
        },
        "holistic_axes": ["ownership", "curiosity"],
        "templates": {"en": "templates/interview-en.md"},
        "question_bank": "question-bank.md",
    }
    (teams_dir / "team.json").write_text(json.dumps(team_json), encoding="utf-8")

    template_text = (
        "# Prep - {{CANDIDATE_NAME}}\n"
        "Seniority: {{SENIORITY_LABEL}} - {{SENIORITY_FOCUS}}\n"
        "Date: {{DATE}}\n\n"
        "<!-- AGENT-FILL: coverage | fill this in -->\n"
        "<!-- AGENT-FILL: flags | fill this in -->\n"
    )
    (teams_dir / "templates" / "interview-en.md").write_text(template_text, encoding="utf-8")

    bank_text = (
        '## Terraform\n'
        '- \U0001F7E2 *"Question one?"*\n'
        '- \U0001F7E1 *"Question two?"*\n'
        '\n'
        '## Kubernetes — advanced\n'
        '- \U0001F534 *"Question three?"*\n'
    )
    (teams_dir / "question-bank.md").write_text(bank_text, encoding="utf-8")

    monkeypatch.setattr(cfg, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(cfg, "CONFIG_PATH", tmp_path / "config" / "hiring.config.json")
    monkeypatch.setattr(cfg, "TEAMS_DIR", tmp_path / "teams")

    return tmp_path


@pytest.fixture
def active_config(tmp_project):
    """Write a valid hiring.config.json selecting the synthetic 'acme' team."""
    config = {
        "team": "acme",
        "language": "en",
        "exercises_repo": "",
        "candidates_dir": "candidates",
    }
    cfg.save_config(config)
    return config
