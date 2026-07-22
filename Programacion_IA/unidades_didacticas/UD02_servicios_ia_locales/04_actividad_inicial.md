# UD02 - Actividad Inicial: Exploración de Endpoints HTTP en Ollama

## Objetivos
Probar manualmente los endpoints del servidor local de Ollama utilizando herramientas de línea de comandos (`curl` o cURL en PowerShell).

## Tareas
1. Verificar que el servidor responde en el puerto 11434:
   ```bash
   curl http://localhost:11434/api/tags
   ```
2. Realizar una petición de inferencia básica:
   ```bash
   curl -X POST http://localhost:11434/api/generate -d "{\"model\": \"llama3.2:3b\", \"prompt\": \"Hola\", \"stream\": false}"
   ```
