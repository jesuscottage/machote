#!/usr/bin/env python3
"""
Extrae titulo y abstract de exportaciones CSV de Elicit u otras herramientas.

Uso:
    python extraer_abstracts.py <ruta_carpeta>

Por cada archivo *-resultados.csv encontrado en la carpeta, genera un archivo
*_abstracts.txt con titulo, abstract, ano y primer autor de cada paper en
formato normalizado compatible con el script de deduplicacion.

Ejemplo:
    python .claude/skills/revision-sistematica/extraer_abstracts.py \
        docs/research/mi-tema/

Solo usa stdlib de Python — sin dependencias externas.
"""

import csv
import sys
from pathlib import Path

# Posibles nombres de columna segun la version del CSV
TITLE_COLS = ["Title", "title", "Paper Title", "paper_title"]
ABSTRACT_COLS = ["Abstract", "abstract", "Summary", "summary"]
YEAR_COLS = ["Year", "year", "Publication Year", "publication_year"]
AUTHORS_COLS = ["Authors", "authors", "Author", "author"]
DOI_COLS = ["DOI", "doi", "Digital Object Identifier"]
PMID_COLS = ["PMID", "pmid", "PubMed ID", "pubmed_id"]

# Encodings a intentar (el primero es el mas comun en Elicit)
ENCODINGS = ["utf-8-sig", "utf-8", "latin-1", "cp1252"]

SEPARATOR = "-" * 70


def get_col(row: dict, candidates: list) -> str:
    """Retorna el primer valor no vacio de las columnas candidatas."""
    for col in candidates:
        if col in row and row[col].strip():
            return row[col].strip()
    return ""


def detectar_separador(primera_linea: str) -> str:
    """Detecta si el CSV usa coma o punto y coma como separador."""
    comas = primera_linea.count(",")
    puntos_y_coma = primera_linea.count(";")
    return ";" if puntos_y_coma > comas else ","


def abrir_csv(csv_path: Path):
    """Abre el CSV probando distintos encodings."""
    for enc in ENCODINGS:
        try:
            with open(csv_path, encoding=enc, newline="") as f:
                primera_linea = f.readline()
            separador = detectar_separador(primera_linea)
            f = open(csv_path, encoding=enc, newline="")
            return f, enc, separador
        except (UnicodeDecodeError, UnicodeError):
            continue
    raise RuntimeError(
        f"No se pudo leer '{csv_path.name}' con ninguno de los encodings "
        f"probados: {ENCODINGS}."
    )


def formatear_autor(authors_str: str) -> str:
    """Extrae 'Apellido et al.' del primer autor."""
    if not authors_str:
        return ""

    lista = [a.strip() for a in authors_str.split(";") if a.strip()]
    if not lista:
        lista = [authors_str.strip()]

    primer_autor = lista[0]
    if "," in primer_autor:
        apellido = primer_autor.split(",")[0].strip()
    else:
        partes = primer_autor.split()
        apellido = partes[-1] if partes else primer_autor

    return f"{apellido} et al." if len(lista) > 1 else apellido


def process_csv(csv_path: Path) -> int:
    """Procesa un CSV y genera el archivo _abstracts.txt en formato normalizado."""
    out_path = csv_path.with_name(csv_path.stem + "_abstracts.txt")

    try:
        f, encoding_usado, separador = abrir_csv(csv_path)
    except RuntimeError as e:
        print(f"  [ERROR] {e}")
        return 0

    count = 0
    with f, open(out_path, "w", encoding="utf-8") as out:
        reader = csv.DictReader(f, delimiter=separador)

        if reader.fieldnames is None:
            print(f"  [ERROR] {csv_path.name}: archivo vacio o sin encabezados")
            return 0

        has_title = any(c in reader.fieldnames for c in TITLE_COLS)
        if not has_title:
            print(f"  [ERROR] {csv_path.name}: no se encontro columna de titulo")
            print(f"    Columnas detectadas: {', '.join(reader.fieldnames[:10])}")
            return 0

        out.write(f"# Abstracts de: {csv_path.name}\n")
        out.write(f"# Encoding: {encoding_usado} | Separador: '{separador}'\n\n")

        for i, row in enumerate(reader, 1):
            title = get_col(row, TITLE_COLS) or "(sin titulo)"
            abstract = get_col(row, ABSTRACT_COLS) or "(sin abstract disponible)"
            year = get_col(row, YEAR_COLS) or "s/f"
            authors = get_col(row, AUTHORS_COLS)
            doi = get_col(row, DOI_COLS)
            pmid = get_col(row, PMID_COLS)

            autor_fmt = formatear_autor(authors) if authors else "Desconocido"

            out.write(SEPARATOR + "\n")
            out.write(f"[{i}] ({year}) {autor_fmt}\n")
            out.write(f"TITULO: {title}\n")
            out.write(f"ABSTRACT: {abstract}\n")
            out.write(f"DOI: {doi if doi else '-'}\n")
            out.write(f"PMID: {pmid if pmid else '-'}\n")
            out.write(f"FUENTE: Elicit-CSV\n")
            out.write(f"CITAS: -\n")
            out.write(f"OPEN_ACCESS: -\n")
            out.write(SEPARATOR + "\n\n")
            count += 1

    print(f"  OK {csv_path.name}: {count} papers -> {out_path.name}")
    return count


def main():
    if len(sys.argv) < 2:
        print("Uso: python extraer_abstracts.py <ruta_carpeta>")
        sys.exit(1)

    folder = Path(sys.argv[1])
    if not folder.exists():
        print(f"Error: la carpeta '{folder}' no existe.")
        sys.exit(1)

    csvs = sorted(folder.glob("*-resultados.csv"))
    if not csvs:
        # Intentar con cualquier CSV
        csvs = sorted(folder.glob("*.csv"))

    if not csvs:
        print(f"No se encontraron archivos CSV en: {folder}")
        sys.exit(1)

    print(f"Procesando {len(csvs)} archivo(s) CSV en: {folder}\n")

    total = 0
    for csv_path in csvs:
        total += process_csv(csv_path)

    print(f"\nTotal: {total} abstracts extraidos de {len(csvs)} archivo(s).")
    print("Los archivos *_abstracts.txt estan listos.")
    print(f"Puedes pasarlos a deduplicar.py si combinas multiples fuentes.")


if __name__ == "__main__":
    main()
