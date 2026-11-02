<!-- version: 1.0.5 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-02 -->
# 📚 docs

For anyone looking for this repo's guides: which docs are for contributors, which are for maintainers, and where a new doc goes.

- 👥 **Contributors:** the guides in [`reference/`](reference/), such as the [Git branching strategy](reference/git_branching_strategy.md), cover working in a repo made from this template.
- 🛠️ **Maintainers:** [`maintenance/`](maintenance/) covers looking after the template itself, such as file headers and test upkeep, and its [`quality/`](maintenance/quality/) folder splits into `themes/`, which says how to score, and `audits/`, which holds the scores.
- 🆕 **New doc:** put a contributor guide in `reference/` and a maintainer-only one under `maintenance/`, open it with the [version header](maintenance/file_headers.md), and give it a row in the [markdown quality audit](maintenance/quality/audits/quality_audit_markdown_files.md), because `make test` fails on a tracked doc missing either.
