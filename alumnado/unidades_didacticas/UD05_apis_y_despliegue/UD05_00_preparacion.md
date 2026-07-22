# UD05 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar la **Unidad Didáctica 5 (APIs, Contenedores y Operación)**, debes asegurarte de disponer del motor de contenedores Docker y Docker Compose instalados y configurados en tu sistema.

---

## 🛠️ Requisitos de Software

### 1. Docker y Docker Compose
- **Windows / macOS:** Instalar **Docker Desktop** (asegurándote de activar el motor WSL2 en Windows).
- **Linux (Ubuntu/Debian):** Instalar Docker Engine y Docker Compose v2+:
  ```bash
  sudo apt update && sudo apt install -y docker.io docker-compose-v2
  ```
- **Configuración de Permisos (Linux):** Añade tu usuario al grupo `docker` para ejecutar comandos sin `sudo`:
  ```bash
  sudo usermod -aG docker $USER
  ```
- **Verificación en consola:**
  ```bash
  docker --version
  docker compose version
  ```

### 2. Entorno Python y Web Framework
Añade las dependencias para la creación de servidores API REST con FastAPI:

```bash
uv add fastapi "uvicorn[standard]" pydantic httpx
```

### 3. Extensiones recomendadas en VS Code
- **Docker** (`ms-azuretools.vscode-docker`) - Para visualizar contenedores en ejecución, inspeccionar logs y gestionar imágenes.

---

## 💻 Requisitos de Hardware

- **Memoria RAM:** Mínimo **8 GB de RAM** (se recomiendan **16 GB** para ejecutar simultáneamente el contenedor de FastAPI, el contenedor de Ollama y la base de datos PostgreSQL en Docker Compose).
- **Almacenamiento:** Mínimo **10 GB de espacio libre en disco** para descargar imágenes Docker base (`python:3.11-slim`, `ollama/ollama`, `postgres:16`).

---

## 🚀 Verificación del Entorno Docker
Ejecuta el siguiente comando para probar la creación y ejecución de un contenedor de prueba:

```bash
docker run --rm hello-world
```
Si ves el mensaje *"Hello from Docker!"*, tu entorno de contenerización está listo para iniciar la **UD05**.
