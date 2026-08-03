---
title: Catálogo de skills de la comunidad
date: 2026-08-03
category: technology
tags: [skills, claude-code, comunidad, plugins]
status: complete
---

# Catálogo de skills de la comunidad

> Skills populares de terceros que se instalan desde GitHub.
> Claude puede recomendar los más relevantes durante la inicialización según el proyecto.
> Instalar con: `claude skills add owner/repo`

## Metodología y workflow

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **Superpowers** | `obra/superpowers` | Metodología completa: brainstorm → spec → worktrees → TDD → code review con sub-agentes | 40.9k stars |
| **Karpathy Guidelines** | `multica-ai/andrej-karpathy-skills` | 4 principios: pensar antes de codear, simplicidad, cambios quirúrgicos, orientado a objetivos | 144k stars |
| **Caveman** | `JuliusBrussee/caveman` | Reduce tokens ~65% eliminando narración innecesaria, conserva hechos técnicos | 68.1k stars |
| **Context Mode** | `mksglu/context-mode` | Filtra ruido de shell output, restaura estado tras resets | 16.3k stars |
| **Handoff** | `mattpocock/skills` | Comprime sesiones en markdown para continuar en nuevas sesiones | Popular |
| **Grill Me** | `mattpocock/skills` | Entrevista al usuario antes de codear para surfacear suposiciones | 156k installs |

## Frontend y diseño

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **Frontend Design** | `anthropics/skills` | UI distintiva, sistema de diseño opinionado (oficial Anthropic) | 277k installs |
| **Vercel React Best Practices** | `vercel-labs/agent-skills` | 57 reglas de performance para React/Next.js | 133k installs/semana |
| **Vercel Web Design Guidelines** | `vercel-labs/agent-skills` | 100+ reglas de accesibilidad y UX | Parte de Vercel suite |
| **Vercel Composition Patterns** | `vercel-labs/agent-skills` | Compound components vs boolean prop proliferation | Parte de Vercel suite |
| **SwiftUI Design** | `wholiver/swiftui-design-skill` | Guía de SwiftUI con quality review | Comunidad |
| **Impeccable** | (comunidad) | Diseño opinionado con defaults estéticos | 40k stars |

## Seguridad

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **Trail of Bits Security** | `trailofbits/skills` | CodeQL, Semgrep, variant analysis para detección de vulnerabilidades | Top 3 Q2 2026 |
| **VibeSec** | (comunidad) | Prevención de vulnerabilidades con guía proactiva | Comunidad |
| **OWASP Security** | (comunidad) | Compliance con OWASP Top 10:2025, 20+ quirks de lenguajes | Comunidad |
| **Defense in Depth** | (comunidad) | Testing de seguridad multi-capa | Comunidad |

## Documentos y datos

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **PDF** | `anthropics/skills` | Crear, editar, extraer texto/tablas de PDFs | Oficial Anthropic |
| **DOCX** | `anthropics/skills` | Crear y editar Word con formato y tracked changes | Oficial Anthropic |
| **XLSX** | `anthropics/skills` | Crear y analizar Excel con fórmulas | Oficial Anthropic |
| **PPTX** | `anthropics/skills` | Crear y editar PowerPoint | Oficial Anthropic |
| **Doc-Coauthoring** | `anthropics/skills` | Escritura colaborativa con aprobación por secciones | Oficial Anthropic |
| **D3.js Visualization** | `chrisvoncsefalvay/claude-d3js-skill` | Visualizaciones de datos interactivas | Comunidad |
| **Markdown → EPUB** | `smerchek/claude-epub-skill` | Convertir markdown a ebooks | Comunidad |

## Testing y QA

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **Webapp Testing** | `anthropics/skills` | Testing de apps web con Playwright | Oficial Anthropic |
| **Playwright Skill** | `lackeyjb/playwright-skill` | Automatización de testing E2E | Comunidad |
| **iOS Simulator** | `conorluddy/ios-simulator-skill` | Testing/debugging de apps iOS | Comunidad |

## Cloud e infraestructura

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **AWS Skills** | `zxkane/aws-skills` | AWS CDK y patrones serverless | Comunidad |
| **Remotion Best Practices** | `remotion-dev/skills` | Generación programática de video con React | 117k installs/semana |

## Meta-tooling

| Skill | Repo | Descripción | Popularidad |
|-------|------|-------------|-------------|
| **Skill Creator** | `anthropics/skills` | Genera nuevos skills con Q&A interactivo | Oficial Anthropic |
| **MCP Builder** | `anthropics/skills` | Scaffolding de servidores MCP | Oficial Anthropic |

## Colecciones curadas

| Colección | Repo | Descripción |
|-----------|------|-------------|
| **awesome-claude-skills** | `BehiSecc/awesome-claude-skills` | Lista curada con 9.9k stars, 11 categorías |
| **ComposioHQ** | `ComposioHQ/awesome-claude-skills` | Otra lista curada popular |
| **Claude AI Skills Collection 2026** | `obviousworks/Claude-AI-skills-collection-2026` | 94 skills en 15 categorías |
| **agentskill.sh** | (web) | Directorio buscable de 69,000+ skills |

## Notas

- **8-12 skills bien elegidos** cubren la mayoría del día de un desarrollador senior
- **Mantener los bodies < 500 tokens** para no desperdiciar contexto
- **Auditar mensualmente**: eliminar skills que no se hayan usado en 30 días
- **Skills globales** (`~/.claude/skills/`) vs **skills de proyecto** (`.claude/skills/`): usar globales para preferencias personales, de proyecto para el equipo
