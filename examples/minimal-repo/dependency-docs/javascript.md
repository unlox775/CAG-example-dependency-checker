# JavaScript Dependencies

Frontend (Vite + React) for the contact form and API client.

## Core UI

- [x] **react**
  - **Necessity**: **CRITICAL**
  - UI framework. Used in `frontend/src/main.jsx`, `App.jsx`, `components/ContactForm.jsx`.

- [x] **react-dom**
  - **Necessity**: **CRITICAL**
  - React DOM renderer. Used in `frontend/src/main.jsx`.

- [x] **clsx**
  - **Necessity**: **LOW**
  - Utility for conditional class names. Used in `frontend/src/App.jsx`.

## Forms and Validation

- [x] **react-hook-form**
  - **Necessity**: **HIGH**
  - Form state management. Used in `frontend/src/components/ContactForm.jsx`.

- [x] **@hookform/resolvers**
  - **Necessity**: **HIGH**
  - Zod resolver for react-hook-form. Used in `frontend/src/components/ContactForm.jsx`.

- [x] **zod**
  - **Necessity**: **HIGH**
  - Schema validation for form data. Used in `frontend/src/components/ContactForm.jsx`.

## HTTP and Data

- [x] **axios**
  - **Necessity**: **HIGH**
  - HTTP client for API requests. Used in `frontend/src/api/client.js`.

- [x] **date-fns**
  - **Necessity**: **MEDIUM**
  - Date formatting. Used in `frontend/src/components/ContactForm.jsx`, `utils/format.js`.

- [x] **lodash**
  - **Necessity**: **MEDIUM**
  - Debounce and utility functions. Used in `frontend/src/components/ContactForm.jsx`.

- [x] **uuid**
  - **Necessity**: **MEDIUM**
  - Generate unique IDs for form submissions. Used in `frontend/src/components/ContactForm.jsx`.

## Dev Dependencies

- [x] **vite**
  - **Necessity**: **CRITICAL**
  - Build tool and dev server. Used in `frontend/vite.config.js`.

- [x] **@vitejs/plugin-react**
  - **Necessity**: **HIGH**
  - Vite plugin for React. Used in `frontend/vite.config.js`.

- [x] **vitest**
  - **Necessity**: **MEDIUM**
  - Unit test runner.

- [x] **@testing-library/react**
  - **Necessity**: **LOW**
  - React component testing utilities.
