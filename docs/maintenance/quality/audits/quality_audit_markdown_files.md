<!-- version: 1.0.82 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-04 -->
# 📊 Markdown Quality Audit

For maintainers of this template: how good each markdown doc is, scored out of 10.

- **Kept accurate by:** [`tests/docs/maintenance/quality/test_quality_audit_markdown_files.py`](../../../../tests/docs/maintenance/quality/test_quality_audit_markdown_files.py), which fails if a tracked doc has no row, a score doesn't match its themes, Gaps doesn't name a theme below ✅, the placeholder cap is broken, or a doc's MAJOR.MINOR version has moved past the Version scored.
- **Scored by:** who gave each row its scores — every row is scored by an independent review in a fresh context, never by the model that wrote the doc.
- **Version:** the doc's version when it was scored, so a guidance change (a MINOR or MAJOR bump) calls for a fresh score, while a PATCH fix doesn't.
- **Not scored:** the PR and issue templates, which are forms to fill in rather than docs to read, plus this audit and the markdown rubric, which can't fairly score themselves.

## ⭐ Quality by doc

Long doc names are shortened to a label here, to keep the table narrow, and each label links to its doc.

Each doc is scored against [`docs/maintenance/quality/themes/quality_themes_markdown_files.md`](../themes/quality_themes_markdown_files.md).

**Key:**

- ✅ 2 = fully met
- 🟡 1 = partly met
- ❌ 0 = not met
- The score is their total out of 10.

