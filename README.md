<!-- version: 2.3.30 -->
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

2. Run `make install` to copy [`src/claude/`](src/claude/) into your Claude config directory, `~/.claude`.
   - It backs up any file it replaces to `~/.claude/backups/` first.

---

## 📦 What you get

Claude reads only the instructions each task needs, so it stays fast and focused. Each rules folder [sets when its rules load](src/claude/README.md#️-when-rules-load). Everything you install is in [`src/claude/`](src/claude/); the rest of the repo explains and maintains it.

- 📄 **`CLAUDE.md`:** [this file](src/claude/CLAUDE.md) builds in [Andrej Karpathy's four rules](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md), so Claude makes fewer common coding mistakes.
- 🔬 **Research-led:** every part of the [design](docs/target_architecture/target_architecture.md) is grounded in [research from Anthropic and DORA](docs/target_architecture/reference_material/README.md) (Google's DevOps research programme).
- 🔄 **AI-SDLC:** for planned work, Claude [agrees what to build and how](src/claude/rules/on_demand/workflows/sdlc_workflow.md) before coding, then checks the result against that plan, following [Anthropic's AI-native software development lifecycle](docs/target_architecture/reference_material/core/anthropic_ai_native_sdlc.md).
- ✅ **Stays lean:** automatic [checks](.github/workflows/ci.yml) stop the always-read instructions growing.

---

## 📝 Contributing

Before raising a PR, read the [contributing guidelines](.github/CONTRIBUTING.md), which cover setup, branches, commit messages and PRs.
