---
name: revision-sistematica
description: >
  Revisión sistemática de literatura académica usando APIs abiertas (PubMed, OpenAlex,
  Semantic Scholar, Europe PMC, arXiv, CrossRef). Soporta modo semilla (desde investigación
  existente) y modo desde cero. Diseña queries con metodología PICO, ejecuta búsquedas
  multi-fuente, deduplica con script Python, aplica snowballing bidireccional, obtiene
  full-text selectivo, y sintetiza hallazgos en una revisión estructurada.
  Basada en PRISMA-S, Cochrane Handbook, PRESS y 94 papers de metodología.
---

# Skill: Revisión sistemática de literatura

## Cuándo usar

- `/revision-sistematica [ruta-semilla]` — modo A: con semilla existente
- `/revision-sistematica [tema o pregunta de investigación]` — modo B: desde cero
- "búsqueda sistemática sobre [X]"
- "necesito una revisión sistemática de [X]"
- "investigación exhaustiva sobre [X]"
- "profundiza la investigación de [X]"
- "necesito más papers sobre [X]"
- "búsqueda académica profunda sobre [X]"

## Requisitos previos

- **Python 3.8+** en el sistema (para el script de deduplicación — usa solo stdlib)
- **PubMed MCP** (opcional pero recomendado) — si disponible, cargar con ToolSearch:
  `select:mcp__claude_ai_PubMed__search_articles,mcp__claude_ai_PubMed__get_article_metadata,mcp__claude_ai_PubMed__find_related_articles,mcp__claude_ai_PubMed__get_full_text_article,mcp__claude_ai_PubMed__convert_article_ids`
- Si PubMed MCP no está disponible, usar PubMed E-utilities vía WebFetch

## Herramientas disponibles

| Fuente | Acceso | Cobertura | Rate limit | Boolean | Uso principal |
|--------|--------|-----------|------------|---------|---------------|
| **PubMed** | MCP o WebFetch (E-utils) | 40M+ artículos biomédicos | 3/s sin key, 10/s con key | Sí (completo: AND/OR/NOT, [tiab], [mh], truncamiento) | Búsqueda primaria biomedicina |
| **OpenAlex** | WebFetch | 288M+ obras multidisciplinarias | 10/s, 100K/día | Filtros + search semántico (no Boolean avanzado) | Búsqueda primaria multidisciplinar |
| **Europe PMC** | WebFetch | 36M+ artículos ciencias de la vida | ~10/s, sin auth | Sí (Boolean nativo, TITLE:, AUTH:) | Complemento biomédico + full-text OA |
| **Semantic Scholar** | WebFetch | 225M+ papers CS/bio | 1/s sin key, 100/5min con key | No (solo keywords + filtros) | Enriquecimiento: citation graph, TLDR |
| **arXiv** | WebFetch | 2.4M+ preprints CS/ML/física/mat | 1/3s, sin auth | Sí (ti:, au:, abs:, cat:) | CS, ML, física, matemáticas |
| **CrossRef** | WebFetch | 180M+ DOIs | 50/s con mailto | Filtros básicos | Solo resolución DOI para deduplicación |

### Selección de fuentes por dominio

| Dominio | Fuentes obligatorias | Fuentes complementarias |
|---------|---------------------|------------------------|
| Biomedicina | PubMed + OpenAlex + Europe PMC | Semantic Scholar |
| CS / ML / IA | OpenAlex + Semantic Scholar + arXiv | PubMed (si tiene componente biomédico) |
| Ciencias sociales | OpenAlex + Semantic Scholar | PubMed (psicología, salud pública) |
| Multidisciplinar | PubMed + OpenAlex | Semantic Scholar + Europe PMC |
| Ingeniería | OpenAlex + Semantic Scholar | arXiv |

**Regla**: PubMed + OpenAlex SIEMPRE se incluyen (son las dos fuentes P0 con mayor cobertura combinada sin costo).

### URLs de APIs

