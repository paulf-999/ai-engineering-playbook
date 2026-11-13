<!-- version: 2.3.20 -->
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

Claude Code reads instruction files before it works. A few of these apply to every task, and the rest are read only when a task needs them, so Claude isn't slowed down by instructions it doesn't need. You get:

- A boilerplate [`CLAUDE.md`](src/claude/CLAUDE.md) to use as your own, the main instructions file Claude Code reads in every session
- [Rules](src/claude/rules/_rules_on_demand/03_workflows/sdlc_workflow.md) that take each change through the stages of Anthropic's [AI-native software development lifecycle (AI-SDLC)](docs/target_architecture/reference_material/core/anthropic_ai_native_sdlc.md): why it matters, what to build, the plan, building and testing, then review
- The [design](docs/target_architecture/target_architecture.md) behind it, with its [principles](docs/target_architecture/design_principles.md) and the [research from Anthropic and DORA (Google's DevOps research programme)](docs/target_architecture/reference_material/README.md) that it draws on
- Automatic [checks](.github/workflows/ci.yml) that stop the every-task instructions growing too long

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover branches, commit messages and PRs.
