"""Sanity checks against the real, shipped 'devops-platform' team pack.

Unlike the rest of the suite these tests do NOT use the tmp_project fixture:
they read the actual checked-in repo content, so they catch accidental
breakage of that pack (a bad edit to team.json, a moved/renamed template)
without needing a live hiring.config.json.
"""
from hiring import config as cfg


def test_devops_platform_pack_is_discoverable_and_valid():
    assert "devops-platform" in cfg.list_team_ids()

    team = cfg.load_team("devops-platform")
    assert team["id"] == "devops-platform"

    for lang, rel_path in team["templates"].items():
        template_path = cfg.team_dir(team) / rel_path
        assert template_path.is_file(), f"missing template for '{lang}': {template_path}"

    bank_path = cfg.team_dir(team) / team.get("question_bank", "question-bank.md")
    assert bank_path.is_file()
