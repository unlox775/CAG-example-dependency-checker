# Python Dependencies Analysis

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This directory contains detailed analysis of all Python dependencies from the `pyproject.toml` file. Dependencies are organized into logical categories for easier navigation and analysis.

## Quick Navigation

- [← Back to Main Dependencies](../README.md)
- [Core Python](core-python.md)
- [Development Tools](development-tools.md)
- [Local Packages](local-packages.md)

## Analysis Status

### ✅ Completed Detailed Analysis
- **Core Python** - Complete with usage patterns, necessity, and compensation analysis
- **Development Tools** - Complete with usage patterns, necessity, and compensation analysis
- **Local Packages** - Complete with usage patterns, necessity, and compensation analysis

### 🔄 In Progress
- **Detailed Usage Analysis**: Continuing to analyze specific usage patterns for each dependency
- **File Location Mapping**: Adding specific file paths and line numbers for dependencies with <5 usage locations

### 📋 Pending
- **Documentation Links**: Adding official documentation and repository links for each dependency
- **Version Analysis**: Comparing current versions with latest stable versions
- **Upgrade Paths**: Documenting upgrade requirements and breaking changes

## Key Findings

### Critical Dependencies (Cannot be removed without major refactoring)
- **pycall** (1.4.1) - Ruby-Python bridge (5 files)
- **pytest** (7.4.3) - Testing framework (50+ files)
- **ruff** (0.1.6) - Linting and formatting (10+ files)

### High-Impact Dependencies (Significant refactoring required)
- **coverage** (7.3.2) - Code coverage (15+ files)
- **uv** (0.1.44) - Python package manager (5+ files)

### Local Workspace Packages
- **pycdo** - Local CDO Python package
- **neighborhood** - Local neighborhood package
- **pythonlab_setup** - Local Python lab setup
- **unittest_runner** - Local test runner

## Analysis Methodology

Each dependency analysis includes:
- **Usage**: Description of how the dependency is used
- **Files**: Count of files using the dependency
- **Key locations**: Specific file paths and line numbers (for <5 files)
- **Necessity**: Criticality assessment (CRITICAL/HIGH/MEDIUM/LOW)
- **Compensation if removed**: What would be needed to replace the dependency
- **Documentation**: Links to official documentation and GitHub repositories
- **Current version**: Version currently in use
- **Latest stable**: Latest stable version available
- **Upgrade path**: Notes on upgrade requirements and breaking changes

## Notes

- File counts are based on automated searches and may need manual verification
- Version recommendations should be verified against current project requirements
- Some dependencies may have indirect usage through other libraries
- Analysis is ongoing and will be updated as more information is gathered

---

*Last updated: Initial analysis phase completed*