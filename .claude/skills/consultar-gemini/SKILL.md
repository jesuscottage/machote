# Skill: /consultar-gemini | /ask-gemini

> Consult Gemini as a second brain for architecture, flow, product, or strategy decisions.
> Claude generates a structured prompt → user pastes in Gemini → Claude reads the response, synthesizes, and proposes an actionable plan.
> **Principle**: Gemini analyzes and opines. Claude synthesizes, decides, and executes.

## Usage / Uso

```
/consultar-gemini [topic or question]
/ask-gemini [topic or question]
```

**Examples:**
```
/consultar-gemini WebSockets vs polling for real-time notifications?
/ask-gemini Best GCP practices for our processing pipeline
/consultar-gemini Validate the complete user onboarding flow
/ask-gemini Should we migrate from Cloud Run to GKE for LLM processing?
```

---

## Use cases

- **Architecture**: Decide between technical approaches
- **User flows**: Validate end-to-end journeys
- **Product**: Evaluate pricing strategies, features, positioning
- **Best practices**: Get recommendations on GCP, security, performance
- **Trade-offs**: Analyze pros and cons of decisions
- **Audits**: Walk through the app looking for gaps

---

## Full flow / Flujo completo

### Step 1 — Understand the query

Identify:
- **Central topic/question**: What needs to be resolved or evaluated?
- **Query type**: Technical decision | Flow validation | Best practices | Audit | Strategy
- **Ideal role for Gemini**: Software architect | SaaS auditor | GCP specialist | Product consultant | etc.

### Step 2 — Gather relevant context

Read only what Gemini needs:
- Relevant source code (specific files, not the whole repo)
- Knowledge base documents (`docs/knowledge/`)
- Existing plans (`docs/plans/`)
- CLAUDE.md of the relevant subproject
- Business rules (`.claude/rules/`)
- Related previous reviews (`docs/reviews/`)

### Step 3 — Create folder structure

```
docs/reviews/{name}-consulta/
├── prompts/
│   └── consulta-{NN}-{topic}.md
└── reportes/
    ├── consulta-{NN}-{topic}.md     # Raw Gemini response (user deposits)
    └── reporte-{NN}-{topic}.md      # Processed report by Claude
```

### Step 4 — Generate prompt for Gemini

Create the prompt using the template in [plantilla-prompt-decisiones.md](plantilla-prompt-decisiones.md).

### Step 5 — Instructions to the user

Show:
```
Consultation prepared for Gemini.
Prompt at: docs/reviews/{name}/prompts/consulta-{NN}-{topic}.md

Instructions:
1. Open the prompt file
2. Copy all content
3. Paste it in Gemini (Antigravity UI or gemini.google.com)
4. Copy Gemini's response
5. Deposit it in: docs/reviews/{name}/reportes/consulta-{NN}-{topic}.md
6. Let me know and I'll process the response
```

---

## Processing Gemini's response

### Step 6 — Read and synthesize

Claude reads Gemini's response and:
1. **Extracts what's valuable**: genuine insights, concrete data, unconsidered risks
2. **Discards noise**: generic recommendations, context repetition, obvious statements
3. **Contrasts with the project**: does the recommendation apply given our stack, constraints, and current state?
4. **Corrects inaccuracies**: note if Gemini assumed something incorrect about the project

### Step 7 — Generate action plan

Claude generates a concrete plan with:
- Specific, executable actions (edit file X, create component Y, update config Z)
- Prioritization (what to do first)
- Which actions Claude can execute automatically vs. which require user intervention

### Step 8 — Present to user and request confirmation

### Step 9 — Execute (if user accepts)

### Step 10 — Generate final report

---

## Query types and suggested roles

| Type | Role for Gemini | Focus |
|------|-----------------|-------|
| **Technical decision** | Senior software architect | Options, trade-offs, scalability |
| **Flow validation** | SaaS application auditor | Complete journey, gaps, UX |
| **Best practices** | {technology} specialist | Patterns, anti-patterns, config |
| **Audit** | Security and compliance auditor | OWASP, GDPR, gaps |
| **Strategy** | SaaS product consultant | Pricing, positioning, competitors |
| **Performance** | Performance engineer | Bottlenecks, metrics, optimization |

---

## Difference with `/revisar-codigo-gemini`

| Aspect | `/revisar-codigo-gemini` | `/consultar-gemini` |
|--------|--------------------------|---------------------|
| **Input** | Source code in batches | Question + relevant context |
| **Gemini output** | Findings table (severity, line, fix) | Argued analysis with options |
| **Claude action** | Verify FP + fix code | Synthesize + propose action plan |
| **Result** | Fixed code + findings report | Documented decision + applied changes |
| **Re-review** | Up to 3 rounds per batch | Normally 1 round (can iterate) |
