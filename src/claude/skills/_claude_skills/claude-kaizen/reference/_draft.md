# 📝 claude-kaizen drafts

**Purpose:** how Claude drafts rules from feedback notes without being asked, when the session-start reminder says so.

1. **Select:** follow phases 1 and 2 of [`_implementation.md`](_implementation.md), reading `_claude_kaizen/rejections.md` in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~/.claude` when unset) first, and keep at most 2 groups.
2. **Draft:** for each, write one rule bullet and its case, per that page's Drafting section, and show both as a diff in your reply.
3. **Stop:** edit no repo file and run no eval, and tell the user to type `/claude-kaizen` to prove the drafts they like.

- 👎 **Declined:** when the user turns a draft down, add it to `_claude_kaizen/rejections.md` as that page's Rejections section shows, with "declined" in place of the counts.
- 🫙 **No candidates:** say so in one line, and log the run to `_claude_kaizen/runs.log` with `proposed=0 kept=0`, so the same notes aren't read again tomorrow.
