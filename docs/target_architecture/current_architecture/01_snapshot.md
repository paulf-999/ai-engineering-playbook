<!-- version: 1.1.0 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-03 -->
# 📸 Current architecture: Snapshot

**Purpose:** each component of the old Claude configuration, how it loads into Claude, and what it's for.

This page is part of the [current architecture](../current_architecture.md) review of commit `915685f`. Rules that load "always" add to every session's context, so they cost tokens whatever the task:

| Component | Count | How it loads | What it's for |
|---|---|---|---|
| 📄 `CLAUDE.md` | 1 file, 42 lines | Always | Index of core principles and imports |
| 📥 Always-on rules | 36 files, about 1,900 lines | Always, about 30,000 tokens | Standards for behaviour, writing, naming, git, security and response format |
| 📂 Path-scoped rules | 10 files, plus 10 language style guides moved from the reference docs at install | Only when Claude opens a matching file | Detailed guidance for certain file types |
| 💤 Lazy-loaded rules | 29 files | Only when another rule tells Claude to read them | Detail split out of longer rules, and rarely needed guidance |
| 📚 Reference docs | 184 files, including 108 quality scorecards | Read by people, or by Claude when a rule points to them | Style guides, and records of each component's reviewed quality |
| 🛠️ Skills | 8 | When a trigger phrase matches | Multi-step workflows, such as raising a PR |
| 🤖 Agents | 3 | When started, as a separate Claude with its own context | Code review, technical writing and quality review |
| 🪝 Hooks | 5 scripts, 4 switched on in settings | Automatically, on prompts and tool calls | Naming and file-location checks, a settings warning and a per-turn reminder |
| 🧪 Tests and checks | 81 test files, 22 pre-commit hooks, 1 CI workflow | Before each commit, then in CI for each PR | Checks on structure, hooks, skills and scripts |
