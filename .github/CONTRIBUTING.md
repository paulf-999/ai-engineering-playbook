<!-- version: 3.3.3 -->
<!-- created: 2025-09-18 -->
<!-- updated: 2026-11-05 -->
# 🤝 Contributing

**Purpose:** the branch, commit and PR conventions every contribution to this repo follows.

Before your first commit, activate a virtualenv (see the [virtualenv setup guide](../docs/guides/virtualenv_setup.md)) and run `make deps`, which installs the pre-commit hooks these conventions rely on.

## 🌱 Branching

- 📖 **Strategy:** follow the [Git branching strategy](../docs/guides/git_branching_strategy.md).
- 🛂 **Checked:** a pre-commit hook rejects branch names that break it.

## 📝 Commits

- 📐 **Format:** write `type(scope): imperative description`, following [Conventional Commits](https://www.conventionalcommits.org/).
  - **Type:** the kind of change, such as `feat`, `fix` or `docs`.
  - **Scope:** the area of the repo affected, such as `makefile` or `ci`.
- 🛂 **Checked:** a commit-message hook rejects any message that doesn't match the format.
- 🧰 **Helper:** stage your files and run `src/sh/git/git_commit.sh` to build a valid message step by step.

Two valid messages:

- `feat(pre-commit): add ruff`
- `fix(makefile): run pytest from make test`

## 🔀 Pull Requests

- 📄 **Template:** fill in the [PR template](pull_request_template.md).
- 🔤 **Title:** use the commit format, because a squash merge makes the title the commit message on `main`.
- 📏 **Size:** keep each PR to 20 files or fewer, or use a [`release/` branch](../docs/guides/git_branching_strategy.md#-exceptions-for-large-changes--use-the-release-prefix) for one bulk change.
- 🗒️ **Optional details:** keep the template's Additional Details section to 5 bullets, with full GitHub URLs, since CI checks both.
- ⚖️ **Evaluation criteria:** when the PR changes `src/claude/`, answer each check in the template's Evaluation criteria section, which CI also checks.
- 💥 **Breaking change:** tick it if it applies, and describe the rollout impact.

### ✅ Before raising a PR

Both checks must pass:

- 🪝 **Pre-commit hooks:** fix what they flag, rather than skipping them with `--no-verify`.
- 🧪 **Tests:** run `make test`.

## 🏷️ File naming

- 🔡 **Rule:** name every file and folder in lowercase snake_case, such as `design_principles.md`.
- ❓ **Why:** Python can't import a module with a hyphen in its name, so the whole repo uses underscores to match.
- 📌 **Exceptions:** conventional names such as `README.md`, `CLAUDE.md` and `Makefile`.
