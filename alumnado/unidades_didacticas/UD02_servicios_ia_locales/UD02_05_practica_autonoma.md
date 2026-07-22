# UD02 - Práctica Autónoma: Generador de JSON Estructurado y Benchmark

## Enunciado
El alumnado ampliará la clase `OllamaClient` para crear una función `extraer_entidades(texto: str) -> dict` que fuerce la salida en formato JSON con la siguiente estructura:
- `personas`: Lista de nombres detectados.
- `organizaciones`: Lista de empresas o instituciones.
- `resumen`: Resumen breve de una frase.

Además, implementará un benchmark simple que registre el tiempo medio de respuesta y los tokens por segundo (`eval_count / eval_duration`).
