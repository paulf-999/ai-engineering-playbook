# ⚙️ Automation controls

**Purpose:** how to cut the user's replies on multi-step work, either with a loop for repeated units or with a front-loaded batch run for varied ones.

## 🧮 Choosing the mode

A loop or batch run saves the user's replies, not tokens, since the same work and reviews still run.

| Check | Loop when | Batch run when |
|---|---|---|
| 🔢 **Units** | 5 or more getting the same change | 3 or more independent tasks, such as GitHub issues |
| 🧠 **Judgement** | Fewer than 1 unit in 5 needs a decision | Every decision can be asked before the run starts |
| ✅ **Verifiable** | A script, test or CI check decides when each unit is done | The same, for every unit |
| ↩️ **Reversible** | Nothing leaves the branch | Each unit lands as its own PR, so it can be reviewed and reverted |

Stay interactive when neither column fits.

## 🔁 Loops

- 💰 **Cost first:** state tokens per unit times units, measured on one unit by hand, and get approval before starting.
- 🛑 **Caps:** cap turns and tokens on `/loop`, `/goal`, `/batch` or a multi-agent workflow, and stop to report at a cap.
- 🎯 **`/goal`:** state a measurable condition, and stop after 3 iterations without progress.
- 🔀 **`/batch`:** the user approves the split into units, 12 at most, before any agent starts.

## 🗂️ Batch runs

1. 🔍 **Triage:** read every unit first, and list each decision it needs.
2. 🤝 **Front-load:** ask all of those decisions in one prompt, with a recommended option for each.
3. ✋ **Waiver:** start only once the user explicitly waives the phase gates and PR confirmations, and note whether they also allowed merging, then carry every unit through to the end without offering next steps for work already allowed.
4. 🔢 **Order:** run units that edit the same file far apart, or last, so their PRs conflict less.
5. 🌿 **Per unit:** branch fresh from `origin/main`, pass the repo's checks, then open one PR that closes its issue, never stacked on another open PR.
6. ⚡ **Overlap:** draft a unit's PR body in the background while the next unit starts.
7. 🔀 **Merge, if allowed:** merge in order, waiting until each PR's checks finish and it shows as clean, then run the checks on the combined `main`, since each PR was tested on its own base.
8. 📋 **Report:** end with one summary of each unit, its PR and anything left open.

- 🛑 **Stop and ask:** when a check fails without an obvious fix, a new decision appears, or a unit's finding changes its scope.

## 🧯 When a run misbehaves

1. **Stop it:** cancel the loop, or stop the batch before its next unit.
2. **Investigate:** read the transcript to see where it diverged.
3. **Narrow it:** cut the units, tighten the condition or ask the missed decision.
4. **Restart only once fixed:** confirm the new spec won't repeat the problem.

- **Turn caps for other unattended runs:** read `on_demand/claude_config/turn_budgets.md`, in your Claude config directory.
