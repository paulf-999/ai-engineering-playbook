"""The config files a default install ships, shared by the installer and rule-structure tests."""

import os
import subprocess

from _paths import REPO_ROOT

# authoring templates the installer never installs
AUTHORING_TEMPLATES = {"_templates/README.md", "_templates/AGENT.md.template", "_templates/rule.md.template"}
# ignore the user's git config, so their settings can't change which files git lists
GIT_ENV = {"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


def is_preference(path):
    """Return whether a src/claude/ path is a preference, which installs only with PREFERENCES=1."""
    return "/preferences/" in f"/{path}"


def tracked_config_files(include_preferences=False):
    """Return the files git tracks under src/claude/ that install, as paths relative to it."""
    command = ["git", "ls-files", "--", "src/claude"]
    output = subprocess.run(
        command, cwd=REPO_ROOT, env={**os.environ, **GIT_ENV}, capture_output=True, text=True, check=True
    )
    paths = {path.removeprefix("src/claude/") for path in output.stdout.splitlines()}
    return {
        path
        for path in paths
        if path not in AUTHORING_TEMPLATES
        and not path.startswith("_templates/skills/")
        and (include_preferences or not is_preference(path))
    }
