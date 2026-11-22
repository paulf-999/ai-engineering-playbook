# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A ready-made set of Claude instructions that your team installs with one command, so everyone works to the same standards.

**Goal:** get new and experienced Claude Code users started quickly.

It's built around two ideas:

- ⚡ **Selective context loading:** Claude reads [only the instructions a task needs](src/claude/rules/README.md), so it stays fast and focused.
- 🔄 **AI-SDLC:** following Anthropic's [course on the SDLC for AI](https://academy.claude.com/courses/ai-native-sdlc-playbook), Claude writes an [intent, spec and plan](src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) for you to approve, then builds to it.

For details, see the [implementation overview](docs/target_architecture/implementation_overview.md).

---

## 🪄 Getting Started

The [getting-started guide](docs/guides/getting_started.md) covers which install to choose, what installing changes and a first prompt to try.

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Run `make install` to install for every project, into `~/.claude`, or `make install PROJECT=<path to repo>` to install into one repo's `.claude/` folder.

---

## 🗺️ What's in this repo

Everything you install is in [`src/claude/`](src/claude/). The rest of the repo explains and maintains it, and you don't need it to use the instructions.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
