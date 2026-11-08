<!-- version: 1.2.0 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-08 -->
# 📝 Module Docstrings

**Purpose:** Establish module docstring format for self-documenting modules.

---

## 📝 Module docstrings

Every module must have a docstring at the top describing its purpose. Place it before imports and `__author__`/`__version__` metadata.

### Format

**Module docstrings must follow progressive disclosure**:

- **Opening line:** One-sentence summary of module purpose
- **Details:** Reserve for README, separate docs, or code comments — NOT the module docstring

```python
"""
[One-sentence purpose — this is sufficient]
"""
```

**Only add sections if absolutely necessary for critical context:**

```python
"""
[One-sentence purpose]

[Optional: 1-2 sentences of critical context OR reference external docs]
"""
```

**Never include** in module docstrings:

- ❌ Usage examples or instructions (belongs in README.md)
- ❌ Requirements or setup steps (belongs in README.md)
- ❌ Detailed workflow steps (document this in code comments or external docs)
- ❌ Dates (belongs in git history, not code)
- ❌ Author info (use `__author__` metadata instead)

### ✅ Good examples

**Correct — brief, discoverable:**

```python
#!/usr/bin/env python3
"""YAML config loader with ${ENV_VAR} interpolation."""

__author__ = "Your Name"
__version__ = "0.1"

import yaml
```

**Correct — brief with critical context:**

```python
#!/usr/bin/env python3
"""Migrates connections from source to target Airbyte server.

See README.md for usage and requirements.
"""

__author__ = "Your Name"
__version__ = "0.1"
```

---

### ❌ WRONG — Too verbose (violates progressive disclosure)

```python
#!/usr/bin/env python3
"""
Description: Airbyte connection migrator — migrates connections from source to target server
             based on migration plan CSV.
Date created: 2026-07-03

Requirements:
    Environment variables must be set in .env
    See README.md for setup instructions
"""
```

**Problem:** Module docstrings should be brief and discoverable via `help(module)` or IDE tooltips. Workflow, requirements, and usage belong in **README.md or separate documentation**, not in the module docstring.

### ❌ Weak opening lines

```python
# ❌ WRONG — too generic: it names the module's type, not what it does
"""Config loader module"""

# ❌ WRONG — implementation detail: it says how, not what it's for
"""This module loads YAML files and parses them"""
```
