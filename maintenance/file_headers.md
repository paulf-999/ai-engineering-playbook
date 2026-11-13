# 🏷️ File Headers

**Purpose:** what the header at the top of each installed file records, and how a test keeps it valid.

## 📄 Format

Every file under `src/claude/`, which `make install` copies into your Claude config directory, opens with a `created` line, so you can see how long ago it was added. Other files have none, and git history records every file's changes. The line sits after any shebang, a YAML file's opening `---` line, or a markdown file's frontmatter block, so YAML never reads it. Markdown uses an HTML comment, and other files use a `#` comment:

```markdown
<!-- created: 2026-10-30 -->
```

Entry-point rules in `src/claude/rules/` add two usage lines after it, `applies_to` and `miss_cost`, set out in [`_authoring_rules.md`](../src/claude/rules/on_demand/claude_config/authoring_guidelines/_authoring_rules.md).

## 📏 Rules

- 🆕 **New file:** set `created` to today.
- ✏️ **Every edit:** leave the line alone, since git records when a file last changed.
- 🚫 **Exempt:** any `.template` file, whose header holds a placeholder.
- ✅ **Checked by:** `tests/test_file_metadata_headers.py`, which fails on a missing line, an impossible date or a date in the future.
