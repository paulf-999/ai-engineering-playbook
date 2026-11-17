# 🔧 Pytest Fixtures & Mocking

**Purpose:** Establish fixtures and mocking conventions for isolating code under test and reducing duplication.

---

## 🔧 Pytest fixtures

### `monkeypatch` — Mock environment variables and module attributes

```python
def test_parse_args_defaults(monkeypatch):
    # Override sys.argv for this test
    monkeypatch.setattr("sys.argv", ["airbyte_connection_creator.py"])
    args = parse_args()
    assert args.config is None
```

### `tmp_path` — Create temporary directory for test files

```python
def test_run_dry_run_plans_but_does_not_create(tmp_path):
    inventory_path = tmp_path / "connection_inventory.yaml"
    log_path = tmp_path / "connection_migration_log.yaml"
    inventory_path.write_text("...")
    ConnectionMigrator(client).run(
        apply=False,
        inventory_path=str(inventory_path),
        log_path=str(log_path),
    )
    assert not log_path.exists()
```

---

### Setup helpers

Set up shared test data with the team's helper pattern, in [`_testing.md`](../../../../team_conventions/python/_testing.md).

---

## 🎭 Mocking

**Use `MagicMock` for external dependencies:**

```python
from unittest.mock import MagicMock


def test_migrate_calls_client_create_source(tmp_path):
    client = MagicMock()
    client.create_source.return_value = {"sourceId": "s1"}

    # When we call migrate, it should call client.create_source
    ConnectionMigrator(client).migrate(_entry())

    # Assert the mock was called
    client.create_source.assert_called_once()
```

### Mock assertions — verify interactions

```python
# Assert called exactly once
client.create_source.assert_called_once()

# Assert called with specific arguments
client.create_source.assert_called_once_with({"name": "Salesforce"})

# Assert not called
client.create_source.assert_not_called()
```

**Why:** Mocking isolates the code being tested from its dependencies. Mock assertions verify the code interacts with dependencies correctly.
