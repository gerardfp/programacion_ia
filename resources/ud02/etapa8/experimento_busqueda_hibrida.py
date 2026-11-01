# resources/ud02/etapa8/experimento_busqueda_hibrida.py
"""
Etapa 8 (Go Beyond): Mejoras avanzadas sobre la recuperación vectorial básica.
1. Demostración de fragmentación con solapamiento (Chunk Overlap) y cabecera contextual
   para no perder el sujeto del documento al cortar textos largos.
2. Benchmark comparativo en PostgreSQL:
   - Búsqueda Léxica Pura (Full-Text Search en español con tsvector / tsquery)
   - Búsqueda Semántica Pura (pgvector con distancia coseno <=>)
   - Búsqueda Híbrida con Reciprocal Rank Fusion (RRF) combinando ambas en una sola consulta SQL
     y manteniendo siempre el filtro de autorización en origen (WHERE departamento = %s).
"""

import sys
from pathlib import Path
import psycopg

# Añadimos la raíz de resources/ud02 al path para importar el paquete src
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.ingesta import ingestar_corpus_json
from src.recuperador import RecuperadorRAG

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"


# ======================================================================================
# PARTE 1: FRAGMENTACIÓN CON SOLAPAMIENTO (CHUNK OVERLAP) Y CABECERA CONTEXTUAL
# ======================================================================================

def fragmentar_con_solapamiento(
    texto: str,
    cabecera_contexto: str,
    tamano_ventana: int = 180,
    solapamiento: int = 45,
) -> list[str]:
    """
    Divide un texto en fragmentos de 'tamano_ventana' caracteres con un solapamiento
    de 'solapamiento' caracteres entre fragmentos consecutivos, anteponiendo siempre
    la cabecera contextual del documento para evitar fragmentos 'huérfanos'.
    """
    if solapamiento >= tamano_ventana:
        raise ValueError("El solapamiento debe ser menor que el tamaño de ventana.")

    paso = tamano_ventana - solapamiento
    fragmentos: list[str] = []
    inicio = 0

    while inicio < len(texto):
        trozo = texto[inicio : inicio + tamano_ventana].strip()
        if trozo:
            fragmentos.append(f"[{cabecera_contexto}] {trozo}")
        if inicio + tamano_ventana >= len(texto):
            break
        inicio += paso

    return fragmentos


# ======================================================================================
# PARTE 2: BÚSQUEDA LÉXICA, SEMÁNTICA E HÍBRIDA (RRF) EN POSTGRESQL
# ======================================================================================

def buscar_lexico_fts(pregunta: str, depto_usuario: str, limite: int = 3) -> list[str]:
    """
    Búsqueda léxica en PostgreSQL mediante Full-Text Search (diccionario 'spanish').
    Usamos OR entre los términos de la consulta para recuperar documentos que coincidan
    con códigos de referencia exactos o términos técnicos específicos.
    """
    sql = """
        WITH query_or AS (
            SELECT to_tsquery(
                'spanish',
                replace(plainto_tsquery('spanish', %s)::text, ' & ', ' | ')
            ) AS q
        )
        SELECT f.codigo_doc
        FROM fragmentos_documento f, query_or
        WHERE f.departamento = %s
          AND query_or.q @@ to_tsvector('spanish', f.titulo || ' ' || f.contenido)
        ORDER BY ts_rank_cd(to_tsvector('spanish', f.titulo || ' ' || f.contenido), query_or.q) DESC
        LIMIT %s;
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (pregunta, depto_usuario, limite))
            return [f[0] for f in cur.fetchall()]


def buscar_semantico_puro(
    recuperador: RecuperadorRAG, pregunta: str, depto_usuario: str, limite: int = 3
) -> list[str]:
    vec = recuperador.generar_embedding(pregunta)
    sql = """
        SELECT codigo_doc
        FROM fragmentos_documento
        WHERE departamento = %s
        ORDER BY embedding <=> %s::vector ASC
        LIMIT %s;
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (depto_usuario, vec, limite))
            return [f[0] for f in cur.fetchall()]


