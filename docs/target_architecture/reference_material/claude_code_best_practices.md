<!-- version: 1.1.0 -->
<!-- created: 2026-11-03 -->
<!-- updated: 2026-11-03 -->
# 🛠️ Claude Code docs: Best practices

**Purpose:** what Anthropic's best-practices page for Claude Code recommends on guiding, checking and enforcing Claude's work, and what that means for this repo.

It's one of the summaries listed in this repo's [reference material](README.md).

## 📋 Executive Summary

- 📘 **What it is:** the official page on what to set up when Claude Code's defaults aren't enough.
- 💡 **Core idea:** an instruction is either guidance Claude weighs, such as `CLAUDE.md` or a skill, or a rule Claude Code always applies, such as a hook.
- ⚖️ **Default:** let Claude decide, and enforce only what must always or never happen.
- 🎯 **For this repo:** it backs enforcing what must hold, and adds the converse: remove hooks that only hold preferences.

## 🔗 Source

- 📘 **Page:** [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices), Claude Code docs, Anthropic.
- 📅 **Version:** the page shows no date or version, so cite the section heading and the capture date.
- 🗓️ **Captured:** 2026-11-03, after reading the whole page, which may have changed since, so recheck it before citing a detail.

## 📋 The docs say

The page makes these points, by section:

- ⚖️ **Two kinds of instruction:** guidance gives "no *guarantee*" Claude follows it, while hooks (scripts run at set points) and deny rules (settings that block an action) apply "every time" ("Deterministic and non-deterministic instructions").
- 🔁 **Moving between them:** a `CLAUDE.md` line that keeps needing emphasis belongs in a hook, and a hook holding only a preference should be deleted (same section).
- 🔍 **What to write down:** only what Claude can't find by reading the repo, such as test commands and decisions made elsewhere ("Tell Claude what it can't see").
- ✅ **Give it a check:** a pass-or-fail check lets Claude fix its own work, at its strictest a hook that blocks finishing until it passes ("Give Claude a check to run").
- 🧹 **Keep enforcement small:** every hook and deny rule sometimes fires wrongly, so "at forty of them, most are probably preferences" ("Choose who a rule applies to").

### ➕ Also on the page

- 🔎 **Scope reviews:** a reviewer asked to find problems "will always find *something*", so tell it to skip style ("Review against your spec").

## 🎯 What it means for this repo

This section is this repo's reading, not the page's, and the principles named are in this repo's [design principles](../design_principles/01_principles.md):

- 🔒 **Enforcement:** it backs "Enforce what must hold" in Anthropic's own words.
- 🗑️ **Retiring hooks:** under "Retire what doesn't pay", each regular review could ask whether every hook holds a real "never".
- 🌱 **Minimal by default:** if Claude reads the repo itself, `CLAUDE.md` needs only what isn't there.
- ⚠️ **Limit:** it's vendor advice with no measured results, so weigh it as guidance, not evidence.
