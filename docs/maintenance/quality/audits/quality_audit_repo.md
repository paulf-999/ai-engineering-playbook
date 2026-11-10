<!-- version: 1.0.7 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 🔢 Measures

| Date | Product files | Support files | `docs/maintenance/` files | Commits touching `docs/maintenance/` | Placeholders | Always-on tokens |
|---|---|---|---|---|---|---|
| 2026-11-10 | 147 | 52 | 10 (7%) | 21 of 50 (42%) | 0 | ~2,304 (77%) |

## 🧪 Outcomes by review

The [measures](../../../target_architecture/target_architecture.md#-measures) for the tasks since the previous review:

| Date | Tasks | Time to acceptance (median minutes) | Rework (fix commits) | Interventions | Upkeep (hours) | Notes |
|---|---|---|---|---|---|---|
| 🏁 2026-11-03 | 1 | 17 | 0 | 0 | — | Starting point, at 887 always-on tokens before any component was added; PR links pointed to the branch, so broke after merge |
| 🔧 2026-11-04 | — | — | — | — | 2.3 | Porting session, not a regular review: five files ported, at 2,077 always-on tokens |

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | **7/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | ❌ 0 | ❌ 0 | **2/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | `naming_standards.md` "Offer options" repeats `behaviour.md` "Present options", `authoring_guidelines.md` repeats `guiding_principles.md`, skill and agent name patterns sit in four files, and `rule.md.template` repeats `file_headers.md` | Findings 3 and 4 |
| 📦 **Always-on headroom** | ~2,304 tokens is 77% of the budget, over the 75% line | Trim about 60 tokens (finding 4) |
| 🔗 **Cross-file consistency** | Rule size is "about 100 lines" in `guiding_principles.md` but 110 in `rule.md.template`, `_templates/README.md` names `~/claude/_templates/` against the installer's config directory, `AGENT.md.template` links a missing `_claude_config_metadata.md`, `code_complexity.md` gives nesting as "< 3", and `behaviour.md` and `reporting.md` set different "big change" thresholds | Findings 2, 3 and 5 |
| 🔁 **Upkeep cost** | 21 of the last 50 commits touch `docs/maintenance/` | Finding 1 |
| 🪜 **Simplest mechanism** | The test audit's hand-kept count table and its checker repeat a one-line grep, three rule templates do one template's job, and `rule.md.template`'s checklist repeats what tests enforce | Findings 1 and 3 |
| 🔮 **Built for today** | Agent and skill templates and authoring rules aren't marked "planned", `claude_naming_patterns.md` has a Hook row with no hooks, and the `Makefile` keeps empty `run` and `clean` targets | Findings 2 and 5 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 📊 **Hand-kept test audit:** replace the MoSCoW count table in `quality_audit_test_files.md` and `test_quality_audit_test_files.py` with the grep in `test_maintenance.md`.
2. 📋 **Agent and skill scaffolding:** mark the agent and skill templates "planned" in `_templates/README.md`, since they're coming soon, and fix the missing link in `AGENT.md.template`.
3. 🧩 **One rule template:** merge `rule.md.template` and the two `rules/` templates, drop checklist items that `test_rules_structure.py` enforces, and settle on one rule size limit.
4. 🎯 **Duplicated rule points:** keep "Before you start" only in `guiding_principles.md`, drop "Offer options" from `naming_standards.md`, and keep name patterns only in `claude_naming_patterns.md`.
5. 🛠️ **Small inconsistencies:** cut `code_complexity.md`'s Quick Reference to a pointer, remove the empty `Makefile` targets, fix the `~/claude/_templates/` path, and give `behaviour.md` and `reporting.md` one threshold.
