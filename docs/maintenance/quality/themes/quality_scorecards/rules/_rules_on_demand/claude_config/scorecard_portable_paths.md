<!-- version: 1.0.0 -->
<!-- created: 2026-11-05 -->
<!-- updated: 2026-11-05 -->
# Quality Scorecard — portable_paths.md

**Date Created:** 2026-11-05
**Date Updated:** 2026-11-05

**Overall score:** 7.5/10

**Recommended improvements:**

- Replace "as the old config's hooks and tests did" with one dated, named incident, or link to the commit or issue that records it.
- Settle the clash between "never hard-code a `~/.claude` path" (line 11) and "using `~/.claude` only as the fallback" (line 12), for example "never hard-code `~/.claude` except as the `CLAUDE_CONFIG_DIR` fallback".
- Extend the shell snippet so it reaches the config root, not just the script's own folder, or say which folder to resolve from.
- Narrow `applies_to` from `**/*.sh, **/*.py` to the config's hook, script and test globs, so the usage audit doesn't count every Python or shell session.

| Dimension | Score | Date Updated | Notes |
|---|---|---|---|
| **Clarity** | 7/10 | 2026-11-05 | • 🎯 **Actionable:** four concrete instructions, one each for the general rule, Python, shell and guard clauses<br>• ⚠️ **Mixed message:** line 11 says "never hard-code a home folder, username or `~/.claude` path", but line 12 then prescribes `~/.claude` as the fallback<br>• ⚠️ **Incomplete shell recipe:** line 13 resolves the script's own folder, not the config root, so a hook in `hooks/` still has to work out `..` itself |
| **Complexity** | 8/10 | 2026-11-05 | • 🧮 **Raw complexity 2:** Concepts 2 (four behaviours) + Scope 0 (single file) + Dependencies 0 + Prerequisites 0<br>• ⚠️ **Formula not found:** the rubric cites a complexity formula in `authoring_guidelines.md`, but no file under `src/claude/rules/_rules_on_demand/claude_config/` mentions "complexity", so this uses the four parts the rubric names |
| **Evidence of Need** | 6/10 | 2026-11-05 | • 🔗 **Claimed, not recorded:** line 15 says hard-coded paths failed "as the old config's hooks and tests did", but names no date, file or incident<br>• 🔍 **src/claude_old/:** the earlier copy has the same five bullets and the same vague Why line, so no incident record is kept there<br>• 🔍 **Git history:** no commit message mentions portable or hard-coded paths, and the repo has no other mention of hard-coded home paths<br>• ⚠️ **No local need:** `src/claude/` has no `hooks/` or `scripts/` today, so nothing in the repo shows the rule's audience needing it |
| **Token Cost Justification** | N/A | 2026-11-05 | • 🎯 **Lazy:** lives in `_rules_on_demand/` with `loading: lazy`, reached through `guiding_principles.md` line 30, and costs about 189 tokens per `docs/maintenance/context_cost.md` |
| **Structural Compliance** | 8/10 | 2026-11-05 | • ✅ **Header and opening:** version, created, updated, applies_to, miss_cost and a `loading: lazy` that matches the folder, then an emoji H1 and a one-line Purpose<br>• ✅ **Layout:** 16 lines, 5 bold-keyword bullets with emojis (at the 5-item cap), one sentence each<br>• ⚠️ **Not proven:** `tests/src/claude/test_rules_structure.py` is staged but uncommitted, and no recorded run shows this file passing<br>• ⚠️ **Broad applies_to:** `**/*.sh, **/*.py` matches every shell and Python file anywhere, wider than the Purpose's "hooks, scripts and tests for Claude's config" |
| **Currency** | 8/10 | 2026-11-05 | • ✅ **Consistent:** the `CLAUDE_CONFIG_DIR`, or `~/.claude` when unset, fallback matches `src/claude/CLAUDE.md` line 50<br>• ✅ **No dead references:** the rule names no file or command that's missing<br>• ⚠️ **Practice unclear:** repo tests resolve paths from `REPO_ROOT` in `tests/_paths.py`, not from `CLAUDE_CONFIG_DIR`, and the rule doesn't say whether "tests" covers them<br>• ⚠️ **History in prose:** "as the old config's hooks and tests did" points to a past state the reader can't check |
| **Test Coverage** | 8/10 | 2026-11-05 | • 🧪 **Structural test exists:** `tests/src/claude/test_rules_structure.py` checks the header, H1, Purpose, length, headings, list size and usage lines for every rule, with tests that prove each check can fail<br>• ✅ **No content test needed:** the rule records no specific incident, so the rubric's content-regression clause doesn't apply<br>• ⚠️ **Unrun:** the test file is staged but not committed, and no run is recorded |
| **Overall** | **7.5/10** | 2026-11-05 | • 💪 **Lean:** a 16-line rule with concrete, language-specific instructions, loaded only on demand<br>• ⚠️ **Weak evidence:** the Why line claims past failures that nothing in the repo records<br>• ⚠️ **Wording:** "never hard-code `~/.claude`" clashes with using it as the fallback |

## 🔗 Related files

- `src/claude/rules/_rules_on_demand/claude_config/portable_paths.md` — the rule being scored
- `src/claude_old/rules/_rules_on_demand/claude_config/portable_paths.md` — Evidence of Need (earlier copy, same Why line)
- `src/claude/rules/_rules_on_demand/claude_config/guiding_principles.md` — Token Cost Justification (the read-on-demand pointer, line 30)
- `src/claude/rules/_rules_on_demand/claude_config/authoring_guidelines.md` — Complexity (cited formula not found)
- `src/claude/CLAUDE.md` — Currency (the matching `CLAUDE_CONFIG_DIR` fallback)
- `docs/maintenance/context_cost.md` — Token Cost Justification (~189 tokens)
- `tests/_paths.py` — Currency (how repo tests resolve paths)
- `tests/src/claude/test_rules_structure.py` — Structural Compliance and Test Coverage
