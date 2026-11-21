# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A ready-made set of Claude instructions that your team installs with one command, so everyone works to the same standards.

Once installed, Claude Code, Anthropic's AI coding assistant, reads only the instructions a task needs, shows you a plan to approve before it writes code, and keeps an instruction only if Claude does better with it than without it.

**Goal:** suit new and experienced Claude Code users, keeping things simple and following Anthropic's [course on building software with AI](https://academy.claude.com/courses/ai-native-sdlc-playbook).

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

## 📦 What you get

- ⚡ **Selective context loading:** Claude reads [only the instructions a task needs](src/claude/rules/README.md), so it stays fast and focused.
- 📄 **`CLAUDE.md`:** [builds in](src/claude/CLAUDE.md) [Andrej Karpathy's four rules](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), such as think before coding and keep changes small, to cut common coding mistakes.
- 🔄 **AI-SDLC:** Claude [agrees a plan](src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) before coding, then checks the result against it.
- 🔍 **Evidence:** a [before-and-after example](docs/examples/dbt/dbt_before_and_after.md) and measured [dbt](docs/examples/dbt/dbt_rules_measured.md) and [Airflow](docs/examples/airflow/airflow_rules_measured.md) runs show the effect.
- 🧩 **Templates:** add your own instructions from [ready-made templates](src/claude/_templates/README.md) that come with tests.
- 👤 **Preferences:** optional personal settings, like the reply format, which you can skip with `PREFERENCES=0`.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
