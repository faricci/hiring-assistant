"""`hiring dashboard` -- serve the project root and open the offline dashboard.

A plain http.server is enough: the dashboard only fetches sibling .md/.json
files, and file:// URLs block that fetch, so a same-origin server is required.
The server also exposes a small read-only JSON endpoint so the dashboard can
list whatever candidate files currently exist, without hard-coding any name.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import webbrowser
from urllib.parse import quote

from . import config as cfg

# candidates/<subdir> -> label shown in the sidebar (e.g. "CV: jane_doe.md")
CANDIDATE_KINDS = {
    "cv_md": "CV",
    "preparation_md": "Interview prep",
    "scorecards": "Scorecard",
    "takehome_md": "Take-home",
    "transcript_md": "Transcript",
}
SUPPORTED_EXTENSIONS = {".md", ".json", ".txt"}


def _discover_candidate_files() -> list[dict[str, str]]:
    """Scan the active candidates/ workspace for renderable artifacts.

    Returns [] if there is no config yet (fresh checkout, 'hiring setup' not
    run) rather than raising -- the dashboard should still load.
    """
    try:
        config = cfg.load_config()
        candidates_root = cfg.candidates_dir(config)
    except cfg.ConfigError:
        return []

    files: list[dict[str, str]] = []
    for subdir, kind in CANDIDATE_KINDS.items():
        folder = candidates_root / subdir
        if not folder.is_dir():
            continue
        for entry in sorted(folder.iterdir()):
            if not entry.is_file() or entry.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue
            try:
                rel = entry.relative_to(cfg.PROJECT_ROOT)
            except ValueError:
                continue  # candidates_dir points outside the served root; can't be fetched
            url_path = "/" + "/".join(quote(part) for part in rel.parts)
            files.append({"name": entry.name, "kind": kind, "path": url_path})
    return files


class DashboardRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Static file server plus a single read-only JSON endpoint."""

    def do_GET(self) -> None:  # noqa: N802 (stdlib override name)
        if self.path == "/api/candidate-files":
            self._serve_candidate_files()
            return
        super().do_GET()

    def _serve_candidate_files(self) -> None:
        payload = json.dumps(_discover_candidate_files()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def run(args: argparse.Namespace) -> int:
    port = args.port
    handler = functools.partial(
        DashboardRequestHandler, directory=str(cfg.PROJECT_ROOT)
    )
    url = f"http://localhost:{port}/dashboard/dashboard.html"

    # 127.0.0.1 only: this is a local dev tool, not meant to be reachable on the network
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Serving {cfg.PROJECT_ROOT} at {url}")
        print("Press Ctrl+C to stop.")
        if not args.no_browser:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
    return 0
