"""Command-line entry point for the Hiring Assistant toolkit."""
from __future__ import annotations

import argparse
import sys

from . import __version__
from .config import ConfigError
from . import setup as setup_cmd
from . import prep as prep_cmd
from . import qindex as qindex_cmd
from . import scorecard as scorecard_cmd
from . import cv2md as cv2md_cmd
from . import dashboard as dashboard_cmd

EPILOG = """\
This is a DETERMINISTIC toolkit first: every command below runs standalone,
no AI required. An AI coding agent is an OPTIONAL layer on top, useful only
for the judgment-heavy steps (reading a CV, writing tailored questions,
evaluating a transcript, scoring).

Run these yourself, anytime, no agent needed:
  hiring setup                                        # once: pick a team + exercises repo
  hiring dashboard                                     # browse process, commands, candidate files
  hiring cv2md candidates/cv_pdf/cv.pdf                # CV PDF -> markdown
  hiring index                                         # rebuild the question-bank index
  hiring scorecard compare                             # rank all candidates

For the rest, open your editor's AI agent picker, select "Hiring Assistant",
and ask in plain language — e.g. "help me evaluate and create the first
interview preparation for Jane Doe". It follows
.github/agents/hiring-assistant.agent.md, reads the CV, and runs these same
commands for you as part of the conversation, adding only the judgment
(fit, flags, tailored questions, scoring):
    hiring prep --name "Jane Doe" --seniority senior     # prep file (fit, flags, questions)
    hiring scorecard init    --name "Jane Doe" --round 1 # after interview 1
    hiring scorecard init    --name "Jane Doe" --round 2 # after interview 2
    hiring scorecard summary --name "Jane Doe"           # weighted score + recommendation

Run 'hiring <command> -h' for details and options on any command.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hiring",
        description=(
            "Deterministic toolkit for a modular technical hiring process: "
            "CV -> prep -> interviews -> scorecard. Every command works standalone; "
            "an AI coding agent (see epilog) is optional and only adds judgment on "
            "top. Team-specific content (profile, questions, scoring, templates) "
            "lives in a team pack under teams/<id>/."
        ),
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"hiring {__version__}")
    sub = parser.add_subparsers(dest="command", required=True, metavar="command")

    # setup ----------------------------------------------------------------
    p_setup = sub.add_parser(
        "setup",
        help="Select the active team pack and the exercises repo (run this first).",
        description=(
            "Write config/hiring.config.json: which team pack drives scoring/questions, "
            "where the cloned exercises repo lives, and the default interview language. "
            "Prompts interactively for anything not passed as a flag. Also installs "
            "requirements.txt (use --skip-deps to opt out)."
        ),
    )
    p_setup.add_argument("--team", help="Team pack id (folder name under teams/).")
    p_setup.add_argument("--exercises-repo", help="Path to a cloned exercises repository.")
    p_setup.add_argument("--language", choices=["en", "it"], help="Default interview language.")
    p_setup.add_argument("--non-interactive", action="store_true",
                         help="Fail instead of prompting when values are missing.")
    p_setup.add_argument("--skip-deps", action="store_true",
                         help="Don't install requirements.txt (e.g. no network/offline run).")
    p_setup.set_defaults(func=setup_cmd.run)

    # teams ----------------------------------------------------------------
    p_teams = sub.add_parser(
        "teams",
        help="List available team packs and show which one is active.",
        description="List every team pack found under teams/<id>/ with its display name, "
                    "marking the one currently selected in config/hiring.config.json.",
    )
    p_teams.set_defaults(func=setup_cmd.list_teams)

    # prep -----------------------------------------------------------------
    p_prep = sub.add_parser(
        "prep",
        help="Generate the interview prep file for a candidate (fit, flags, questions).",
        description=(
            "Render the active team's prep template into candidates/preparation_md/, "
            "filling placeholders and leaving <!-- AGENT-FILL --> markers for the agent "
            "to complete after reading the candidate's CV."
        ),
    )
    p_prep.add_argument("--name", required=True, help="Candidate full name.")
    p_prep.add_argument("--seniority", choices=["senior", "mid", "junior"], default="senior",
                        help="Seniority level, adjusts question focus (default: senior).")
    p_prep.add_argument("--language", choices=["en", "it"],
                        help="Override the default language set by 'hiring setup'.")
    p_prep.add_argument("--force", action="store_true", help="Overwrite an existing prep file.")
    p_prep.set_defaults(func=prep_cmd.run)

    # index ----------------------------------------------------------------
    p_index = sub.add_parser(
        "index",
        help="Rebuild the question-bank index for the active team (run after editing it).",
        description=(
            "Scan the active team's question-bank.md and rebuild question-bank-index.json: "
            "a compact map of categories, line ranges, and tags so the agent can jump to the "
            "relevant section instead of reading the whole bank."
        ),
    )
    p_index.set_defaults(func=qindex_cmd.run)

    # scorecard ------------------------------------------------------------
    p_score = sub.add_parser(
        "scorecard",
        help="Init, summarize, or compare candidate scorecards.",
        description=(
            "init: create a blank scorecard for an interview round from the team's score model. "
            "summary: compute the weighted score (Behaviour/Skills/Knowledge) and recommendation "
            "band for one candidate. compare: rank every candidate side by side."
        ),
    )
    p_score.add_argument("mode", choices=["init", "summary", "compare"],
                         help="init=create round scorecard, summary=score one candidate, "
                              "compare=rank all candidates.")
    p_score.add_argument("--name", help="Candidate full name (required for init/summary).")
    p_score.add_argument("--round", type=int, default=1, help="Interview round number (init only, default: 1).")
    p_score.set_defaults(func=scorecard_cmd.run)

    # cv2md ----------------------------------------------------------------
    p_cv = sub.add_parser(
        "cv2md",
        help="Convert a CV PDF (or a folder of PDFs) to markdown for analysis.",
        description="Convert one PDF or every PDF in a folder to markdown under "
                    "candidates/cv_md/, ready for the agent to read and evaluate.",
    )
    p_cv.add_argument("source", help="Path to a PDF file or a folder of PDFs.")
    p_cv.set_defaults(func=cv2md_cmd.run)

    # dashboard --------------------------------------------------------------
    p_dash = sub.add_parser(
        "dashboard",
        help="Serve the project root and open the offline dashboard in a browser.",
        description=(
            "Start a local web server (127.0.0.1 only) rooted at the project folder and open "
            "dashboard/dashboard.html. Required for the dashboard's reference-file links, "
            "since opening the HTML file directly (file://) blocks reading sibling files."
        ),
    )
    p_dash.add_argument("--port", type=int, default=8080, help="Port to serve on (default: 8080).")
    p_dash.add_argument("--no-browser", action="store_true", help="Don't auto-open the browser.")
    p_dash.set_defaults(func=dashboard_cmd.run)

    return parser



def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