| Doc | Scored by | Version | Core coverage | Leanness | Clarity | Maintainability | Accuracy | Score | Gaps |
|---|---|---|---|---|---|---|---|---|---|
| | | | *Covers reader's tasks* | *Short, no repeats* | *Easy to follow and skim* | *Won't drift* | *Correct today* | | |
| [`CLAUDE.md`](../../../../CLAUDE.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`.github/CONTRIBUTING.md`](../../../../.github/CONTRIBUTING.md) | Independent review | 3.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`README.md`](../../../../README.md) | Independent review | 2.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`SECURITY.md`](../../../../.github/SECURITY.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`docs` README](../../../README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Branching strategy](../../../guides/git_branching_strategy.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`file_headers.md`](../../file_headers.md) | Independent review | 1.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test rubric](../themes/quality_themes_test_files.md) | Independent review | 3.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Test maintenance](../../test_maintenance.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Task log](../../task_log.md) | Independent review | 1.2.0 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | ✅ 2 | **B · 8/10** | Clarity: the Tasks row's feedback names no component; Leanness: that cell is over 25 words, and the timing sentence repeats the measures definition |
| [Context cost](../../context_cost.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **A · 9/10** | Maintainability: the table is an exhaustive file list, though generated and checked |
| [Virtualenv setup](../../../guides/virtualenv_setup.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`src` README](../../../../src/README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [`tests` README](../../../../tests/README.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Global CLAUDE.md](../../../../src/claude/CLAUDE.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Guiding principles](../../../../src/claude/rules/_rules_on_demand/guiding_principles.md) | Independent review | 2.4.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the engineer test in Real problem doesn't say what \"anyway\" means |
| [Authoring guidelines](../../../../src/claude/rules/_rules_on_demand/authoring_guidelines.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "lean session" is a project term the page doesn't explain |
| [Turn budgets](../../../../src/claude/rules/_rules_on_demand/turn_budgets.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Portable paths](../../../../src/claude/rules/_rules_on_demand/portable_paths.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | 🟡 1 | ✅ 2 | **B · 8/10** | Clarity: never hard-code `~/.claude` reads against using it as the fallback; Maintainability: the Why bullet cites history |
| [TODO logging](../../../../src/claude/rules/_rules_on_demand/todo_logging.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Writing style](../../../../src/claude/rules/writing_style.md) | Independent review | 3.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Naming standards](../../../../src/claude/rules/naming_standards.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude naming patterns](../../../../src/claude/rules/_rules_on_demand/claude_naming_patterns.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: the Hook row lists hook types without saying what each means |
| [Response standards](../../../../src/claude/rules/claude_response_standards.md) | Independent review | 4.0.1 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Behaviour](../../../../src/claude/rules/behaviour.md) | Independent review | 2.2.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Check tools first, Report checks and Pre-existing issues give no reason |
| [Claude plans](../../../../src/claude/rules/claude_plans.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Plan approval gives no reason, and "you" is ambiguous |
| [Saving plans](../../../../src/claude/rules/_rules_on_demand/saving_plans.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: it doesn't say what happens when a plan finishes, or where plan mode's scratch folder is |
| [Git](../../../../src/claude/rules/git.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: Flag complex operations and Worktrees give no reason |
| [Security](../../../../src/claude/rules/security.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Code security](../../../../src/claude/rules/path_scoped_rules/code_security.md) | Independent review | 2.0.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | **B · 8/10** | Leanness: the Logs bullet repeats security.md; Accuracy: "whenever a code file is open" overstates the five globs |
| [Permission recommendations](../../../../src/claude/rules/_rules_on_demand/permission_recommendations.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Markdown layout](../../../../src/claude/rules/_rules_on_demand/writing_style/_markdown_layout.md) | Independent review | 2.0.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: "Review for cuts" repeats the parent's Brevity bullet |
| [Audience and depth](../../../../src/claude/rules/_rules_on_demand/writing_style/_audience_and_depth.md) | Independent review | 2.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "Partial" for the data analytics team is undefined |
| [Drafts and errors](../../../../src/claude/rules/_rules_on_demand/writing_style/_drafts_and_errors.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: nothing says the table lists the allowed domains, or which one errors use |
| [Tests audit](quality_audit_test_files.md) | Independent review | 3.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture](../../../target_architecture/current_architecture.md) | Independent review | 2.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: snapshot](../../../target_architecture/current_architecture/01_snapshot.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: what works well](../../../target_architecture/current_architecture/02_what_works_well.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: complexity](../../../target_architecture/current_architecture/03_complexity_without_evidence.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: alignment](../../../target_architecture/current_architecture/04_reference_alignment.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Current architecture: proposed changes](../../../target_architecture/current_architecture/05_proposed_changes.md) | Independent review | 1.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture README](../../../target_architecture/README.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Target architecture](../../../target_architecture/target_architecture.md) | Independent review | 1.5.0 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 9/10** | Leanness: the "Not counted" bullet's "caps at 200 lines or 25KB" repeats the memory docs summary and changes nothing the reader does |
| [Design principles](../../../target_architecture/design_principles.md) | Independent review | 1.7.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Principles page](../../../target_architecture/design_principles/01_principles.md) | Independent review | 1.5.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Criteria page](../../../target_architecture/design_principles/02_evaluation_criteria.md) | Independent review | 1.6.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Reference material README](../../../target_architecture/reference_material/README.md) | Independent review | 1.7.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Handover review](../../../target_architecture/reference_material/handover_review.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [AI-native SDLC reference](../../../target_architecture/reference_material/anthropic_ai_native_sdlc.md) | Independent review | 2.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: overview](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/01_overview.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: plays by stage](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/02_plays_by_stage.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: caveats](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/03_caveats.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: our reading](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/04_our_reading.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [SDLC: relevance](../../../target_architecture/reference_material/anthropic_ai_native_sdlc/05_relevance.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA AI capabilities](../../../target_architecture/reference_material/dora_ai_capabilities.md) | Independent review | 2.2.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: overview](../../../target_architecture/reference_material/dora_ai_capabilities/01_overview.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: seven capabilities](../../../target_architecture/reference_material/dora_ai_capabilities/02_seven_capabilities.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: findings](../../../target_architecture/reference_material/dora_ai_capabilities/03_findings.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: limitations](../../../target_architecture/reference_material/dora_ai_capabilities/04_limitations.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: applicability](../../../target_architecture/reference_material/dora_ai_capabilities/05_applicability.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF Standard](../../../target_architecture/reference_material/togaf_standards.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: core concepts](../../../target_architecture/reference_material/togaf_standards/01_core_concepts.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: ADM cycle](../../../target_architecture/reference_material/togaf_standards/02_adm_cycle.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: content and continuum](../../../target_architecture/reference_material/togaf_standards/03_content_and_continuum.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [TOGAF: governance and tailoring](../../../target_architecture/reference_material/togaf_standards/04_governance_and_tailoring.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude Code best practices](../../../target_architecture/reference_material/claude_code_best_practices.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Böckeler: harness engineering](../../../target_architecture/reference_material/bockeler_harness_engineering.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Anthropic: agent evals](../../../target_architecture/reference_material/anthropic_agent_evals.md) | Independent review | 1.1.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [Claude Code memory docs](../../../target_architecture/reference_material/claude_code_memory_docs.md) | Independent review | 1.4.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [METR trial](../../../target_architecture/reference_material/metr_developer_productivity_trial.md) | Independent review | 1.3.0 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | ✅ 2 | **A · 10/10** | — |
| [DORA: State of AI 2025](../../../target_architecture/reference_material/dora_state_of_ai_2025.md) | Independent review | 1.0.0 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **A · 9/10** | Clarity: "delivery instability", the page's central term, is never explained |
