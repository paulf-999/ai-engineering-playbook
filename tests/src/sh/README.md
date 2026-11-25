# 🐚 tests/src/sh

**Purpose:** what each test of the shell scripts in `src/sh/` checks.

| Test | What it checks |
|---|---|
| 📦 [test_claude_install_config.py](test_claude_install_config.py) | The install script copies `src/claude/` into a Claude config directory, correcting links, after a typed `install` |
| 📊 [test_claude_report_context_cost.py](test_claude_report_context_cost.py) | The context cost report tables each `src/claude/` file's tokens and when it loads |
| 📏 [test_claude_validate_always_on_budget.py](test_claude_validate_always_on_budget.py) | The always-on budget check caps the Claude context loaded into every session |
| 🧱 [test_script_structure.py](test_script_structure.py) | Every script in `src/sh/`, `shell_utils.sh` and the bash script template follow the template's structure |
| 🤝 [test_shell_utils.py](test_shell_utils.py) | The shared shell helper functions |
| 🌿 [git/test_git_validate_branch_name.py](git/test_git_validate_branch_name.py) | The git branch name validation pre-commit hook |
| 🔢 [git/test_git_validate_num_file_changes.py](git/test_git_validate_num_file_changes.py) | The PR file-count check, which skips `release/` branches |
| 🏷️ [git/test_git_validate_skill_versions.py](git/test_git_validate_skill_versions.py) | The skill version check, which fails a PR that changes a skill without bumping its contract version |
| 📝 [git/test_git_validate_pr_description.py](git/test_git_validate_pr_description.py) | The PR description check: a `src/claude/` PR has a Plan section, any Plan section is complete, and an always-on PR has the criteria |
