"""`hiring dashboard` -- serve the project root and open the offline dashboard.

A plain http.server is enough: the dashboard only fetches sibling .md/.json
files, and file:// URLs block that fetch, so a same-origin server is required.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import webbrowser

from . import config as cfg


def run(args: argparse.Namespace) -> int:
    port = args.port
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=str(cfg.PROJECT_ROOT)
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
