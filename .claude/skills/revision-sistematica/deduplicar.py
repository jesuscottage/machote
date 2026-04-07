#!/usr/bin/env python3
"""
Deduplicador de papers academicos para busquedas sistematicas.

Pipeline de 4 fases:
  1. Normalizacion de campos
  2. Coincidencia exacta por DOI
  3. Coincidencia exacta por PMID
  4. Fuzzy matching por titulo + autor + ano

Uso:
    python deduplicar.py <ruta_archivo_resultados_crudos.md>

Genera un archivo 03-corpus-deduplicado.md en la misma carpeta.

Solo usa stdlib de Python (difflib, re, collections) — sin dependencias externas.
"""

import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path


# --- Modelo de datos ---

class Paper:
    """Representa un paper normalizado."""

    def __init__(self):
        self.numero = 0
        self.ano = ""
        self.autor_header = ""
        self.titulo = ""
        self.abstract = ""
        self.doi = ""
        self.pmid = ""
        self.fuente = ""
        self.citas = ""
        self.open_access = ""
        # Campos de deduplicacion
        self.titulo_norm = ""
        self.doi_norm = ""
        self.primer_autor_norm = ""
        self.fuentes = []  # lista de fuentes donde aparecio
        self.raw_text = ""  # texto original completo

    def __repr__(self):
        return f"Paper({self.numero}, {self.ano}, {self.titulo[:50]}...)"


# --- Fase 0: Parsing ---

SEPARATOR = "-" * 70


def parsear_archivo(ruta: Path) -> list[Paper]:
    """Parsea el archivo de resultados crudos y extrae papers."""
    contenido = ruta.read_text(encoding="utf-8")
    bloques = contenido.split(SEPARATOR)
    papers = []

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque or bloque.startswith("---") or bloque.startswith("#"):
            continue

        paper = Paper()
        paper.raw_text = bloque
        lineas = bloque.split("\n")

        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue

            # Header: [N] (AÑO) Apellido et al.
            match_header = re.match(r"\[(\d+)\]\s*\((\d{4})\)\s*(.*)", linea)
            if match_header:
                paper.numero = int(match_header.group(1))
                paper.ano = match_header.group(2)
                paper.autor_header = match_header.group(3).strip()
                continue

            if linea.startswith("TITULO:"):
                paper.titulo = linea[7:].strip()
            elif linea.startswith("ABSTRACT:"):
                paper.abstract = linea[9:].strip()
            elif linea.startswith("DOI:"):
                paper.doi = linea[4:].strip()
            elif linea.startswith("PMID:"):
                paper.pmid = linea[5:].strip()
            elif linea.startswith("FUENTE:"):
                paper.fuente = linea[7:].strip()
            elif linea.startswith("FUENTES:"):
                paper.fuente = linea[8:].strip()
            elif linea.startswith("CITAS:"):
                paper.citas = linea[6:].strip()
            elif linea.startswith("OPEN_ACCESS:"):
                paper.open_access = linea[12:].strip()

        # Solo agregar si tiene al menos titulo
        if paper.titulo and paper.titulo != "(sin titulo)":
            papers.append(paper)

    return papers


# --- Fase 1: Normalizacion ---

def normalizar_doi(doi: str) -> str:
    """Normaliza DOI: lowercase, sin prefijo URL."""
    if not doi or doi == "-":
        return ""
    doi = doi.lower().strip()
    # Remover prefijos URL comunes
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:", "doi.org/"]:
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi


def normalizar_titulo(titulo: str) -> str:
    """Normaliza titulo: lowercase, sin puntuacion, sin articulos."""
    t = titulo.lower().strip()
    # Remover puntuacion
    t = re.sub(r"[^\w\s]", "", t)
    # Remover articulos al inicio
    t = re.sub(r"^(the|a|an)\s+", "", t)
    # Colapsar espacios
    t = re.sub(r"\s+", " ", t).strip()
    return t


def normalizar_autor(autor: str) -> str:
    """Extrae apellido del primer autor, normalizado."""
    if not autor:
        return ""
    autor = autor.strip()
    # Remover "et al."
    autor = re.sub(r"\s*et\s+al\.?\s*$", "", autor, flags=re.IGNORECASE)
    # Si tiene coma, tomar antes de la coma (apellido)
    if "," in autor:
        autor = autor.split(",")[0]
    # Si tiene espacios, tomar la ultima palabra (apellido)
    elif " " in autor:
        partes = autor.split()
        autor = partes[-1]
    return autor.lower().strip()


def normalizar_papers(papers: list[Paper]) -> None:
    """Aplica normalizacion a todos los papers (in-place)."""
    for p in papers:
        p.doi_norm = normalizar_doi(p.doi)
        p.titulo_norm = normalizar_titulo(p.titulo)
        p.primer_autor_norm = normalizar_autor(p.autor_header)
        p.fuentes = [p.fuente] if p.fuente else []


# --- Fase 2: Coincidencia por DOI ---

