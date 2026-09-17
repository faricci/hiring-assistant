"""`hiring cv2md` — convert a CV PDF (or a folder of PDFs) to markdown.

Uses ``pymupdf4llm`` when available. Output goes to ``candidates/cv_md/``. The
dependency is optional so the rest of the toolkit works without it.
"""
from __future__ import annotations

import argparse
import datetime as _dt
from pathlib import Path

from . import config as cfg


def _convert_one(pdf_path: Path, out_dir: Path) -> Path:
    import pymupdf4llm  # imported lazily so the dep stays optional

    out_dir.mkdir(parents=True, exist_ok=True)
    md_text = pymupdf4llm.to_markdown(str(pdf_path))
    header = (
        "---\n"
        f"source: {pdf_path.name}\n"
        f"converted: {_dt.datetime.now().isoformat(timespec='seconds')}\n"
        "---\n\n"
    )
    out_path = out_dir / f"{pdf_path.stem}.md"
    cfg.write_text_resilient(out_path, header + md_text)
    return out_path


def run(args: argparse.Namespace) -> int:
    config = cfg.load_config()
    out_dir = cfg.candidates_dir(config) / "cv_md"

    source = Path(args.source).expanduser()
    if not source.exists():
        raise FileNotFoundError(f"Source not found: {source}")

    pdfs = [source] if source.is_file() else sorted(source.glob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found in: {source}")
        return 1

    try:
        import pymupdf4llm  # noqa: F401
    except ImportError:
        print("error: pymupdf4llm is not installed. Install it with:")
        print("  pip install pymupdf4llm")
        return 2

    failures = 0
    for pdf in pdfs:
        try:
            out_path = _convert_one(pdf, out_dir)
            print(f"Converted: {pdf.name} -> {out_path.relative_to(cfg.PROJECT_ROOT)}")
        except Exception as exc:  # noqa: BLE001 - report and continue the batch
            failures += 1
            print(f"error: failed to convert {pdf.name}: {exc}")
    return 1 if failures else 0
