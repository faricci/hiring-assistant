from hiring import config as cfg
from hiring import dashboard


def test_discover_returns_empty_without_config(tmp_project):
    assert dashboard._discover_candidate_files() == []


def test_discover_finds_supported_files_by_kind(tmp_project, active_config):
    base = cfg.candidates_dir(active_config)
    (base / "cv_md").mkdir(parents=True)
    (base / "cv_md" / "jane.md").write_text("# CV", encoding="utf-8")
    (base / "preparation_md").mkdir(parents=True)
    (base / "preparation_md" / "jane.md").write_text("# Prep", encoding="utf-8")
    (base / "scorecards").mkdir(parents=True)
    (base / "scorecards" / "jane.json").write_text("{}", encoding="utf-8")
    (base / "scorecards" / "jane.png").write_bytes(b"\x89PNG")  # unsupported extension

    files = dashboard._discover_candidate_files()
    by_kind = {f["kind"]: f for f in files}

    assert by_kind["CV"]["name"] == "jane.md"
    assert by_kind["Interview prep"]["name"] == "jane.md"
    assert by_kind["Scorecard"]["name"] == "jane.json"
    assert all(f["name"] != "jane.png" for f in files)
    assert all(f["path"].startswith("/") for f in files)


def test_discover_skips_paths_outside_project_root(tmp_project, active_config, tmp_path_factory):
    outside = tmp_path_factory.mktemp("outside-candidates")
    (outside / "cv_md").mkdir()
    (outside / "cv_md" / "jane.md").write_text("# CV", encoding="utf-8")

    config = dict(active_config, candidates_dir=str(outside))
    cfg.save_config(config)

    assert dashboard._discover_candidate_files() == []


def test_discover_ignores_missing_subdirs(tmp_project, active_config):
    # No candidates/<subdir> folders created at all -- should not raise.
    assert dashboard._discover_candidate_files() == []
