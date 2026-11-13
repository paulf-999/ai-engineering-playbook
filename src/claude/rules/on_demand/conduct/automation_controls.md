<!-- version: 2.0.3 -->
<!-- created: 2026-08-28 -->
<!-- updated: 2026-11-13 -->
<!-- applies_to: * -->
<!-- miss_cost: medium — an unattended loop runs on and overspends -->
# ⚙️ Automation controls

**Purpose:** when to hand a task to a loop, such as `/loop`, `/goal`, `/batch` or a multi-agent workflow, and the caps and stop steps that keep one from overspending.

## 🧮 When to use a loop

A loop saves the user's time spent replying at each step, but rarely saves tokens, since the same work and reviews still run.

Propose a loop only when every check below passes, and stay interactive otherwise:

| Check | Passes when |
|---|---|
| 🔢 **Repetition** | There are 5 or more similar units, such as files getting the same change |
| ✅ **Verifiable** | A script, test or CI check decides when each unit is done |
| 🧠 **Low judgement** | Fewer than 1 unit in 5 is expected to need the user's decision |
| ↩️ **Reversible** | The work stays on a branch, with nothing posted outside the repo |
| 💰 **Bounded cost** | The estimate below is stated, and the user approves it before the run starts |

### 💰 Estimating cost

- 🧾 **Estimate:** tokens per unit times the number of units, plus each review agent the loop spawns.
- 📏 **Measure first:** run one unit by hand and read its token use from the agent's usage report, rather than guessing.
- 🛑 **Cap:** set a token cap with the estimate, and stop to report once a run reaches it.
- ⚖️ **Compare:** say what the loop saves, such as the gate replies skipped, beside what it costs.

## 🚀 `/loop`: repeat a prompt

- ⏱️ **Interval:** 10 minutes by default, and 5 at least, since shorter polls spend tokens on overhead.
- 🔄 **Turns:** 10 per iteration, with more only on the user's say-so.
- ⌛ **Runtime:** 2 hours, then ask before going on.
- 🛑 **Stop:** a fixed-interval loop stops only when Claude is asked to cancel it, while Esc stops a self-paced one between iterations.

## 🎯 `/goal`: work until a condition holds

- ✅ **Condition first:** state a measurable condition before starting, such as "all tests pass".
- 🔄 **Turns:** 20, with more only on the user's say-so.
- 🚩 **No progress:** stop and report after 3 iterations without progress, or after 30 minutes.
- 🛑 **Stop:** run `/goal clear`.

## 🔀 `/batch`: split work across agents

- ✋ **Approve first:** the user approves the split into units before any agent starts.
- 🔢 **Units:** ask for 12 at most, though `/batch` can propose up to 30, with each independent and opening one PR.
- 🛑 **Stop:** stop a unit's agent from `/tasks`, and check its worktree and PR afterwards.

## 🧯 When a loop misbehaves

1. **Stop it:** use the stop step above for its command.
2. **Investigate:** read the transcript to see where it diverged, before restarting.
3. **Narrow it:** cut the units, tighten the condition or lengthen the interval.
4. **Restart only once fixed:** confirm the new spec won't repeat the problem.

- **Turn caps for other unattended runs:** read `on_demand/claude_config/turn_budgets.md`, in your Claude config directory.
