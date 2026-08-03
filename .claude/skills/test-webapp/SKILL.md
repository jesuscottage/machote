---
name: test-webapp
description: Test a web application using Playwright browser automation. Navigates the app, tests flows, captures screenshots, and reports issues. Requires Playwright MCP or Playwright installed. Use when user says "test the app", "test webapp", "probar la app", "QA", or /test-webapp.
---

# Webapp Testing

> Inspired by Anthropic's official webapp-testing skill.
> Drives a real browser to validate a web app's functionality.

## Prerequisites

- Playwright MCP enabled, OR `npx playwright` available
- App running locally (e.g., `http://localhost:3000`)

## Process

### 1. Identify what to test

Ask or infer:
- App URL (default: `http://localhost:3000`)
- Key user flows to test (signup, login, CRUD, checkout, etc.)
- Known broken areas?

### 2. Create test plan

```markdown
## Test Plan — {app name}

| # | Flow | Steps | Expected result |
|---|------|-------|-----------------|
| 1 | Homepage loads | Navigate to / | Page renders, no console errors |
| 2 | Login flow | Fill form, submit | Redirect to dashboard |
| 3 | ... | ... | ... |
```

### 3. Execute tests

For each flow:
1. Navigate to the URL
2. Interact with elements (click, fill, submit)
3. Assert expected results (text present, redirect happened, no errors)
4. **Capture screenshot** on failure → save to `.tmp/test-screenshots/`
5. Check browser console for errors

### 4. Report

```markdown
## QA Report — {app name} ({date})

| # | Flow | Status | Notes | Screenshot |
|---|------|--------|-------|------------|
| 1 | Homepage | PASS | Loaded in 1.2s | — |
| 2 | Login | FAIL | 500 error on submit | .tmp/test-screenshots/login-fail.png |

### Issues found

1. **[HIGH]** Login returns 500 — `POST /api/auth/login` fails
2. **[LOW]** Missing alt text on hero image

### Console errors

- `TypeError: Cannot read property 'user' of undefined` at dashboard.js:34
```

### 5. Fix cycle

If user approves, fix the issues found and re-test the affected flows.
