# 📏 Measured: do the Airflow rules change Claude's output?

**Purpose:** what 48 scripted runs showed about whether the Airflow rules make Claude follow them, on 4 common DAG tasks in two sample projects.

> [!NOTE]
> Run on 2026-11-18 with Claude Opus 5.5. It measures whether Claude follows the written rules, using checks the rules' author wrote, not whether the result is a better DAG, which needs people to judge. It's 3 runs per task, on one model, so treat the figures as a signal, not a precise rate. The infra guides are measured separately, for [Terraform](../infra/terraform_rules_measured.md) and [Ansible](../infra/ansible_rules_measured.md).

## 📊 Results

Each task ran 3 times without the rules and 3 times with them, in a fresh copy of a sample project. A script checked each output against the rules. Two samples were used:

- 🪞 **Rich:** one existing DAG already follows the team's layout, and the shared `common.py` documents each helper, so Claude can copy the conventions from the repo.
- 🗂️ **Sparse:** one plain single-file DAG with its SQL inline, and `common.py` lists the helper names only, so the conventions come only from the rules.

| Task | Rich, without | Rich, with | Sparse, without | Sparse, with |
|---|---|---|---|---|
| 📅 **Daily load:** a stage file into a Snowflake table at 06:00 | 100% | 100% | 27% | 100% |
| 🐳 **dbt run:** the `finance` models every weekday | 93% | 100% | 52% | 100% |
| 🔄 **Airbyte sync** every hour, then the `hubspot` dbt models | 98% | 100% | 58% | 100% |
| ✏️ **Edit:** add a rebuild task to the existing DAG | 100% | 100% | 57% | 86% |
| **All checks**, the mean of the 4 task figures | **98%** | **100%** | **49%** | **96%** |

Split by [kind of rule](../../guides/authoring_guide/_rule_classification.md):

| Checks | Rich, without | Rich, with | Sparse, without | Sparse, with |
|---|---|---|---|---|
| 🧰 **Standards:** `schedule`, not `schedule_interval`, no zero retries, a failure callback, no hardcoded schedule, `>>` dependencies, idempotent SQL writes | 100% | 100% | 84% | 100% |
| 🏢 **Team conventions:** the DAG folder with `config.yaml` and `README.md`, the mandatory config keys, `common` helpers, `task_` prefixes, the `# DAG graph` comment, SQL out of `dag.py`, frequency in the name | 96% | 100% | 25% | 97% |

## 🔍 What changed

- 🪞 **The rich sample needed little help:** Claude copied the existing DAG either way. Without the rules, all 3 dbt runs left `data_src` out of `config.yaml`, and DAG names drifted from the guide's patterns, such as `sync_hubspot_hourly` for `parent_dag_hubspot_hourly`.
- 📁 **The sparse sample got the team's layout only with the rules:** without them, no run used the `dags/topics/<topic>/<dag>/` folder or wrote a `config.yaml`, and with them every new DAG did.
- 📄 **Single-file DAGs without the rules:** all 3 daily runs wrote one flat file, with the schedule and SQL hardcoded and no failure callback.
- ❌ **Still missed:** in the sparse edit, all 3 runs with the rules kept the new SQL inline, matching the existing file, though they added the `task_` prefix, the `# DAG graph` comment and a `CREATE OR REPLACE` rebuild.

## 🧪 How it was run

- 🗂️ **Sample projects:** a `your_dags_package/` with `includes/common.py` and one existing `load_orders_daily` DAG, laid out as above for each sample.
- 🤖 **Each run:** a separate `claude -p --safe-mode` session, so nothing else loaded, with read and write tools only and the same prompt in both conditions, ending "Go ahead without asking me questions."
- 📦 **With the rules:** the session's system prompt held what a default install loads when Claude works on a file under `dags/`: `CLAUDE.md`, the always-on rules, and the Airflow, Python, code security and testing rules with their team conventions. The on-demand files sat in a config folder for Claude to read when a rule pointed there. That matches an install closely, but isn't one, since the installer won't run inside Claude Code.
- ✅ **Scoring:** a script read each run's new or changed files and checked them. It can tell whether a rule was followed, but not whether the DAG runs.
- 💰 **Cost:** $9.71 for the 48 runs, with runs that had the rules costing more, since they wrote more files, including tests.
