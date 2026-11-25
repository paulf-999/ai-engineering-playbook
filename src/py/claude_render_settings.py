"""Print the hooks and deny rules an install merges into settings.json, filled in from the settings template.

It lists the tracked hooks under src/claude/hooks/ from the current folder, stops if the template lacks one, and leaves
out any hook the template names that isn't there. It needs Jinja, which make install sets up in .venv.

Usage: claude_render_settings.py <folder the hooks install into> [--all-hooks], from the repo root
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

TEMPLATE = Path(__file__).resolve().parents[1] / "sh" / "claude_install_config" / "settings.json.j2"
HOOKS_SOURCE = Path("src/claude/hooks")


def main():
    """Print the rendered settings, or stop naming each hook the template lacks."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("hooks_dir", help="the folder the hooks install into")
    parser.add_argument("--all-hooks", action="store_true", help="include the hooks a project install leaves out")
    args = parser.parse_args()
    shipped = shipped_hooks()
    unlisted = shipped - named_hooks(render(args.hooks_dir, all_hooks=True), args.hooks_dir)
    if unlisted:
        sys.exit(f"{TEMPLATE.name} has no entry for: {', '.join(sorted(unlisted))}")
    settings = render(args.hooks_dir, args.all_hooks)
    print(json.dumps(without_missing_hooks(settings, args.hooks_dir, shipped), ensure_ascii=False))


def shipped_hooks(root=Path()):
    """Return the tracked hooks that exist, as paths relative to the hooks folder."""
    command = ["git", "ls-files", "-z", "--", str(HOOKS_SOURCE)]
    listed = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False).stdout.split("\0")
    hooks = [Path(path) for path in listed if Path(path).match("hook_*.sh")]
    return {str(hook.relative_to(HOOKS_SOURCE)) for hook in hooks if (root / hook).is_file()}


def render(hooks_dir, all_hooks):
    """Return the settings the template holds, as a dictionary.

    :param hooks_dir: the folder the hooks install into
    :param all_hooks: whether to include the hooks a project install leaves out
    """
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE.parent),
        undefined=StrictUndefined,
        # the output is JSON, so each value is escaped for JSON below rather than for HTML
        autoescape=False,
    )
    escaped_dir = json.dumps(hooks_dir, ensure_ascii=False)[1:-1]
    return json.loads(environment.get_template(TEMPLATE.name).render(hooks_dir=escaped_dir, all_hooks=all_hooks))


def hook_path(hook, hooks_dir):
    """Return the path, relative to the hooks folder, of the file a hook's command runs."""
    return hook["command"].removeprefix(f'bash "{hooks_dir}/').removesuffix('"')


def named_hooks(settings, hooks_dir):
    """Return the hooks the settings name, as paths relative to the hooks folder."""
    entries = [entry for entries in settings["hooks"].values() for entry in entries]
    return {hook_path(hook, hooks_dir) for entry in entries for hook in entry["hooks"]}


def without_missing_hooks(settings, hooks_dir, shipped):
    """Return the settings without the entries whose hook isn't shipped."""
    hooks = {
        event: [entry for entry in entries if all(hook_path(hook, hooks_dir) in shipped for hook in entry["hooks"])]
        for event, entries in settings["hooks"].items()
    }
    return {**settings, "hooks": {event: entries for event, entries in hooks.items() if entries}}


if __name__ == "__main__":
    main()
