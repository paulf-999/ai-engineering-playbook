# 📝 Draft save locations

**Purpose:** where to save drafts and error write-ups, and how to name them.

- 📝 **Drafts:** write proposed content to `~/_drafts/<domain>/YYYY_MM_DD_<topic>.md` before it goes to an external system.
- 🚨 **Errors:** write error details to `~/_errors/<domain>/YYYY_MM_DD_<topic>.md`.
- 🏷️ **Names:** lead with the date, then a snake_case topic, such as `2026_08_04_onboarding_plan.md`.

| Domain | Use for |
|---|---|
| 👥 `1on1` | One-to-one meeting notes and prep |
| 📄 `confluence` | Confluence page drafts |
| ✉️ `email` | Email drafts |
| 🗂️ `general` | Anything that fits no other domain |
| 🎫 `jira` | Jira ticket drafts |
| 🗓️ `meetings` | Meeting notes and agendas |
| 🧭 `plans` | Plans and proposals to share, rather than ones Claude carries out |
| 💬 `teams` | Microsoft Teams message drafts |

## 📞 Called by

This rule is invoked by [`rules/always_on/02_preferences/claude_working_files.md`](../../../always_on/02_preferences/claude_working_files.md), before saving a draft or an error write-up.
