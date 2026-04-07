# Skill: /revisar-codigo-gemini | /review-code-gemini

> Code review with Gemini as an independent reviewer.
> Claude generates prompts per batch → the user pastes them in Gemini → Claude verifies findings and applies fixes.
> **Principle**: Gemini ONLY reports findings. Claude applies the fixes.

## Usage / Uso

```
/revisar-codigo-gemini [files, folder, or review name]
/review-code-gemini [files, folder, or review name]
```

**Examples:**
```
/revisar-codigo-gemini src/services/ src/types/
/review-code-gemini app/routers/
/revisar-codigo-gemini                          # Review changes in git diff
```

---

## Full flow / Flujo completo

### Step 1 — Identify files to review

If files/folder provided as argument, use those.
If not, get modified files with:
```bash
git diff --name-only HEAD
```
If no changes in HEAD:
```bash
git diff --name-only main
```

Read each identified file with the Read tool.

### Step 2 — Group into batches

Group files into **batches of ~2,500 lines** max (practical limit for Gemini without truncation).

Group by functional domain (e.g., models, services, routes, components, config).

### Step 3 — Create folder structure

```
docs/reviews/{review-name}/
├── TRACKING.md
├── prompts/
│   ├── lote-01-{area}.md
│   └── ...
└── reportes/
    ├── lote-01-{area}.md        # Raw Gemini report (user deposits here)
    ├── reporte-01-{area}.md     # Processed report by Claude (with verification)
    └── ...
```

### Step 4 — Generate prompts per batch

For each batch, create a prompt file in `prompts/lote-{NN}-{area}.md` using the template in [plantilla-prompt-codigo.md](plantilla-prompt-codigo.md).

The prompt contains:
1. **Instructions for Gemini** (role, what to look for, output format)
2. **Project business rules and security rules** (invariants to verify)
3. **Exclusions** (what NOT to report)
4. **Output instruction** (path where Gemini saves its report)
5. **Source code** of each file in the batch (with filename and numbered lines)

### Step 5 — Create TRACKING.md

Create tracking file with:
- Metadata (date, reviewer, stack, repo)
- Batch table: Batch | Area | Files | Lines | Prompt | Report | Status
- Usage instructions for the collaborator
- Summary findings table (updated as batches are processed)

### Step 6 — Instructions to the user

Show:
```
Review prepared: {N} batches ready.
Tracking at: docs/reviews/{name}/TRACKING.md

For each batch:
1. Open the prompt file (column "Prompt" in TRACKING.md)
2. Copy all content
3. Paste it in Gemini (Antigravity UI or gemini.google.com)
4. Copy Gemini's response
5. Deposit it in: docs/reviews/{name}/reportes/lote-{NN}-{area}.md
6. Let me know and I'll process the findings

You can do multiple batches at once — each prompt is independent.
```

---

## Processing Gemini reports

When the user reports they've deposited a report:

### Step 7 — Verify findings and filter false positives

**Critical step**: Claude verifies EACH finding against the actual source code before acting.

For each finding reported by Gemini:
1. **Read the exact file and line** mentioned
2. **Verify if the code is from the project or a library**
3. **Evaluate if the finding is valid** in context — consider:
   - Is it a deliberate pattern documented in CLAUDE.md or project conventions?
   - Is the "problem" actually a reasonable fallback or design decision?
   - Did the reviewer confuse a dev mock with production code?
   - Does the finding assume a different library version?
4. **Classify** as:
   - **Confirmed**: Real finding → proceed to fix
   - **False positive**: Discard with documented reason
   - **Reclassified**: Change severity with justification

### Step 8 — Fix confirmed issues

For each **confirmed** HIGH or MEDIUM finding:
1. Read the affected file
2. Apply the fix using Edit
3. Record what was fixed and why

**Do not fix** false positives or findings reclassified to LOW (list as optional improvements).

### Step 9 — Re-review (max 3 rounds)

If files were corrected, generate a new prompt ONLY with corrected files. The user repeats the cycle.

Repeat Steps 7-8 until:
- Clean round (no confirmed HIGH/MEDIUM findings), or
- 3 total rounds reached

### Step 10 — Generate final report per batch

Create file in `reportes/reporte-{NN}-{area}.md` with dashboard, findings table, false positives, corrections applied, and summary.

### Step 11 — Update tracking

Update `TRACKING.md`: mark batch as completed, register finding counts.

### Step 12 — Report to user

Show concise summary: files reviewed, original vs confirmed findings, corrections applied, next pending batch.

---

## Severity reference

| Severity | Criteria | Action |
|----------|----------|--------|
| **HIGH** | Security, business rule violation, data loss, production crash | Fix immediately |
| **MEDIUM** | Quality, incorrect types, degraded performance, broken UX | Fix in this review |
| **LOW** | Cosmetic, minor conventions, optional improvements | List, don't fix |

## Finding categories

| Category | Examples |
|----------|----------|
| **Security** | XSS, injection, auth bypass, sensitive data exposure |
| **Business** | Invariant violations, invalid states, incorrect calculations |
| **Performance** | N+1 queries, unnecessary renders, memory leaks |
| **Types** | Incorrect types, frontend↔backend inconsistencies |
| **UX/A11y** | Accessibility, keyboard navigation, ARIA, responsive |
| **Quality** | Dead code, unused imports, inconsistent naming |
