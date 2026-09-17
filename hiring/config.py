"""Configuration and team-pack resolution.

The config file (``config/hiring.config.json``) is written by ``hiring setup`` and
selects the active team pack plus the location of the external exercises repo. All
paths are resolved relative to the project root so the CLI works from any cwd.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config" / "hiring.config.json"
TEAMS_DIR = PROJECT_ROOT / "teams"
DEFAULT_CANDIDATES_DIR = "candidates"


class ConfigError(Exception):
    """Raised when configuration or a team pack is missing or malformed."""


def write_text_resilient(path: Path, content: str, *, encoding: str = "utf-8",
                          retries: int = 5, delay: float = 0.3) -> Path:
    """Write text, retrying on OSError.

    Cloud-synced folders (OneDrive, etc.) can spuriously raise FileNotFoundError or
    other OSErrors on the first write to a brand-new file while a placeholder is
    still being resolved. A short retry clears this without needing user action.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    last_exc: OSError | None = None
    for attempt in range(retries):
        try:
            path.write_text(content, encoding=encoding)
            return path
        except OSError as exc:
            last_exc = exc
            if attempt < retries - 1:
                time.sleep(delay)
    assert last_exc is not None
    raise last_exc


def load_config() -> dict[str, Any]:
    """Load the active configuration, or raise a helpful error if absent."""
    if not CONFIG_PATH.exists():
        raise ConfigError(
            "No configuration found. Run 'hiring setup' first "
            f"(expected: {CONFIG_PATH.relative_to(PROJECT_ROOT)})."
        )
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Config file is not valid JSON: {exc}") from exc


def save_config(config: dict[str, Any]) -> Path:
    """Persist configuration as UTF-8 JSON, creating the config folder if needed."""
    return write_text_resilient(
        CONFIG_PATH, json.dumps(config, indent=2, ensure_ascii=False) + "\n"
    )


def list_team_ids() -> list[str]:
    """Return the ids of available team packs (folders containing team.json)."""
    if not TEAMS_DIR.exists():
        return []
    return sorted(
        p.name for p in TEAMS_DIR.iterdir() if (p / "team.json").is_file()
    )


def load_team(team_id: str) -> dict[str, Any]:
    """Load and validate a team pack's team.json by id."""
    team_dir = TEAMS_DIR / team_id
    manifest = team_dir / "team.json"
    if not manifest.is_file():
        available = ", ".join(list_team_ids()) or "(none)"
        raise ConfigError(
            f"Team pack '{team_id}' not found. Available: {available}."
        )
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"team.json for '{team_id}' is not valid JSON: {exc}") from exc
    _validate_team(team_id, data)
    data["_dir"] = str(team_dir)
    return data


def _validate_team(team_id: str, data: dict[str, Any]) -> None:
    for key in ("id", "display_name", "score_model", "templates"):
        if key not in data:
            raise ConfigError(f"Team pack '{team_id}' is missing required key '{key}'.")
    if data["id"] != team_id:
        raise ConfigError(
            f"Team pack folder '{team_id}' does not match team id '{data['id']}'."
        )


def active_team(config: dict[str, Any]) -> dict[str, Any]:
    """Resolve the team pack referenced by the active configuration."""
    team_id = config.get("team")
    if not team_id:
        raise ConfigError("Config has no 'team' selected. Run 'hiring setup'.")
    return load_team(team_id)


def team_dir(team: dict[str, Any]) -> Path:
    return Path(team["_dir"])


def candidates_dir(config: dict[str, Any]) -> Path:
    """Absolute path to the candidates workspace, created on demand."""
    rel = config.get("candidates_dir", DEFAULT_CANDIDATES_DIR)
    path = (PROJECT_ROOT / rel).resolve()
    return path


def safe_name(name: str) -> str:
    """Collapse a candidate name into a filesystem-safe token."""
    token = "".join(ch for ch in name.strip() if ch.isalnum() or ch in " _-")
    return "".join(part.capitalize() if part.islower() else part
                    for part in token.replace("-", " ").replace("_", " ").split())
