# UD02 - Guía para el Profesorado

## Objetivos Didácticos
- Comprender la arquitectura cliente-servidor de servicios de inferencia local como Ollama.
- Desarrollar clientes en Python utilizando gestores de proyectos modernos (`uv`, `httpx` / `urllib`) para invocar modelos `llama3.2` o `qwen2.5`.
- Exigir salida estructurada en formato JSON mediante la especificación de esquemas y prompt engineering.
- Medir rendimiento: tokens por segundo, tiempo hasta primer token (TTFT) y latencia total.

## Infraestructura Preparada
El profesorado desplegará un contenedor Ollama en la red local del centro para que el alumnado pueda realizar las primeras pruebas sin necesidad de descargar modelos pesados individualmente en sus equipos.

## Secuencia de Sesiones (15 horas)
1. **Sesión 1-2 (3h):** Arquitectura cliente-servidor de LLMs locales. Endpoints `/api/generate` y `/api/chat`.
2. **Sesión 3-4 (3h):** Creación del proyecto cliente con `uv init` y gestión de dependencias HTTP.
3. **Sesión 5-6 (3h):** Prompting estructurado y forzado de salida JSON (`format: "json"`).
4. **Sesión 7-8 (3h):** Benchmark de modelos locales: medición de latencia y consumo de RAM/GPU.
5. **Sesión 9-10 (3h):** Implementación de streaming y gestión de timeouts/reintentos.
