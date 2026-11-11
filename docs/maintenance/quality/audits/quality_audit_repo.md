<!-- version: 1.0.18 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-11 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts, kept across reviews on the [component feedback page](quality_audit_repo/component_feedback.md).

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | ✅ 2 | **9/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | 🟡 1 | ✅ 2 | 🟡 1 | ✅ 2 | **8/10** |

## 🔍 Why the latest scores

The blind run of `main` at #170, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 3 duplicates: the grade scale in `quality_themes_rules.md` and `quality_themes_test_files.md`, turning Intent and Spec into `intent.md` and `spec.md` in `sdlc_workflow.md`, `saving_plans.md` and `target_architecture.md`, and running `make test` before a PR in `CLAUDE.md`, `tests/README.md` and `CONTRIBUTING.md` | Findings 3 and 5 |
| 🔁 **Upkeep cost** | 16 of the last 50 commits, or 32%, of which 11 edit the repo rubric between reviews | Finding 1 |
| 🪜 **Simplest mechanism** | 2 issues: about 7 tests in `test_rules_structure.py` that test the checks themselves, and a `# MoSCoW:` label on each of the 96 test functions per `test_maintenance.md` | Findings 2 and 4 |

The one contradiction left, `target_architecture.md` still naming a per-prompt hook red flag that `02_evaluation_criteria.md` no longer lists, is within ✅. Always-on headroom is ✅ at about 2,248 of 3,000 tokens, only 2 tokens under the 75% line.

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧊 **Freeze the rubric:** save edits to `quality_themes_repo.md`, `quality_themes_rules.md` and `quality_themes_test_files.md` for the regular review, which would take Upkeep to about 5 of 50.
2. 🧪 **Tests of the checks:** drop the 7 or so tests in `test_rules_structure.py` that only show each check can fail, and rely on the checks running against the real rules.
3. 📝 **One home for Intent and Spec:** fold `saving_plans.md` into `sdlc_workflow.md`, or have one point to the other, and have `target_architecture.md` link rather than restate.
4. 🏷️ **Fewer MoSCoW labels:** keep `# MoSCoW:` labels only where the tests audit's Core coverage needs them.
5. 🎯 **Small fixes:** keep the grade scale in one rubric, align the per-prompt hook line in `target_architecture.md` with `02_evaluation_criteria.md`, and optionally drop the Evals and CI/CD rows from the Workflow table.
