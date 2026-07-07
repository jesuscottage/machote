# Plantilla de Prompt — Modo C: GPT (Copilot web, acceso vía GitHub)

> **Uso**: Prompt para GPT vía GitHub Copilot web. GPT accede a los repos vía GitHub.
> El prompt debe incluir los repos explícitos y paths de archivos a investigar.
> **Push obligatorio** antes de usar este modo — GPT Copilot accede al código desde GitHub.
> El usuario copia la respuesta del chat y la pega en el placeholder.
>
> **Configuración**: reemplaza `{REPOS_GITHUB}` con los repos reales del proyecto antes de usar.

---

## Plantilla completa

````markdown
# {TITULO}

## Tu rol

Eres un **{ROL}** con amplia experiencia en **{DOMINIO}**.

## Proyecto

**{NOMBRE_PROYECTO}** — {DESCRIPCION_BREVE}

Trabaja exclusivamente con estos repositorios:

{REPOS_GITHUB}

## Contexto

{CONTEXTO}

## Archivos de referencia

Lee estos archivos antes de responder:

{ARCHIVOS}

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

| Variable | Descripción |
|---|---|
| `{TITULO}` | Título descriptivo |
| `{ROL}` | Rol experto asignado |
| `{DOMINIO}` | Área de expertise |
| `{NOMBRE_PROYECTO}` | Nombre del proyecto actual |
| `{DESCRIPCION_BREVE}` | Una línea describiendo el proyecto |
| `{REPOS_GITHUB}` | Lista de repos GitHub del proyecto (formato: `- \`owner/repo\` — descripción`). **Configurar una vez al adaptar esta plantilla al proyecto.** |
| `{CONTEXTO}` | Situación actual, decisiones previas |
| `{ARCHIVOS}` | Lista de paths relativos que GPT debe leer desde los repos GitHub |
| `{TAREA}` | Qué se espera del modelo |
| `{RESTRICCIONES}` | Limitaciones técnicas, de negocio, de formato |
| `{FORMATO}` | Estructura esperada de la respuesta |

### Ejemplo de `{REPOS_GITHUB}` para un proyecto típico

```
- `owner/mi-proyecto` — Documentación, conocimiento, planes, reglas
- `owner/mi-backend` — API (FastAPI / Express / Rails)
- `owner/mi-frontend` — UI (Next.js / React / Vue)
```