```
PubMed E-utilities:
  esearch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=200&term={QUERY}
  efetch:  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&retmax=50&id={PMID_LIST}

OpenAlex:
  search:  https://api.openalex.org/works?search={QUERY}&filter={FILTERS}&per_page=50&page={N}&mailto=user@example.com

Semantic Scholar:
  search:  https://api.semanticscholar.org/graph/v1/paper/search?query={QUERY}&fields=title,authors,year,abstract,citationCount,externalIds,isOpenAccess&limit=100

Europe PMC:
  search:  https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={QUERY}&format=json&pageSize=100&cursorMark={CURSOR}
  fulltext: https://www.ebi.ac.uk/europepmc/webservices/rest/{ID}/fullTextXML

arXiv:
  search:  https://export.arxiv.org/api/query?search_query={QUERY}&start=0&max_results=100

CrossRef:
  works:   https://api.crossref.org/works?query={QUERY}&rows=50&mailto=user@example.com
  by DOI:  https://api.crossref.org/works/{DOI}
```

---

## Proceso

### Fase 1 — Definición y semilla

**Detectar el modo automáticamente:**
- Si el argumento es una ruta a una carpeta existente con `revision.md`, `revision-es.md`,
  `*_abstracts.txt`, o CSVs → **Modo A**
- Si el argumento es texto libre (tema o pregunta) → **Modo B**

#### Modo A — Con semilla existente

1. Leer `revision.md` o `revision-es.md` (preferido) o los `*_abstracts.txt` de la carpeta
2. Extraer de la revisión/abstracts:
   - Pregunta central de investigación
   - Términos clave (en inglés, para queries)
   - Autores principales y papers más citados
   - DOIs/PMIDs si están disponibles
   - Gaps identificados en la revisión previa
   - Dominio temático (para seleccionar fuentes apropiadas)
3. Leer `00-busquedas.md` o `00-definicion.md` si existe para obtener contexto adicional

#### Modo B — Desde cero (sin semilla)

Recopilar del usuario (en un solo mensaje si no está claro):

1. **Pregunta de investigación central** — lo más específica posible
2. **Dominio temático** — biomedicina, CS/ML, ciencias sociales, ingeniería, multidisciplinar
3. **Año de corte** — sugerido: últimos 5-10 años
4. **Tipo de estudios preferidos** — revisiones sistemáticas, RCTs, cualquier diseño, etc.
5. **Contexto** — por qué esta investigación, qué decisión informa

#### Crear carpeta

- **Modo A**: usar la carpeta de la semilla existente
- **Modo B**: crear `[ruta-elegida-por-usuario]/[slug-kebab-case-del-tema]/`
  Si el usuario no especifica ruta, usar `docs/research/[slug]/`

#### Output: `00-definicion.md`

```markdown
---
tema: [Nombre descriptivo]
pregunta-central: "[Pregunta exacta]"
dominio: [dominio temático]
fecha: YYYY-MM-DD
año-corte: YYYY
modo: semilla|desde-cero
fuentes-seleccionadas: [lista de APIs a consultar]
estado: fase-1-completada
---

## Contexto

[2-4 oraciones: por qué esta investigación, qué decisión informa]

## Términos clave (inglés)

### Concepto 1 — [nombre PICO: Population/Intervention/Comparison/Outcome]
- [término principal]
- [sinónimo 1]
- [sinónimo 2]
- [MeSH term si aplica]

### Concepto 2 — [nombre PICO]
- ...

## Papers semilla

[Solo modo A: lista de papers clave de la revisión previa, con DOI/PMID si disponible]

## Gaps a investigar

[Solo modo A: gaps identificados en la revisión previa que esta revisión busca cubrir]

## Fuentes seleccionadas

[Lista con justificación por dominio]
```

---

### Fase 2 — Diseño de queries ⏸️ PAUSA INTERACTIVA

#### 2.1 Query maestra (sintaxis PubMed)

Construir una query Boolean siguiendo la estructura PICO:
- **OR** dentro de cada concepto (sinónimos, MeSH, texto libre)
- **AND** entre conceptos
- **Nunca usar NOT** (reduce recall; Cochrane Handbook lo desaconseja)
- Incluir MeSH terms con explosión cuando sea posible
- Incluir truncamiento (`*`) para variantes morfológicas
- Usar `[tiab]` para texto libre y `[mh]` para MeSH

Ejemplo de estructura:
```
(("termino1"[tiab] OR "sinonimo1"[tiab] OR "MeSH Term"[mh]) AND
 ("termino2"[tiab] OR "sinonimo2"[tiab] OR "MeSH Term 2"[mh]) AND
 ("termino3"[tiab] OR "sinonimo3"[tiab]))
```

