<!-- version: 1.0.32 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-02 -->
# 📊 Markdown Quality Audit

For maintainers of this template: how good each markdown doc is, scored out of 10.

- **Kept accurate by:** [`tests/docs/maintenance/quality/test_quality_audit_markdown_files.py`](../../../../tests/docs/maintenance/quality/test_quality_audit_markdown_files.py), which fails if a tracked doc has no row, a score or grade doesn't match its themes, or Gaps doesn't name a theme below ✅.
- **Scored by:** who gave each row its scores — every row is scored by an independent review in a fresh context, never by the model that wrote the doc.
- **Not scored:** the PR and issue templates, which are forms to fill in rather than docs to read, and this audit, which can't fairly score itself.

## ⭐ Quality by doc

Long doc names are shortened to a label here, to keep the table narrow, and each label links to its doc.

Each doc is scored against [`docs/maintenance/quality/themes/quality_themes_markdown_files.md`](../themes/quality_themes_markdown_files.md).

**Key:**

- ✅ 2 = fully met
- 🟡 1 = partly met
- ❌ 0 = not met
- The score is their total out of 10.

| Doc | Scored by | Core coverage | Leanness | Clarity | Maintainability | Accuracy | Score | Gaps |
|---|---|---|---|---|---|---|---|---|
| | | *Covers reader's tasks* | *Short, no repeats* | *Easy to follow and skim* | *Won't drift* | *Correct today* | | |
| [`CLAUDE.md`](../../../../CLAUDE.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`.github/CONTRIBUTING.md`](../../../../.github/CONTRIBUTING.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`README.md`](../../../../README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`SECURITY.md`](../../../../.github/SECURITY.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`docs` README](../../../README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Branching strategy](../../../git_branching_strategy.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`file_headers.md`](../../file_headers.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Markdown rubric](../themes/quality_themes_markdown_files.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test rubric](../themes/quality_themes_test_files.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test maintenance](../../test_maintenance.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Virtualenv setup](../../../virtualenv_setup.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`src` README](../../../../src/README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`tests` README](../../../../tests/README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Global CLAUDE.md](../../../../src/templates/global_claude.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Tests audit](quality_audit_test_files.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture README](../../../target-architecture/README.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line, overview content or links to child pages; Clarity: no H1 or context, so a newcomer can't tell what the target architecture is |
| [Target architecture](../../../target-architecture/architecture.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line and no description of the configuration or its components; Clarity: no H1 or context to orient a newcomer |
| [Design principles](../../../target-architecture/design-principles.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line and no principles or constraints listed; Clarity: no H1, and "your chosen" doesn't say whose principles they are or why |
| [Reference material README](../../../target-architecture/reference-material/README.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | **F · 5/10** | Core coverage: placeholder only, with no audience line, source register or links to the reference pages; Clarity: no H1, and "the four references" aren't named; Maintainability: hard-coded count "four" will drift as references change; Accuracy: says four references but only two reference pages exist |
| [AI-native SDLC reference](../../../target-architecture/reference-material/anthropic-ai-native-sdlc.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line, source link, guidance or implications; Clarity: no H1, and the source and the term "SDLC" aren't explained |
| [DORA AI capabilities](../../../target-architecture/reference-material/dora-ai-capabilities.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line, source link, capabilities or evidence; Clarity: no H1, and DORA and the "seven capabilities" aren't explained |
