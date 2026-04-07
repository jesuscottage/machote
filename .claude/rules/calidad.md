# Rule: Code Quality / Regla: Calidad de Código

**Priority**: High — applies to all code written or modified by Claude.

## Pre-implementation

- **Use `/prompt-contract`** before implementing any non-trivial task
- **Use `/reverse-prompt`** when requirements are ambiguous
- Define success criteria before writing code

## Code conventions

### Naming
- Follow the language's standard conventions:
  - **Python**: `snake_case` for functions/variables, `PascalCase` for classes
  - **TypeScript/JavaScript**: `camelCase` for functions/variables, `PascalCase` for classes/types
  - **CSS**: `kebab-case` for class names
  - **Files**: `kebab-case` for most files; `PascalCase` for component files (React)

### Documentation
- Write comments in the project's configured language (see `idioma.md`)
- Comment **why**, not **what** — the code should be self-explanatory
- Do not add comments to code you didn't change
- Do not add docstrings, type annotations, or comments beyond what was asked

### Error handling
- Handle errors at system boundaries (user input, external APIs, file I/O)
- Do not add defensive error handling for internal code that can't fail
- Use specific error types, not generic catches
- Log errors with context (what operation, what input, what happened)

## Post-implementation

- **Use `/agent-review`** after completing non-trivial implementations
- Run linting and type-checking before reporting "done"
- Verify that existing tests still pass

## Testing

- Write tests for non-trivial functionality when requested
- Follow the project's existing test patterns and frameworks
- Test both happy path and edge cases
- Never mock what you can test directly

## Git commits

- Use **Conventional Commits** format
- Write commit messages in the project's configured language
- Keep commits atomic — one logical change per commit
- Never commit `.env`, credentials, or large binaries

## Avoid over-engineering

- Only make changes that are directly requested or clearly necessary
- Don't add features, refactor code, or make "improvements" beyond what was asked
- Three similar lines of code is better than a premature abstraction
- Don't design for hypothetical future requirements
- Don't add error handling for scenarios that can't happen
