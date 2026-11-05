<!-- version: 1.0.97 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-05 -->
# 📊 Markdown Quality Audit

For maintainers of this template: how good each markdown doc is, scored out of 10.

- **Kept accurate by:** [`tests/docs/maintenance/quality/test_quality_audit_markdown_files.py`](../../../../tests/docs/maintenance/quality/test_quality_audit_markdown_files.py), which fails if a tracked doc has no row, a score doesn't match its themes, Gaps doesn't name a theme below ✅, the placeholder cap is broken, or a doc's MAJOR.MINOR version has moved past the Version scored.
- **Scored by:** who gave each row its scores — every row is scored by an independent review in a fresh context, never by the model that wrote the doc.
- **Version:** the doc's version when it was scored, so a guidance change (a MINOR or MAJOR bump) calls for a fresh score, while a PATCH fix doesn't.
- **Not scored:** the PR and issue templates, which are forms to fill in rather than docs to read, plus this audit and the markdown rubric, which can't fairly score themselves.

## ⭐ Quality by doc

Long doc names are shortened to a label here, to keep the table narrow, and each label links to its doc.

Each doc is scored against [`docs/maintenance/quality/themes/quality_themes_markdown_files.md`](../themes/quality_themes_markdown_files.md).

**Key:**

- ✅ 2 = fully met
- 🟡 1 = partly met
- ❌ 0 = not met
- The score is their total out of 10.

