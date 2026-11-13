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

Two valid messages:

- `feat(pre-commit): add ruff`
- `fix(makefile): run pytest from make test`

## 🔀 Pull Requests

- 📄 **Template:** fill in the [PR template](pull_request_template.md).
- 🔤 **Title:** use the commit format, because a squash merge makes the title the commit message on `main`.
- 📏 **Size:** keep each PR within the file limit CI checks, or use a [`release/` branch](../docs/guides/git_branching_strategy.md#-exceptions-for-large-changes--use-the-release-prefix) for one bulk change.
- ⚖️ **Evaluation criteria:** when the PR changes an always-on or enforcing file, such as `src/claude/CLAUDE.md`, a rule in a numbered folder or a hook, have a fresh-context reviewer agent fill the template's Evaluation criteria section, which CI checks is answered.
- 💥 **Breaking change:** tick it if it applies, and describe the rollout impact.

### ✅ Before raising a PR

- 🪝 **Pre-commit hooks:** fix what they flag, rather than skipping them with `--no-verify`.
- 🧪 **Done:** meet [Done means](../CLAUDE.md) in `CLAUDE.md` before raising the PR.
- 📊 **Scores:** leave the [quality audits](../maintenance/quality/audits/) as they are, since each regular review re-scores every test and rule changed since the last one, in one PR.

## 🚀 Releases

A release tags `main` once merged PRs are worth installing together.

- 🔢 **Version:** tag `vMAJOR.MINOR.PATCH`, per [Semantic Versioning](https://semver.org/). Below `1.0.0`, bump MINOR for features or breaking changes and PATCH for fixes only.
- 📝 **Notes:** open with one line on what the release delivers, then up to 5 emoji bullets, with file links pinned to the tag.
- 🛠️ **Publish:** run `gh release create vX.Y.Z --target main --title vX.Y.Z --notes-file <notes.md>`.
- 🔀 **Not a `release/` branch:** that prefix is for one bulk change over the PR file limit, not for versions.

## 🏷️ File naming

- 🔡 **Rule:** follow the [naming standards](../src/claude/rules/01_standards/naming_standards.md), which the Claude config also loads in every session.
- 📌 **Exceptions:** conventional names such as `README.md`, `CLAUDE.md` and `Makefile`.
