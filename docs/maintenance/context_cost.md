<!-- version: 1.0.39 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-09 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **Path-scoped rules:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~544 |
| 2 | `rules/01_standards/claude_response_standards.md` | ~219 |
| 3 | `rules/01_standards/naming_standards.md` | ~292 |
| 4 | `rules/02_conduct/behaviour.md` | ~356 |
| 5 | `rules/02_conduct/security.md` | ~205 |
| 6 | `rules/02_conduct/writing_style.md` | ~340 |
| 7 | `rules/03_workflows/claude_plans.md` | ~161 |
| | **Subtotal** | **~2120** |

## 📂 Path-scoped rules

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/_path_scoped_rules/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~196 |
| 2 | `rules/_path_scoped_rules/style_guides/airflow.md` | `**/dags/**/*.py` | ~1105 |
| 3 | `rules/_path_scoped_rules/style_guides/bash.md` | `**/*.sh` | ~629 |
| 4 | `rules/_path_scoped_rules/style_guides/dbt.md` | `**/models/**/*.sql`, `**/dbt_project.yml` | ~1115 |
| 5 | `rules/_path_scoped_rules/style_guides/infra/ansible.md` | `**/playbooks/**/*.yml`, `**/roles/**/*.yml` | ~909 |
| 6 | `rules/_path_scoped_rules/style_guides/infra/docker.md` | `**/Dockerfile*` | ~143 |
| 7 | `rules/_path_scoped_rules/style_guides/infra/terraform.md` | `**/*.tf` | ~479 |
| 8 | `rules/_path_scoped_rules/style_guides/python.md` | `**/*.py` | ~1115 |
| 9 | `rules/_path_scoped_rules/style_guides/sql.md` | `**/*.sql` | ~751 |
| 10 | `rules/_path_scoped_rules/style_guides/utilities/makefile.md` | `**/Makefile`, `**/*.mk` | ~247 |
| 11 | `rules/_path_scoped_rules/style_guides/utilities/mermaid.md` | `**/*.mmd` | ~198 |
| 12 | `rules/_path_scoped_rules/testing.md` | `**/*.py`, `**/*.sh`, `**/*.sql` | ~216 |
| | **Subtotal** | | **~7106** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `README.md` | ~475 |
| 2 | `_templates/README.md` | ~869 |
| 3 | `rules/_rules_on_demand/02_conduct/automation_controls.md` | ~719 |
| 4 | `rules/_rules_on_demand/02_conduct/reporting.md` | ~165 |
| 5 | `rules/_rules_on_demand/02_conduct/todo_logging.md` | ~179 |
| 6 | `rules/_rules_on_demand/02_conduct/writing_style/_audience_and_depth.md` | ~324 |
| 7 | `rules/_rules_on_demand/02_conduct/writing_style/_drafts_and_errors.md` | ~199 |
| 8 | `rules/_rules_on_demand/02_conduct/writing_style/_markdown_layout.md` | ~264 |
| 9 | `rules/_rules_on_demand/03_workflows/git.md` | ~325 |
| 10 | `rules/_rules_on_demand/03_workflows/saving_plans.md` | ~170 |
| 11 | `rules/_rules_on_demand/claude_config/authoring_guidelines.md` | ~552 |
| 12 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md` | ~410 |
| 13 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md` | ~560 |
| 14 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_skills.md` | ~474 |
| 15 | `rules/_rules_on_demand/claude_config/claude_naming_patterns.md` | ~224 |
| 16 | `rules/_rules_on_demand/claude_config/guiding_principles.md` | ~447 |
| 17 | `rules/_rules_on_demand/claude_config/permission_recommendations.md` | ~154 |
| 18 | `rules/_rules_on_demand/claude_config/portable_paths.md` | ~190 |
| 19 | `rules/_rules_on_demand/claude_config/turn_budgets.md` | ~174 |
| 20 | `rules/_rules_on_demand/style_guides/airflow/_best_practices.md` | ~1071 |
| 21 | `rules/_rules_on_demand/style_guides/airflow/_dag_configuration.md` | ~609 |
| 22 | `rules/_rules_on_demand/style_guides/airflow/_dag_design.md` | ~876 |
| 23 | `rules/_rules_on_demand/style_guides/airflow/_tasks_and_operators.md` | ~1077 |
| 24 | `rules/_rules_on_demand/style_guides/dbt/_macros.md` | ~779 |
| 25 | `rules/_rules_on_demand/style_guides/dbt/_model_organisation.md` | ~1034 |
| 26 | `rules/_rules_on_demand/style_guides/dbt/_naming_conventions.md` | ~969 |
| 27 | `rules/_rules_on_demand/style_guides/dbt/_snapshots.md` | ~523 |
| 28 | `rules/_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md` | ~558 |
| 29 | `rules/_rules_on_demand/style_guides/infra/ansible/_playbooks.md` | ~679 |
| 30 | `rules/_rules_on_demand/style_guides/infra/ansible/_roles_and_tasks.md` | ~1036 |
| 31 | `rules/_rules_on_demand/style_guides/infra/ansible/_variables.md` | ~795 |
| 32 | `rules/_rules_on_demand/style_guides/infra/docker/_advanced.md` | ~768 |
| 33 | `rules/_rules_on_demand/style_guides/infra/docker/_fundamentals.md` | ~444 |
| 34 | `rules/_rules_on_demand/style_guides/infra/terraform/_ci_and_tooling.md` | ~603 |
| 35 | `rules/_rules_on_demand/style_guides/infra/terraform/_conventions.md` | ~571 |
| 36 | `rules/_rules_on_demand/style_guides/infra/terraform/_declarations.md` | ~609 |
| 37 | `rules/_rules_on_demand/style_guides/infra/terraform/_modules.md` | ~740 |
| 38 | `rules/_rules_on_demand/style_guides/infra/terraform/_providers.md` | ~535 |
| 39 | `rules/_rules_on_demand/style_guides/infra/terraform/_structure.md` | ~613 |
| 40 | `rules/_rules_on_demand/style_guides/jira.md` | ~393 |
| 41 | `rules/_rules_on_demand/style_guides/jira/_business_value.md` | ~898 |
| 42 | `rules/_rules_on_demand/style_guides/jira/_definition_of_ready.md` | ~272 |
| 43 | `rules/_rules_on_demand/style_guides/jira/_field_standards.md` | ~662 |
| 44 | `rules/_rules_on_demand/style_guides/jira/_jira_values_template.md` | ~359 |
| 45 | `rules/_rules_on_demand/style_guides/jira/_sprint_planning.md` | ~586 |
| 46 | `rules/_rules_on_demand/style_guides/jira/_ticket_conventions.md` | ~573 |
| 47 | `rules/_rules_on_demand/style_guides/python/_comments.md` | ~258 |
| 48 | `rules/_rules_on_demand/style_guides/python/_python_environment.md` | ~479 |
| 49 | `rules/_rules_on_demand/style_guides/python/code_complexity.md` | ~890 |
| 50 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md` | ~331 |
| 51 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md` | ~332 |
| 52 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_size_limits.md` | ~575 |
| 53 | `rules/_rules_on_demand/style_guides/python/logging.md` | ~509 |
| 54 | `rules/_rules_on_demand/style_guides/python/logging/_error_anti_patterns.md` | ~639 |
| 55 | `rules/_rules_on_demand/style_guides/python/logging/_error_handling.md` | ~669 |
| 56 | `rules/_rules_on_demand/style_guides/python/logging/_setup_and_levels.md` | ~854 |
| 57 | `rules/_rules_on_demand/style_guides/python/logging/_what_not_to_log.md` | ~704 |
| 58 | `rules/_rules_on_demand/style_guides/python/logging/_what_to_log.md` | ~417 |
| 59 | `rules/_rules_on_demand/style_guides/python/module_organisation.md` | ~500 |
| 60 | `rules/_rules_on_demand/style_guides/python/module_organisation/_constants.md` | ~376 |
| 61 | `rules/_rules_on_demand/style_guides/python/module_organisation/_docstrings.md` | ~578 |
| 62 | `rules/_rules_on_demand/style_guides/python/module_organisation/_metadata_and_ordering.md` | ~417 |
| 63 | `rules/_rules_on_demand/style_guides/python/module_organisation/_public_private.md` | ~590 |
| 64 | `rules/_rules_on_demand/style_guides/python/testing.md` | ~468 |
| 65 | `rules/_rules_on_demand/style_guides/python/testing/_assertions.md` | ~500 |
| 66 | `rules/_rules_on_demand/style_guides/python/testing/_fixtures_mocking.md` | ~745 |
| 67 | `rules/_rules_on_demand/style_guides/python/testing/_naming_structure.md` | ~593 |
| 68 | `rules/_rules_on_demand/style_guides/sql/_cte_style_guide.md` | ~523 |
| 69 | `rules/_rules_on_demand/style_guides/sql/_formatting.md` | ~930 |
| 70 | `rules/_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md` | ~481 |
| 71 | `rules/_rules_on_demand/style_guides/sql/_sqlfluff.md` | ~388 |
| 72 | `rules/_rules_on_demand/style_guides/utilities/datetime.md` | ~464 |
| 73 | `rules/_rules_on_demand/style_guides/utilities/makefile/_naming_conventions.md` | ~142 |
| 74 | `rules/_rules_on_demand/style_guides/utilities/makefile/_variables_operators_and_commands.md` | ~529 |
| 75 | `rules/_rules_on_demand/style_guides/utilities/mermaid/_advanced.md` | ~542 |
| 76 | `rules/_rules_on_demand/style_guides/utilities/mermaid/_fundamentals.md` | ~414 |
| 77 | `rules/_rules_on_demand/testing/_testing_anti_patterns.md` | ~692 |
| 78 | `rules/_rules_on_demand/testing/_testing_design_pattern.md` | ~473 |
| | **Subtotal** | **~42541** |
