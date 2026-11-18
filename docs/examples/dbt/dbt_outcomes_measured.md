# 📏 Measured: do the dbt rules make Claude's dbt work better?

**Purpose:** what 24 scripted runs and a blind review showed about whether the dbt rules change the correctness, review score, rework and cost of Claude's work on 4 dbt tasks.

> [!NOTE]
> Run on 2026-11-18 with Claude Opus 5.5, on the same tasks and setup as the [compliance runs](dbt_rules_measured.md). Correctness was checked by building each output on DuckDB and comparing it with known answers. The blind review was by 3 model reviewers, not people, since no independent human reviewer was available. It's 3 runs per task, on one model and one sample project, so treat the figures as a signal, not a precise rate.

## 📊 Results

Each task ran 3 times without the rules and 3 times with them:

| Measure | Without the rules | With the rules |
|---|---|---|
| ✅ **Correct answer** on the first try | 12 of 12 | 11 of 12 |
| 🔧 **Fix turns** needed to get `dbt build` passing | 0 | 1 |
| 📋 **Rule checks** passed, as in the compliance runs | 72% | 96% |
| 👀 **Blind review score**, from 1 to 5 | 3.9 | 4.0 |
| 💰 **Cost** per run | $0.13 | $0.28 |
| ⏱️ **Time** per run | 38s | 57s |

The blind review scores by task, each the mean of 3 reviewers on one output:

| Task | Without | With |
|---|---|---|
| 🧮 **Mart model:** "count each customer's orders" | 4.3 | 4.3 |
| 📥 **Staging model** for a raw `payments` source | 4.0 | 5.0 |
| 📸 **Snapshot** tracking changes to customers | 4.0 | 2.0 |
| 📝 **YAML** for an existing staging model | 3.3 | 4.7 |

## 🔍 What it shows

- 🟰 **Correctness didn't change:** every output in both conditions gave the right answer in the end. These tasks were too simple for the rules to prevent errors.
- 🔧 **The one failed build** used Snowflake's `NUMBER` type, which the SQL standards ask for and DuckDB lacks. It would have built on Snowflake, and one fix turn repaired it.
- 👍 **Staging and YAML scored higher with the rules:** the staging model came with a tested properties file, and the YAML didn't invent a list of order statuses, as the output without the rules did.
- 👎 **The snapshot scored lowest with the rules:** all 3 reviewers gave it 2, calling it over-built. It followed the team's snapshot convention, a `dim_` model read with `ref()`, the `check` strategy and the `WAREHOUSE` schema. The reviewers judged by general dbt practice and didn't know the team's reasons, but the convention may be worth a second look.
- 💰 **The rules cost more:** about twice the cost and 50% more time per task, since Claude reads the extra guides first.
- ⚖️ **Overall:** the rules made the work match the team's conventions and didn't make it more correct. Reviewers who didn't know those conventions rated it about the same.

## 🧪 How it was run

- 🗂️ **Sample project:** the one from the compliance runs, with its raw tables loaded into DuckDB from CSV files with known answers. These are the order counts per customer, 12 payments totalling 380.00, and a second customer file in which 2 customers change and 1 is added.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, with the same prompts and the same rules in the system prompt as the compliance runs.
- ✅ **Correctness:** a script ran `dbt build` on each output, then checked its task:
  - **Mart:** a model maps each customer to the right order count.
  - **Staging:** a model holds all 12 payments and the amount total.
  - **Snapshot:** after the customers change, it has 9 rows, with 2 versions closed.
  - **YAML:** the tests pass on clean data and fail once a duplicate order id and a null customer id arrive.
  - **Checked:** 4 hand-written correct outputs passed and 5 wrong ones failed.
- 🔧 **Fix turns:** when the build failed, the same session got a fixed "fix the failing build" prompt with the build's output, up to 2 times.
- 👀 **Blind review:** one output per task and condition, shuffled and labelled A to H. Each reviewer was a separate `claude -p --safe-mode` session in an empty folder, 2 on Sonnet 5.5 and 1 on Opus 5.5, scoring each output as a pull request: 5 would merge as is, 1 wrong or unusable. The scores were saved before they were matched to the conditions. The rules' style, such as uppercase keywords and leading commas, could still hint at which outputs used them.
- 💰 **Cost:** $4.87 for the 24 runs and $0.23 for the reviews.
