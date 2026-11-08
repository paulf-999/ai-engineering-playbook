<!-- version: 1.0.3 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-08 -->
# ✅ Assertions & Exception Testing

**Purpose:** Establish assertion and exception testing conventions for validating expected behaviour.

---

## ✅ Assertions

**Use plain assertions — pytest rewrites them for clear failure messages:**

```python
# ✅ GOOD — pytest shows clear diff on failure
assert args.config == "foo.yaml"
assert isinstance(result, list)
assert not log_path.exists()

# ✅ GOOD — comparison operators
assert len(log["migrations"]) == 1
assert cost < 500

# ✅ Use `in` for membership
assert "created_at" in logged
assert log_path in tmp_path.iterdir()
```

### Assertion messages — explain what went wrong

```python
# ❌ WEAK — no context
assert cost < 500

# ✅ GOOD — explains expected vs actual
assert cost < 500, f"Token cost too high: {cost} (expected <500)"
```

---

## 🚨 Exception testing

**Use `pytest.raises` to assert exceptions:**

```python
import pytest


def test_load_config_raises_on_file_not_found():
    """Verify FileNotFoundError is raised when config file doesn't exist."""
    with pytest.raises(FileNotFoundError):
        load_config("/nonexistent/path.yaml")


def test_load_config_raises_on_invalid_yaml(tmp_path):
    """Verify YAMLError is raised for malformed YAML."""
    bad = tmp_path / "invalid.yaml"
    bad.write_text("key: [unclosed")
    with pytest.raises(yaml.YAMLError):
        load_config(bad)


def test_validate_config_raises_with_pattern_match():
    """Verify ValueError message contains expected text."""
    with pytest.raises(ValueError, match="Invalid table_descriptor"):
        validate_config({"connections": [{"table_descriptor": "invalid"}]})
```

**Why:** Testing exceptions ensures error handling works and provides clear error messages.

---

## ⚡ Quick reference

| Goal | Pattern | Example |
|---|---|---|
| **Test exception raised** | `pytest.raises()` | `with pytest.raises(ValueError, match="pattern"):` |
| **Verify assertion message** | Use `assert` with message | `assert x < 10, f"Expected x < 10, got {x}"` |
