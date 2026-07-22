# UD06 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar la **Unidad Didáctica 6 (Proyecto Final Integrador)**, debes revisar que dispones del stack tecnológico completo instalado y funcionando en tu equipo de desarrollo.

---

## 🛠️ Requisitos de Software Integrados

Asegúrate de tener instaladas todas las herramientas y librerías trabajadas durante las unidades anteriores:

### 1. Herramientas de Base
- **Python 3.11+** y **`uv`**.
- **Docker** y **Docker Compose v2+**.
- **Git** para el control de versiones del proyecto.

### 2. Pila Tecnológica de Python (`uv.lock`)
Tu archivo `pyproject.toml` del proyecto final debe incorporar el conjunto de dependencias necesarias:

```bash
uv add fastapi "uvicorn[standard]" pydantic chromadb sentence-transformers sqlalchemy psycopg2-binary httpx streamlit pytest
```

---

## 💻 Requisitos de Hardware para Integración

- **Memoria RAM:** Mínimo **16 GB de RAM** (o 8 GB con descarga del servicio LLM Ollama al servidor del centro).
- **Almacenamiento:** Mínimo **15 GB de espacio libre en disco** para persistencia de la base de datos relacional, la base vectorial ChromaDB y las imágenes Docker.

---

## 🚀 Lista de Comprobación Previas a la Entrega

Antes de iniciar el desarrollo del producto mínimo viable (MVP), verifica que:
1. Tu servicio Ollama responde correctamente (`http://localhost:11434`).
2. Puedes construir imágenes de Docker sin errores de permisos (`docker build .`).
3. Dispones de la extensión **Marp for VS Code** lista para la preparación de tu diapositiva de defensa técnica (`UD06_02_presentacion.md`).
