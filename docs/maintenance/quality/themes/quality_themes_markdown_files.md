<!-- version: 2.2.0 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-03 -->
# 📄 Markdown Quality Rubric

**Purpose:** how maintainers score each markdown doc out of 10, where 10 means short, correct and easy to follow.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the totals map to grades: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🎯 **Core coverage** | Its Purpose line says what it covers, and the page fully delivers that | Misses or only partly covers one promised point | Placeholder, or the reader can't tell what it's for |
| ⚖️ **Leanness** | Within the limits below, with nothing to cut, linking to detail rather than repeating it | Over a limit, has a sentence or caveat to cut, or repeats another doc | Mostly repetition or padding |
| 📖 **Clarity** | Key point first, every term explained, rules justified, and a newcomer can follow it without other pages | One lapse, such as an undefined term or a buried point | Hard to follow even after a full read |
| 🔧 **Maintainability** | One topic, with no history, file trees, exhaustive lists or hard-coded counts | One such lapse | Two or more lapses |
| 🔍 **Accuracy** | Every path, command, link and claim checks out against its source | One wrong path, link or claim | Several errors, or a broken command |

## 📏 How to score

- 🧍 **Own reader:** judge coverage by what the Purpose line promises, since that's what the reader came for.
- 🚧 **Placeholder cap:** when Core coverage is ❌, every other theme scores 🟡 at most, because an empty page is easy to keep short and correct.
- 📐 **Limits:** aim for about 300 words a page, with 500 as the ceiling, and 25 words a table cell, since long pages bury the point.
  - **Exempt:** lookup tables, which readers search rather than read.
- 😀 **Emojis:** one at the start of each heading, table row and labelled top-level bullet, but none on plain list items or steps, so emojis mark structure without cluttering lists.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

## 🔤 Terms

Clarity and Leanness meet here, so these settle which terms a page must explain.

- 🛠️ **Common terms:** standard engineering terms, such as CI, PR, hook and pre-commit, need no definition.
- 🧩 **Project terms:** a term this project coined gets a short explanation on first use, or a link to where it's defined.
- ✂️ **Not repetition:** a phrase explaining a term isn't repetition, while restating its rules or numbers is.

## 🔁 Re-scoring

A round is one blind review, given only the page and this rubric.

- ⚖️ **Fixes add nothing:** a fix mustn't make the page longer, so adding a point means cutting another.
- 🛑 **Two rounds:** blind scores vary by about a point, so if reviewers disagree across two rounds, settle the point here rather than editing the page again.
- 🤏 **Borderline notes:** a reviewer's notes that don't cost a mark aren't gaps.
- 🧾 **List lead-ins:** a list needs a lead-in sentence only when the heading right above it doesn't already say what the items are.

## 🧩 Exceptions

- 📸 **Snapshots:** a page describing a dated commit is checked against that commit, and its counts don't cost Maintainability.
- 🔒 **Maintainer docs:** pages needn't link to `docs/maintenance/`, which is for maintainers only.

## 📊 Where scores live

The [audit](../audits/quality_audit_markdown_files.md) holds each doc's scores and says which files aren't scored and when a doc needs a fresh score.
