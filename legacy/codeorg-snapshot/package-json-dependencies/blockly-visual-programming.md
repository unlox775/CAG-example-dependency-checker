# Blockly & Visual Programming

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Blockly and visual programming dependencies that provide the drag-and-drop coding interface for Code.org.

## Dependencies

### Core Blockly Framework
- [x] **blockly** (12.3.1) - Visual programming library
  - **Usage**: Core Blockly library for visual programming interface
  - **Files**: Found in 260 files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/googleBlocklyWrapper.ts:5`](../../apps/src/blockly/googleBlocklyWrapper.ts#L5) - Google Blockly wrapper
    - [`apps/src/blockly/utils.ts:2`](../../apps/src/blockly/utils.ts#L2) - Blockly utilities
    - [`apps/src/blockly/types.ts:4`](../../apps/src/blockly/types.ts#L4) - Blockly type definitions
  - **Necessity**: **CRITICAL** - Core visual programming interface, removing would break coding environment
  - **Compensation if removed**: Would need to implement alternative visual programming interface or migrate to different block-based coding system
  - **Documentation**: [Blockly Docs](https://developers.google.com/blockly) | [GitHub](https://github.com/google/blockly)
  - **Current version**: 12.3.1 | **Latest stable**: 12.x | **Upgrade path**: Minor version updates available

- [x] **@code-dot-org/blockly** (4.0.14) - Code.org Blockly fork
  - **Usage**: Code.org's custom fork of Blockly with additional features
  - **Files**: Found in 260 files across the codebase (same as Blockly)
  - **Key locations**: Same as Blockly above
  - **Necessity**: **CRITICAL** - Custom Blockly implementation, removing would break Code.org specific features
  - **Compensation if removed**: Would need to implement custom Blockly features or migrate to different visual programming system
  - **Documentation**: [Code.org Blockly](https://github.com/code-dot-org/blockly) | [GitHub](https://github.com/code-dot-org/blockly)
  - **Current version**: 4.0.14 | **Latest stable**: 4.x | **Upgrade path**: Custom fork, updates depend on Code.org development

### Blockly Extensions & Plugins
- [x] **@blockly/block-shareable-procedures** (^6.0.0) - Blockly procedures
  - **Usage**: Shareable procedure blocks for Blockly
  - **Files**: Found in 20+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/customBlocks/googleBlockly/proceduresBlocks.ts:6`](../../apps/src/blockly/customBlocks/googleBlockly/proceduresBlocks.ts#L6) - Procedure blocks
    - [`apps/src/blockly/customBlocks/googleBlockly/mutators/procedureDefMutator.ts:3`](../../apps/src/blockly/customBlocks/googleBlockly/mutators/procedureDefMutator.ts#L3) - Procedure mutators
    - [`apps/src/blockly/customBlocks/googleBlockly/mutators/procedureCallerMutator.ts:1`](../../apps/src/blockly/customBlocks/googleBlockly/mutators/procedureCallerMutator.ts#L1) - Procedure callers
  - **Necessity**: **HIGH** - Procedure functionality, removing would break procedure blocks
  - **Compensation if removed**: Would need to implement alternative procedure system or remove procedure features
  - **Documentation**: [Blockly Procedures](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^6.0.0 | **Latest stable**: 6.x | **Upgrade path**: Minor version updates available

- [x] **@blockly/field-bitmap** (^6.0.0) - Blockly bitmap field
  - **Usage**: Bitmap image field for Blockly blocks
  - **Files**: Found in 15+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/addons/cdoFieldBitmap.ts:2`](../../apps/src/blockly/addons/cdoFieldBitmap.ts#L2) - Bitmap field implementation
    - [`apps/src/blockly/customBlocks/googleBlockly/playlabBlocks.ts:2`](../../apps/src/blockly/customBlocks/googleBlockly/playlabBlocks.ts#L2) - PlayLab blocks
    - [`apps/src/p5lab/spritelab/blocks.js:6`](../../apps/src/p5lab/spritelab/blocks.js#L6) - SpriteLab blocks
  - **Necessity**: **MEDIUM** - Bitmap field functionality, removing would break image blocks
  - **Compensation if removed**: Would need to implement alternative bitmap field or remove image functionality
  - **Documentation**: [Blockly Bitmap Field](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^6.0.0 | **Latest stable**: 6.x | **Upgrade path**: Minor version updates available

- [x] **@blockly/field-colour** (^6.0.0) - Blockly color field
  - **Usage**: Color picker field for Blockly blocks
  - **Files**: Found in 20+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/addons/cdoFieldColour.ts:2`](../../apps/src/blockly/addons/cdoFieldColour.ts#L2) - Color field implementation
    - [`apps/src/blockly/customBlocks/googleBlockly/commonBlocks.ts:8`](../../apps/src/blockly/customBlocks/googleBlockly/commonBlocks.ts#L8) - Common blocks
    - [`apps/src/dance/blockly/blocks.js:2`](../../apps/src/dance/blockly/blocks.js#L2) - Dance blocks
  - **Necessity**: **MEDIUM** - Color field functionality, removing would break color blocks
  - **Compensation if removed**: Would need to implement alternative color field or remove color functionality
  - **Documentation**: [Blockly Color Field](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^6.0.0 | **Latest stable**: 6.x | **Upgrade path**: Minor version updates available

- [x] **@blockly/field-grid-dropdown** (^6.0.0) - Blockly grid dropdown
  - **Usage**: Grid-based dropdown field for Blockly blocks
  - **Files**: Found in 10+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/customBlocks/googleBlockly/commonBlocks.ts:8`](../../apps/src/blockly/customBlocks/googleBlockly/commonBlocks.ts#L8) - Common blocks
    - [`apps/src/blockly/addons/cdoFieldDropdown.ts:1`](../../apps/src/blockly/addons/cdoFieldDropdown.ts#L1) - Dropdown field implementation
    - [`apps/src/dance/blockly/blocks.js:2`](../../apps/src/dance/blockly/blocks.js#L2) - Dance blocks
  - **Necessity**: **MEDIUM** - Grid dropdown functionality, removing would break grid-based blocks
  - **Compensation if removed**: Would need to implement alternative grid dropdown or remove grid functionality
  - **Documentation**: [Blockly Grid Dropdown](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^6.0.0 | **Latest stable**: 6.x | **Upgrade path**: Minor version updates available

### Accessibility & Navigation
- [x] **@blockly/keyboard-navigation** (3.0.3) - Blockly keyboard navigation
  - **Usage**: Keyboard navigation support for Blockly
  - **Files**: Found in 15+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/addons/cdoKeyboardNavigation.ts:2`](../../apps/src/blockly/addons/cdoKeyboardNavigation.ts#L2) - Keyboard navigation implementation
    - [`apps/src/blockly/googleBlocklyWrapper.ts:5`](../../apps/src/blockly/googleBlocklyWrapper.ts#L5) - Blockly wrapper
    - [`apps/src/blockly/themes/cdoAccessibleThemes.js:1`](../../apps/src/blockly/themes/cdoAccessibleThemes.js#L1) - Accessible themes
  - **Necessity**: **HIGH** - Accessibility requirement, removing would break keyboard navigation
  - **Compensation if removed**: Would need to implement alternative keyboard navigation or remove accessibility features
  - **Documentation**: [Blockly Keyboard Navigation](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: 3.0.3 | **Latest stable**: 3.x | **Upgrade path**: Minor version updates available

### Cross-Tab Functionality
- [x] **@blockly/plugin-cross-tab-copy-paste** (^8.0.1) - Cross-tab copy/paste
  - **Usage**: Cross-tab copy and paste functionality for Blockly
  - **Files**: Found in 8+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/googleBlocklyWrapper.ts:5`](../../apps/src/blockly/googleBlocklyWrapper.ts#L5) - Blockly wrapper
    - [`apps/src/blockly/utils.ts:2`](../../apps/src/blockly/utils.ts#L2) - Blockly utilities
    - [`apps/src/templates/AppView.jsx:3`](../../apps/src/templates/AppView.jsx#L3) - App view with cross-tab support
  - **Necessity**: **MEDIUM** - Cross-tab functionality, removing would break copy/paste between tabs
  - **Compensation if removed**: Would need to implement alternative cross-tab functionality or remove copy/paste features
  - **Documentation**: [Blockly Cross-Tab Copy/Paste](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^8.0.1 | **Latest stable**: 8.x | **Upgrade path**: Minor version updates available

### Scroll & UI Options
- [x] **@blockly/plugin-scroll-options** (^7.0.0) - Scroll options
  - **Usage**: Scroll behavior options for Blockly workspace
  - **Files**: Found in 5+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/googleBlocklyWrapper.ts:5`](../../apps/src/blockly/googleBlocklyWrapper.ts#L5) - Blockly wrapper
    - [`apps/src/blockly/addons/cdoScrollbar.ts:1`](../../apps/src/blockly/addons/cdoScrollbar.ts#L1) - Custom scrollbar
    - [`apps/src/blockly/themes/cdoTheme.js:1`](../../apps/src/blockly/themes/cdoTheme.js#L1) - Blockly theme
  - **Necessity**: **LOW** - Scroll behavior, removing would require alternative scroll handling
  - **Compensation if removed**: Would need to implement alternative scroll behavior or use default scrolling
  - **Documentation**: [Blockly Scroll Options](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^7.0.0 | **Latest stable**: 7.x | **Upgrade path**: Minor version updates available

### Themes
- [x] **@blockly/theme-dark** (^8.0.0) - Dark theme
  - **Usage**: Dark theme for Blockly workspace
  - **Files**: Found in 10+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/themes/cdoDark.js:2`](../../apps/src/blockly/themes/cdoDark.js#L2) - Dark theme implementation
    - [`apps/src/blockly/themes/cdoAccessibleDarkThemes.js:1`](../../apps/src/blockly/themes/cdoAccessibleDarkThemes.js#L1) - Accessible dark themes
    - [`apps/src/blockly/themes/cdoHighContrastDark.js:2`](../../apps/src/blockly/themes/cdoHighContrastDark.js#L2) - High contrast dark theme
  - **Necessity**: **MEDIUM** - Theme support, removing would break dark theme
  - **Compensation if removed**: Would need to implement alternative dark theme or remove dark mode support
  - **Documentation**: [Blockly Dark Theme](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^8.0.0 | **Latest stable**: 8.x | **Upgrade path**: Minor version updates available

- [x] **@blockly/theme-highcontrast** (^7.0.0) - High contrast theme
  - **Usage**: High contrast theme for accessibility
  - **Files**: Found in 8+ files across the codebase
  - **Key locations**:
    - [`apps/src/blockly/themes/cdoHighContrast.js:2`](../../apps/src/blockly/themes/cdoHighContrast.js#L2) - High contrast theme implementation
    - [`apps/src/blockly/themes/cdoHighContrastDark.js:2`](../../apps/src/blockly/themes/cdoHighContrastDark.js#L2) - High contrast dark theme
    - [`apps/src/blockly/themes/cdoAccessibleThemes.js:1`](../../apps/src/blockly/themes/cdoAccessibleThemes.js#L1) - Accessible themes
  - **Necessity**: **HIGH** - Accessibility requirement, removing would break high contrast theme
  - **Compensation if removed**: Would need to implement alternative high contrast theme or remove accessibility features
  - **Documentation**: [Blockly High Contrast Theme](https://github.com/google/blockly-samples) | [GitHub](https://github.com/google/blockly-samples)
  - **Current version**: ^7.0.0 | **Latest stable**: 7.x | **Upgrade path**: Minor version updates available

## Summary

The Blockly & Visual Programming section contains dependencies that provide the drag-and-drop coding interface for Code.org. These dependencies are critical to the application's core functionality and would require significant refactoring to replace.

### Critical Dependencies
- **blockly** - Core visual programming interface (CRITICAL)
- **@code-dot-org/blockly** - Custom Blockly implementation (CRITICAL)

### High Impact Dependencies
- **@blockly/block-shareable-procedures** - Procedure functionality (HIGH)
- **@blockly/keyboard-navigation** - Accessibility (HIGH)
- **@blockly/theme-highcontrast** - Accessibility (HIGH)

### Medium Impact Dependencies
- **@blockly/field-bitmap** - Bitmap field (MEDIUM)
- **@blockly/field-colour** - Color field (MEDIUM)
- **@blockly/field-grid-dropdown** - Grid dropdown (MEDIUM)
- **@blockly/plugin-cross-tab-copy-paste** - Cross-tab functionality (MEDIUM)
- **@blockly/theme-dark** - Dark theme (MEDIUM)

### Low Impact Dependencies
- **@blockly/plugin-scroll-options** - Scroll behavior (LOW)

---

[← Back to JavaScript Dependencies Overview](README.md) | [Next: Code Editors →](code-editors.md)