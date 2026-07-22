# Guía de Resolución de Problemas de Infraestructura (Troubleshooting)

## 1. El servicio Ollama no responde o da Connection Refused
- Verifique que el contenedor esté corriendo con `docker ps`.
- Revise los logs con `docker logs profesor_ollama`.
- Asegúrese de que ningún otro proceso local esté ocupando el puerto 11434 (`netstat -ano | findstr 11434` en Windows).

## 2. Errores de memoria GPU/RAM en inferencia
- Reduzca el tamaño de contexto o utilice una versión cuantizada más ligera del modelo (e.g. `llama3.2:1b` o `qwen2.5:1.5b`).
