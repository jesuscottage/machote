# Plantilla de Prompt — Modo A (ambos vía Antigravity)

> **Uso**: Un solo prompt para ambos modelos. Ambos tienen acceso completo al proyecto vía Antigravity.
> Los modelos investigan archivos del proyecto y depositan sus reportes directamente.

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

## Archivos de referencia

Antes de responder, investiga a fondo los siguientes archivos del proyecto. Lee todo lo que necesites para dar una respuesta bien fundamentada:

{ARCHIVOS}

Si consideras que hay otros archivos relevantes que no están en la lista, investígalos también.

## Tarea

{TAREA}

## Restricciones

{RESTRICCIONES}

## Formato de respuesta

{FORMATO}

## Instrucción de output

**IMPORTANTE**: Deposita tu respuesta completa en el archivo que corresponda a tu modelo:

- **Si eres Gemini**: crea el archivo `{RUTA_REPORTE}-gemini.md` directamente en el repositorio.
- **Si eres GPT**: crea el archivo `{RUTA_REPORTE}-gpt.md` directamente en el repositorio.

No incluyas en tu reporte el contenido de esta instrucción ni el código fuente que revisaste.
````

---

## Variables

| Variable | Descripción | Obligatoria |
|---|---|---|
| `{TITULO}` | Título descriptivo de la consulta | Sí |
| `{ROL}` | Rol experto asignado | Sí |
| `{DOMINIO}` | Área de expertise | Sí |
| `{NOMBRE_PROYECTO}` | Nombre del proyecto actual | Sí |
| `{DESCRIPCION_BREVE}` | Una línea describiendo el proyecto | Sí |
| `{CONTEXTO}` | Situación actual, decisiones previas, estado del problema | Sí |
| `{ARCHIVOS}` | Lista de paths relativos que el modelo debe leer (e investigar más si lo considera necesario) | Sí |
| `{TAREA}` | Qué se espera del modelo — pregunta, revisión, verificación, análisis | Sí |
| `{RESTRICCIONES}` | Limitaciones técnicas, de negocio, de formato | Sí |
| `{FORMATO}` | Estructura esperada de la respuesta (usar predefinidos de SKILL.md o crear ad-hoc) | Sí |
| `{RUTA_REPORTE}` | Path relativo base (sin sufijo `-gemini`/`-gpt`). Ejemplo: `docs/reviews/{nombre}/reportes/consulta-01-tema` | Sí |
