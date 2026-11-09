<!-- version: 1.0.2 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps one row per run.

## 🔢 Measures by run

| Date | Product files | Support files | `src/claude` | `docs` | `tests` | `src/sh` | Commits touching `docs/maintenance/` | Always-on tokens |
|---|---|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | 143 | 72 | 107 files, 252 KB | 69 files, 240 KB | 20 files, 117 KB | 10 files, 49 KB | 13 of 50 (26%) | ~2,664 |

## ⭐ Scores by run

| Date | Proportionality | Evidence of need | Single source | **Bloat** | Cross-file consistency | Upkeep cost | **Over-engineering** |
|---|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ✅ 2 | ❌ 0 | ❌ 0 | **3/10** | ❌ 0 | 🟡 1 | **3/10** |

### 🔍 Why the latest scores

| Theme | Why it scores this | To improve it |
|---|---|---|
| ⚖️ **Proportionality** | 72 support files against 143 product files, so well within the limit | Keep support growing no faster than the product |
| 🧾 **Evidence of need** | Scorecard folders and templates exist for agents, hooks and skills the repo doesn't have | Remove them, or mark the folders "planned" (findings 1 and 2) |
| 🎯 **Single source** | Two test-scoring systems, and duplicate shell helpers and bash templates | Keep one of each (findings 3 and 4) |
| 🔗 **Cross-file consistency** | The scorecard READMEs contradict each other and the score history | Fix or remove those files (finding 5) |
| 🔁 **Upkeep cost** | 26% of recent commits touch `docs/maintenance/`, mostly to re-score docs | Drop the version-staleness gate, so edits stop forcing re-scores |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🗂️ **Collapse the scorecards:** drop the empty `agents/`, `hooks/`, `skills/` and `tests/` folders under [`quality_scorecards/`](../themes/quality_scorecards/README.md), and cut its unbuilt review steps.
2. 📋 **Templates without components:** `AGENT.md.template` and the `skills/` templates in [`src/claude/_templates/`](../../../../src/claude/_templates/README.md) serve agents and skills the repo doesn't have.
3. 🧪 **Two test-scoring systems:** `quality_scorecards/tests/README.md` scores 7 dimensions, while the [test rubric](../themes/quality_themes_test_files.md) scores 5 themes.
4. 🐚 **Duplicate shell helpers:** `src/sh/shell_utils.sh` matches `src/claude/_templates/utils/shell_utils.sh` byte for byte, and the two bash templates differ only in their headers.
5. 🔗 **Contradictions:** `score_history.csv` credits `quality_scorecard_reviewer`, which the scorecards README says isn't built, and `rules/README.md` asks for per-rule scorecards that the top-level README drops.
