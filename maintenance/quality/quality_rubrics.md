# 📐 Quality rubrics

**Purpose:** how a reviewer scores the repo's tests, its rules and the repo as a whole at each regular review.

Each section is one rubric, and the [quality audit](quality_audit.md) holds the latest scores.

## 🧪 Tests

### 🏷️ Themes

The tests for a script are scored on five themes:

| Theme | What ✅ looks like |
|---|---|
| 🎯 **Core coverage** | Every Must-level behaviour, a core promise of a hook or CI check, has a test (see the [priority scores](../test_maintenance.md#-priority-scores)) |
| ⚖️ **Leanness** | No duplicate tests, and no cosmetic ones that check only wording or layout |
| 📖 **Clarity** | A newcomer can tell what each test checks from its name and docstring |
| 🧩 **Simplicity** | Short tests in plain pytest, where a harmless change breaks at most one test |
| 🧊 **Reliability** | Isolated, repeatable tests whose failures say what broke |

### 🔢 Scores

Each theme scores ✅ 2 when fully met, 🟡 1 when partly met and ❌ 0 when not met. The five add up to a score out of 10, graded A for 9 or more, B for 8, C for 7, D for 6 and F below 6, so four ✅ and one 🟡 show as **A · 9/10**.

### 📏 How to score

- 🗂️ **Score the script, not each test:** look at all of a script's tests together.
- 🌙 **Rare paths don't cost points:** an untested error that almost never happens isn't a Core coverage gap.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

#### 🔍 Theme-specific rules

- 📖 **Clarity:** parsing, regexes, ordering checks and unexplained inputs need a one-line comment, while plain setup doesn't.
- 🧩 **Simplicity:** a test body over about 12 lines costs a point, since it usually checks more than one thing.
  - **Also costs a point:** mocking the script's internals, or asserting the same message text in several tests.
- 🧊 **Reliability:** run each test in a temporary folder or repo.
  - **Git config:** ignore the user's own settings, so the result is the same on any machine.
  - **Failures:** each assertion message says what broke.

### 🛑 Avoiding over-testing

- 📉 **Could tests:** more `Could` tests than `Must` tests costs a Leanness point, as the [periodic review](../test_maintenance.md#-periodic-review) explains.
- 🙅 **Lower scores don't mean add tests:** if a new test would cost Leanness or Simplicity points, leave it out.
- ✂️ **Removing tests can raise the score:** deleting a duplicate or cosmetic test improves Leanness.

### 🕵️ Reviewer brief

Each [periodic review](../test_maintenance.md#-periodic-review) refreshes the row of every script whose tests changed since the last one, in one PR. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief inflates scores:

```text
Score each script listed after this brief against the Tests section of maintenance/quality/quality_rubrics.md.
Read each script with its tests, and run them to check they pass.
Return one audit row per script: the five theme scores, the grade and total, and Gaps.
```

### 📊 Where scores live

The [tests audit](quality_audit.md#-tests) holds each script's scores and gaps, and `tests/maintenance/quality/test_quality_audit_test_files.py` fails if a score doesn't add up.

## 📏 Rules

Right place and No duplicate apply the [evaluation criteria](../../docs/target_architecture/design_principles/02_evaluation_criteria.md) to one rule at a time. A rule here means an entry-point rule in `src/claude/rules/` together with its children, the `_`-prefixed files it points to.

### 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and the totals map to grades: A for 9 or more, B for 8, C for 7, D for 6, and F below 6.

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🎯 **Changes behaviour** | Every point tells Claude something it wouldn't do by default | One or two points restate default behaviour | Mostly default behaviour |
| 🧭 **Right place** | Prose is the right form, it loads only for tasks that need it, and must-hold points are also checked | One lapse, such as broad `paths:` globs or a must-hold point left as prose only | Two or more lapses |
| 🔁 **No duplicate** | No other rule, doc, hook, test or CI check covers it | One point repeats another source | Mostly repeats another source |
| 📖 **Clarity** | Key point first, every term explained, and Claude can act on it without other pages | One lapse, such as an undefined term or a buried point | Hard to follow |
| 🔍 **Accuracy** | Every path, command, link and claim checks out, including any check it says exists | One wrong path, link or claim | Several errors |

### 📏 How to score

- 📍 **Cite it:** each 🟡 or ❌ names the line or file that costs the mark.
- 🌐 **Other repos:** a path-scoped rule written for another repo's layout, such as its folders or hooks, isn't inaccurate for naming things this repo lacks.
- 👨‍👧 **Families:** score a rule with its children, since they load together, and leave the children without rows.
- 🧾 **Need at review time:** whether a rule gets used is checked at each regular review, by the evaluation criteria's Trial check, not here.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

### 🕵️ Reviewer brief

Each regular review refreshes the row of every rule changed since the last one, in one PR. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief inflates scores:

```text
Score each rule below against the Rules section of maintenance/quality/quality_rubrics.md.
Read each rule with its children, and search the repo for duplicates and to check its claims.
Return one audit row per rule: the five theme scores, the grade and total, and Gaps.
```

### 📊 Where scores live

The [audit](quality_audit.md#-rules) holds each rule's row.

## 🏗️ Repo

A per-file score rates how well a file is written, not whether it should exist. This rubric looks across files instead.

### 🏷️ Themes

Each theme scores ✅ 2, 🟡 1 or ❌ 0, and each score adds up its 5 themes, so 10 out of 10 means none of the problem.

#### 🎈 Bloat

Files and text the repo doesn't need:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| ⚖️ **Proportionality** | Support files are no more than product files | Up to double | More than double |
| 🧾 **Evidence of need** | At most 1 file has no current user or inbound link | 2 or 3 have none | 4 or more have none |
| 🎯 **Single source** | At most 1 fact, rule or check lives in more than one place | 2 or 3 duplicates | 4 or more duplicates |
| 📦 **Always-on headroom** | Always-on tokens are 75% of the budget or less | Up to 90% | Over 90% |
| 🚧 **Placeholders** | No "not built yet" or "Nothing scored yet" text | 1 to 5 | More than 5 |

#### 🏗️ Over-engineering

Process and machinery heavier than the repo needs:

| Theme | ✅ 2 | 🟡 1 | ❌ 0 |
|---|---|---|---|
| 🔗 **Cross-file consistency** | At most 1 contradiction between files | 2 or 3 contradictions | 4 or more contradictions |
| 🔁 **Upkeep cost** | 20% or fewer of the last 50 commits touch `maintenance/`, other than to record a review or cut process | Up to 40% | Over 40% |
| 🗃️ **Process weight** | `maintenance/` files are a tenth of product files or fewer | Up to a quarter | More than a quarter |
| 🪜 **Simplest mechanism** | At most 1 check or process is heavier than the simplest that works, such as a scored rubric where a test would do | 2 or 3 | 4 or more |
| 🔮 **Built for today** | At most 1 level, stage or extension point for a need that hasn't arisen | 2 or 3 | 4 or more |

### 📏 How to score

- 📐 **Measured themes:** Proportionality, Always-on headroom, Placeholders, Upkeep cost and Process weight come from the measures below, not judgement, so they can't drift upwards.
- 📍 **Judged themes:** each 🟡 or ❌ for the other five must cite a path.
- 🧊 **Frozen between reviews:** change this rubric only at a regular review, so runs stay comparable and its edits don't drive up Upkeep cost.
- 🔢 **Count issues:** score a judged theme by how many distinct issues it has, since a fresh reviewer always finds one or two.
- 🧮 **No double count:** Evidence of need counts whole files nothing uses, and Built for today counts unused capacity inside files that are used.
- 🤝 **Kept by choice:** don't mark down any of these, which the user keeps on purpose:
  - **Planned:** a folder or file that its README or parent rule marks "planned", and the budget script's scanning of skills, agents, `@` imports and a project `.claude/`.
  - **Audits:** the [tests audit](quality_audit.md#-tests) and [rules audit](quality_audit.md#-rules), with their rubrics and checkers.
  - **Headers:** the `created`, `applies_to` and `miss_cost` lines on installed files.
  - **Review and seams:** the fresh-context reviewer that fills each config PR's evaluation criteria, and the `ALWAYS_ON_TOKEN_BUDGET` and `MAX_FILES_ALLOWED` overrides the tests use.
  - **Copies and lists:** the separate `shell_utils.sh` copies, the further-reading list in `reference_material/README.md`, and the token report, `maintenance/context_cost.md`, whose commits the upkeep measure leaves out.
- 🔢 **Product and support:** product is `src/claude/` and `docs/target_architecture/`, and support is `tests/`, `src/sh/`, `maintenance/` and `.github/`.

### 🔢 Measures

Run these from the repo root on `main` under `bash`, since another shell's `grep` wrapper can change the counts, and score the measured themes from them:

```bash
# product and support file counts
git ls-files src/claude docs/target_architecture | wc -l
git ls-files tests src/sh maintenance .github | wc -l
# files and KB by area
for area in src/claude docs tests src/sh; do echo "${area}: $(git ls-files "${area}" | wc -l) files, $(git ls-files -z "${area}" | xargs -0 cat | wc -c | awk '{print int($1 / 1024)}') KB"; done
# commits of the last 50 on main that touch maintenance/, other than the kept token report,
# leaving out commits that only record a review, by changing nothing in it outside quality_audit.md,
# and commits that cut process, by removing more lines than they add there outside quality_audit.md
git log --first-parent -50 --format=%h origin/main | while read -r commit; do
    files=$(git show --name-only --format= "${commit}" | grep -v '^maintenance/context_cost\.md$')
    grep '^maintenance/' <<< "${files}" | grep -qv '^maintenance/quality/quality_audit\.md$' || continue
    git show --numstat --format= "${commit}" -- maintenance ':!maintenance/quality/quality_audit.md' ':!maintenance/context_cost.md' \
        | awk '{added += $1; removed += $2} END {exit !(removed <= added)}' && echo "${commit}"
done | wc -l
# maintenance/ files
git ls-files maintenance | wc -l
# placeholder phrases, leaving out this rubric and its audit
git grep -ciE 'not built yet|nothing scored yet' -- '*.md' ':!maintenance/quality/quality_*.md' | awk -F: '{sum += $2} END {print sum + 0}'
# always-on tokens, against the 3,000-token budget
src/sh/claude_validate_always_on_budget.sh
```

### 🕵️ Reviewer brief

At each [regular review](../../docs/target_architecture/design_principles/01_principles.md#-numbers-and-tests), one fresh-context Explore agent gets only this brief, since a primed brief inflates scores. It runs in a scratch worktree of `main` with the audit deleted, so no search can show it the last run's scores:

```text
Score this repo against the Repo section of maintenance/quality/quality_rubrics.md.
Run its measures, score each theme, and cite a path for each judged 🟡 or ❌.
Return the measures, the ten theme scores with a reason each, one line of
feedback per component the transcripts show helping, hindering or going unused,
the Bloat and Over-engineering totals, and up to 5 findings ranked by how much
they would cut, each naming the files involved.
```

### 📊 Where scores live

The [audit](quality_audit.md#️-repo) holds the latest run's scores and the current findings. Its [component feedback](quality_audit.md#-component-feedback) section keeps one row per component that helped, listing each run it helped in, and the latest run's Unused and Hindered rows.
