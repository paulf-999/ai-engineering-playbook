<!-- version: 2.3.1 -->
<!-- created: 2022-11-04 -->
<!-- updated: 2026-11-04 -->
# 🧭 AI Engineering Playbook

**Purpose:** a practical playbook for consistent, repeatable AI-assisted engineering, starting with the design for a lean Claude Code setup.

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

---

## 📦 What it provides

The playbook adds a Claude Code component only when real tasks show it's needed. It provides:

- The [target architecture](docs/target_architecture/target_architecture.md): what every session loads, what loads only when needed, and how results are measured
- [Design principles](docs/target_architecture/design_principles.md) and the checks each new component must pass
- The [reference material](docs/target_architecture/reference_material/README.md) it draws on, from Anthropic and DORA (DevOps Research and Assessment)
- A starter global Claude config, [`src/templates/global_claude.md`](src/templates/global_claude.md)
- Pre-commit hooks on every commit, and tests and [CI checks](.github/workflows/ci.yml) on every PR

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover branches, commit messages and PRs.

---

## 🪄 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Create and activate a virtualenv (see the [virtualenv setup guide](docs/guides/virtualenv_setup.md)), then run `make deps` to install the requirements and the pre-commit git hooks.
3. Run `make test` to check everything works.
