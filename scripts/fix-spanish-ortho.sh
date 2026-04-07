#!/usr/bin/env bash
# fix-spanish-ortho.sh — Corrige ortografía española en archivos markdown
# Uso: ./scripts/fix-spanish-ortho.sh [--apply] <archivo-o-directorio>
#
# Por defecto muestra los cambios (dry-run). Con --apply los aplica.
# Diseñado para docs/knowledge/ del proyecto Delph-AI.
#
# PROTECCIONES:
# - No modifica líneas con URLs (http://, https://)
# - No modifica contenido dentro de links markdown: (texto-con-guiones.md)
# - No modifica líneas de frontmatter con claves tipo "fecha-revision:"
# - Palabras ambiguas (publica/publico/mas) excluidas por ser verbos o conjunciones
# - Word-boundary (\b) en todas las sustituciones de Categoría B

set -euo pipefail

APPLY=false
TARGET=""

# --- Parsear argumentos ---
for arg in "$@"; do
  case "$arg" in
    --apply) APPLY=true ;;
    *) TARGET="$arg" ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "Uso: $0 [--apply] <archivo-o-directorio>"
  echo "  Sin --apply: muestra cambios (dry-run)"
  echo "  Con --apply: aplica las correcciones"
  exit 1
fi

# --- Encontrar archivos .md ---
if [[ -d "$TARGET" ]]; then
  FILES=$(find "$TARGET" -name "*.md" -type f | sort)
elif [[ -f "$TARGET" ]]; then
  FILES="$TARGET"
else
  echo "Error: '$TARGET' no existe"
  exit 1
fi

TOTAL_FILES=0
TOTAL_CHANGES=0
CHANGED_FILES=0

