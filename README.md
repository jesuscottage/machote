# Machote — Claude Code Project Template

Reusable repository template for organizing any project with Claude Code
in the most effective way possible.

## What's included

- **51 skills** organized by category (development, research, leads, YouTube, infrastructure)
- **4 shared rules** (organization, language, security, quality)
- **1 research agent** with knowledge base persistence
- **1 semantic commit command** (bilingual)
- **Knowledge management** with mandatory indexes
- **MCP catalog** (25 categories, 150+ servers, not installed by default)

## Quick setup

### 1. Clone

```bash
git clone https://github.com/jesuscottage/machote.git my-project
cd my-project
rm -rf .git
git init
```

### 2. Activate MCPs (optional)

```bash
cp .mcp.json.example .mcp.json
# Edit .mcp.json: uncomment the servers you need
```

See `docs/knowledge/technology/mcp-catalog.md` for the complete catalog with descriptions.

### 3. Customize

1. Edit `CLAUDE.md` with your project's info (name, stack, structure)
2. Edit `.claude/context/reminders.md` with your specific context
3. Edit `.claude/rules/idioma.md`: change `idioma-principal` if needed (default: `es`)
4. Add business rules in `.claude/rules/negocio.md` (create new file)
5. Populate `docs/knowledge/` with your research

### 4. Open Claude Code

**Always open from the project root.** The rules only load from the root.

---

## Adapt to an existing project

This template also works for existing projects. Tell Claude what your project is
and that you want to adapt it — Claude will follow the adaptation rules in
`docs/knowledge/methodology/adaptacion-proyecto-existente.md` automatically.

The adaptation is **strictly additive**: only creates new folders, never touches
your code, configs, .env, Docker, CI/CD, or dependencies.

---

## Featured skills

### For ANY development project
- `/prompt-contract` — Contract before implementing (prevents rework)
- `/agent-review` — Automatic review post-implementation
- `/reverse-prompt` — Clarifying questions (prevents assumptions)
- `/revision-sistematica` — Exhaustive academic research (7 phases, 6 APIs)
- `/consultar-conocimiento` — Query your knowledge base
- `/generar-informe` — Project status report
- `/stochastic-multi-agent-consensus` — Poll N agents for decisions
- `/model-chat` — Debate between Claude instances

### For agencies / freelancers
- Gmail, leads, Instantly, proposals, onboarding skills
- YouTube skills (outliers, thumbnails, metadata, tracking)
- `/design-website` — HTML mockups for prospects

### For complex decisions
- `/stochastic-multi-agent-consensus` — Poll of N agents with consensus aggregation
- `/model-chat` — Multi-instance debate with synthesis
- `/consultar-gemini` — Architecture consultations with Gemini as second brain

---

## Claude's persistent memory

Claude automatically stores persistent memory in:
```
~/.claude/projects/{project-hash}/memory/
```

Recommended organization:
- `MEMORY.md` — Memory index
- `feedback_*.md` — User feedback on Claude's behavior
- `project_*.md` — Project information (stack, state, decisions)
- `reference_*.md` — External references (repos, URLs, contacts)

This is automatic — you don't need to create it manually.

---

## Project structure explained

| Directory | Purpose |
|-----------|---------|
| `.claude/rules/` | Shared rules that Claude must follow |
| `.claude/skills/` | ALL skills — one folder per skill with SKILL.md |
| `.claude/agents/` | Agent definitions (researcher, etc.) |
| `.claude/commands/` | Custom slash commands (/commit, etc.) |
| `.claude/context/` | Context auto-injected at session start |
| `docs/knowledge/` | Persistent knowledge base with INDEX.md |
| `docs/plans/` | Actionable plans with progress tracking |
| `docs/reviews/` | Code reviews and consultations (created as needed) |
| `scripts/` | Auxiliary scripts (orthography fix, etc.) |
| `docs/knowledge/technology/` | MCP catalog, architecture decisions, stack docs |

---

## License

MIT
