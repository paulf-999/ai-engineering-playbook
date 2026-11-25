# 🗺️ Rules by topic

**Purpose:** every rule for one topic, such as security, and when each loads, so you needn't search `always_on/`, `path_scoped/` and `on_demand/` separately.

This page sits in `docs/`, so it's never installed. It lists parent files only, since each parent links its own `_` child files. A test fails when a parent rule is missing from the map, except the style guides.

## 🔄 Workflow and planning

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🔄 [ai_sdlc_workflow.md](../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | Always-on rule | Every session |
| 🪜 [ai_sdlc_stages.md](../../src/claude/rules/on_demand/01_standards/ai_sdlc_stages.md) | On-demand rule | Before work on an SDLC stage |
| 🛡️ [behaviour.md](../../src/claude/rules/always_on/01_standards/behaviour.md) | Always-on rule | Every session |
| 📤 [claude_saved_plans.md](../../src/claude/rules/on_demand/02_preferences/claude_saved_plans.md) | On-demand rule | When writing a plan |
| 🗂️ [claude_working_files.md](../../src/claude/rules/always_on/02_preferences/claude_working_files.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| ✅ [claude_task_reporting.md](../../src/claude/rules/on_demand/01_standards/conduct/claude_task_reporting.md) | On-demand rule | Before saying a task is done |
| 🤖 [claude_loops_and_batches.md](../../src/claude/rules/on_demand/01_standards/conduct/claude_loops_and_batches.md) | On-demand rule | Before proposing or starting a loop or other unattended run |
| ⏱️ [claude_turn_limits.md](../../src/claude/rules/on_demand/01_standards/claude_config/claude_turn_limits.md) | On-demand rule | When setting turn caps for `claude -p` or another unattended run |

</details>

## 🔐 Security

<details>
<summary>Show the files</summary>

| File | Kind | When it loads |
|---|---|---|
| 🔐 [security.md](../../src/claude/rules/always_on/01_standards/security.md) | Always-on rule | Every session |
| 🛡️ [code_security.md](../../src/claude/rules/path_scoped/01_standards/code_security.md) | Path-scoped rule | Reading `.py`, `.sh`, `.sql`, `.tf` or `.tfvars` files |
| 🔑 [permission_recommendations.md](../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md) | On-demand rule | Before recommending a permission or allowlist change |

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
| 🔍 [claude_pr_review.md](../../src/claude/rules/always_on/02_preferences/claude_pr_review.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| 🔁 [claude_pr_review_loop.md](../../src/claude/rules/on_demand/02_preferences/claude_pr_review_loop.md) | On-demand rule | Before running `git-create-pr` |

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
