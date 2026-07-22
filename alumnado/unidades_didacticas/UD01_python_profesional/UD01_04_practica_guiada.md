# UD01 - Práctica Guiada: Estructuración del paquete `ia_utils`

## Enunciado
En esta práctica guiada configuraremos el entorno virtual de trabajo y crearemos la estructura oficial del paquete `ia_utils`.

## Pasos Guiados
1. Crear el entorno virtual y sincronizar el proyecto con `uv`:
   ```bash
   uv venv
   uv sync
   ```
2. Generar o actualizar el archivo de bloqueo reproducible `uv.lock`:
   ```bash
   uv lock
   ```
3. Ejecutar las pruebas o herramientas de desarrollo directamente a través de `uv`:
   ```bash
   uv run pytest
   ```
4. Completar la implementación de `InferenciaInput` en `src/ia_utils/validator.py`.
