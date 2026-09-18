import json

import pytest

from hiring import config as cfg


def test_load_config_missing_raises(tmp_project):
    with pytest.raises(cfg.ConfigError):
        cfg.load_config()


def test_save_and_load_config_roundtrip(tmp_project):
    written = {"team": "acme", "language": "en", "exercises_repo": "", "candidates_dir": "candidates"}
    path = cfg.save_config(written)
    assert path == cfg.CONFIG_PATH
    assert cfg.load_config() == written


def test_load_config_invalid_json_raises(tmp_project):
    cfg.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    cfg.CONFIG_PATH.write_text("{not json", encoding="utf-8")
    with pytest.raises(cfg.ConfigError):
        cfg.load_config()


def test_list_team_ids_finds_synthetic_team(tmp_project):
    assert cfg.list_team_ids() == ["acme"]


def test_list_team_ids_empty_when_teams_dir_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(cfg, "TEAMS_DIR", tmp_path / "does-not-exist")
    assert cfg.list_team_ids() == []


def test_load_team_success(tmp_project):
    team = cfg.load_team("acme")
    assert team["display_name"] == "Acme Team"
    assert team["_dir"] == str(cfg.TEAMS_DIR / "acme")


def test_load_team_unknown_raises(tmp_project):
    with pytest.raises(cfg.ConfigError, match="not found"):
        cfg.load_team("nope")


def test_load_team_missing_required_key_raises(tmp_project):
    team_dir = cfg.TEAMS_DIR / "broken"
    team_dir.mkdir()
    (team_dir / "team.json").write_text(json.dumps({"id": "broken"}), encoding="utf-8")
    with pytest.raises(cfg.ConfigError, match="missing required key"):
        cfg.load_team("broken")


def test_load_team_id_mismatch_raises(tmp_project):
    team_dir = cfg.TEAMS_DIR / "mismatched"
    team_dir.mkdir()
    (team_dir / "team.json").write_text(json.dumps({
        "id": "other", "display_name": "X", "score_model": {}, "templates": {},
    }), encoding="utf-8")
    with pytest.raises(cfg.ConfigError, match="does not match"):
        cfg.load_team("mismatched")


def test_active_team_requires_team_key(tmp_project):
    cfg.save_config({"language": "en"})
    with pytest.raises(cfg.ConfigError, match="no 'team' selected"):
        cfg.active_team(cfg.load_config())


def test_active_team_resolves_selected_team(tmp_project, active_config):
    team = cfg.active_team(active_config)
    assert team["id"] == "acme"


def test_candidates_dir_default(tmp_project):
    path = cfg.candidates_dir({})
    assert path == (cfg.PROJECT_ROOT / "candidates").resolve()


def test_candidates_dir_override(tmp_project):
    path = cfg.candidates_dir({"candidates_dir": "custom"})
    assert path == (cfg.PROJECT_ROOT / "custom").resolve()


@pytest.mark.parametrize("raw,expected", [
    ("jane doe", "JaneDoe"),
    ("  Jane   Doe  ", "JaneDoe"),
    ("jane-doe", "JaneDoe"),
    ("jane_doe", "JaneDoe"),
    ("O'Brien!!", "OBrien"),
    ("Already CamelCase", "AlreadyCamelCase"),
])
def test_safe_name(raw, expected):
    assert cfg.safe_name(raw) == expected
