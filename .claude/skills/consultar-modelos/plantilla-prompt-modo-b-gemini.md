# Plantilla de Prompt — Modo B: Gemini (Antigravity)

> **Uso**: Prompt para Gemini vía Antigravity. Tiene acceso completo al proyecto.
> Se le anima a investigar archivos del proyecto y depositar su reporte directamente.

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

**IMPORTANTE**: Deposita tu respuesta completa directamente en el siguiente archivo:

```
{RUTA_REPORTE}-gemini.md
```

No incluyas en tu reporte el contenido de esta instrucción ni el código fuente que revisaste.
````

---

## Variables

| Variable | Descripción |
|---|---|
| `{TITULO}` | Título descriptivo de la consulta |
| `{ROL}` | Rol experto asignado |
| `{DOMINIO}` | Área de expertise |
| `{NOMBRE_PROYECTO}` | Nombre del proyecto actual |
| `{DESCRIPCION_BREVE}` | Una línea describiendo el proyecto |
| `{CONTEXTO}` | Situación actual, decisiones previas |
| `{ARCHIVOS}` | Lista de paths relativos a investigar |
| `{TAREA}` | Qué se espera del modelo |
| `{RESTRICCIONES}` | Limitaciones técnicas, de negocio, de formato |
| `{FORMATO}` | Estructura esperada de la respuesta |
| `{RUTA_REPORTE}` | Path relativo base (sin sufijo). Ejemplo: `docs/reviews/{nombre}/reportes/consulta-01-tema` |
