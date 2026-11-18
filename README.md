# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A practical playbook that treats AI-assisted engineering as a discipline, not a collection of prompts.

**Goal:** favour simplicity, selective context loading, spec-led workflows and evidence-based decisions.

It's built for data teams working with dbt, Snowflake and Airflow, though its general rules suit any project.

---

## 🪄 Getting Started

The [getting-started guide](docs/guides/getting_started.md) covers what you need, which install to choose, what installing changes and a first prompt to try.

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Run `make install PROJECT=<path to repo>` to install into one repo's `.claude/` folder, or `make install` to install for every project, into `~/.claude` or `$CLAUDE_CONFIG_DIR` if set.

> [!NOTE]
> Run it in your own terminal, and `make uninstall` with the same `PROJECT=` undoes it.

---

## 🗺️ What's in this repo

Everything you install is in [`src/claude/`](src/claude/). The rest of the repo explains and maintains it, and you don't need it to use the instructions.

---

## 📦 What you get

- ⚡ **Lean:** Claude [loads instructions in three ways](src/claude/rules/README.md): core rules every session, file-specific rules only when it works on matching files, and the rest only when a task calls for them, so it stays fast and focused.
- 📄 **`CLAUDE.md`:** [this file](src/claude/CLAUDE.md) builds in [Andrej Karpathy's four rules](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), so Claude makes fewer common coding mistakes.
- 🔄 **AI-SDLC:** for planned work, Claude [agrees what to build and how](src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) before coding, then checks the result against that plan.
- 🔍 **Evidence:** a [before-and-after example](docs/examples/dbt/dbt_before_and_after.md) and [measured runs](docs/examples/dbt/dbt_rules_measured.md) show what the dbt rules change. Only the dbt rules are measured so far.
- 👤 **Opt-in preferences:** personal ones, such as the reply format, install only with `make install PREFERENCES=1`.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
