<!-- version: 1.0.27 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-07 -->
# 💰 Context cost

**Purpose:** how many tokens each file in the global Claude config adds, and when it loads, estimated as characters ÷ 4, leaving out HTML comments, which Claude Code strips.

This page belongs to the repo's maintenance records. `make context_cost` writes it from `src/claude/`, and a pre-commit check fails if it's out of date, so don't edit the tables by hand.

- 🔒 **Every session:** counts towards the [always-on budget](../target_architecture/target_architecture.md#-always-on-budget), which also counts this repo's own `CLAUDE.md`.
- 📂 **With matching files:** loads only once Claude opens a file that matches one of its globs.
- 💤 **On demand:** loads only when Claude follows a pointer to it.

## 🔒 Every session

| # | File | Tokens |
|---|---|---|
| 1 | `CLAUDE.md` | ~546 |
| 2 | `rules/01_standards/claude_response_standards.md` | ~218 |
| 3 | `rules/01_standards/naming_standards.md` | ~233 |
| 4 | `rules/02_conduct/behaviour.md` | ~446 |
| 5 | `rules/02_conduct/security.md` | ~204 |
| 6 | `rules/02_conduct/writing_style.md` | ~340 |
| 7 | `rules/03_workflows/claude_plans.md` | ~160 |
| 8 | `rules/03_workflows/git.md` | ~325 |
| | **Subtotal** | **~2474** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/_path_scoped_rules/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| 2 | `rules/_path_scoped_rules/style_guides/airflow.md` | `**/dags/**/*.py` | ~1105 |
| 3 | `rules/_path_scoped_rules/style_guides/bash.md` | `**/*.sh` | ~628 |
| 4 | `rules/_path_scoped_rules/style_guides/dbt.md` | `**/models/**/*.sql`, `**/dbt_project.yml` | ~1114 |
| 5 | `rules/_path_scoped_rules/style_guides/infra/ansible.md` | `**/playbooks/**/*.yml`, `**/roles/**/*.yml` | ~908 |
| 6 | `rules/_path_scoped_rules/style_guides/infra/docker.md` | `**/Dockerfile*` | ~142 |
| 7 | `rules/_path_scoped_rules/style_guides/infra/terraform.md` | `**/*.tf` | ~478 |
| 8 | `rules/_path_scoped_rules/style_guides/python.md` | `**/*.py` | ~1114 |
| 9 | `rules/_path_scoped_rules/style_guides/sql.md` | `**/*.sql` | ~750 |
| 10 | `rules/_path_scoped_rules/style_guides/utilities/makefile.md` | `**/Makefile`, `**/*.mk` | ~247 |
| 11 | `rules/_path_scoped_rules/style_guides/utilities/mermaid.md` | `**/*.mmd` | ~198 |
| 12 | `rules/_path_scoped_rules/testing.md` | `**/*.py`, `**/*.sh`, `**/*.sql` | ~215 |
| | **Subtotal** | | **~7097** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `_templates/README.md` | ~1188 |
| 2 | `_templates/skills/_quality_scorecard_template.md` | ~1258 |
| 3 | `rules/_rules_on_demand/02_conduct/automation_controls.md` | ~719 |
| 4 | `rules/_rules_on_demand/02_conduct/todo_logging.md` | ~178 |
| 5 | `rules/_rules_on_demand/02_conduct/writing_style/_audience_and_depth.md` | ~324 |
| 6 | `rules/_rules_on_demand/02_conduct/writing_style/_drafts_and_errors.md` | ~199 |
| 7 | `rules/_rules_on_demand/02_conduct/writing_style/_markdown_layout.md` | ~264 |
| 8 | `rules/_rules_on_demand/03_workflows/saving_plans.md` | ~169 |
| 9 | `rules/_rules_on_demand/claude_config/authoring_guidelines.md` | ~552 |
| 10 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_agents.md` | ~360 |
| 11 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md` | ~561 |
| 12 | `rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_skills.md` | ~433 |
| 13 | `rules/_rules_on_demand/claude_config/claude_naming_patterns.md` | ~198 |
| 14 | `rules/_rules_on_demand/claude_config/guiding_principles.md` | ~447 |
| 15 | `rules/_rules_on_demand/claude_config/permission_recommendations.md` | ~154 |
| 16 | `rules/_rules_on_demand/claude_config/portable_paths.md` | ~190 |
| 17 | `rules/_rules_on_demand/claude_config/turn_budgets.md` | ~174 |
| 18 | `rules/_rules_on_demand/style_guides/airflow/_best_practices.md` | ~1071 |
| 19 | `rules/_rules_on_demand/style_guides/airflow/_dag_configuration.md` | ~609 |
| 20 | `rules/_rules_on_demand/style_guides/airflow/_dag_design.md` | ~876 |
| 21 | `rules/_rules_on_demand/style_guides/airflow/_tasks_and_operators.md` | ~1077 |
| 22 | `rules/_rules_on_demand/style_guides/dbt/_macros.md` | ~779 |
| 23 | `rules/_rules_on_demand/style_guides/dbt/_model_organisation.md` | ~1034 |
| 24 | `rules/_rules_on_demand/style_guides/dbt/_naming_conventions.md` | ~969 |
| 25 | `rules/_rules_on_demand/style_guides/dbt/_snapshots.md` | ~523 |
| 26 | `rules/_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md` | ~558 |
| 27 | `rules/_rules_on_demand/style_guides/infra/ansible/_playbooks.md` | ~679 |
| 28 | `rules/_rules_on_demand/style_guides/infra/ansible/_roles_and_tasks.md` | ~1024 |
| 29 | `rules/_rules_on_demand/style_guides/infra/ansible/_variables.md` | ~795 |
| 30 | `rules/_rules_on_demand/style_guides/infra/docker/_advanced.md` | ~768 |
| 31 | `rules/_rules_on_demand/style_guides/infra/docker/_fundamentals.md` | ~444 |
| 32 | `rules/_rules_on_demand/style_guides/infra/terraform/_ci_and_tooling.md` | ~603 |
| 33 | `rules/_rules_on_demand/style_guides/infra/terraform/_conventions.md` | ~571 |
| 34 | `rules/_rules_on_demand/style_guides/infra/terraform/_declarations.md` | ~609 |
| 35 | `rules/_rules_on_demand/style_guides/infra/terraform/_modules.md` | ~740 |
| 36 | `rules/_rules_on_demand/style_guides/infra/terraform/_providers.md` | ~535 |
| 37 | `rules/_rules_on_demand/style_guides/infra/terraform/_structure.md` | ~613 |
| 38 | `rules/_rules_on_demand/style_guides/jira.md` | ~393 |
| 39 | `rules/_rules_on_demand/style_guides/jira/_business_value.md` | ~898 |
| 40 | `rules/_rules_on_demand/style_guides/jira/_definition_of_ready.md` | ~272 |
| 41 | `rules/_rules_on_demand/style_guides/jira/_field_standards.md` | ~662 |
| 42 | `rules/_rules_on_demand/style_guides/jira/_jira_values_template.md` | ~359 |
| 43 | `rules/_rules_on_demand/style_guides/jira/_sprint_planning.md` | ~586 |
| 44 | `rules/_rules_on_demand/style_guides/jira/_ticket_conventions.md` | ~573 |
| 45 | `rules/_rules_on_demand/style_guides/python/_comments.md` | ~258 |
| 46 | `rules/_rules_on_demand/style_guides/python/_python_environment.md` | ~479 |
| 47 | `rules/_rules_on_demand/style_guides/python/code_complexity.md` | ~836 |
| 48 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md` | ~331 |
| 49 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md` | ~748 |
| 50 | `rules/_rules_on_demand/style_guides/python/logging.md` | ~436 |
| 51 | `rules/_rules_on_demand/style_guides/python/logging/_error_handling.md` | ~1177 |
| 52 | `rules/_rules_on_demand/style_guides/python/logging/_setup_and_levels.md` | ~854 |
| 53 | `rules/_rules_on_demand/style_guides/python/logging/_what_to_log.md` | ~1100 |
| 54 | `rules/_rules_on_demand/style_guides/python/module_organisation.md` | ~407 |
| 55 | `rules/_rules_on_demand/style_guides/python/module_organisation/_docstrings.md` | ~1171 |
| 56 | `rules/_rules_on_demand/style_guides/python/module_organisation/_public_private.md` | ~947 |
| 57 | `rules/_rules_on_demand/style_guides/python/testing.md` | ~467 |
| 58 | `rules/_rules_on_demand/style_guides/python/testing/_assertions.md` | ~716 |
| 59 | `rules/_rules_on_demand/style_guides/python/testing/_fixtures_mocking.md` | ~815 |
| 60 | `rules/_rules_on_demand/style_guides/python/testing/_naming_structure.md` | ~396 |
| 61 | `rules/_rules_on_demand/style_guides/sql/_cte_style_guide.md` | ~523 |
| 62 | `rules/_rules_on_demand/style_guides/sql/_formatting.md` | ~929 |
| 63 | `rules/_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md` | ~481 |
| 64 | `rules/_rules_on_demand/style_guides/sql/_sqlfluff.md` | ~388 |
| 65 | `rules/_rules_on_demand/style_guides/utilities/datetime.md` | ~464 |
| 66 | `rules/_rules_on_demand/style_guides/utilities/makefile/_naming_conventions.md` | ~142 |
| 67 | `rules/_rules_on_demand/style_guides/utilities/makefile/_variables_operators_and_commands.md` | ~529 |
| 68 | `rules/_rules_on_demand/style_guides/utilities/mermaid/_advanced.md` | ~542 |
| 69 | `rules/_rules_on_demand/style_guides/utilities/mermaid/_fundamentals.md` | ~414 |
| 70 | `rules/_rules_on_demand/testing/_testing_anti_patterns.md` | ~692 |
| 71 | `rules/_rules_on_demand/testing/_testing_design_pattern.md` | ~472 |
| | **Subtotal** | **~42729** |
