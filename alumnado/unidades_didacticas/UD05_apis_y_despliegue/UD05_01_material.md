# UD05 - Material Teórico para el Alumnado

## 1. Publicación de APIs con FastAPI

FastAPI proporciona generación automática de documentación OpenAPI (`/docs`) e integración nativa con esquemas Pydantic.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/v1/predict")
def predict(data: PromptRequest):
    return {"respuesta": f"Procesado: {data.prompt}"}
```

## 2. Contenerización Eficiente con `uv` en Docker

Utilizar la imagen ligera de `uv` dentro de un Dockerfile permite construir imágenes rápidas y con caché optimizada:

```dockerfile
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
RUN uv pip install --system fastapi uvicorn pydantic httpx
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 3. Orquestación Multi-Servicio con Docker Compose

Docker Compose nos permite arrancar en una sola orden la API del proyecto y el servidor Ollama local comunicándolos mediante una red interna aislada.
