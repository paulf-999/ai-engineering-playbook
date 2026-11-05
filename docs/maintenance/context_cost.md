<!-- version: 1.0.14 -->
<!-- created: 2026-11-04 -->
<!-- updated: 2026-11-05 -->
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
| 2 | `rules/01_ways_of_working/behaviour.md` | ~450 |
| 3 | `rules/01_ways_of_working/claude_plans.md` | ~162 |
| 4 | `rules/01_ways_of_working/git.md` | ~325 |
| 5 | `rules/01_ways_of_working/security.md` | ~204 |
| 6 | `rules/02_communication/claude_response_standards.md` | ~218 |
| 7 | `rules/02_communication/naming_standards.md` | ~197 |
| 8 | `rules/02_communication/writing_style.md` | ~318 |
| | **Subtotal** | **~2422** |

## 📂 With matching files

| # | File | Globs | Tokens |
|---|---|---|---|
| 1 | `rules/_path_scoped_rules/code_security.md` | `**/*.py`, `**/*.sh`, `**/*.sql`, `**/*.js`, `**/*.ts` | ~195 |
| 2 | `rules/_path_scoped_rules/style_guides/airflow.md` | `**/dags/**/*.py` | ~1105 |
| 3 | `rules/_path_scoped_rules/style_guides/dbt.md` | `**/models/**/*.sql`, `**/dbt_project.yml` | ~1114 |
| 4 | `rules/_path_scoped_rules/style_guides/infra/ansible.md` | `**/playbooks/**/*.yml`, `**/roles/**/*.yml` | ~908 |
| 5 | `rules/_path_scoped_rules/style_guides/infra/terraform.md` | `**/*.tf` | ~478 |
| 6 | `rules/_path_scoped_rules/style_guides/python.md` | `**/*.py` | ~1114 |
| 7 | `rules/_path_scoped_rules/style_guides/sql.md` | `**/*.sql` | ~750 |
| | **Subtotal** | | **~5666** |

## 💤 On demand

| # | File | Tokens |
|---|---|---|
| 1 | `rules/_rules_on_demand/01_ways_of_working/automation_controls.md` | ~719 |
| 2 | `rules/_rules_on_demand/01_ways_of_working/saving_plans.md` | ~169 |
| 3 | `rules/_rules_on_demand/01_ways_of_working/todo_logging.md` | ~141 |
| 4 | `rules/_rules_on_demand/02_communication/writing_style/_audience_and_depth.md` | ~324 |
| 5 | `rules/_rules_on_demand/02_communication/writing_style/_drafts_and_errors.md` | ~199 |
| 6 | `rules/_rules_on_demand/02_communication/writing_style/_markdown_layout.md` | ~264 |
| 7 | `rules/_rules_on_demand/claude_config/authoring_guidelines.md` | ~268 |
| 8 | `rules/_rules_on_demand/claude_config/claude_naming_patterns.md` | ~199 |
| 9 | `rules/_rules_on_demand/claude_config/guiding_principles.md` | ~447 |
| 10 | `rules/_rules_on_demand/claude_config/permission_recommendations.md` | ~154 |
| 11 | `rules/_rules_on_demand/claude_config/portable_paths.md` | ~189 |
| 12 | `rules/_rules_on_demand/claude_config/turn_budgets.md` | ~174 |
| 13 | `rules/_rules_on_demand/style_guides/airflow/_best_practices.md` | ~1071 |
| 14 | `rules/_rules_on_demand/style_guides/airflow/_dag_configuration.md` | ~609 |
| 15 | `rules/_rules_on_demand/style_guides/airflow/_dag_design.md` | ~876 |
| 16 | `rules/_rules_on_demand/style_guides/airflow/_tasks_and_operators.md` | ~1077 |
| 17 | `rules/_rules_on_demand/style_guides/dbt/_macros.md` | ~779 |
| 18 | `rules/_rules_on_demand/style_guides/dbt/_model_organisation.md` | ~1034 |
| 19 | `rules/_rules_on_demand/style_guides/dbt/_naming_conventions.md` | ~969 |
| 20 | `rules/_rules_on_demand/style_guides/dbt/_snapshots.md` | ~523 |
| 21 | `rules/_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md` | ~558 |
| 22 | `rules/_rules_on_demand/style_guides/infra/ansible/_playbooks.md` | ~679 |
| 23 | `rules/_rules_on_demand/style_guides/infra/ansible/_roles_and_tasks.md` | ~1024 |
| 24 | `rules/_rules_on_demand/style_guides/infra/ansible/_variables.md` | ~795 |
| 25 | `rules/_rules_on_demand/style_guides/infra/terraform/_ci_and_tooling.md` | ~603 |
| 26 | `rules/_rules_on_demand/style_guides/infra/terraform/_conventions.md` | ~571 |
| 27 | `rules/_rules_on_demand/style_guides/infra/terraform/_declarations.md` | ~609 |
| 28 | `rules/_rules_on_demand/style_guides/infra/terraform/_modules.md` | ~740 |
| 29 | `rules/_rules_on_demand/style_guides/infra/terraform/_providers.md` | ~535 |
| 30 | `rules/_rules_on_demand/style_guides/infra/terraform/_structure.md` | ~613 |
| 31 | `rules/_rules_on_demand/style_guides/python/_comments.md` | ~258 |
| 32 | `rules/_rules_on_demand/style_guides/python/_python_environment.md` | ~479 |
| 33 | `rules/_rules_on_demand/style_guides/python/code_complexity.md` | ~836 |
| 34 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md` | ~331 |
| 35 | `rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md` | ~748 |
| 36 | `rules/_rules_on_demand/style_guides/python/logging.md` | ~436 |
| 37 | `rules/_rules_on_demand/style_guides/python/logging/_error_handling.md` | ~1177 |
| 38 | `rules/_rules_on_demand/style_guides/python/logging/_setup_and_levels.md` | ~854 |
| 39 | `rules/_rules_on_demand/style_guides/python/logging/_what_to_log.md` | ~1100 |
| 40 | `rules/_rules_on_demand/style_guides/python/module_organisation.md` | ~407 |
| 41 | `rules/_rules_on_demand/style_guides/python/module_organisation/_docstrings.md` | ~1171 |
| 42 | `rules/_rules_on_demand/style_guides/python/module_organisation/_public_private.md` | ~947 |
| 43 | `rules/_rules_on_demand/style_guides/python/testing.md` | ~467 |
| 44 | `rules/_rules_on_demand/style_guides/python/testing/_assertions.md` | ~716 |
| 45 | `rules/_rules_on_demand/style_guides/python/testing/_fixtures_mocking.md` | ~815 |
| 46 | `rules/_rules_on_demand/style_guides/python/testing/_naming_structure.md` | ~396 |
| 47 | `rules/_rules_on_demand/style_guides/sql/_cte_style_guide.md` | ~523 |
| 48 | `rules/_rules_on_demand/style_guides/sql/_formatting.md` | ~929 |
| 49 | `rules/_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md` | ~481 |
| 50 | `rules/_rules_on_demand/style_guides/sql/_sqlfluff.md` | ~388 |
| | **Subtotal** | **~30391** |
