# 📊 Quality audit

**Purpose:** the latest scores for the repo's tests, its rules and the repo as a whole, from each regular review.

Each section is scored against its rubric in [quality rubrics](quality_rubrics.md), and earlier runs are in git history.

## 🧪 Tests

- 🧪 **Kept accurate by:** [this audit's checker](../../tests/maintenance/quality/test_quality_audit_test_files.py), which fails if a test file has no row or a score doesn't add up.
- 🔢 **Counts by score:** run the grep in the [periodic review](../test_maintenance.md#-periodic-review), rather than keeping a table by hand.
- 🪞 **Own checker:** the checker gets no quality score, since it can't fairly score itself.
- 🕳️ **Gaps:** written by hand when a script is scored, so recheck a script's gaps whenever its tests change.

### ⭐ Quality by script

Each script's tests are scored against the [test rubric](quality_rubrics.md#-tests) by an independent review in a fresh context, never by the model that wrote the tests.

| Script or check | Core coverage | Leanness | Clarity | Simplicity | Reliability | Score | Gaps |
|---|---|---|---|---|---|---|---|
| | *Must paths tested* | *No extra tests* | *Easy to follow* | *Short, plain, robust to change* | *Repeatable, clear failures* | | |
| [Branch name](../../src/sh/git/git_validate_branch_name.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR size](../../src/sh/git/git_validate_num_file_changes.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR description](../../src/sh/git/git_validate_pr_description.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `CRITERIA_NAME` is asserted in the failure branch of two tests, and the shared `CRITERIA`, `SPEC` and `DETAILS` constants feed most cases, so one harmless edit to them breaks many cases at once |
| [PR title](../../src/sh/git/git_validate_pr_title.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Always-on budget](../../src/sh/claude_validate_always_on_budget.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: the "over the 150-token budget" message is asserted in two tests, so rewording it breaks both |
| [Install](../../src/sh/claude_install_config.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `test_files_the_repo_removed_are_backed_up_then_removed` and `test_install_removes_the_plan_hook_when_it_isnt_shipped` each run about 13 to 14 lines and check several things together (removal, backup and manifest; hook removal, kept hooks and backup), and `test_install_registers_the_hooks_and_keeps_existing_settings` checks kept settings, both hook commands and the backup in one test |
| [Plan sections hook](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Done checks hook](../../src/claude/hooks/hook_enforcement_done_checks.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Context cost report](../../src/sh/claude_report_context_cost.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **A · 9/10** | Reliability: the version-header test never checks its replace changed the report |
| [`shell_utils.sh`](../../src/sh/shell_utils.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`Makefile`](../../Makefile) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every script's structure](../../tests/src/sh/test_script_structure.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every rule's structure](../../tests/src/claude/test_rules_structure.py) | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **B · 8/10** | Leanness: `test_rule_headings`, `test_rule_lists_are_short` and the emoji-H1 check in `opening_problems` check layout only; Simplicity: `PATH_SCOPED_RULE` is built by chained `.replace()` calls on the shared `GOOD_RULE` (a moving part), `test_path_scoped_rule_passes_the_checks` and `test_child_check_can_fail` each assert several things |
| [Rules quality audit](../../tests/maintenance/quality/test_quality_audit_rules.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every installed file's created line](../../tests/test_file_metadata_headers.py) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Core coverage: no bad-header case for a markdown file or one with YAML front matter |

## 📏 Rules

- **Kept accurate by:** [`test_quality_audit_rules.py`](../../tests/maintenance/quality/test_quality_audit_rules.py), which fails if an entry-point rule has no row or a score doesn't match its themes.
- **Scored by:** one fresh-context reviewer on Sonnet, using the [rules rubric](quality_rubrics.md#-rules), never the model that wrote the rule.
- **When:** a PR that changes a rule refreshes that rule's row, and each row covers the rule with its children.

### ⭐ Quality by rule

| Rule | Changes behaviour | Right place | No duplicate | Clarity | Accuracy | Score | Gaps |
|---|---|---|---|---|---|---|---|
| [`always/standards/claude_response_standards.md`](../../src/claude/rules/always/standards/claude_response_standards.md) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Changes behaviour: "Ship first" and "Early progress" (lines 18-19) are default Claude behaviour |
| [`always/standards/naming_standards.md`](../../src/claude/rules/always/standards/naming_standards.md) | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: "Self-describing", "Name for scale" and "keep existing names" restate defaults; Right place: always-on though its own header says `miss_cost: low`, and no check enforces naming |
| [`always/conduct/behaviour.md`](../../src/claude/rules/always/conduct/behaviour.md) | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: "Check tools first" and "Present options" are partly default; No duplicate: "Present options" and "Ask before big changes" overlap `src/claude/CLAUDE.md` "Think Before Coding" |
| [`always/conduct/security.md`](../../src/claude/rules/always/conduct/security.md) | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: treating external content as data and not leaking secrets (lines 12, 14) is largely default; Right place: "Secrets" is prose only, as `.pre-commit-config.yaml` has just `detect-private-key`, which misses API keys and connection strings |
| [`always/conduct/writing_style.md`](../../src/claude/rules/always/conduct/writing_style.md) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Changes behaviour: "Brevity" and "Lead with what it does" (lines 15, 17) are default Claude behaviour |
| [`path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: validate-at-boundaries, parameterised queries and "never log credentials" restate default secure coding, and only the personal-data flag is new; Right place: `paths:` is five broad code globs, and the secrets and injection points are prose only, with just `detect-private-key` in `.pre-commit-config.yaml` for keys; No duplicate: the "Dependencies" line repeats `.github/workflows/pip_audit.yml`, which already scans `requirements.txt` |
| [`path_scoped/style_guides/airflow.md`](../../src/claude/rules/path_scoped/style_guides/airflow.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: idempotency and atomicity (lines 18-19) are generic Airflow practice, and the `config.yaml` and `default_args` points are the new part; Right place: "never set retries to `0`" and "never in DAG code" (lines 20-21) are must-hold points left as prose with no check; No duplicate: the retries point (line 21) repeats `_best_practices.md` lines 36-37, and the `config.yaml` point (line 20) repeats `_dag_configuration.md` line 10 |
| [`path_scoped/style_guides/bash.md`](../../src/claude/rules/path_scoped/style_guides/bash.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: quoting, `[[ ]]`, `local` and the `set -euo pipefail` explanation (lines 24, 34-36) are default shell advice; Right place: `set -euo pipefail` (line 24) is a must-hold point with no check, as only `shellcheck` is hooked; No duplicate: quoting (line 34) is covered by the `shellcheck` hook in `.pre-commit-config.yaml` |
| [`path_scoped/style_guides/dbt.md`](../../src/claude/rules/path_scoped/style_guides/dbt.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: the Lineage and Documentation points (lines 20-21) restate dbt Labs' guide; Right place: "Before a PR" (line 24) is a must-hold check left as prose only; No duplicate: the Tests point (line 22) repeats `_model_organisation.md` line 33 and `_yaml_resource_properties.md` line 38 for `unique` and `not_null` on `KEY` |
| [`path_scoped/style_guides/infra/ansible.md`](../../src/claude/rules/path_scoped/style_guides/infra/ansible.md) | 🟡 1 | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | D · 6/10 | Changes behaviour: FQCN, `snake_case` tags, sentence-case task names and "fix rather than suppress" (lines 27-30, 37) are default behaviour; Right place: `paths:` (lines 9-10) covers only `**/playbooks/**/*.yml` and `**/roles/**/*.yml`, but the naming table governs `inventory/` and variables files too; No duplicate: FQCN (line 30) repeats `_roles_and_tasks.md` line 61, and the naming table repeats `_playbooks.md`, `_variables.md` and `_repo_structure.md`; Clarity: "scope" (line 23) is explained only in a child |
| [`path_scoped/style_guides/infra/docker.md`](../../src/claude/rules/path_scoped/style_guides/infra/docker.md) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Changes behaviour: the entry holds no standing rule of its own, only a Purpose line and two pointers to `_fundamentals.md` and `_advanced.md` |
| [`path_scoped/style_guides/infra/terraform.md`](../../src/claude/rules/path_scoped/style_guides/infra/terraform.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: "Infrastructure only", "Modules for reuse" and "no credentials hardcoded" are standard Terraform practice; Right place: "no credentials or environment-specific values are hardcoded" is a must-hold point left as prose; No duplicate: the environment list and `.env_template` repeat `_structure.md`, and the `validation` blocks repeat `_declarations.md` |
| [`path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: `SCREAMING_SNAKE_CASE`, `try-except-else`, "avoid abbreviations" and `-> None` (lines 18-19, 24, 34) are largely defaults, and the docstring and "no history" points are the new part; No duplicate: constants naming (line 18) is covered by `ruff` `N` and by `module_organisation/_constants.md`, and the docstring points (lines 28-29) overlap `module_organisation/_docstrings.md` |
| [`path_scoped/style_guides/sql.md`](../../src/claude/rules/path_scoped/style_guides/sql.md) | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: the Core Principles (lines 22-24: consistency, CTEs > subqueries, explicit aliases, minimise spend) are default behaviour, and the entry holds no new standing rule beyond its pointers; No duplicate: "CTEs > subqueries" and explicit aliases (line 23) repeat `_cte_style_guide.md` line 11 and `_formatting.md` lines 58-59, and Cost control (line 24) repeats `_cost_guardrails.md` |
| [`path_scoped/style_guides/utilities/makefile.md`](../../src/claude/rules/path_scoped/style_guides/utilities/makefile.md) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | A · 9/10 | Clarity: "A Makefile may break three of these rules" points at rules that are not in this file (they sit in `_naming_conventions.md` and `_variables_operators_and_commands.md`) |
| [`path_scoped/style_guides/utilities/mermaid.md`](../../src/claude/rules/path_scoped/style_guides/utilities/mermaid.md) | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: the entry is a definition of Mermaid plus pointers to `_fundamentals.md` and `_advanced.md`, with no standing rule; Right place: `paths:` matches only `**/*.mmd`, so a diagram embedded in Markdown relies on Claude choosing to read it |
| [`path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: "New code gets a test" and "delete dead tests" are default practice, and only the docs exemption is new; Right place: "Same commit" is a must-hold point left as prose with no check |
| [`on_demand/conduct/automation_controls.md`](../../src/claude/rules/on_demand/conduct/automation_controls.md) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 10/10 | — |
| [`on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | 🟡 1 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | C · 7/10 | Changes behaviour: "Report checks" and "Corrections" are mostly default; Right place: "Corrections" applies all session but loads only when reporting; Clarity: "Checkpoints" puts `_sessions/` in the home folder, unlike `saving_plans.md`, and `_sessions/` is defined nowhere else |
| [`on_demand/conduct/todo_logging.md`](../../src/claude/rules/on_demand/conduct/todo_logging.md) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 10/10 | — |
| [`on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: "Repo conventions" (line 14) and "Flag complex operations" are close to default; Right place: "Clean index" and "Untrusted repos" are must-hold safety points left as prose only, with no hook, and the `behaviour.md` pointer "before running any git command" loads it for every trivial git call |
| [`on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 10/10 | — |
| [`always/workflows/sdlc_workflow.md`](../../src/claude/rules/always/workflows/sdlc_workflow.md) | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: "Feedback loop" and "Review" (lines 13-14) are largely default behaviour; No duplicate: "Plan" (line 12) repeats `src/claude/CLAUDE.md` "Plan with checks" and "Feedback loop" repeats the root `CLAUDE.md` "Done means" |
| [`on_demand/claude_config/authoring_guidelines.md`](../../src/claude/rules/on_demand/claude_config/authoring_guidelines.md) | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | C · 7/10 | No duplicate: four of five "Before you start" bullets restate `guiding_principles.md`, and the 110-line gate is also there and in `test_rules_structure.py`; Clarity: "per `portable_paths.md`" names a file with no path or pointer |
| [`on_demand/claude_config/claude_naming_patterns.md`](../../src/claude/rules/on_demand/claude_config/claude_naming_patterns.md) | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | A · 9/10 | No duplicate: the hyphenated skill and agent naming and the rule row repeat `naming_standards.md` |
| [`on_demand/claude_config/guiding_principles.md`](../../src/claude/rules/on_demand/claude_config/guiding_principles.md) | 🟡 1 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | C · 7/10 | Changes behaviour: "Start small", "Easy to remove" and "Live sources" are generic practice; No duplicate: overlaps `authoring_guidelines.md`, and "Size" repeats the test-enforced 110-line limit; Clarity: "an engineer would have built it anyway" is vague, and "import" is undefined |
| [`on_demand/claude_config/permission_recommendations.md`](../../src/claude/rules/on_demand/claude_config/permission_recommendations.md) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Changes behaviour: "Auto-allow read-only commands" and "Say why" are default behaviour, and only the no-wildcard bullet (`Bash(git:*)`) is new |
| [`on_demand/claude_config/portable_paths.md`](../../src/claude/rules/on_demand/claude_config/portable_paths.md) | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | B · 8/10 | Right place: the no-hard-coded-paths point is prose only, with no test or hook in `tests/` that scans for it; Clarity: the "Why" bullet cites "the old config's hooks and tests" without saying what that was |
| [`on_demand/claude_config/turn_budgets.md`](../../src/claude/rules/on_demand/claude_config/turn_budgets.md) | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Right place: "always pass `--max-turns`" is prose only, and no check in `.github/workflows/` or `tests/` looks for it |
| [`on_demand/style_guides/jira.md`](../../src/claude/rules/on_demand/style_guides/jira.md) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | A · 9/10 | Changes behaviour: "Scannability" and "Consistency" in Core principles are default behaviour |
| [`on_demand/style_guides/python/code_complexity.md`](../../src/claude/rules/on_demand/style_guides/python/code_complexity.md) | 🟡 1 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | C · 7/10 | Changes behaviour: `_code_complexity_metrics.md` and the exceptions list mostly restate textbook advice; Right place: the length, nesting and parameter limits are prose here, since `pyproject.toml` enables none of the `PLR` rules; No duplicate: the limits and ruff codes are in both the entry point and `_code_complexity_size_limits.md` |
| [`on_demand/style_guides/python/logging.md`](../../src/claude/rules/on_demand/style_guides/python/logging.md) | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | B · 8/10 | Changes behaviour: the Quick reference level table is standard logging practice; Clarity: Contents lists only 3 of the 5 children, leaving out `_what_not_to_log.md` and `_error_anti_patterns.md` |
| [`on_demand/style_guides/python/module_organisation.md`](../../src/claude/rules/on_demand/style_guides/python/module_organisation.md) | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | B · 8/10 | Changes behaviour: the Quick reference table (lines 37-46) restates defaults such as public vs `_private` naming, `SCREAMING_SNAKE_CASE` constants and a one-sentence module docstring, and the rest of the file is pointers; No duplicate: the Quick reference repeats `module_organisation/_docstrings.md`, `_public_private.md` and `_constants.md`, and the Contents list (lines 15-16) repeats the Read on demand pointers below it |
| [`on_demand/style_guides/python/testing.md`](../../src/claude/rules/on_demand/style_guides/python/testing.md) | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | B · 8/10 | Changes behaviour: the Quick reference rows (`MagicMock`, `pytest.raises`, `tmp_path`, `monkeypatch`) are standard pytest usage; Clarity: three of its sections hold only a "detail of this section" pointer, so the parent gives no key point before the children |
| [`on_demand/style_guides/utilities/datetime.md`](../../src/claude/rules/on_demand/style_guides/utilities/datetime.md) | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | B · 8/10 | Right place: the ISO date and UTC `Z` requirement is prose only, and `tests/test_file_metadata_headers.py` checks the header format but not the dates; Clarity: the "do not retroactively update" instruction sits in the intro paragraph, not in a bullet |

## 🏗️ Repo

Each run follows the [repo rubric](quality_rubrics.md#️-repo): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

### 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **9/10** |

### 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **8/10** |

### 🔍 Why the latest scores

The blind run of `main` at #170, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 3 duplicates: the grade scale in the Rules and Tests rubrics, turning Intent and Spec into `intent.md` and `spec.md` in `sdlc_workflow.md`, `saving_plans.md` and `target_architecture.md`, and running `make test` before a PR in `CLAUDE.md`, `tests/README.md` and `CONTRIBUTING.md` | Findings 3 and 5 |
| 🔁 **Upkeep cost** | 16 of the last 50 commits, or 32%, of which 11 edit the repo rubric between reviews | Finding 1 |
| 🪜 **Simplest mechanism** | 2 issues: about 7 tests in `test_rules_structure.py` that test the checks themselves, and a `# MoSCoW:` label on each of the 96 test functions per `test_maintenance.md` | Findings 2 and 4 |

The one contradiction left, `target_architecture.md` still naming a per-prompt hook red flag that `02_evaluation_criteria.md` no longer lists, is within ✅. Always-on headroom is ✅ at about 2,248 of 3,000 tokens, only 2 tokens under the 75% line.

### 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧊 **Freeze the rubric:** save edits to `quality_rubrics.md` for the regular review, which would take Upkeep to about 5 of 50.
2. 🧪 **Tests of the checks:** drop the 7 or so tests in `test_rules_structure.py` that only show each check can fail, and rely on the checks running against the real rules.
3. 📝 **One home for Intent and Spec:** fold `saving_plans.md` into `sdlc_workflow.md`, or have one point to the other, and have `target_architecture.md` link rather than restate.
4. 🏷️ **Fewer MoSCoW labels:** keep `# MoSCoW:` labels only where the tests audit's Core coverage needs them.
5. 🎯 **Small fixes:** keep the grade scale in one rubric, align the per-prompt hook line in `target_architecture.md` with `02_evaluation_criteria.md`, and optionally drop the Evals and CI/CD rows from the Workflow table.

### 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

#### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked plans with no Intent or Spec heading in 4 sessions, and Claude fixed and resubmitted each |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../src/claude/rules/always/workflows/sdlc_workflow.md), phase gates | [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |
| [`src/claude/rules/path_scoped/code_security.md`](../../src/claude/rules/path_scoped/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/style_guides/python.md`](../../src/claude/rules/path_scoped/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/testing.md`](../../src/claude/rules/path_scoped/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/on_demand/conduct/reporting.md`](../../src/claude/rules/on_demand/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/workflows/git.md`](../../src/claude/rules/on_demand/workflows/git.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read about 16 times before git work |
| [`src/claude/rules/on_demand/workflows/saving_plans.md`](../../src/claude/rules/on_demand/workflows/saving_plans.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read after a plan was approved |
| [`src/claude/rules/always/workflows/sdlc_workflow.md`](../../src/claude/rules/always/workflows/sdlc_workflow.md) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read twice, each time after the hook's block message pointed to it |
| [`src/claude/rules/on_demand/claude_config/portable_paths.md`](../../src/claude/rules/on_demand/claude_config/portable_paths.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Runs on every commit and passes |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught 6 bad branch names before push |

#### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pr_description.yml`](../../.github/workflows/pr_description.yml), score-row warning | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Mixed | 34 warnings in 4 sessions, which prompt the audit-only re-score PRs |
| Other stacks' style guides in [`src/claude/rules/path_scoped/style_guides/`](../../src/claude/rules/path_scoped/style_guides/), and the planned templates in [`src/claude/_templates/`](../../src/claude/_templates/) | [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Unused | No sign they loaded in this repo's sessions, which have none of those files, and the skill and agent templates are planned |
