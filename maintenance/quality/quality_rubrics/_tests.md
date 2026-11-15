# 🧪 Tests

> [!NOTE]
> **For repo maintainers only:** you don't need this page to install or use the Claude Code instructions.

**Purpose:** the checklist a reviewer runs on each script's tests at a regular review, as part of the [quality rubrics](../quality_rubrics.md).

## ✅ Checklist

Check a script's tests together, rather than one test at a time:

| Check | What passing looks like |
|---|---|
| 🎯 **Core coverage** | Every Must-level behaviour, a core promise of a hook or CI check, has a test (see the [priority scores](../../test_maintenance.md#-priority-scores)) |
| ⚖️ **Leanness** | No duplicate tests, and no cosmetic ones that check only wording or layout |
| 📖 **Clarity** | A newcomer can tell what each test checks from its name and docstring |
| 🧩 **Simplicity** | Short tests in plain pytest, where a harmless change breaks at most one test |
| 🧊 **Reliability** | Isolated, repeatable tests whose failures say what broke |

## 📏 How to check

- 🌙 **Rare paths aren't gaps:** an untested error that almost never happens isn't a Core coverage finding.
- 📖 **Clarity:** parsing, regexes, ordering checks and unexplained inputs need a one-line comment, while plain setup doesn't.
- 🧩 **Simplicity:** a test body over about 12 lines usually checks more than one thing, as does mocking the script's internals or asserting the same message text in several tests.
- 🧊 **Reliability:** each test runs in a temporary folder or repo, ignores the user's own git config, and says what broke in each assertion message.
- 🙅 **Don't add tests to pass:** a finding is fixed by changing or deleting a test, never by adding one that would itself fail Leanness or Simplicity.

## 🕵️ Reviewer brief

Each [periodic review](../../test_maintenance.md#-periodic-review) checks every script whose tests changed since the last one. One fresh-context reviewer on Sonnet gets only this brief, since a primed brief goes easier on the work:

```text
Check each script listed after this brief against maintenance/quality/quality_rubrics/_tests.md.
Read each script with its tests, and run them to check they pass.
Return one finding per failed check: the script, the check, the test and line, and the fix.
```

## 🎫 Where findings go

Open a GitHub issue for each finding the review doesn't fix in its own PR, so the fixes are tracked rather than recorded as scores.