#### 2.2 Traducción adaptada por API

A partir de la query maestra, generar una versión adaptada para cada API seleccionada:

| API | Estrategia de traducción |
|-----|------------------------|
| **PubMed** | Usar query maestra directamente (es la base) |
| **OpenAlex** | Extraer keywords principales, usar `search=` + `filter=publication_year:>YYYY,type:article`. No intentar Boolean complejo — OpenAlex busca semánticamente |
| **Europe PMC** | Adaptar field codes: `[tiab]` → búsqueda general, `[mh]` → mantener (Europe PMC soporta MeSH vía PubMed). Boolean nativo funciona |
| **Semantic Scholar** | Simplificar a 2-3 queries de keywords (sin Boolean). Usar `fieldsOfStudy` y `year` como filtros |
| **arXiv** | Usar `ti:` y `abs:` para keywords principales. Especificar `cat:` (cs.AI, cs.CL, cs.IR, etc.) |
| **CrossRef** | No usar para búsqueda. Solo para resolver DOIs faltantes en Fase 4 |

Documentar cada traducción y sus limitaciones.

#### 2.3 Auto-validación PRESS simplificada

Antes de presentar al usuario, verificar:

1. **Conceptos PICO cubiertos**: ¿Todos los conceptos de la pregunta tienen al menos un término en la query?
2. **Sinónimos suficientes**: ¿Cada concepto principal tiene al menos 2 sinónimos o variantes?
3. **Operadores correctos**: ¿OR dentro de conceptos, AND entre conceptos, sin NOT?

Si alguna validación falla, corregir automáticamente y documentar la corrección.

#### Output: `01-queries.md`

```markdown
---
tema: [Nombre]
fecha: YYYY-MM-DD
estado: pendiente-ejecucion
n-queries: N
fuentes: [lista]
---

## Query maestra (PubMed)

```
[query Boolean completa]
```

## Validación PRESS simplificada

- [x] Todos los conceptos PICO cubiertos
- [x] Sinónimos suficientes (≥2 por concepto)
- [x] Operadores Boolean correctos

## Traducciones por API

### PubMed
**Query**: [query exacta a ejecutar]
**Filtros**: [años, tipo de estudio]

### OpenAlex
**URL**: `https://api.openalex.org/works?search=[keywords]&filter=[filtros]&per_page=50`
**Limitaciones**: No soporta Boolean avanzado ni MeSH; búsqueda semántica

### Europe PMC
**Query**: [query adaptada]
**Limitaciones**: [si las hay]

### Semantic Scholar
**Query 1**: [keywords grupo 1]
**Query 2**: [keywords grupo 2]
**Limitaciones**: Sin Boolean; múltiples queries simples

### arXiv (si aplica)
**Query**: [query con cat: y ti:/abs:]

## Resumen

