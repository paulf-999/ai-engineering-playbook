# 🔧 confluence-create-page troubleshooting

**Purpose:** matches a symptom to its cause and fix, for access, drafting and publishing problems.

## 🔗 Atlassian access fails

- **Symptom:** `getAccessibleAtlassianResources` errors or returns no sites.
- **Cause:** the Atlassian MCP server is off, or its login has expired.
- **Fix:** enable the Atlassian MCP server, restart Claude Code, then run the skill again.

## 🔐 Permission denied when publishing

- **Symptom:** Confluence rejects `createConfluencePage` for the chosen space.
- **Cause:** you can't add pages to that space, or the space key or parent page is wrong.
- **Fix:** check the space key and parent page in Confluence, ask a space admin for edit access, or pick a space you can write to.

## ⏳ Publishing hangs or fails part-way

- **Symptom:** the publish call is slow, errors, or you can't tell whether it worked.
- **Cause:** a slow or unreachable Confluence site, or a dropped MCP connection.
- **Fix:** check the parent page in Confluence for a new draft before retrying, so you don't create a duplicate.
  - **Draft kept:** the approved local draft stays where it was saved, so a retry needs no new review.

## ✋ You don't want to publish yet

- **Symptom:** the draft isn't right, or the page isn't needed now.
- **Fix:** ask for changes and review the draft again, or cancel, which creates nothing and keeps the draft.

## 📄 The page isn't live

- **Symptom:** the new page shows as a draft in Confluence.
- **Cause:** by design, since the skill always creates pages with `status: draft`.
- **Fix:** open the page in Confluence and publish it yourself, and set the wide view there if you want it.

## 👤 Names were replaced with roles

- **Symptom:** the page says "platform owner" where you gave a person's name.
- **Cause:** by design, since the skill names no individuals in the page body.
- **Fix:** add names in Confluence after publishing if your space allows it.
