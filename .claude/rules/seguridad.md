# Rule: Security and Privacy / Regla: Seguridad y Privacidad

**Priority**: Critical — never compromise these rules for development convenience.

## Secrets and Environment Variables

- **Never hardcode secrets** — use environment variables in `.env.local`
- **`.env.local`** per subproject (not versioned, in `.gitignore`)
- Document each variable with section, origin, date, and purpose as a comment
- **`NEXT_PUBLIC_` prefix** (if using Next.js): only for public data (Firebase config, Stripe publishable key, API URLs)
- **Never use `NEXT_PUBLIC_` for**: secret keys, admin credentials, LLM tokens, DB connection strings, webhook secrets
- **Backend**: use `pydantic-settings` with `SecretStr` for API keys, passwords, and tokens
- **Production**: use cloud secret managers (GCP Secret Manager, AWS Secrets Manager, etc.)

### Strict rules

- **Do not log user data** with `console.log` in production
- **Strip logs** in production build
- **Do not include PII** in query keys (e.g., TanStack Query — visible in DevTools)
- **Do not share credentials** between services or environments (dev/staging/prod)
- **Do not put secrets** in query strings, URLs, Docker layers, or commits

## Authentication and Authorization

- **Verify tokens server-side** for all authenticated routes
- **Never store tokens in localStorage** — use HttpOnly cookies or session memory
- **Automatic token refresh** — handle expiration silently
- **Bearer token** in all authenticated requests: `Authorization: Bearer <token>`

## Inputs and XSS

- **Validate and sanitize** all user inputs before sending to the API (Zod, joi, etc.)
- **Do not use `dangerouslySetInnerHTML`** — if necessary, sanitize with DOMPurify first
- **Escape HTML** in any user-generated content displayed in the UI
- **Strict CSP** — include nonces for inline scripts

## Security Headers (if applicable)

Maintain these headers configured:
```
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-...'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=63072000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## GDPR / Privacy

- **Consent before non-essential cookies** — implement GDPR-compliant banner
- **No tracking without consent** — analytics only with explicit opt-in
- **Right to be forgotten**: when deleting account, clear localStorage and sessionStorage
- **Data minimization**: only request and store strictly necessary data

## Dependencies

- Run `npm audit` / `pip audit` before each release and resolve critical/high vulnerabilities
- Do not install dependencies from unverified sources
- Keep dependencies updated — review weekly

## OWASP Top 10 Vigilance

When reviewing or modifying code related to auth, payments, or user data handling,
**always verify** that none of the OWASP Top 10 vulnerabilities are introduced:
- A01 Broken Access Control
- A02 Cryptographic Failures
- A03 Injection
- A04 Insecure Design
- A07 Identification and Authentication Failures
- A08 Software and Data Integrity Failures