| Doc | Scored by | Version | Core coverage | Leanness | Clarity | Maintainability | Accuracy | Score | Gaps |
|---|---|---|---|---|---|---|---|---|---|
| | | | *Covers reader's tasks* | *Short, no repeats* | *Easy to follow and skim* | *Won't drift* | *Correct today* | | |
| [`CLAUDE.md`](../../../../CLAUDE.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`.github/CONTRIBUTING.md`](../../../../.github/CONTRIBUTING.md) | Independent review | 3.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`README.md`](../../../../README.md) | Independent review | 2.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`SECURITY.md`](../../../../.github/SECURITY.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`docs` README](../../../README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Branching strategy](../../../guides/git_branching_strategy.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`file_headers.md`](../../file_headers.md) | Independent review | 1.5.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test rubric](../themes/quality_themes_test_files.md) | Independent review | 3.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test maintenance](../../test_maintenance.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Task log](../../task_log.md) | Independent review | 1.2.0 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Clarity: the Tasks row's feedback names no component; Leanness: that cell is over 25 words, and the timing sentence repeats the measures definition |
| [Context cost](../../context_cost.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Maintainability: the table is an exhaustive file list, though generated and checked |
| [Virtualenv setup](../../../guides/virtualenv_setup.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`src` README](../../../../src/README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`tests` README](../../../../tests/README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Global CLAUDE.md](../../../../src/claude/CLAUDE.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Guiding principles](../../../../src/claude/rules/_rules_on_demand/claude_config/guiding_principles.md) | Independent review | 2.4.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the engineer test in Real problem doesn't say what \"anyway\" means |
| [Authoring guidelines](../../../../src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "lean session" is a project term the page doesn't explain |
| [Turn budgets](../../../../src/claude/rules/_rules_on_demand/claude_config/turn_budgets.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Portable paths](../../../../src/claude/rules/_rules_on_demand/claude_config/portable_paths.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **B · 8/10** | Clarity: never hard-code `~/.claude` reads against using it as the fallback; Maintainability: the Why bullet cites history |
| [TODO logging](../../../../src/claude/rules/_rules_on_demand/02_conduct/todo_logging.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Automation controls](../../../../src/claude/rules/_rules_on_demand/02_conduct/automation_controls.md) | Independent review | 2.0.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: just over the 500-word ceiling |
| [Writing style](../../../../src/claude/rules/02_conduct/writing_style.md) | Independent review | 3.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Naming standards](../../../../src/claude/rules/01_standards/naming_standards.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude naming patterns](../../../../src/claude/rules/_rules_on_demand/claude_config/claude_naming_patterns.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the Hook row lists hook types without saying what each means |
| [Response standards](../../../../src/claude/rules/01_standards/claude_response_standards.md) | Independent review | 4.0.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Behaviour](../../../../src/claude/rules/02_conduct/behaviour.md) | Independent review | 2.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude plans](../../../../src/claude/rules/03_workflows/claude_plans.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Plan approval gives no reason, and "you" is ambiguous |
| [Saving plans](../../../../src/claude/rules/_rules_on_demand/03_workflows/saving_plans.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: it doesn't say what happens when a plan finishes, or where plan mode's scratch folder is |
| [Git](../../../../src/claude/rules/03_workflows/git.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Flag complex operations and Worktrees give no reason |
| [Security](../../../../src/claude/rules/02_conduct/security.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Code security](../../../../src/claude/rules/_path_scoped_rules/code_security.md) | Independent review | 2.0.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | **B · 8/10** | Leanness: the Logs bullet repeats security.md; Accuracy: "whenever a code file is open" overstates the five globs |
| [Python style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/python.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: over 500 words, repeating `_comments.md`; Clarity: "Absolute imports" describes the wildcard ban |
| [Python: comments](../../../../src/claude/rules/_rules_on_demand/style_guides/python/_comments.md) | Independent review | 1.0.1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: general comment rules are nested under the TODO bullet |
| [Python: environment](../../../../src/claude/rules/_rules_on_demand/style_guides/python/_python_environment.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **B · 8/10** | Clarity: says tests are co-located but shows a separate tree; Maintainability: another project's path |
| [Python: complexity](../../../../src/claude/rules/_rules_on_demand/style_guides/python/code_complexity.md) | Independent review | 1.1.1 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: thresholds repeat the metrics page; Clarity: LOC and CC used before defined |
| [Python: complexity exceptions](../../../../src/claude/rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_exceptions.md) | Independent review | 1.0.1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: its checklist repeats the parent's thresholds |
| [Python: complexity metrics](../../../../src/claude/rules/_rules_on_demand/style_guides/python/code_complexity/_code_complexity_metrics.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | **B · 8/10** | Clarity: its acceptable range disagrees with the parent; Accuracy: another project's path |
| [Python: logging](../../../../src/claude/rules/_rules_on_demand/style_guides/python/logging.md) | Independent review | 1.1.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **A · 9/10** | Accuracy: entry and exit level disagrees with `_what_to_log.md` |
| [Python: what to log](../../../../src/claude/rules/_rules_on_demand/style_guides/python/logging/_what_to_log.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: over 500 words, with the PII rule twice |
| [Python: error handling](../../../../src/claude/rules/_rules_on_demand/style_guides/python/logging/_error_handling.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: over 500 words, repeating the traceback rule; Clarity: bad pattern 4 contradicts an example |
| [Python: logger setup](../../../../src/claude/rules/_rules_on_demand/style_guides/python/logging/_setup_and_levels.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **A · 9/10** | Accuracy: states DEBUG is off in production as fact |
| [Python: module organisation](../../../../src/claude/rules/_rules_on_demand/style_guides/python/module_organisation.md) | Independent review | 1.1.1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | **B · 8/10** | Leanness: rows copied from `_public_private.md`; Accuracy: shows a multi-line docstring the child forbids |
| [Python: docstrings](../../../../src/claude/rules/_rules_on_demand/style_guides/python/module_organisation/_docstrings.md) | Independent review | 1.1.1 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | 🟡 1 | **D · 6/10** | Leanness: over 500 words; Clarity: format guidance contradicts its example; Maintainability: off-topic ordering section; Accuracy: its example uses the prefix it calls wrong |
| [Python: public and private](../../../../src/claude/rules/_rules_on_demand/style_guides/python/module_organisation/_public_private.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | 🟡 1 | **C · 7/10** | Leanness: over 500 words; Clarity: a wrong example isn't explained; Accuracy: a function is listed as both public and private |
| [Python: testing](../../../../src/claude/rules/_rules_on_demand/style_guides/python/testing.md) | Independent review | 1.1.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Python: assertions](../../../../src/claude/rules/_rules_on_demand/style_guides/python/testing/_assertions.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Maintainability: the test organisation section belongs in the naming page |
| [Python: fixtures and mocking](../../../../src/claude/rules/_rules_on_demand/style_guides/python/testing/_fixtures_mocking.md) | Independent review | 1.0.3 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | **B · 8/10** | Clarity: promises env vars but patches `sys.argv`; Accuracy: calls plain helpers fixtures |
| [Python: test naming](../../../../src/claude/rules/_rules_on_demand/style_guides/python/testing/_naming_structure.md) | Independent review | 1.0.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SQL style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/sql.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: Enforcement line and checklist repeat Tooling and Mistakes |
| [SQL: formatting](../../../../src/claude/rules/_rules_on_demand/style_guides/sql/_formatting.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: over 500 words; Clarity: most rules unjustified, and `UNION ALL` sits under Joins |
| [SQL: CTEs](../../../../src/claude/rules/_rules_on_demand/style_guides/sql/_cte_style_guide.md) | Independent review | 1.0.6 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: grouping list and Contents repeat the headings; Clarity: fragments never assembled into one query |
| [SQL: Snowflake data types](../../../../src/claude/rules/_rules_on_demand/style_guides/sql/_snowflake_data_type_standards.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: Contents for three headings, plus a filler sentence; Clarity: NTZ and TZ never explained |
| [SQL: SQLFluff](../../../../src/claude/rules/_rules_on_demand/style_guides/sql/_sqlfluff.md) | Independent review | 1.1.2 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **B · 8/10** | Leanness: repeats the parent's resolve-before-commit rule; Maintainability: excluded-rules table copies `.sqlfluff` |
| [dbt style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/dbt.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: over 500 words; Clarity: `KEY` used without saying it's the surrogate key |
| [dbt: model organisation](../../../../src/claude/rules/_rules_on_demand/style_guides/dbt/_model_organisation.md) | Independent review | 1.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | **C · 7/10** | Leanness: over 500 words; Clarity: the team's default lookback window is never stated; Maintainability: hard-coded folder tree |
| [dbt: naming](../../../../src/claude/rules/_rules_on_demand/style_guides/dbt/_naming_conventions.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: repeats the surrogate-key rules; Clarity: lowercase column rule clashes with uppercase `KEY` names |
| [dbt: YAML properties](../../../../src/claude/rules/_rules_on_demand/style_guides/dbt/_yaml_resource_properties.md) | Independent review | 1.0.6 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **B · 8/10** | Core coverage: source definitions have no example; Leanness: repeats the `KEY` test rule |
| [dbt: macros](../../../../src/claude/rules/_rules_on_demand/style_guides/dbt/_macros.md) | Independent review | 1.0.6 | ✅ 2 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | **B · 8/10** | Maintainability: pinned package versions and a directory tree will drift |
| [dbt: snapshots](../../../../src/claude/rules/_rules_on_demand/style_guides/dbt/_snapshots.md) | Independent review | 1.0.5 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Airflow style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/airflow.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **B · 8/10** | Leanness: over 600 words, and the mistakes table repeats best practices; Maintainability: hard-coded count of principles |
| [Airflow: DAG design](../../../../src/claude/rules/_rules_on_demand/style_guides/airflow/_dag_design.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | 🟡 1 | ❌ 0 | ✅ 2 | **C · 7/10** | Clarity: Contents sits after the first section; Maintainability: file tree plus a Confluence history note |
| [Airflow: DAG configuration](../../../../src/claude/rules/_rules_on_demand/style_guides/airflow/_dag_configuration.md) | Independent review | 1.0.5 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: field table and catchup rule repeat sibling pages |
| [Airflow: tasks and operators](../../../../src/claude/rules/_rules_on_demand/style_guides/airflow/_tasks_and_operators.md) | Independent review | 1.0.6 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: over 500 words, and the `# DAG graph` rule is stated twice |
| [Airflow: best practices](../../../../src/claude/rules/_rules_on_demand/style_guides/airflow/_best_practices.md) | Independent review | 1.1.2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: over 500 words, repeating the parent's idempotency, retries and catchup rules |
| [Terraform style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/infra/terraform.md) | Independent review | 1.5.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Terraform: structure](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_structure.md) | Independent review | 2.0.3 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Maintainability: file tree lists every module directory |
| [Terraform: conventions](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_conventions.md) | Independent review | 2.0.4 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Core coverage: no patterns for databases or service users; Clarity: role prefixes and suffixes never explained |
| [Terraform: declarations](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_declarations.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Terraform: modules](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_modules.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: Module README section repeats the structure page |
| [Terraform: providers](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_providers.md) | Independent review | 1.1.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Terraform: CI and tooling](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/terraform/_ci_and_tooling.md) | Independent review | 1.0.5 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Maintainability: hook table copies `.pre-commit-config.yaml` |
| [Ansible style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/infra/ansible.md) | Independent review | 1.4.0 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | **C · 7/10** | Leanness: tree and naming table repeat the child pages; Clarity: inputs-pattern note assumes back-story; Maintainability: full repo tree will drift |
| [Ansible: playbooks](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/ansible/_playbooks.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **B · 8/10** | Leanness: naming, tree and CODEOWNERS repeat other pages; Maintainability: folder tree |
| [Ansible: roles and tasks](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/ansible/_roles_and_tasks.md) | Independent review | 1.0.7 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | **C · 7/10** | Leanness: over 500 words, repeating variable naming; Clarity: rescue bullet packs four points; Maintainability: role file tree |
| [Ansible: variables](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/ansible/_variables.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: precedence reminder restates the hierarchy; Clarity: site and scope codes never defined |
| [Bash style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/bash.md) | Independent review | 1.5.0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | **C · 7/10** | Clarity: naming and comment rules unjustified; Maintainability: hard-coded lists of utility functions and log colours; Accuracy: its own examples use the end-of-line comments it forbids |
| [Docker style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/infra/docker.md) | Independent review | 1.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Docker: fundamentals](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/docker/_fundamentals.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: `:latest` rule stated twice, and the apt block repeats the advanced page |
| [Docker: advanced](../../../../src/claude/rules/_rules_on_demand/style_guides/infra/docker/_advanced.md) | Independent review | 1.0.3 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: repeats the fundamentals page's copy-order and apt-cleanup guidance |
| [Makefile style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/utilities/makefile.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **B · 8/10** | Clarity: "these rules" points to rules stated only in child pages; Maintainability: hard-coded count of exceptions |
| [Makefile: naming](../../../../src/claude/rules/_rules_on_demand/style_guides/utilities/makefile/_naming_conventions.md) | Independent review | 1.1.1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: no reason given for lowercase names |
| [Makefile: variables and commands](../../../../src/claude/rules/_rules_on_demand/style_guides/utilities/makefile/_variables_operators_and_commands.md) | Independent review | 1.1.1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: the `@echo` carve-out repeats the parent's exception |
| [Mermaid style guide](../../../../src/claude/rules/_path_scoped_rules/style_guides/utilities/mermaid.md) | Independent review | 1.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Mermaid: fundamentals](../../../../src/claude/rules/_rules_on_demand/style_guides/utilities/mermaid/_fundamentals.md) | Independent review | 1.0.2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "Role READMEs" undefined, and the top-down rule unjustified |
| [Mermaid: advanced](../../../../src/claude/rules/_rules_on_demand/style_guides/utilities/mermaid/_advanced.md) | Independent review | 2.0.2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: no reason given for `classDef milestone` on every diagram |
| [Date and time standards](../../../../src/claude/rules/_rules_on_demand/style_guides/utilities/datetime.md) | Independent review | 2.0.3 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | **C · 7/10** | Leanness: no-retroactive-update rule stated twice; Clarity: "DR" undefined; Maintainability: hand-kept Contents and org-specific lists |
| [Jira style guide](../../../../src/claude/rules/_rules_on_demand/style_guides/jira.md) | Independent review | 2.1.0 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: Core principles restate the required fields; Clarity: "Jira values" and "hygiene checks" used before being explained |
| [Jira: ticket conventions](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_ticket_conventions.md) | Independent review | 2.0.2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: "No prose walls" repeats "no prose paragraphs"; Clarity: rules unjustified, and the example drops its H3 heading |
| [Jira: field standards](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_field_standards.md) | Independent review | 2.0.3 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: Components and Business value sections repeat the table; Clarity: "ADF", "Triage" and "hygiene failure" unexplained |
| [Jira: definition of ready](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_definition_of_ready.md) | Independent review | 2.0.3 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Impact Rating block and matrix unexplained, and checks unjustified |
| [Jira: sprint planning](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_sprint_planning.md) | Independent review | 2.0.3 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: closing epic sentence repeats a bullet; Clarity: BAU and MCP tool names unexplained |
| [Jira: business value](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_business_value.md) | Independent review | 2.0.5 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: over 500 words |
| [Jira: values template](../../../../src/claude/rules/_rules_on_demand/style_guides/jira/_jira_values_template.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "ADF document" and "Summary area" unexplained |
| [Testing](../../../../src/claude/rules/_path_scoped_rules/testing.md) | Independent review | 4.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Testing: design pattern](../../../../src/claude/rules/_rules_on_demand/testing/_testing_design_pattern.md) | Independent review | 1.0.3 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: never says where the goal statement goes |
| [Testing: anti-patterns](../../../../src/claude/rules/_rules_on_demand/testing/_testing_anti_patterns.md) | Independent review | 1.2.1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the fragile-test example shows shared state, not implementation coupling |
| [Permission recommendations](../../../../src/claude/rules/_rules_on_demand/claude_config/permission_recommendations.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Markdown layout](../../../../src/claude/rules/_rules_on_demand/02_conduct/writing_style/_markdown_layout.md) | Independent review | 2.0.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: "Review for cuts" repeats the parent's Brevity bullet |
| [Audience and depth](../../../../src/claude/rules/_rules_on_demand/02_conduct/writing_style/_audience_and_depth.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "Partial" for the data analytics team is undefined |
| [Drafts and errors](../../../../src/claude/rules/_rules_on_demand/02_conduct/writing_style/_drafts_and_errors.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: nothing says the table lists the allowed domains, or which one errors use |
| [Tests audit](quality_audit_test_files.md) | Independent review | 3.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture](../../../target_architecture/current_architecture.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: snapshot](../../../target_architecture/current_architecture/01_snapshot.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: what works well](../../../target_architecture/current_architecture/02_what_works_well.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: complexity](../../../target_architecture/current_architecture/03_complexity_without_evidence.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: alignment](../../../target_architecture/current_architecture/04_reference_alignment.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: proposed changes](../../../target_architecture/current_architecture/05_proposed_changes.md) | Independent review | 1.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture README](../../../target_architecture/README.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture](../../../target_architecture/target_architecture.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: the "Not counted" bullet's "caps at 200 lines or 25KB" repeats the memory docs summary and changes nothing the reader does |
| [Design principles](../../../target_architecture/design_principles.md) | Independent review | 1.7.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Principles page](../../../target_architecture/design_principles/01_principles.md) | Independent review | 1.5.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Criteria page](../../../target_architecture/design_principles/02_evaluation_criteria.md) | Independent review | 1.7.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Reference material README](../../../target_architecture/reference_material/README.md) | Independent review | 1.7.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Handover review](../../../target_architecture/reference_material/handover_review.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [AI-native SDLC reference](../../../target_architecture/reference_material/anthropic_ai_native_sdlc.md) | Independent review | 2.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: overview](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/01_overview.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: plays by stage](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/02_plays_by_stage.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: caveats](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/03_caveats.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: our reading](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/04_our_reading.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: relevance](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/05_relevance.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA AI capabilities](../../../target_architecture/reference_material/dora_ai_capabilities.md) | Independent review | 2.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: overview](../../../target_architecture/reference_material/dora_ai_capabilities/01_overview.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: seven capabilities](../../../target_architecture/reference_material/dora_ai_capabilities/02_seven_capabilities.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: findings](../../../target_architecture/reference_material/dora_ai_capabilities/03_findings.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: limitations](../../../target_architecture/reference_material/dora_ai_capabilities/04_limitations.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: applicability](../../../target_architecture/reference_material/dora_ai_capabilities/05_applicability.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF Standard](../../../target_architecture/reference_material/togaf_standards.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: core concepts](../../../target_architecture/reference_material/togaf_standards/01_core_concepts.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: ADM cycle](../../../target_architecture/reference_material/togaf_standards/02_adm_cycle.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: content and continuum](../../../target_architecture/reference_material/togaf_standards/03_content_and_continuum.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: governance and tailoring](../../../target_architecture/reference_material/togaf_standards/04_governance_and_tailoring.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude Code best practices](../../../target_architecture/reference_material/claude_code_best_practices.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Böckeler: harness engineering](../../../target_architecture/reference_material/bockeler_harness_engineering.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Anthropic: agent evals](../../../target_architecture/reference_material/anthropic_agent_evals.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude Code memory docs](../../../target_architecture/reference_material/claude_code_memory_docs.md) | Independent review | 1.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [METR trial](../../../target_architecture/reference_material/metr_developer_productivity_trial.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: State of AI 2025](../../../target_architecture/reference_material/dora_state_of_ai_2025.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "delivery instability", the page's central term, is never explained |
