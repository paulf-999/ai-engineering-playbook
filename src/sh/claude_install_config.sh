#!/bin/bash
# shellcheck disable=SC2034  # the libraries in claude_install_config/ read these variables
set -euo pipefail  # Fail fast, including on unset variables and errors anywhere in a pipeline.

# Description: Copy the repo's Claude config (src/claude/) into your Claude config directory, backing up each file it overwrites
#              On-demand files in rules/on_demand/ go beside rules/, since Claude Code loads everything under rules/
#              Links between files are corrected for where each one installs
#              A manifest records what was installed, so files the repo has since removed are backed up and removed,
#              along with any folder that leaves empty
#              It also keeps the config's hooks and deny rules in settings.json in step, keeping every other setting
#              With PROJECT set, it installs into that repo's .claude/ folder instead, leaving the done checks and worktree edits hooks out unless HOOKS=1
#              With UNINSTALL=1, it removes what the manifest lists, restores each file's pre-install backup and strips
#              the config's hooks and deny rules from settings.json
#              With YES=1, install skips the typed confirmation for provisioning scripts, but never from Claude Code
#              It adds the rules in 02_preferences/ folders unless PREFERENCES=0, but never into a PROJECT install
#              An install with preferences also files saved plans by status and archives old drafts, and only warns if that fails
#              It never installs the skill, agent and rule templates, which are for authoring in this repo
#              Those hooks and deny rules come from claude_install_config/settings.json.j2, which must list every hook
# Usage: [PROJECT=<repo> [HOOKS=1]] [PREFERENCES=0] [UNINSTALL=1 | YES=1] src/sh/claude_install_config.sh (run from the repo root, at
#        your own terminal or in a provisioning script; make install and make uninstall call it)

# Load reusable shell script vars & functions
# shellcheck source=SCRIPTDIR/shell_utils.sh
source "$(dirname "${BASH_SOURCE[0]}")/shell_utils.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_file_selection.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_selection.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_file_changes.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_changes.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_confirmation.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_confirmation.sh"
# shellcheck source=SCRIPTDIR/claude_install_config/_settings.sh
source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_settings.sh"

# Catch Ctrl+C, so an interrupted run says so and exits 1
trap handle_interruption SIGINT

#=======================================================================
# Variables
#=======================================================================

# mirrors the config directory's layout, so each file is copied to the same relative path, except on-demand files
SOURCE_DIR="src/claude"
CONFIG_DIR="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
# a repo to install into instead of your Claude config directory, and whether its install includes the done checks hook
PROJECT="${PROJECT:-}"
WITH_HOOKS="${HOOKS:-}"
# where project installs backed up before BACKUP_PREFIX held a hash, empty for your own config directory
OLD_BACKUP_PREFIX=""
UNINSTALL="${UNINSTALL:-}"
# skips install's typed confirmation, for devcontainers and onboarding scripts that have no terminal
ASSUME_YES="${YES:-}"
# 0 leaves out the rules in 02_preferences/ folders, one person's taste, which otherwise install everywhere but a project
PREFERENCES="${PREFERENCES:-}"
if [[ -n "${PROJECT}" ]]; then
    if [[ ! -d "${PROJECT}" ]]; then
        echo "PROJECT=${PROJECT} isn't a folder - nothing changed." >&2
        exit 1
    fi
    PROJECT="$(cd "${PROJECT}" && pwd)"
    TARGET_DIR="${PROJECT}/.claude"
    # backups go in your own config directory, so they're never committed with the repo
    OLD_BACKUP_PREFIX="${CONFIG_DIR}/backups/project_$(basename "${PROJECT}")_"
    # a hash of the repo's full path keeps apart the backups of repos with the same folder name
    PROJECT_HASH="$(cd "${PROJECT}" && pwd -P | git hash-object --stdin)"
    BACKUP_PREFIX="${OLD_BACKUP_PREFIX}${PROJECT_HASH:0:12}_"
else
    TARGET_DIR="${CONFIG_DIR}"
    BACKUP_PREFIX="${TARGET_DIR}/backups/install_"
fi
# each install's backups start with BACKUP_PREFIX then the date, so uninstall can find the oldest copy of each file
BACKUP_DIR="${BACKUP_PREFIX}$(date +%Y_%m_%d_%H%M%S)"
[[ "${UNINSTALL}" == 1 ]] && BACKUP_DIR="${BACKUP_PREFIX}uninstall_$(date +%Y_%m_%d_%H%M%S)"
# where an install backs up a copy an earlier install wrote, which uninstall never restores, since it isn't the user's
UPGRADE_BACKUP_DIR="${BACKUP_PREFIX}upgrade_$(date +%Y_%m_%d_%H%M%S)"
# the paths the last install wrote, one per line, so the next install can remove any the repo no longer has
MANIFEST="${TARGET_DIR}/.playbook_install_manifest"
# settings.json holds personal settings, so install merges the hooks into it rather than copying a file over it
SETTINGS="${TARGET_DIR}/settings.json"
# the hooks folder as hook commands name it: a project's settings are shared, so they use Claude Code's own variable
HOOKS_DIR="${TARGET_DIR}/hooks"
# shellcheck disable=SC2016  # Claude Code expands it, not this script
if [[ -n "${PROJECT}" ]]; then HOOKS_DIR='$CLAUDE_PROJECT_DIR/.claude/hooks'; fi
# fills in the settings template, with the repo's own .venv, which make install creates and adds Jinja to
RENDERER="$(dirname "${BASH_SOURCE[0]}")/../py/claude_render_settings.py"
RENDER_PYTHON="${RENDER_PYTHON:-$(dirname "${BASH_SOURCE[0]}")/../../.venv/bin/python}"
# the deny rules the last install added, as a JSON list, so the next install can remove any the config has since dropped
DENY_MANIFEST="${TARGET_DIR}/.playbook_install_deny_rules"

#=======================================================================
# Functions
#=======================================================================

# Copy the config into the target, after a typed confirmation
run_install() {
    resolve_preferences
    render_settings
    list_source_files
    list_removed_files
    confirm_install
    install_files
    remove_old_files
    register_settings
    file_plans
}

# Remove what the last install added, after a typed confirmation
run_uninstall() {
    # with no files to install or settings rendered, every file the manifest lists counts as removed, and no hook or deny
    # rule ships
    list_removed_files
    confirm_uninstall
    uninstall_files
    register_settings
    rm -f "${DENY_MANIFEST}"
}

# File saved plans by status and archive old drafts, which is a preference, so it's skipped with PREFERENCES=0 and in a project
file_plans() {
    [[ "${PREFERENCES}" == 1 ]] || return 0
    if ! python3 "$(dirname "${BASH_SOURCE[0]}")/../py/claude_manage_plans.py" clean --yes; then
        log_message "${WARNING}" "Saved plans weren't filed or drafts archived - run make clean_plans to see why."
    fi
}

#=======================================================================
# Main script logic
#=======================================================================
print_section_header "${DEBUG}" "Script execution started."

if [[ "${UNINSTALL}" == 1 ]]; then run_uninstall; else run_install; fi

print_section_header "${DEBUG}" "Script execution completed." && echo
