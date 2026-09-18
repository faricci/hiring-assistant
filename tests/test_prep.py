import argparse

import pytest

from hiring import config as cfg
from hiring import prep


def _ns(**kwargs):
    defaults = dict(name="Jane Doe", seniority="senior", language=None, force=False)
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


def test_prep_creates_file_with_substitutions(tmp_project, active_config):
    rc = prep.run(_ns())
    assert rc == 0
    out = cfg.candidates_dir(active_config) / "preparation_md" / "JaneDoe_interview_prep.md"
    assert out.is_file()
    text = out.read_text(encoding="utf-8")
    assert "Jane Doe" in text
    assert "{{CANDIDATE_NAME}}" not in text
    assert "Senior (5+ years)" in text
    assert "<!-- AGENT-FILL:" in text


def test_prep_refuses_overwrite_without_force(tmp_project, active_config, capsys):
    prep.run(_ns())
    rc = prep.run(_ns())
    assert rc == 1
    assert "already exists" in capsys.readouterr().out


def test_prep_force_overwrites(tmp_project, active_config):
    prep.run(_ns())
    rc = prep.run(_ns(force=True, seniority="junior"))
    assert rc == 0
    out = cfg.candidates_dir(active_config) / "preparation_md" / "JaneDoe_interview_prep.md"
    assert "Junior (< 3 years)" in out.read_text(encoding="utf-8")


def test_prep_unknown_language_raises(tmp_project, active_config):
    with pytest.raises(cfg.ConfigError, match="no template"):
        prep.run(_ns(language="it"))


def test_prep_missing_template_file_raises(tmp_project, active_config):
    template_path = cfg.TEAMS_DIR / "acme" / "templates" / "interview-en.md"
    template_path.unlink()
    with pytest.raises(FileNotFoundError):
        prep.run(_ns())
