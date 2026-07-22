# UD02 - Material Teórico para el Alumnado

## 1. Arquitectura de Inferencia Local

Un servidor de inferencia como Ollama expone una API HTTP REST que permite interactuar con Grandes Modelos de Lenguaje (LLMs) ejecutados localmente en CPU o GPU:

```text
+-------------------+      HTTP POST /api/generate      +-------------------+
|  Cliente Python   | --------------------------------> |  Servidor Ollama  |
|   (uv + httpx)    | <-------------------------------- | (llama3.2 / Qwen) |
+-------------------+       JSON Response / Stream      +-------------------+
```

## 2. Peticiones HTTP y Salida JSON Estructurada

Para integraciones fiables en sistemas de información, debemos solicitar respuestas en formato JSON estricto:

```json
{
  "model": "llama3.2:3b",
  "prompt": "Extrae el nombre y email del texto: 'Contacto: Juan Perez (juan@example.com)'",
  "format": "json",
  "stream": false
}
```

## 3. Métricas de Rendimiento en Inferencia
- **Total Duration:** Tiempo total transcurrido desde la petición hasta el fin de generación.
- **Load Duration:** Tiempo empleado en cargar el modelo en memoria VRAM/RAM.
- **Eval Count & Duration:** Número de tokens generados y velocidad en tokens/segundo.
