# CLAUDE.md — Machote (Claude Code Project Template)

> Reusable template for organizing any project with Claude Code.
> Primary language: configurable in `.claude/rules/idioma.md` (default: Spanish).
> See `README.md` for setup instructions.

## Configuración inicial del proyecto

Cuando se inicializa un proyecto desde este template, Claude DEBE completar los siguientes pasos en la primera sesión.

> **Adaptación de proyecto existente**: si el usuario quiere aplicar esta plantilla a un proyecto que ya tiene código y estructura propia, Claude DEBE consultar `docs/knowledge/methodology/adaptacion-proyecto-existente.md` y seguir las reglas de adaptación aditiva antes de ejecutar los pasos siguientes.

### 1. Idioma
Editar `.claude/rules/idioma.md` → cambiar `idioma-principal` a `es` o `en` según el proyecto.

### 2. Reminders
Editar `.claude/context/reminders.md` → actualizar la fecha y ajustar el resumen al proyecto.

### 3. Personalizar archivos del proyecto

La inicialización transforma los archivos del template al contexto del proyecto real.
Cada archivo tiene un **estado template** (antes) y un **estado proyecto** (después).

#### `CLAUDE.md` — Transformación

**Antes** (template): contiene el flujo de inicialización (estos 5 pasos).
**Después** (proyecto): contiene el contexto útil para Claude en el proyecto inicializado.

Reemplazar TODA la sección "Configuración inicial del proyecto" (desde `## Configuración inicial` hasta `---`) con:

```markdown
## {Nombre del proyecto}

> {Descripción de una línea}

**Stack**: {lenguajes, frameworks, DB, cloud, etc.}
**Repo**: {URL del repositorio}

## Contexto del proyecto

{Descripción del proyecto: qué hace, para quién, estado actual, decisiones clave}
```

**Conservar intactas** las secciones posteriores: Project Structure, Rules, Skills, Knowledge Management, Plans, MCPs — actualizando solo el nombre "Machote" por el nombre real del proyecto en el árbol de estructura.

#### `README.md` — Transformación

**Antes** (template): describe qué es Machote y todo lo que contiene la plantilla.
**Después** (proyecto): describe el proyecto real, conservando las secciones de estructura inherentes al diseño.

Reemplazar con:

```markdown
# {Nombre del proyecto}

{Descripción del proyecto}

## Stack

{Tabla o lista del stack técnico}

## Estructura del proyecto

{Conservar la tabla de directorios y su propósito — knowledge, scripts, .tmp, plans, etc.
 Estas secciones son parte del diseño del proyecto, no del template.}

## Desarrollo

{Instrucciones para desarrollar, correr, deployar — si aplica}
```

**Eliminar**: secciones específicas del template (Quick Setup de clonación, "Adapt to existing project", catálogo de skills del template).
**Conservar**: estructura de directorios, propósito de cada carpeta, reglas de organización.

#### `docs/knowledge/INDEX.md`

Actualizar la fecha. Las entradas existentes (mcp-catalog, adaptación, hooks-reference) son documentos del template y se mantienen como referencia.

### 4. MCPs y Skills recomendados

#### MCPs

Revisar `docs/knowledge/technology/mcp-catalog.md` (catálogo exhaustivo con 25 categorías y 150+ servidores MCP).
Según el stack y objetivo del proyecto, **recomendar al usuario los 3–5 MCPs más relevantes**.

Reglas:
- **Context7 siempre recomendado** para proyectos de desarrollo.
- Analizar el stack del proyecto (lenguaje, framework, DB, cloud, CI/CD) y sugerir MCPs que encajen.
- Máximo 3–5 MCPs para evitar consumo excesivo de tokens.
- Presentar una tabla con: nombre, qué aporta al proyecto, y si requiere API key.
- Preguntar al usuario si quiere activarlos y, si acepta, configurar `.mcp.json` automáticamente.
- Si el proyecto no tiene `.mcp.json`, crearlo a partir de `.mcp.json.example`.

#### Skills

El template incluye 26 skills locales. Según el proyecto, algunos pueden no ser relevantes y otros de la comunidad podrían aportar.

**Revisar los skills actuales** y recomendar:
- **Quitar** skills que no apliquen al proyecto (ej: `/algorithmic-art` en un backend puro, `/design-website` en un CLI tool).
- **Agregar** skills de la comunidad desde `docs/knowledge/technology/skills-catalog.md` (ej: Vercel React Best Practices para un proyecto Next.js, Trail of Bits para un proyecto con requisitos de seguridad).

