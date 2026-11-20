# 📝 Output format

**Purpose:** the layout of Claude's replies and bullets.

## 📤 Replies

- 📋 **Summary:** open with a bold **Summary** label, then 3 or 4 themes.
- 🏷️ **Themes:** give each theme a heading line of an emoji and a bold keyword, with no dash or colon.
- 🔹 **Bullets:** under each theme, put bullets that start with an emoji and make one point in about 15 words.
- 🔢 **Next steps:** when follow-ups exist, end with numbered options, each an emoji and bold keyword with one child bullet, and mark the best "(recommended)".
- ⏭️ **Skip:** skip this shape for short answers and casual chat.

## ✍️ Everything you write

- 🔑 **Bold keyword bullets:** open a rule or definition bullet with its key term in bold and a colon, and leave plain lists unlabelled.

## 📚 Read on demand

- [`on_demand/02_preferences/claude_markdown_style.md`](../../on_demand/02_preferences/claude_markdown_style.md), in your Claude config directory, before writing or restructuring a markdown doc.
