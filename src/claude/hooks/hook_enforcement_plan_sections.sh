#!/bin/bash
# version: 1.0.0
# created: 2026-11-10
# updated: 2026-11-10
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: PreToolUse hook on ExitPlanMode that blocks a plan with no Intent or Spec heading
# Usage: registered in settings.json by make install; Claude Code pipes the hook's JSON input to stdin

# This hook doesn't source shell_utils.sh: Claude Code reads its stderr and exit code, so it must print nothing else

#=======================================================================
# Variables
#=======================================================================

# exit code 2 tells Claude Code to block the tool call and show stderr to Claude
BLOCK=2
# a markdown heading of any level whose first word is the section name, after any emoji or bold, ignoring case
INTENT_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*intent\b'
SPEC_HEADING='^#{1,6}[[:space:]]+[^[:alpha:]]*spec\b'

#=======================================================================
# Functions
#=======================================================================

# Print the names of the sections the plan on stdin lacks, one per line
missing_sections() {
    local plan
    plan="$(cat)"
    grep -Eiq "${INTENT_HEADING}" <<< "${plan}" || echo "Intent"
    grep -Eiq "${SPEC_HEADING}" <<< "${plan}" || echo "Spec"
}

#=======================================================================
# Main script logic
#=======================================================================

# without jq the plan can't be read, so allow the call rather than block every plan
command -v jq > /dev/null || exit 0

PLAN="$(jq -r '.tool_input.plan // empty' 2> /dev/null || true)"
# no plan text means there's nothing to check
[[ -n "${PLAN}" ]] || exit 0

MISSING="$(missing_sections <<< "${PLAN}")"
[[ -z "${MISSING}" ]] && exit 0

echo "This plan has no $(paste -sd '/' - <<< "${MISSING}") heading." \
    "Read _rules_on_demand/03_workflows/sdlc_workflow.md in your Claude config directory," \
    "then open the plan with an Intent section, then a Spec section, and submit it again." >&2
exit "${BLOCK}"
