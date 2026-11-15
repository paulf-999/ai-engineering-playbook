# 💰 Budget and guards

**Purpose:** the cap on what loads into every session, and the checks that protect the design. It's part of the [target architecture](README.md).

## 💰 Always-on budget

- 📏 **Measure:** the tokens, the units Claude reads text in, that load into every session, estimated as total characters ÷ 4, leaving out HTML comments, which Claude Code strips.
- 📂 **Counted:** the `CLAUDE.md` files and their `@` imports, rules with no `paths:` setting, and skill and agent descriptions, in both the project's `.claude/` and the global config in `src/claude/`.
- 🚫 **Not counted:** auto memory's `MEMORY.md`, which Claude Code also loads every session but keeps on each machine, outside the repo, and caps at 200 lines or 25KB.
- 🚧 **Ceiling:** set in the [principles' numbers](design_principles/01_principles.md#-numbers-and-tests), and raised only by a PR that links logged evidence.

## 🛡️ Design guards

These checks protect the design itself, alongside the repo's other [CI checks](../../.github/workflows/ci.yml):

| Guard | Fails when | How it runs |
|---|---|---|
| 💰 **Always-on budget** | The estimate exceeds the ceiling | [`claude_validate_always_on_budget.sh`](../../src/sh/claude_validate_always_on_budget.sh), as a pre-commit hook that CI also runs |
| 📏 **Rule size** | A rule runs over 110 lines, not counting comments or frontmatter | [`test_rules_structure.py`](../../tests/src/claude/test_rules_structure.py), in the pytest run that CI also runs |
| 📦 **PR size** | A PR changes more files than its limit allows, except on a `release/` branch | Runs [`git_validate_num_file_changes.sh`](../../src/sh/git/git_validate_num_file_changes.sh) |

- 📄 **Context size:** the Rule size guard caps every rule at 110 lines, including on-demand and path-scoped rules, so a single read stays at about 2 pages, far below the 20-page standards document [DORA warns](reference_material/core/dora_ai_capabilities.md#-findings-worth-carrying-forward) is too much for a model. On-demand files need no limit of their own.
