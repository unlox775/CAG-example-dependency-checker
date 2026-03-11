.PHONY: help install check-dependencies check-all agent-check-dependencies agent-check-all clean

PWD := $(shell pwd)
DEPENDENCY_CHECKER_CONFIG ?= dependency-checker.config.json
VENV_DIR ?= .venv
PYTHON ?= $(VENV_DIR)/bin/python3
PIP ?= $(VENV_DIR)/bin/pip
OUTPUT ?= codex-final.txt
OUTPATH := $(PWD)/$(OUTPUT)

help:
	@echo "Standalone Dependency Checker (CAG Example)"
	@echo "==========================================="
	@echo "install                    Create local venv and install requirements"
	@echo "check-dependencies         Run dependency documentation gate (direct)"
	@echo "check-all                  Alias for check-dependencies"
	@echo "agent-check-dependencies   Run check inside Codex (primary; handles gate loop)"
	@echo "agent-check-all            Alias for agent-check-dependencies"
	@echo "clean                      Remove local run artifacts"

install:
	python3 -m venv "$(VENV_DIR)"
	"$(PIP)" install -r requirements.txt

# --- Agent targets (primary) — run inside Codex ---

agent-check-dependencies: install
	rm -f "$(OUTPATH)"
	DEPENDENCY_CHECKER_CONFIG="$(DEPENDENCY_CHECKER_CONFIG)" EDITOR=true codex exec \
	  -C $(PWD) \
	  -s workspace-write \
	  -c approval_policy=never \
	  -o "$(OUTPATH)" \
	  'Run the dependency documentation checker using AGENTS.md. Use config $(DEPENDENCY_CHECKER_CONFIG). When the gate fails with ❌ VALIDATION ERROR and 🔧 AI AGENT HELPER --> FIX REQUIRED, fix the dependency docs as indicated and rerun make check-dependencies until the gate passes.'
	@echo "--- final output ---"
	@cat "$(OUTPATH)"

agent-check-all: agent-check-dependencies

# --- Manual targets — same command without Codex ---

check-dependencies:
	@if [ -x "$(PYTHON)" ]; then \
		"$(PYTHON)" dependency_checker.py --config "$(DEPENDENCY_CHECKER_CONFIG)"; \
	else \
		python3 dependency_checker.py --config "$(DEPENDENCY_CHECKER_CONFIG)"; \
	fi

check-all: check-dependencies

clean:
	rm -rf __pycache__ .pytest_cache "$(VENV_DIR)"
	rm -f results/dependency-checker-last-run-*.txt
	rm -f codex-final.txt
