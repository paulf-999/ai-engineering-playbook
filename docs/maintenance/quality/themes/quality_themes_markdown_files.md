<!-- version: 2.1.0 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-03 -->
# 📄 Markdown Quality Rubric

For maintainers of this repo: how to score each markdown doc out of 10, where 10 means short, correct and easy to follow.

---

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the five add up to a grade: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🎯 **Core coverage** | Says who it's for, and fully answers each question that reader brings | Misses one question, or answers it only partly | Placeholder, or the reader can't tell what it's for |
| ⚖️ **Leanness** | Within the limits below, with nothing to cut, linking to detail rather than repeating it | Over a limit, has a sentence or caveat to cut, or repeats another doc | Mostly repetition or padding |
| 📖 **Clarity** | Key point first, jargon explained, rules justified, and emojis as below | One lapse, such as an unexplained term or a buried point | Hard to follow even after a full read |
| 🔧 **Maintainability** | One topic, no history, no file trees, full option lists or hard-coded counts | One such lapse | Two or more lapses |
| ✅ **Accuracy** | Every path, command, link and claim checks out against its source | One wrong path, link or claim | Several errors, or a broken command |

## 📏 How to score

- 🧍 **Score for its own reader:** judge coverage by the questions its opening line promises.
- 🚧 **Placeholder cap:** when Core coverage is ❌, every other theme scores 🟡 at most, because an empty page is easy to keep short and correct.
- 📐 **Limits:** aim for about 300 words a page, with 500 as the ceiling, and 25 words a table cell, unless the page is a lookup table that readers search rather than read.
- 😀 **Emojis:** one at the start of each heading, table row and labelled top-level bullet, but none on plain list items, steps, or `Part of` and `Read` links.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

## 🔁 Re-scoring

- ⚖️ **Fixes add nothing:** a fix mustn't make the page longer, so adding a point means cutting another.
- 🛑 **Two rounds:** if a point flips between rounds, settle it in this rubric, not by editing the page again.
- 🤏 **Borderline notes:** a reviewer's notes that don't cost a mark aren't gaps.

## 🧩 Exceptions

- 📸 **Snapshots:** a page describing a dated commit is checked against that commit, and its counts don't cost Maintainability.
- 🔒 **Maintainer docs:** pages needn't link to `docs/maintenance/`, which is for maintainers only.

## 📊 Where scores live

- 📋 **Audit:** [`quality_audit_markdown_files.md`](../audits/quality_audit_markdown_files.md) holds each doc's scores, gaps and the version scored.
- 🧪 **Checked by:** [`test_quality_audit_markdown_files.py`](../../../../tests/docs/maintenance/quality/test_quality_audit_markdown_files.py), which fails when a row is missing, doesn't add up, breaks the placeholder cap or is out of date.
- 🔢 **Versions:** a content change raises MINOR, so it needs a fresh score, while a typo fix raises only PATCH.
- 🚫 **Not scored:** the PR and issue templates, the audit and this rubric.