| Fuente | N queries | Papers esperados |
|--------|-----------|-----------------|
| PubMed | 1 | ~N |
| OpenAlex | 1 | ~N |
| ... | ... | ... |
| **Total** | **X** | **~N** |
```

#### ⏸️ PAUSA

Presentar al usuario:
- Query maestra y resultado de validación PRESS
- Traducciones por API con limitaciones documentadas
- Papers esperados
- Preguntar: "¿Quieres ajustar alguna query o fuente antes de ejecutar?"

**Esperar confirmación antes de continuar a Fase 3.**

---

### Fase 3 — Ejecución

Ejecutar búsquedas **secuencialmente**, fuente por fuente, en este orden:

1. **PubMed** (más confiable, vocabulario controlado):
   - Si PubMed MCP disponible: `search_articles` → `get_article_metadata`
   - Si no: WebFetch a E-utilities (esearch → efetch)
   - Extraer: PMID, DOI, título, abstract, autores, año, journal, MeSH

2. **OpenAlex** vía WebFetch:
   - Paginar con `page` y `per_page=50`
   - Extraer: OpenAlex ID, DOI, título, abstract (reconstruir de `abstract_inverted_index`), autores, año, cited_by_count, is_oa
   - Para reconstruir abstract invertido: ordenar por posición y unir palabras

3. **Europe PMC** vía WebFetch:
   - Paginar con `cursorMark`
   - Extraer: PMID, PMCID, DOI, título, abstract, autores, año, journal, citedByCount

4. **Semantic Scholar** vía WebFetch (solo queries clave, rate limit estricto):
   - Extraer: S2 ID, DOI, PMID (externalIds), título, abstract, autores, año, citationCount, isOpenAccess

5. **arXiv** vía WebFetch (solo si dominio CS/ML/física):
   - Parsear respuesta Atom XML
   - Extraer: arXiv ID, título, abstract, autores, año, categorías

#### Formato normalizado por paper

Cada paper se normaliza a este formato texto (una entrada por paper, separada por líneas de guiones):

```
----------------------------------------------------------------------
[N] (AÑO) Apellido et al.
TITULO: [texto]
ABSTRACT: [texto o "(sin abstract disponible)"]
DOI: [doi o "-"]
PMID: [pmid o "-"]
FUENTE: [PubMed|OpenAlex|SemanticScholar|EuropePMC|arXiv]
CITAS: [N o "-"]
OPEN_ACCESS: [si|no]
----------------------------------------------------------------------
```

**CRÍTICO**: Este formato es el que parsea el script de deduplicación. No modificarlo.

#### Límites

- Máximo **200 resultados por fuente**
- Máximo **800 papers crudos** en total (antes de deduplicación)
- Si una API falla o no responde: documentar el error y continuar con las demás
- Si una query retorna 0 resultados: simplificar (quitar filtros, ampliar términos)
- Si retorna >200: filtrar por año más reciente o relevancia

#### Output: `02-resultados-crudos.md`

```markdown
---
tema: [Nombre]
fecha: YYYY-MM-DD
estado: resultados-obtenidos
n-papers-crudos: N
---

## Resumen de ejecución

| Fuente | Query (resumen) | Papers obtenidos | Errores |
|--------|----------------|-----------------|---------|
| PubMed | [resumen corto] | N | - |
| OpenAlex | [resumen corto] | N | - |
| ... | ... | ... | ... |
| **Total** | | **N** | |

## Resultados

----------------------------------------------------------------------
[1] (2024) Smith et al.
TITULO: Example paper title here
ABSTRACT: This study examines...
DOI: 10.1234/example
PMID: 12345678
FUENTE: PubMed
CITAS: 45
OPEN_ACCESS: si
----------------------------------------------------------------------

[2] (2023) Jones et al.
...
```

---

### Fase 4 — Deduplicación

Ejecutar el script de deduplicación:

```bash
python .claude/skills/revision-sistematica/deduplicar.py [ruta]/02-resultados-crudos.md
```

El script genera `03-corpus-deduplicado.md` en la misma carpeta con:
- Papers únicos en formato normalizado
- Campo `FUENTES:` (plural) listando todas las fuentes donde apareció
- Resumen estadístico de deduplicación al inicio del archivo

Si Python no está disponible, hacer la deduplicación manualmente:
1. Agrupar por DOI (los que tengan DOI idéntico son duplicados)
2. Agrupar por PMID (los que tengan PMID idéntico son duplicados)
3. Para el resto: comparar títulos; si son prácticamente idénticos + mismo año + mismo primer autor → duplicado
4. Para cada grupo de duplicados: mantener el que tenga abstract más completo
5. Registrar conteo: total importados, duplicados eliminados, únicos resultantes

#### Leer el output

Leer `03-corpus-deduplicado.md` para verificar:
- Número de papers únicos
- Distribución por fuente
- Tasa de deduplicación (esperada: 25-45% para búsquedas biomédicas multi-fuente)

---

### Fase 5 — Snowballing y refinamiento ⏸️ PAUSA INTERACTIVA

#### 5.1 Selección de semillas

Del corpus deduplicado, seleccionar **5-10 papers semilla** usando estos criterios (en orden de prioridad):

1. **Relevancia directa** a la pregunta central (título/abstract altamente pertinente)
2. **Citation count alto** (indicador de influencia en el campo)
3. **Diversidad temática** (no elegir 5 papers del mismo subtema)
4. **Año reciente** (priorizar últimos 3 años para snowballing forward)

#### 5.2 Snowballing forward (papers que citan a las semillas)

Para cada semilla:
- Si tiene PMID y PubMed MCP disponible: `find_related_articles`
- Si tiene DOI: OpenAlex `https://api.openalex.org/works?filter=cites:{OPENALEX_ID}&per_page=10`
- Máximo 10 papers por semilla, 50 en total

