# Consultation Prompt Template / Plantilla de Prompt — Consulta a Gemini

> **Usage**: Claude generates a prompt using this template → user pastes in Gemini → Gemini deposits its analysis.
> **Variables to replace**: `{TITLE}`, `{ROLE}`, `{DOMAIN}`, `{BRIEF_DESCRIPTION}`, `{CONTEXT}`, `{QUESTION}`, `{CONSTRAINTS}`, `{REPORT_PATH}`

---

## Full template

````markdown
# Consultation: {TITLE}

## Your role

You are a **{ROLE}** with extensive experience in **{DOMAIN}**.

Project: **{PROJECT_NAME}** — {BRIEF_DESCRIPTION}

## Project context

{CONTEXT}

## Question / Decision to evaluate

{QUESTION}

## Constraints to consider

{CONSTRAINTS}

## What I expect from your response

Structure your response as follows:

### 1. Analysis of the current situation
- What is the real state of the problem/decision?
- What risks or gaps exist?

### 2. Viable options
For each option (min. 2, max. 4):
- **Description**: What this option entails
- **Pros**: Concrete advantages
- **Cons**: Disadvantages and risks
- **Estimated effort**: Low / Medium / High
- **Viability**: High / Medium / Low (given the context)

### 3. Reasoned recommendation
- Which option do you recommend and why?
- Under what conditions would you change your recommendation?

### 4. Risks of the recommended option
- What could go wrong?
- How to mitigate each risk?

### 5. Concrete action plan
If your recommendation is accepted, list specific steps:
1. Step 1 (which files to touch, what to change)
2. Step 2
3. ...

Be specific: mention files, functions, concrete configurations when possible.

## Output instruction

**IMPORTANT**: When done, save the complete response directly to this file:

```
{REPORT_PATH}
```
````

---

## Variables

| Variable | Description | Example |
|---|---|---|
| `{TITLE}` | Descriptive consultation title | `WebSockets vs polling for notifications` |
| `{ROLE}` | Expert role assigned to Gemini | `software architect`, `SaaS auditor`, `GCP specialist` |
| `{DOMAIN}` | Relevant area of expertise | `distributed systems`, `web app security`, `SaaS pricing` |
| `{PROJECT_NAME}` | Your project name | `My-Project` |
| `{BRIEF_DESCRIPTION}` | One line describing the project | `SaaS platform for X with Y` |
| `{CONTEXT}` | Relevant project information | Code, docs, current state — only what's needed |
| `{QUESTION}` | The question or decision to evaluate | Clear, scoped, unambiguous |
| `{CONSTRAINTS}` | Technical, business, or time limitations | Current stack, budget, deadlines |
| `{REPORT_PATH}` | Path where Gemini deposits its response | `docs/reviews/{name}/reportes/consulta-01-topic.md` |

---

## Common roles (quick reference)

| Query type | Suggested role | Domain |
|---|---|---|
| Stack/tooling decision | Senior software architect | Distributed systems, cloud |
| User flow / UX | SaaS application auditor | UX research, product design |
| Cloud infrastructure | Cloud platform specialist | AWS, GCP, Azure |
| Security / compliance | Security and compliance auditor | OWASP, GDPR, PCI-DSS |
| Pricing / business | B2B SaaS product consultant | Pricing, GTM, unit economics |
| Performance | Performance engineer | Profiling, caching, query optimization |
| Database | Senior DBA | PostgreSQL, indexing, schema migration |
