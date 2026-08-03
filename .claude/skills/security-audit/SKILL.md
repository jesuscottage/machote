---
name: security-audit
description: Run a security audit of the codebase focusing on OWASP Top 10, secrets exposure, dependency vulnerabilities, and auth/input handling. Inspired by Trail of Bits methodology. Use when user says "security audit", "auditoría de seguridad", "check security", "review vulnerabilities", or /security-audit.
---

# Security Audit

> Inspired by Trail of Bits security skills (community top 3, Q2 2026).
> Complements `.claude/rules/seguridad.md` — the rule prevents issues, this skill finds existing ones.

## Process

### 1. Scope

Ask the user or infer:
- Full codebase or specific area? (auth, payments, API, etc.)
- Which language/framework?
- Any known concerns?

### 2. Automated checks

Run what's available in the project:

```bash
# Dependencies
npm audit 2>/dev/null || pip audit 2>/dev/null || true

# Secrets in git history
gitleaks git --no-banner -v 2>/dev/null || true

# Linting with security rules (if configured)
# eslint --rule 'security/*' or semgrep --config auto
```

### 3. Manual review (OWASP Top 10)

For each applicable category, review code:

| # | Category | What to check |
|---|----------|--------------|
| A01 | Broken Access Control | Route guards, role checks, IDOR, path traversal |
| A02 | Cryptographic Failures | Hardcoded secrets, weak hashing, plaintext storage |
| A03 | Injection | SQL injection, command injection, XSS, template injection |
| A04 | Insecure Design | Missing rate limiting, no input validation at boundaries |
| A05 | Security Misconfiguration | Debug mode in prod, default credentials, verbose errors |
| A07 | Auth Failures | Token storage (localStorage vs HttpOnly), session management |
| A08 | Data Integrity | Unsigned updates, unvalidated deserialization |
| A09 | Logging Failures | PII in logs, missing audit trail, no alerting |
| A10 | SSRF | Unvalidated URLs, internal service exposure |

### 4. Report

Output as a table:

```markdown
## Security Audit Report — {project} ({date})

### Findings

| # | Severity | Category | File:Line | Finding | Recommended fix |
|---|----------|----------|-----------|---------|-----------------|
| 1 | HIGH | A03 | src/api.ts:42 | SQL concatenation | Use parameterized query |

### Summary

- **Critical/High**: {count} — must fix before deploy
- **Medium**: {count} — fix in next sprint
- **Low/Info**: {count} — nice to have
- **Dependencies**: {count} vulnerabilities from `npm audit`

### Next steps

1. {Prioritized action items}
```

### 5. Save report

Save to `docs/reviews/security-audit-{date}/` following the project review structure.
