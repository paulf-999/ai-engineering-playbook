# 🧪 Python team conventions: testing

**Purpose:** this team's test helpers and how it groups tests, which the testing guides refer to by role.

## 🔧 Setup helpers

Create underscore-prefixed helper functions to set up test data:

```python
from unittest.mock import MagicMock


def _make_client():
    """Create mock Airbyte client with default return values."""
    client = MagicMock()
    client.base_url = "https://api.example.com:8006"
    client.list_sources.return_value = []
    client.list_destinations.return_value = []
    return client


def _entry(source_system="salesforce_prod", source_server="dc1_source_1"):
    """Create a sample connection entry for testing."""
    return {
        "source_server": source_server,
        "source_system": source_system,
        "source": {"name": "Salesforce Prod", "connector_type": "source-salesforce"},
        "destination": {"name": "Snowflake Raw", "connector_type": "destination-snowflake"},
    }


def test_migrate_creates_source(tmp_path):
    client = _make_client()
    entry = _entry(source_system="salesforce_prod")

    ConnectionMigrator(client).process(entry)
    client.create_source.assert_called_once()
```

**Why:** Underscore-prefixed helpers reduce duplication and make tests more readable.

Use these `_make_*()` helpers in place of custom pytest fixtures.

## 📁 Grouping tests

**Group related tests with comments:**

```python
# --- load_config tests ---


def test_load_config_reads_yaml_file():
    """File is read and parsed correctly."""
    ...


def test_load_config_interpolates_env_vars():
    """${ENV_VAR} references are resolved from environment."""
    ...


def test_load_config_raises_on_missing_env_var():
    """Raises EnvironmentError if ${VAR} is not set."""
    ...


# --- validate_config tests ---


def test_validate_config_passes_valid_config():
    """Valid config passes validation."""
    ...


def test_validate_config_raises_on_invalid_table_descriptor():
    """Raises ValueError for unknown table_descriptor."""
    ...
```

**Why:** Comments make test intent scannable and group related tests visually.