#### 5.3 Snowballing backward (referencias de las semillas)

Para cada semilla con DOI en OpenAlex:
- `https://api.openalex.org/works/{DOI}` → extraer `referenced_works`
- Consultar las 5-10 referencias más citadas
- Máximo 30 papers en total

#### 5.4 Deduplicar papers nuevos

Comparar los papers de snowballing contra el corpus existente:
- Por DOI
- Por título normalizado (lowercase, sin puntuación)
- Agregar solo los que sean genuinamente nuevos

#### 5.5 Análisis de precisión

Revisar títulos/abstracts del corpus y evaluar:
- Papers altamente relevantes vs ruido (falsos positivos)
- Patrones: qué términos aparecen en los relevantes pero no en el ruido
- Si se identifica una nueva veta temática no cubierta: ejecutar máx 25 papers adicionales
- Máximo 2 iteraciones de refinamiento

#### 5.6 Validación de cobertura (solo modo A)

Verificar que los papers clave de la semilla aparezcan en los resultados.
Si faltan >30% de los papers semilla, ajustar queries o fuentes.

#### Output

Actualizar `03-corpus-deduplicado.md` añadiendo los papers nuevos con `FUENTE: Snowballing-forward` o `FUENTE: Snowballing-backward`.

Crear `04-snowballing.md` con el log de trazabilidad:

```markdown
---
tema: [Nombre]
fecha: YYYY-MM-DD
n-semillas: N
n-forward: N
n-backward: N
n-nuevos-tras-dedup: N
---

## Semillas seleccionadas

| # | Paper | Año | Citas | Criterio |
|---|-------|-----|-------|----------|
| 1 | [Apellido et al.] | YYYY | N | Relevancia + citas |
| ... | ... | ... | ... | ... |

## Forward snowballing

[Papers encontrados por cada semilla]

## Backward snowballing

[Papers encontrados por cada semilla]

## Validación de cobertura (solo modo A)

- Papers semilla re-encontrados: N de N (X%)
- Papers semilla no encontrados: [lista con justificación]
```

Actualizar el resumen estadístico al inicio de `03-corpus-deduplicado.md`.

#### ⏸️ PAUSA

Presentar al usuario:
- N papers totales en corpus (originales + snowballing)
- Papers nuevos aportados por forward vs backward
- Top 10 papers más citados del corpus completo
- Preguntar: "¿Quieres ajustar algo o continuar con la síntesis?"

**Esperar confirmación antes de continuar.**

---

### Fase 6 — Full-text selectivo

Para los **10-15 papers más relevantes** del corpus, obtener texto completo si es open access:

#### Criterios de selección (en orden)

1. Directamente relevantes a la pregunta central
2. Con metodología replicable o resultados cuantitativos clave
3. Que cubran gaps identificados en los abstracts
4. Revisión sistemática o meta-análisis del tema (si existen)
5. Papers seminales con alto citation count

#### Cómo obtener full-text

1. Si tiene PMID y es open access en PMC:
   - PubMed MCP: `get_full_text_article`
   - O WebFetch: `https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML`

2. Si tiene DOI y OpenAlex reporta `is_oa: true`:
   - Intentar `oa_url` de OpenAlex

3. Si está en arXiv:
   - WebFetch al HTML vía `https://arxiv.org/abs/{ID}`

**Nunca intentar acceder a papers detrás de paywall.**

#### Qué extraer de cada full-text

Para cada paper con texto completo, crear un resumen extenso:
- **Metodología**: diseño del estudio, muestra, herramientas
- **Resultados cuantitativos clave**: números, porcentajes, p-values
- **Limitaciones**: reportadas por los autores
- **Conclusiones principales**: 2-3 oraciones

Incluir estos resúmenes en la sección "Papers con análisis full-text" del corpus.

---

### Fase 7 — Síntesis

Leer `03-corpus-deduplicado.md` y generar la síntesis. **No leer archivos intermedios
de fases anteriores** — el corpus final contiene todo lo necesario.

#### Output: `revision-es.md`

