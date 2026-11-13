# 📊 Test Coverage Audit

**Purpose:** how good each script's tests are, scored against the test rubric.

- 🧪 **Kept accurate by:** [this audit's checker](../../../tests/maintenance/quality/test_quality_audit_test_files.py), which fails if a test file has no row or a score doesn't add up.
- 🔢 **Counts by score:** run the grep in the [periodic review](../../test_maintenance.md#-periodic-review), rather than keeping a table by hand.
- 🪞 **Own checker:** the checker gets no quality score, since it can't fairly score itself.
- 🕳️ **Gaps:** written by hand when a script is scored, so recheck a script's gaps whenever its tests change.

## ⭐ Quality by script

Each script's tests are scored against the [test rubric](../themes/quality_themes_test_files.md) by an independent review in a fresh context, never by the model that wrote the tests.

| Script or check | Core coverage | Leanness | Clarity | Simplicity | Reliability | Score | Gaps |
|---|---|---|---|---|---|---|---|
| | *Must paths tested* | *No extra tests* | *Easy to follow* | *Short, plain, robust to change* | *Repeatable, clear failures* | | |
| [Header bump](../../../src/sh/bump_file_headers.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Branch name](../../../src/sh/git/git_validate_branch_name.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR size](../../../src/sh/git/git_validate_num_file_changes.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR description](../../../src/sh/git/git_validate_pr_description.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `CRITERIA_NAME` is asserted in the failure branch of two tests, and the shared `CRITERIA`, `SPEC` and `DETAILS` constants feed most cases, so one harmless edit to them breaks many cases at once |
| [PR title](../../../src/sh/git/git_validate_pr_title.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Always-on budget](../../../src/sh/claude_validate_always_on_budget.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: the "over the 150-token budget" message is asserted in two tests, so rewording it breaks both |
| [Install](../../../src/sh/claude_install_config.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `test_files_the_repo_removed_are_backed_up_then_removed` and `test_install_removes_the_plan_hook_when_it_isnt_shipped` each run about 13 to 14 lines and check several things together (removal, backup and manifest; hook removal, kept hooks and backup), and `test_install_registers_the_hooks_and_keeps_existing_settings` checks kept settings, both hook commands and the backup in one test |
| [Plan sections hook](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Done checks hook](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Context cost report](../../../src/sh/claude_report_context_cost.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **A · 9/10** | Reliability: the version-header test never checks its replace changed the report |
| [`shell_utils.sh`](../../../src/sh/shell_utils.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`Makefile`](../../../Makefile) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every script's structure](../../../tests/src/sh/test_script_structure.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every rule's structure](../../../tests/src/claude/test_rules_structure.py) | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **B · 8/10** | Leanness: `test_rule_headings`, `test_rule_lists_are_short` and the emoji-H1 check in `opening_problems` check layout only; Simplicity: `PATH_SCOPED_RULE` is built by chained `.replace()` calls on the shared `GOOD_RULE` (a moving part), `test_path_scoped_rule_passes_the_checks` and `test_child_check_can_fail` each assert several things |
| [Rules quality audit](../../../tests/maintenance/quality/test_quality_audit_rules.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every tracked file's header](../../../tests/test_file_metadata_headers.py) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Core coverage: no bad-header case for a markdown file or one with YAML front matter |
