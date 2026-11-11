<!-- version: 1.0.14 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-11 -->
# 🏗️ Repo Quality Audit

**Purpose:** for maintainers, how bloated and how over-engineered the repo is as a whole, each scored out of 10 at each regular review.

Each run follows the [repo rubric](../themes/quality_themes_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history.

## 💬 Component feedback

How each Claude config component fared in the session transcripts since the last review, as the [target architecture](../../../target_architecture/target_architecture.md#-measures) asks:

| Component | Effect | Evidence |
|---|---|---|
| `hooks/hook_enforcement_plan_sections.sh` | Helped | Blocked a plan with no Intent or Spec in 3 sessions and sent Claude to `sdlc_workflow.md`, which was then read |
| `03_workflows/claude_plans.md`, the `sdlc_workflow.md` pointer | Unused | All 3 blocked plans were drafted without reading it first, so the hook did the work |
| `_rules_on_demand/03_workflows/saving_plans.md` | Helped | The most-read on-demand rule, and approved plans landed in `_plans/active/` |
| `_rules_on_demand/03_workflows/git.md` | Helped | Read 6 times |
| `_path_scoped_rules/**` | Hindered | Before #146 all 12 loaded in every session, such as `terraform.md` about 27 times in this repo, and the 2 latest sessions show none |
| `_rules_on_demand/claude_config/guiding_principles.md` | Unused | Always-on pointer, but no session read the installed copy |
| Other on-demand rules and style guides | Unused | No session in any project read an installed copy |

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-11 | ✅ 2 | ✅ 2 | ❌ 0 | 🟡 1 | ✅ 2 | **7/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-11 | 🟡 1 | ❌ 0 | ✅ 2 | 🟡 1 | 🟡 1 | **5/10** |

## 🔍 Why the latest scores

Each theme below ✅, with what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 5 duplicates: mechanism and no-duplicate advice in both `guiding_principles.md` and `authoring_guidelines.md`, the 110-line limit in both, `authoring_guidelines.md`'s Header bullet restating `file_headers.md`, the `intent.md` and `spec.md` split in `sdlc_workflow.md`, `saving_plans.md`, `target_architecture.md` and the hook message, and when each rule folder loads in `src/claude/README.md`, `_authoring_rules.md` and `src/README.md` | Findings 3 and 4 |
| 📦 **Always-on headroom** | About 2,301 of 3,000 tokens, or 76.7%, about 51 tokens over the 75% line | Finding 3 |
| 🔗 **Cross-file consistency** | 3 contradictions: `authoring_guidelines.md` puts the header on lines 1 to 3 where `file_headers.md` and the path-scoped rules put it after the frontmatter, `target_architecture.md` red-flags porting any hook where `02_evaluation_criteria.md` flags only every-prompt hooks, and `tests/README.md` mirrors source paths where `test_hook_enforcement_plan_sections.py` and the `test_quality_audit_*.py` files don't | Findings 4 and 5 |
| 🔁 **Upkeep cost** | 39 of the last 50 commits, or 78%, touch `docs/maintenance/` other than to record a review, and the repo rubric changed 14 times in two days | Finding 2 |
| 🪜 **Simplest mechanism** | 3 heavier than needed: a scored repo rubric and audit run about 5 times in 50 commits, Intent and Spec handled by a pointer, an on-demand rule and a hook, and rules capped by both 110 lines and token limits in `test_rules_structure.py` | Findings 2, 3 and 4 |
| 🔮 **Built for today** | 2 cases: `src/make/variables.mk` defines 7 colours where `Makefile` uses 2, and `.worktreeinclude` copies a `.env` nothing uses | Finding 5 |

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. 🧪 **Unread style guides:** retire or trial the 33 data and infra style-guide files, about 89 KB, in `_rules_on_demand/style_guides/` and their path-scoped parents, since no session in any project read them.
2. 🧊 **Repo review at the regular review only:** run this rubric only at each regular review and keep it frozen between them, since it drives most of the upkeep.
3. 🪝 **Let the hook carry Intent and Spec:** drop the `sdlc_workflow.md` pointer from `claude_plans.md`, and state the `intent.md` and `spec.md` split once, in `saving_plans.md`.
4. 🎯 **Merge shared authoring guidance:** keep one copy of what `guiding_principles.md` and `authoring_guidelines.md` share, link the Header bullet to `file_headers.md`, and keep one size cap in `test_rules_structure.py`.
5. 🧹 **Small fixes:** remove the unused colours and the `.env` line, move or reword the mismatched test paths, and align the hook red-flag line in `target_architecture.md` with `02_evaluation_criteria.md`.
