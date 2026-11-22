# 🛠️ confluence-create-page implementation

**Purpose:** maps the skill's phases to the files that hold their detail, so no page reaches Confluence before the user approves its draft.

## 🔄 Phases

| Phase | What happens | Detail |
|---|---|---|
| **0 — Pre-check** | Call `getAccessibleAtlassianResources` for the cloud ID | `_troubleshooting.md` → Atlassian access fails |
| **1 — Pattern and place** | Pick the pattern, and confirm the space and parent page | Patterns below |
| **2 — Gather** | Follow the pattern's steps to collect the content | `_<pattern>.md` |
| **3 — Draft review** | Save a markdown draft, show it and revise it until the user approves | Draft review below |
| **4 — Create** | Build the page from the approved draft and call `createConfluencePage` with `status: draft` | `_common_header.md`, `_common_formatting.md` |

## 🧩 Patterns

Skip the question when the request names a pattern, and otherwise offer these two:

| Pattern | What it makes |
|---|---|
| `general_page` | A general-purpose page with free-form sections |
| `platform_risk_assessment` | A Platform Risk & Maturity Assessment that rates one tool or component across fixed themes as Low, Medium or High |

- **Other page types:** say they aren't supported, offer these two, and never invent a new structure.
- **Space and parent:** confirm both before Phase 2, check the parent exists with `getConfluencePage`, and never publish at the space root.

## 🖊️ Draft review

This phase always runs, even when the user gives every detail up front or asks to "just publish".

1. **Save:** save the draft with the topic `confluence_<slug>`, where the slug holds only lowercase letters, digits and underscores, following any drafts rule your config has, and otherwise write it to a temporary file.
2. **Render:** use markdown for the page's parts, such as `> ℹ️` for info panels, `> 📝` for note panels and tables for structured data.
3. **Ask:** tell the user where the draft is, and ask them to approve it, request changes or cancel.
4. **Revise:** apply each change to the same file and ask again, for as many rounds as it takes.
5. **Create:** after an explicit approval, ask whether to prefix the title with "WIP - " (default yes), then go to Phase 4.

## 🚨 Error handling

- **No Atlassian access:** stop at Phase 0, as `_troubleshooting.md` describes.
- **Cancel or no approval:** create nothing, and keep the draft.
- **Publish fails:** follow `_troubleshooting.md`, keep the draft, and never report a page the call didn't return.
