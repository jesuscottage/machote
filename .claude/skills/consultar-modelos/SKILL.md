# Skill: /consultar-modelos

> Consultar a Gemini y GPT como revisores externos para decisiones, revisiones de código, verificaciones o análisis.
> **3 modos** según la interfaz de acceso de cada modelo.
> **Principio**: los modelos analizan y opinan. Claude sintetiza, identifica falsos positivos, decide y ejecuta.

## Uso

```
/consultar-modelos [tema o pregunta]                  # → Claude elige el modo
/consultar-modelos [tema] modo-a                      # → Ambos vía Antigravity
/consultar-modelos [tema] modo-b                      # → Gemini Antigravity + GPT web
/consultar-modelos [tema] modo-c                      # → Gemini Antigravity + GPT Copilot web
/consultar-modelos [tema] solo-gemini                 # → Solo Gemini (Antigravity)
/consultar-modelos [tema] solo-gpt                    # → Solo GPT (el modo determina la interfaz)
```

**Ejemplos:**
```
/consultar-modelos Verificar esquema SQL de billing tras migración
/consultar-modelos Revisar endpoint de autenticación modo-b
/consultar-modelos ¿Cómo implementar sistema de pagos? modo-a
/consultar-modelos Validar flujo de OAuth con proveedor externo modo-c
```

---

## Modos

### Modo A — Ambos vía Antigravity

| Modelo | Interfaz | Acceso | Prompt |
|--------|----------|--------|--------|
| **Gemini** | Antigravity UI | Completo al proyecto | Único, compartido |
| **GPT** | Antigravity UI | Completo al proyecto | Único, compartido |

- **Un solo prompt** para ambos modelos.
- Ambos tienen acceso completo al proyecto — animarlos a investigar archivos relevantes.
- La instrucción de output indica **dos rutas de archivo** (una por modelo) para que cada uno deposite su reporte directamente.

### Modo B — Gemini Antigravity + GPT web

| Modelo | Interfaz | Acceso | Prompt |
|--------|----------|--------|--------|
| **Gemini** | Antigravity UI | Completo al proyecto | Prompt con paths a investigar |
| **GPT** | Web (chatgpt.com) | Sin acceso al repo | Prompt autocontenido (código embebido) |

- **Dos prompts separados**: uno para Gemini (con paths de archivos), otro para GPT (autocontenido con código embebido).
- **Dos archivos placeholder** para los reportes.
- GPT necesita todo el contexto embebido en el prompt (código, reglas de negocio, restricciones).
- El usuario copia la respuesta de GPT del chat y la pega en el placeholder.

### Modo C — Gemini Antigravity + GPT Copilot web

| Modelo | Interfaz | Acceso | Prompt |
|--------|----------|--------|--------|
| **Gemini** | Antigravity UI | Completo al proyecto | Prompt con paths a investigar |
| **GPT** | GitHub Copilot web | Vía repos GitHub | Prompt con repos + paths explícitos |

- **Dos prompts separados**: uno para Gemini (con paths), otro para GPT (con repos GitHub explícitos).
- **Push obligatorio** antes de consultar — GPT Copilot accede vía GitHub.
- **Dos archivos placeholder** para los reportes.
- El usuario copia la respuesta de GPT del chat y la pega en el placeholder.

> **Configuración requerida para Modo C**: antes de usar, identificar los repos GitHub del proyecto
> y reemplazar `{REPOS_GITHUB}` en la plantilla [plantilla-prompt-modo-c-gpt.md](plantilla-prompt-modo-c-gpt.md).

---

## Flujo completo

### Paso 1 — Entender la consulta

Identificar:
- **Tema/pregunta central**: ¿Qué se quiere resolver o evaluar?
- **Tipo de consulta**: Decisión técnica | Revisión de código | Verificación de datos | Análisis de arquitectura | Estrategia | Otro
- **Modo**: A, B o C (si no se indica, elegir según contexto)
- **Destino**: Gemini, GPT, o ambos (por defecto siempre ambos)
- **Rol ideal**: seleccionar de la tabla de roles en la sección de referencia

### Paso 2 — Recopilar contexto

Según el tipo de consulta, leer los archivos relevantes del proyecto:
- Código fuente (archivos específicos, no todo el repo)
- Documentos de la base de conocimiento (`docs/knowledge/`)
- Planes (`docs/plans/`)
- Reglas de negocio (`.claude/rules/`)
- Revisiones previas (`docs/reviews/`)

