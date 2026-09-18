import argparse
import json

import pytest

from hiring import config as cfg
from hiring import scorecard


def _ns(mode, name=None, round=1):
    return argparse.Namespace(mode=mode, name=name, round=round)


def test_init_creates_zeroed_scorecard(tmp_project, active_config):
    rc = scorecard.run(_ns("init", name="Jane Doe", round=1))
    assert rc == 0
    path = cfg.candidates_dir(active_config) / "scorecards" / "Jane_Doe_round1.json"
    assert path.is_file()
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["candidate"] == "Jane Doe"
    assert data["scores"]["behaviour"] == {"energy": 0, "communication": 0}
    assert data["recommendation"] == "pending"


def test_init_requires_name(tmp_project, active_config):
    with pytest.raises(cfg.ConfigError):
        scorecard.run(_ns("init", name=None))


def test_init_refuses_to_overwrite_existing_round(tmp_project, active_config, capsys):
    scorecard.run(_ns("init", name="Jane Doe"))
    rc = scorecard.run(_ns("init", name="Jane Doe"))
    assert rc == 1
    assert "already exists" in capsys.readouterr().out


def _write_scorecard(config, name, round_, scores, recommendation="pending", archetype="unclear"):
    directory = cfg.candidates_dir(config) / "scorecards"
    directory.mkdir(parents=True, exist_ok=True)
    data = {
        "candidate": name,
        "round": round_,
        "date": "2026-01-01",
        "contribution_archetype": archetype,
        "scores": scores,
        "recommendation": recommendation,
        "strengths": ["Good communicator"],
        "concerns": [],
        "holistic_axes": {"ownership": 4, "curiosity": 5},
        "pre_employment_checks": {
            "reference_check": {"status": "not_started"},
            "background_check": {"status": "not_started"},
        },
    }
    path = directory / f"{name.replace(' ', '_')}_round{round_}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_summary_computes_weighted_score(tmp_project, active_config, capsys):
    _write_scorecard(active_config, "Jane Doe", 1, scores={
        "behaviour": {"energy": 4, "communication": 4},
        "skills": {"coding": 3, "debugging": 5},
        "knowledge": {"fundamentals": 4},
    })
    rc = scorecard.run(_ns("summary", name="Jane Doe"))
    assert rc == 0
    out = capsys.readouterr().out
    assert "Weighted total:" in out
    assert "4.0 / 5" in out


def test_summary_no_scorecard_found(tmp_project, active_config, capsys):
    rc = scorecard.run(_ns("summary", name="Ghost"))
    assert rc == 1
    assert "No scorecards found" in capsys.readouterr().out


def test_summary_uses_latest_round(tmp_project, active_config, capsys):
    _write_scorecard(active_config, "Jane Doe", 1, scores={
        "behaviour": {"energy": 2, "communication": 2},
        "skills": {"coding": 2, "debugging": 2},
        "knowledge": {"fundamentals": 2},
    })
    _write_scorecard(active_config, "Jane Doe", 2, scores={
        "behaviour": {"energy": 5, "communication": 5},
        "skills": {"coding": 5, "debugging": 5},
        "knowledge": {"fundamentals": 5},
    })
    rc = scorecard.run(_ns("summary", name="Jane Doe"))
    assert rc == 0
    out = capsys.readouterr().out
    assert "Round 2" in out
    assert "5.0 / 5" in out


def test_compare_ranks_and_writes_comparison_md(tmp_project, active_config):
    _write_scorecard(active_config, "Alice", 1, scores={
        "behaviour": {"energy": 5, "communication": 5},
        "skills": {"coding": 5, "debugging": 5},
        "knowledge": {"fundamentals": 5},
    })
    _write_scorecard(active_config, "Bob", 1, scores={
        "behaviour": {"energy": 2, "communication": 2},
        "skills": {"coding": 2, "debugging": 2},
        "knowledge": {"fundamentals": 2},
    })
    rc = scorecard.run(_ns("compare"))
    assert rc == 0
    text = (cfg.candidates_dir(active_config) / "scorecards" / "_comparison.md").read_text(encoding="utf-8")
    assert "Alice" in text and "Bob" in text
    assert "**5.0**" in text
    assert "**2.0**" in text


def test_compare_no_scorecards(tmp_project, active_config, capsys):
    rc = scorecard.run(_ns("compare"))
    assert rc == 1
    assert "No scorecards found" in capsys.readouterr().out


@pytest.mark.parametrize("weighted,behaviour_avg,expected", [
    (4.5, 4.0, "strong_recommendation"),
    (3.7, 4.0, "recommendation"),
    (3.2, 4.0, "not_brilliant"),
    (2.0, 4.0, "not_proceeding"),
    (4.5, 2.0, "behaviour_review_required"),  # behaviour floor overrides a high score
])
def test_recommend_thresholds(weighted, behaviour_avg, expected):
    assert scorecard._recommend(weighted, behaviour_avg, scorecard.DEFAULT_THRESHOLDS) == expected
