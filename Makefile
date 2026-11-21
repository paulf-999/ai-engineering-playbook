SHELL = /bin/sh

#================================================================
# Usage
#================================================================
# make help		# list the available targets
# make all		# run deps then install, the default target the Makefile linter requires
# make deps		# install the dependencies and git hooks
# make install		# copy src/claude/ into your Claude config directory, or PROJECT=<repo>'s .claude/ folder
# make uninstall	# remove what make install added, restoring the files it replaced
# make install YES=1	# install without the typed confirmation, for provisioning scripts outside Claude Code
# make install PREFERENCES=0	# leave out the preferences, such as the reply format
# make test		# run the tests (pytest)
# make evals		# run the evals tagged trigger: live with claude -p, on your own login, setting up .venv on first use
# make evals BEHAVIOUR=1	# run the evals tagged behaviour: true end to end, and grade their assertions
# make evals RULES=1	# run each rule eval with and without its rule, and say if the rule helps
# make evals RULES=1 CASE=<name>	# run only the named rule eval
# make evals README=1	# score the README with cold readers playing a new and an experienced Claude Code user
# make evals RULES=1 RUNS=<n>	# set the rule evals' runs per condition, 3 by default, or the README evals' readers per persona, 4
# make context_cost	# rewrite maintenance/context_cost.md from src/claude/
# make clean		# delete the pytest, ruff and Python caches

#=======================================================================
# Variables
#=======================================================================
.EXPORT_ALL_VARIABLES:

# ANSI colour codes for the target messages: green, then reset
INFO := \033[0;32m
COLOUR_OFF := \033[0m

# the virtualenv make evals runs in, which it creates with only pyyaml on first use, so nobody needs make deps first
EVALS_VENV ?= .venv
# the eval runner make evals picks: the trigger evals, or the rule, behaviour or README evals when RULES=1, BEHAVIOUR=1 or README=1 is set
EVAL_RUNNER := $(if $(RULES),rule,$(if $(BEHAVIOUR),behaviour,$(if $(README),readme,trigger)))

#=======================================================================
# Targets
#=======================================================================
all: deps install

help:
	@echo "${INFO}\nAvailable targets:${COLOUR_OFF}\n"
	@sed -n 's/^# make /make /p' Makefile

deps:
	@echo "${INFO}\nCalled makefile target 'deps'. Download any required libraries.${COLOUR_OFF}\n"
	@test -n "$$VIRTUAL_ENV" || { echo "Activate the virtualenv first: see docs/guides/virtualenv_setup.md"; exit 1; }
	@python -m pip install -r requirements.txt
	@python -m pre_commit install

install:
	@echo "${INFO}\nCalled makefile target 'install'. Copy the Claude config into $${PROJECT:+$$PROJECT/.claude}$$([ -n "$${PROJECT:-}" ] || echo "$${CLAUDE_CONFIG_DIR:-$$HOME/.claude}").${COLOUR_OFF}"
	@bash src/sh/claude_install_config.sh

uninstall:
	@echo "${INFO}\nCalled makefile target 'uninstall'. Remove the Claude config that make install added.${COLOUR_OFF}"
	@UNINSTALL=1 bash src/sh/claude_install_config.sh

context_cost:
	@bash src/sh/claude_report_context_cost.sh

test:
	@echo "${INFO}\nCalled makefile target 'test'. Perform any required tests.${COLOUR_OFF}\n"
	@pytest

$(EVALS_VENV)/.evals_ready:
	@python3 -m venv $(EVALS_VENV)
	@$(EVALS_VENV)/bin/python -m pip install --quiet --disable-pip-version-check "$$(grep -i '^pyyaml==' requirements.txt | cut -d' ' -f1)"
	@touch $@

evals: $(EVALS_VENV)/.evals_ready
	@echo "${INFO}\nCalled makefile target 'evals'. Run the $(EVAL_RUNNER) evals.${COLOUR_OFF}\n"
	@$(EVALS_VENV)/bin/python src/py/claude_run_$(EVAL_RUNNER)_evals.py

clean:
	@rm -rf .pytest_cache .ruff_cache
	@find src tests -name __pycache__ -type d -prune -exec rm -rf {} +

# Phony targets
.PHONY: all help deps install uninstall test clean context_cost evals

# .PHONY tells Make that these targets don't represent files
# This prevents conflicts with any files named "all" or "clean"
