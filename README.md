<!-- version: 2.3.24 -->
<!-- created: 2022-11-04 -->
<!-- updated: 2026-11-13 -->
# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A practical playbook for consistent, repeatable work with AI coding assistants, starting with a lean set of instructions for Claude Code.

---

## 🪄 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Create and activate a virtualenv (see the [virtualenv setup guide](docs/guides/virtualenv_setup.md)).
3. Run `make deps` to install the requirements and the pre-commit git hooks.
4. Run `make install` to copy [`src/claude/`](src/claude/) into your Claude config directory, `~/.claude`.

---

## 📦 What you get

Claude reads only the instructions each task needs, so it stays fast and focused.

- 📄 **`CLAUDE.md`:** [this file](src/claude/CLAUDE.md) makes Claude state its assumptions, ask when unclear, keep changes small and prove them with tests.
- 🔬 **Research-led:** every part of the [design](docs/target_architecture/target_architecture.md) is grounded in [research from Anthropic and DORA](docs/target_architecture/reference_material/README.md) (Google's DevOps research programme).
- 🔄 **AI-SDLC:** Claude [agrees what to build and how](src/claude/rules/_rules_on_demand/03_workflows/sdlc_workflow.md) before coding, then checks the result against that plan, following [Anthropic's AI-native software development lifecycle](docs/target_architecture/reference_material/core/anthropic_ai_native_sdlc.md).
- ✅ **Stays lean:** automatic [checks](.github/workflows/ci.yml) stop the always-read instructions growing.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover branches, commit messages and PRs.
