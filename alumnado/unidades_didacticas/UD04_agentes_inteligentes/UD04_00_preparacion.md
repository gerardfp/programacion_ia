# UD04 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar la **Unidad Didáctica 4 (Agentes Inteligentes y Automatización)**, debes preparar las herramientas para la ejecución segura de funciones (*Tool Calling*) y la conexión con bases de datos relacionales.

---

## 🌐 Infraestructura de Servidor y Base de Datos

### 1. Base de Datos Relacional PostgreSQL 16
- **Servidor:** Instancia PostgreSQL disponible en la red del aula o localmente (ejemplo: `localhost:5432` o la IP indicada por el profesor).
- **Base de Datos de Pruebas:** `empresa_db`.
- **Credenciales del Alumno:**
  - **Usuario:** `alumno_lectura`
  - **Contraseña:** `password123`
  - **Permisos:** Exclusivamente de consulta (`SELECT`).

### 2. Servidor LLM Ollama
- Modelo `llama3.2:3b` preparado y respondiendo peticiones HTTP en el puerto `11434`.

---

## 🛠️ Requisitos de Software

### 1. Paquetes de Python para Agentes y BD
Añade las dependencias necesarias a tu proyecto `uv`:

```bash
uv add pydantic httpx sqlalchemy psycopg2-binary
```

### 2. Extensiones recomendadas en VS Code
- **Database Client** (`cweijan.vscode-database-client2`) o **SQLTools** (`mtxr.sqltools`) para conectarte a PostgreSQL y explorar las tablas de prueba (`productos`, `stock`, `pedidos`).

---

## 💻 Requisitos de Hardware

- **Memoria RAM:** Mínimo **8 GB de RAM**.
- **Conectividad:** Red local operativa para realizar peticiones concurrentes al servidor de inferencia y al servidor PostgreSQL.

---

## 🚀 Verificación del Entorno
Crea un archivo `test_agent_env.py` y ejecútalo con `uv run python test_agent_env.py`:

```python
from pydantic import BaseModel, Field

class HerramientaParametros(BaseModel):
    consulta: str = Field(..., description="Consulta SQL o término de búsqueda")

param = HerramientaParametros(consulta="SELECT * FROM stock")
print("Herramienta y esquema Pydantic configurados correctamente:", param.model_dump())
```
Si el esquema se valida correctamente, tu entorno está listo para iniciar la **UD04**.
