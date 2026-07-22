# UD02 - Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Consumo de API HTTP** | Cliente robusto con gestión de timeouts, errores de conexión y reintentos. | Cliente funcional conectando correctamente con Ollama. | Peticiones HTTP básicas con errores ocasionales. | No consigue conectar con la API de Ollama. |
| **Salida JSON Estructurada** | Esquema JSON perfecto, parseado automáticamente con Pydantic. | Salida JSON válida en la mayoría de peticiones. | Respuestas de texto plano sin estructurar. | JSON malformado o ininterpretable. |
| **Métricas de Latencia** | Mide TTFT, latencia total y tokens/segundo con logs estructurados. | Registra la latencia global en segundos. | Medición imprecisa o incompleta. | Sin medición de rendimiento. |
