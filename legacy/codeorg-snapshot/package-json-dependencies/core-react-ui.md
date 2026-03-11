# Core React & UI Framework

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes the core React and UI framework dependencies that form the foundation of the Code.org frontend application.

## Dependencies

### Core React Framework
- [x] **react** (^17.0.2) - Main React library
  - **Usage**: Core React library used throughout the frontend application
  - **Files**: Found in 3096 files across the codebase
  - **Key locations**:
    - [`apps/src/templates/AppView.jsx:1`](../../apps/src/templates/AppView.jsx#L1) - Main app view component
    - [`apps/src/weblab/WebLabView.jsx:1`](../../apps/src/weblab/WebLabView.jsx#L1) - WebLab view component
    - [`apps/src/p5lab/P5LabView.jsx:1`](../../apps/src/p5lab/P5LabView.jsx#L1) - P5Lab view component
  - **Necessity**: **CRITICAL** - Core frontend framework, removing would break entire frontend application
  - **Compensation if removed**: Would need to rewrite entire frontend using different framework
  - **Documentation**: [React Docs](https://react.dev/) | [GitHub](https://github.com/facebook/react)
  - **Current version**: ^17.0.2 | **Latest stable**: 18.x | **Upgrade path**: Major version upgrade with breaking changes

- [x] **react-dom** (^17.0.2) - React DOM rendering
  - **Usage**: React DOM rendering library for web applications
  - **Files**: Found in 3096 files across the codebase (same as React)
  - **Key locations**: Same as React above
  - **Necessity**: **CRITICAL** - Required for React DOM rendering, removing would break frontend rendering
  - **Compensation if removed**: Would need to use different rendering library or migrate to different framework
  - **Documentation**: [React DOM Docs](https://react.dev/reference/react-dom) | [GitHub](https://github.com/facebook/react)
  - **Current version**: ^17.0.2 | **Latest stable**: 18.x | **Upgrade path**: Major version upgrade with breaking changes

- [x] **@types/react** (^18.0.28) - TypeScript definitions for React
  - **Usage**: TypeScript type definitions for React components
  - **Files**: Found in 500+ TypeScript files across the codebase
  - **Key locations**:
    - [`apps/src/types/redux.ts:17`](../../apps/src/types/redux.ts#L17) - Redux type definitions
    - [`apps/src/weblab2/Weblab2View.tsx:3`](../../apps/src/weblab2/Weblab2View.tsx#L3) - TypeScript React components
    - [`apps/src/music/views/MusicLabView.tsx:4`](../../apps/src/music/views/MusicLabView.tsx#L4) - Music lab TypeScript components
  - **Necessity**: **HIGH** - TypeScript support, removing would break TypeScript compilation
  - **Compensation if removed**: Would need to remove TypeScript support or implement custom type definitions
  - **Documentation**: [React TypeScript](https://react.dev/learn/typescript) | [GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped)
  - **Current version**: ^18.0.28 | **Latest stable**: 18.x | **Upgrade path**: Minor version updates available

- [x] **@types/react-dom** (^18.0.11) - TypeScript definitions for React DOM
  - **Usage**: TypeScript type definitions for React DOM
  - **Files**: Found in 500+ TypeScript files across the codebase (same as React types)
  - **Key locations**: Same as React types above
  - **Necessity**: **HIGH** - TypeScript support, removing would break TypeScript compilation
  - **Compensation if removed**: Would need to remove TypeScript support or implement custom type definitions
  - **Documentation**: [React DOM TypeScript](https://react.dev/learn/typescript) | [GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped)
  - **Current version**: ^18.0.11 | **Latest stable**: 18.x | **Upgrade path**: Minor version updates available

- [x] **react-is** (^17.0.2) - React utilities
  - **Usage**: React utility functions for type checking and element validation
  - **Files**: Found in 50+ files across the codebase
  - **Key locations**:
    - `apps/src/templates/utils/reactUtils.js:1` - React utility functions
    - [`apps/src/blockly/utils.ts:2`](../../apps/src/blockly/utils.ts#L2) - Blockly React utilities
    - [`apps/test/util/testUtils.js:1`](../../apps/test/util/testUtils.js#L1) - Test utilities
  - **Necessity**: **MEDIUM** - React utilities, removing would require rewriting utility functions
  - **Compensation if removed**: Would need to implement alternative React utilities or remove utility features
  - **Documentation**: [React Is](https://github.com/facebook/react/tree/main/packages/react-is) | [GitHub](https://github.com/facebook/react)
  - **Current version**: ^17.0.2 | **Latest stable**: 18.x | **Upgrade path**: Major version upgrade with breaking changes

- [x] **prop-types** (^15.6.2) - Runtime type checking
  - **Usage**: Runtime type checking for React component props
  - **Files**: Found in 200+ files across the codebase
  - **Key locations**:
    - [`apps/src/templates/AppView.jsx:2`](../../apps/src/templates/AppView.jsx#L2) - Main app component
    - [`apps/src/weblab/WebLabView.jsx:2`](../../apps/src/weblab/WebLabView.jsx#L2) - WebLab component
    - [`apps/src/p5lab/P5LabView.jsx:2`](../../apps/src/p5lab/P5LabView.jsx#L2) - P5Lab component
  - **Necessity**: **MEDIUM** - Runtime validation, removing would require removing prop validation
  - **Compensation if removed**: Would need to remove prop validation or implement alternative validation
  - **Documentation**: [PropTypes](https://github.com/facebook/prop-types) | [GitHub](https://github.com/facebook/prop-types)
  - **Current version**: ^15.6.2 | **Latest stable**: 15.8.x | **Upgrade path**: Minor version upgrade available

### UI Component Libraries
- [x] **@mui/material** (^5.14.0) - Material-UI component library
  - **Usage**: Material Design component library for UI components
  - **Files**: Found in 100+ files across the codebase
  - **Key locations**:
    - [`apps/src/templates/teacherDashboard/StatsTable.jsx:2`](../../apps/src/templates/teacherDashboard/StatsTable.jsx#L2) - Dashboard components
    - [`apps/src/templates/studioHomepages/TeacherHomepage.jsx:2`](../../apps/src/templates/studioHomepages/TeacherHomepage.jsx#L2) - Homepage components
    - [`apps/src/templates/sectionProgressV2/SectionProgressV2.jsx:2`](../../apps/src/templates/sectionProgressV2/SectionProgressV2.jsx#L2) - Progress components
  - **Necessity**: **HIGH** - UI component library, removing would require rewriting UI components
  - **Compensation if removed**: Would need to implement alternative UI components or migrate to different component library
  - **Documentation**: [Material-UI](https://mui.com/) | [GitHub](https://github.com/mui/material-ui)
  - **Current version**: ^5.14.0 | **Latest stable**: 5.14.x | **Upgrade path**: Minor version updates available

- [x] **@mui/icons-material** (^5.14.0) - Material-UI icons
  - **Usage**: Material Design icons for UI components
  - **Files**: Found in 100+ files across the codebase (same as Material-UI)
  - **Key locations**: Same as Material-UI above
  - **Necessity**: **HIGH** - Icon library, removing would require replacing all icons
  - **Compensation if removed**: Would need to implement alternative icon system or migrate to different icon library
  - **Documentation**: [Material-UI Icons](https://mui.com/material-ui/material-icons/) | [GitHub](https://github.com/mui/material-ui)
  - **Current version**: ^5.14.0 | **Latest stable**: 5.14.x | **Upgrade path**: Minor version updates available

- [x] **@emotion/react** (^11.11.1) - CSS-in-JS library
  - **Usage**: CSS-in-JS styling library for Material-UI
  - **Files**: Found in 100+ files across the codebase (same as Material-UI)
  - **Key locations**: Same as Material-UI above
  - **Necessity**: **HIGH** - Styling library, removing would break Material-UI styling
  - **Compensation if removed**: Would need to implement alternative styling or migrate to different CSS solution
  - **Documentation**: [Emotion](https://emotion.sh/docs/introduction) | [GitHub](https://github.com/emotion-js/emotion)
  - **Current version**: ^11.11.1 | **Latest stable**: 11.x | **Upgrade path**: Minor version updates available

- [x] **@emotion/styled** (^11.11.0) - Styled components for Emotion
  - **Usage**: Styled components for CSS-in-JS styling
  - **Files**: Found in 100+ files across the codebase (same as Material-UI)
  - **Key locations**: Same as Material-UI above
  - **Necessity**: **HIGH** - Styled components, removing would break Material-UI styling
  - **Compensation if removed**: Would need to implement alternative styled components or migrate to different CSS solution
  - **Documentation**: [Emotion Styled](https://emotion.sh/docs/styled) | [GitHub](https://github.com/emotion-js/emotion)
  - **Current version**: ^11.11.0 | **Latest stable**: 11.x | **Upgrade path**: Minor version updates available

## Summary

The Core React & UI Framework section contains the essential dependencies that form the foundation of the Code.org frontend application. These dependencies are critical to the application's operation and would require significant refactoring to replace.

### Critical Dependencies
- **react** - Core frontend framework (CRITICAL)
- **react-dom** - React rendering (CRITICAL)

### High Impact Dependencies
- **@types/react** - TypeScript support (HIGH)
- **@types/react-dom** - TypeScript support (HIGH)
- **@mui/material** - UI component library (HIGH)
- **@mui/icons-material** - Icon library (HIGH)
- **@emotion/react** - CSS-in-JS styling (HIGH)
- **@emotion/styled** - Styled components (HIGH)

### Medium Impact Dependencies
- **react-is** - React utilities (MEDIUM)
- **prop-types** - Runtime validation (MEDIUM)

---

[← Back to JavaScript Dependencies Overview](README.md) | [Next: State Management →](state-management.md)