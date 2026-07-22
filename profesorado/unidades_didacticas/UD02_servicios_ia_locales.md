# UD02 - Guía Docente y Evaluación: Servicios de IA Locales

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 15 horas  
**Resultado de Aprendizaje:** RA2 - Integra y consume servicios y modelos locales de IA.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Comprender la arquitectura cliente-servidor de servicios de inferencia local como Ollama.
- Desarrollar clientes en Python utilizando gestores de proyectos modernos (`uv`, `httpx`) para invocar modelos `llama3.2` o `qwen2.5`.
- Exigir salida estructurada en formato JSON mediante la especificación de esquemas Pydantic y prompt engineering.
- Medir rendimiento: tokens por segundo, tiempo hasta primer token (TTFT) y latencia total.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio de Inferencia Ollama:** Desplegado mediante Docker Compose o servicio de sistema en la IP del aula (ej. `http://192.168.1.100:11434`).
- **Modelos pre-descargados:** 
  - `ollama pull llama3.2:3b` (modelo por defecto ligero).
  - `ollama pull qwen2.5:3b` (para benchmarking comparativo).
- **Red Local:** Puerto `11434` accesible para todos los puestos de alumnos. Variable de entorno configurada `OLLAMA_HOST=0.0.0.0`.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (15 horas)

#### **Sesión 1-2 (3 horas): Inferencia Local vs Nube y Arquitectura Ollama**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Inferencia Local vs Nube (Privacidad, coste cero por token y control total).
  - *Diapositiva 2:* Arquitectura de Ollama (API REST, gestión de modelos `pull` / `run`).
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD02_servicios_ia_locales/UD02_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Presentación de las ventajas de la inferencia local en centros educativos y empresas.
  2. Demostración interactiva en consola invocando la API de Ollama mediante `curl` al servidor del centro.
  3. **Actividad a realizar:** `UD02_03_actividad_inicial.md` (Exploración de la API de Ollama y envío de peticiones `/api/generate` manuales).

#### **Sesión 3-4 (3 horas): Cliente Python Asíncrono con `uv` y `httpx`**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Consumo de la API de Ollama desde Python gestionado con `uv`.
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación del consumo programático con `httpx` (manejo de timeouts y peticiones POST).
  2. **Práctica Guiada (Parte 1):** Inicio de `UD02_04_practica_guiada.md` utilizando el esqueleto `starter/`. Construcción de la clase `OllamaClient`.

#### **Sesión 5-6 (3 horas): Respuestas Estructuradas con Modo JSON y Pydantic**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Respuestas estructuradas (JSON Mode) y validación inmediata con Pydantic.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación de la propiedad `"format": "json"` en las peticiones a Ollama y forzado de esquemas.
  2. **Práctica Guiada (Parte 2):** Completar `UD02_04_practica_guiada.md`. Parseo automático de la respuesta JSON a modelos de Pydantic.

#### **Sesión 7-8 (3 horas): Benchmarking de Rendimiento y Medición de Métricas**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Rendimiento y métricas: Tokens por segundo (TTFT, VRAM, consumo CPU/GPU).
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación del cálculo de tokens/segundo analizando los metadatos de respuesta (`eval_count` / `eval_duration`).
  2. **Práctica Autónoma:** Desarrollo de `UD02_05_practica_autonoma.md` (Creación de un validador y benchmark de inferencia local).

#### **Sesión 9-10 (3 horas): Resiliencia, Reto de Ampliación y Evaluación**
- **Desarrollo de la Sesión:**
  1. **Reto de Ampliación:** Trabajo en `UD02_06_reto_ampliacion.md` (Implementación de reintentos automáticos con backoff exponencial e interfaz CLI de consulta).
  2. Evaluación de las entregas en Git frente a la solución de referencia en `profesorado/soluciones/UD02_servicios_ia_locales/`.

---

### ⚠️ Errores Frecuentes del Alumnado
- No configurar un timeout adecuado en `httpx` (causando bloqueos por defecto a los 5 segundos).
- Intentar parsear respuestas sin haber enviado `"format": "json"` en la petición a Ollama.
- No controlar las excepciones de conexión (`httpx.ConnectError`) cuando el servidor Ollama se reinicia.
- Confundir tokens por segundo del prompt (*prompt_eval*) con tokens por segundo de respuesta (*eval_count*).

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
[profesorado/soluciones/UD02_servicios_ia_locales/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD02_servicios_ia_locales)
