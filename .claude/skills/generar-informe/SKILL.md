---
name: generar-informe
description: >
  Generate a structured report of the current project state, roadmap progress,
  accumulated tech debt, and recommended next steps. Useful for planning sessions,
  stakeholder updates, or sprint retrospectives.
  Triggers: "/generar-informe", "/generate-report", "/status-report", "informe de estado", "status report"
---

# Skill: /generar-informe | /generate-report

## When to use / Cuándo usar

Invoke with `/generar-informe [type]` or `/generate-report [type]`.
Available types:
- `/generar-informe estado` | `/generate-report status` — current project state
- `/generar-informe sprint` | `/generate-report sprint` — sprint change summary
- `/generar-informe tecnico` | `/generate-report technical` — detailed technical report
- `/generar-informe stakeholder` | `/generate-report stakeholder` — non-technical executive version

## Process / Proceso

### Step 1: Gather current state

```bash
# Code state (adapt commands to your stack)
# For JS/TS projects:
npm run lint 2>&1 | tail -20
npm run build 2>&1 | tail -20

# For Python projects:
ruff check . 2>&1 | tail -20
python -m pytest --co -q 2>&1 | tail -10

# Tech debt
grep -rn "TODO\|FIXME\|HACK" src/ --include="*.ts" --include="*.tsx" --include="*.py" | wc -l

# Existing tests
find src -name "*.test.*" -o -name "*.spec.*" -o -name "test_*" | wc -l
```

Also read:
- `CLAUDE.md` — project structure and known issues
- `docs/plans/` — active plans and progress
- `docs/knowledge/INDEX.md` — available research

### Step 2: Verify roadmap progress

If `docs/plans/` contains master plans with checkboxes, count completed vs pending tasks.

### Step 3: Generate report

## Templates by type

### Type: status
```markdown
# Project Status — [project name] — [date]

## Executive summary
[2-3 paragraphs on general state]

## Roadmap progress
### Phase 1: [name] [X/Y tasks]
- ✅ Completed task
- ❌ Pending task

## Quality metrics
- Open TODOs in code: X
- Existing tests: X
- Lint errors: X
- Type errors: X

## Top 5 tech debt
1. ...

## Next 3 recommended steps
1. ...
```

### Type: stakeholder
```markdown
# [Project] — Product Update — [month year]

## What was achieved?
[No jargon, what works today that didn't before]

## What's next?
[Upcoming features in business language]

## Identified risks
[Only critical ones, in non-technical language]

## When will it be ready for users?
[Honest estimate based on the roadmap]
```

### Type: technical
Additionally include:
- Bundle size analysis if available
- Test coverage
- Dependency vulnerabilities (`npm audit` / `pip audit`)
- Comparison against security checklist

## Rules

- Always base on the real state of the code — do not assume
- Be honest about progress — neither excessively optimistic nor pessimistic
- Separate facts (the code does X) from opinions (this is tech debt because...)
- Output in the project's configured language
