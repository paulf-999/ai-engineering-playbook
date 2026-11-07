---
<!-- version: 2.0.1 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-07 -->
<!-- applies_to: **/*.py, **/*.sh, **/*.sql, **/*.js, **/*.ts -->
<!-- miss_cost: high — code ships with a secret or an injection hole -->
<!-- loading: path-scoped — loads with code files -->
paths:
  - "**/*.py"
  - "**/*.sh"
  - "**/*.sql"
  - "**/*.js"
  - "**/*.ts"
---
# 🛡️ Code security

**Purpose:** secure coding standards that load whenever a code file is open.

- 🔑 **Secrets from the environment:** load secrets from environment variables or a secret manager, and keep `.env` files in `.gitignore`.
- 🛡️ **Validate at boundaries:** check user input, API responses and ingested files where they enter the system.
- 🧱 **No queries built from input:** use parameterised queries, and never build SQL or shell commands from raw input.
- 📦 **Dependencies:** pin versions, and check for known vulnerabilities before adding one, such as with `pip-audit`.
- 🙈 **Logs:** never log credentials, tokens or personal data, and flag any code that handles personal data.
