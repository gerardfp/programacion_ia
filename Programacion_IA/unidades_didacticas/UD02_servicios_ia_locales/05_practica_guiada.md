# UD02 - Práctica Guiada: Cliente Python para Ollama con `uv`

## Enunciado
Construiremos una clase `OllamaClient` profesional utilizando `uv` para gestionar el entorno y las dependencias.

## Pasos Guiados
1. Inicializar el entorno con `uv`:
   ```bash
   uv init --lib ollama-client
   uv add httpx pydantic
   uv sync
   ```
2. Implementar la clase `OllamaClient` en `ollama_client.py` permitiendo configurar `base_url`, `model` y soporte para `format="json"`.
3. Probar el cliente ejecutándolo con `uv run python ollama_client.py`.
