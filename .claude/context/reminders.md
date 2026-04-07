# Project Context Reminders / Recordatorios de Contexto

> Auto-loaded at session start via SessionStart hook.
> Last updated: [UPDATE THIS DATE]

---

## Project structure

- **Root**: shared Claude config, knowledge base, plans, scripts
- Always open Claude Code from the project root

## Rules (summary — see `.claude/rules/` for details)

- **Organization** (`organizacion.md`): mandatory directory structure, all skills in `.claude/skills/`
- **Language** (`idioma.md`): project language configurable (es/en), Spanish accents mandatory
- **Security** (`seguridad.md`): never hardcode secrets, OWASP Top 10, validate inputs
- **Quality** (`calidad.md`): prompt-contract before implementing, agent-review after

## Knowledge base

- **Research & findings**: `docs/knowledge/` with index at `INDEX.md`
  - Subcategories: competitors, market, methodology, regulations, technology
- **Actionable plans**: `docs/plans/` with checkboxes
- **Query**: `/consultar-conocimiento [topic]` or `/query-knowledge [topic]`

## Key skills

| Skill | Trigger (es) | Trigger (en) |
|-------|-------------|-------------|
| Prompt contract | `/prompt-contract`, "contrato" | `/prompt-contract`, "contract" |
| Agent review | "auto-revisión" | "review this", `/agent-review` |
| Systematic review | `/revision-sistematica` | `/systematic-review` |
| Gemini code review | `/revisar-codigo-gemini` | `/review-code-gemini` |
| Gemini consultation | `/consultar-gemini` | `/ask-gemini` |
| Knowledge query | `/consultar-conocimiento` | `/query-knowledge` |
| Status report | `/generar-informe` | `/generate-report` |
| Fix spelling | `/corregir-ortografia` | `/fix-spelling` |
| Multi-agent consensus | "consenso" | "consensus", `/stochastic-multi-agent-consensus` |
| Model debate | "debate de modelos" | "model chat", `/model-chat` |

## MCPs

- Not installed by default. See `setup/mcp-catalog.md` for recommendations.
- To activate: copy `.mcp.json.example` to `.mcp.json` and uncomment servers.
