---
paths:
  - "**/Makefile"
  - "**/*.mk"
---
# 🛠️ Makefile Style Guide & Standards

**Purpose:** how to write Makefile recipes. This team's naming, assignment, shell and messaging choices are in [`team_conventions/utilities/makefile.md`](../../team_conventions/utilities/makefile.md), which loads with this guide.

## 🧮 Recipes

- **`@` to silence:** prefix a command with `@` to stop Make printing the command itself before running it.
- **`$@` for the target:** use `$@`, which expands to the current target's name, instead of repeating the name in the recipe.

```makefile
build:
	@mkdir -p $@
```