```markdown
---
tema: [Nombre descriptivo]
pregunta-central: "[Pregunta de investigación]"
fecha-revision: YYYY-MM-DD
n-papers: N
n-papers-full-text: N
rango-anos: XXXX-XXXX
n-fuentes: X
tipo: revision-sistematica
modo: semilla|desde-cero
estado: completo
---

## Resumen ejecutivo

[3-5 oraciones con el hallazgo más importante. Debe poder leerse de forma
independiente y dar una respuesta concreta a la pregunta central.]

---

## Metodología de búsqueda

### Fuentes consultadas
[Lista de APIs consultadas con fechas de acceso]

### Estrategia de búsqueda
[Query maestra PubMed + descripción del proceso de traducción a cada API]

### Diagrama PRISMA simplificado

| Etapa | N |
|-------|---|
| Identificados (todas las fuentes) | N |
| Duplicados eliminados | N |
| Snowballing (forward + backward) | +N |
| Corpus final | N |
| Con full-text obtenido | N |

### Cobertura por fuente

| Fuente | Papers únicos | % del corpus |
|--------|--------------|-------------|
| PubMed | N | X% |
| OpenAlex | N | X% |
| ... | ... | ... |
| Snowballing | N | X% |
| **Total** | **N** | **100%** |

---

## Mapa temático

| # | Subtema | N papers | Descripción breve |
|---|---------|----------|------------------|
| 1 | [Subtema] | N | [1 línea] |
| 2 | [Subtema] | N | [1 línea] |
| ... | ... | ... | ... |

---

## Síntesis por subtema

### 1. [Subtema]

[Párrafo de síntesis. Citar con formato [Apellido, año].
Para papers con full-text, incluir datos cuantitativos específicos.]

### 2. [Subtema]

[Párrafo...]

[... hasta N subtemas]

---

## Análisis profundo (full-text)

[Síntesis detallada de los 10-15 papers con texto completo. Incluir:
metodología, resultados cuantitativos, y limitaciones reportadas.
Esta sección permite un nivel de detalle que los abstracts no ofrecen.]

---

## Calidad de la evidencia

[Breve evaluación de la base de evidencia:
- ¿Qué proporción son revisiones sistemáticas/meta-análisis vs estudios primarios?
- ¿Predominan RCTs, estudios observacionales, case reports?
- ¿Hay estudios con muestras grandes o la mayoría son pilotos?
- El nivel de evidencia general es alto, moderado o bajo?]

---

## Hallazgos principales

- [Hallazgo 1, con mayor consistencia] — [Apellido, año]; [Apellido, año]
- [Hallazgo 2] — [Apellido, año]
- ...

---

## Contradicciones explícitas

- [Tema donde Paper A concluye X pero Paper B concluye Y]
  - A favor de X: [Apellido, año] — [resumen del argumento/evidencia]
  - A favor de Y: [Apellido, año] — [resumen del argumento/evidencia]
  - Posible explicación: [diferencias metodológicas, poblaciones, etc.]
- ...

*(Si no hay contradicciones relevantes, omitir esta sección)*

---

## Gaps identificados

- [Pregunta importante sin respuesta en la literatura actual]
- [Área con muy pocos estudios o evidencia insuficiente]
- ...

---

## Papers recomendados

| Título | Año | Primer autor | Citas | Por qué es relevante |
|--------|-----|-------------|-------|---------------------|
| ... | ... | ... | ... | ... |

---

## Implicaciones para el proyecto

[Sección obligatoria: qué significa este conjunto de evidencia para las decisiones
del proyecto. Ser concreto — no repetir hallazgos, sino traducirlos en decisiones
o acciones específicas.]

---

## Cross-reference con semilla (solo modo A)

[Cuántos papers de la investigación original se re-encontraron en la búsqueda
sistemática. Esto valida que la búsqueda cubre el terreno conocido.]

---

## Referencias completas

- Apellido, A., & Apellido, B. (año). *Título del paper*. Nombre del journal.
- ...
```

#### Pasos finales

1. Actualizar `00-definicion.md` frontmatter: `estado: completo`
2. Ofrecer actualizar `docs/knowledge/INDEX.md` con la nueva entrada (si aplica)
3. Informar al usuario el resumen de la investigación completada

---

