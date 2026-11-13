<!-- version: 1.0.70 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-13 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~535 |
| 2 | `rules/01_standards/claude_response_standards.md` | ~218 |
| 3 | `rules/01_standards/naming_standards.md` | ~247 |
| 4 | `rules/02_conduct/behaviour.md` | ~315 |
| 5 | `rules/02_conduct/security.md` | ~203 |
| 6 | `rules/02_conduct/writing_style.md` | ~313 |
| 7 | `rules/03_workflows/claude_plans.md` | ~177 |
| | **Subtotal** | **~2010** |

## 📂 Path-scoped rules

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/path_scoped/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| 2 | `rules/path_scoped/style_guides/airflow.md` | `**/dags/**/*.py` | ~321 |
| 3 | `rules/path_scoped/style_guides/bash.md` | `**/*.sh` | ~352 |
| 4 | `rules/path_scoped/style_guides/dbt.md` | `**/models/**/*.sql`, `**/models/**/*.yml`, `**/dbt_project.yml` | ~405 |
| 5 | `rules/path_scoped/style_guides/infra/ansible.md` | `**/playbooks/**/*.yml`, `**/roles/**/*.yml` | ~459 |
| 6 | `rules/path_scoped/style_guides/infra/docker.md` | `**/Dockerfile*` | ~129 |
| 7 | `rules/path_scoped/style_guides/infra/terraform.md` | `**/*.tf` | ~438 |
| 8 | `rules/path_scoped/style_guides/python.md` | `**/*.py` | ~419 |
| 9 | `rules/path_scoped/style_guides/sql.md` | `**/*.sql` | ~316 |
| 10 | `rules/path_scoped/style_guides/utilities/makefile.md` | `**/Makefile`, `**/*.mk` | ~233 |
| 11 | `rules/path_scoped/style_guides/utilities/mermaid.md` | `**/*.mmd` | ~184 |
| 12 | `rules/path_scoped/testing.md` | `**/*.py`, `**/*.sh`, `**/*.sql` | ~202 |
| | **Subtotal** | | **~3657** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `README.md` | ~524 |
| 2 | `_templates/README.md` | ~786 |
| 3 | `rules/on_demand/02_conduct/automation_controls.md` | ~717 |
| 4 | `rules/on_demand/02_conduct/reporting.md` | ~174 |
| 5 | `rules/on_demand/02_conduct/todo_logging.md` | ~179 |
| 6 | `rules/on_demand/02_conduct/writing_style/_audience_and_depth.md` | ~324 |
| 7 | `rules/on_demand/02_conduct/writing_style/_drafts_and_errors.md` | ~199 |
| 8 | `rules/on_demand/02_conduct/writing_style/_markdown_layout.md` | ~264 |
| 9 | `rules/on_demand/03_workflows/git.md` | ~325 |
| 10 | `rules/on_demand/03_workflows/saving_plans.md` | ~235 |
| 11 | `rules/on_demand/03_workflows/sdlc_workflow.md` | ~255 |
| 12 | `rules/on_demand/claude_config/authoring_guidelines.md` | ~367 |
| 13 | `rules/on_demand/claude_config/authoring_guidelines/_authoring_agents.md` | ~408 |
| 14 | `rules/on_demand/claude_config/authoring_guidelines/_authoring_rules.md` | ~507 |
| 15 | `rules/on_demand/claude_config/authoring_guidelines/_authoring_skills.md` | ~472 |
| 16 | `rules/on_demand/claude_config/claude_naming_patterns.md` | ~185 |
| 17 | `rules/on_demand/claude_config/guiding_principles.md` | ~397 |
| 18 | `rules/on_demand/claude_config/permission_recommendations.md` | ~182 |
| 19 | `rules/on_demand/claude_config/portable_paths.md` | ~189 |
| 20 | `rules/on_demand/claude_config/turn_budgets.md` | ~174 |
| 21 | `rules/on_demand/style_guides/airflow/_best_practices.md` | ~1071 |
| 22 | `rules/on_demand/style_guides/airflow/_dag_configuration.md` | ~609 |
| 23 | `rules/on_demand/style_guides/airflow/_dag_design.md` | ~876 |
| 24 | `rules/on_demand/style_guides/airflow/_tasks_and_operators.md` | ~1077 |
| 25 | `rules/on_demand/style_guides/dbt/_macros.md` | ~779 |
| 26 | `rules/on_demand/style_guides/dbt/_model_organisation.md` | ~1034 |
| 27 | `rules/on_demand/style_guides/dbt/_naming_conventions.md` | ~969 |
| 28 | `rules/on_demand/style_guides/dbt/_snapshots.md` | ~523 |
| 29 | `rules/on_demand/style_guides/dbt/_yaml_resource_properties.md` | ~558 |
| 30 | `rules/on_demand/style_guides/infra/ansible/_playbooks.md` | ~679 |
| 31 | `rules/on_demand/style_guides/infra/ansible/_repo_structure.md` | ~456 |
| 32 | `rules/on_demand/style_guides/infra/ansible/_roles_and_tasks.md` | ~1036 |
| 33 | `rules/on_demand/style_guides/infra/ansible/_variables.md` | ~795 |
| 34 | `rules/on_demand/style_guides/infra/docker/_advanced.md` | ~768 |
| 35 | `rules/on_demand/style_guides/infra/docker/_fundamentals.md` | ~444 |
| 36 | `rules/on_demand/style_guides/infra/terraform/_ci_and_tooling.md` | ~603 |
| 37 | `rules/on_demand/style_guides/infra/terraform/_conventions.md` | ~571 |
| 38 | `rules/on_demand/style_guides/infra/terraform/_declarations.md` | ~609 |
| 39 | `rules/on_demand/style_guides/infra/terraform/_modules.md` | ~740 |
| 40 | `rules/on_demand/style_guides/infra/terraform/_providers.md` | ~535 |
| 41 | `rules/on_demand/style_guides/infra/terraform/_structure.md` | ~613 |
| 42 | `rules/on_demand/style_guides/jira.md` | ~345 |
| 43 | `rules/on_demand/style_guides/jira/_business_value.md` | ~898 |
| 44 | `rules/on_demand/style_guides/jira/_definition_of_ready.md` | ~272 |
| 45 | `rules/on_demand/style_guides/jira/_field_standards.md` | ~662 |
| 46 | `rules/on_demand/style_guides/jira/_jira_values_template.md` | ~359 |
| 47 | `rules/on_demand/style_guides/jira/_sprint_planning.md` | ~586 |
| 48 | `rules/on_demand/style_guides/jira/_ticket_conventions.md` | ~573 |
| 49 | `rules/on_demand/style_guides/python/_comments.md` | ~258 |
| 50 | `rules/on_demand/style_guides/python/_python_environment.md` | ~478 |
| 51 | `rules/on_demand/style_guides/python/code_complexity.md` | ~372 |
| 52 | `rules/on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md` | ~300 |
| 53 | `rules/on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md` | ~335 |
| 54 | `rules/on_demand/style_guides/python/code_complexity/_code_complexity_size_limits.md` | ~459 |
| 55 | `rules/on_demand/style_guides/python/logging.md` | ~339 |
| 56 | `rules/on_demand/style_guides/python/logging/_error_anti_patterns.md` | ~639 |
| 57 | `rules/on_demand/style_guides/python/logging/_error_handling.md` | ~669 |
| 58 | `rules/on_demand/style_guides/python/logging/_setup_and_levels.md` | ~854 |
| 59 | `rules/on_demand/style_guides/python/logging/_what_not_to_log.md` | ~704 |
| 60 | `rules/on_demand/style_guides/python/logging/_what_to_log.md` | ~417 |
| 61 | `rules/on_demand/style_guides/python/module_organisation.md` | ~372 |
| 62 | `rules/on_demand/style_guides/python/module_organisation/_constants.md` | ~376 |
| 63 | `rules/on_demand/style_guides/python/module_organisation/_docstrings.md` | ~222 |
| 64 | `rules/on_demand/style_guides/python/module_organisation/_metadata_and_ordering.md` | ~417 |
| 65 | `rules/on_demand/style_guides/python/module_organisation/_public_private.md` | ~590 |
| 66 | `rules/on_demand/style_guides/python/testing.md` | ~313 |
| 67 | `rules/on_demand/style_guides/python/testing/_assertions.md` | ~500 |
| 68 | `rules/on_demand/style_guides/python/testing/_fixtures_mocking.md` | ~745 |
| 69 | `rules/on_demand/style_guides/python/testing/_naming_structure.md` | ~593 |
| 70 | `rules/on_demand/style_guides/sql/_cost_guardrails.md` | ~148 |
| 71 | `rules/on_demand/style_guides/sql/_cte_style_guide.md` | ~523 |
| 72 | `rules/on_demand/style_guides/sql/_formatting.md` | ~930 |
| 73 | `rules/on_demand/style_guides/sql/_snowflake_data_type_standards.md` | ~481 |
| 74 | `rules/on_demand/style_guides/sql/_sqlfluff.md` | ~432 |
| 75 | `rules/on_demand/style_guides/utilities/datetime.md` | ~463 |
| 76 | `rules/on_demand/style_guides/utilities/makefile/_naming_conventions.md` | ~142 |
| 77 | `rules/on_demand/style_guides/utilities/makefile/_variables_operators_and_commands.md` | ~529 |
| 78 | `rules/on_demand/style_guides/utilities/mermaid/_advanced.md` | ~542 |
| 79 | `rules/on_demand/style_guides/utilities/mermaid/_fundamentals.md` | ~414 |
| 80 | `rules/on_demand/testing/_testing_anti_patterns.md` | ~692 |
| 81 | `rules/on_demand/testing/_testing_design_pattern.md` | ~473 |
| | **Subtotal** | **~41656** |
