# ✅ Best Practices

**Purpose:** the practices for idempotency, retries, error handling, testing and configuration that keep Airflow pipelines reliable. This team's helpers, layout and values are in [`airflow_team_conventions.md`](../../../path_scoped/style_guides/airflow_team_conventions.md).

## 🔄 Idempotency

Every DAG run for a given `logical_date` must produce the same result regardless of re-runs. Design tasks to be safe to retry:

- **SQL writes:** use `INSERT OVERWRITE` or `MERGE` rather than bare `INSERT`
- **Data replacement:** delete and recreate target data for the execution window before writing — never append blindly
- **State assumptions:** do not assume previous run state exists or is accurate

## 📋 Contents

- [📅 Catchup and backfilling](#-catchup-and-backfilling)
- [🔁 Retries and backoff](#-retries-and-backoff)
- [🚨 Error handling](#-error-handling)
- [🧪 Testing](#-testing)
- [🔐 Variables and Connections](#-variables-and-connections)
- [📖 Astronomer anti-patterns](#-astronomer-anti-patterns)

---

## 📅 Catchup and backfilling

- **Central control:** set `catchup=False` once, centrally, per the team's conventions, not in individual DAG files
- **Intentional backfill:** use the Airflow CLI command: `airflow dags backfill -s <start> -e <end> <dag_id>`

---

## 🔁 Retries and backoff

- **Set in defaults:** configure `retries` and `retry_delay` in `default_args` so all tasks inherit consistent behaviour
- **Assume failures:** do not set retries to `0` for production DAGs — network timeouts and API rate limits are common
- **Exponential backoff:** set it on the task itself for tasks that call external APIs, since `default_args` are central:

```python
from datetime import timedelta

task_call_api = PythonOperator(
    task_id="task_call_api",
    python_callable=call_api,
    retry_exponential_backoff=True,
    max_retry_delay=timedelta(minutes=60),
)
```

---

## 🚨 Error handling

- **Use callbacks:** use `on_failure_callback` to notify on task failure — do not rely solely on email alerts
- **Share callbacks:** keep callback functions in the team's shared module, rather than inlining them in DAG files

```python
def notify_on_failure(context: dict) -> None:
    dag_id = context["dag"].dag_id
    task_id = context["task_instance"].task_id
    logical_date = context["logical_date"]
    # send alert (Slack, PagerDuty, etc.)
```

- **Register centrally:** set the shared callback once in the central default args, not in each DAG file

---

## 🧪 Testing

- **Load test:** running each DAG file with `python` must exit cleanly
- **Unit tests:** use `pytest` with Airflow test utilities for task callables
- **Integrity validation:** in CI, `airflow dags list-import-errors` must report no errors, and `airflow dags test <dag_id> <logical_date>` must pass
- **Avoid `depends_on_past=True`:** without explicit justification — it makes testing and backfilling significantly harder

---

## 🔐 Variables and Connections

- **Never hardcode:** environment-specific values (URLs, credentials, schema names) must not be in DAG files
- **Inputs from config:** pass DAG inputs through the DAG's config file, read by the team's helpers
  - **Don't read Variables in dag.py:** do not directly access Airflow Variables in `dag.py`
- **Connections:** use Airflow Connections for external system credentials (databases, APIs, cloud), and reference their IDs in shared utilities, not hardcoded
- **Variables:** use for runtime configuration values that aren't DAG-specific, read with `Variable.get("my_var")` in shared utilities only
- **Secrets backend:** store sensitive values in the configured secrets backend, not plaintext in Airflow metadata

---

## 📖 Astronomer anti-patterns

Additional parse-time and runtime pitfalls to avoid (from [Astronomer best practices](https://docs.astronomer.io/learn/dag-best-practices)):

- **Heavy parse-time computation:** keep DAG files as configuration only — do not perform computation at import time
- **Top-level DB/API calls:** avoid them in DAG files — they run every time the scheduler parses the file
- **Metadata DB overload:** use connection and variable caching to reduce load on the metadata database

## 📞 Called by

- [`rules/path_scoped/style_guides/airflow.md`](../../../path_scoped/style_guides/airflow.md), before changing retries, callbacks, tests or Variables.
