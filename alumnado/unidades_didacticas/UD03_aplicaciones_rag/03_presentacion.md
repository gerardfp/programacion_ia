---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD03: Aplicaciones RAG Locales'
footer: 'Curso 2026-2027 | Módulo 5073'
style: |
  section {
    background-color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #1e3a8a;
  }
  h2 {
    color: #2563eb;
  }
  code {
    background-color: #e2e8f0;
    color: #0f172a;
  }
---

# UD03: Aplicaciones RAG Locales
## Retrieval-Augmented Generation con Embeddings y Bases Vectoriales

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** Asistentes Documentales Privados sin Alucinaciones

---

## 1. El Problema de las Alucinaciones y Ventana de Contexto

- **Limitaciones de los LLM puros:**
  - Desconocen datos privados o internos de la organización.
  - Alucinan respuestas cuando no disponen de información exacta.
  - Ventana de contexto limitada y costosa de llenar con documentos completos.
- **Solución RAG:** Recuperar fragmentos relevantes de datos propios y proporcionarlos en el prompt al modelo.

---

## 2. Arquitectura de un Sistema RAG

```text
Documentos → Ingesta / Chunking → Embeddings → Base Vectorial (ChromaDB)
                                                        ↓
Pregunta del usuario → Generar Embedding → Búsqueda Semántica → Top K Chunks
                                                        ↓
Prompt Aumentado (Pregunta + Contexto) → LLM Local (Ollama) → Respuesta con Fuentes
```

---

## 3. Embeddings Locales y Bases Vectoriales

- **Embeddings:** Vectores numéricos que capturan el significado semántico del texto.
- **Modelos de embeddings locales:** `sentence-transformers/all-MiniLM-L6-v2`.
- **Bases de Datos Vectoriales Locales:**
  - **ChromaDB:** Base de datos vectorial embebida y liviana para Python.
  - **pgvector:** Extensión de PostgreSQL para búsqueda por similitud de cosenos.

---

## 4. Implementación del Motor RAG en Python

```python
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Crear cliente vectorial y modelo
client = chromadb.Client()
collection = client.get_or_create_collection("documentos_centro")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Ingestar documento
vector = model.encode("El horario de laboratorio es de 8:00 a 14:00.").tolist()
collection.add(ids=["doc1"], embeddings=[vector], documents=["Horario laboratorio..."])
```

---

## 5. Evaluación de Fidelidad y Citación de Fuentes

- **Auditoría de respuestas:** Exigir que la respuesta incluya los metadatos de los documentos consultados (pág., ID, título).
- **Control de acceso:** Filtrar la búsqueda semántica por metadatos autorizados (ej. `categoria = 'publico'`).
- **Validación anti-alucinación:** Verificar que la respuesta se fundamente estrictamente en el contexto recuperado.
