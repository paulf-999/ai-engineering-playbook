<!-- version: 1.0.6 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps one row per run.

## 🔢 Measures by run

| Date | Product files | Support files | `docs/maintenance/` files | Commits touching `docs/maintenance/` | Placeholders | Always-on tokens |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | 143 | 72 | 30 (21%) | 13 of 50 (26%) | 28 | ~2,664 (89%) |
| ✂️ 2026-11-09 | 141 | 55 | 12 (9%) | 18 of 50 (36%) | 0 | ~2,664 (89%) |
| 🧹 2026-11-09 | 142 | 50 | 10 (7%) | 19 of 50 (38%) | 0 | ~2,245 (75%) |

## 🧪 Outcomes by review

The [measures](../../../target_architecture/target_architecture.md#-measures) for the tasks since the previous review:

| Date | Tasks | Time to acceptance (median minutes) | Rework (fix commits) | Interventions | Upkeep (hours) | Notes |
|---|---|---|---|---|---|---|
| 🏁 2026-11-03 | 1 | 17 | 0 | 0 | — | Starting point, at 887 always-on tokens before any component was added; PR links pointed to the branch, so broke after merge |
| 🔧 2026-11-04 | — | — | — | — | 2.3 | Porting session, not a regular review: five files ported, at 2,077 always-on tokens |

## 🎈 Bloat by run

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ✅ 2 | ❌ 0 | ❌ 0 | 🟡 1 | ❌ 0 | **3/10** |
| ✂️ 2026-11-09 | ✅ 2 | 🟡 1 | ❌ 0 | 🟡 1 | ✅ 2 | **6/10** |
| 🧹 2026-11-09 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering by run

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ❌ 0 | 🟡 1 | 🟡 1 | ❌ 0 | ❌ 0 | **2/10** |
| ✂️ 2026-11-09 | ❌ 0 | 🟡 1 | ✅ 2 | ❌ 0 | ❌ 0 | **3/10** |
| 🧹 2026-11-09 | ❌ 0 | 🟡 1 | ✅ 2 | ❌ 0 | ❌ 0 | **3/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | Rule points repeat each other: `naming_standards.md` "Offer options" and `behaviour.md` "Present options", `authoring_guidelines.md` and `guiding_principles.md`, and `code_complexity.md` and its size-limits child | Keep each point in one place (finding 3) |
| 🔗 **Cross-file consistency** | `AGENT.md.template` links a missing `_claude_config_metadata.md`, `claude_naming_patterns.md` cites files that don't exist, `code_complexity.md` gives nesting as "< 3" against a limit of 3, and `behaviour.md` says "several files" where `reporting.md` says "many files or turns" | Findings 1, 3 and 5 |
| 🔁 **Upkeep cost** | 19 of the last 50 commits touch `docs/maintenance/` | Findings 2 and 3 |
| 🪜 **Simplest mechanism** | The test audit's hand-kept count table and its checker repeat a one-line grep, and three rule templates do one template's job | Findings 2 and 4 |
| 🔮 **Built for today** | Agent and skill templates and authoring rules serve components that don't exist, and the `Makefile` keeps empty `run` and `clean` targets | Findings 1 and 5 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 📋 **Agent and skill scaffolding:** delete `AGENT.md.template`, the `skills/` templates, `_authoring_agents.md` and `_authoring_skills.md`, and the agent, skill and hook rows in `claude_naming_patterns.md`, since no agent, skill or hook exists.
2. 📊 **Hand-kept test audit:** replace the MoSCoW count table in `quality_audit_test_files.md` and its checker with the grep in `test_maintenance.md`.
3. 🎯 **Duplicated rule points:** keep "Before you start" only in `guiding_principles.md`, drop "Offer options" from `naming_standards.md`, and cut `code_complexity.md`'s Quick Reference to a pointer.
4. 🧩 **Three rule templates:** merge `rule.md.template` and the two `rules/` templates into one, since `test_rules_structure.py` enforces the shape.
5. 🛠️ **Empty targets and thresholds:** remove the empty `run` and `clean` targets from `Makefile`, and give `behaviour.md` and `reporting.md` one threshold.