Presentar así:
```
Según tu proyecto ({stack}), te recomiendo estos ajustes a los skills:

Quitar (no aplican):
- /algorithmic-art — no es un proyecto visual
- /design-website — no necesitas mockups HTML

Agregar (de la comunidad):
| Skill | Repo | Aporta |
|-------|------|--------|
| Vercel React Best Practices | vercel-labs/agent-skills | 57 reglas de performance para Next.js |
| Playwright Skill | lackeyjb/playwright-skill | Testing E2E avanzado |

¿Quieres que aplique estos cambios?
```

Para agregar skills de la comunidad: `claude skills add owner/repo`.
Para quitar skills locales: eliminar la carpeta de `.claude/skills/{name}/`.

### 5. Hooks opcionales

Presentar al usuario los hooks opcionales y preguntar cuáles desea activar.
Consultar `docs/knowledge/technology/hooks-reference.md` para la configuración exacta de cada hook.

Presentar así:

```
Este template incluye 3 hooks opcionales:

1. Sonido al terminar — beeps cuando termino de responder (para no estar mirando la pantalla)
2. Sonido de notificación — beeps cuando necesito tu atención (permisos, preguntas)
3. Pre-commit Gitleaks — bloquea commits que contengan API keys, tokens o credenciales filtradas

¿Cuáles quieres activar? (puedes elegir todos, algunos, o ninguno)
```

**Para hooks de sonido** (1 y/o 2):
- Crear o actualizar `.claude/settings.json` con la configuración del hook
- Si ya existe `.claude/settings.json`, hacer merge (no sobrescribir)
- Si el usuario ya tiene los hooks globalmente en `~/.claude/settings.json`, informar que no necesita duplicarlos

**Para Pre-commit Gitleaks** (3):
1. Verificar si `gitleaks` está instalado: ejecutar `command -v gitleaks`
2. Si NO está instalado: mostrar el comando según plataforma (`winget install Gitleaks.Gitleaks` / `brew install gitleaks`) y pedir que lo instale
3. Crear `.githooks/` y copiar el script: `cp scripts/gitleaks-pre-commit.sh .githooks/pre-commit && chmod +x .githooks/pre-commit`
4. Copiar configuración a la raíz: `cp scripts/gitleaks.toml .gitleaks.toml`
5. Activar: `git config core.hooksPath .githooks`
6. Verificar: `git config core.hooksPath` debe mostrar `.githooks`
7. Recordar al usuario que puede personalizar `.gitleaks.toml` con reglas de su stack

---

## Project Structure

```
Machote/
├── CLAUDE.md                     # This file — project instructions for Claude
├── README.md                     # Setup and usage instructions
├── .gitignore                    # Ignored files
├── .mcp.json.example             # MCP catalog (not active by default)
├── .claude/
│   ├── rules/                    # Shared rules
│   │   ├── organizacion.md       # MANDATORY: directory structure
│   │   ├── idioma.md             # Language + Spanish accents
│   │   ├── seguridad.md          # OWASP, secrets, inputs
│   │   └── calidad.md            # Conventions, testing, docs
│   ├── agents/
│   │   └── investigador.md       # Research agent
│   ├── skills/                   # 26 skills organized by category
│   ├── commands/
│   │   └── commit.md             # Semantic commit + push + PR
│   └── context/
│       └── reminders.md          # Auto-injected at session start
├── scripts/
│   ├── fix-spanish-ortho.sh      # Spanish orthography fix script
│   ├── gitleaks-pre-commit.sh    # Pre-commit hook source (copied during setup)
│   └── gitleaks.toml             # Gitleaks config source (copied during setup)
├── .tmp/                         # Temporary files — gitignored, never committed
└── docs/
    ├── knowledge/
    │   ├── INDEX.md              # Knowledge base index (mandatory)
    │   └── technology/
    │       ├── mcp-catalog.md    # Exhaustive MCP catalog (25 categories, 150+)
    │       ├── hooks-reference.md # Optional hooks reference (sound, gitleaks)
    │       └── skills-catalog.md  # Community skills catalog (40+ with repos)
    └── plans/                    # Actionable plans with checkboxes
```

## Rules

