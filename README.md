<!-- version: 2.2.0 -->
<!-- created: 2022-11-04 -->
<!-- updated: 2026-11-03 -->
# 🧭 AI Engineering Playbook

*A practical playbook for consistent, repeatable AI-assisted engineering.*

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

---

## 🎯 Purpose

A **lean, evidence-led Claude Code setup**, providing:

- The [target architecture](docs/target_architecture/target_architecture.md): what's mandatory, what loads on demand, and how it's measured
- [Design principles](docs/target_architecture/design_principles.md) and the checks each new component must pass
- The [reference material](docs/target_architecture/reference_material/README.md) it draws on, from Anthropic and DORA (DevOps Research and Assessment)
- A starter global Claude config, [`src/templates/global_claude.md`](src/templates/global_claude.md)
- Pre-commit hooks, tests and [CI](.github/workflows/ci.yml) on every PR

---

## 📝 Contributing

Before raising a PR, please:

- Follow the [Contributing Guidelines](.github/CONTRIBUTING.md) – commit messages and PR rules.
- Use the [Git Branching Strategy](docs/reference/git_branching_strategy.md) – branch types and naming rules.
- Complete the [Pull Request Template](.github/pull_request_template.md) – summary, change type, testing.

---

## 🪄 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Create and activate a virtualenv (see [docs/reference/virtualenv_setup.md](docs/reference/virtualenv_setup.md)), then run `make deps` to install the requirements and the pre-commit git hooks.
3. Run `make test` to check everything works.
