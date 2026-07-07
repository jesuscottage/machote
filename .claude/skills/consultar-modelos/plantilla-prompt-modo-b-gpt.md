# Plantilla de Prompt — Modo B: GPT (web, autocontenido)

> **Uso**: Prompt autocontenido para GPT vía web (chatgpt.com). GPT NO tiene acceso al proyecto.
> Todo el contexto (código, reglas, restricciones) debe estar embebido en el prompt.
> El usuario copia la respuesta del chat y la pega en el placeholder.

---

## Plantilla completa

````markdown
# {TITULO}

## Tu rol

Eres un **{ROL}** con amplia experiencia en **{DOMINIO}**.

## Proyecto

**{NOMBRE_PROYECTO}** — {DESCRIPCION_BREVE}

## Contexto

{CONTEXTO}

## Reglas de negocio relevantes

{REGLAS_NEGOCIO}

## Código fuente

A continuación se incluye todo el código relevante para esta consulta:

{CODIGO_EMBEBIDO}

## Tarea

{TAREA}

## Restricciones

{RESTRICCIONES}

## Formato de respuesta

{FORMATO}

## Instrucción de output

Proporciona tu reporte completo directamente en tu respuesta, formateado en Markdown.
El usuario lo copiará al archivo correspondiente del proyecto.
````

---

## Variables

| Variable | Descripción | Nota |
|---|---|---|
| `{TITULO}` | Título descriptivo | |
| `{ROL}` | Rol experto asignado | |
| `{DOMINIO}` | Área de expertise | |
| `{NOMBRE_PROYECTO}` | Nombre del proyecto actual | |
| `{DESCRIPCION_BREVE}` | Una línea describiendo el proyecto | |
| `{CONTEXTO}` | Situación actual, decisiones previas | Más detallado que en Modo A — GPT no puede investigar |
| `{REGLAS_NEGOCIO}` | Reglas de negocio invariantes relevantes | Solo las necesarias, extraídas de `.claude/rules/` |
| `{CODIGO_EMBEBIDO}` | Código fuente completo de archivos relevantes | Cada archivo con `### ruta/archivo.ext` + bloque de código |
| `{TAREA}` | Qué se espera del modelo | |
| `{RESTRICCIONES}` | Limitaciones | |
| `{FORMATO}` | Estructura esperada de la respuesta | |

### Notas sobre el código embebido

- Cada archivo debe estar precedido por su ruta relativa como encabezado `###`
- Incluir el código completo del archivo (no fragmentos) dentro de bloques de código con lenguaje
- Máximo recomendado: ~3,000 líneas totales para evitar truncamiento
- Si hay demasiado código, priorizar los archivos más relevantes para la tarea
