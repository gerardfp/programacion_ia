# UD04 - Práctica Guiada: Agente con Registro de Herramientas con `uv`

## Enunciado
Desarrollaremos la clase `AgenteInteligenteSolucion` capaz de registrar funciones Python y ejecutarlas de forma segura.

## Pasos Guiados
1. Inicializar proyecto con `uv`:
   ```bash
   uv init --lib agent-core
   uv add pydantic
   uv sync
   ```
2. Completar el archivo `agent.py` registrando la herramienta `consultar_stock`.
3. Ejecutar y verificar la auditoría con `uv run python agent.py`.
