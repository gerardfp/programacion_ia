# resources/ud02/etapa1/experimento_04_pgvector.py
"""
Etapa 1 - Parte 4: Almacenamiento y búsqueda semántica en PostgreSQL con pgvector.
1. Calcula y guarda los embeddings (VECTOR(1024)) de los 12 fragmentos en PostgreSQL.
2. Ejecuta una consulta semántica con el operador de distancia coseno (<=>) directamente en SQL.
"""

import httpx
import psycopg

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "bge-m3"


def generar_embedding(texto: str) -> list[float]:
    res = httpx.post(
        OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "input": texto},
        timeout=30.0,
    )
    res.raise_for_status()
    return res.json()["embeddings"][0]


def indexar_fragmentos_pendientes() -> None:
    """Genera y almacena el vector embedding para las filas que aún tengan embedding IS NULL."""
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, codigo_doc, contenido FROM fragmentos_documento WHERE embedding IS NULL;")
            pendientes = cur.fetchall()

            if not pendientes:
                print("Todos los fragmentos en PostgreSQL ya tienen su vector embedding indexado.\n")
                return

            print(f"Generando embeddings con '{EMBED_MODEL}' para {len(pendientes)} fragmentos...")
            for fila_id, codigo_doc, contenido in pendientes:
                vector = generar_embedding(contenido)
                cur.execute(
                    "UPDATE fragmentos_documento SET embedding = %s::vector WHERE id = %s;",
                    (vector, fila_id),
                )
                print(f"  [OK] Indexado {codigo_doc} ({len(vector)} dimensiones)")
        conn.commit()
    print("Indexación completada.\n")


def buscar_con_pgvector(pregunta: str, limite: int = 3) -> list[tuple]:
    vector_pregunta = generar_embedding(pregunta)

    # El operador <=> de pgvector calcula la distancia coseno directamente en PostgreSQL
    sql = """
        SELECT codigo_doc, departamento, titulo,
               (embedding <=> %s::vector) AS distancia
        FROM fragmentos_documento
        ORDER BY distancia ASC
        LIMIT %s;
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (vector_pregunta, limite))
            return cur.fetchall()


if __name__ == "__main__":
    print("=== EXPERIMENTO 04: BÚSQUEDA VECTORIAL EN POSTGRESQL CON PGVECTOR ===\n")
    indexar_fragmentos_pendientes()

    pregunta = "¿Qué suelo pongo en el bordillo de una piscina para no resbalar?"
    print(f"Pregunta del cliente: {pregunta!r}\n")
    print("Top 3 fragmentos más cercanos según pgvector (embedding <=> vector_pregunta):")
    for cod, depto, titulo, dist in buscar_con_pgvector(pregunta, limite=3):
        print(f"  -> [{cod}] (depto: {depto:<9} | distancia: {dist:.4f}) {titulo}")
