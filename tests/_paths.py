"""Repo paths shared by every test, so no test works out the repo root from its own depth."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "src" / "sh"
