<!-- created: 2026-08-28 -->
<!-- applies_to: **/*.py -->
<!-- miss_cost: low — modules lose their docstrings and clear interfaces -->
# 📦 Python Module Organisation

**Purpose:** the house rules for laying out a Python module, so it explains itself and its public interface is clear.

## 📐 Module layout

In this order:

```python
"""Migrates connections from the source Airbyte server to the target.

See README.md for usage and requirements.
"""

__author__ = "Your Name"
__version__ = "0.1"

import os

# Default configuration values
DEFAULT_TIMEOUT = 30
DEFAULT_RETRIES = 3


def main(args=None):
    """Run the migration."""
    _dispatch_command(_setup_parser().parse_args(args))


def _setup_parser(): ...
```

- 📝 **Docstring:** one sentence saying what the module is for, not its type or how it works, with one or two more only if a reader needs them.
- 🏷️ **Metadata:** only `__author__` and `__version__`, since dates, history and descriptions belong in git or the docstring.
- 🗂️ **Constants:** group related ones under a comment naming the group, and name magic strings and numbers rather than repeating them inline.
- 🔽 **Function order:** the entry point first, then the functions it calls, so the file reads top to bottom.

## 🔒 Public and private

- 🌐 **Public:** no underscore, for functions other modules import, such as `load_config()`.
- 🔐 **Private:** a leading underscore, for helpers used only in this module, such as `_interpolate()`, so they can change freely.
- ⚖️ **Match the use:** never give the main API an underscore, or leave an internal helper without one.
