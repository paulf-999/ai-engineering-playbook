<!-- version: 3.4.23 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-09 -->
# 📊 Test Coverage Audit

**Purpose:** how many tests each script has, and how good those tests are.

- 🧪 **Kept accurate by:** [this audit's checker](../../../../tests/docs/maintenance/quality/test_quality_audit_test_files.py), which fails if either table falls out of step with the test files.
- 🪞 **Own checker:** the checker counts its own tests but gets no quality score, since it can't fairly score itself.
- 🕳️ **Gaps:** written by hand when a script is scored, so recheck a script's gaps whenever its tests change.

## 🏷️ MoSCoW scores by script

This table counts each script's tests by their [priority score](../../test_maintenance.md#-priority-scores):

- 🔢 **Total (functions):** the test functions, each of which carries one score.
- 🧪 **Test Cases:** the cases pytest runs, since a parametrised function runs once per input.
  - **Totals:** this figure matches what `make test` reports.

| Script or check | Must | Should | Could | Won't | Total (functions) | **Test Cases** |
|---|---|---|---|---|---|---|
| [`bump_file_headers.sh`](../../../../src/sh/bump_file_headers.sh) | 3 | 9 | 2 | 0 | 14 | **14** |
| [`git_commit.sh`](../../../../src/sh/git/git_commit.sh) | 3 | 8 | 2 | 0 | 13 | **17** |
| [`git_validate_branch_name.sh`](../../../../src/sh/git/git_validate_branch_name.sh) | 3 | 0 | 1 | 0 | 4 | **10** |
| [`git_validate_num_file_changes.sh`](../../../../src/sh/git/git_validate_num_file_changes.sh) | 3 | 4 | 3 | 0 | 10 | **12** |
| [`git_validate_pr_description.sh`](../../../../src/sh/git/git_validate_pr_description.sh) | 6 | 0 | 0 | 0 | 6 | **22** |
| [`git_validate_pr_title.sh`](../../../../src/sh/git/git_validate_pr_title.sh) | 3 | 0 | 0 | 0 | 3 | **14** |
| [`claude_validate_always_on_budget.sh`](../../../../src/sh/claude_validate_always_on_budget.sh) | 4 | 1 | 0 | 0 | 5 | **18** |
| [`claude_install_config.sh`](../../../../src/sh/claude_install_config.sh) | 7 | 1 | 0 | 0 | 8 | **8** |
| [`shell_utils.sh`](../../../../src/sh/shell_utils.sh) | 2 | 1 | 2 | 0 | 5 | **13** |
| [`Makefile`](../../../../Makefile) | 2 | 0 | 0 | 0 | 2 | **2** |
| [Every script's structure](../../../../tests/src/sh/test_script_structure.py) | 1 | 3 | 1 | 0 | 5 | **14** |
| [Every rule's structure](../../../../tests/src/claude/test_rules_structure.py) | 13 | 4 | 0 | 0 | 17 | **594** |
| [Rules quality audit](../../../../tests/docs/maintenance/quality/test_quality_audit_rules.py) | 2 | 1 | 0 | 0 | 3 | **5** |
| [This audit's checker](../../../../tests/docs/maintenance/quality/test_quality_audit_test_files.py) | 0 | 2 | 0 | 0 | 2 | **2** |
| [Every tracked file's header](../../../../tests/test_file_metadata_headers.py) | 2 | 0 | 0 | 0 | 2 | **4** |
| **Totals** | | | | | **99** | **749** |

## ⭐ Quality by script

Each script's tests are scored against the [test rubric](../themes/quality_themes_test_files.md) by an independent review in a fresh context, never by the model that wrote the tests.

| Script or check | Core coverage | Leanness | Clarity | Simplicity | Reliability | Score | Gaps |
|---|---|---|---|---|---|---|---|
| | *Must paths tested* | *No extra tests* | *Easy to follow* | *Short, plain, robust to change* | *Repeatable, clear failures* | | |
| [Header bump](../../../../src/sh/bump_file_headers.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`git_commit.sh`](../../../../src/sh/git/git_commit.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Branch name](../../../../src/sh/git/git_validate_branch_name.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR size](../../../../src/sh/git/git_validate_num_file_changes.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR description](../../../../src/sh/git/git_validate_pr_description.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [PR title](../../../../src/sh/git/git_validate_pr_title.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Always-on budget](../../../../src/sh/claude_validate_always_on_budget.sh) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: the "over the 150-token budget" message is asserted in two tests, so rewording it breaks both |
| [Install](../../../../src/sh/claude_install_config.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`shell_utils.sh`](../../../../src/sh/shell_utils.sh) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`Makefile`](../../../../Makefile) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every script's structure](../../../../tests/src/sh/test_script_structure.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every rule's structure](../../../../tests/src/claude/test_rules_structure.py) | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Simplicity: the shared good-rule example adds a moving part |
| [Rules quality audit](../../../../tests/docs/maintenance/quality/test_quality_audit_rules.py) | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Every tracked file's header](../../../../tests/test_file_metadata_headers.py) | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Core coverage: no bad-header case for a markdown file or one with YAML front matter |
