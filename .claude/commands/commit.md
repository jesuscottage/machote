---
description: Generate a semantic commit, push, and optionally open a PR / Genera un commit semántico, hace push y opcionalmente abre PR
allowed-tools: Bash
---

Execute the following git flow for the current repository changes.

Optional argument: `$ARGUMENTS` (can be: empty, `no-push`, `pr`).

**Push is always done by default.** Use `no-push` for local commit only.

## Steps

### 1. Review current state

```bash
git status
git diff --stat
```

Identify what files have changed. If nothing is staged, review which files
should be included in this commit.

### 2. Stage relevant files (if staging is empty)

Add modified files selectively. **NEVER** use `git add -A` or `git add .`.
Never add:
- `.env*` files
- `node_modules/`
- Large binary files
- `package-lock.json` if `package.json` wasn't modified
- `__pycache__/` or `.pyc` files

Use `git add [file1] [file2] ...` with specific paths.

### 3. Generate commit message

Analyze staged changes and generate a commit message following
[Conventional Commits](https://www.conventionalcommits.org) in the
project's configured language (see `.claude/rules/idioma.md`):

```
type(scope): brief imperative description (max 72 chars)

More detailed description if necessary. Explain the "why",
not the "what" (the diff already shows the what).

- Additional point if there are multiple relevant changes
- Another point if applicable

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Valid types:**
- `feat`: new feature
- `fix`: bug fix
- `security`: security change
- `refactor`: refactoring without behavior change
- `docs`: documentation only
- `chore`: config, dependencies
- `test`: new or fixed tests
- `style`: formatting, no logic change

If the change spans multiple areas, use the most representative scope or omit it.

### 4. Create the commit

```bash
git commit -m "$(cat <<'EOF'
[generated message]
EOF
)"
```

### 5. Push (always, unless argument includes "no-push")

```bash
git push origin HEAD
```

### 6. Open Pull Request (if argument includes "pr")

```bash
gh pr create --title "[PR title]" --body "$(cat <<'EOF'
## Summary

[2-3 bullet points of the change]

## How to test

[verification steps]

Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

## Usage examples

- `/commit` → commit + push (default)
- `/commit no-push` → local commit only, no push
- `/commit pr` → commit + push + open PR to main
