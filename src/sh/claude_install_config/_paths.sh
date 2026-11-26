#!/bin/bash
# shellcheck disable=SC2034  # the main script and the other libraries in claude_install_config/ read these variables

# Description: Set the paths and inputs that claude_install_config.sh and its other libraries read
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_paths.sh",
#        from claude_install_config.sh, straight after shell_utils.sh

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
RENDERER="$(dirname "${BASH_SOURCE[0]}")/../../py/claude_render_settings.py"
RENDER_PYTHON="${RENDER_PYTHON:-$(dirname "${BASH_SOURCE[0]}")/../../../.venv/bin/python}"
# the deny rules the last install added, as a JSON list, so the next install can remove any the config has since dropped
DENY_MANIFEST="${TARGET_DIR}/.playbook_install_deny_rules"

#=======================================================================
# Functions
#=======================================================================

# no functions of its own
