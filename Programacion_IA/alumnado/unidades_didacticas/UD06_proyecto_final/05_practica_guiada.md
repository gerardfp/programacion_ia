# UD06 - Práctica Guiada: Estructura Estándar del Proyecto con `uv`

## Enunciado
Inicializaremos el repositorio git del proyecto final con la estructura limpia exigida en los criterios de evaluación.

## Pasos Guiados
1. Crear el proyecto con `uv`:
   ```bash
   uv init --app proyecto-final-ia
   uv add fastapi uvicorn pydantic httpx chromadb
   uv add --dev pytest
   uv lock
   ```
2. Crear la estructura de carpetas: `src/`, `tests/`, `docs/`, `docker/`.
