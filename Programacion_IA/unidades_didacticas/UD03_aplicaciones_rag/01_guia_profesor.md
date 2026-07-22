# UD03 - Guía para el Profesorado

## Objetivos Didácticos
- Construir un motor de recuperación de información semántica sin enviar datos a internet.
- Comprender las fases del pipeline RAG: Ingesta -> Fragmentación (Chunking) -> Embeddings -> Almacenamiento Vectorial -> Recuperación k-NN -> Inferencia Contextualizada.
- Evaluar y prevenir alucinaciones mediante citación de fuentes originales y metadatos.

## Arquitectura Recomendada
- Gestor de Proyectos: `uv` con `pyproject.toml` y `uv.lock`.
- Modelos de Embedding: `sentence-transformers/all-MiniLM-L6-v2` o `bge-small-en-v1.5`.
- Base Vectorial: `ChromaDB` (almacenamiento persistente local en disco).
- LLM Inferencia: Ollama (`llama3.2:3b`).

## Secuencia de Sesiones (25 horas)
1. **Sesión 1-4 (4h):** Ingesta documental (PDF, Markdown, TXT) y fragmentación (chunking con solapamiento).
2. **Sesión 5-8 (4h):** Vectores y espacio embeddings. Generación de vectores densos locales.
3. **Sesión 9-12 (4h):** Bases de datos vectoriales: ChromaDB / PostgreSQL pgvector. Indexación y persistencia.
4. **Sesión 13-16 (4h):** Construcción del Pipeline RAG y armado dinámico de prompts contextualizados.
5. **Sesión 17-20 (4h):** Evaluación de respuestas: Fidelidad al contexto y mitigación de alucinaciones.
6. **Sesión 21-25 (5h):** Desarrollo y presentación de la aplicación RAG completa.
