#!/bin/bash

# Description: Which source files install, where, and with which links and pointers
# Usage: source "$(dirname "${BASH_SOURCE[0]}")/claude_install_config/_file_selection.sh",
#        from claude_install_config.sh, once _paths.sh sets the paths and inputs these functions read

#=======================================================================
# Variables
#=======================================================================

LAZY_RULES_DIR="rules/on_demand"
# authoring templates that never install
AUTHORING_TEMPLATES=" _templates/AGENT.md.template _templates/rule.md.template "
# the tracked files under SOURCE_DIR, set by list_source_files
SOURCE_FILES=()
# where each source file installs, one per line, set by list_source_files
TARGET_PATHS=""
# the Markdown files with a link that climbs out of its folder, one per line, set by list_source_files
LINKING_FILES=""
# where the last file passed to target_path installs
TARGET_PATH=""
# files the last install wrote that the repo no longer has, set by list_removed_files
REMOVED_FILES=()

#=======================================================================
# Functions
#=======================================================================

# Settle which files install and which are removed
select_files() {
    resolve_preferences
    list_source_files
    list_removed_files
}

# Settle PREFERENCES: 0 leaves preferences out, otherwise they install,
# except into a project, which never gets them, since its .claude/ folder is shared
resolve_preferences() {
    case "${PREFERENCES}" in
        0) ;;
        "")
            PREFERENCES=1
            if [[ -n "${PROJECT}" ]]; then PREFERENCES=0; fi
            ;;
        *)
            log_message "${ERROR}" "PREFERENCES can only be 0, not '${PREFERENCES}', since preferences install by default - nothing changed."
            exit 1
            ;;
    esac
}

# Succeed if an installed path is a preference
is_preference() {
    [[ "/${1}" == */preferences/* || "/${1}" == */02_preferences/* ]]
}

# Succeed if a tracked file under SOURCE_DIR should install
is_installable() {
    local file="${1}"
    # a tracked file deleted from the working tree counts as removed
    file_exists "${SOURCE_DIR}/${file}" || return 1
    # a hook installs only if the rendered settings name it, in a command that ends with its path and an escaped quote
    [[ "${file}" =~ ^hooks/(.*/)?hook_[^/]*\.sh$ && "${RENDERED_SETTINGS}" != *"/${file}\\\""* ]] && return 1
    [[ "${PREFERENCES}" != 1 ]] && is_preference "${file}" && return 1
    [[ "${AUTHORING_TEMPLATES}" == *" ${file} "* || "${file}" == _templates/skills/* ]] && return 1
    # a README explains a folder to people browsing the repo, and never loads
    [[ "${file##*/}" == README.md ]] && return 1
    # a skill group's own files, such as its README, describe the group, which doesn't exist once installed flat
    [[ "${file}" =~ ^skills/_[^/]+/[^/]+$ ]] && return 1
    return 0
}

