# ✍️ Blog posts

**Purpose:** how Claude writes and reviews blog posts in the maintainer's voice, and the bar each post must reach before publishing.

## 🗣️ Voice

Drawn from posts on [the maintainer's Medium page](https://medium.com/@paul-fry), and the maintainer's own preferences:

- 🧱 **Structure:** open with an italic "This post…" line, then follow the Structure section below.
- 💬 **Phrases:** use plain first-person ones, such as "I'd recommend", "To be honest", "i.e.,", "e.g.," and "described below".
- ❓ **Habits:** ask the odd rhetorical question, name the caveats, and sign off briefly, such as "Enjoy!" or "Good luck!".
- 🔗 **Links:** list resources as "Title | site".
- 🚫 **Avoid:** slogans, dramatic one-line paragraphs, emoji bullets, and tables, which Medium lacks.

## 🏗️ Structure

Lead with the answer, then give the problem and work through the detail:

1. **TL;DR:** up to three bullets giving the answer, the evidence with its key figures and main caveat, and what to do first.
2. **Problem statement:** a section with that name, saying what goes wrong and for whom.
3. **Solution:** the checklist, rules or code.
4. **Detail:** how to do it, and the limits.
5. **Close:** "If you only do one thing", then Useful Resources, with no Agenda or Summary.

- 🌉 **Content flow:** when a section changes topic, open with a sentence or two linking it to what came before.
- 🧪 **Example sub-headings:** give each example block a sub-heading starting "Example:".
- ✂️ **One format per point:** make a point once, as a list, an example or a visual, rather than repeat it in several.

## 😏 Humour and visuals

- 🎯 **Humour:** use two or three light jokes or sarcastic asides, aimed at the maintainer or the tools, never at colleagues.
- 🚫 **Serious parts:** keep jokes out of figures, caveats and instructions.
- ✍️ **Whose jokes:** suggest lines for the maintainer to swap, since jokes drift from their voice first.
- 🖼️ **Visuals:** use at most three, preferring the maintainer's own diagrams and recordings, with alt text and a check of any logo's or GIF's terms.
- 😀 **Emojis:** use a few in headings only.

## ✏️ Writing

Follow [`claude_writing_style.md`](../../src/claude/rules/always_on/02_preferences/claude_writing_style.md), and where it differs from the voice above, the voice wins.

- 👤 **No invented experience:** never write an anecdote, reaction, result or team detail the maintainer hasn't given, and ask for one instead.
- 🔒 **Privacy:** leave out colleagues' names and anything that identifies an employer, and flag a story a colleague could recognise.
- 🧪 **Examples:** give each main point a short worked example, such as a snippet, a before and after or a filled-in template, and say when it's made up.
- 📖 **Sources:** open each source before citing it, say when it's a vendor, paywalled or only a correlation, and check claims about Claude against Anthropic's docs, saying where the post differs.
- 🖼️ **Versions:** mark each draft with a status line giving its version and reading time, such as "draft v0.1.0 · ~4 min", and put "blog" in its file name.

## ⏱️ Reading time

- 🎯 **Target:** 4 minutes, and 5 at most.
- 🧮 **Measure:** words outside code ÷ 238, plus 3 seconds per code line, leaving out Useful Resources.
- 🪓 **Over 5:** split the post rather than cut its evidence or caveats.
- 🔎 **After a cut:** have a cold reader compare the old and new versions for dropped caveats.

## 🏅 Quality themes

Score each from 0 to 10, where 10 means nothing to fix:

| Theme | What a high score means |
|---|---|
| 🗣️ **Voice** | Reads as if the maintainer wrote it, without parody |
| ✏️ **Writing style** | Meets the Writing section above |
| 🧭 **Clarity** | The stated audience can follow it in one read |
| 🌊 **Content flow** | Each section follows from the one before, with new ideas introduced before they're used |
| 🎁 **Usefulness** | The reader leaves with something specific to do, shown by an example |
| 🔬 **Honesty** | Claims are supported or marked as opinion, and limits are stated |
| 💡 **Insight** | It says something readers are unlikely to have met elsewhere, resting on evidence |
| 😏 **Engagement** | The reader wants to keep going and share it, without losing trust in it |
| 🎯 **Focus** | One clear takeaway, with no padding or repetition |

The insight score uses these anchors:

- **2:** common advice.
- **5:** common advice, well organised.
- **8:** at least one non-obvious point backed by evidence.
- **10:** changes how an experienced reader would act.

## ✅ Review and pass mark

- 👥 **Readers:** 3 cold `claude -p --safe-mode` readers score each post separately, given plain theme names and sample posts, but not this rule or its text.
- 📏 **Pass:** every theme's median is 8 or more, and the post is within its reading time.
- 🔎 **Facts:** a separate reader checks each claim against its sources and finds none contradicted, overstated or unsupported, since voice scores rarely vary.
- 🔁 **Rounds:** run 2 at most, then hand the open findings to the maintainer.
- ⚠️ **Last edits:** say which edits came after the final scoring, since they're unscored.
