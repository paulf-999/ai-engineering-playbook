"""Review any local target blind, with three cold readers who play a newcomer, a maintainer and an adopting manager.

Each reader is a `claude -p --safe-mode` run with read-only tools, so it sees only its lens and a scratch copy of
the target, with none of your config. Safe mode also confines the file tools to that copy. A git repo is copied by a
fresh clone, so readers see only committed files, and a folder is copied without likely secret files, `.venv`,
nested git folders or symlinks that point out of it.
Each reader lists up to 8 findings, and the report groups them by the file each cites, ranked by how many readers
named that file. Set `TARGET` to the repo, folder or file to review, and `OUT` to write the report to a file.
"""

import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LENSES = {
    "newcomer": "You'd be the one using this. Can you tell what it's for, get it running and trust it?",
    "maintainer": "You'd own and change this. Look at its structure, coupling, duplication and testability, and at "
    "its failure modes, recovery, secrets, permissions and pinned versions.",
    "adopting manager": "You're deciding whether your team adopts this. Weigh its value against its cost, its risk "
    "and any reliance on one person.",
}
# Readers at once, kept low so parallel claude -p calls stay within plan rate limits
MAX_WORKERS = 3
MODEL = "sonnet"
MAX_TURNS = "40"
TIMEOUT_SECONDS = 900
READ_ONLY_TOOLS = ["Read", "Glob", "Grep"]
# files a folder copy leaves out: likely secrets, starting from git-create-pr's list, plus local environments and
# nested git folders, whose history can hold secrets a later commit removed
SKIPPED_IN_COPIES = [
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "*.p12",
    "*.pfx",
    "*.p8",
    "*.tfvars",
    "id_rsa*",
    "id_ed25519*",
    "credentials*",
    ".git-credentials",
    ".npmrc",
    ".pypirc",
    ".netrc",
    ".aws",
    ".venv",
    ".git",
]
SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {
            "type": "array",
            "maxItems": 8,
            "items": {
                "type": "object",
                "properties": {"file": {"type": "string"}, "problem": {"type": "string"}, "change": {"type": "string"}},
                "required": ["file", "problem", "change"],
            },
        }
    },
    "required": ["findings"],
}
BRIEF = """{lens} A colleague pointed you at the files in {root}. Explore them as you naturally would, and say where \
you'd stop or get stuck. List up to 8 findings, each with the file, the problem and the change you'd make."""


def main():
    """Review TARGET with each lens and print the ranked report, or write it to OUT."""
    if shutil.which("claude") is None:
        sys.exit("claude isn't on PATH - install Claude Code and log in first.")
    target = os.environ.get("TARGET", "")
    if not Path(target).exists():
        sys.exit(f"TARGET {target!r} doesn't exist - set it to a repo, folder or file.")
    with tempfile.TemporaryDirectory(prefix="architecture_review_") as scratch:
        root = prepare(target, scratch)
        results = collect(root)
        # every reader failing, such as on a rate limit or a lapsed login, must not look like a clean review
        if all(findings is None for findings in results.values()):
            sys.exit("Every reader failed, so there's no report - check the errors above, then run it again.")
        report = render(rank(results, root), target)
    out = os.environ.get("OUT")
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(report)
        print(f"Wrote {out}")
    else:
        print(report)


def prepare(target, scratch):
    """Copy target into scratch and return the copy: a fresh clone for a git repo's top folder, else a plain copy."""
    target = Path(target).resolve()
    root = Path(scratch) / target.name
    if (target / ".git").exists():
        subprocess.run(["git", "clone", "--quiet", str(target), str(root)], check=True)
        drop_outward_links(root)
    elif target.is_dir():
        # leave out likely secrets and environments, and copy symlinks as links so nothing outside target comes along
        shutil.copytree(target, root, symlinks=True, ignore=shutil.ignore_patterns(*SKIPPED_IN_COPIES))
        drop_outward_links(root)
    else:
        root.mkdir()
        shutil.copy2(target, root)
    return root


