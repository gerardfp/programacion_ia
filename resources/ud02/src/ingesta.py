# resources/ud02/src/ingesta.py
"""
Pipeline de fragmentación (chunking) e ingesta vectorial en PostgreSQL + pgvector.
Lee el corpus documental desde 'datos/corpus_ceramica.json', genera el vector embedding
de cada fragmento con el modelo 'bge-m3' en Ollama y lo almacena en 'fragmentos_documento'.
"""

import json
from pathlib import Path
import httpx
import psycopg

DB_URL = "postgresql://postgres:postgres@localhost:5432/ceramica_rag"
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"
RUTA_CORPUS = Path(__file__).resolve().parent.parent / "datos" / "corpus_ceramica.json"


def dividir_documento_por_parrafos(texto_largo: str, max_caracteres: int = 500) -> list[str]:
    """
    Función didáctica de fragmentación (chunking): divide un documento extenso en fragmentos
    respetando los saltos de párrafo siempre que no superen 'max_caracteres'.
    """
    parrafos = [p.strip() for p in texto_largo.split("\n\n") if p.strip()]
    fragmentos: list[str] = []
    acumulado = ""

    for parrafo in parrafos:
        candidato = f"{acumulado}\n\n{parrafo}".strip() if acumulado else parrafo
        if len(candidato) <= max_caracteres:
            acumulado = candidato
        else:
            if acumulado:
                fragmentos.append(acumulado)
            acumulado = parrafo

    if acumulado:
        fragmentos.append(acumulado)
    return fragmentos


def generar_embedding(texto: str, ollama_url: str = OLLAMA_URL, model: str = EMBED_MODEL) -> list[float]:
    """Solicita a Ollama el vector de embeddings para un texto dado."""
    try:
        response = httpx.post(
            f"{ollama_url}/api/embed",
            json={"model": model, "input": texto},
            timeout=30.0,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise ConnectionError(f"Error al generar embedding con Ollama ({model}): {e}") from e

    return response.json()["embeddings"][0]


def ingestar_corpus_json(
    db_url: str = DB_URL,
    ruta_json: Path = RUTA_CORPUS,
    ollama_url: str = OLLAMA_URL,
) -> int:
    """
    Lee los fragmentos del archivo JSON, calcula su embedding con 'bge-m3'
    y hace un UPSERT en la tabla 'fragmentos_documento'.
    """
    documentos = json.loads(ruta_json.read_text(encoding="utf-8"))

    sql_upsert = """
        INSERT INTO fragmentos_documento (codigo_doc, titulo, fuente, departamento, contenido, embedding)
        VALUES (%s, %s, %s, %s, %s, %s::vector)
        ON CONFLICT (codigo_doc) DO UPDATE SET
            titulo = EXCLUDED.titulo,
            fuente = EXCLUDED.fuente,
            departamento = EXCLUDED.departamento,
            contenido = EXCLUDED.contenido,
            embedding = EXCLUDED.embedding;
    """

    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            for doc in documentos:
                # Incluimos título y contenido para enriquecer el contexto semántico del vector
                texto_a_vectorizar = f"{doc['titulo']}. {doc['contenido']}"
                vector = generar_embedding(texto_a_vectorizar, ollama_url=ollama_url)
                cur.execute(
                    sql_upsert,
                    (
                        doc["codigo_doc"],
                        doc["titulo"],
                        doc["fuente"],
                        doc["departamento"],
                        doc["contenido"],
                        vector,
                    ),
                )
        conn.commit()

    return len(documentos)


if __name__ == "__main__":
    print(f"Iniciando ingesta desde {RUTA_CORPUS.name} con modelo '{EMBED_MODEL}'...")
    total = ingestar_corpus_json()
    print(f"Ingesta finalizada con éxito: {total} fragmentos vectorizados en PostgreSQL.")
