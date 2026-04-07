# Code Review Prompt Template / Plantilla de Prompt — Revisión de Código con Gemini

> **Usage**: Claude generates a prompt using this template → user pastes in Gemini → Gemini deposits the report.
> **Variables to replace**: `{NN}`, `{AREA}`, `{STACK}`, `{FOCUS}`, `{REPORT_PATH}`, `{FILES}`

---

## Full template

````markdown
# Code Review — Batch {NN}: {AREA}

## Instructions

You are a senior code reviewer for this project.
Stack: {STACK}

Your job is to review: **{FOCUS}**

**Review looking for:**
1. Logic bugs and edge cases
2. Security vulnerabilities (OWASP Top 10, XSS, injection, auth bypass, exposed sensitive data)
3. Business rule violations (see context below)
4. Performance issues (unnecessary renders, N+1 queries, memory leaks, event loop blocking)
5. Type inconsistencies (do frontend types match what the backend sends?)
6. Incomplete error handling or silenced exceptions
7. Race conditions in async operations
8. Dead code or unused imports
9. Broken conventions (naming, project patterns)

**Business rule invariants** (violations = HIGH severity):
{PROJECT_BUSINESS_RULES}

**Security rules:**
{PROJECT_SECURITY_RULES}

**For each finding, report EXACTLY in this format:**

| # | Severity | File | Line | Category | Description | Fix suggestion |
|---|----------|------|------|----------|-------------|----------------|
| 1 | HIGH/MEDIUM/LOW | path/file.ext | NN | Security/Business/Performance/Types/UX-A11y/Quality | What's wrong | How to fix it |

**DO NOT report:**
- Generated library code (e.g., shadcn/ui components)
- Translation/localization files
- Dependencies in package.json/requirements.txt
- Subjective style preferences
- Explicit TODOs already documented
- Missing tests (unless specifically requested)

If you find no significant issues, respond: "APPROVED — no significant findings."

## Output instruction

**IMPORTANT**: When done, save the complete report directly to this file:

```
{REPORT_PATH}
```

The file should contain ONLY your report with the findings table (or the APPROVED message). Do not include the source code you reviewed.

---

## Code to review

{FILES}
````

---

## Variables

| Variable | Description | Example |
|---|---|---|
| `{NN}` | Batch number (2 digits) | `01`, `02` |
| `{AREA}` | Functional area of the batch | `Types and transport`, `HTTP Services` |
| `{STACK}` | Relevant stack for this batch | `Next.js 16 + TypeScript + React 19` |
| `{FOCUS}` | Description of what's being reviewed | `Auth, billing, and settings type definitions` |
| `{REPORT_PATH}` | Path where Gemini deposits the report | `docs/reviews/{review}/reportes/lote-01-types.md` |
| `{FILES}` | Source code with `### path/file.ext` + code block | See batch files |
| `{PROJECT_BUSINESS_RULES}` | Project-specific business invariants | Add your project's rules here |
| `{PROJECT_SECURITY_RULES}` | Project-specific security rules | Add your project's security rules |

---

## Notes

- For mixed batches (frontend + backend), indicate both stacks
- Max ~2,500 lines per batch to avoid truncation in Gemini
- Each file should have its relative path as `###` header
