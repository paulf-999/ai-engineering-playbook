# ✍️ Blog posts

**Purpose:** how Claude writes and reviews blog posts in the maintainer's voice, and the bar each post must reach before publishing.

## 🗣️ Voice

Drawn from posts on [the maintainer's Medium page](https://medium.com/@paul-fry):

- 🧱 **Structure:** open with an italic "This post…" line, then an Agenda, numbered sections, a Summary and Useful Resources.
- 💬 **Phrases:** use plain first-person ones, such as "I'd recommend", "To be honest", "i.e.,", "e.g.," and "described below".
- ❓ **Habits:** ask the odd rhetorical question, name the caveats, and sign off briefly, such as "Enjoy!" or "Good luck!".
- 🔗 **Links:** list resources as "Title | site".
- 🚫 **Avoid:** slogans, dramatic one-line paragraphs, emoji bullets, and tables, which Medium lacks.

## ✏️ Writing

Follow [`claude_writing_style.md`](../../src/claude/rules/always_on/02_preferences/claude_writing_style.md), and where it differs from the voice above, the voice wins.

- 👤 **No invented experience:** never write an anecdote, reaction, result or team detail the maintainer hasn't given, and ask for one instead.
- 🔒 **Privacy:** leave out colleagues' names and anything that identifies an employer, and flag a story a colleague could recognise.
- 📖 **Primary sources:** open each source before citing it, and say when it's a vendor, paywalled or only a correlation.
- 🖼️ **Versions:** mark each draft with a status line giving its version and reading time, such as "draft v0.1.0 · ~4 min", and put "blog" in its file name.

## ⏱️ Reading time

- 🎯 **Target:** 4 minutes, and 5 at most.
- 🧮 **Measure:** words outside code ÷ 238, plus 3 seconds per code line, leaving out the Agenda and Useful Resources.
- 🪓 **Over 5:** split the post rather than cut its evidence or caveats.
- 🔎 **After a cut:** have a cold reader compare the old and new versions for dropped caveats.

## 🏅 Quality themes

Score each from 0 to 10, where 10 means nothing to fix:

| Theme | What a high score means |
|---|---|
| 🗣️ **Voice** | Reads as if the maintainer wrote it, without parody |
| ✏️ **Writing style** | Meets the Writing section above |
| 🧭 **Clarity** | The stated audience can follow it in one read |
| 🎁 **Usefulness** | The reader leaves with something specific to do |
| 🔬 **Honesty** | Claims are supported or marked as opinion, and limits are stated |
| 💡 **Insight** | It says something readers are unlikely to have met elsewhere, resting on evidence |
| 🎯 **Focus** | One clear takeaway, with no padding or repetition |

The insight score uses these anchors:

- **2:** common advice.
- **5:** common advice, well organised.
- **8:** at least one non-obvious point backed by evidence.
- **10:** changes how an experienced reader would act.

## ✅ Review and pass mark

- 👥 **Readers:** 3 cold `claude -p --safe-mode` readers score each post separately, given the themes, the Writing section and sample posts.
- 📏 **Pass:** every theme's median is 8 or more, and the post is within its reading time.
- 🔎 **Facts:** a separate reader checks each claim against its sources and finds none contradicted, overstated or unsupported, since voice scores rarely vary.
- 🔁 **Rounds:** run 2 at most, then hand the open findings to the maintainer.
- ⚠️ **Last edits:** say which edits came after the final scoring, since they're unscored.
