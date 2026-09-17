"""`hiring setup` — write config/hiring.config.json selecting a team and exercises repo."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from . import config as cfg

REQUIREMENTS_PATH = cfg.PROJECT_ROOT / "requirements.txt"


def _install_dependencies() -> bool:
    """Install packages from requirements.txt. Returns True on success."""
    if not REQUIREMENTS_PATH.exists():
        return True
    print(f"Installing dependencies from {REQUIREMENTS_PATH.relative_to(cfg.PROJECT_ROOT)}...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_PATH)],
    )
    if result.returncode != 0:
        print("warning: dependency installation failed; 'hiring cv2md' may not work "
              "until you run 'pip install -r requirements.txt' manually.")
        return False
    return True


def list_teams(_args: argparse.Namespace) -> int:
    ids = cfg.list_team_ids()
    if not ids:
        print("No team packs found under teams/.")
        return 1
    print("Available team packs:")
    for team_id in ids:
        team = cfg.load_team(team_id)
        marker = ""
        try:
            if cfg.load_config().get("team") == team_id:
                marker = "  (active)"
        except cfg.ConfigError:
            pass
        print(f"  - {team_id}: {team['display_name']}{marker}")
    return 0


def _prompt(question: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{question}{suffix}: ").strip()
    return answer or (default or "")


def run(args: argparse.Namespace) -> int:
    teams = cfg.list_team_ids()
    if not teams:
        print("No team packs found under teams/. Add one before running setup.")
        return 1

    existing = {}
    if cfg.CONFIG_PATH.exists():
        try:
            existing = cfg.load_config()
        except cfg.ConfigError:
            existing = {}

    # --- team ---
    team_id = args.team or existing.get("team")
    if team_id not in teams:
        if args.non_interactive:
            raise cfg.ConfigError(
                f"--team is required (one of: {', '.join(teams)})."
            )
        print("Available team packs:")
        for i, tid in enumerate(teams, 1):
            print(f"  {i}. {tid} — {cfg.load_team(tid)['display_name']}")
        choice = _prompt("Select a team pack (id or number)", teams[0])
        if choice.isdigit() and 1 <= int(choice) <= len(teams):
            team_id = teams[int(choice) - 1]
        elif choice in teams:
            team_id = choice
        else:
            raise cfg.ConfigError(f"Unknown team pack '{choice}'.")

    team = cfg.load_team(team_id)

    # --- language ---
    default_lang = args.language or existing.get(
        "language", team.get("default_language", "en")
    )
    language = default_lang
    if not args.language and not args.non_interactive:
        language = _prompt("Default interview language (en/it)", default_lang)
    if language not in ("en", "it"):
        raise cfg.ConfigError("Language must be 'en' or 'it'.")

    # --- exercises repo ---
    exercises_repo = args.exercises_repo or existing.get("exercises_repo", "")
    if not exercises_repo and not args.non_interactive:
        exercises_repo = _prompt(
            "Path to a cloned exercises repo (optional, Enter to skip)", ""
        )
    if exercises_repo:
        resolved = Path(exercises_repo).expanduser()
        if not resolved.exists():
            print(f"warning: exercises repo path does not exist yet: {resolved}")
        exercises_repo = str(resolved)

    config = {
        "team": team_id,
        "language": language,
        "exercises_repo": exercises_repo,
        "candidates_dir": existing.get("candidates_dir", cfg.DEFAULT_CANDIDATES_DIR),
    }
    path = cfg.save_config(config)

    # Ensure the candidates workspace exists.
    base = cfg.candidates_dir(config)
    for sub in ("cv_pdf", "cv_md", "preparation_md", "takehome_md",
                "transcript_md", "scorecards"):
        (base / sub).mkdir(parents=True, exist_ok=True)

    if not args.skip_deps:
        _install_dependencies()

    print(f"Configuration written: {path.relative_to(cfg.PROJECT_ROOT)}")
    print(f"  team:           {team_id} ({team['display_name']})")
    print(f"  language:       {language}")
    print(f"  exercises_repo: {exercises_repo or '(not set)'}")
    print(f"  candidates:     {base.relative_to(cfg.PROJECT_ROOT)}/")
    return 0
