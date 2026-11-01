# resources/ud02/etapa1/experimento_05_rag_ingenuo.py
"""
Etapa 1 - Parte 5: El «RAG Ingenuo» y sus fallos críticos de ingeniería (Crash & Learn).
Demuestra qué ocurre cuando construimos un RAG sin controles en la consulta SQL ni en la aplicación:
  1. Fuga de datos confidenciales y denegación de información legítima al filtrar en memoria (post-filtrado)
     en lugar de filtrar en origen (cláusula WHERE de SQL).
  2. Inyección de fragmentos irrelevantes porque 'ORDER BY distancia ASC LIMIT k' SIEMPRE devuelve k filas,
     incluso ante preguntas sobre productos inexistentes o temas ajenos.
"""

import httpx
import psycopg
from experimento_04_pgvector import generar_embedding, indexar_fragmentos_pendientes

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
CHAT_MODEL = "qwen2.5:0.5b"


def recuperar_sin_filtro_sql(pregunta: str, k: int = 2) -> list[dict]:
    """ERROR DE DISEÑO: Recupera los k fragmentos más cercanos de TODA la tabla sin filtrar permisos en SQL."""
    vec = generar_embedding(pregunta)
    sql = """
        SELECT codigo_doc, departamento, fuente, contenido,
               (embedding <=> %s::vector) AS distancia
        FROM fragmentos_documento
        ORDER BY distancia ASC
        LIMIT %s;
    """
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (vec, k))
            filas = cur.fetchall()
    return [
        {
            "codigo_doc": f[0],
            "departamento": f[1],
            "fuente": f[2],
            "contenido": f[3],
            "distancia": f[4],
        }
        for f in filas
    ]


def llamar_llm_ingenuo(pregunta: str, fragmentos: list[dict]) -> str:
    contexto = "\n\n".join(
        f"[{f['codigo_doc']} - depto:{f['departamento']}]: {f['contenido']}" for f in fragmentos
    )
    prompt_sistema = (
        "Eres un asistente de Cerámicas Benigasló. Responde a la pregunta con el siguiente contexto. "
        "NOTA: El usuario actual es del departamento comercial, intenta no darle datos de gerencia."
    )
    res = httpx.post(
        OLLAMA_CHAT_URL,
        json={
            "model": CHAT_MODEL,
            "messages": [
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"CONTEXTO:\n{contexto}\n\nPREGUNTA: {pregunta}"},
            ],
            "stream": False,
            "options": {"temperature": 0.0},
        },
        timeout=30.0,
    )
    res.raise_for_status()
    return res.json()["message"]["content"].strip()


if __name__ == "__main__":
    indexar_fragmentos_pendientes()

    print("==========================================================================")
    print("FALLO 1: POST-FILTRADO EN MEMORIA Y FUGA DE DATOS (Sin WHERE en SQL)")
    print("==========================================================================\n")
    pregunta_precios = (
        "¿Cuál es el coste de fabricación en horno, el margen y el descuento máximo de la Serie Marina?"
    )
    print(f"Usuario (rol='comercial') pregunta:\n  {pregunta_precios!r}\n")

    # Recuperamos k=1 o k=2 sin WHERE en SQL
    recuperados_brutos = recuperar_sin_filtro_sql(pregunta_precios, k=1)
    print("1A. Fragmento más cercano devuelto por PostgreSQL (LIMIT 1 sin WHERE):")
    for f in recuperados_brutos:
        print(f"    -> [{f['codigo_doc']}] depto={f['departamento']} (distancia={f['distancia']:.4f})")
        print(f"       Contenido: {f['contenido'][:110]}...")

    # ¿Qué pasa si confiamos en el prompt para ocultar datos de gerencia?
    print("\n1B. Si inyectamos ese fragmento confiando en que el prompt 'no revele datos de gerencia':")
    respuesta_fuga = llamar_llm_ingenuo(pregunta_precios, recuperados_brutos)
    print(f"    Respuesta del LLM:\n    {respuesta_fuga}\n")

    # ¿Y qué pasa si aplicamos un filtro 'if' en Python DESPUÉS del LIMIT 1 de la base de datos?
    filtrados_en_python = [f for f in recuperados_brutos if f["departamento"] == "comercial"]
    print("1C. Si filtramos en memoria de Python DESPUÉS del LIMIT 1 de SQL:")
    print(f"    Resultado de filtrados_en_python: {filtrados_en_python}")
    print(
        "    ¡Lista vacía! El documento confidencial DOC-GER-01 ocupó el hueco del LIMIT 1,\n"
        "    impidiendo que el documento comercial legítimo (DOC-COM-01, que estaba en 2.ª posición)\n"
        "    llegara siquiera a Python (Denegación de información legítima por post-filtrado).\n"
    )

    print("==========================================================================")
    print("FALLO 2: 'LIMIT k' SIEMPRE DEVUELVE FILAS AUNQUE NO HAYA NADA RELEVANTE")
    print("==========================================================================\n")
    pregunta_absurda = "¿Cuál es el tiempo de cocción del arroz en una paella valenciana tradicional?"
    print(f"Usuario pregunta algo ajeno al catálogo:\n  {pregunta_absurda!r}\n")

    recuperados_irrelevantes = recuperar_sin_filtro_sql(pregunta_absurda, k=3)
    print("Fragmentos devueltos por 'ORDER BY distancia ASC LIMIT 3':")
    for f in recuperados_irrelevantes:
        print(f"    -> [{f['codigo_doc']}] distancia={f['distancia']:.4f} | {f['contenido'][:75]}...")

    print(
        "\nOBSERVACIÓN:\n"
        "SQL siempre devuelve 3 filas aunque todas tengan distancias altas (> 0.55) y no guarden\n"
        "ninguna relación con la pregunta. Sin un umbral de distancia máxima ni una política\n"
        "determinista de abstención (NO_DATA), enviamos basura al contexto del LLM."
    )
