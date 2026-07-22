# UD03 - Guía Docente y Evaluación: Aplicaciones RAG Locales

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 25 horas  
**Resultado de Aprendizaje:** RA3 - Desarrolla aplicaciones RAG (Retrieval-Augmented Generation) locales.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Construir un motor de recuperación de información semántica sin enviar datos a internet.
- Comprender las fases del pipeline RAG: Ingesta -> Fragmentación (Chunking) -> Embeddings -> Almacenamiento Vectorial -> Recuperación k-NN -> Inferencia Contextualizada.
- Evaluar y prevenir alucinaciones mediante citación de fuentes originales y metadatos.

### Arquitectura Recomendada
- Gestor de Proyectos: `uv` con `pyproject.toml` y `uv.lock`.
- Modelos de Embedding: `sentence-transformers/all-MiniLM-L6-v2` o `bge-small-en-v1.5`.
- Base Vectorial: `ChromaDB` (almacenamiento persistente local en disco).
- LLM Inferencia: Ollama (`llama3.2:3b`).

### Secuencia de Sesiones (25 horas)
1. **Sesión 1-4 (4h):** Ingesta documental (PDF, Markdown, TXT) y fragmentación (chunking con solapamiento).
2. **Sesión 5-8 (4h):** Vectores y espacio embeddings. Generación de vectores densos locales.
3. **Sesión 9-12 (4h):** Bases de datos vectoriales: ChromaDB / PostgreSQL pgvector. Indexación y persistencia.
4. **Sesión 13-16 (4h):** Construcción del Pipeline RAG y armado dinámico de prompts contextualizados.
5. **Sesión 17-20 (4h):** Evaluación de respuestas: Fidelidad al contexto y mitigación de alucinaciones.
6. **Sesión 21-25 (5h):** Desarrollo y presentación de la aplicación RAG completa.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Pipeline RAG Funcional:** Código en Git con ingestión, almacenamiento vectorial en ChromaDB y generación contextualizada.
- **Fidelidad y Mitigación de Alucinaciones:** Instrucciones claras en el prompt para no responder sin datos en el contexto.
- **Citación de Fuentes:** Inclusión explícita de metadatos de los documentos de origen.

---

## 3. Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Pipeline RAG** | Ingesta, chunking, embeddings y ChromaDB integrados a la perfección. | Pipeline funcional con respuestas contextualmente correctas. | Ingesta parcial o fallos en la recuperación vectorial. | No recupera contexto ni conecta con la base vectorial. |
| **Citación y Alucinaciones** | Cita fuentes exactas y evita alucinaciones cuando no hay contexto. | Muestra las fuentes de información. | Alucina respuestas ignorando el contexto recuperado. | Sin control de alucinación ni fuentes. |
| **Persistencia** | Colección ChromaDB persistente en disco correctamente estructurada. | Persistencia funcional en disco. | Colección volátil exclusivamente en memoria. | Error en almacenamiento de vectores. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD03_aplicaciones_rag/`
