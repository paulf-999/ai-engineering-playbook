# 🤖 tests/src/claude

**Purpose:** what each test of the Claude config in `src/claude/` checks.

| Test | What it checks |
|---|---|
| ✅ [test_hook_enforcement_done_checks.py](test_hook_enforcement_done_checks.py) | The done checks hook stops Claude once to run the repo's checks after files change |
| 🗂️ [test_hook_enforcement_plan_sections.py](test_hook_enforcement_plan_sections.py) | The plan sections hook blocks a plan that has no Intent or Spec heading |
| 📐 [test_rules_structure.py](test_rules_structure.py) | Every rule file under `src/claude/rules/` meets the rule template's structural gates |
