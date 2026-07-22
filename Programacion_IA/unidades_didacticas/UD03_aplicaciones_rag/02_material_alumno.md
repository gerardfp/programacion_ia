# UD03 - Material Teórico para el Alumnado

## 1. ¿Qué es RAG (Retrieval-Augmented Generation)?

RAG combina la capacidad sintáctica de un LLM local con el conocimiento específico recuperado de una base de datos vectorial local.

```text
[ Documentos PDF / MD ]
       │
       ▼ (Chunking)
[ Fragmentos de texto ] ──► (SentenceTransformers) ──► [ Base Vectorial (ChromaDB) ]
                                                                 │
[ Pregunta Usuario ] ──────► (Consulta K-NN) ────────────────────┤
                                                                 ▼
[ Contexto Relevante ] ──► [ Prompt Armado ] ──► [ Ollama LLM ] ──► [ Respuesta ]
```

## 2. Fragmentación de Texto (Chunking)

La fragmentación divide documentos extensos en fragmentos más pequeños (ej. 500 caracteres) con solapamiento (*overlap* de 50 caracteres) para preservar la continuidad semántica.

## 3. Consultas Semánticas con ChromaDB

ChromaDB nos permite almacenar vectores y asociarles metadatos (como el archivo de origen y la página) para citar fuentes exactas.
