<!-- version: 1.0.44 -->
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
| [Branching strategy](../../../reference/git_branching_strategy.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`file_headers.md`](../../file_headers.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Markdown rubric](../themes/quality_themes_markdown_files.md) | Independent review | ✅ 2 | 🟡 1 | 🟡 1 | 🟡 1 | 🟡 1 | **D · 6/10** | Leanness: 528 words, over its own limit, with limits repeated between the table and How to score; Clarity: the `Part of` and `Read` exemption and "tracked doc" are unexplained; Maintainability: the size limits appear twice and "the five" is a hard-coded count; Accuracy: it says maintainer docs aren't linked from contributor docs, but three are |
| [Test rubric](../themes/quality_themes_test_files.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test maintenance](../../test_maintenance.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Virtualenv setup](../../../reference/virtualenv_setup.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`src` README](../../../../src/README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`tests` README](../../../../tests/README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Global CLAUDE.md](../../../../src/templates/global_claude.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Tests audit](quality_audit_test_files.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture](../../../target_architecture/current_architecture.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: snapshot](../../../target_architecture/current_architecture/01_snapshot.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: what works well](../../../target_architecture/current_architecture/02_what_works_well.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: complexity](../../../target_architecture/current_architecture/03_complexity_without_evidence.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: alignment](../../../target_architecture/current_architecture/04_reference_alignment.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: proposed changes](../../../target_architecture/current_architecture/05_proposed_changes.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture README](../../../target_architecture/README.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line, overview content or links to child pages; Clarity: no H1 or context, so a newcomer can't tell what the target architecture is |
| [Target architecture](../../../target_architecture/target_architecture.md) | Independent review | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **C · 7/10** | Core coverage: placeholder only, with no audience line and no description of the configuration or its components; Clarity: no H1 or context to orient a newcomer |
| [Design principles](../../../target_architecture/design_principles.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Principles page](../../../target_architecture/design_principles/01_principles.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Criteria page](../../../target_architecture/design_principles/02_evaluation_criteria.md) | Independent review | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Core coverage: the Evidence, Cost and Before-and-after checks rely on the unbuilt task log and budget check, with no interim way to answer them; Clarity: "logged tasks", "always-on budget check" and "Tier" are undefined on the page, and the two-task threshold has no reason |
| [Reference material README](../../../target_architecture/reference_material/README.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [AI-native SDLC reference](../../../target_architecture/reference_material/anthropic_ai_native_sdlc.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: overview](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/01_overview.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: plays by stage](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/02_plays_by_stage.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: caveats](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/03_caveats.md) | Independent review | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **B · 8/10** | Clarity: "the indicators", "plays" and "closing lesson" go unexplained for a reader who lands here directly, and the link label "Capture as intent.md" reads like a filename; Maintainability: the "in beta" status of Claude Tag will go out of date |
| [SDLC: our reading](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/04_our_reading.md) | Independent review | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "organisation features" is vague, "the planned audit" isn't linked to any plan, and the glossary and reading bullets run together with no heading between them |
| [SDLC: relevance](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/05_relevance.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA AI capabilities](../../../target_architecture/reference_material/dora_ai_capabilities.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: overview](../../../target_architecture/reference_material/dora_ai_capabilities/01_overview.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: seven capabilities](../../../target_architecture/reference_material/dora_ai_capabilities/02_seven_capabilities.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: findings](../../../target_architecture/reference_material/dora_ai_capabilities/03_findings.md) | Independent review | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: glossary terms and findings run together as one unheaded bullet list, "Context rot" appears in both, and "the rubric" and "it also amplifies" depend on context the page never gives |
| [DORA: limitations](../../../target_architecture/reference_material/dora_ai_capabilities/04_limitations.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: applicability](../../../target_architecture/reference_material/dora_ai_capabilities/05_applicability.md) | Independent review | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
