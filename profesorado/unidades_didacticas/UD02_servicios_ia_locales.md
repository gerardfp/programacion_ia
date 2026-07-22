# UD02 - Guía Docente y Evaluación: Servicios de IA Locales

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 15 horas  
**Resultado de Aprendizaje:** RA2 - Integra y consume servicios y modelos locales de IA.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Comprender la arquitectura cliente-servidor de servicios de inferencia local como Ollama.
- Desarrollar clientes en Python utilizando gestores de proyectos modernos (`uv`, `httpx` / `urllib`) para invocar modelos `llama3.2` o `qwen2.5`.
- Exigir salida estructurada en formato JSON mediante la especificación de esquemas y prompt engineering.
- Medir rendimiento: tokens por segundo, tiempo hasta primer token (TTFT) y latencia total.

### Infraestructura Preparada
El profesorado desplegará un contenedor Ollama en la red local del centro para que el alumnado pueda realizar las primeras pruebas sin necesidad de descargar modelos pesados individualmente en sus equipos.

### Secuencia de Sesiones (15 horas)
1. **Sesión 1-2 (3h):** Arquitectura cliente-servidor de LLMs locales. Endpoints `/api/generate` y `/api/chat`.
2. **Sesión 3-4 (3h):** Creación del proyecto cliente con `uv init` y gestión de dependencias HTTP.
3. **Sesión 5-6 (3h):** Prompting estructurado y forzado de salida JSON (`format: "json"`).
4. **Sesión 7-8 (3h):** Benchmark de modelos locales: medición de latencia y consumo de RAM/GPU.
5. **Sesión 9-10 (3h):** Implementación de streaming y gestión de timeouts/reintentos.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Cliente HTTP funcional:** Código cliente ejecutable en Git que consuma la API de Ollama sin errores.
- **Salida JSON estricta:** Garantía de parsed JSON mediante Pydantic.
- **Benchmark:** Reporte en consola o Markdown con métricas de latencia y tokens/segundo.

---

## 3. Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Consumo de API HTTP** | Cliente robusto con gestión de timeouts, errores de conexión y reintentos. | Cliente funcional conectando correctamente con Ollama. | Peticiones HTTP básicas con errores ocasionales. | No consigue conectar con la API de Ollama. |
| **Salida JSON Estructurada** | Esquema JSON perfecto, parseado automáticamente con Pydantic. | Salida JSON válida en la mayoría de peticiones. | Respuestas de texto plano sin estructurar. | JSON malformado o ininterpretable. |
| **Métricas de Latencia** | Mide TTFT, latencia total y tokens/segundo con logs estructurados. | Registra la latencia global en segundos. | Medición imprecisa o incompleta. | Sin medición de rendimiento. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD02_servicios_ia_locales/`
