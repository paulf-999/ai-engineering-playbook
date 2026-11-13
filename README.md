<!-- version: 2.3.7 -->
<!-- created: 2022-11-04 -->
<!-- updated: 2026-11-13 -->
# 🧭 AI Engineering Playbook

**Purpose:** a ready-made set of instructions for Claude Code, Anthropic's AI coding assistant, kept small so Claude stays focused on your task.

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

---

## 📦 What you get

Claude Code reads instruction files before it works. A few of these apply to every task, and the rest are read only when a task needs them, so Claude isn't slowed down by instructions it doesn't need. You get:

- [Core guidelines](src/claude/CLAUDE.md): a short page of good working habits Claude follows on every task
- [Style guides](src/claude/rules/_path_scoped_rules/style_guides/) for SQL, dbt, Python, Airflow, Terraform and more, each used only when Claude works on that kind of file
- Guidance Claude looks up only when a task calls for it, such as using git, writing tests or planning work
- The [design](docs/target_architecture/target_architecture.md) behind it, with its [principles](docs/target_architecture/design_principles.md) and the [research from Anthropic and DORA](docs/target_architecture/reference_material/README.md), Google's DevOps research programme, that it draws on
- Automatic [checks](.github/workflows/ci.yml) that stop the every-task instructions growing too long

---

## 🪄 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Create and activate a virtualenv (see the [virtualenv setup guide](docs/guides/virtualenv_setup.md)), then run `make deps` to install the requirements and the pre-commit git hooks.
3. Run `make test` to check everything works.
4. Run `make install` from your own terminal to copy [`src/claude/`](src/claude/) into your Claude config directory, `$CLAUDE_CONFIG_DIR` or `~/.claude`, backing up any file it replaces or removes, since it also removes files an earlier install added that the repo has since dropped.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover branches, commit messages and PRs.
