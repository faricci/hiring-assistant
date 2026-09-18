import argparse
import json

import pytest

from hiring import config as cfg
from hiring import qindex


def test_build_index_counts_categories_and_levels(tmp_path):
    bank = tmp_path / "bank.md"
    bank.write_text(
        '## Terraform\n'
        '- \U0001F7E2 *"Q1?"*\n'
        '- \U0001F7E1 *"Q2?"*\n'
        '- \U0001F534 *"Q3?"*\n'
        '\n'
        '## Kubernetes\n'
        '### Advanced\n'
        '- \U0001F7E2 *"Q4?"*\n'
        '| exercise | difficulty |\n'
        '|---|---|\n'
        '| do X | easy |\n',
        encoding="utf-8",
    )
    index = qindex.build_index(bank, tag_map={"terraform": ["iac", "terraform"]})
    cats = {c["name"]: c for c in index["categories"]}

    assert set(cats) == {"Terraform", "Kubernetes"}
    assert cats["Terraform"]["question_count"] == 3
    assert cats["Terraform"]["levels"] == {"base": 1, "intermediate": 1, "advanced": 1}
    assert cats["Terraform"]["tags"] == ["iac", "terraform"]
    assert cats["Kubernetes"]["has_subsections"] is True
    assert cats["Kubernetes"]["question_count"] == 1
    # Both the table header row and the data row count (only the "|---|" style
    # separator is excluded) -- this is documenting existing behavior.
    assert cats["Kubernetes"]["exercise_count"] == 2
    assert index["_meta"]["total_lines"] == len(bank.read_text(encoding="utf-8").splitlines())


def test_build_index_skips_index_and_changelog_headings(tmp_path):
    bank = tmp_path / "bank.md"
    bank.write_text('## Index\nsome toc\n\n## Real Category\n- \U0001F7E2 *"Q?"*\n', encoding="utf-8")
    index = qindex.build_index(bank, tag_map={})
    assert [c["name"] for c in index["categories"]] == ["Real Category"]


def test_build_index_falls_back_to_word_tags_when_no_tag_map_match(tmp_path):
    bank = tmp_path / "bank.md"
    bank.write_text('## Something Custom\n- \U0001F7E2 *"Q?"*\n', encoding="utf-8")
    index = qindex.build_index(bank, tag_map={})
    assert index["categories"][0]["tags"] == ["something", "custom"]


def test_run_writes_index_json(tmp_project, active_config, capsys):
    rc = qindex.run(argparse.Namespace())
    assert rc == 0
    out_path = cfg.TEAMS_DIR / "acme" / "question-bank-index.json"
    assert out_path.is_file()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert [c["name"] for c in data["categories"]] == ["Terraform", "Kubernetes"]
    assert "Question bank index generated" in capsys.readouterr().out


def test_run_missing_bank_raises(tmp_project, active_config):
    (cfg.TEAMS_DIR / "acme" / "question-bank.md").unlink()
    with pytest.raises(FileNotFoundError):
        qindex.run(argparse.Namespace())
