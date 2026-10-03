# UD02 - Material Teórico para el Alumnado

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

## 4. ⚠️ El Fallo del RAG Ingenuo (*Naive RAG*)

El enfoque básico de tutorial divide texto ciegamente y busca solo por similitud de cosenos. **¿Por qué falla en la empresa real?**
1. **Pérdida de códigos y SKUs exactos:** Si el usuario pregunta por el número de pieza `REF-9921-X`, el modelo de embeddings busca el significado semántico general de "pieza", recupera fragmentos irrelevantes y el LLM **alucina inventando especificaciones**.
2. **Tablas rotas:** Si un chunk corta una tabla a la mitad, los números pierden su encabezado de columna y la respuesta es incorrecta.

## 5. ✅ La Solución de Vanguardia: Búsqueda Híbrida y Re-ranking

1. **Búsqueda Híbrida (Hybrid Search):** Combinamos búsqueda vectorial densa con búsqueda léxica de palabras clave (**BM25**). La consulta exacta por código ahora siempre recupera el fragmento correcto.
2. **Re-ranking con Cross-Encoder:** Un modelo clasificador local (`bge-reranker`) reordena los candidatos recuperados y sitúa en primer lugar el fragmento con mayor probabilidad real de responder la pregunta.