**No sobrecargar**: solo lo que el modelo necesita para dar una respuesta informada.
**Modo B**: para GPT, embeber todo el código relevante directamente en el prompt.

### Paso 3 — Determinar carpeta de destino

**Si ya existe una revisión relacionada**, reutilizar su carpeta:
```
docs/reviews/{revisión-existente}/prompts/consulta-NN-tema.md
```

**Si es una consulta nueva**, crear estructura:
```
docs/reviews/{nombre-consulta}/
├── prompts/
│   ├── consulta-NN-tema.md              # Modo A: prompt único
│   ├── consulta-NN-tema-gemini.md       # Modo B/C: prompt Gemini
│   └── consulta-NN-tema-gpt.md          # Modo B/C: prompt GPT
└── reportes/
    ├── consulta-NN-tema-gemini.md       # Placeholder reporte Gemini
    └── consulta-NN-tema-gpt.md          # Placeholder reporte GPT
```

### Paso 4 — Generar prompt(s)

Usar la plantilla según el modo:

- **Modo A**: [plantilla-prompt-modo-a.md](plantilla-prompt-modo-a.md) — un solo prompt, instrucción de output con dos rutas.
- **Modo B**: [plantilla-prompt-modo-b-gemini.md](plantilla-prompt-modo-b-gemini.md) + [plantilla-prompt-modo-b-gpt.md](plantilla-prompt-modo-b-gpt.md) — dos prompts separados.
- **Modo C**: [plantilla-prompt-modo-c-gemini.md](plantilla-prompt-modo-c-gemini.md) + [plantilla-prompt-modo-c-gpt.md](plantilla-prompt-modo-c-gpt.md) — dos prompts separados.

**Checklist obligatorio antes de mostrar al usuario:**
- [ ] Rol asignado (específico, no genérico)
- [ ] Contexto mínimo necesario (situación actual, decisiones previas)
- [ ] Tarea clara y acotada
- [ ] Restricciones explícitas
- [ ] Formato de respuesta definido
- [ ] **Instrucción de output** con paths de archivos de salida (NUNCA omitir)
- [ ] **Placeholders creados** en `reportes/` para ambos modelos

Requisitos adicionales por modo:
- **Modo A**: animar a los modelos a investigar archivos del proyecto antes de responder
- **Modo B**: código completo embebido en el prompt de GPT
- **Modo C**: repos GitHub explícitos en el prompt de GPT

### Paso 4.5 — Push obligatorio (solo Modo C)

GPT (Copilot web) accede a los repos vía GitHub. Si los cambios no están pusheados, GPT no los verá.

```bash
git add [archivos relevantes]
git commit -m "wip: push pre-consulta modelos"
git push origin HEAD
```

### Paso 5 — Crear placeholders e instrucciones al usuario

**SIEMPRE crear ambos archivos placeholder** antes de mostrar instrucciones:

```markdown
<!-- Pegar aquí la respuesta del modelo a la consulta NN -->
```

**Mostrar instrucciones según el modo:**

#### Modo A
```
Prompt preparado para ambos modelos (Antigravity).

Prompt: docs/reviews/{nombre}/prompts/consulta-NN-tema.md

Instrucciones:
1. Abre el archivo de prompt
2. Pégalo en Antigravity UI — primero Gemini, luego GPT
3. Las respuestas quedarán en:
   - Gemini: docs/reviews/{nombre}/reportes/consulta-NN-tema-gemini.md (lo crea Gemini)
   - GPT: docs/reviews/{nombre}/reportes/consulta-NN-tema-gpt.md (lo crea GPT)
4. Avísame cuando estén listas
```

#### Modo B
```
Dos prompts preparados.

Gemini (Antigravity): docs/reviews/{nombre}/prompts/consulta-NN-tema-gemini.md
GPT (web):            docs/reviews/{nombre}/prompts/consulta-NN-tema-gpt.md

Instrucciones:
1. Pega el prompt de Gemini en Antigravity UI
   → Gemini deposita su reporte en: docs/reviews/{nombre}/reportes/consulta-NN-tema-gemini.md
2. Pega el prompt de GPT en chatgpt.com
   → Copia la respuesta y pégala en: docs/reviews/{nombre}/reportes/consulta-NN-tema-gpt.md
3. Avísame cuando estén listas
```

