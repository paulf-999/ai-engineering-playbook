---
paths:
  - "**/dags/**/*.py"
---
# 🌬️ Airflow team conventions

**Purpose:** this team's Airflow layout, helpers, names and values. Another team can replace them with its own, while the standards stay in `airflow.md`.

## 🧱 Basics

- 📁 **DAG as a folder:** each DAG is a folder under `dags/topics/<topic>/` with `dag.py`, `config.yaml` and `README.md`, and shared code lives in `includes/`, not `plugins/`.
- ⚙️ **Config:** every DAG reads its settings from its own `config.yaml`, through `your_dags_package.includes.common`.
- 🔁 **Retries:** `retries=3` and `retry_delay=timedelta(minutes=5)`, set once in `common.get_dag_default_args()`.
- 🏷️ **Task IDs:** prefix tasks with `task_` and TaskGroups with `tg_`, and reuse the generators in `includes/airflow_tasks/` for Airbyte and dbt.
- 🔐 **Shared code:** callbacks, such as `email_notifications`, Connection IDs and Variables, such as `AIRFLOW_ENVIRONMENT_LEVEL`, live in `includes/` utilities.

## 📋 Standard dag.py boilerplate

Every `dag.py` starts the same way. All DAG configuration comes from `config.yaml` — nothing is hardcoded:

```python
from airflow import DAG
from your_dags_package.includes import common  # ruff: isort: skip

# Retrieve default & optional DAG parameters
default_dag_params, optional_dag_params = common.get_default_dag_params(__file__)

# Create the Airflow DAG
with DAG(**default_dag_params) as dag:
    # task definitions here

    # DAG graph
    task_a >> task_b
```

- **`default_dag_params`:** contains `dag_id`, `schedule`, `start_date`, `catchup`, `tags`, `description`, `doc_md`, `default_args`
- **`optional_dag_params`:** contains `dag_inputs` (raw config.yaml), `py_helpers` (from `__py_helpers.py`), and `sql_queries` (from `__sql_queries.py`)
- **DAG graph:** always end the DAG block with a `# DAG graph` comment followed by all task dependency declarations

## 📂 DAG-specific helpers

Store Python callables and SQL queries in dedicated files within the DAG folder, not inline in `dag.py`:

| File | Purpose | Access pattern |
|------|---------|-----------------|
| `__py_helpers.py` | DAG-specific Python functions | `optional_dag_params["py_helpers"].<function_name>` |
| `__sql_queries.py` | DAG-specific SQL queries as strings | `optional_dag_params["sql_queries"].<variable_name>` |

Both files are auto-imported by `common.get_default_dag_params()` if they exist in the DAG folder.

## 🔧 Operators

- 🐳 **dbt runs:** `DockerOperator` with `common.get_common_dbt_docker_params()`.
- 🔄 **Airbyte syncs:** `common.generate_common_airbyte_tasks()`.
- ↪️ **Child DAGs:** `TriggerDagRunOperator` with `common.get_common_trigger_dagrun_params()`.
- 📊 **Dependencies:** declared together under a `# DAG graph` comment at the bottom of the DAG block.

## 📚 Read on demand

- `on_demand/style_guides/airflow_team_conventions/_dag_design.md`, in your Claude config directory, when creating a DAG folder or naming a DAG.
- `on_demand/style_guides/airflow_team_conventions/_dag_configuration.md`, when editing a DAG's `config.yaml`, schedule, tags or default args.
