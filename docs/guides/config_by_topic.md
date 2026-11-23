# 🗺️ Config by topic

**Purpose:** every Claude config file for one topic, such as security, and when each loads, so you needn't search `always_on/`, `path_scoped/`, `on_demand/`, skills, agents and hooks separately.

This page sits in `docs/`, so it's never installed. It lists parent files only, since each parent links its own `_` child files, except where a child holds a topic's main content. A test fails when a parent file is missing from the map.

## 🔐 Security

| File | Kind | When it loads |
|---|---|---|
| 🔐 [security.md](../../src/claude/rules/always_on/01_standards/security.md) | Always-on rule | Every session |
| 🛡️ [code_security.md](../../src/claude/rules/path_scoped/01_standards/code_security.md) | Path-scoped rule | Reading `.py`, `.sh`, `.sql`, `.tf` or `.tfvars` files |
| 🔑 [permission_recommendations.md](../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md) | On-demand rule | Before recommending a permission or allowlist change |
| 🐙 [github_actions/_security_hardening.md](../../src/claude/rules/on_demand/style_guides/cicd/github_actions/_security_hardening.md) | On-demand child | Before adding a secret, deploy job, `pull_request_target` trigger or third-party action |
| 🔷 [azure_devops/_security_hardening.md](../../src/claude/rules/on_demand/style_guides/cicd/azure_devops/_security_hardening.md) | On-demand child | Before adding a secret, service connection, deploy stage or third-party task |
| 🐳 [docker/_advanced.md](../../src/claude/rules/on_demand/style_guides/infra/docker/_advanced.md#-security) | On-demand child | When hardening an image, in its Security section |
| 🔍 [code-reviewer/AGENT.md](../../src/claude/agents/core/code-reviewer/AGENT.md) | Agent | When asked to review or score a local diff |

## 🧪 Testing

| File | Kind | When it loads |
|---|---|---|
| 🧪 [path_scoped/01_standards/testing.md](../../src/claude/rules/path_scoped/01_standards/testing.md) | Path-scoped rule | Reading `.py`, `.sh` or dbt model `.sql` files |
| 📋 [on_demand/01_standards/testing.md](../../src/claude/rules/on_demand/01_standards/testing.md) | On-demand rule | Before writing or reviewing a test |
| 🐍 [python/testing.md](../../src/claude/rules/on_demand/style_guides/python/testing.md) | On-demand rule | Before writing or changing pytest tests |

## 🌿 Git and PRs

| File | Kind | When it loads |
|---|---|---|
| 🌿 [git.md](../../src/claude/rules/on_demand/01_standards/git.md) | On-demand rule | Before any git command, or when the worktree hook blocks an edit |
| 📤 [git-create-pr/SKILL.md](../../src/claude/skills/_git_skills/git-create-pr/SKILL.md) | Skill | When asked to create or open a PR |
| 👀 [git-review-pr/SKILL.md](../../src/claude/skills/_git_skills/git-review-pr/SKILL.md) | Skill | When asked to review a GitHub PR |

## ✏️ Writing and docs

| File | Kind | When it loads |
|---|---|---|
| ✏️ [claude_writing_style.md](../../src/claude/rules/always_on/02_preferences/claude_writing_style.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| 📝 [claude_output_format.md](../../src/claude/rules/always_on/02_preferences/claude_output_format.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| 🇬🇧 [house_style_team_conventions.md](../../src/claude/rules/always_on/01_standards/house_style_team_conventions.md) | Always-on rule | Every session |
| 🧱 [claude_markdown_style.md](../../src/claude/rules/on_demand/02_preferences/claude_markdown_style.md) | On-demand rule | Before writing or restructuring a markdown doc |
| 👥 [audience_and_depth.md](../../src/claude/rules/on_demand/01_standards/conduct/audience_and_depth.md) | On-demand rule | Before writing for people outside the repo, such as a Confluence page, ticket or email |
| 👥 [audience_and_depth_team_conventions.md](../../src/claude/rules/on_demand/01_standards/conduct/audience_and_depth_team_conventions.md) | On-demand rule | Before setting a page's depth for this team's audiences |
| 🎫 [jira.md](../../src/claude/rules/on_demand/style_guides/jira.md) | On-demand rule | Before writing or changing a Jira ticket |
| 🎫 [jira_team_conventions.md](../../src/claude/rules/on_demand/style_guides/jira/jira_team_conventions.md) | On-demand rule | Before drafting a ticket, for this team's format, fields and sprints |
| 🎟️ [jira-create-issue/SKILL.md](../../src/claude/skills/_atlassian_skills/jira-create-issue/SKILL.md) | Skill | When asked to create a Jira ticket |
| 📄 [confluence-create-page/SKILL.md](../../src/claude/skills/_atlassian_skills/confluence-create-page/SKILL.md) | Skill | When asked to create a Confluence page |
| 🖋️ [technical-writer/AGENT.md](../../src/claude/agents/core/technical-writer/AGENT.md) | Agent | When drafting a PR body or new Confluence page |

## 🔄 Workflow and planning

| File | Kind | When it loads |
|---|---|---|
| 🔄 [ai_sdlc_workflow.md](../../src/claude/rules/always_on/01_standards/ai_sdlc_workflow.md) | Always-on rule | Every session |
| 🛡️ [behaviour.md](../../src/claude/rules/always_on/01_standards/behaviour.md) | Always-on rule | Every session |
| 🗂️ [claude_working_files.md](../../src/claude/rules/always_on/02_preferences/claude_working_files.md) | Always-on rule | Every session, unless installed with `PREFERENCES=0` |
| ✅ [reporting.md](../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | On-demand rule | Before saying a task is done |
| 🤖 [automation_controls.md](../../src/claude/rules/on_demand/01_standards/conduct/automation_controls.md) | On-demand rule | Before proposing or starting a loop or other unattended run |
| ⏱️ [turn_budgets.md](../../src/claude/rules/on_demand/01_standards/claude_config/turn_budgets.md) | On-demand rule | When setting turn caps for `claude -p` or another unattended run |
| 🗂️ [hook_enforcement_plan_sections.sh](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | Hook | On `ExitPlanMode`, blocking a long plan with no Intent or Spec heading |
| ✅ [hook_enforcement_done_checks.sh](../../src/claude/hooks/hook_enforcement_done_checks.sh) | Hook | On stop, sending Claude back once to run the done checks |
| 🌳 [hook_enforcement_worktree_edits.sh](../../src/claude/hooks/hook_enforcement_worktree_edits.sh) | Hook | On a session's first edit in a repo's main folder |
| 🔁 [hook_reminder_kaizen_due.sh](../../src/claude/hooks/hook_reminder_kaizen_due.sh) | Hook | On session start, once 5 or more feedback notes are new |
| 🔁 [claude-kaizen/SKILL.md](../../src/claude/skills/_claude_skills/claude-kaizen/SKILL.md) | Skill | On `/claude-kaizen`, or when the kaizen reminder suggests it |
| 📜 [claude-capture-session-prompts/SKILL.md](../../src/claude/skills/_claude_skills/claude-capture-session-prompts/SKILL.md) | Skill | When asked to capture or audit a day's session prompts |

## 📛 Naming

| File | Kind | When it loads |
|---|---|---|
| 📛 [naming_standards.md](../../src/claude/rules/always_on/01_standards/naming_standards.md) | Always-on rule | Every session |
| 📅 [datetime.md](../../src/claude/rules/on_demand/style_guides/utilities/datetime.md) | On-demand rule | When writing a date or time into a name, code or log |
| 📅 [datetime_team_conventions.md](../../src/claude/rules/on_demand/style_guides/utilities/datetime_team_conventions.md) | On-demand rule | Before writing a date into a filename or human-facing document |

## 🧠 Claude config authoring

| File | Kind | When it loads |
|---|---|---|
| 🧭 [guiding_principles.md](../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | On-demand rule | Before proposing a rule, skill, hook, import, setting or memory note |
| 🏷️ [claude_naming_patterns.md](../../src/claude/rules/on_demand/01_standards/claude_config/claude_naming_patterns.md) | On-demand rule | Before naming a new rule, skill or agent |
| 🔑 [permission_recommendations.md](../../src/claude/rules/on_demand/01_standards/claude_config/permission_recommendations.md) | On-demand rule | Before recommending a permission or allowlist change |

## 🧰 Language style guides

Each language row links its style guide and the team's conventions, which load on the same paths.

| File | Kind | When it loads |
|---|---|---|
| 🌬️ [airflow.md](../../src/claude/rules/path_scoped/style_guides/airflow.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/airflow_team_conventions.md) | Path-scoped rule | Reading `dags/` Python files |
| 🔷 [azure_devops.md](../../src/claude/rules/path_scoped/style_guides/cicd/azure_devops.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/cicd/azure_devops_team_conventions.md) | Path-scoped rule | Reading Azure pipeline YAML files |
| 🐚 [bash.md](../../src/claude/rules/path_scoped/style_guides/bash.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/bash_team_conventions.md) | Path-scoped rule | Reading `.sh` files |
| 🧱 [dbt.md](../../src/claude/rules/path_scoped/style_guides/dbt.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/dbt_team_conventions.md) | Path-scoped rule | Reading dbt models or `dbt_project.yml` |
| 🐙 [github_actions.md](../../src/claude/rules/path_scoped/style_guides/cicd/github_actions.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/cicd/github_actions_team_conventions.md) | Path-scoped rule | Reading `.github/workflows/` YAML files |
| 📦 [ansible.md](../../src/claude/rules/path_scoped/style_guides/infra/ansible.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/infra/ansible_team_conventions.md) | Path-scoped rule | Reading `playbooks/` or `roles/` YAML files |
| 🐳 [docker.md](../../src/claude/rules/path_scoped/style_guides/infra/docker.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/infra/docker_team_conventions.md) | Path-scoped rule | Reading a `Dockerfile` |
| 🌍 [terraform.md](../../src/claude/rules/path_scoped/style_guides/infra/terraform.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/infra/terraform_team_conventions.md) | Path-scoped rule | Reading `.tf` files |
| 🐍 [python.md](../../src/claude/rules/path_scoped/style_guides/python.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/python_team_conventions.md) | Path-scoped rule | Reading `.py` files |
| 🐍 [python/code_complexity.md](../../src/claude/rules/on_demand/style_guides/python/code_complexity.md) | On-demand rule | When a Python function grows long or deeply nested |
| 🐍 [python/logging.md](../../src/claude/rules/on_demand/style_guides/python/logging.md) | On-demand rule | Before adding Python logging or error handling |
| 🐍 [python/module_organisation.md](../../src/claude/rules/on_demand/style_guides/python/module_organisation.md) | On-demand rule | When writing docstrings or splitting public and private code |
| 🗄️ [sql.md](../../src/claude/rules/path_scoped/style_guides/sql.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/sql_team_conventions.md) | Path-scoped rule | Reading `.sql` files |
| ❄️ [sql/snowflake.md](../../src/claude/rules/on_demand/style_guides/sql/snowflake.md) | On-demand rule | When sizing a warehouse, setting `AUTO_SUSPEND` or fixing a SQLFluff failure |
| 🛠️ [makefile.md](../../src/claude/rules/path_scoped/style_guides/utilities/makefile.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/utilities/makefile_team_conventions.md) | Path-scoped rule | Reading a `Makefile` or `.mk` file |
| 🧜 [mermaid.md](../../src/claude/rules/path_scoped/style_guides/utilities/mermaid.md), [team conventions](../../src/claude/rules/path_scoped/style_guides/utilities/mermaid_team_conventions.md) | Path-scoped rule | Reading `.mmd` files |
| 🧜 [mermaid_styling_team_conventions.md](../../src/claude/rules/on_demand/style_guides/utilities/mermaid_styling_team_conventions.md) | On-demand rule | When choosing Mermaid node shapes, text or styling |
