---
name: prompt-contract
description: >
  Generate a structured contract (GOAL/CONSTRAINTS/FORMAT/FAILURE) before implementing
  non-trivial tasks. Defines success, limits, output shape, and explicit failure conditions.
  Treat the contract as an engineering spec, not a suggestion.
  Triggers: "contract", "contrato", "prompt contract", /prompt-contract.
allowed-tools: AskUserQuestion, Read, Grep, Glob, Bash, Edit, Write, TodoWrite
---

# Skill: /prompt-contract

> Before implementing any non-trivial task, generate a structured contract that defines
> what success looks like, what's out of scope, what gets delivered, and what conditions mean it's NOT done.
> **Invocable as / Invocable como**: `/prompt-contract`, "contract", "contrato", "prompt contract"

## When to use / Cuándo usar

Invoke **before starting implementation** when the user asks to build, create, implement, or
refactor something non-trivial. Do NOT trigger for:
- Lookups, research, or information gathering
- Single-line fixes, typos, or obvious bugs
- Tasks where the user has provided exhaustive, specific instructions
- Pure conversational or informational requests

## Process / Proceso

### 1. Analyze the request (silent — no output to user)

Before generating the contract, silently identify:
- **Success metric**: What does "done" look like? Find a number or concrete deliverable.
- **Implicit assumptions**: What are you about to assume without being told?
- **Hard limits**: Language, dependencies, performance, integration with the rest of the project
- **Output shape**: What files, formats, structures will be produced?
- **Failure modes**: What shortcuts would you take if rushed? What edge cases would you skip?

### 2. Draft the contract

Write a 4-section contract:

```
## Contract / Contrato

GOAL / OBJETIVO: [Quantifiable success. Include a number or concrete deliverable.
                   "Working X" is not a goal. "X that handles Y at Z performance" is.]

CONSTRAINTS / RESTRICCIONES:
- [Hard limit 1 — language, deps, compatibility]
- [Hard limit 2 — performance, size, complexity ceiling]
- [Hard limit 3 — integration requirements, existing patterns to follow]
- [3-5 constraints is typical]

FORMAT / ENTREGABLES:
- [Exact files to produce, with paths]
- [What each file contains]
- [Style: type hints, tests, docstrings — only what's relevant]

FAILURE / FALLO (any of these = not done):
- [Specific shortcut you'd be tempted to take]
- [Edge case that must be handled, not skipped]
- [Integration point that must actually work, not just compile]
- [The "technically works but..." outcome you must avoid]
```

### 3. Present for approval

Show the contract to the user with `AskUserQuestion`:
- **"Approved, implement" (Recommended)** — Proceed using the contract as spec
- **"Needs changes"** — User provides feedback, revise the contract

One revision cycle max — if more feedback after that, incorporate and go.

### 4. Execute against the contract

Once approved:
1. Create a task list (TodoWrite) derived directly from the contract
2. Implement against the contract as a hard spec — not a guideline
3. Before marking complete, verify every FAILURE condition is avoided
4. The FAILURE section is a checklist: go through each item and confirm it doesn't apply

### 5. Self-verify

After implementation, before reporting done:
- Re-read the FAILURE section
- For each failure condition, confirm with evidence (test output, code inspection, or logic) that it's been avoided
- If any failure condition is met, fix it before reporting done
- Do NOT report "done with caveats" — either all failure conditions are clear, or you're not done

## Contract quality rules / Reglas de calidad

**GOAL must have a number or concrete deliverable.** Not "build a rate limiter" but "rate limiter handling 50K req/sec at <1ms p99."

**CONSTRAINTS must be hard limits, not preferences.** Not "should be fast" but "must respond in <200ms." Not "keep it simple" but "under 150 lines total."

**FORMAT must be exact.** Not "some tests" but "5+ tests in test_X.py." Not "well-documented" but "docstring with 2 usage examples."

**FAILURE must catch shortcuts.** Think: "If I were lazy or rushed, what would I skip?" That's your failure condition. Common ones:
- No test for the unhappy path
- Hardcoded values that should be configurable
- Works for the demo case but breaks on empty/null/large input
- Missing error handling at integration boundaries
- "Works on my machine" — no consideration of deployment context

## Example 1 (English)

User: "Build a token bucket rate limiter"

```
## Contract

GOAL: Token bucket rate limiter handling 50K req/sec at <1ms p99 latency per check.

CONSTRAINTS:
- Pure Python, no external dependencies
- Thread-safe without asyncio
- Must work as both decorator and context manager
- Under 100 lines total including tests

FORMAT:
- Single file: rate_limiter.py
- Includes dataclass config, implementation, and 5+ pytest tests
- Type hints on all public methods
- Docstring with usage examples

FAILURE (any of these = not done):
- No test for concurrent access
- Latency exceeds 1ms on 50K synthetic requests
- Allows >105% of rate limit through (5% tolerance)
- Missing edge case: what happens at exactly 0 remaining tokens
```

## Example 2 (Español)

Usuario: "Implementar el endpoint de compra de tokens extra"

```
## Contrato

OBJETIVO: Endpoint POST /api/v1/billing/purchase-tokens que debite vía Stripe
y acredite tokens atómicamente, manejando los paquetes de tokens definidos en el sistema.

RESTRICCIONES:
- FastAPI + SQLAlchemy 2.0 async (patrón repository del proyecto)
- Stripe SDK (nunca datos raw de tarjeta — solo paymentMethodId)
- Balance nunca puede exceder el tope de seguridad configurado
- Transacción atómica: si Stripe cobra pero la BD falla, reembolsar automáticamente

ENTREGABLES:
- `app/routers/billing.py` — nuevo endpoint POST /purchase-tokens
- `app/services/billing.py` — lógica de compra con validación de tope
- `app/schemas/billing.py` — PurchaseTokensRequest/Response
- Reporte breve de qué se implementó

FALLO (cualquiera de estos = NO está hecho):
- Se acreditan tokens sin confirmar el cobro de Stripe
- El balance puede exceder el tope después de la compra
- No se valida que el usuario tenga un paymentMethod activo antes de cobrar
- Error de Stripe devuelve 500 genérico en vez de error descriptivo al frontend
- No se usa transacción atómica (cobro y acreditación desincronizados)
```
