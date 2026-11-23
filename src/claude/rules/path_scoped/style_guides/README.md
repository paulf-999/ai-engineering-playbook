# 🎨 style_guides

**Purpose:** style guides that load when Claude works on a file matching the guide's `paths:` list, with each topic's standards and team conventions side by side.

- 🧰 **Standards:** a plain name, such as `python.md`, for good practice whatever the team.
- 🏢 **Team conventions:** the same name plus `_team_conventions`, such as `python_team_conventions.md`, with the same `paths:` list, so both load together. Another team replaces these files with its own and keeps the standards.

| File or folder | Loads for | What it covers |
|---|---|---|
| 🌬️ [`airflow.md`](airflow.md), [`airflow_team_conventions.md`](airflow_team_conventions.md) | Python files under `dags/` | DAG principles; this team's layout, helpers, names and values |
| 🖥️ [`bash.md`](bash.md), [`bash_team_conventions.md`](bash_team_conventions.md) | Shell scripts | Shell safety; this team's variable casing and script helpers |
| 🚀 [`cicd/`](cicd/) | Workflows under `.github/workflows/` and Azure Pipelines YAML | GitHub Actions and Azure Pipelines guides, each with this team's conventions |
| 🔵 [`dbt.md`](dbt.md), [`dbt_team_conventions.md`](dbt_team_conventions.md) | dbt models and `dbt_project.yml` | Lineage, docs, tests and materialisation; this team's layers, names and YAML patterns |
| 🏗️ [`infra/`](infra/) | Ansible playbooks and roles, Dockerfiles and `.tf` files | Ansible, Docker and Terraform guides, each with this team's conventions |
| 🐍 [`python.md`](python.md), [`python_team_conventions.md`](python_team_conventions.md) | Python files | Standards beyond PEP 8 and `ruff`; this team's Python choices |
| 🗄️ [`sql.md`](sql.md), [`sql_team_conventions.md`](sql_team_conventions.md) | SQL files | Readable, cost-aware SQL; this team's casing, naming and comma style |
| 🧰 [`utilities/`](utilities/) | Makefiles and `.mmd` files | Makefile and Mermaid guides, each with this team's choices |
