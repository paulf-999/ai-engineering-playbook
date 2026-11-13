<!-- version: 2.3.6 -->
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

To try it, copy [`src/claude/CLAUDE.md`](src/claude/CLAUDE.md) into the `.claude` folder in your home folder, where Claude Code looks for your instructions. To install everything:

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Set up Python (see the [virtualenv setup guide](docs/guides/virtualenv_setup.md)), then run `make deps` to install the tools and `make test` to check they work.
3. Run `make install` in your own terminal. It copies the instructions into `~/.claude`, or `$CLAUDE_CONFIG_DIR` if you've set it, backs up every file it changes to `~/.claude/backups/`, and removes only files an earlier install added.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover branches, commit messages and PRs.
