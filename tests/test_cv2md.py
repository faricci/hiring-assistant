import argparse
import builtins

import pytest

from hiring import config as cfg
from hiring import cv2md


def _ns(source):
    return argparse.Namespace(source=source)


def test_run_missing_source_raises(tmp_project, active_config):
    with pytest.raises(FileNotFoundError):
        cv2md.run(_ns(str(cfg.PROJECT_ROOT / "nope.pdf")))


def test_run_folder_with_no_pdfs(tmp_project, active_config, capsys):
    empty_dir = cfg.PROJECT_ROOT / "empty"
    empty_dir.mkdir()
    rc = cv2md.run(_ns(str(empty_dir)))
    assert rc == 1
    assert "No PDF files found" in capsys.readouterr().out


def test_run_reports_missing_optional_dependency(tmp_project, active_config, monkeypatch, capsys):
    """Simulate pymupdf4llm being absent, regardless of whether it is actually
    installed in the environment running the suite."""
    pdf = cfg.PROJECT_ROOT / "cv.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake")

    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "pymupdf4llm":
            raise ImportError("simulated: not installed")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    rc = cv2md.run(_ns(str(pdf)))
    assert rc == 2
    assert "pymupdf4llm is not installed" in capsys.readouterr().out
