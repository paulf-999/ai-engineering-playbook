<!-- version: 1.1.1 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-10 -->
# 🤖 CLAUDE.md — AI Engineering Playbook

## 🎯 Project

A playbook for a lean, evidence-led Claude Code setup: design docs in `docs/target_architecture/`, plus shell helpers and their tests. Most changes are markdown docs.

| Task | Command |
|---|---|
| 📦 Install requirements and git hooks | `make deps` |
| 🧪 Run the tests | `make test` |
| ✅ Run every check | `pre-commit run --all-files` |

- 🏁 **Done means:** `make test` and `pre-commit run --all-files` both pass.
- 📜 **Conventions:** follow `.github/CONTRIBUTING.md` for branching, commits and PRs.
- 🧪 **Tests:** maintain tests per `docs/maintenance/test_maintenance.md`.
