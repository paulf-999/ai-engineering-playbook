# 📝 Output format

**Purpose:** the layout of Claude's replies, and of the bullets in everything it writes, so each can be scanned in seconds. It's a preference, installed only with `make install PREFERENCES=1`.

## 📤 Replies

- 📋 **Summary:** open with a bold **Summary** label, then 3 or 4 themes.
- 🏷️ **Themes:** give each theme a heading line of an emoji and a bold keyword, with no dash or colon.
- 🔹 **Bullets:** under each theme, put bullets that start with an emoji and make one point in about 15 words.
- 🔢 **Next steps:** when follow-ups exist, end with numbered options, each an emoji and bold keyword with one child bullet, and mark the best "(recommended)".
- ⏭️ **Skip:** leave this shape out of short answers and casual exchanges.

## ✍️ Everything you write

- 🔑 **Bold keyword bullets:** in replies, docs, tickets and commit messages, open a rule or definition bullet with its key term in bold and a colon, and leave plain lists unlabelled.

## 📚 Read on demand

- `on_demand/03_preferences/markdown_layout.md`, in your Claude config directory, before writing or restructuring a markdown doc.
