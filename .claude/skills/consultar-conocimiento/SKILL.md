---
name: consultar-conocimiento
description: >
  Query the project's knowledge base (competitors, regulations, methodology, market, technology).
  Use when you need business context for product, pricing, security, or architecture decisions.
  Read only relevant documents, never all at once.
  Triggers: "/consultar-conocimiento", "/query-knowledge", "what do we know about", "qué sabemos sobre"
---

# Skill: /consultar-conocimiento | /query-knowledge

## When to use / Cuándo usar

Invoke with `/consultar-conocimiento [topic]` or `/query-knowledge [topic]`.
Examples:
- "What do we know about competitors?"
- "¿Qué sabemos sobre el pricing de competidores?"
- "Query knowledge about GDPR compliance"
- "¿Qué investigaciones tenemos sobre el método X?"

## Process / Proceso

### Step 1: Read the index
Read `docs/knowledge/INDEX.md` to see what documents are available.
Documents commented with `<!-- -->` have not been created yet.

### Step 2: Identify relevant documents
Based on the user's query, identify which existing (non-commented) documents are relevant.
If the query is broad, use Grep in `docs/knowledge/` to search by keywords in frontmatters.

### Step 3: Read only what's needed
Read only the documents identified as relevant.
**Never read all documents at once** — this wastes context.

### Step 4: Synthesize
Present the user a structured summary with:
- **Relevant findings** for their query
- **Sources** (indicate which document each piece of data comes from)
- **Information date** (from each document's frontmatter)
- **Identified gaps** — if information is missing on the topic, suggest running
  the researcher agent to find and store it

## Response format

```markdown
## Query: [requested topic]

### Available information
[Summary of findings, citing the source document]

### Sources consulted
- `docs/knowledge/[category]/[file].md` (date: YYYY-MM-DD)

### Missing information
[If no documents exist on the topic, or if information is outdated]
Suggestion: run the researcher agent to update.
```

## Rules

- Always start by reading INDEX.md, never guess what documents exist
- If a document doesn't exist yet (commented in INDEX), inform the user
- Respond in the project's configured language
- Do not fabricate information that isn't in the documents
- If information is > 3 months old, warn that it may be outdated
