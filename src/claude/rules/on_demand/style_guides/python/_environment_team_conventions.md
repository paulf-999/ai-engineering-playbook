# 🐍 Python team conventions: environment and tooling

**Purpose:** this team's Python version, linters, test layout, virtual environment and dependency pinning.

## 📋 Contents

- [🐍 Python version](#-python-version)
- [🔧 Linting & formatting](#-linting--formatting)
- [🧪 Testing](#-testing)
- [📦 Virtual environment](#-virtual-environment)
- [📌 Dependencies](#-dependencies)

---

## 🐍 Python version

The team targets **Python 3.10**. When writing code intended to run on others' machines, always assume Python 3.10.

## 🔧 Linting & formatting

`ruff` is the primary linter and formatter. `flake8` is also used; both enforce 120-char line length.

## 🧪 Testing

**Test file location:** `tests/` directory, co-located with the code being tested. Example: `tests/airbyte_manager/test_config_loader.py` for `src/py/airbyte_manager/helpers/config/config_loader.py`.

**Running tests:**

```bash
pytest                                              # run all tests
pytest --cov=src --cov-report=term-missing         # run with coverage report
```

## 📦 Virtual environment

Use `virtualenv` to isolate project dependencies:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Deactivate with `deactivate`.

## 📌 Dependencies

- Declare all project dependencies in `requirements.txt`.
- Pin direct dependencies exactly using `==` — do not pin transitive (indirect) dependencies.
- When updating a dependency, update the pinned version explicitly in `requirements.txt`.

```text
boto3==1.34.0
requests==2.31.0
```

## 📞 Called by

- [`rules/path_scoped/style_guides/python_team_conventions.md`](../../../path_scoped/style_guides/python_team_conventions.md), when setting up a virtual environment or dependencies.
