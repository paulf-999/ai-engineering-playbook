<!-- version: 1.6.1 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-11 -->
# 🏷️ File Headers

**Purpose:** how the version header at the top of each file works, and how a commit check keeps it up to date.

## 📄 Format

Every file opens with a three-line header, placed after any shebang, a YAML file's opening `---` line, or a markdown file's frontmatter block, so YAML never reads it. Markdown uses HTML comments, and other files use `#` comments:

```markdown
<!-- version: 1.0.0 -->
<!-- created: 2026-10-30 -->
<!-- updated: 2026-11-05 -->
```

Entry-point rules in `src/claude/rules/` add two usage lines after it, `applies_to` and `miss_cost`, set out in [`_authoring_rules.md`](../../src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines/_authoring_rules.md).

## 📏 Rules

A pre-commit check, described below, does most of the work:

- 🆕 **New file:** start at `version: 1.0.0`, with `created` and `updated` both set to today.
- ✏️ **Every edit:** leave `created` alone, and let the check handle the rest.
- 🙋 **By hand:** raise MINOR when you add guidance or behaviour, and MAJOR when you reverse or remove it.
- 🚫 **Exempt:** the PR and issue templates, any `.template` file and `LICENSE`.
  - **Full list:** the `EXEMPT` set and `.template` check in `tests/test_file_metadata_headers.py`.

## ⚙️ Automation

The check runs on every commit, once `make deps` has installed the git hooks:

| When you commit a file that… | The check… |
|---|---|
| 🔄 Has changed, including a file moved with `git mv` and edited | Sets `updated` to today and raises PATCH by 1 |
| ✋ Has a version you already raised by hand | Keeps your version and only updates the date |
| ⏸️ Is new, has no header, or was only moved | Leaves it alone |
| 🛑 Has no `updated` line, or a version like `1.0` | Stops the commit and says what to fix |

- 🔁 **After a bump:** the commit stops so you can review it, then re-add the file and commit again.
- 📍 **Where it lives:** `src/sh/bump_file_headers.sh`, run by the `bump_file_headers` hook in `.pre-commit-config.yaml`.
- ✅ **Checked by:** `tests/test_file_metadata_headers.py`, which fails on a missing or malformed header.
- ⚠️ **Gap:** CI can't spot a missed bump, so a commit made with `--no-verify` can skip one.
