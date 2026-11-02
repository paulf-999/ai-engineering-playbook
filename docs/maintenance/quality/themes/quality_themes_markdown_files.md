<!-- version: 2.0.0 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-02 -->
# 📄 Markdown Quality Rubric

For maintainers of this repo: how to score each markdown doc out of 10, where 10 means short, correct and easy to follow.

---

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the five add up to a grade: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🎯 **Core coverage** | Says who it's for, and fully answers each question that reader brings | Misses one question, or answers it only partly | Placeholder, or the reader can't tell what it's for |
| ⚖️ **Leanness** | Within the limits below, linking to detail rather than repeating it | Over a limit, or repeats a section from another doc | Mostly repetition or padding |
| 📖 **Clarity** | Key point first, jargon explained, rules justified, and emojis as below | One lapse, such as an unexplained term or a buried point | Hard to follow even after a full read |
| 🔧 **Maintainability** | One topic, no history, no file trees, full option lists or hard-coded counts | One such lapse | Two or more lapses |
| ✅ **Accuracy** | Every path, command, link and claim checks out against its source | One wrong path, link or claim | Several errors, or a broken command |

## 📏 How to score

- 🧍 **Score each file for its own reader:** compare it with other docs only to spot repetition.
- 🚧 **Placeholder cap:** when Core coverage is ❌, every other theme scores 🟡 at most, because an empty page is easy to keep short and correct.
- 📐 **Limits:** about 500 words a page and 25 words a table cell, unless the page is a lookup table that readers search rather than read.
- 😀 **Emojis:** one at the start of each heading, table row and top-level bullet, except `Part of` and `Read` link bullets.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

## 🧩 Exceptions

- 📸 **Snapshots:** a page that says it describes a dated commit is checked for Accuracy against that commit, and its counts don't cost Maintainability.
- 🔒 **Maintainer docs:** not linking to docs under `docs/maintenance/` isn't a Core coverage gap, since they're for maintainers only.

## 📊 Where scores live

- 📋 **Audit:** [`quality_audit_markdown_files.md`](../audits/quality_audit_markdown_files.md) holds each doc's scores, gaps and the version scored.
- 🧪 **Checked by:** [`test_quality_audit_markdown_files.py`](../../../../tests/docs/maintenance/quality/test_quality_audit_markdown_files.py), which fails on a missing row, a score or Gaps entry that doesn't add up, a broken placeholder cap, or a doc whose MAJOR.MINOR version has moved past the one scored.
- 🔢 **Versions:** a content change raises MINOR, so it needs a fresh score, while a typo fix raises only PATCH.
- 🚫 **Not scored:** the PR and issue templates, which are forms, plus the audit and this rubric, which can't fairly score themselves.