# --- Función de sustituciones ---
apply_fixes() {
  local file="$1"
  local tmp="${file}.ortho-tmp"

  cp "$file" "$tmp"

  # ============================================================
  # CATEGORÍA A: Plurales con acentos INCORRECTOS
  # Estas palabras NUNCA son correctas — reemplazo directo
  # En español: -ción (singular) → -ciones (plural, SIN tilde)
  # Seguro incluso en URLs porque estas formas incorrectas no existen
  # ============================================================
  sed -i \
    -e 's/revisiónes/revisiones/g' \
    -e 's/Revisiónes/Revisiones/g' \
    -e 's/evaluaciónes/evaluaciones/g' \
    -e 's/Evaluaciónes/Evaluaciones/g' \
    -e 's/instalaciónes/instalaciones/g' \
    -e 's/Instalaciónes/Instalaciones/g' \
    -e 's/instituciónales/institucionales/g' \
    -e 's/Instituciónales/Institucionales/g' \
    -e 's/publicaciónes/publicaciones/g' \
    -e 's/Publicaciónes/Publicaciones/g' \
    -e 's/decisiónes/decisiones/g' \
    -e 's/Decisiónes/Decisiones/g' \
    -e 's/organizaciónes/organizaciones/g' \
    -e 's/Organizaciónes/Organizaciones/g' \
    -e 's/configuraciónes/configuraciones/g' \
    -e 's/certificaciónes/certificaciones/g' \
    -e 's/suscripciónes/suscripciones/g' \
    -e 's/investigaciónes/investigaciones/g' \
    -e 's/recomendaciónes/recomendaciones/g' \
    -e 's/regulaciónes/regulaciones/g' \
    -e 's/aplicaciónes/aplicaciones/g' \
    -e 's/especificaciónes/especificaciones/g' \
    -e 's/situaciónes/situaciones/g' \
    -e 's/condiciónes/condiciones/g' \
    -e 's/limitaciónes/limitaciones/g' \
    -e 's/funciónes/funciones/g' \
    -e 's/Funciónes/Funciones/g' \
    -e 's/opciónes/opciones/g' \
    -e 's/Opciónes/Opciones/g' \
    -e 's/instrucciónes/instrucciones/g' \
    -e 's/secciónes/secciones/g' \
    -e 's/Secciónes/Secciones/g' \
    -e 's/relaciónes/relaciones/g' \
    -e 's/Relaciónes/Relaciones/g' \
    -e 's/versiónes/versiones/g' \
    -e 's/Versiónes/Versiones/g' \
    -e 's/operaciónes/operaciones/g' \
    -e 's/instituciónal/institucional/g' \
    -e 's/Instituciónal/Institucional/g' \
    -e 's/profesiónal/profesional/g' \
    -e 's/Profesiónal/Profesional/g' \
    -e 's/internaciónal/internacional/g' \
    -e 's/Internaciónal/Internacional/g' \
    -e 's/naciónal/nacional/g' \
    -e 's/Naciónal/Nacional/g' \
    -e 's/convenciónal/convencional/g' \
    -e 's/tradiciónales/tradicionales/g' \
    -e 's/adiciónales/adicionales/g' \
    -e 's/funciónal/funcional/g' \
    -e 's/métodología/metodología/g' \
    -e 's/públicación/publicación/g' \
    -e 's/públicaciones/publicaciones/g' \
    "$tmp"

  # ============================================================
  # CATEGORÍA B: Acentos faltantes (word-boundary con \b)
  # Solo reemplaza palabras completas para evitar falsos positivos
  #
  # EXCLUYE líneas que contengan:
  #   - URLs (http:// o https://)
  #   - Links markdown a archivos: ](algo-con-guion.md)
  #   - Claves de frontmatter con guión: "fecha-revision:", "n-busquedas:"
  #
  # PALABRAS EXCLUIDAS del diccionario (ambiguas verbo/adjetivo):
  #   - publica (verbo "publicar": él publica)
  #   - publico (verbo "publicar": yo publico)
  #   - practica (verbo "practicar" o sustantivo sin acento en ciertos contextos)
  #   - mas (conjunción adversativa = "pero")
  # ============================================================

  # Usar un script awk para aplicar sustituciones solo en líneas seguras
  awk '
  # Saltar líneas con URLs (con o sin protocolo)
  /https?:\/\// { print; next }
  # Saltar líneas con dominios sin protocolo (algo.mx, algo.com, etc.)
  /[a-zA-Z0-9]+\.(mx|com|org|edu|net|gov|io)/ { print; next }
  # Saltar líneas con links markdown a archivos .md
  /\]\([^)]*\.md\)/ { print; next }
  # Saltar líneas de frontmatter con claves-guión (fecha-revision, n-busquedas, etc.)
  /^[a-z]+-[a-z]+:/ { print; next }
  {
    # Palabras inequívocas — solo sustantivos/adjetivos que SIEMPRE llevan acento
    gsub(/\yanalisis\y/, "análisis")
    gsub(/\yAnalisis\y/, "Análisis")
    gsub(/\ymetodologia\y/, "metodología")
    gsub(/\yMetodologia\y/, "Metodología")
    gsub(/\ydocumentacion\y/, "documentación")
    gsub(/\yDocumentacion\y/, "Documentación")
    gsub(/\yinformacion\y/, "información")
    gsub(/\yInformacion\y/, "Información")
    gsub(/\yultima\y/, "última")
    gsub(/\yultimo\y/, "último")
    gsub(/\yunico\y/, "único")
    gsub(/\yunica\y/, "única")
    gsub(/\ybusqueda\y/, "búsqueda")
    gsub(/\ybusquedas\y/, "búsquedas")
    gsub(/\yindice\y/, "índice")
    gsub(/\ypagina\y/, "página")
    gsub(/\ypaginas\y/, "páginas")
    gsub(/\ycodigo\y/, "código")
    gsub(/\yproduccion\y/, "producción")
    gsub(/\yautenticacion\y/, "autenticación")
    gsub(/\yconfiguracion\y/, "configuración")
    gsub(/\ygestion\y/, "gestión")
    gsub(/\ynavegacion\y/, "navegación")
    gsub(/\ycreacion\y/, "creación")
    gsub(/\yestadisticas\y/, "estadísticas")
    gsub(/\ytecnico\y/, "técnico")
    gsub(/\ytecnica\y/, "técnica")
    gsub(/\ytecnicos\y/, "técnicos")
    gsub(/\ytecnicas\y/, "técnicas")
    gsub(/\yacademico\y/, "académico")
    gsub(/\yacademica\y/, "académica")
    gsub(/\yacademicos\y/, "académicos")
    gsub(/\yacademicas\y/, "académicas")
    gsub(/\yautomatico\y/, "automático")
    gsub(/\yautomatica\y/, "automática")
    gsub(/\ydiseno\y/, "diseño")
    gsub(/\ytamano\y/, "tamaño")
    gsub(/\ypequeno\y/, "pequeño")
    gsub(/\ypequena\y/, "pequeña")
    gsub(/\ytambien\y/, "también")
    gsub(/\yTambien\y/, "También")
    gsub(/\ydescripcion\y/, "descripción")
    gsub(/\ydeduplicacion\y/, "deduplicación")
    gsub(/\ytipografia\y/, "tipografía")
    gsub(/\yauditoria\y/, "auditoría")
    gsub(/\ysemantico\y/, "semántico")
    gsub(/\yespanol\y/, "español")
    gsub(/\yhibrido\y/, "híbrido")
    gsub(/\yfuncion\y/, "función")
    gsub(/\ysesion\y/, "sesión")
    gsub(/\yproteccion\y/, "protección")
    gsub(/\ymodulo\y/, "módulo")
    gsub(/\ypatron\y/, "patrón")
    gsub(/\yextraccion\y/, "extracción")
    gsub(/\ycategorica\y/, "categórica")
    gsub(/\yatencion\y/, "atención")
    gsub(/\yposicion\y/, "posición")
    gsub(/\ycomparacion\y/, "comparación")
    gsub(/\yevaluacion\y/, "evaluación")
    gsub(/\ysolucion\y/, "solución")
    gsub(/\yclasificacion\y/, "clasificación")
    gsub(/\ysuscripcion\y/, "suscripción")
    gsub(/\ySuscripcion\y/, "Suscripción")
    gsub(/\yorganizacion\y/, "organización")
    gsub(/\yOrganizacion\y/, "Organización")
    gsub(/\ypublicacion\y/, "publicación")
    gsub(/\yPublicacion\y/, "Publicación")
    gsub(/\ydecision\y/, "decisión")
    gsub(/\yregulacion\y/, "regulación")
    gsub(/\yaplicacion\y/, "aplicación")
    gsub(/\yespecificacion\y/, "especificación")
    gsub(/\ycondicion\y/, "condición")
    gsub(/\ylimitacion\y/, "limitación")
    gsub(/\yoperacion\y/, "operación")
    gsub(/\yseccion\y/, "sección")
    gsub(/\ySeccion\y/, "Sección")
    gsub(/\yrelacion\y/, "relación")
    gsub(/\yinstruccion\y/, "instrucción")
    gsub(/\yopcion\y/, "opción")
    gsub(/\yprecision\y/, "precisión")
    gsub(/\yPrecision\y/, "Precisión")
    gsub(/\yreduccion\y/, "reducción")
    gsub(/\ydireccion\y/, "dirección")
    gsub(/\yademas\y/, "además")
    gsub(/\yAdemas\y/, "Además")
    gsub(/\ynumero\y/, "número")
    gsub(/\ynumeros\y/, "números")
    gsub(/\ynumerico\y/, "numérico")
    gsub(/\ynumerica\y/, "numérica")
    gsub(/\ynumericos\y/, "numéricos")
    gsub(/\ybasico\y/, "básico")
    gsub(/\ybasica\y/, "básica")
    gsub(/\ydinamico\y/, "dinámico")
    gsub(/\ydinamica\y/, "dinámica")
    gsub(/\ytraves\y/, "través")
    gsub(/\ytipico\y/, "típico")
    gsub(/\ytipica\y/, "típica")
    gsub(/\ygenerico\y/, "genérico")
    gsub(/\ygenerica\y/, "genérica")
    gsub(/\ygenericos\y/, "genéricos")
    gsub(/\ygenericas\y/, "genéricas")
    gsub(/\ymetrica\y/, "métrica")
    gsub(/\ymetricas\y/, "métricas")
    gsub(/\ydiagnostico\y/, "diagnóstico")
    gsub(/\yproposito\y/, "propósito")
    gsub(/\ycritico\y/, "crítico")
    gsub(/\ycritica\y/, "crítica")
    gsub(/\ycriticos\y/, "críticos")
    gsub(/\ycriticas\y/, "críticas")
    gsub(/\yexplicito\y/, "explícito")
    gsub(/\yexplicita\y/, "explícita")
    gsub(/\yperiodo\y/, "período")
    gsub(/\yperiodos\y/, "períodos")
    # revision/version: solo como sustantivos sueltos (no en compuestos con guión)
    gsub(/\yrevision\y/, "revisión")
    gsub(/\yRevision\y/, "Revisión")
    gsub(/\yversion\y/, "versión")
    gsub(/\yVersion\y/, "Versión")
    gsub(/\yinvestigacion\y/, "investigación")
    gsub(/\yInvestigacion\y/, "Investigación")
    print
  }
  ' "$tmp" > "${tmp}.awk" && mv "${tmp}.awk" "$tmp"

  # --- Comparar ---
  local changes
  changes=$(diff "$file" "$tmp" 2>/dev/null || true)

  if [[ -n "$changes" ]]; then
    local count
    count=$(echo "$changes" | grep -c "^[<>]" || true)
    TOTAL_CHANGES=$((TOTAL_CHANGES + count / 2))
    CHANGED_FILES=$((CHANGED_FILES + 1))

    if [[ "$APPLY" == true ]]; then
      mv "$tmp" "$file"
      echo "  ✓ $(basename "$file") — $((count / 2)) correcciones aplicadas"
    else
      echo "  ⚠ $(basename "$file") — $((count / 2)) correcciones pendientes:"
      diff --color=auto -u "$file" "$tmp" | head -50 || true
      echo ""
      rm "$tmp"
    fi
  else
    rm "$tmp"
  fi

  TOTAL_FILES=$((TOTAL_FILES + 1))
}

# --- Procesar archivos ---
echo ""
if [[ "$APPLY" == true ]]; then
  echo "═══ Aplicando correcciones ortográficas ═══"
else
  echo "═══ Dry-run: mostrando correcciones pendientes ═══"
fi
echo ""

while IFS= read -r file; do
  apply_fixes "$file"
done <<< "$FILES"

echo ""
echo "═══ Resumen ═══"
echo "  Archivos procesados: $TOTAL_FILES"
echo "  Archivos con cambios: $CHANGED_FILES"
echo "  Correcciones totales: $TOTAL_CHANGES"
if [[ "$APPLY" != true && $CHANGED_FILES -gt 0 ]]; then
  echo ""
  echo "  Ejecutar con --apply para aplicar los cambios."
fi
