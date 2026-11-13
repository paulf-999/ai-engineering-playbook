<!-- created: 2026-11-08 -->
# 🏷️ Module metadata and function ordering

**Purpose:** The metadata a module declares after its docstring, and the order its functions go in.

---

## 🏷️ Module metadata

After the docstring and before imports, declare module-level metadata.

### ✅ Standard metadata

```python
"""
Description: YAML config loader with ${ENV_VAR} interpolation
"""

__author__ = "Your Name"
__version__ = "0.1"

import os
import yaml
```

### Metadata fields

- 👤 **`__author__`:** Who wrote/maintains this module (for questions, maintenance)
- 🔢 **`__version__`:** Version number of this module (helpful for tracking API changes)

### ❌ What NOT to include

```python
# ❌ WRONG — belongs in docstring, not metadata
__description__ = "Loads YAML config files"

# ❌ WRONG — belongs in git history, not code
__history__ = "Added in PR #42"

# ❌ WRONG — too granular; commit message has this
__last_modified__ = "2026-08-20"
```

---

## 📐 Function Ordering

**Order functions by call hierarchy, not definition order:**

```python
# ❌ WRONG — helpers defined before main entry point
def _setup_parser(): ...


def _dispatch_command(args): ...


def main(args=None):
    parser = _setup_parser()
    parsed_args = parser.parse_args(args)
    _dispatch_command(parsed_args)


# ✅ RIGHT — entry point first, then functions it calls
def main(args=None):
    parser = _setup_parser()
    parsed_args = parser.parse_args(args)
    _dispatch_command(parsed_args)


def _setup_parser(): ...


def _dispatch_command(args): ...
```

**Why:** Reading the file top-to-bottom tells the story of what the code does. Entry point (main) → supporting functions. Aids maintainability and understanding.