| Rule | File | What it defines |
|------|------|-----------------|
| Organization | `.claude/rules/organizacion.md` | **Mandatory** directory structure |
| Language | `.claude/rules/idioma.md` | Language setting + Spanish accents |
| Security | `.claude/rules/seguridad.md` | OWASP, secrets, inputs |
| Quality | `.claude/rules/calidad.md` | Conventions, testing, docs |

## Skills (26 total)

### Development & Quality

| Skill | Triggers (es) | Triggers (en) | Description |
|-------|--------------|---------------|-------------|
| `/prompt-contract` | "contrato", "prompt contract" | "contract", "prompt contract" | Structured contract before implementing |
| `/agent-review` | "auto-revisión", "revisar esto" | "review this", "self-review", "agent review" | Sub-agents review code post-implementation |
| `/reverse-prompt` | (auto on implementation) | (auto on implementation) | 5+ clarifying questions before implementing |
| `/consultar-modelos` | "consultar modelos", "preguntar a Gemini y GPT" | "ask models", "consult models" | Consult Gemini + GPT as external reviewers (3 modes) |
| `/revisar-codigo-gemini` | "revisar código con Gemini" | "review code with Gemini" | Code review with Gemini as reviewer |
| `/generar-informe` | "informe de estado" | "status report", "generate report" | Structured project status report |
| `/corregir-ortografia` | "corregir acentos" | "fix spelling", "fix accents" | Fix accents in markdown files |

### Multi-agent

| Skill | Triggers (es) | Triggers (en) | Description |
|-------|--------------|---------------|-------------|
| `/stochastic-multi-agent-consensus` | "consenso", "N agentes" | "consensus", "poll agents" | N agents analyze, aggregate by consensus |
| `/model-chat` | "debate de modelos" | "model chat", "agent debate" | 5+ instances debate in shared room |

### Research

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/revision-sistematica` | "búsqueda sistemática", "systematic review" | 7 phases, 6 APIs, PRISMA-S methodology |
| `/x-search` | "buscar en X/Twitter", "search X/Twitter" | Search X/Twitter with Grok API |

### Design & Diagrams

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/design-website` | "diseñar sitio web", "design website" | Premium HTML mockups |
| `/diagram-generator` | "generar diagrama", "generate diagram" | Hand-drawn style diagrams |
| `/excalidraw-flowchart` | "flowchart", "diagrama de flujo" | Excalidraw flowcharts |

### Planning & Documentation

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/plan` | "planificar", "plan this", "create a plan" | Persistent markdown plans that survive /clear and context loss |
| `/generate-doc` | "generar documento", "create report", "write a spec" | Structured documents (specs, proposals, reports) in markdown/HTML |
| `/outline-generator` | "outline", "course outline" | Structured outlines for courses, presentations |

### Security & Testing

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/security-audit` | "auditoría de seguridad", "security audit" | OWASP Top 10 audit, secrets, dependencies (inspired by Trail of Bits) |
| `/test-webapp` | "probar la app", "test webapp", "QA" | Test web apps with Playwright: flows, screenshots, console errors |

### Content & Learning

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/video-to-action` | (on YouTube link) | Extract actionable steps from YouTube videos |
| `/algorithmic-art` | "arte algorítmico", "generative art" | Algorithmic art with p5.js and seeded randomness |

### Meta-tooling

| Skill | Triggers | Description |
|-------|----------|-------------|
| `/create-skill` | "crear skill", "new skill", "build a skill" | Create new skills interactively with proper SKILL.md structure |

### Automation & Infrastructure

| Skill | Description |
|-------|-------------|
| `/browser-stealth` | Stealth browsing that bypasses bot detection |
| `/multi-agent-chrome` | Parallel browser automation with multiple Chrome instances |
| `/modal-deploy` | Deploy workflows to Modal as persistent HTTP endpoints |
| `/add-webhook` | Create Modal webhooks for event-driven execution |

## Knowledge Management

- **Research & findings**: `docs/knowledge/` with index at `INDEX.md`
- **Categories**: competitors, market, methodology, regulations, technology
- **Always update INDEX.md** when adding or removing documents

## Plans

- **Actionable plans**: `docs/plans/` with checkboxes
- **Master plans**: `plan-maestro-*.md` with sub-plan references
- **Track progress**: update checkboxes as tasks complete

## MCPs

Not installed by default. See `docs/knowledge/technology/mcp-catalog.md` for the complete catalog.
To activate: copy `.mcp.json.example` to `.mcp.json` and uncomment servers.
