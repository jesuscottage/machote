# Rule: Project Organization (Mandatory / Obligatoria)

**Priority**: Critical — this structure is mandatory, not a suggestion.

## Rule

Every project using this template MUST follow this directory structure.
Claude MUST place files in the correct location and MUST NOT create alternative structures.

## Directory structure

```
project-root/
├── CLAUDE.md                    # Project instructions for Claude (always at root)
├── .claude/
│   ├── settings.json            # Project hooks (PreToolUse, SessionStart)
│   ├── rules/                   # Shared rules (language, security, quality, business)
│   ├── agents/                  # Agent definitions (researcher, etc.)
│   ├── skills/                  # ALL skills live here — one folder per skill
│   │   └── {skill-name}/
│   │       ├── SKILL.md         # Skill definition (frontmatter + process)
│   │       └── scripts/         # Auxiliary scripts (Python, JS, Bash)
│   ├── commands/                # Custom slash commands
│   └── context/
│       └── reminders.md         # Auto-injected context at session start
│
├── docs/
│   ├── knowledge/               # Knowledge base — persistent research & findings
│   │   ├── INDEX.md             # MANDATORY index — always update when adding docs
│   │   ├── competitors/         # Competitor analysis
│   │   ├── market/              # Market research, pricing, segments
│   │   ├── methodology/         # Frameworks, standards, best practices
│   │   ├── regulations/         # GDPR, legal, compliance
│   │   └── technology/          # Stack, libraries, architecture decisions
│   ├── plans/                   # Actionable plans with checkboxes
│   │   ├── plan-maestro-*.md    # Master plans (contain sub-plan references)
│   │   └── {plan-name}/        # Sub-plans grouped by master plan
│   └── reviews/                 # Code reviews and consultations
│       └── {review-name}/
│           ├── TRACKING.md
│           ├── prompts/
│           └── reportes/
│
├── scripts/                     # Auxiliary scripts (orthography, generation, etc.)
├── setup/                       # Setup instructions (hooks, MCPs)
└── .mcp.json                    # Active MCP servers (optional)
```

## Mandatory behaviors

### Knowledge management
- **Every research finding** must be saved to `docs/knowledge/{category}/` with YAML frontmatter
- **Always update** `docs/knowledge/INDEX.md` when adding or removing documents
- **Never read all documents at once** — use the index to find relevant ones
- **Frontmatter format** for knowledge documents:
  ```yaml
  ---
  title: Document title
  date: YYYY-MM-DD
  category: competitors|market|methodology|regulations|technology
  tags: [tag1, tag2]
  status: draft|complete|outdated
  ---
  ```

### Plans
- **Master plans** (`plan-maestro-*.md`) contain high-level goals and link to sub-plans
- **Sub-plans** live in folders named after the master plan
- **Use checkboxes** (`- [ ]` / `- [x]`) to track progress
- **Update checkboxes** in real-time as tasks are completed

### Skills
- **All skills** must be inside `.claude/skills/{name}/SKILL.md`
- **Never place skills** outside of `.claude/skills/`
- **Skill frontmatter** must include `name`, `description`, and optionally `allowed-tools`

### Reviews
- **Code reviews** follow the structure: `docs/reviews/{name}/` with `TRACKING.md`, `prompts/`, `reportes/`
- **Tracking** documents progress per batch

### Temporary files
- **`.tmp/`** for throwaway files (gitignored)
- **`active/`** for in-progress work artifacts (gitignored)

## Adapting to existing projects

When adapting this structure to an existing project:
1. **Only ADD** — never modify or delete existing project files
2. **Never touch** code, configs, package.json, Docker, CI/CD, APIs, or .env files
3. If `.claude/settings.json` already exists, **merge** hooks (don't overwrite)
4. If `CLAUDE.md` already exists, **append** to it (don't replace)
5. If skills exist outside `.claude/`, **copy** them to the correct location (don't move until user confirms)
6. Present a list of proposed changes BEFORE executing
7. Wait for explicit user confirmation

## Why this matters

Without consistent organization:
- Skills get lost or duplicated
- Knowledge isn't indexed and can't be found
- Plans have no tracking
- New collaborators waste time understanding the structure
- Claude wastes context window re-discovering project layout each session
