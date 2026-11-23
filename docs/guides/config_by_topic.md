# 🗺️ Config by topic

**Purpose:** every Claude config file for one topic, such as security, and when each loads, so you needn't search `always_on/`, `path_scoped/`, `on_demand/`, skills, agents and hooks separately.

This page sits in `docs/`, so it's never installed. It lists parent files only, since each parent links its own `_` child files. A test fails when a parent file is missing from the map, except the style guides.

## 🔄 Workflow and planning

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🔄 [ai_sdlc_workflow.md](../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | Always-on rule | Every session |
| 🛡️ [behaviour.md](../../src/claude/rules/always_on/01_standards/behaviour.md) | Always-on rule | Every session |
| 🗂️ [claude_working_files.md](../../src/claude/rules/always_on/02_preferences/claude_working_files.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| ✅ [reporting.md](../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | On-demand rule | Before saying a task is done |
| 🤖 [automation_controls.md](../../src/claude/rules/on_demand/01_standards/conduct/automation_controls.md) | On-demand rule | Before proposing or starting a loop or other unattended run |
| ⏱️ [turn_budgets.md](../../src/claude/rules/on_demand/01_standards/claude_config/turn_budgets.md) | On-demand rule | When setting turn caps for `claude -p` or another unattended run |
| 🗂️ [hook_enforcement_plan_sections.sh](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | Hook | On `ExitPlanMode`, blocking a long plan with no Intent or Spec heading |
| 🔍 [hook_enforcement_plan_review.sh](../../src/claude/hooks/hook_enforcement_plan_review.sh) | Hook | On `ExitPlanMode`, blocking a long plan until a cold reviewer scores it 10/10, for up to 2 rounds |
| ✅ [hook_enforcement_done_checks.sh](../../src/claude/hooks/hook_enforcement_done_checks.sh) | Hook | On stop, sending Claude back once to run the done checks |
| 🌳 [hook_enforcement_worktree_edits.sh](../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | Hook | On a session's first edit in a repo's main folder |
| 🔁 [hook_reminder_kaizen_due.sh](../../src/claude/hooks/hook_reminder_kaizen_due.sh) | Hook | On session start, once 5 or more feedback notes are new |
| 🔁 [claude-kaizen/SKILL.md](../../src/claude/skills/_claude_skills/claude-kaizen/SKILL.md) | Skill | On `/claude-kaizen`, or when the kaizen reminder suggests it |
| 📜 [claude-capture-session-prompts/SKILL.md](../../src/claude/skills/_claude_skills/claude-capture-session-prompts/SKILL.md) | Skill | When asked to capture or audit a day's session prompts |

</details>

## 🔐 Security

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🔐 [security.md](../../src/claude/rules/always_on/01_standards/security.md) | Always-on rule | Every session |
| 🛡️ [code_security.md](../../src/claude/rules/path_scoped/01_standards/code_security.md) | Path-scoped rule | Reading `.py`, `.sh`, `.sql`, `.tf` or `.tfvars` files |
| 🔑 [permission_recommendations.md](../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md) | On-demand rule | Before recommending a permission or allowlist change |
| 🔍 [code-reviewer/AGENT.md](../../src/claude/agents/core/code-reviewer/AGENT.md) | Agent | When asked to review or score a local diff |

</details>

## 🧠 Claude config authoring

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🧭 [guiding_principles.md](../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | On-demand rule | Before proposing a rule, skill, hook, import, setting or memory note |
| 🏷️ [claude_naming_patterns.md](../../src/claude/rules/on_demand/01_standards/claude_config/claude_naming_patterns.md) | On-demand rule | Before naming a new rule, skill or agent |
| 🔑 [permission_recommendations.md](../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md) | On-demand rule | Before recommending a permission or allowlist change |

</details>

## 🧪 Testing

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🧪 [path_scoped/01_standards/testing.md](../../src/claude/rules/path_scoped/01_standards/testing.md) | Path-scoped rule | Reading `.py`, `.sh` or dbt model `.sql` files |
| 📋 [on_demand/01_standards/testing.md](../../src/claude/rules/on_demand/01_standards/testing.md) | On-demand rule | Before writing or reviewing a test |

</details>

## 🌿 Git and PRs

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🌿 [git.md](../../src/claude/rules/on_demand/01_standards/git.md) | On-demand rule | Before any git command, or when the worktree hook blocks an edit |
| 📤 [git-create-pr/SKILL.md](../../src/claude/skills/_git_skills/git-create-pr/SKILL.md) | Skill | When asked to create or open a PR |
| 👀 [git-review-pr/SKILL.md](../../src/claude/skills/_git_skills/git-review-pr/SKILL.md) | Skill | When asked to review a GitHub PR |

</details>

## ✏️ Writing and docs

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| ✏️ [claude_writing_style.md](../../src/claude/rules/always_on/02_preferences/claude_writing_style.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| 📝 [claude_output_format.md](../../src/claude/rules/always_on/02_preferences/claude_output_format.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| 🇬🇧 [house_style_team_conventions.md](../../src/claude/rules/always_on/01_standards/house_style_team_conventions.md) | Always-on rule | Every session |
| 🧱 [claude_markdown_style.md](../../src/claude/rules/on_demand/02_preferences/claude_markdown_style.md) | On-demand rule | Before writing or restructuring a markdown doc |
| 👥 [audience_and_depth.md](../../src/claude/rules/on_demand/01_standards/conduct/audience_and_depth.md) | On-demand rule | Before writing for people outside the repo, such as a Confluence page, ticket or email |
| 👥 [audience_and_depth_team_conventions.md](../../src/claude/rules/on_demand/01_standards/conduct/audience_and_depth_team_conventions.md) | On-demand rule | Before setting a page's depth for this team's audiences |
| 🎟️ [jira-create-issue/SKILL.md](../../src/claude/skills/_atlassian_skills/jira-create-issue/SKILL.md) | Skill | When asked to create a Jira ticket |
| 📄 [confluence-create-page/SKILL.md](../../src/claude/skills/_atlassian_skills/confluence-create-page/SKILL.md) | Skill | When asked to create a Confluence page |
| 🖋️ [technical-writer/AGENT.md](../../src/claude/agents/core/technical-writer/AGENT.md) | Agent | When drafting a PR body or new Confluence page |

</details>

## 📛 Naming

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 📛 [naming_standards.md](../../src/claude/rules/always_on/01_standards/naming_standards.md) | Always-on rule | Every session |
| 📅 [datetime.md](../../src/claude/rules/on_demand/style_guides/utilities/datetime.md) | On-demand rule | When writing a date or time into a name, code or log |
| 📅 [datetime_team_conventions.md](../../src/claude/rules/on_demand/style_guides/utilities/datetime_team_conventions.md) | On-demand rule | Before writing a date into a filename or human-facing document |

</details>
