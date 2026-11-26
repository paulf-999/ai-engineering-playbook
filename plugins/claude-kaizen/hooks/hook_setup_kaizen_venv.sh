#!/bin/bash
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: SessionStart hook that builds the plugin's Python virtualenv, which the rule eval runner needs for
#              PyYAML, on the first session and again whenever requirements.txt changes
# Usage: registered by the plugin's hooks.json; Claude Code sets CLAUDE_PLUGIN_ROOT and CLAUDE_PLUGIN_DATA

# Claude Code adds this hook's stdout to the session, so every step stays silent, and a failure leaves the
# requirements copy unwritten, so the next session tries again

#=======================================================================
# Variables
#=======================================================================

ROOT="${CLAUDE_PLUGIN_ROOT}"
DATA="${CLAUDE_PLUGIN_DATA}"

#=======================================================================
# Main script logic
#=======================================================================

if cmp -s "${ROOT}/requirements.txt" "${DATA}/requirements.txt" && [[ -x "${DATA}/venv/bin/python" ]]; then
    exit 0
fi
command -v python3 > /dev/null || exit 0
mkdir -p "${DATA}"
if python3 -m venv "${DATA}/venv" > /dev/null 2>&1 \
    && "${DATA}/venv/bin/python" -m pip install --quiet --disable-pip-version-check -r "${ROOT}/requirements.txt" > /dev/null 2>&1; then
    cp "${ROOT}/requirements.txt" "${DATA}/requirements.txt"
fi
exit 0
