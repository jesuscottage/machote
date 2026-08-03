# Machote — Claude Code Project Template

Plantilla universal para inicializar cualquier proyecto con Claude Code y construirlo de forma ordenada y eficiente.

Proporciona estructura, reglas, skills, y herramientas desde el primer minuto — para que Claude trabaje con contexto, organización y criterio desde la sesión cero.

## Qué incluye

### Configuración de Claude

| Componente | Ubicación | Descripción |
|------------|-----------|-------------|
| **4 reglas compartidas** | `.claude/rules/` | Organización obligatoria, idioma, seguridad (OWASP), calidad de código |
| **26 skills curados** | `.claude/skills/` | Desarrollo, multi-agente, investigación, planning, seguridad, testing, diseño, contenido, automatización, meta-tooling |
| **1 agente investigador** | `.claude/agents/` | Investigación de tecnologías, competidores, regulaciones con persistencia en knowledge base |
| **1 comando de commit** | `.claude/commands/` | Commit semántico + push + PR (bilingüe) |
| **Contexto automático** | `.claude/context/` | `reminders.md` se auto-inyecta en cada sesión |

### Estructura del proyecto

| Directorio | Propósito |
|------------|-----------|
| `docs/knowledge/` | Base de conocimiento persistente con `INDEX.md` obligatorio. Categorías: competitors, market, methodology, regulations, technology |
| `docs/plans/` | Planes accionables con checkboxes y tracking de progreso |
| `docs/reviews/` | Revisiones de código y consultas (se crean según necesidad) |
| `scripts/` | Scripts reutilizables (corrección ortográfica, fuentes de hooks) |
| `.tmp/` | Archivos temporales — scripts de un solo uso, capturas de debugging, CSVs intermedios. Gitignored, nunca se commitean |

### Catálogo de MCPs

`docs/knowledge/technology/mcp-catalog.md` — catálogo exhaustivo de 150+ servidores MCP organizados en 25 categorías (desarrollo, bases de datos, cloud, CI/CD, comunicación, etc.). No se instalan por defecto; Claude recomienda los más relevantes durante la inicialización según el stack del proyecto.

### Hooks opcionales

`docs/knowledge/technology/hooks-reference.md` — referencia técnica de 3 hooks que Claude ofrece durante la inicialización:

| Hook | Qué hace |
|------|----------|
| **Sonido al terminar** | Beeps cuando Claude termina de responder |
| **Sonido de notificación** | Beeps cuando Claude pide atención |
| **Pre-commit Gitleaks** | Bloquea commits con credenciales filtradas (API keys, tokens, passwords) |

## Cómo usarlo

### 1. Clonar

```bash
git clone https://github.com/{owner}/machote.git my-project
cd my-project
rm -rf .git
git init
```

### 2. Abrir Claude Code

**Siempre abrir desde la raíz del proyecto.** Las reglas solo se cargan desde la raíz.

En la primera sesión, Claude ejecuta automáticamente el flujo de inicialización descrito en `CLAUDE.md`:
- Configura el idioma
- Personaliza los archivos del proyecto
- Recomienda MCPs según el stack
- Ofrece hooks opcionales
- Transforma `CLAUDE.md` y `README.md` al contexto del proyecto real

### 3. Adaptar a un proyecto existente

También funciona para proyectos con código existente. Decirle a Claude qué proyecto es y que se quiere adaptar — Claude sigue las reglas de adaptación aditiva en `docs/knowledge/methodology/adaptacion-proyecto-existente.md`.

La adaptación es **estrictamente aditiva**: solo crea carpetas nuevas, nunca toca código, configs, .env, Docker, CI/CD ni dependencias existentes.

---

## Skills destacados

### Desarrollo y calidad
- `/prompt-contract` — Contrato estructurado antes de implementar
- `/agent-review` — Sub-agentes revisan automáticamente post-implementación
- `/reverse-prompt` — Preguntas clarificadoras (previene suposiciones)
- `/consultar-modelos` — Consultar Gemini + GPT como revisores externos
- `/security-audit` — Auditoría OWASP Top 10 (inspirado en Trail of Bits)
- `/test-webapp` — Testing de apps web con Playwright

### Planning, investigación y documentación
- `/plan` — Planes persistentes en markdown que sobreviven /clear
- `/generate-doc` — Generar specs, propuestas, reportes en markdown/HTML
- `/revision-sistematica` — Investigación académica exhaustiva (7 fases, 6 APIs)
- `/stochastic-multi-agent-consensus` — N agentes con consenso

### Diseño, contenido y meta-tooling
- `/diagram-generator` + `/excalidraw-flowchart` — Diagramas y flowcharts
- `/design-website` — Mockups HTML premium
- `/create-skill` — Meta-skill: crear nuevos skills interactivamente

---

## Estructura completa

```
project-root/
├── CLAUDE.md                     # Instrucciones para Claude (flujo de setup / contexto del proyecto)
├── README.md                     # Este archivo
├── .gitignore
├── .mcp.json.example             # Catálogo MCP (no activo por defecto)
├── .claude/
│   ├── rules/                    # Reglas compartidas
│   │   ├── organizacion.md       # Estructura obligatoria de directorios
│   │   ├── idioma.md             # Idioma + acentos en español
│   │   ├── seguridad.md          # OWASP, secretos, inputs
│   │   └── calidad.md            # Convenciones, testing, docs
│   ├── agents/
│   │   └── investigador.md       # Agente de investigación
│   ├── skills/                   # 26 skills organizados por categoría
│   ├── commands/
│   │   └── commit.md             # Commit semántico + push + PR
│   └── context/
│       └── reminders.md          # Contexto auto-inyectado en cada sesión
├── scripts/
│   ├── fix-spanish-ortho.sh      # Corrección ortográfica en español
│   ├── gitleaks-pre-commit.sh    # Fuente del hook pre-commit (se copia durante setup)
│   └── gitleaks.toml             # Configuración base de Gitleaks (se copia durante setup)
├── .tmp/                         # Archivos temporales (gitignored)
└── docs/
    ├── knowledge/
    │   ├── INDEX.md              # Índice de la knowledge base (obligatorio)
    │   ├── methodology/          # Frameworks, estándares, best practices
    │   └── technology/           # Stack, MCPs, hooks, decisiones de arquitectura
    └── plans/                    # Planes accionables con checkboxes
```

---

## Licencia

MIT
