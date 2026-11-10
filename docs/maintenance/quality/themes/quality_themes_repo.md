<!-- version: 1.0.4 -->
<!-- created: 2026-11-09 -->
<!-- updated: 2026-11-10 -->
# 🏗️ Repo Quality Rubric

**Purpose:** how a reviewer gives the whole repo a bloat score and an over-engineering score, each out of 10, which per-file scores can't see.

A per-file score rates how well a file is written, not whether it should exist. This rubric looks across files instead.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and each score adds up its 5 themes, so 10 out of 10 means none of the problem.

### 🎈 Bloat

Files and text the repo doesn't need:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| ⚖️ **Proportionality** | Support files are no more than product files | Up to double | More than double |
| 🧾 **Evidence of need** | Every file has a current user or inbound link | One file has none | Several have none |
| 🎯 **Single source** | Each fact, rule or check lives in one place | One duplicate | Several duplicates |
| 📦 **Always-on headroom** | Always-on tokens are 75% of the budget or less | Up to 90% | Over 90% |
| 🚧 **Placeholders** | No "not built yet" or "Nothing scored yet" text | 1 to 5 | More than 5 |

### 🏗️ Over-engineering

Process and machinery heavier than the repo needs:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🔗 **Cross-file consistency** | No file contradicts another | One contradiction | Several contradictions |
| 🔁 **Upkeep cost** | 20% or fewer of the last 50 commits touch `docs/maintenance/` | Up to 40% | Over 40% |
| 🗃️ **Process weight** | `docs/maintenance/` files are a tenth of product files or fewer | Up to a quarter | More than a quarter |
| 🪜 **Simplest mechanism** | Each check or process is the simplest that works, such as a test before a scored rubric | One heavier than needed | Several |
| 🔮 **Built for today** | No levels, stages or extension points for needs that haven't arisen | One | Several |

## 📏 How to score

- 📐 **Measured themes:** Proportionality, Always-on headroom, Placeholders, Upkeep cost and Process weight come from the measures below, not judgement, so they can't drift upwards.
- 📍 **Judged themes:** each 🟡 or ❌ for the other five must cite a path.
- 🧮 **No double count:** Evidence of need counts whole files nothing uses, and Built for today counts unused capacity inside files that are used.
- 🤝 **Kept by choice:** don't mark down a folder its README marks "planned", the separate `shell_utils.sh` copies, or the token report, `docs/maintenance/context_cost.md`, whose commits the upkeep measure leaves out.
- 🔢 **Product and support:** product is `src/claude/` and `docs/target_architecture/`, and support is `tests/`, `src/sh/`, `docs/maintenance/` and `.github/`.

## 🔢 Measures

Run these from the repo root on `main`, and record each result:

```bash
# product and support file counts
git ls-files src/claude docs/target_architecture | wc -l
git ls-files tests src/sh docs/maintenance .github | wc -l
# files and KB by area
for area in src/claude docs tests src/sh; do echo "${area}: $(git ls-files "${area}" | wc -l) files, $(git ls-files -z "${area}" | xargs -0 cat | wc -c | awk '{print int($1 / 1024)}') KB"; done
# commits of the last 50 on main that touch docs/maintenance/, other than the kept token report
git log --first-parent -50 --format=%h origin/main | while read -r commit; do git show --name-only --format= "${commit}" | grep '^docs/maintenance/' | grep -qv '^docs/maintenance/context_cost\.md$' && echo "${commit}"; done | wc -l
# docs/maintenance/ files
git ls-files docs/maintenance | wc -l
# placeholder phrases, leaving out this rubric and its audit
git grep -ciE 'not built yet|nothing scored yet' -- '*.md' ':!docs/maintenance/quality/*/quality_*_repo.md' | awk -F: '{sum += $2} END {print sum + 0}'
# always-on tokens, against the 3,000-token budget
src/sh/claude_validate_always_on_budget.sh
```

For the audit's Outcomes table, read the session transcripts since the last review, in the `projects/` folder of the Claude config directory, and count fix commits with `git log`.

## 🕵️ Reviewer brief

At each [regular review](../../../target_architecture/design_principles/01_principles.md#-numbers-and-tests), one fresh-context Explore agent gets only this brief, since a primed brief inflates scores:

```text
Score this repo against docs/maintenance/quality/themes/quality_themes_repo.md.
Run its measures, score each theme, and cite a path for each judged 🟡 or ❌.
Return the measures, the Outcomes row, the ten theme scores with a reason each,
the Bloat and Over-engineering totals, and up to 5 findings ranked by how much
they would cut, each naming the files involved.
```

## 📊 Where scores live

The [audit](../audits/quality_audit_repo.md) holds one row per run and the current findings.
