# UD04 - Material Teórico para el Alumnado

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

## 4. ⚠️ La Ceguera Operativa: Depurar con `print()` en Producción (Crash & Learn)

Cuando la aplicación corre en varios contenedores Docker recibiendo peticiones de usuarios concurrentes:
- Los mensajes `print()` aparecen desordenados e indistinguibles en la consola de Docker (`docker compose logs`).
- Si una petición tarda 12 segundos o da error 500, **no sabemos en qué punto falló**: ¿fue la carga de Ollama en VRAM, la consulta SQL a Postgres o la vectorización en ChromaDB?
- No hay forma de medir cuántos tokens se consumieron ni cuál es la latencia por etapa.

## 5. ✅ La Solución Profesional: Observabilidad Local con Langfuse

Añadimos **Langfuse** (plataforma open-source de telemetría de IA) al archivo `compose.yaml`:
- **Trazas Visuales (Traces):** Cada petición genera un árbol jerárquico que muestra exactamente cuánto tiempo tardó cada llamada a Ollama o a las herramientas.
- **Métricas Reales:** Tiempo hasta el primer token (TTFT), velocidad en tokens/segundo y registro del prompt exacto recibido por el modelo.
- **Panel Web Local:** Los alumnos abren `http://localhost:3000` y diagnostican cuellos de botella con la misma herramienta que emplean los equipos profesionales de ingeniería de IA.
