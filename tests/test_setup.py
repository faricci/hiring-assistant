import argparse

import pytest

from hiring import config as cfg
from hiring import setup as setup_cmd


def _ns(**kwargs):
    defaults = dict(team=None, exercises_repo=None, language=None,
                     non_interactive=True, skip_deps=True)
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


def test_list_teams_reports_none_when_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cfg, "TEAMS_DIR", tmp_path / "teams")
    rc = setup_cmd.list_teams(argparse.Namespace())
    assert rc == 1
    assert "No team packs found" in capsys.readouterr().out


def test_list_teams_lists_and_marks_active(tmp_project, active_config, capsys):
    rc = setup_cmd.list_teams(argparse.Namespace())
    assert rc == 0
    out = capsys.readouterr().out
    assert "acme: Acme Team" in out
    assert "(active)" in out


def test_run_writes_config_non_interactive(tmp_project):
    rc = setup_cmd.run(_ns(team="acme", language="en"))
    assert rc == 0
    config = cfg.load_config()
    assert config["team"] == "acme"
    assert config["language"] == "en"
    for sub in ("cv_pdf", "cv_md", "preparation_md", "takehome_md", "transcript_md", "scorecards"):
        assert (cfg.candidates_dir(config) / sub).is_dir()


def test_run_non_interactive_requires_team(tmp_project):
    with pytest.raises(cfg.ConfigError, match="--team is required"):
        setup_cmd.run(_ns(team=None))


def test_run_rejects_invalid_language(tmp_project):
    with pytest.raises(cfg.ConfigError, match="Language must be"):
        setup_cmd.run(_ns(team="acme", language="fr"))


def test_run_no_teams_available(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cfg, "TEAMS_DIR", tmp_path / "teams")
    monkeypatch.setattr(cfg, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(cfg, "CONFIG_PATH", tmp_path / "config" / "hiring.config.json")
    rc = setup_cmd.run(_ns(team=None))
    assert rc == 1
    assert "No team packs found" in capsys.readouterr().out
