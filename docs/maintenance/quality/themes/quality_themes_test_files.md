<!-- version: 3.1.0 -->
<!-- created: 2026-10-31 -->
<!-- updated: 2026-11-03 -->
# 🧪 Test Quality Rubric

**Purpose:** how to score the tests for each script out of 10, where 10 means enough tests that stay easy to read, not the most tests.

## 🏷️ Themes

The tests for a script are scored on five themes:

| Theme | What ✅ looks like |
|---|---|
| 🎯 **Core coverage** | Every Must-level behaviour, a core promise of a hook or CI check, has a test (see the [priority scores](../../test_maintenance.md#-priority-scores)) |
| ⚖️ **Leanness** | No duplicate tests, and no cosmetic ones that check only wording or layout |
| 📖 **Clarity** | A newcomer can tell what each test checks from its name and docstring |
| 🧩 **Simplicity** | Short tests in plain pytest, where a harmless change breaks at most one test |
| 🧊 **Reliability** | Isolated, repeatable tests whose failures say what broke |

## 🔢 Scores

Each theme scores ✅ 2 when fully met, 🟡 1 when partly met and ❌ 0 when not met. The five add up to a score out of 10, graded as in the [markdown rubric](quality_themes_markdown_files.md#-themes), so four ✅ and one 🟡 show as **A · 9/10**.

## 📏 How to score

- 🗂️ **Score the script, not each test:** look at all of a script's tests together.
- 🌙 **Rare paths don't cost points:** an untested error that almost never happens isn't a Core coverage gap.
- 🕳️ **Gaps:** name every theme below ✅ in the audit's Gaps column, starting with the theme's name.

### 🔍 Theme-specific rules

- 📖 **Clarity:** parsing, regexes, ordering checks and unexplained inputs need a one-line comment, while plain setup doesn't.
- 🧩 **Simplicity:** a test body over about 12 lines costs a point, since it usually checks more than one thing.
  - **Also costs a point:** mocking the script's internals, or asserting the same message text in several tests.
- 🧊 **Reliability:** run each test in a temporary folder or repo.
  - **Git config:** ignore the user's own settings, so the result is the same on any machine.
  - **Failures:** each assertion message says what broke.

## 🛑 Avoiding over-testing

- 📉 **Could tests:** more `Could` tests than `Must` tests costs a Leanness point, as the [periodic review](../../test_maintenance.md#-periodic-review) explains.
- 🙅 **Lower scores don't mean add tests:** if a new test would cost Leanness or Simplicity points, leave it out.
- ✂️ **Removing tests can raise the score:** deleting a duplicate or cosmetic test improves Leanness.

## 📊 Where scores live

The [tests audit](../audits/quality_audit_test_files.md) holds each script's scores and gaps, and `tests/docs/maintenance/quality/test_quality_audit_test_files.py` fails if a score doesn't add up.
