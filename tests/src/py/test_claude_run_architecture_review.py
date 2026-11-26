"""Tests for the architecture review runner's target copy, reader brief and ranking, without a live claude run."""

import importlib
import subprocess
import sys

import pytest
from _paths import REPO_ROOT

# The runner is imported by name, as it is when run as a script
sys.path.insert(0, str(REPO_ROOT / "src" / "py"))
runner = importlib.import_module("claude_run_architecture_review")


def _make_finding(file, problem="unclear"):
    """Return one reader finding for file."""
    return {"file": file, "problem": problem, "change": "fix it"}


# --- target copy tests ---


def test_prepare_clones_a_repo_without_untracked_files(tmp_path):
    """A git repo is copied by a fresh clone, so untracked files never reach the readers."""
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "kept.md").write_text("committed\n")
    git = ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(["git", "init", "--quiet", str(repo)], check=True)
    subprocess.run([*git, "add", "kept.md"], check=True)
    subprocess.run([*git, "commit", "--quiet", "-m", "init"], check=True)
    (repo / "untracked.md").write_text("local\n")
    root = runner.prepare(repo, tmp_path / "scratch")
    assert (root / "kept.md").exists()
    assert not (root / "untracked.md").exists()


def test_prepare_copies_a_folder_and_a_single_file(tmp_path):
    """A plain folder is copied whole, and a single file lands alone in its own folder."""
    folder = tmp_path / "process"
    folder.mkdir()
    (folder / "steps.md").write_text("# Steps\n")
    (tmp_path / "scratch").mkdir()
    for secret in (".env", "deploy.pem", "credentials.json", ".npmrc"):
        (folder / secret).write_text("TOKEN=x\n")
    (folder / "link.md").symlink_to(tmp_path / "outside.md")
    copy = runner.prepare(folder, tmp_path / "scratch")
    assert (copy / "steps.md").exists()
    assert not [name for name in (".env", "deploy.pem", "credentials.json", ".npmrc") if (copy / name).exists()]
    assert (copy / "link.md").is_symlink()
    root = runner.prepare(folder / "steps.md", tmp_path / "scratch")
    assert [path.name for path in root.iterdir()] == ["steps.md"]


# --- reader tests ---


def test_build_prompt_gives_the_lens_and_the_path_only(tmp_path):
    """Each brief opens with its lens and names the scratch path, with nothing about the target."""
    prompt = runner.build_prompt("newcomer", tmp_path)
    assert prompt.startswith(runner.LENSES["newcomer"])
    assert str(tmp_path) in prompt


def test_collect_briefs_one_reader_per_lens(tmp_path):
    """Parallel readers still land under their own lens, each briefed with that lens."""

    def fake_read(prompt, root):
        return [_make_finding("a.py", prompt)]

    results = runner.collect(tmp_path, read=fake_read)
    assert set(results) == set(runner.LENSES)
    for lens, findings in results.items():
        assert findings[0]["problem"].startswith(runner.LENSES[lens])


def test_collect_keeps_the_other_readers_when_one_fails(tmp_path):
    """A reader whose run fails returns None, and the other lenses keep their findings."""

    def fake_read(prompt, root):
        if prompt.startswith(runner.LENSES["maintainer"]):
            raise runner.subprocess.TimeoutExpired("claude", 1)
        return [_make_finding("a.py")]

    results = runner.collect(tmp_path, read=fake_read)
    assert results["maintainer"] is None
    assert len(results["newcomer"]) == 1


def test_main_fails_when_every_reader_fails(tmp_path, monkeypatch):
    """When no reader returns findings, main exits with an error rather than printing an empty report."""
    monkeypatch.setenv("TARGET", str(tmp_path))
    monkeypatch.setattr(runner.shutil, "which", lambda name: "/bin/claude")
    monkeypatch.setattr(runner, "collect", lambda root: dict.fromkeys(runner.LENSES))
    with pytest.raises(SystemExit) as raised:
        runner.main()
    assert "Every reader failed" in str(raised.value), f"the exit should say why: {raised.value}"


# --- ranking tests ---


def test_rank_orders_files_by_distinct_readers(tmp_path):
    """A file two readers cite outranks one a single reader cites twice, and cited paths match across forms."""
    results = {
        "newcomer": [_make_finding(f"{tmp_path}/README.md:12"), _make_finding("z.py"), _make_finding("z.py")],
        "maintainer": [_make_finding("./README.md"), _make_finding(".github/ci.yml")],
        "adopting manager": [],
    }
    ranked = runner.rank(results, tmp_path)
    assert [file for file, _ in ranked] == ["README.md", ".github/ci.yml", "z.py"]
    report = runner.render(ranked, "/repo")
    assert report.index("`README.md` (2 of 3 readers)") < report.index("`z.py` (1 of 3 readers)")


def test_cited_files_splits_a_field_and_finds_bare_names(tmp_path):
    """One field naming several files yields each once, and a bare name maps to its only path outside .git."""
    for path in ("src/sh/install.sh", ".git/hooks/install.sh", "Makefile"):
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text("")
    cited = "Makefile (lines 24, 46-49); install.sh and Makefile"
    assert runner.cited_files(cited, tmp_path) == ["Makefile", "src/sh/install.sh"]


@pytest.mark.parametrize(
    ("cited", "expected"),
    [
        ("{root}/steps.md:12-30", "steps.md"),
        ("steps.md (lines 9, 26)", "steps.md"),
        ("steps.md/steps.md", "steps.md"),
        ("`./steps.md`", "steps.md"),
        ("steps.md", "steps.md"),
    ],
)
def test_cited_files_drops_line_notes_and_the_scratch_folder(tmp_path, cited, expected):
    """A single file copied into a folder of its own name is cited many ways, and each maps back to the file."""
    root = tmp_path / "steps.md"
    assert runner.cited_files(cited.format(root=root), root) == [expected]


def test_rank_keeps_a_citation_with_glob_characters(tmp_path):
    """A cited name holding glob characters is matched literally, so ranking keeps it instead of failing."""
    (tmp_path / "a.py").write_text("x\n")
    ranked = runner.rank({"newcomer": [_make_finding("[draft]*.md")], "maintainer": None}, tmp_path)
    assert [file for file, _ in ranked] == ["[draft]*.md"]
