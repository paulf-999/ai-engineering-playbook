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
| **Setup helpers** | The team's helper pattern | See `_testing_team_conventions.md` |

## 📚 Read on demand

- [`on_demand/style_guides/python/testing/_naming_structure.md`](testing/_naming_structure.md), in your Claude config directory, for test naming & structure.
- [`on_demand/style_guides/python/testing/_fixtures_mocking.md`](testing/_fixtures_mocking.md), in your Claude config directory, for pytest fixtures & mocking.
- [`on_demand/style_guides/python/testing/_assertions.md`](testing/_assertions.md), in your Claude config directory, for assertions & exception testing.

## 📞 Called by

This rule is invoked by:

- [`rules/on_demand/01_standards/testing.md`](../../01_standards/testing.md), before writing or changing pytest tests.
- [`rules/path_scoped/style_guides/python.md`](../../../path_scoped/style_guides/python.md), before writing or changing pytest tests.
