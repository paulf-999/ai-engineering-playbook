<!-- created: 2026-08-28 -->
# 📝 Module Docstrings

**Purpose:** how to write a module's docstring, so `help(module)` and IDE tooltips show what it's for.

## 📐 Format

Every module starts with a docstring, before its imports and its `__author__` and `__version__` metadata.

- 1️⃣ **Opening line:** one sentence saying what the module is for, not what type it is or how it works.
- ➕ **Context:** add one or two sentences only if a reader needs them, or point to the README.
- 🚫 **Leave out:** usage, setup steps, workflow, dates and authors, which belong in the README, comments, git or `__author__`.

## ✅ Example

```python
"""Migrates connections from source to target Airbyte server.

See README.md for usage and requirements.
"""
```

Weak opening lines, by contrast, are `"""Config loader module"""`, which names its type, and `"""This module loads YAML files and parses them"""`, which says how it works.
