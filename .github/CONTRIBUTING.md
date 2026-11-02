<!-- version: 3.2.3 -->
<!-- created: 2025-09-18 -->
<!-- updated: 2026-11-02 -->
# 🤝 Contributing

For anyone contributing to this repo: the branch, commit and PR conventions to follow.

After cloning, activate a virtualenv (see [Virtualenv setup](../docs/reference/virtualenv_setup.md)) and run `make deps` once, so the pre-commit hooks these conventions rely on are installed. `make deps` stops if no virtualenv is active, so packages never land in your system Python.

---

## 🌱 Branching

Follow the rules in [Git Branching Strategy](../docs/reference/git_branching_strategy.md). Branch names are automatically validated by the pre-commit hook at `src/sh/git/git_validate_branch_name.sh`.

## 📝 Commits

Follow [Conventional Commits](https://www.conventionalcommits.org/) using the format `type(scope): imperative description`, where `type` is a Conventional Commits type such as `feat`, `fix` or `docs`, and `scope` is the area of the repo affected (e.g. `makefile`, `pre-commit`, `ci`). A commit-msg hook runs commitlint, which rejects any message not in this format, and `src/sh/git/git_commit.sh` lists every type it allows.

Examples:

- `feat(pre-commit): add ruff`
- `fix(makefile): run pytest from make test`

To build a valid message interactively, stage your files and run `src/sh/git/git_commit.sh`. It offers the top-level folders of the staged files as the scope, or lets you type your own.

## 🔀 Pull Requests

- Use the [PR template](pull_request_template.md) and fill in the summary section.
- Write the PR title in the same `type(scope): description` format as a commit, because squash merges use it as the commit message on `main` and CI checks it.
- Keep PRs small and focused — split into multiple PRs by logical area if a change goes over the file limit, or use a `release/` branch for one bulk change (see [Exceptions for Large Changes](../docs/reference/git_branching_strategy.md#-exceptions-for-large-changes--use-the-release-prefix)).
- Keep **Additional Details** to 5 bullets or fewer, and use full GitHub URLs for links, because CI checks both and relative links don't work in a PR.
- Mark **Breaking Change** if applicable and describe the rollout impact.
- Pre-commit hooks must pass before raising a PR — fix the underlying issue rather than bypassing with `--no-verify`.
- Run `make test` and make sure it passes before raising a PR.

## 🏷️ File naming

- **Rule:** name every file and folder in lowercase snake_case, e.g. `docs/target_architecture/design_principles.md`.
- **Why one rule:** Python can't import a module with hyphens in its name, so docs and scripts use underscores to match.
- **Exceptions:** conventional names keep their usual form, such as `README.md`, `CLAUDE.md`, `CONTRIBUTING.md` and `Makefile`.
