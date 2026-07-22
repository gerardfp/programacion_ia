# UD03 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar la **Unidad Didáctica 3 (Aplicaciones RAG Locales)**, debes asegurarte de disponer del stack de librerías para procesamiento vectorial y el dataset sintético de muestra.

---

## 📁 Archivos y Datasets Requeridos

Asegúrate de que el dataset de prueba está disponible en tu repositorio local:
- Ruta: `alumnado/datasets/sample_dataset/sample.json`
- Contiene fragmentos sintéticos sobre configuración de servidores y redes para indexar en la base vectorial.

---

## 🛠️ Requisitos de Software

### 1. Librerías de Python para RAG y Embeddings
Instala en tu proyecto de `uv` las librerías necesarias para fragmentación, vectorización y almacenamiento persistente:

```bash
uv add chromadb sentence-transformers httpx pydantic pypdf
```

### 2. Modelo de Embeddings Local
- **Modelo por defecto:** `sentence-transformers/all-MiniLM-L6-v2`.
- **Descarga:** El modelo se descargará automáticamente en la caché local (`~/.cache/huggingface/`) en la primera ejecución de Python (~90 MB).

### 3. Servidor de Inferencia LLM
- Servidor Ollama disponible en `http://localhost:11434` con el modelo `llama3.2:3b` previamente preparado.

---

## 💻 Requisitos de Hardware y Almacenamiento

- **Memoria RAM:** Mínimo **8 GB de RAM** para cargar simultáneamente el modelo de embeddings en memoria y gestionar la base de datos vectorial ChromaDB.
- **Espacio en Disco:** Mínimo **2 GB de espacio libre** para:
  - Caché del modelo de embeddings (`all-MiniLM-L6-v2`).
  - Directorio persistente de vectores local `./chroma_db`.

---

## 🚀 Verificación del Entorno RAG
Crea un fichero corto `test_rag_env.py` y ejecútalo con `uv run python test_rag_env.py`:

```python
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Probar carga de modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
vector = model.encode("Prueba de vectorización RAG")

# 2. Probar base de datos ChromaDB local
client = chromadb.Client()
collection = client.create_collection("test_col")
collection.add(ids=["1"], embeddings=[vector.tolist()], documents=["Prueba de documento"])

print("Embeddings y ChromaDB funcionando correctamente. Dimensión del vector:", len(vector))
```
Si el script se ejecuta e imprime la dimensión 384, tu entorno está listo para la **UD03**.
