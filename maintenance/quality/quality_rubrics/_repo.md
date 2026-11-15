# 🏗️ Repo

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** how the repo as a whole is scored for bloat and over-engineering, with the measures to run, as part of the [quality rubric](../quality_rubrics.md).

A per-file score rates how well a file is written, not whether it should exist. This rubric looks across files instead.

## 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and each score adds up its 5 themes, so 10 out of 10 means none of the problem.

### 🎈 Bloat

Files and text the repo doesn't need:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| ⚖️ **Proportionality** | Support files are no more than product files | Up to double | More than double |
| 🧾 **Evidence of need** | At most 1 file has no current user or inbound link | 2 or 3 have none | 4 or more have none |
| 🎯 **Single source** | At most 1 fact, rule or check lives in more than one place | 2 or 3 duplicates | 4 or more duplicates |
| 📦 **Always-on headroom** | Always-on tokens are 75% of the budget or less | Up to 90% | Over 90% |
| 🚧 **Placeholders** | No "not built yet" or "Nothing scored yet" text | 1 to 5 | More than 5 |

### 🏗️ Over-engineering

Process and machinery heavier than the repo needs:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🔗 **Cross-file consistency** | At most 1 contradiction between files | 2 or 3 contradictions | 4 or more contradictions |
| 🔁 **Upkeep cost** | 20% or fewer of the last 50 commits touch `maintenance/`, other than to record a review or cut process | Up to 40% | Over 40% |
| 🗃️ **Process weight** | `maintenance/` files are a tenth of product files or fewer | Up to a quarter | More than a quarter |
| 🪜 **Simplest mechanism** | At most 1 check or process is heavier than the simplest that works, such as a scored rubric where a test would do | 2 or 3 | 4 or more |
| 🔮 **Built for today** | At most 1 level, stage or extension point for a need that hasn't arisen | 2 or 3 | 4 or more |

## 📏 How to score

- 📐 **Measured themes:** Proportionality, Always-on headroom, Placeholders, Upkeep cost and Process weight come from the measures below, not judgement, so they can't drift upwards.
- 📍 **Judged themes:** each 🟡 or ❌ for the other five must cite a path.
- 🧊 **Frozen between reviews:** change this rubric only at a regular review, so runs stay comparable and its edits don't drive up Upkeep cost.
- 🔢 **Count issues:** score a judged theme by how many distinct issues it has, since a fresh reviewer always finds one or two.
- 🧮 **No double count:** Evidence of need counts whole files nothing uses, and Built for today counts unused capacity inside files that are used.
- 🤝 **Kept by choice:** don't mark down any of these, which the user keeps on purpose:
  - **Planned:** a folder or file that its README or parent rule marks "planned", and the budget script's scanning of skills, agents, `@` imports and a project `.claude/`.
  - **Audits:** the repo audit, this rubric with its checklists, and the persona review.
  - **Headers:** the `created`, `applies_to` and `miss_cost` lines on installed files.
  - **Seams:** the `ALWAYS_ON_TOKEN_BUDGET` and `MAX_FILES_ALLOWED` overrides the tests use.
  - **Copies and lists:** the separate `shell_utils.sh` copies, the further-reading list in `reference_material/README.md`, and the token report, `maintenance/context_cost.md`, whose commits the upkeep measure leaves out.
- 🔢 **Product and support:** product is `src/claude/` and `docs/target_architecture/`, and support is `tests/`, `src/sh/`, `maintenance/` and `.github/`.

## 🔢 Measures

Run these from the repo root on `main` under `bash`, since another shell's `grep` wrapper can change the counts, and score the measured themes from them:

```bash
# product and support file counts
git ls-files src/claude docs/target_architecture | wc -l
git ls-files tests src/sh maintenance .github | wc -l
# files and KB by area
for area in src/claude docs tests src/sh; do echo "${area}: $(git ls-files "${area}" | wc -l) files, $(git ls-files -z "${area}" | xargs -0 cat | wc -c | awk '{print int($1 / 1024)}') KB"; done
# commits of the last 50 on main that touch maintenance/, other than the kept token report,
# leaving out commits that only record a review, by changing nothing in it outside the audit,
# and commits that cut process, by removing more lines than they add there outside the audit
git log --first-parent -50 --format=%h origin/main | while read -r commit; do
    files=$(git show --name-only --format= "${commit}" | grep -v '^maintenance/context_cost\.md$')
    grep '^maintenance/' <<< "${files}" | grep -qv '^maintenance/quality/quality_audit\.md$' || continue
    git show --numstat --format= "${commit}" -- maintenance ':!maintenance/quality/quality_audit.md' ':!maintenance/context_cost.md' \
        | awk '{added += $1; removed += $2} END {exit !(removed <= added)}' && echo "${commit}"
done | wc -l
# maintenance/ files
git ls-files maintenance | wc -l
# placeholder phrases, leaving out this rubric and its audit
git grep -ciE 'not built yet|nothing scored yet' -- '*.md' ':!maintenance/quality/' | awk -F: '{sum += $2} END {print sum + 0}'
# always-on tokens, against the 3,000-token budget
src/sh/claude_validate_always_on_budget.sh
```

## 🕵️ Reviewer brief

At each [regular review](../../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests), one fresh-context Explore agent gets only this brief, since a primed brief inflates scores. It runs in a scratch worktree of `main` with `quality_audit.md` deleted, so no search can show it the last run's scores:

```text
Score this repo against maintenance/quality/quality_rubrics/_repo.md.
Run its measures, score each theme, and cite a path for each judged 🟡 or ❌.
Return the measures, the ten theme scores with a reason each, one line of
feedback per component the transcripts show helping, hindering or going unused,
the Bloat and Over-engineering totals, and up to 5 findings ranked by how much
they would cut, each naming the files involved.
```

## ✅ Rules and tests checklists

At each regular review, one fresh-context reviewer on Sonnet also checks every rule, with its children, and every script's tests changed since the last review:

| Check | A rule passes when | A script's tests pass when |
|---|---|---|
| 🎯 **Need** | Every point tells Claude something it wouldn't do by default | Every core promise of a hook or CI check has a test |
| 🔁 **No duplicate** | No other rule, doc, hook, test or CI check covers it | No duplicate tests, and none that check only wording or layout |
| 📖 **Clarity** | Key point first, every term explained, and actionable alone | A newcomer can tell what each test checks from its name |
| 🧩 **Right shape** | It loads only for tasks that need it, and must-hold points are also checked | Short, isolated plain pytest, where a harmless change breaks at most one test |
| 🔍 **Accuracy** | Every path, command, link and claim checks out | Each assertion says what broke |

The reviewer gets only this brief:

```text
Check each rule and script listed below against the checklists in maintenance/quality/quality_rubrics/_repo.md.
Read each rule with its children, and each script with its tests, and run the tests.
Return one finding per failed check: the file, the check, the line, and the fix.
```

### 🎫 Where findings go

Open a GitHub issue for each finding the review doesn't fix in its own PR. Fix a test finding by changing or deleting a test, never by adding one.

## 📊 Where scores live

The [audit](../quality_audit.md) holds the latest run's scores and the current findings. Its [component feedback](../quality_audit.md#-component-feedback) section keeps one row per component that helped, listing each run it helped in, and the latest run's Unused and Hindered rows.