## Rate limits y manejo de errores

| API | Límite | Estrategia |
|-----|--------|-----------|
| PubMed MCP | ~3 req/s (NCBI) | Manejado por MCP internamente |
| PubMed E-utils | 3/s sin key, 10/s con key | Incluir `&api_key=` si disponible |
| OpenAlex | 10/s, 100K/día | Sin restricción práctica; incluir `mailto=` en URL |
| Semantic Scholar | 1/s sin key | Usar solo para queries clave, no como fuente primaria |
| Europe PMC | ~10/s, sin auth | Sin restricción práctica |
| arXiv | 1 req/3s | Limitar a 2-3 queries máximo |
| CrossRef | 50/s con mailto | Solo para resolver DOIs |

### Manejo de errores

- **API no responde**: esperar 5 segundos, reintentar 1 vez. Si falla de nuevo, documentar y continuar
- **Rate limit (429)**: documentar, pasar a otra fuente, volver a intentar al final
- **0 resultados**: simplificar query (quitar filtros, ampliar términos). Si sigue en 0, documentar
- **>200 resultados por query**: filtrar por año más reciente. No paginar indefinidamente
- **Tema sin cobertura en PubMed**: normal para temas no biomédicos. No es error

---

## Reglas

### Búsqueda
- **Queries en inglés** — la búsqueda académica funciona mejor en inglés
- **Query maestra primero** — siempre diseñar en sintaxis PubMed y luego traducir
- **Nunca usar NOT** — reduce recall (Cochrane Handbook lo desaconseja)
- **Validación PRESS obligatoria** — verificar 3 dominios antes de ejecutar
- **PubMed + OpenAlex siempre** — son las dos fuentes P0 sin importar el dominio

### Deduplicación
- **Script primero** — siempre intentar ejecutar deduplicar.py antes de deduplicar manualmente
- **Prioridad de registro maestro**: PubMed > Europe PMC > OpenAlex > Semantic Scholar > arXiv
- **Conservar abstract más completo** al fusionar duplicados
- **Nunca eliminar un paper único** — en caso de duda, mantener como no-duplicado

### Snowballing
- **5-10 semillas máximo** — seleccionadas por relevancia × citation count
- **50 papers nuevos máximo** por snowballing total
- **Deduplicar contra corpus existente** antes de agregar

### Full-text
- **Solo open access** — nunca intentar acceder a papers detrás de paywall
- **10-15 papers máximo** — seleccionados por relevancia y disponibilidad
- **Extraer secciones clave** — no copiar el texto completo

### Síntesis
- **No inventar hallazgos** — basar todo en lo que los abstracts/full-text dicen explícitamente
- **Citas inline** — formato `[Apellido, año]`, nunca números entre corchetes
- **Sección "Implicaciones"** — obligatoria, nunca omitirla
- **Sección "Calidad de evidencia"** — obligatoria, evaluar nivel general
- **Contradicciones** — documentar explícitamente cuando papers llegan a conclusiones opuestas
- **Si abstract dice "(sin abstract disponible)"** — incluir en estadísticas pero no en síntesis
- **Si hay menos de 15 papers con abstract** — avisar al usuario que la calidad será limitada

### Formato
- **Formato normalizado de papers** — respetar el formato exacto que parsea el script de deduplicación
- **Separar papers con líneas de guiones** (`----------------------------------------------------------------------`)
- **Frontmatter YAML** en todos los archivos de output
- **Un archivo por fase** — no mezclar outputs de fases diferentes

### Pausas
- **Pausa después de Fase 2** — obligatoria (el usuario debe validar queries)
- **Pausa después de Fase 5** — obligatoria (el usuario debe validar corpus)
- **No saltar pausas** — incluso si el usuario dice "ejecuta todo de corrido"

### Ejecución
- **Todo secuencial** — no lanzar agentes en paralelo para las búsquedas
- **Escribir a disco cada fase** — para no perder progreso si se interrumpe
- **No leer archivos intermedios en Fase 7** — solo leer 03-corpus-deduplicado.md
- **Cargar PubMed MCP tools** — siempre usar ToolSearch para cargar las herramientas diferidas antes de la primera llamada
- **Papers semilla en modo A** — verificar que ≥70% se re-encuentren; si no, ajustar queries