def dedup_por_doi(papers: list[Paper]) -> tuple[list[Paper], int]:
    """Agrupa papers por DOI exacto. Retorna (unicos, n_duplicados)."""
    con_doi = {}
    sin_doi = []
    n_dupes = 0

    for p in papers:
        if not p.doi_norm:
            sin_doi.append(p)
            continue
        if p.doi_norm in con_doi:
            maestro = con_doi[p.doi_norm]
            # Verificar que titulos sean minimamente similares (>0.70)
            sim = SequenceMatcher(None, maestro.titulo_norm, p.titulo_norm).ratio()
            if sim >= 0.70:
                # Fusionar: mantener abstract mas completo
                if len(p.abstract) > len(maestro.abstract):
                    maestro.abstract = p.abstract
                maestro.fuentes.append(p.fuente)
                n_dupes += 1
            else:
                # DOI compartido pero titulos muy diferentes (ej: coleccion de abstracts)
                sin_doi.append(p)
        else:
            con_doi[p.doi_norm] = p

    return list(con_doi.values()) + sin_doi, n_dupes


# --- Fase 3: Coincidencia por PMID ---

def dedup_por_pmid(papers: list[Paper]) -> tuple[list[Paper], int]:
    """Agrupa papers por PMID exacto. Retorna (unicos, n_duplicados)."""
    con_pmid = {}
    sin_pmid = []
    n_dupes = 0

    for p in papers:
        pmid = p.pmid.strip()
        if not pmid or pmid == "-":
            sin_pmid.append(p)
            continue
        if pmid in con_pmid:
            maestro = con_pmid[pmid]
            if len(p.abstract) > len(maestro.abstract):
                maestro.abstract = p.abstract
            maestro.fuentes.append(p.fuente)
            n_dupes += 1
        else:
            con_pmid[pmid] = p

    return list(con_pmid.values()) + sin_pmid, n_dupes


# --- Fase 4: Fuzzy matching ---

def dedup_fuzzy(papers: list[Paper], umbral_titulo: float = 0.90) -> tuple[list[Paper], int]:
    """
    Fuzzy matching por titulo + autor + ano.
    Usa blocking por ano + primeras 3 letras del primer autor.
    """
    n_dupes = 0

    # Crear bloques para reducir comparaciones
    bloques = defaultdict(list)
    for p in papers:
        # Key de blocking: ano + primeras 3 letras del apellido
        key = f"{p.ano}_{p.primer_autor_norm[:3]}" if p.primer_autor_norm else f"{p.ano}_"
        bloques[key].append(p)

    # Tambien crear bloques solo por ano (para autores con variaciones)
    bloques_ano = defaultdict(list)
    for p in papers:
        bloques_ano[p.ano].append(p)

    eliminados = set()

    # Comparar dentro de cada bloque
    for key, bloque in bloques.items():
        for i in range(len(bloque)):
            if id(bloque[i]) in eliminados:
                continue
            for j in range(i + 1, len(bloque)):
                if id(bloque[j]) in eliminados:
                    continue

                sim_titulo = SequenceMatcher(
                    None, bloque[i].titulo_norm, bloque[j].titulo_norm
                ).ratio()

                if sim_titulo >= umbral_titulo:
                    # Duplicado confirmado
                    maestro = bloque[i]
                    dup = bloque[j]
                    if len(dup.abstract) > len(maestro.abstract):
                        maestro.abstract = dup.abstract
                    maestro.fuentes.extend(dup.fuentes)
                    eliminados.add(id(dup))
                    n_dupes += 1
                elif sim_titulo >= 0.80:
                    # Candidato: verificar autor + ano
                    sim_autor = SequenceMatcher(
                        None,
                        bloque[i].primer_autor_norm,
                        bloque[j].primer_autor_norm,
                    ).ratio()
                    ano_cercano = abs(int(bloque[i].ano or 0) - int(bloque[j].ano or 0)) <= 1
                    if sim_autor >= 0.80 and ano_cercano:
                        maestro = bloque[i]
                        dup = bloque[j]
                        if len(dup.abstract) > len(maestro.abstract):
                            maestro.abstract = dup.abstract
                        maestro.fuentes.extend(dup.fuentes)
                        eliminados.add(id(dup))
                        n_dupes += 1

    resultado = [p for p in papers if id(p) not in eliminados]
    return resultado, n_dupes


# --- Output ---

