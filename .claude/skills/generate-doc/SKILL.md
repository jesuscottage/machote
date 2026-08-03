---
name: generate-doc
description: Generate structured documents (reports, proposals, specs, presentations) as markdown or HTML. Supports export-ready formatting with tables, diagrams, and sections. Use when user says "generate document", "create report", "generar documento", "write a spec", "crear informe", or /generate-doc.
---

# Document Generator

> Inspired by Anthropic's official document skills (PDF, DOCX, PPTX).
> Creates structured documents in markdown or HTML — export-ready for any format.

## Process

### 1. Identify document type

| Type | Structure | Output |
|------|-----------|--------|
| **Technical spec** | Problem, solution, architecture, API, trade-offs | Markdown |
| **Project proposal** | Executive summary, scope, timeline, budget, risks | Markdown/HTML |
| **Status report** | Progress, blockers, metrics, next steps | Markdown |
| **Presentation outline** | Slides with title, key points, speaker notes | Markdown |
| **Runbook** | Step-by-step procedures for operations | Markdown |
| **Custom** | User-defined structure | Markdown/HTML |

### 2. Gather content

- Ask the user for key information or infer from project context
- Read relevant files from `docs/knowledge/`, `docs/plans/`, or codebase
- If generating from existing data, summarize don't copy

### 3. Generate

Structure with:
- **YAML frontmatter** (title, date, author, status)
- **Executive summary** (3-5 lines, the TL;DR)
- **Body** with numbered sections, tables, and diagrams where useful
- **Next steps / recommendations** at the end

### 4. Output

Save to the appropriate location:
- Technical docs → `docs/knowledge/{category}/`
- Reports → `docs/reviews/` or `docs/plans/`
- Temporary/one-off → `.tmp/`

If saving to knowledge base, update `docs/knowledge/INDEX.md`.

### 5. Export-ready HTML (optional)

If the user needs a presentable document, generate self-contained HTML with:
- Clean typography (system fonts)
- Print-friendly styles (`@media print`)
- Tables with borders
- Save to `.tmp/{name}.html`
