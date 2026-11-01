# resources/ud02/etapa7/experimento_hnsw.py
"""
Etapa 7: Demostración práctica de escalabilidad vectorial en PostgreSQL + pgvector.
Compara el plan de ejecución (EXPLAIN ANALYZE) y el tiempo de búsqueda entre:
  1. Búsqueda exacta sin índice vectorial (Sequential Scan: compara contra todas las filas).
  2. Búsqueda aproximada con índice HNSW (Hierarchical Navigable Small World).
"""

import random
import psycopg

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"
NUM_FILAS = 6000
DIM = 128  # Usamos dimensión 128 para generar e insertar el banco de pruebas en pocos segundos


def generar_vector_aleatorio(dim: int) -> list[float]:
    return [round(random.uniform(-1.0, 1.0), 5) for _ in range(dim)]


def ejecutar_explain(cur: psycopg.Cursor, vector_consulta: list[float]) -> list[str]:
    cur.execute(
        """
        EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
        SELECT id, codigo
        FROM benchmark_vectores
        ORDER BY embedding <=> %s::vector ASC
        LIMIT 5;
        """,
        (vector_consulta,),
    )
    return [fila[0] for fila in cur.fetchall()]


def main() -> None:
    random.seed(42)
    print(f"=== EXPERIMENTO ETAPA 7: BÚSQUEDA SECUENCIAL vs ÍNDICE HNSW ({NUM_FILAS} vectores) ===\n")

    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS benchmark_vectores;")
            cur.execute(
                f"""
                CREATE TABLE benchmark_vectores (
                    id SERIAL PRIMARY KEY,
                    codigo VARCHAR(30) NOT NULL,
                    embedding VECTOR({DIM}) NOT NULL
                );
                """
            )

            print(f"Insertando {NUM_FILAS} vectores de prueba en 'benchmark_vectores'...")
            datos = [
                (f"BENCH-{i:05d}", generar_vector_aleatorio(DIM))
                for i in range(NUM_FILAS)
            ]
            cur.executemany(
                "INSERT INTO benchmark_vectores (codigo, embedding) VALUES (%s, %s::vector);",
                datos,
            )
            cur.execute("ANALYZE benchmark_vectores;")
        conn.commit()

        vector_query = generar_vector_aleatorio(DIM)

        with conn.cursor() as cur:
            print("\n--- 1. SIN ÍNDICE VECTORIAL (Sequential Scan Exacto) ---")
            plan_sin_indice = ejecutar_explain(cur, vector_query)
            for linea in plan_sin_indice:
                print(f"  {linea}")

            print("\nCreando índice vectorial HNSW (vector_cosine_ops)...")
            cur.execute(
                """
                CREATE INDEX benchmark_vectores_hnsw_idx
                ON benchmark_vectores
                USING hnsw (embedding vector_cosine_ops);
                """
            )
            cur.execute("ANALYZE benchmark_vectores;")

            # Desactivamos enable_seqscan en la sesión de prueba para garantizar que el planificador
            # utilice el índice HNSW incluso con tablas medianas que caben en memoria caché.
            cur.execute("SET LOCAL enable_seqscan = off;")

            print("\n--- 2. CON ÍNDICE HNSW (Index Scan Aproximado) ---")
            plan_con_hnsw = ejecutar_explain(cur, vector_query)
            for linea in plan_con_hnsw:
                print(f"  {linea}")

            # Limpieza de la tabla temporal de benchmark
            cur.execute("DROP TABLE IF EXISTS benchmark_vectores;")
        conn.commit()


if __name__ == "__main__":
    main()
