<!-- version: 1.0.0 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-09 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, whether the repo as a whole is over-engineered or bloated, scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps one row per run.

## 🔢 Measures by run

| Date | Product files | Support files | `src/claude` | `docs` | `tests` | `src/sh` | Commits touching `docs/maintenance/` | Always-on tokens |
|---|---|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | 143 | 72 | 107 files, 252 KB | 69 files, 240 KB | 20 files, 117 KB | 10 files, 49 KB | 13 of 50 (26%) | ~2,664 |

## ⭐ Scores by run

| Date | Proportionality | Evidence of need | Single source | Cross-file consistency | Upkeep cost | Score |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ✅ 2 | ❌ 0 | ❌ 0 | ❌ 0 | 🟡 1 | **3/10** |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🗂️ **Collapse the scorecards:** drop the empty `agents/`, `hooks/`, `skills/` and `tests/` folders under [`quality_scorecards/`](../themes/quality_scorecards/README.md), and cut its unbuilt review steps.
2. 📋 **Templates without components:** `AGENT.md.template` and the `skills/` templates in [`src/claude/_templates/`](../../../../src/claude/_templates/README.md) serve agents and skills the repo doesn't have.
3. 🧪 **Two test-scoring systems:** `quality_scorecards/tests/README.md` scores 7 dimensions, while the [test rubric](../themes/quality_themes_test_files.md) scores 5 themes.
4. 🐚 **Duplicate shell helpers:** `src/sh/shell_utils.sh` matches `src/claude/_templates/utils/shell_utils.sh` byte for byte, and the two bash templates differ only in their headers.
5. 🔗 **Contradictions:** `score_history.csv` credits `quality_scorecard_reviewer`, which the scorecards README says isn't built, and `rules/README.md` asks for per-rule scorecards that the top-level README drops.
