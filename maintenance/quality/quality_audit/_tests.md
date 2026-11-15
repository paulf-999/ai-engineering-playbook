# 🧪 Tests

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest score for each script's tests, as part of the [quality audit](../quality_audit.md).

- 🔢 **Counts by score:** run the grep in the [periodic review](../../test_maintenance.md#-periodic-review), rather than keeping a table by hand.
- 🏷️ **Priorities:** [`test_moscow_tags.py`](../../../tests/test_moscow_tags.py) fails if a `# MoSCoW:` tag is anything but `Must`, since only Musts are tagged.
- 🕳️ **Gaps:** written by hand when a script is scored, so recheck a script's gaps whenever its tests change.

## ⭐ Quality by script

Each script's tests are scored against the [test rubric](../quality_rubrics/_tests.md) by an independent review in a fresh context, never by the model that wrote the tests.

| Script or check | Core coverage | Leanness | Clarity | Simplicity | Reliability | Score | Gaps |
|---|---|---|---|---|---|---|---|
| | *Must paths tested* | *No extra tests* | *Easy to follow* | *Short, plain, robust to change* | *Repeatable, clear failures* | | |
| [Branch name](../../../src/sh/git/git_validate_branch_name.sh) | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the regex-probing inputs `feature/My-Change`, `feat/x` and `feature/` in `test_invalid_branch_names_fail` have no comment saying which rule each breaks. |
| [PR size](../../../src/sh/git/git_validate_num_file_changes.sh) | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | **B · 8/10** | Leanness: there are 4 Should tests (override, deletions, missing base, bad limit) against 3 Must. Reliability: `isolated_git_repo` copies `os.environ`, so an exported `MAX_FILES_ALLOWED` changes the 20-file limit and breaks the at-limit and over-limit tests. |
| [PR description](../../../src/sh/git/git_validate_pr_description.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `CRITERIA_NAME` is asserted in the failure branch of two tests, and the shared `CRITERIA`, `SPEC` and `DETAILS` constants feed most cases, so one harmless edit to them breaks many cases at once |
| [Always-on budget](../../../src/sh/claude_validate_always_on_budget.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: the "over the 150-token budget" message is asserted in two tests, so rewording it breaks both |
| [Install](../../../src/sh/claude_install_config.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: `test_files_the_repo_removed_are_backed_up_then_removed` and `test_install_removes_the_plan_hook_when_it_isnt_shipped` each run about 13 to 14 lines and check several things together (removal, backup and manifest; hook removal, kept hooks and backup), and `test_install_registers_the_hooks_and_keeps_existing_settings` checks kept settings, both hook commands and the backup in one test |
| [Plan sections hook](../../../src/claude/hooks/hook_enforcement_plan_sections.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Done checks hook](../../../src/claude/hooks/hook_enforcement_done_checks.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Context cost report](../../../src/sh/claude_report_context_cost.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | **A · 9/10** | Reliability: the version-header test never checks its replace changed the report |
| [`shell_utils.sh`](../../../src/sh/shell_utils.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`Makefile`](../../../Makefile) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every script's structure](../../../tests/src/sh/test_script_structure.py) | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: there are 2 Should tests against 1 Must, and `test_a_missing_part_is_reported` only shows the check can fail. |
| [Every rule's structure](../../../tests/src/claude/test_rules_structure.py) | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Leanness: `test_rule_headings`, `test_rule_lists_are_short`, `test_pointers_sit_in_read_on_demand_section` and the emoji-H1 check in `opening_problems` check layout only. Clarity: the docstring of `test_rule_opens_with_header_h1_and_purpose` promises a "3-line header", but `HEADER_FIELDS` only requires the `created` line. |
| [Every installed file's created line](../../../tests/test_file_metadata_headers.py) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Core coverage: no bad-header case for a markdown file or one with YAML front matter |
