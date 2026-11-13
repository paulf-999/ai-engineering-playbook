<!-- created: 2026-08-28 -->
# 🔒 Public vs Private Functions

**Purpose:** Establish conventions for distinguishing public API from internal helpers — ensuring module interfaces are clear and changes to internals don't break users.

---

## 🔒 Public vs private functions

Use underscore prefix to signal whether a function is part of the module's public API or an internal helper.

### ✅ Public functions (no underscore)

```python
def load_config(path: str) -> dict:
    """Load YAML config and interpolate ${ENV_VAR} references.

    This is the main API for users of this module.
    """
    ...


def validate_config(config: dict) -> None:
    """Validate config structure and required keys.

    Raises ValueError if config is invalid.
    """
    ...
```

**Why:** Functions without underscore are the module's public interface. Users can rely on these and will be notified of breaking changes.

### ✅ Private functions (with underscore)

```python
def _derive_connection_name(source_system: str, table_descriptor: str) -> str:
    """Internal helper — derive connection name from source and descriptor."""
    ...


def _interpolate(obj) -> dict:
    """Internal helper — recursively interpolate ${ENV_VAR} in strings."""
    ...
```

**Why:** Underscore prefix signals "internal use only." Changes to these are free; users don't depend on them.

### Guideline

- **Public (`no_underscore`):** Functions that other modules import and call
  - Core operations: `load_config()`, `validate_config()`, `migrate_connections()`
  - Filtering/transformation: `get_connection_by_name()`, `apply_connection_names()`
- **Private (`_underscore`):** Helpers used only within this module
  - Setup/initialization: `_make_client()`, `_load_plan()`
  - Processing steps: `_interpolate()`, `_apply_connection_names()`
  - Data construction: `_entry()`, `_write_inventory()`

### ❌ Wrong patterns

```python
# ❌ WRONG — inconsistent: both should be public or both private
def load_config(path):  # public
    ...


def process_config(config):  # public but could be confused with private
    ...


# ❌ WRONG — public function with leading underscore (confuses users)
def _load_config(path):  # looks private but is the main API
    ...
    ...


# ❌ WRONG — helper without underscore (unclear it's internal)
def interpolate_env_vars(obj):  # looks like public API but is just a helper
    ...
```
