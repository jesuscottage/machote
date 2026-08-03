---
title: Reglas de adaptación a proyecto existente
date: 2026-08-03
category: methodology
tags: [adaptación, inicialización, template, proyecto-existente]
status: complete
---

# Adaptación de la plantilla a un proyecto existente

Cuando el usuario quiere aplicar esta plantilla a un proyecto que ya tiene código,
archivos de configuración y estructura propia, Claude DEBE seguir estas reglas
estrictamente para no romper nada.

## Principio fundamental

**La adaptación es ADITIVA** — solo se agregan archivos nuevos, nunca se modifican
ni eliminan los existentes del proyecto.

## Paso 1 — Auditoría (solo lectura)

Antes de cualquier cambio, auditar el estado actual:

1. ¿Existe `.claude/`? ¿Qué contiene?
2. ¿Hay skills, reglas o agentes fuera de `.claude/`?
3. ¿Existen `docs/knowledge/`, `docs/plans/`, `scripts/`?
4. ¿Existe `CLAUDE.md`?
5. ¿Existe `.claude/settings.json`?
6. ¿Existe `.mcp.json`?
7. Listar conflictos potenciales.

**Presentar resumen al usuario y esperar confirmación explícita antes de proceder.**

## Paso 2 — Lo que SÍ se hace

- **Crear** `.claude/rules/` con las 4 reglas (organización, idioma, seguridad, calidad)
- **Crear** `.claude/agents/` con `investigador.md`
- **Crear** `.claude/commands/` con `commit.md`
- **Crear** `.claude/context/` con `reminders.md` (luego personalizar)
- **Crear** `.claude/skills/` con todos los skills
- **Crear** `docs/knowledge/INDEX.md`
- **Crear** `docs/knowledge/technology/mcp-catalog.md`
- **Crear** `docs/plans/`
- **Crear** `scripts/fix-spanish-ortho.sh`
- **Crear** `.mcp.json.example`
- **Merge** `.gitignore` — agregar entradas faltantes, nunca reemplazar

## Paso 3 — Lo que NUNCA se hace

- **Nunca modificar** código fuente existente
- **Nunca modificar** package.json, requirements.txt, Docker, CI/CD, configs de build
- **Nunca modificar** .env ni credenciales/secretos
- **Nunca modificar** conexiones API, endpoints, configuración de servicios
- **Nunca eliminar** archivos o directorios existentes
- **Nunca mover** archivos existentes — si hay skills fuera de `.claude/`, COPIARLOS
  e informar al usuario dónde están los originales para que decida

## Paso 4 — Integración de CLAUDE.md

Si CLAUDE.md ya existe, **no es un simple append** — el objetivo es producir el
mejor CLAUDE.md posible integrando el contenido existente con la estructura de
la plantilla.

1. **Leer** el CLAUDE.md existente — entender qué información específica del proyecto contiene
2. **Escribir** un CLAUDE.md integrado que:
   - Conserve TODA la información específica del proyecto (stack, convenciones, issues conocidos, etc.)
   - Reorganice en la estructura limpia de la plantilla (Project Structure, Rules, Skills, Knowledge, Plans, MCPs)
   - Agregue la tabla de skills completa con triggers bilingües
   - Agregue referencias a reglas, knowledge base, planes y MCPs
   - Elimine redundancia — un solo documento cohesivo, no contenido viejo + nuevo pegado
3. **Mostrar** diff o resumen al usuario y esperar confirmación antes de sobrescribir

Si CLAUDE.md no existe: crear desde la plantilla y personalizar para el proyecto.

## Paso 5 — Personalización

1. Actualizar `.claude/context/reminders.md` con la estructura y stack real del proyecto
2. Si el proyecto tiene reglas de negocio, crear `.claude/rules/negocio.md`
3. Ajustar idioma en `.claude/rules/idioma.md`
4. Si ya existían reglas o contexto, integrar su contenido en la nueva estructura
5. Recomendar MCPs relevantes según el stack (ver paso 5 de configuración inicial en CLAUDE.md)

## Paso 6 — Resumen final

Mostrar al usuario:
1. Qué se creó (lista de archivos/directorios nuevos)
2. Qué se fusionó (.gitignore, CLAUDE.md)
3. Qué NO se tocó (archivos existentes del proyecto)
4. Skills o configs que existían fuera de `.claude/` y requieren revisión
5. Próximos pasos recomendados (ej: activar MCPs)
