# 📊 Quality audit

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest bloat and over-engineering scores for the repo as a whole, its findings and component feedback, from each regular review, plus the latest persona review.

Each run follows the [repo rubric](quality_rubrics/_repo.md): one fresh-context reviewer runs its measures and scores its themes, and this page keeps the latest run's scores, with earlier runs in git history. Tests and rules are checked against their checklists instead, with findings going to GitHub issues.

## 🎈 Bloat

| Date | Proportionality | Evidence of need | Single source | Always-on headroom | Placeholders | **Bloat** |
|---|---|---|---|---|---|---|
| 2026-11-16 | ✅ 2 | ✅ 2 | ❌ 0 | ✅ 2 | ✅ 2 | **8/10** |

## 🏗️ Over-engineering

| Date | Cross-file consistency | Upkeep cost | Process weight | Simplest mechanism | Built for today | **Over-engineering** |
|---|---|---|---|---|---|---|
| 2026-11-16 | 🟡 1 | ✅ 2 | ✅ 2 | 🟡 1 | ✅ 2 | **8/10** |

## 🔍 Why the latest scores

The blind run of `main` at `6008ce9`, after [#301](https://github.com/paulf-999/ai-engineering-playbook/pull/301), [#302](https://github.com/paulf-999/ai-engineering-playbook/pull/302) and [#305](https://github.com/paulf-999/ai-engineering-playbook/pull/305) fixed the last run's findings and [#307](https://github.com/paulf-999/ai-engineering-playbook/pull/307) widened the judged bands and defined one issue per fact, rule or mechanism. It's the first run under that rubric, so it's the new baseline rather than comparable with earlier runs. It ran as `claude -p --safe-mode` in a fresh clone, with each theme below ✅ and what would raise it:

| Theme | Why it scores this | To improve it |
|---|---|---|
| 🎯 **Single source** | 6 duplicates: the 15-line plan threshold, the 3-phase gate and the 3,000-token budget restated in `src/claude/README.md`, the PR template's default lines copied into `git_validate_pr_description.sh` and its test, the 40-line child minimum, and the hyphenated skill and agent names | Findings 1 and 3 |
| 🔗 **Cross-file consistency** | 4 contradictions: what the budget covers in `src/claude/README.md:32`, the always-on exemption missing from `rule.md.template:20`, `docs/README.md:10` placing tests in `maintenance/`, and `02_evaluation_criteria.md` leaving out Cost and Rule size yet listing them | Findings 1 to 4 |
| 🪜 **Simplest mechanism** | 3: manual Cost and Rule size checkboxes the hooks and tests already check, commitlint on both commits and the PR title, and the PR description check | Finding 2 |

Measures: 38 support files against 93 product files, 8 of the last 50 commits (16%) on upkeep, 5 `maintenance/` files besides the audit, no placeholders, and always-on context at about 2,244 of 3,000 tokens (74.8%).

## 🎯 Current findings

The latest run's findings, ranked by how much each would cut. Each run replaces this list, and the next PRs work through it.

1. ✂️ **Link the restated numbers:** point `src/claude/README.md:32-35` to `sdlc_workflow.md` and `01_principles.md` for the 15-line, 3-phase and 3,000-token figures, which also fixes its budget-scope contradiction.
2. 🪜 **Drop the manual checkboxes:** remove Cost and Rule size at `02_evaluation_criteria.md:32-33`, which pre-commit and the tests already check, and which line 9 says the table leaves out.
3. 🧹 **One home for two facts:** have `git_validate_pr_description.sh` read its default lines from `pull_request_template.md`, and point `rule.md.template:20` and `authoring_guide.md:11` to the 40-line minimum in `test_rules_structure.py`, which fixes the template's missing exemption.
4. 🔗 **Fix the tests location:** `docs/README.md:10` says `maintenance/` holds the tests, which live in `tests/`.

The run also proposed removing the agent and skill templates and their guides, dropping commitlint's commit-msg hook and linking the numbers in `README.md:33`. These are left out because the templates are kept for porting, the git checks are kept by choice, and the README stays a plain-worded entry page.

## 💬 Component feedback

Rows are sorted by path. Each component that helped has one row, and each review adds its PR to that row, or adds a row, but replaces the Unused and Hindered rows, since those are what it acts on.

### ✅ Helped

| Component | Helped in | Latest evidence |
|---|---|---|
| [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught a real missing `yaml` dependency |
| [`CLAUDE.md`](../../CLAUDE.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Its Done means had Claude run the tests in 42 sessions and pre-commit in 40 |
| [`maintenance/quality/quality_rubrics/_personas.md`](quality_rubrics/_personas.md) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300) | Produced concrete outside findings in 21 sessions |
| [Portable paths](../../docs/guides/authoring_guide.md#-portable-paths) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 5 times |
| [`src/claude/hooks/hook_enforcement_plan_sections.sh`](../../src/claude/hooks/hook_enforcement_plan_sections.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Blocked 12 sessions' plans, each rewritten properly, though also some trivial non-repo plans |
| [`src/claude/rules/always_on/01_standards/conduct/writing_style.md`](../../src/claude/rules/always_on/01_standards/conduct/writing_style.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `_markdown_layout.md` was read on demand in 8 to 11 sessions |
| [`src/claude/rules/always_on/01_standards/workflows/sdlc_workflow.md`](../../src/claude/rules/always_on/01_standards/workflows/sdlc_workflow.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Followed whenever the plan hook pointed to it |
| [`src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md`](../../src/claude/rules/on_demand/01_standards/claude_config/guiding_principles.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Read, with the testing rules, before writing a new hook and its tests |
| [`src/claude/rules/on_demand/01_standards/conduct/reporting.md`](../../src/claude/rules/on_demand/01_standards/conduct/reporting.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Read about 6 times |
| [`src/claude/rules/on_demand/01_standards/workflows/git.md`](../../src/claude/rules/on_demand/01_standards/workflows/git.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/on_demand/03_preferences/working_files/_saving_plans.md`](../../src/claude/rules/on_demand/03_preferences/working_files/_saving_plans.md) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168), [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161), [#149](https://github.com/paulf-999/ai-engineering-playbook/pull/149), [#143](https://github.com/paulf-999/ai-engineering-playbook/pull/143) | Read on demand in 8 to 11 sessions |
| [`src/claude/rules/path_scoped/01_standards/code_security.md`](../../src/claude/rules/path_scoped/01_standards/code_security.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/claude/rules/path_scoped/01_standards/style_guides/python.md`](../../src/claude/rules/path_scoped/01_standards/style_guides/python.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 13 sessions, where Python files were open |
| [`src/claude/rules/path_scoped/01_standards/testing.md`](../../src/claude/rules/path_scoped/01_standards/testing.md) | [#161](https://github.com/paulf-999/ai-engineering-playbook/pull/161) | Loaded in about 14 sessions, where matching files were open |
| [`src/sh/claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#168](https://github.com/paulf-999/ai-engineering-playbook/pull/168) | Caught one overrun at about 3,887 tokens |
| [`src/sh/git/git_validate_branch_name.sh`](../../src/sh/git/git_validate_branch_name.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246), [#172](https://github.com/paulf-999/ai-engineering-playbook/pull/172) | Caught `docs/` and `refactor/` prefixes and commits on `main`, with one false fire on a detached HEAD |
| [`src/sh/git/git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Never failed, but moved large PRs onto `release/` branches |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [#300](https://github.com/paulf-999/ai-engineering-playbook/pull/300), [#264](https://github.com/paulf-999/ai-engineering-playbook/pull/264), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | Caught bad PR descriptions locally and in CI |
| [`tests/`](../../tests/) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308), [#246](https://github.com/paulf-999/ai-engineering-playbook/pull/246) | `make test` found local failures in 21 sessions before any PR |

### ⚠️ Unused or hindered, latest run

| Component | Run | Effect | Evidence |
|---|---|---|---|
| [`.github/workflows/pip_audit.yml`](../../.github/workflows/pip_audit.yml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Unused | Never caught anything in a transcript |
| [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Hindered | checkmake linted `makefile.md` as a Makefile, now excluded, and blocked removing `clean` |
| [`Makefile`](../../Makefile) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Unused | `make clean`, `make uninstall` and `make help` were almost never run |
| [`src/claude/hooks/hook_enforcement_done_checks.sh`](../../src/claude/hooks/hook_enforcement_done_checks.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Unused | Never fired in any session |
| [`src/claude/rules/on_demand/01_standards/`](../../src/claude/rules/on_demand/) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Unused | `_todo_logging.md`, `turn_budgets.md`, `claude_naming_patterns.md` and the domain style guides were never read for real work |
| [`src/claude/rules/path_scoped/01_standards/`](../../src/claude/rules/path_scoped/) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Hindered | Their old `applies_to:` frontmatter loaded them every session, about 7,850 extra tokens, and the non-Python rules never loaded |
| [`src/sh/claude_install_config.sh`](../../src/sh/claude_install_config.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Hindered | Refused twice to run inside Claude Code, as designed, and cost a turn each time |
| [`src/sh/claude_report_context_cost.sh`](../../src/sh/claude_report_context_cost.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Hindered | Failed 8 times as out of date, each fixed by regenerating and recommitting |
| [`src/sh/git/git_validate_pr_description.sh`](../../src/sh/git/git_validate_pr_description.sh) | [#308](https://github.com/paulf-999/ai-engineering-playbook/pull/308) | Mixed | Caught leftover template text, but failed CI on a 6-versus-5 bullet nit |

## 👥 Persona review

The latest [blind persona review](quality_rubrics/_personas.md), run on 2026-11-16 against commit `f5fdf5d` by a data engineer (DE), data analyst (DA) and engineering manager (EM). It's the first round with readers matched to the team's skill levels and given a goal each, in [#303](https://github.com/paulf-999/ai-engineering-playbook/pull/303), so it isn't comparable with earlier rounds. Each run replaces this section, with earlier runs in git history.

### 🏗️ Over-engineering verdict

No reader calls the delivered config over-engineered, but all three say the repo is much heavier than what they'd use:

- 📦 **What you get:** a lean core, about 2,000 always-on tokens, rules that load only when needed, and a careful installer (all three).
- ⚖️ **What surrounds it:** of 149 files, DE would use about 12 and DA about 8, and DE says the rest "isn't in my way; I just skip it".
- 📍 **Where:** design docs, `maintenance/` and `tests/`, where all three stopped reading, and the jargon from them, such as tiers, guards and phase gates (DA, EM).
- 🧪 **Effort against evidence:** EM says the effort "far outweighs the evidence that it works", and DA calls it "high complexity for a modest, unproven payoff".

### 🎯 Shared points

Each point two or more readers raised, ranked by how many raised it, then by impact:

| # | Theme | Raised by | Impact | Status |
|---|---|---|---|---|
| 1️⃣ | **Another team's dbt and Airflow conventions install as rules, with no way to customise them that survives a reinstall** | DE, DA, EM | Blocks use | Open; labelled as examples in [#298](https://github.com/paulf-999/ai-engineering-playbook/pull/298), which all three found too easy to miss |
| 2️⃣ | **No "which install is right for me" path, such as a project install for a dbt repo** | DE, DA, EM | Blocks use | Open |
| 3️⃣ | **The dbt example breaks its own rules: uppercase CTEs, a `KEY` on an aggregate, an `MD5` stand-in and no YAML** | DE, DA, EM | Confuses | [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) |
| 4️⃣ | **The reply style should be opt-in, not opt-out** | DE, DA, EM | Confuses | Opt-in with `PREFERENCES=1` |
| 5️⃣ | **The data guides are unproven** | DE, DA, EM | Confuses | [#281](https://github.com/paulf-999/ai-engineering-playbook/issues/281) |
| 6️⃣ | **Nothing for analysts, such as turning a business request into SQL or a dbt model** | DA, EM | Blocks use | Open |
| 7️⃣ | **Undefined jargon, such as always-on, path-scoped, hooks and phase gates** | DA, EM | Confuses | Open |

Single-reader asks:

- 🛠️ **DE:** selective installs by guide, dbt globs that miss `.yaml`, `macros/` and `snapshots/`, and the dbt and Airflow versions the guides assume.
- 📊 **DA:** say the planning rules don't slow down a single query, and the four dbt layers differ from dbt Labs' three.
- 🧭 **EM:** tagged releases for a pinned version, and a two-week trial in one dbt repo before any team rollout.

All three readers named the same strengths: the installer, rules that load only when needed, and the repo's honesty about itself.
