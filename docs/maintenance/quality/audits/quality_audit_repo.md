<!-- version: 1.0.13 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts since the last review, as the [target architecture](../../../target_architecture/target_architecture.md#-measures) asks. The installed config was from before #135, so newer components had no runtime trial:

| Component | Effect | Evidence |
|---|---|---|
| `03_workflows/claude_plans.md`, phase gates | Helped | The user drove multi-phase work one phase at a time, such as "i've merged 24, start phase 4" |
| `_rules_on_demand/03_workflows/saving_plans.md` | Helped | Read from the installed path twice, and approved plans landed in `_plans/` |
| `hooks/hook_enforcement_plan_sections.sh` | Unused | Not registered in the installed `settings.json`, and no block appears in any transcript |
| `_rules_on_demand/03_workflows/sdlc_workflow.md` | Unused | Appears only in the 2 sessions that wrote it |
| `_rules_on_demand/style_guides/**` and `_path_scoped_rules/style_guides/**` | Unused | No transcript reads an installed copy, though they hold over 70% of `src/claude/`'s KB |

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | **7/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-10 | ❌ 0 | ❌ 0 | ✅ 2 | 🟡 1 | ✅ 2 | **5/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 4 duplicates: the fresh-context reviewer in `02_evaluation_criteria.md`, `CONTRIBUTING.md` and the PR template, running `make test` before a PR in `CLAUDE.md`, `tests/README.md` and `CONTRIBUTING.md`, where `_rules_on_demand/` installs in `src/README.md`, `src/claude/README.md` and `target_architecture.md`, and `sdlc_workflow.md` restating `CLAUDE.md`'s plan-with-checks loop | Finding 4 |
| 📦 **Always-on headroom** | About 2,301 of 3,000 tokens, or 76.7%, just over the 75% line | Trim an always-on rule |
| 🔗 **Cross-file consistency** | 4 contradictions: `05_relevance.md` calls adopted plays a proposal not yet adopted, and says project hooks only though a global hook ships, `target_architecture.md` puts every component in a tier but no tier lists hooks, and `file_headers.md` exempts empty placeholder files that `test_file_metadata_headers.py` doesn't | Finding 5 |
| 🔁 **Upkeep cost** | 38 of the last 50 commits touch `docs/maintenance/` other than to record a review, including feature commits that only re-score an audit row, and the repo rubric changed in 14 of them | Finding 5 |
| 🪜 **Simplest mechanism** | 3 heavier than needed: Intent and Spec handled by a pointer, an on-demand rule and a hook, `git_commit.sh` building messages that commitlint already checks, and `git_validate_pr_description.sh` machine-checking bullet counts and URLs | Findings 2 and 3 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧪 **Trial the style guides:** run `make install` so the about 69 style-guide files get a real trial, then retire whichever stacks stay unread.
2. 🪜 **One Intent and Spec mechanism:** keep either the hook, with its guidance in the block message, or `sdlc_workflow.md`, and drop the other along with its pointer and tests.
3. 🗑️ **Scripts that repeat checks:** drop `git_commit.sh`, which commitlint covers, and the bullet and URL checks in `git_validate_pr_description.sh`, with their tests and `CONTRIBUTING.md` mentions.
4. 🎯 **One home per fact:** state the fresh-context reviewer, `make test` before a PR and the `_rules_on_demand/` install location once each, and link to them.
5. 🔗 **Contradictions and upkeep:** fix the 4 contradictions, and decide at the next regular review whether feature commits that re-score an audit row should count towards Upkeep cost.