# Collect the files git tracks under SOURCE_DIR, so untracked drafts and caches are never installed
list_source_files() {
    local file
    while IFS= read -r -d '' file; do
        file="${file#"${SOURCE_DIR}"/}"
        is_installable "${file}" || continue
        SOURCE_FILES+=("${file}")
        target_path "${file}"
        TARGET_PATHS+="${TARGET_PATH}"$'\n'
    done < <(git ls-files -z -- "${SOURCE_DIR}")
    # one grep for every file, as most have no such link, so need no rendering
    LINKING_FILES="$(git grep -lF -e '](../' -- "${SOURCE_DIR}/*.md" || true)"
    if [[ "${#SOURCE_FILES[@]}" -eq 0 ]]; then
        log_message "${ERROR}" "No tracked files found under ${SOURCE_DIR} - nothing to install."
        exit 1
    fi
}

# Collect the manifest's paths that are no longer installed, skipping any path that could point outside the target
list_removed_files() {
    local path
    file_exists "${MANIFEST}" || return 0
    # one grep lists the manifest's paths that TARGET_PATHS lacks, rather than one grep per path
    while IFS= read -r path; do
        [[ -n "${path}" && "${path}" != /* && "${path}" != *..* ]] || continue
        if file_exists "${TARGET_DIR}/${path}"; then REMOVED_FILES+=("${path}"); fi
    done < <(grep -Fxv -f <(printf '%s' "${TARGET_PATHS}") -- "${MANIFEST}" || true)
}

# Set TARGET_PATH to where a source file installs: on-demand files move from rules/on_demand/ to on_demand/,
# and a skill in a group folder such as skills/_git_skills/ installs flat under skills/, where Claude Code finds it
# it sets a variable rather than printing, so callers needn't start a subshell for each file
target_path() {
    local file="${1}"
    if [[ "${file}" == "${LAZY_RULES_DIR}/"* ]]; then
        TARGET_PATH="${file#rules/}"
    elif [[ "${file}" =~ ^skills/_[^/]+/(.+/.+)$ ]]; then
        TARGET_PATH="skills/${BASH_REMATCH[1]}"
    else
        TARGET_PATH="${file}"
    fi
}

# Print a source file as it installs: links point at where files install, and in a project, pointers name its .claude/
# folder, not your config directory
render() {
    if has_links "${1}"; then
        target_path "${1}"
        relink "${1}" "${TARGET_PATH}" < "${SOURCE_DIR}/${1}" | render_text
    else
        render_text < "${SOURCE_DIR}/${1}"
    fi
}

# Succeed if a source file has a link that climbs out of its folder, which may need to change as it installs
has_links() {
    [[ $'\n'"${LINKING_FILES}"$'\n' == *$'\n'"${SOURCE_DIR}/${1}"$'\n'* ]]
}

# Print text from stdin, from the source file $1 that installs at $2, with each link that climbs out of its folder
# pointing at where its target installs, by the same moves as target_path, so change both together; it reads inline
# links only, as the config has no reference-style ones
relink() {
    LC_ALL=C awk -v from="${1}" -v to="${2}" '
        # the path a link in the file "base" points at, or "" if it climbs out of the config
        function resolve(base, link,    parts, kept, count, depth, i, path) {
            sub(/[^\/]*$/, "", base)
            count = split(base link, parts, "/")
            for (i = 1; i <= count; i++) {
                if (parts[i] == "..") { if (--depth < 0) return "" }
                else if (parts[i] != "" && parts[i] != ".") kept[++depth] = parts[i]
            }
            for (i = 1; i <= depth; i++) path = path (i > 1 ? "/" : "") kept[i]
            return path
        }
        function installed(path) {
            if (path ~ /^rules\/on_demand(\/|$)/) return substr(path, 7)
            if (path ~ /^skills\/_[^\/]+\/[^\/]+\//) sub(/^skills\/_[^\/]+\//, "skills/", path)
            return path
        }
        # the relative link from the file "base" to path
        function relative(base, path,    ours, theirs, depth, count, same, i, link) {
            depth = split(base, ours, "/") - 1
            count = split(path, theirs, "/")
            while (same < depth && same < count - 1 && ours[same + 1] == theirs[same + 1]) same++
            for (i = same; i < depth; i++) link = link "../"
            for (i = same + 1; i <= count; i++) link = link theirs[i] (i < count ? "/" : "")
            return link
        }
        {
            rest = $0; line = ""
            while (match(rest, /\]\(\.\.\/[^)# \t]+/)) {
                link = substr(rest, RSTART + 2, RLENGTH - 2)
                path = resolve(from, link)
                line = line substr(rest, 1, RSTART + 1) (path == "" ? link : relative(to, installed(path)))
                rest = substr(rest, RSTART + RLENGTH)
            }
            print line rest
        }'
}

# Print text from stdin as it installs, so a past version of a file can be compared with what an install wrote
render_text() {
    if [[ -n "${PROJECT}" ]]; then
        # shellcheck disable=SC2016  # the backticks and \$CLAUDE_CONFIG_DIR are literal text in the rules, not expansions
        sed -e 's/in your Claude config directory (`$CLAUDE_CONFIG_DIR`, or `~\/.claude` when unset)/in this project'"'"'s `.claude\/` folder/' \
            -e 's/in your Claude config directory/in this project'"'"'s `.claude\/` folder/'
    else
        cat
    fi
}
