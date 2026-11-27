# 🐚 tests/src/sh

**Purpose:** what each test of the shell scripts in `src/sh/` checks.

| Test | What it checks |
|---|---|
| 📦 [test_claude_install_config.py](test_claude_install_config.py) | The install script copies `src/claude/` into a Claude config directory, correcting links, after a typed `install`, and uninstalls it |
| 🗂️ [claude_install_config/test_file_handling.py](claude_install_config/test_file_handling.py) | The install's file libraries pick, render, compare and back up files |
| ⌨️ [claude_install_config/test_confirmation.py](claude_install_config/test_confirmation.py) | The install's confirmations accept only the exact word and explain each removal |
| ⚙️ [claude_install_config/test_settings.py](claude_install_config/test_settings.py) | The install merges hooks and deny rules into `settings.json`, strips dead hooks and keeps everything else |
| 📊 [test_claude_report_context_cost.py](test_claude_report_context_cost.py) | The context cost report tables each `src/claude/` file's tokens and when it loads |
| 📏 [test_claude_validate_always_on_budget.py](test_claude_validate_always_on_budget.py) | The always-on budget check caps the Claude context loaded into every session |
| 🧱 [test_script_structure.py](test_script_structure.py) | Every script and library in `src/sh/` and the bash script template follow the template's structure |
| 🤝 [test_shell_utils.py](test_shell_utils.py) | The shared shell helper functions |
| 🌿 [git/test_git_validate_branch_name.py](git/test_git_validate_branch_name.py) | The git branch name validation pre-commit hook |
| 🔢 [git/test_git_validate_num_file_changes.py](git/test_git_validate_num_file_changes.py) | The PR file-count check, which skips `release/` branches |
| 🏷️ [git/test_git_validate_skill_versions.py](git/test_git_validate_skill_versions.py) | The skill version check, which fails a PR that changes a skill without bumping its contract version |
| 🚦 [git/test_git_validate_open_prs.py](git/test_git_validate_open_prs.py) | The open PR check, which limits an author to six PRs ready for review and leaves out drafts and Dependabot |
