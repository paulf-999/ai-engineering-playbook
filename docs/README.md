<!-- version: 1.1.1 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-04 -->
# 📚 Docs folder guide

**Purpose:** what each folder under `docs/` holds, and where a new doc goes.

The folders, by reader:

- 🏗️ **Design:** [`target_architecture/`](target_architecture/) holds the design for this repo's Claude configuration, and the sources behind it.
- 👥 **Contributors:** [`guides/`](guides/) holds how-to guides, such as the [Git branching strategy](guides/git_branching_strategy.md).
- 🛠️ **Maintainers:** [`maintenance/`](maintenance/) covers upkeep of this repo, such as file headers and test upkeep.
  - **Quality:** its `quality/` folder holds how docs and tests are scored, in `themes/`, and the scores, in `audits/`.

## 🆕 Adding a doc

`make test` fails on a new doc that misses steps 2 or 3:

1. Put it in the folder for its reader, from the list above.
2. Open it with the [version header](maintenance/file_headers.md).
3. Give it a row in the [markdown quality audit](maintenance/quality/audits/quality_audit_markdown_files.md).
4. Start it with a **Purpose:** line, per the [markdown rubric](maintenance/quality/themes/quality_themes_markdown_files.md).
