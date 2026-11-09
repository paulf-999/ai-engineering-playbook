<!-- version: 1.0.5 -->
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

## 🎈 Bloat by run

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ✅ 2 | ❌ 0 | ❌ 0 | 🟡 1 | ❌ 0 | **3/10** |
| ✂️ 2026-11-09 | ✅ 2 | 🟡 1 | ❌ 0 | 🟡 1 | ✅ 2 | **6/10** |

## 🏗️ Over-engineering by run

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 🏁 2026-11-09 | ❌ 0 | 🟡 1 | 🟡 1 | ❌ 0 | ❌ 0 | **2/10** |
| ✂️ 2026-11-09 | ❌ 0 | 🟡 1 | ✅ 2 | ❌ 0 | ❌ 0 | **3/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🧾 **Evidence of need** | `src/templates/jinja/` is an empty folder nothing uses | Delete it (finding 3) |
| 🎯 **Single source** | The shell helpers and bash templates each exist twice | Keep one of each (finding 3) |
| 📦 **Always-on headroom** | Always-on context is 89% of the budget | Cut about 415 tokens, or move sections on demand (finding 4) |
| 🔗 **Cross-file consistency** | The agent and skill templates start at 0.x where the header rules say 1.0.0, and the script test checks a different bash template from the one the rules name | Findings 2 and 3 |
| 🔁 **Upkeep cost** | 12 of the 18 maintenance commits regenerate `context_cost.md` | Stop committing the generated report (finding 1) |
| 🪜 **Simplest mechanism** | A committed, freshness-checked token report repeats what the budget check prints | Finding 1 |
| 🔮 **Built for today** | Agent and skill templates carry maturity stages and eval counts for components that don't exist | Finding 2 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧮 **Generated token report:** stop committing `docs/maintenance/context_cost.md` and drop its pre-commit freshness check, since `claude_validate_always_on_budget.sh` already prints the numbers.
2. 📋 **Templates without components:** remove `AGENT.md.template` and the `skills/` templates, with their maturity stages, from [`src/claude/_templates/`](../../../../src/claude/_templates/README.md).
3. 🐚 **Duplicate shell files:** keep one `shell_utils.sh` and one bash template, and delete `src/templates/`, including its empty `jinja/` folder.
4. 📦 **Always-on headroom:** trim `src/claude/CLAUDE.md` and `behaviour.md`, the two largest always-on files, to get under 75% of the budget.
5. 🔁 **Per-doc scoring:** consider scoring docs at each regular review rather than in every PR, since the markdown audit was touched in 8 of the last 50 commits.
