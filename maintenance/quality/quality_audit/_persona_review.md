# 👥 Persona review

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the latest blind review by three likely users, scored against the [persona rubric](../quality_rubrics/_personas.md).

The latest blind persona review, run on 2026-11-18 on Sonnet against commit `3d3c973` by a data engineer (DE), data analyst (DA) and engineering manager (EM). It's the sixth round, after the rule folder folds in [#367](https://github.com/paulf-999/ai-engineering-playbook/pull/367) and [#368](https://github.com/paulf-999/ai-engineering-playbook/pull/368). Each run replaces this page, with earlier runs in git history.

## 🏗️ Over-engineering verdict

No reader calls the installed config over-engineered, but all three find the repo heavy around it:

- 📦 **What you get:** DE says the machinery is "invisible to me", and EM says the complexity is "mostly hidden" from someone who only installs it (all three).
- ⚖️ **What surrounds it:** more than 100 files, three loading tiers, a budget check, audits and design docs (all three). DA says about 15 files are useful to an analyst. Kept by choice: the audits and rubrics.
- 🧑‍🔧 **Who carries it:** EM sees a system someone has to maintain, and wants a named owner for rule changes.
- 🧪 **Evidence:** all three trust the [measured dbt runs](../../../docs/examples/dbt/dbt_rules_measured.md), at 97% of checks with the rules against 71% without. DE and EM note that Airflow and the infra guides are unmeasured.

## 🎯 Shared points

| # | Theme | Raised by | Impact | Status |
|---|---|---|---|---|
| 1️⃣ | **Setup prerequisites and switches**, such as `jq`, a git clone, running the installer in your own terminal, and the `PROJECT=`, `HOOKS=1` and `PREFERENCES=1` combinations | DE, DA, EM | Blocks use | [#374](https://github.com/paulf-999/ai-engineering-playbook/issues/374) |
| 2️⃣ | **The conventions are one team's, with no check that your repo matches**, such as the `prod_analytics/` layout, `mart_` and `pub_` prefixes, and the Airflow `common` module | DE, DA, EM | Confuses | Kept by choice for a standards-only install or local overrides, since the repo starts this team from its own conventions. [#375](https://github.com/paulf-999/ai-engineering-playbook/issues/375) adds a table of what the rules assume |
| 3️⃣ | **Installing changes behaviour beyond style**, such as Intent and Spec sections, phase gates, British spelling and the `.env` deny | DE, DA, EM | Confuses | Kept by choice: the AI-SDLC rule and plan hook stay on for everyone. [#376](https://github.com/paulf-999/ai-engineering-playbook/issues/376) shows the changes before the install step |
| 4️⃣ | **Maintainer material outweighs the product** | DE, DA, EM | Polish | Kept by choice: the audits and rubrics |
| 5️⃣ | **Emoji density in docs and rule files** | DE, DA, EM | Polish | Kept by choice: the markdown style is the maintainer's preference |
| 6️⃣ | **Jargon, with the terms table behind a link and a collapsed block** in `src/claude/README.md` | DE, DA | Confuses | [#377](https://github.com/paulf-999/ai-engineering-playbook/issues/377) |
| 7️⃣ | **No single recommended command**: the README leads with a global install while the guide recommends one repo | DE, EM | Confuses | [#378](https://github.com/paulf-999/ai-engineering-playbook/issues/378) |
| 8️⃣ | **The README never says who the repo is for or what it assumes** | DA, EM | Confuses | [#375](https://github.com/paulf-999/ai-engineering-playbook/issues/375) |
| 9️⃣ | **Airflow and the infra guides are unmeasured**, with no Airflow example | DE, EM | Confuses | [#379](https://github.com/paulf-999/ai-engineering-playbook/issues/379) |
| 🔟 | **Preferences read as one person's taste** | DE, EM | Polish | Kept by choice: personal preferences are opt-in with `PREFERENCES=1` |

Last round's "first five minutes" point is fixed: no reader raised it, and DA cites the try-it prompt in [`getting_started.md`](../../../docs/guides/getting_started.md).

Single-reader asks:

- 🛠️ **DE:** fix the stale `workflows/git.md` link in `src/claude/hooks/README.md`, since fixed in [#370](https://github.com/paulf-999/ai-engineering-playbook/pull/370), and add a link check to CI.
- 📊 **DA:** an analyst path, a business-request-to-SQL example, a way to turn off pauses for quick queries, and a `make all` that doesn't stop at `deps` without a virtualenv.
- 🧭 **EM:** an example where the rules make Claude slower or worse, a one-week pilot plan, an engineer's sign-off on the hooks and installer, and a named owner.

All three readers named the same strengths: the honest measured runs and before-and-after example, the cautious installer with a matching uninstall, the single-repo install for a pilot, and rules that load only when needed.
