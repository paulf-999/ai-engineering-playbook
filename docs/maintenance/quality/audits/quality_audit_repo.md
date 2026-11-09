<!-- version: 1.0.3 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps one row per run.

## 🔢 Measures by run

| Date | Product files | Support files | `docs/maintenance/` files | Commits touching `docs/maintenance/` | Placeholders | Always-on tokens |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | 143 | 72 | 30 (21%) | 13 of 50 (26%) | 28 | ~2,664 (89%) |

## 🎈 Bloat by run

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ✅ 2 | ❌ 0 | ❌ 0 | 🟡 1 | ❌ 0 | **3/10** |

## 🏗️ Over-engineering by run

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ❌ 0 | 🟡 1 | 🟡 1 | ❌ 0 | ❌ 0 | **2/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🧾 **Evidence of need** | Scorecard folders and templates serve agents, hooks and skills the repo doesn't have | Remove them, or mark the folders "planned" (findings 1 and 2) |
| 🎯 **Single source** | Rules and tests are each scored two ways, and the shell helpers and bash templates are duplicated | Keep one of each (findings 3 and 4) |
| 📦 **Always-on headroom** | Always-on context is 89% of the budget | Cut about 400 tokens, or move sections on demand (finding 5) |
| 🚧 **Placeholders** | All 28 sit in `quality_scorecards/` | Collapse that folder (finding 1) |
| 🔗 **Cross-file consistency** | The scorecard READMEs contradict each other and the score history | Collapse that folder (finding 1) |
| 🔁 **Upkeep cost** | Commits re-scoring docs after each guidance edit | Drop the version-staleness gate (finding 3) |
| 🗃️ **Process weight** | `quality_scorecards/` alone holds 20 of the 30 maintenance files | Collapse that folder (finding 1) |
| 🪜 **Simplest mechanism** | A scored review, a staleness gate and six summaries sit on top of the structure test | Keep the test and one audit (findings 1 and 3) |
| 🔮 **Built for today** | Maturity stages, eval runners and five-type rollups wait for components that don't exist | Remove them with the folders they serve (findings 1 and 2) |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🗂️ **Collapse the scorecards:** keep only what's used in [`quality_scorecards/`](../themes/quality_scorecards/README.md), dropping its `agents/`, `hooks/`, `skills/` and `tests/` folders and its unbuilt review steps.
2. 📋 **Templates without components:** remove `AGENT.md.template` and the `skills/` templates in [`src/claude/_templates/`](../../../../src/claude/_templates/README.md), since no agents or skills exist.
3. 🧪 **Score each type one way:** keep the markdown audit and the [test rubric](../themes/quality_themes_test_files.md), and drop the second scoring system for each and the version-staleness gate.
4. 🐚 **Duplicate shell files:** `src/sh/shell_utils.sh` matches `src/claude/_templates/utils/shell_utils.sh` byte for byte, and the two bash templates are near-copies.
5. 📦 **Always-on headroom:** trim the largest always-on files, `src/claude/CLAUDE.md` and `behaviour.md`, to get back under 75% of the budget.
