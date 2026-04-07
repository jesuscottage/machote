---
name: corregir-ortografia
description: >
  Fix Spanish orthography in markdown files: missing accents, incorrect plural tildes,
  and common errors. Uses a script with a curated dictionary and word-boundaries to avoid
  false positives. Invoke on docs/knowledge/ or any directory/file with .md files.
  Triggers: "/corregir-ortografia", "/fix-spelling", "corregir acentos", "fix accents"
---

# Skill: /corregir-ortografia | /fix-spelling

## When to use / Cuándo usar

Invoke with `/corregir-ortografia [path]` or `/fix-spelling [path]` when you need to fix
Spanish orthography in markdown files. Examples:
- `/corregir-ortografia docs/knowledge/` — fix the entire knowledge base
- `/fix-spelling docs/knowledge/competidores/rayyan.md` — a specific file
- `/corregir-ortografia docs/plans/` — fix plans

## Process / Proceso

### Step 1: Dry-run
Run the script in read-only mode to see proposed changes:
```bash
bash scripts/fix-spanish-ortho.sh <path>
```

### Step 2: Review changes
Analyze the diff shown. Verify that:
- There are no false positives (English words modified, broken URLs)
- The changes are orthographically correct
- Code blocks are not modified

### Step 3: Apply
If changes are correct, run with `--apply`:
```bash
bash scripts/fix-spanish-ortho.sh --apply <path>
```

### Step 4: Post-application verification
Run grep to confirm no known errors remain:
```bash
grep -rn "revisiónes\|evaluaciónes\|decisiónes\|instituciónales\|publicaciónes" <path> || echo "✓ No incorrect plurals"
grep -rn "\banalisis\b\|\bmetodologia\b\|\binvestigacion\b" <path> || echo "✓ No missing accents"
```

### Step 5: Report
Inform the user how many files and corrections were applied.

## Rules

- Always run dry-run first before applying
- If the diff shows a false positive, do NOT apply — report to the user and adjust the script
- The script only modifies `.md` files
- It does not modify content inside code blocks (```)
- Category A substitutions (incorrect plurals like "revisiónes") are always safe
- Category B substitutions (missing accents) use word-boundary (`\b`) for safety
- Respond in the project's configured language

## Dictionary maintenance

If new words needing correction are found:
1. Add them to `scripts/fix-spanish-ortho.sh`
2. Category A: if the incorrect word is NEVER valid → direct substitution
3. Category B: if the unaccented word could exist in English → use `\b` word-boundary
4. Run dry-run to validate before applying
