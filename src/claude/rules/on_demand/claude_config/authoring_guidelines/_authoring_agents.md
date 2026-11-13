<!-- version: 1.1.1 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-13 -->
# 🤖 Authoring agents

**Purpose:** when to build an agent for Claude's config, and how to write and check one.

This page is part of the authoring guidelines, `on_demand/claude_config/authoring_guidelines.md`.

## 🧭 When an agent

- 👥 **Own context:** build one only when the work needs a separate context or an independent view, such as a blind review.
- 🔄 **Otherwise:** use a skill for a procedure and a rule for guidance, since an agent costs a fresh context each run.
- 🏷️ **Name and place:** `agents/<group>/<name>/AGENT.md`, with a `<domain>-<purpose>` name, such as `technical-writer`, hyphenated to match skills, though the [Claude Code subagent docs](https://code.claude.com/docs/en/sub-agents) allow any name without a `:`.

## 📝 Writing it

- 📄 **Template:** start from `_templates/AGENT.md.template`, and keep the result to about 40 to 60 lines.
- 🗣️ **Description:** say when Claude should delegate to it, since Claude Code decides from the description alone, and keep it short, since it loads in every session.
- 🔐 **Tools:** list only what the job needs, since leaving `tools:` out grants every tool.
- 🌳 **Isolation:** set `isolation: worktree` only for an agent that changes files.
- 🚧 **Constraints:** say what it doesn't do, and why.

## ✅ Before merging

- 🧪 **Evals:** add evals that cover its main triggers and one case where it shouldn't fire.
- 📋 **Evaluation criteria:** answer the PR template's Evaluation criteria section.
- 🏅 **Review:** have a fresh-context reviewer score it against a rubric for its type, modelled on `docs/maintenance/quality/themes/quality_themes_rules.md`, in the playbook repo.
