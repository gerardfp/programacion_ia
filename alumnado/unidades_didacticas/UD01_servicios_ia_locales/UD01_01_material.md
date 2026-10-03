# UD01 - Material Teórico para el Alumnado

## 1. Arquitectura de Inferencia Local

Un servidor de inferencia como Ollama expone una API HTTP REST que permite interactuar con Grandes Modelos de Lenguaje (LLMs) ejecutados localmente en CPU o GPU:

```text
+-------------------+      HTTP POST /api/generate      +-------------------+
|  Cliente Python   | --------------------------------> |  Servidor Ollama  |
|   (uv + httpx)    | <-------------------------------- | (llama3.2 / Qwen) |
+-------------------+       JSON Response / Stream      +-------------------+
```

## 2. Peticiones HTTP y Salida JSON Estructurada

### ⚠️ El Fallo del Método Ingenuo (Crash & Learn)
Si le pedimos al modelo *"Devuélveme un JSON con los datos"* sin forzar el modo JSON en la API, el LLM incluirá preámbulos conversacionales o bloques markdown:
```text
¡Hola! Con mucho gusto, aquí tienes los datos solicitados:
```json
{"nombre": "Juan"}
```
Espero haberte ayudado.
```
Al intentar parsear esto con `json.loads(respuesta.text)` en Python, el programa lanzará inmediatamente un error catastrófico: **`json.decoder.JSONDecodeError`**.

### ✅ La Solución Profesional
Activamos el modo JSON nativo (`"format": "json"`) y validamos la salida con un esquema estricto de **Pydantic V2**:

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
