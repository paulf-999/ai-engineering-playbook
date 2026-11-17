# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A practical playbook for consistent, repeatable work with AI coding assistants, starting with a lean set of instructions for Claude Code.

---

## 🪄 Getting Started

The [getting-started guide](docs/guides/getting_started.md) covers what you need, which install to choose, what installing changes and a first prompt to try.

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Run `make install` to copy [`src/claude/`](src/claude/) into your Claude config directory, `~/.claude`, or `$CLAUDE_CONFIG_DIR` if set.

> [!NOTE]
> Run it in your own terminal. For one repo only, use `make install PROJECT=<path to repo>`, and `make uninstall` undoes either.

---

## 📦 What you get

- ⚡ **Lean:** Claude reads only the instructions each task needs, so it stays fast and focused.
- 📄 **`CLAUDE.md`:** [this file](src/claude/CLAUDE.md) builds in [Andrej Karpathy's four rules](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), so Claude makes fewer common coding mistakes.
- 🔄 **AI-SDLC:** for planned work, Claude [agrees what to build and how](src/claude/rules/always_on/01_standards/workflows/sdlc_workflow.md) before coding, then checks the result against that plan.
- 🔍 **Evidence:** a [before-and-after example](docs/examples/dbt_before_and_after.md) and [measured runs](docs/examples/dbt_rules_measured.md) show what the dbt rules change.
- 👤 **Opt-in preferences:** personal ones, such as the reply format, install only with `make install PREFERENCES=1`.

---

## 🗺️ What's in this repo

Everything you install is in [`src/claude/`](src/claude/). The rest of the repo explains and maintains it, and you don't need it to use the instructions.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
