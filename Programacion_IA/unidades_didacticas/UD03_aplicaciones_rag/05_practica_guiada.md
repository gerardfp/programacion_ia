# UD03 - Práctica Guiada: Motor RAG con ChromaDB y `uv`

## Enunciado
Crearemos un motor RAG modular capaz de indexar documentos y responder preguntas sobre ellos.

## Pasos Guiados
1. Inicializar proyecto con `uv`:
   ```bash
   uv init --lib rag-engine
   uv add chromadb sentence-transformers httpx
   uv sync
   ```
2. Completar la implementación de `RAGEngineSolucion` en `rag_engine.py`.
3. Ejecutar las pruebas con `uv run python rag_engine.py`.
