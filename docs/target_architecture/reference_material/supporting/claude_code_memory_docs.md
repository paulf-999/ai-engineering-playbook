# 🧠 Claude Code docs: How Claude remembers your project

**Purpose:** what Anthropic's Claude Code docs say about the files Claude loads into every session, and what that means for this repo's always-on budget.

It's one of the summaries listed in this repo's [reference material](../README.md).

## 📋 Executive Summary

- 📘 **What it is:** the official page on `CLAUDE.md` and rules files, the instructions Claude Code loads for itself.
- 💡 **Core idea:** these files are context Claude reads, not settings Claude Code enforces.
- 📏 **Size:** keep each `CLAUDE.md` under 200 lines, and use path-scoped rules for anything that matters to only part of a repo.
- 🎯 **For this repo:** it backs the [always-on budget](../../README.md#-always-on-budget), a cap on the text loaded into every session, and shows what the cap must count.

## 🔗 Source

- 📘 **Page:** [How Claude remembers your project](https://code.claude.com/docs/en/memory), Claude Code docs, Anthropic.
- 📅 **Version:** the page shows no date or version, so cite the section heading and the capture date.
- 🗓️ **Captured:** 2026-11-03, after reading the whole page.

## 📋 The docs say

The page makes these points, by section:

- 🧭 **Context, not enforcement:** Claude "treats them as context, not enforced configuration", so blocking an action needs a hook, a script Claude Code runs at a set point ("CLAUDE.md vs auto memory").
- ✍️ **When to add a line:** when Claude makes the same mistake twice, or you retype last session's correction ("When to add to CLAUDE.md").
- 📏 **Size:** longer files "consume more context and reduce adherence" ("Write effective instructions").
- 📥 **Imports:** `@path` imports organise a file but "don't reduce its context cost", since they load with it (same section).
- 🗂️ **Path-scoped rules:** a rule with `paths:` frontmatter loads only when Claude reads, writes or edits a matching file ("Organize rules with `.claude/rules/`").

### ➕ Also on the page

- ⚔️ **Conflicts:** if two instructions contradict, "Claude may pick one arbitrarily" ("Write effective instructions").
- 💬 **Comments are free:** block-level HTML comments in `CLAUDE.md` files are stripped before loading ("How CLAUDE.md files load").
- 🧠 **Auto memory:** notes Claude keeps outside the repo, whose `MEMORY.md` loads its first 200 lines or 25KB every session ("How it works").

## 🎯 What it means for this repo

This section is this repo's reading, not the page's:

- 📏 **Budget basis:** the 200-line guidance is the basis of the budget's [ceiling](../../design_principles/01_principles.md#-numbers-and-tests).
- 🧮 **What to count:** the budget's [Counted list](../../README.md#-always-on-budget) follows the page for files in the repo, and leaves out auto memory on purpose, since it lives on each machine.
  - **Skills:** the live best-practices page says that for a skill Claude can start on its own, Claude sees its name and description in each session ("[Put team procedures in skills](https://code.claude.com/docs/en/best-practices#put-team-procedures-in-skills)").
- 🏷️ **Version headers:** this repo's `<!-- version -->` headers cost nothing in `CLAUDE.md` files, but the page doesn't say the same for rule files.
