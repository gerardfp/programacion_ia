# UD05 - Práctica Guiada: API REST de Inferencia con FastAPI y `uv`

## Enunciado
Construiremos una API REST en `main.py` capaz de recibir peticiones de inferencia y conectar con Ollama.

## Pasos Guiados
1. Inicializar el proyecto con `uv`:
   ```bash
   uv init --app ia-api
   uv add fastapi uvicorn pydantic httpx
   uv sync
   ```
2. Implementar los endpoints `/health` y `/api/v1/predict`.
3. Comprobar la API ejecutando `uv run uvicorn main:app --host 0.0.0.0 --port 8000`.