#### Modo C
```
Dos prompts preparados. Push realizado.

Gemini (Antigravity): docs/reviews/{nombre}/prompts/consulta-NN-tema-gemini.md
GPT (Copilot web):    docs/reviews/{nombre}/prompts/consulta-NN-tema-gpt.md

Instrucciones:
1. Pega el prompt de Gemini en Antigravity UI
   → Gemini deposita su reporte en: docs/reviews/{nombre}/reportes/consulta-NN-tema-gemini.md
2. Pega el prompt de GPT en GitHub Copilot web
   → Copia la respuesta y pégala en: docs/reviews/{nombre}/reportes/consulta-NN-tema-gpt.md
3. Avísame cuando estén listas
```

---

## Procesamiento de respuestas

Cuando el usuario avisa que las respuestas están listas:

### Paso 6 — Leer, sintetizar e identificar falsos positivos

1. **Extraer lo valioso**: insights genuinos, datos concretos, riesgos no considerados
2. **Descartar ruido**: recomendaciones genéricas, repeticiones del contexto, obviedades
3. **Contrastar con el proyecto**: ¿la recomendación aplica dado nuestro stack, restricciones y estado?
4. **Identificar falsos positivos (OBLIGATORIO)**: para CADA hallazgo reportado, verificar en el código
   real si aplica. Clasificar explícitamente como genuino o falso positivo con justificación.
   Ejemplos comunes de FP: el modelo no encontró el archivo (falta push), asume estado desactualizado,
   reporta bug ya corregido, o malinterpreta el contexto del proyecto.
5. **Si se consultó a ambos**: cruzar respuestas, identificar coincidencias y discrepancias

### Paso 7 — Presentar síntesis y plan

**OBLIGATORIO**: incluir siempre las dos tablas (genuinos + falsos positivos) en la síntesis.
Si no hay falsos positivos, indicar "Ninguno" en la tabla.

```
## Síntesis de la consulta

[Resumen de 3-5 líneas de lo más valioso]

### Hallazgos genuinos

| # | Hallazgo | Fuente | Acción |
|---|----------|--------|--------|
| G1 | [descripción] | Gemini/GPT/ambos | [fix concreto] |

### Falsos positivos

| # | Hallazgo | Fuente | Por qué es FP |
|---|----------|--------|---------------|
| FP1 | [descripción] | Gemini/GPT | [justificación] |

## Plan de acción

1. [Acción 1] — Claude puede ejecutar
2. [Acción 2] — Requiere decisión del usuario
...

¿Procedo?
```

### Paso 8 — Ejecutar (si el usuario acepta)

Aplicar los cambios aprobados y registrar cada modificación.

---

## Referencia rápida

### Roles comunes

| Tipo de consulta | Rol sugerido | Dominio |
|---|---|---|
| Decisión de stack | Arquitecto de software senior | Sistemas distribuidos, cloud |
| Flujo de usuario | Auditor de aplicaciones SaaS | UX, product design |
| Infraestructura cloud | Especialista en {proveedor cloud} | Cloud Run, Lambda, Azure Functions |
| Seguridad / compliance | Auditor de seguridad y compliance | OWASP, GDPR, PCI-DSS |
| Pricing / negocio | Consultor de producto SaaS B2B | Pricing, unit economics |
| Base de datos | DBA senior {motor} | Esquemas, migración, indexación |
| Revisión de código | Ingeniero senior {stack} | {lenguaje/framework específico} |
| Verificación de datos | Analista de datos / QA | Integridad, consistencia |

### Formatos de respuesta predefinidos

#### Para decisiones técnicas o de negocio
```
### 1. Análisis de la situación actual
### 2. Opciones viables (mín. 2, máx. 4) — con pros, contras, esfuerzo, viabilidad
### 3. Recomendación fundamentada
### 4. Riesgos y mitigaciones
### 5. Plan de acción concreto (archivos, funciones, pasos)
```

#### Para revisión de código
```
Tabla de hallazgos con columnas: #, Severidad (Alta/Media/Baja/Info), Archivo:Línea, Hallazgo, Fix sugerido
Después: resumen ejecutivo y patrones detectados
```

#### Para verificación de datos
```
Tabla comparativa: Dato en documento | Valor verificado | Fuente | Estado (OK/Corregir/Revisar)
Después: correcciones necesarias con valores exactos
```

#### Para respuesta libre
```
Estructura tu respuesta de la forma que mejor se adapte al problema.
Sé específico: menciona archivos, funciones, configuraciones concretas.
```
