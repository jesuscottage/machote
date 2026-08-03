---
name: create-skill
description: Interactively create a new Claude Code skill with proper SKILL.md structure, frontmatter, and process definition. Meta-skill for extending the template. Use when user says "create a skill", "new skill", "crear skill", "build a skill", or /create-skill.
---

# Skill Creator

> Inspired by Anthropic's official skill-creator.
> Meta-skill that helps create new skills with the correct structure.

## Process

### 1. Interview (5 questions)

Ask the user:

1. **Name**: What should this skill be called? (kebab-case, e.g., `code-review`)
2. **Purpose**: What does it do in one sentence?
3. **Trigger**: When should it activate? (slash command, keyword, automatic?)
4. **Process**: What are the steps? (high-level, 3-7 steps)
5. **Output**: What does it produce? (report, code, file, action?)

### 2. Generate SKILL.md

Create `.claude/skills/{name}/SKILL.md`:

```markdown
---
name: {name}
description: {one-line description}. Use when {trigger conditions}.
---

# {Title}

> {Brief description of purpose}

## Process

### 1. {First step}

{Details}

### 2. {Second step}

{Details}

...
```

### 3. Validate

Check:
- [ ] Frontmatter has `name` and `description`
- [ ] Description includes trigger words/phrases
- [ ] Process has clear, actionable steps
- [ ] No overlap with existing skills (check `.claude/skills/`)
- [ ] Body is under 500 tokens (keep it lean)

### 4. If the skill needs scripts

Create auxiliary scripts in `.claude/skills/{name}/scripts/`:

```
.claude/skills/{name}/
├── SKILL.md
└── scripts/
    └── {script-name}.py
```

### 5. Confirm

Show the user the generated skill and ask for approval before finalizing.

## Guidelines

- **Keep skills focused**: one skill = one job
- **Under 500 tokens**: long skills waste context on every session
- **Triggers matter**: if Claude can't know when to use it, it won't be used
- **No overlap**: check existing skills first
