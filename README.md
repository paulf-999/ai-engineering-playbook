# 🧭 AI Engineering Playbook

[![CI](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/paulf-999/ai-engineering-playbook/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue?logo=python\&logoColor=white)](https://docs.astral.sh/ruff/)

A practical playbook for consistent, repeatable work with AI coding assistants, starting with a lean set of instructions for Claude Code.

---

## 🪄 Getting Started

You need `git`, `bash` and [`jq`](https://jqlang.org/) on macOS or Linux, and a git clone rather than a zip download, since the installer copies only tracked files.

1. Clone the repository:

   ```bash
   git clone https://github.com/paulf-999/ai-engineering-playbook.git
   cd ai-engineering-playbook
   ```

2. Run `make install` to copy [`src/claude/`](src/claude/) into your Claude config directory, `~/.claude`, or `$CLAUDE_CONFIG_DIR` if set.

> [!NOTE]
> It backs up any file it replaces to `backups/` in that directory first. To install into one repo's `.claude/` folder instead, run `make install PROJECT=<path to repo>`. To undo an install, run `make uninstall`, with the same `PROJECT=` if you set one.

---

## 🔧 What installing changes

Besides adding instructions, installing changes how Claude works in every project:

- 💬 **Replies:** Claude opens with a short summary, uses emoji bullets and British spelling, and offers options before big changes.
- 🗺️ **Plans:** a long plan must say what you want and how to check it's done, and Claude waits for your go-ahead even after you accept it.
- 🪝 **Hooks:** one blocks long plans that skip those sections, and one sends Claude back to run the repo's checks before it finishes, which a one-repo install leaves out unless you add `HOOKS=1`.
- 🔒 **Files:** Claude's file tools can't read `.env` files, and it saves plans to your Claude config directory and progress notes to your home folder.

---

## 📦 What you get

- ⚡ Claude reads only the instructions each task needs, so it stays fast and focused.
- 📂 Each rules folder [sets when its rules load](src/claude/README.md#️-when-rules-load).
- 📦 Everything you install is in [`src/claude/`](src/claude/); the rest of the repo explains and maintains it.
- 🔍 See [a before-and-after example](docs/examples/dbt_before_and_after.md).

<!-- separates the intro list from the feature list -->

- 📄 **`CLAUDE.md`:** [this file](src/claude/CLAUDE.md) builds in [Andrej Karpathy's four rules](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), so Claude makes fewer common coding mistakes.
- 🔄 **AI-SDLC:** for planned work, Claude [agrees what to build and how](src/claude/rules/always_on/workflows/sdlc_workflow.md) before coding, then checks the result against that plan, following [Anthropic's AI-native software development lifecycle](docs/target_architecture/reference_material/core/anthropic_ai_native_sdlc.md).
- 🔬 **Research-led:** every part of the [design](docs/target_architecture/README.md) is grounded in [research from Anthropic and DORA](docs/target_architecture/reference_material/README.md) (Google's DevOps research programme).
- ✅ **Stays lean:** automatic [checks](docs/target_architecture/architecture/_budget_and_guards.md#️-design-guards) stop the always-read instructions growing.

---

## 🗺️ What's in this repo

| Folder | What it holds |
|---|---|
| 📦 [`src/claude/`](src/claude/) | What you install: the instructions Claude reads |
| 🏗️ [`docs/`](docs/) | Why it's built this way: the design and the research behind it |
| 🛠️ [`maintenance/`](maintenance/), [`tests/`](tests/), [`.github/`](.github/) | How it stays healthy: tests for the installer, hooks and scripts, plus quality scores and CI. You don't need these to use it |

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
