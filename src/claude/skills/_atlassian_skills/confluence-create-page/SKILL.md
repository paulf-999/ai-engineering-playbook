---
name: confluence-create-page
description: Create a Confluence page from the team's templates, after you approve a local draft — use when asked to create, write or add a Confluence page, publish a draft to Confluence, or write a platform risk assessment
tags:
  criticality: should
  status: active
  tested: true
---

## 🤖 Instructions for Claude

- **Pre-check:** call `getAccessibleAtlassianResources` to get the cloud ID, and if it fails tell the user to enable the Atlassian MCP server and restart Claude Code, then stop.
- **Read first:** read `reference/_implementation.md` for the phases, then the chosen pattern in `reference/patterns/` and both files in `reference/common/` before drafting.
- **Always:** save the draft with the topic `confluence_<slug>`, following any drafts rule your config has, and otherwise write it to a temporary file, then tell the user where it is.
- **Always:** show the draft and wait for an explicit approval before calling `createConfluencePage`, even when asked to "just publish".
- **Always:** create the page with `status: draft`, so nothing goes live until the user publishes it in Confluence.
- **Never:** infer the space or parent page, so confirm both with the user, and never publish at the space root.
- **Never:** name individuals in the page body, so use a role such as "the platform owner" instead, leaving the Creator field as the only name.

## 🎯 Purpose

Turns notes or an outline into a Confluence page in the team's format, with a local draft you approve before anything reaches Confluence:

- **Patterns** — a `general_page` with free-form sections, or a `platform_risk_assessment` that rates one tool's maturity.
- **Draft** — writes a markdown draft you can read and change, and revises it until you approve it.
- **Publish** — creates the page as a Confluence draft under the parent you confirm, with the team's header and formatting.

## 💡 Example Usage

```text
$ /confluence-create-page a page about the Q3 roadmap
[Phase 1] Pattern: general_page · Space and parent page? DATA, under "Roadmaps"
[Phase 2] Title, status, purpose and sections gathered
[Phase 3] Draft saved: 2026_11_18_confluence_q3_roadmap.md
          Approve, request changes or cancel? (y/e/n): e, shorten the Overview
          Draft updated. Approve? y
[Phase 4] Created as a Confluence draft:
          https://yourteam.atlassian.net/wiki/spaces/DATA/pages/12345
```

## ✨ Best For

One new page at a time that follows the team's header, formatting and page patterns, without hand-writing Confluence's page format.

**Caveats:** it creates new pages as Confluence drafts only.

- **Going live:** publish the page yourself in Confluence, and set its wide view there, since the API can't.
- **Existing pages:** it doesn't edit them, so change those in Confluence.
- **Evals by hand:** nothing runs `tests/evals.yaml` yet, so check a change to the skill against its scenarios by hand.

## 📚 References

- `reference/_implementation.md` — the phase map, the pattern choice and the draft review rules
- `reference/patterns/_general_page.md` and `reference/patterns/_platform_risk_assessment.md` — what each pattern gathers and how its page is laid out
- `reference/common/_common_header.md` and `reference/common/_common_formatting.md` — the page header and formatting every pattern uses
- `reference/_troubleshooting.md` — symptoms, causes and fixes when access, drafting or publishing fails
- `tests/evals.yaml` — 11 scenarios covering both patterns, the space and parent checks, draft review, the no-MCP stop, a publish error and two cases where it shouldn't fire
