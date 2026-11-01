# resources/ud02/etapa1/experimento_02_busqueda_sql.py
"""
Etapa 1 - Parte 2: La Brecha Léxica en la búsqueda tradicional por palabras (SQL ILIKE).
Comprueba por qué buscar coincidencias literales de palabras en PostgreSQL falla
cuando el usuario utiliza lenguaje cotidiano y las fichas usan terminología técnica.
"""

import psycopg

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"


def buscar_por_palabras_sql(palabras_clave: list[str]) -> list[tuple]:
    """Busca fragmentos que contengan cualquiera de las palabras clave usando ILIKE."""
    condiciones = " OR ".join(["contenido ILIKE %s" for _ in palabras_clave])
    parametros = [f"%{palabra}%" for palabra in palabras_clave]

    sql = f"""
        SELECT codigo_doc, titulo, contenido
        FROM fragmentos_documento
        WHERE {condiciones};
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            return cur.fetchall()


print("=== EXPERIMENTO 02: BÚSQUEDA LÉXICA CLÁSICA EN POSTGRESQL (ILIKE) ===\n")

# Caso 1: El usuario conoce la jerga técnica exacta del catálogo ("antideslizante", "C3")
print("--- Caso 1: Búsqueda con términos técnicos exactos ['antideslizante', 'Clase C3'] ---")
resultados_1 = buscar_por_palabras_sql(["antideslizante", "Clase C3"])
print(f"Fragmentos encontrados: {len(resultados_1)}")
for cod, titulo, _ in resultados_1:
    print(f"  -> [{cod}] {titulo}")

# Caso 2: El cliente pregunta con sus propias palabras:
# "¿Qué suelo pongo en el bordillo de una piscina para no resbalar?"
print(
    "\n--- Caso 2: Pregunta cotidiana del cliente: "
    "'¿Qué suelo pongo en el bordillo de una piscina para no resbalar?' ---"
)
palabras_cliente = ["piscina", "bordillo", "resbalar"]
print(f"Buscando en SQL con ILIKE las palabras: {palabras_cliente}")
resultados_2 = buscar_por_palabras_sql(palabras_cliente)
print(f"Fragmentos encontrados: {len(resultados_2)}")

if not resultados_2:
    print(
        "\n¡0 RESULTADOS!\n"
        "A pesar de que el fragmento DOC-TEC-01 (Serie Marina) está diseñado exactamente para eso,\n"
        "la ficha técnica dice 'playas de coronación de vasos acuáticos' y 'acabado antideslizante Clase C3',\n"
        "sin mencionar jamás las palabras 'piscina', 'bordillo' ni 'resbalar'.\n"
        "Esto se conoce como BRECHA LÉXICA: mismo significado, distintas palabras."
    )