def drop_outward_links(root):
    """Remove each copied symlink that points outside root, so no reader can follow one out of the copy."""
    root = Path(root).resolve()
    for path in list(root.rglob("*")):
        if path.is_symlink() and not path.resolve().is_relative_to(root):
            path.unlink()


def build_prompt(lens, root):
    """Return the brief one reader gets: its lens and where the files are, with nothing about what they are."""
    return BRIEF.format(lens=LENSES[lens], root=root)


def read_once(prompt, root):
    """Run one safe-mode reader with read-only tools in root and return its findings."""
    command = ["claude", "-p", prompt, "--safe-mode", "--strict-mcp-config", "--no-session-persistence"]
    command += ["--model", MODEL, "--max-turns", MAX_TURNS, "--tools", *READ_ONLY_TOOLS]
    command += ["--output-format", "json", "--json-schema", json.dumps(SCHEMA)]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
    return json.loads(result.stdout)["structured_output"]["findings"]


def collect(root, read=read_once):
    """Run one reader per lens in parallel, returning each lens's findings, or None for a reader that failed."""

    def run_lens(lens):
        # one failed or timed-out reader shouldn't discard the other readers' findings
        try:
            return lens, read(build_prompt(lens, root), root)
        except (subprocess.SubprocessError, ValueError, KeyError, TypeError) as error:
            print(f"The {lens} reader failed, so the report leaves it out: {error!r}", file=sys.stderr)
            return lens, None

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        return dict(pool.map(run_lens, LENSES))


def rank(results, root):
    """Group findings by cited file, ranked by how many distinct readers named it, then by file name."""
    files = {}
    for lens, findings in results.items():
        for finding in findings or []:
            for file in cited_files(finding["file"], root):
                files.setdefault(file, []).append((lens, finding))
    return sorted(files.items(), key=lambda item: (-len({lens for lens, _ in item[1]}), item[0]))


def cited_files(cited, root):
    """Return each file one finding cites, relative to root, since readers often name several in one field."""
    # readers add line notes such as "(lines 9, 26)", whose commas would otherwise split the field
    cited = re.sub(r"\s*\([^)]*\)", "", cited)
    parts = re.split(r"\s*;\s*|,\s+|\s+and\s+", cited)
    return list(dict.fromkeys(relative_file(part, root) for part in parts if part.strip()))


def relative_file(cited, root):
    """Return a cited file relative to root, without any line note, so each reader's citation of it matches."""
    cited = re.sub(r":\d[\d,\s-]*$", "", cited.strip().strip("`"))
    # macOS temp folders resolve from /var to /private/var, so readers may cite either form, or start from root's name
    for prefix in (str(Path(root).resolve()), str(root), Path(root).name):
        cited = cited.removeprefix(f"{prefix}/")
    while cited.startswith("./"):
        cited = cited[2:]
    # a bare file name, such as install.sh, maps to its path when only one file in root has that name
    try:
        found = [] if (Path(root) / cited).exists() else list(Path(root).rglob(glob.escape(Path(cited).name)))
    except (OSError, ValueError):
        # an unusual citation, such as one too long for a path, keeps its own text rather than ending the run
        found = []
    matches = [path for path in found if ".git" not in path.relative_to(root).parts]
    return matches[0].relative_to(root).as_posix() if len(matches) == 1 else cited or "."


def render(ranked, target):
    """Return the ranked findings as a markdown report."""
    lines = [f"# Architecture review: {Path(target).name}", "", f"**Target:** `{target}`", ""]
    for file, findings in ranked:
        readers = len({lens for lens, _ in findings})
        lines += [f"## `{file}` ({readers} of {len(LENSES)} readers)", ""]
        # readers sometimes write lists inside a finding, which would break out of its bullet
        lines += [
            f"- **{lens}:** {' '.join(finding['problem'].split())} **Change:** {' '.join(finding['change'].split())}"
            for lens, finding in findings
        ]
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
