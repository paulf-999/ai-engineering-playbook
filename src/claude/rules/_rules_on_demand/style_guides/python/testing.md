<!-- version: 1.1.5 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-11 -->
<!-- applies_to: **/test_*.py, **/conftest.py -->
<!-- miss_cost: medium — tests miss intended behaviour and need rewriting -->
# 🧪 Python Testing Conventions

**Purpose:** Establish pytest conventions for test naming, structure, fixtures, mocking, and assertions — preventing testing debt and validating intended behaviour.

---

## ⚡ Quick reference

| Goal | Pattern | Example |
|---|---|---|
| **Mock a dependency** | `MagicMock()` | `client = MagicMock(); client.create.return_value = {...}` |
| **Verify mock was called** | `assert_called_once()` | `client.create.assert_called_once()` |
| **Test exception raised** | `pytest.raises()` | `with pytest.raises(ValueError, match="pattern"):` |
| **Use temp files** | `tmp_path` fixture | `path = tmp_path / "file.txt"; path.write_text(...)` |
| **Override env var** | `monkeypatch` fixture | `monkeypatch.setenv("VAR", "value")` |
| **Setup helpers** | `_make_*()` functions | `def _make_client(): return MagicMock()` |

## 📚 Read on demand

- **Read on demand:** `_rules_on_demand/style_guides/python/testing/_naming_structure.md`, in your Claude config directory, for test naming & structure.
- **Read on demand:** `_rules_on_demand/style_guides/python/testing/_fixtures_mocking.md`, in your Claude config directory, for pytest fixtures & mocking.
- **Read on demand:** `_rules_on_demand/style_guides/python/testing/_assertions.md`, in your Claude config directory, for assertions & exception testing.
