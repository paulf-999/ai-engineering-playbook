"""Tests that docs/guides/config_by_topic.md links every parent config file, so a new rule can't be left off the map."""

import re

from _paths import REPO_ROOT

MAP = REPO_ROOT / "docs" / "guides" / "config_by_topic.md"
CONFIG_DIR = REPO_ROOT / "src" / "claude"
MAPPED_FOLDERS = ("rules", "skills", "agents", "hooks")


def parent_config_files():
    """Return every non-README .md or .sh file under the mapped folders whose name doesn't start with _."""
    return {
        path.relative_to(CONFIG_DIR).as_posix()
        for folder in MAPPED_FOLDERS
        for path in (CONFIG_DIR / folder).rglob("*")
        if path.suffix in {".md", ".sh"} and not path.name.startswith("_") and path.name != "README.md"
    }


def test_map_links_every_parent_config_file():
    """A parent rule, skill, agent or hook missing from the map fails, naming each missing file."""
    links = set(re.findall(r"\]\(\.\./\.\./src/claude/([^)#]+)", MAP.read_text()))
    missing = sorted(parent_config_files() - links)
    assert not missing, f"add these to {MAP.name}: {missing}"