def generar_output(
    papers: list[Paper],
    stats: dict,
    ruta_output: Path,
    tema: str = "",
) -> None:
    """Genera el archivo de corpus deduplicado."""
    # Limpiar fuentes duplicadas y vacias
    for p in papers:
        p.fuentes = list(dict.fromkeys(f for f in p.fuentes if f))

    lineas = []
    lineas.append("---")
    lineas.append(f"tema: {tema}")
    lineas.append(f"estado: corpus-deduplicado")
    lineas.append(f"n-papers-unicos: {len(papers)}")
    lineas.append(f"n-total-importados: {stats['total']}")
    lineas.append(f"n-duplicados-eliminados: {stats['total'] - len(papers)}")
    lineas.append("---")
    lineas.append("")
    lineas.append("## Resumen de deduplicacion")
    lineas.append("")
    lineas.append(f"- **Papers importados**: {stats['total']}")
    lineas.append(f"- **Duplicados por DOI**: {stats['doi']}")
    lineas.append(f"- **Duplicados por PMID**: {stats['pmid']}")
    lineas.append(f"- **Duplicados por fuzzy matching**: {stats['fuzzy']}")
    lineas.append(f"- **Total duplicados eliminados**: {stats['doi'] + stats['pmid'] + stats['fuzzy']}")
    lineas.append(f"- **Papers unicos**: {len(papers)}")
    tasa = (stats['doi'] + stats['pmid'] + stats['fuzzy']) / max(stats['total'], 1) * 100
    lineas.append(f"- **Tasa de deduplicacion**: {tasa:.1f}%")
    lineas.append("")

    # Distribucion por fuente
    conteo_fuentes = defaultdict(int)
    for p in papers:
        for f in p.fuentes:
            conteo_fuentes[f] += 1
    if conteo_fuentes:
        lineas.append("## Cobertura por fuente")
        lineas.append("")
        lineas.append("| Fuente | Papers unicos | % del corpus |")
        lineas.append("|--------|--------------|-------------|")
        for fuente, count in sorted(conteo_fuentes.items(), key=lambda x: -x[1]):
            pct = count / max(len(papers), 1) * 100
            lineas.append(f"| {fuente} | {count} | {pct:.1f}% |")
        lineas.append(f"| **Total** | **{len(papers)}** | **100%** |")
        lineas.append("")

    lineas.append("## Corpus")
    lineas.append("")

    # Papers renumerados
    for i, p in enumerate(papers, 1):
        lineas.append(SEPARATOR)
        lineas.append("")
        fuentes_str = ", ".join(p.fuentes) if p.fuentes else p.fuente or "Desconocida"
        lineas.append(f"[{i}] ({p.ano}) {p.autor_header}")
        lineas.append(f"TITULO: {p.titulo}")
        lineas.append(f"ABSTRACT: {p.abstract}")
        lineas.append(f"DOI: {p.doi if p.doi and p.doi != '-' else '-'}")
        lineas.append(f"PMID: {p.pmid if p.pmid and p.pmid != '-' else '-'}")
        lineas.append(f"FUENTES: {fuentes_str}")
        lineas.append(f"CITAS: {p.citas}")
        lineas.append(f"OPEN_ACCESS: {p.open_access}")
        lineas.append("")

    lineas.append(SEPARATOR)

    ruta_output.write_text("\n".join(lineas), encoding="utf-8")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print("Uso: python deduplicar.py <ruta_archivo_resultados_crudos.md>")
        print("")
        print("Genera 03-corpus-deduplicado.md en la misma carpeta.")
        sys.exit(1)

    ruta_input = Path(sys.argv[1])

    if not ruta_input.exists():
        print(f"Error: no se encontro '{ruta_input}'")
        sys.exit(1)

    # Extraer tema del frontmatter si existe
    tema = ""
    contenido = ruta_input.read_text(encoding="utf-8")
    match_tema = re.search(r"^tema:\s*(.+)$", contenido, re.MULTILINE)
    if match_tema:
        tema = match_tema.group(1).strip()

    print(f"Leyendo: {ruta_input}")
    papers = parsear_archivo(ruta_input)
    total = len(papers)
    print(f"Papers parseados: {total}")

    if total == 0:
        print("No se encontraron papers. Verificar formato del archivo.")
        sys.exit(1)

    # Fase 1: Normalizacion
    print("\nFase 1: Normalizacion...")
    normalizar_papers(papers)

    # Fase 2: DOI
    print("Fase 2: Deduplicacion por DOI...")
    papers, n_doi = dedup_por_doi(papers)
    print(f"  Duplicados por DOI: {n_doi}")

    # Fase 3: PMID
    print("Fase 3: Deduplicacion por PMID...")
    papers, n_pmid = dedup_por_pmid(papers)
    print(f"  Duplicados por PMID: {n_pmid}")

    # Fase 4: Fuzzy
    print("Fase 4: Fuzzy matching (titulo + autor + ano)...")
    papers, n_fuzzy = dedup_fuzzy(papers)
    print(f"  Duplicados por fuzzy: {n_fuzzy}")

    # Resumen
    total_dupes = n_doi + n_pmid + n_fuzzy
    print(f"\n{'='*50}")
    print(f"Total importados:     {total}")
    print(f"Duplicados eliminados: {total_dupes}")
    print(f"  - Por DOI:          {n_doi}")
    print(f"  - Por PMID:         {n_pmid}")
    print(f"  - Por fuzzy:        {n_fuzzy}")
    print(f"Papers unicos:        {len(papers)}")
    print(f"Tasa de deduplicacion: {total_dupes / max(total, 1) * 100:.1f}%")

    # Generar output
    ruta_output = ruta_input.parent / "03-corpus-deduplicado.md"
    stats = {"total": total, "doi": n_doi, "pmid": n_pmid, "fuzzy": n_fuzzy}
    generar_output(papers, stats, ruta_output, tema)
    print(f"\nOutput: {ruta_output}")


if __name__ == "__main__":
    main()
