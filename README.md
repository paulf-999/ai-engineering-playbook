<!-- version: 2.1.6 -->
<!-- created: 2022-11-04 -->
<!-- updated: 2026-11-02 -->
# 🧩 Template Git Repo

*Baseline for creating new internal repositories with consistent structure and standards.*

[![CI](https://github.com/paulf-999/template_git_repo/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/template_git_repo/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

---

## 🎯 Purpose

A **generic starting point** for new projects, providing:

- 🗂️ **Git structure:** a standard layout.
- 📋 **Templates:** templates for PRs, CODEOWNERS and branching.
- 🤖 **Claude config:** a starter global Claude config, [`src/templates/global_claude.md`](src/templates/global_claude.md).

### ✅ Checks

- 🪝 **Pre-commit hooks:** for linting and validation.
- 🧪 **Tests:** for the helper scripts, run with `make test`.
- ⚙️ **CI:** [runs on every PR](.github/workflows/ci.yml), which re-runs the hooks and tests and checks the PR's title and size.

---

## 📝 Contributing

Before raising a PR, please:

- 📜 **Conventions:** follow the [Contributing Guidelines](.github/CONTRIBUTING.md) – overview of branch naming, commit messages and PR rules.
- 🌿 **Branches:** use the [Git Branching Strategy](docs/reference/git_branching_strategy.md) – includes branch types and naming rules.
- 👥 **Reviewers:** rely on [CODEOWNERS](.github/CODEOWNERS) – reviewers are auto-assigned by repo area.
- 🧾 **PR description:** complete the [Pull Request Template](.github/pull_request_template.md) – summary, change type, testing.

---

## 🪄 How to Use This Repo

### 🆕 Create the repo

1. **Template:** click **“Use this template”** at the top of the repository page.
2. **Name:** enter a name for your new repository and create it.
3. **Clone:** clone your new repository locally:

   ```bash
   git clone <new-repo-url>
   cd <new-repo>
   ```

### 🛠️ Set it up

1. **Install:** create and activate a virtualenv (see [docs/reference/virtualenv_setup.md](docs/reference/virtualenv_setup.md)), then run `make deps` to install the requirements and the pre-commit git hooks.
2. **Customise:** update the `README.md`, `requirements.txt` and `.github/CODEOWNERS` as needed, and fill in the TODOs in `CLAUDE.md`.
3. **Check:** run `make test` to check everything works.
