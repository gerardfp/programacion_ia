---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD05: APIs y Despliegue'
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

# UD05: APIs, Contenedores y Operación
## Publicación de Servicios de IA con FastAPI y Docker Compose

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** Contenerización Profesional y Despliegue en Servidores del Centro

---

## 1. De Prototipo a Servicio Backend

- Los modelos y aplicaciones de IA deben ser expuestos como **APIs REST de alto rendimiento**.
- **FastAPI:**
  - Asincronía nativa (`async/await`).
  - Validación automática de tipos con Pydantic.
  - Documentación interactiva autogenerada en Swagger UI (`/docs`).

---

## 2. Definición de Endpoints en FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Servicio Inferencia IA")

class Consulta(BaseModel):
    prompt: str

@app.post("/v1/predict")
async def predecir(consulta: Consulta):
    if not consulta.prompt:
        raise HTTPException(status_code=400, detail="Prompt vacío")
    return {"resultado": f"Respuesta generada para: {consulta.prompt}"}
```

---

## 3. Contenerización Profesional con Docker y `uv`

- **Imagen Docker optimizada:**
  ```dockerfile
  FROM python:3.11-slim
  COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
  WORKDIR /app
  COPY pyproject.toml uv.lock ./
  RUN uv sync --frozen
  COPY src/ ./src/
  CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

---

## 4. Orquestación Multi-servicio con Docker Compose

```yaml
version: '3.8'
services:
  api_ia:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OLLAMA_HOST=http://ollama:11434
    depends_on:
      - ollama

  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_storage:/root/.ollama

volumes:
  ollama_storage:
```

---

## 5. Buenas Prácticas Operativas y Monitorización

- **Healthchecks:** Endpoint `/health` para comprobar el estado de Ollama y la base de datos.
- **Variables de Entorno (`.env`):** Separar credenciales y puertos del código fuente.
- **Monitorización de Logs:** Inspección centralizada mediante `docker compose logs -f`.
