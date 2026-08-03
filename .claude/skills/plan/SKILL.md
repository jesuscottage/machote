---
name: plan
description: Create and maintain persistent markdown plans that survive /clear, context loss, and session changes. Plans live in docs/plans/ and track progress with checkboxes. Use when starting a complex task, when user says "plan this", "create a plan", "planificar", or /plan.
---

# Persistent Planning

> Inspired by planning-with-files (community top 3, Q2 2026).
> Plans persist as markdown files — they survive /clear, compacts, and new sessions.

## When to trigger

- User starts a complex multi-step task
- User says "plan this", "planificar", "create a plan", "/plan"
- Task will require more than 3-5 steps

## Process

### 1. Create the plan file

```
docs/plans/{descriptive-name}.md
```

### 2. Structure

```markdown
# Plan: {Title}

> Created: {date}
> Status: in-progress | completed | paused
> Owner: Claude + {user}

## Goal

{One paragraph: what success looks like}

## Steps

- [ ] Step 1 — {description}
- [ ] Step 2 — {description}
- [ ] Step 3 — {description}
...

## Decisions

| Decision | Option chosen | Why |
|----------|--------------|-----|

## Notes

{Context, blockers, open questions}
```

### 3. Keep it alive

- **Update checkboxes in real-time** as steps complete
- **Add steps** discovered during implementation
- **Log decisions** so future sessions have context
- **Mark completed** when all steps are done
- On context loss or new session: **read the plan first** to recover state

### 4. For master plans

If the plan is large (10+ steps), create a master plan that links to sub-plans:

```markdown
## Sub-plans

- [x] [Phase 1: Setup](phase-1-setup.md)
- [ ] [Phase 2: Implementation](phase-2-implementation.md)
- [ ] [Phase 3: Testing](phase-3-testing.md)
```

Sub-plans go in `docs/plans/{master-plan-name}/`.
