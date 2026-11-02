<!-- version: 1.0.1 -->
<!-- created: 2026-11-02 -->
<!-- updated: 2026-11-02 -->
# 📸 Current architecture: Snapshot

For anyone shaping the target architecture: what the repo contains, how each part loads into Claude, and what it is for.

- **Part of:** [Current architecture](../current_architecture.md).
- 📌 **Snapshot:** everything here describes [`claude_ai_playbook`](https://github.com/paulf-999/claude_ai_playbook) at commit `915685f`, dated 2026-10-31.

| Component | Count | How it loads | What it's for |
|---|---|---|---|
| 📄 `CLAUDE.md` | 1 file, 42 lines | Always, in every session. | Index of core principles and imports. |
| 📥 Always-on rules | 36 files, about 1,900 lines | Always, in every session, about 30,000 tokens. | Standards for behaviour, writing, naming, git, security and response format. |
| 📂 Path-scoped rules | 10 files, plus 10 style guides added at install | Only when Claude opens a matching file. | Detail on authoring, directories, rule loading, testing and plan format, plus language style guides. |
| 💤 Lazy-loaded rules | 29 files | On demand, read only when a rule points to them. | Bulky children and rarely needed guidance. |
| 📚 Reference docs | 184 markdown files, including 108 quality scorecards and the 10 style guides installed as path-scoped rules | On demand, read by people, or by Claude when a rule points to them. | Style guides, and scorecards recording each artefact's independently reviewed quality. |
| 🛠️ Skills | 8 | On request, when a trigger phrase matches. | Workflows packaging multi-step tasks, such as raising a PR or a Jira ticket. |
| 🤖 Agents | 3 | On spawn, as a separate Claude instance with its own context. | Code review, technical writing and scorecard review, each in its own context for independence. |
| 🪝 Hooks | 5 scripts, 4 registered | Run automatically by Claude Code on prompts and tool calls. | Naming and file-location checks, a stale-settings warning and a per-turn response-format reminder. |
| 🧪 Tests and checks | 81 test files, 22 pre-commit hooks, 1 CI workflow | Checks before each commit, then CI (continuous integration) on GitHub for each PR. | Verification of structure, hooks, skills and scripts. |