def buscar_hibrido_rrf(
    recuperador: RecuperadorRAG,
    pregunta: str,
    depto_usuario: str,
    limite: int = 3,
    k_rrf: int = 60,
) -> list[tuple[str, float]]:
    """
    Búsqueda Híbrida en PostgreSQL combinando ranking semántico (pgvector) y
    ranking léxico (Full-Text Search) mediante Reciprocal Rank Fusion (RRF).
    Observa cómo el control de acceso (WHERE departamento = %s) se aplica en origen
    dentro de ambas subconsultas CTE antes de calcular los rankings.
    """
    vec = recuperador.generar_embedding(pregunta)

    sql_rrf = """
        WITH query_or AS (
            SELECT to_tsquery(
                'spanish',
                replace(plainto_tsquery('spanish', %s)::text, ' & ', ' | ')
            ) AS q
        ),
        ranking_semantico AS (
            SELECT codigo_doc,
                   ROW_NUMBER() OVER (ORDER BY embedding <=> %s::vector ASC) AS pos_sem
            FROM fragmentos_documento
            WHERE departamento = %s
            LIMIT 10
        ),
        ranking_lexico AS (
            SELECT f.codigo_doc,
                   ROW_NUMBER() OVER (
                       ORDER BY ts_rank_cd(
                           to_tsvector('spanish', f.titulo || ' ' || f.contenido),
                           query_or.q
                       ) DESC
                   ) AS pos_lex
            FROM fragmentos_documento f, query_or
            WHERE f.departamento = %s
              AND query_or.q @@ to_tsvector('spanish', f.titulo || ' ' || f.contenido)
            LIMIT 10
        )
        SELECT COALESCE(s.codigo_doc, l.codigo_doc) AS codigo_doc,
               (
                   COALESCE(1.0 / (%s + s.pos_sem), 0.0) +
                   COALESCE(1.0 / (%s + l.pos_lex), 0.0)
               ) AS rrf_score
        FROM ranking_semantico s
        FULL OUTER JOIN ranking_lexico l ON s.codigo_doc = l.codigo_doc
        ORDER BY rrf_score DESC
        LIMIT %s;
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql_rrf,
                (pregunta, vec, depto_usuario, depto_usuario, k_rrf, k_rrf, limite),
            )
            return [(f[0], float(f[1])) for f in cur.fetchall()]


CASOS_BENCHMARK = [
    {
        "nombre": "1. Coloquial sin palabras técnicas (Sinónimos)",
        "depto": "tecnico",
        "consulta": "¿Qué suelo pongo alrededor de la piscina para no resbalar?",
        "esperado": "DOC-TEC-01",
    },
    {
        "nombre": "2. Código de referencia alfanumérico exacto (SKU)",
        "depto": "tecnico",
        "consulta": "REV-205-INT",
        "esperado": "DOC-TEC-04",
    },
    {
        "nombre": "3. Código de norma técnica exacta",
        "depto": "tecnico",
        "consulta": "ensayo UNE-EN ISO 10545-12",
        "esperado": "DOC-TEC-02",
    },
    {
        "nombre": "4. Mixta: SKU exacto + consulta comercial de palé",
        "depto": "comercial",
        "consulta": "PAV-904-EXT descuento por palé",
        "esperado": "DOC-COM-01",
    },
]


def main() -> None:
    print("=== DEMO 1: CHUNKING CON SOLAPAMIENTO Y CABECERA CONTEXTUAL ===\n")
    ficha_ejemplo = (
        "El pavimento porcelánico espesorado de 20 mm está diseñado para climas extremos. "
        "Supera 150 ciclos de hielo-deshielo sin fisuración hasta -25 °C según norma ISO 10545-12. "
        "Su carga de rotura supera los 10.000 N permitiendo paso de vehículos ligeros."
    )
    chunks = fragmentar_con_solapamiento(
        texto=ficha_ejemplo,
        cabecera_contexto="Producto: Serie Pirineos | Ref: PAV-710-GEL",
        tamano_ventana=120,
        solapamiento=35,
    )
    for idx, ch in enumerate(chunks, start=1):
        print(f"  Chunk {idx}: {ch}")

    print("\n=== DEMO 2: COMPARATIVA LÉXICA vs SEMÁNTICA vs HÍBRIDA (RRF) ===\n")
    ingestar_corpus_json()
    recuperador = RecuperadorRAG()

    for caso in CASOS_BENCHMARK:
        res_lex = buscar_lexico_fts(caso["consulta"], caso["depto"], limite=3)
        res_sem = buscar_semantico_puro(recuperador, caso["consulta"], caso["depto"], limite=3)
        res_hib = [cod for cod, _ in buscar_hibrido_rrf(recuperador, caso["consulta"], caso["depto"], limite=3)]

        print(f"{caso['nombre']}")
        print(f"  Consulta: {caso['consulta']!r} (Esperado en #1: {caso['esperado']})")
        print(f"  -> Léxica Pura (FTS):     {res_lex}")
        print(f"  -> Semántica Pura (Vec):  {res_sem}")
        print(f"  -> Híbrida (RRF):         {res_hib}\n")


if __name__ == "__main__":
    main()
