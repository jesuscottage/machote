# Knowledge Base Index / Índice de Conocimiento

> Last updated / Última actualización: 2026-08-03
> Query: `/consultar-conocimiento [topic]` or `/query-knowledge [topic]`
> The researcher agent keeps this index updated.

---

## Categories / Categorías

| Folder | Content |
|--------|---------|
| `competitors/` | Direct and indirect competitor analysis |
| `market/` | TAM, segments, pricing benchmarks, trends |
| `methodology/` | Frameworks, best practices, standards |
| `regulations/` | GDPR, local laws, compliance |
| `technology/` | Stack, libraries, architecture decisions |

---

## Documents / Documentos

<!-- Add documents here as you research each topic -->
<!-- Format: | ID | `category/filename.md` | Title | Date | Brief description | -->

| ID | Path | Title | Date | Description |
|----|------|-------|------|-------------|
| 001 | `technology/mcp-catalog.md` | Catálogo exhaustivo de servidores MCP | 2026-08-03 | 25 categorías, 150+ servidores MCP verificados con comandos de instalación, descripción y requisitos |
| 002 | `methodology/adaptacion-proyecto-existente.md` | Reglas de adaptación a proyecto existente | 2026-08-03 | Protocolo aditivo para aplicar la plantilla a proyectos con código existente sin romper nada |
| 003 | `technology/hooks-reference.md` | Referencia de hooks opcionales | 2026-08-03 | Configuración de hooks de sonido (Stop, Notification) y pre-commit Gitleaks para detección de credenciales |
| 004 | `technology/skills-catalog.md` | Catálogo de skills de la comunidad | 2026-08-03 | Skills populares de terceros (Superpowers, Trail of Bits, Karpathy, Vercel, etc.) con repos y métricas |

---

## How to add documents / Cómo agregar documentos

1. Create a file in the appropriate category folder (e.g., `docs/knowledge/technology/my-topic.md`)
2. Add YAML frontmatter:
   ```yaml
   ---
   title: Document title
   date: YYYY-MM-DD
   category: competitors|market|methodology|regulations|technology
   tags: [tag1, tag2]
   status: draft|complete|outdated
   ---
   ```
3. Write the content
4. **Update this INDEX.md** — add a row to the table above
5. If using the researcher agent, it does steps 1-4 automatically
