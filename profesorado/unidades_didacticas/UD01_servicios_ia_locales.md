# UD01 - Guía Docente y Evaluación: Inferencia y Contratos de Software

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 10 horas (Bloque 1 / UD01 del curso intensivo)  
**Resultado de Aprendizaje:** RA2 - Consume servicios y modelos locales de IA mediante contratos de datos verificables.  
**Identificador Curricular Intensivo:** UD01 - LLM y Contratos de Software  

---

## 1. Guía para el Profesorado

### Problema Técnico Central
> **¿Cómo interactúo con un modelo de lenguaje desde un programa de software de forma robusta, estructurada y predecible?**  
> El texto libre generado por un LLM es intrínsecamente estocástico. El alumnado debe asimilar el **Principio 1 del Harness: Integridad y Contratos** (*el modelo propone dentro de unos límites; el software exterior valida y decide si la estructura es admisible*). Para ello, dominará la comunicación HTTP esencial, la estructura formal de mensajes por roles (`system`, `user`, `assistant`), las técnicas de *Prompt Engineering* para anclaje (*grounding*) frente a la alucinación, la gestión de la ventana de contexto (*context window*), y la validación de esquemas estructurados con Pydantic (`BaseModel`, `model_validate_json`).

### Objetivos Didácticos
- Comprender la arquitectura cliente-servidor HTTP esencial: peticiones (`method`, `URL`, `headers`, `body`) y respuestas (`status code`, `headers`, `body`).
- Entender el concepto de asincronía (`httpx` asíncrono) como mecanismo para no bloquear el bucle de eventos mientras se espera respuesta de red I/O.
- Estructurar diálogos formales mediante listas de mensajes y roles tipados (`system`, `user`, `assistant`).
- Conocer la gestión de la ventana de contexto (*context window*): límites de memoria del modelo, saturación y trade-offs de latencia.
- Dominar el *Prompt Engineering* como disciplina de software: delimitación de bloques, restricciones explícitas, formatos esperados, plantillas parametrizadas y cláusulas estrictas de abstención ("Si no dispones del dato en el contexto, responde NO_DATA").
- Definir formalmente **Alucinación** (generación verosímil pero falsa/desanclada) y su contramedida: el **Grounding** (anclaje factual en fuentes).
- **Fallo Didáctico vs Solución de Ingeniería (Crash & Learn):** Comprobar cómo pedir "devuélveme un JSON" en texto libre rompe `json.loads()` por preámbulos conversacionales, y resolverlo mediante el modo JSON estructurado validado por contratos Pydantic.
- Distinguir conceptualmente: **Contratos de salida estructurada** (validación de datos) $\neq$ **Tool Calling** (solicitud de ejecución de acciones).
- Observar el comportamiento de streaming (Server-Sent Events) como demostración práctica de concurrencia y latencia.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio de Inferencia Ollama:** Servidor en la red del aula (`http://192.168.1.100:11434` o local en Docker Compose).
- **Modelos pre-descargados:** `ollama pull llama3.2:3b` y `ollama pull qwen2.5:3b`.
- **Librerías Python del Alumno:** `httpx`, `pydantic` instaladas mediante `uv add`.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (10 horas)

#### **Sesión 1-2 (4 horas): Fundamentos HTTP, Inferencia Local y Estructura de Mensajes**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Fundamentos HTTP (Petición/Respuesta, Códigos de Estado) y Arquitectura Cliente-Servidor de Inferencia Local.
  - *Diapositiva 2:* Estructura formal de una conversación: Mensajes y roles (`system`, `user`, `assistant`) frente a concatenación de texto plano.
  - *Diapositiva 3:* Parámetros de inferencia (temperatura, longitud) y límites físicos de la ventana de contexto (*Context Window*).
- **Material Teórico:** UD01 en [README.md](file:///home/gerard/programacion_ia/README.md#ud01-servicios-ia-locales).
- **Desarrollo de la Sesión:**
  1. Exploración con `curl` del protocolo HTTP hacia `/api/tags` y `/api/chat`.
  2. Construcción de una estructura de mensajes en Python con rol de sistema restrictivo y rol de usuario.
  3. Experimentación con la temperatura (0.0 vs 1.0) y saturación intencionada de la ventana de contexto para observar el truncado de información.
  4. **Actividad Inicial:** Etapa 1 en [README.md](file:///home/gerard/programacion_ia/README.md#ud01-etapa1).

#### **Sesión 3-4 (4 horas): Prompt Engineering, Alucinación, Contratos y Pydantic**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Prompt Engineering como disciplina de software: delimitadores, instrucciones negativas, plantillas y few-shot.
  - *Diapositiva 5:* El problema de la Alucinación y la necesidad de Grounding (anclaje factual con cláusulas de abstención).
  - *Diapositiva 6:* El fallo de parsear texto libre con `json.loads()` frente a contratos y validación con Pydantic (`model_validate_json`).
- **Material Teórico:** Etapas 3 a 5 del manual del alumno.
- **Desarrollo de la Sesión (Crash & Learn):**
  1. **El Fallo:** El alumnado pide extraer datos en JSON sin activar formato JSON. El LLM añade preámbulos conversacionales ("¡Claro! Aquí tienes tu JSON:") y `json.loads()` crashea con `JSONDecodeError`.
  2. **La Solución:** Solicitud de esquema JSON al modelo y validación estricta en el Harness con `BaseModel` de Pydantic (`model_validate_json`).
  3. **Práctica Guiada y Práctica Autónoma:** Etapas 3 y 5 en [README.md](file:///home/gerard/programacion_ia/README.md#ud01-etapa3).

#### **Sesión 5 (2 horas): Demostración de Streaming y Métricas de Inferencia**
- **Diapositivas a proyectar:** 
  - *Diapositiva 7:* Streaming y eventos de servidor (SSE): recepción progresiva vs espera bloqueante.
  - *Diapositiva 8:* Métricas operativas: latencia total y tokens por segundo.
- **Desarrollo de la Sesión:**
  1. Demostración guiada de consumo de respuestas token a token mediante Server-Sent Events.
  2. Observación de métricas de rendimiento (`eval_count` / `eval_duration`).
  3. **Reto de Consolidación:** Etapa 7 en [README.md](file:///home/gerard/programacion_ia/README.md#ud01-etapa7).

---

### ⚠️ Errores Frecuentes del Alumnado
- No configurar un timeout adecuado en `httpx` (provocando bloqueos por defecto a los 5 segundos).
- Intentar parsear respuestas sin haber enviado el flag de formato estructurado en la petición a Ollama.
- No controlar las excepciones de conexión (`httpx.ConnectError`) cuando el servicio de inferencia no está disponible.
- Confundir tokens por segundo de procesamiento de prompt con tokens por segundo de generación de respuesta.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Cliente HTTP y Roles:** Código cliente ejecutable en Git que consuma la API de inferencia local gestionando roles (`system`, `user`, `assistant`) y errores de conexión.
- **Diseño de Prompts y Grounding:** Plantillas de instrucciones parametrizadas con delimitadores y cláusulas estrictas de abstención ("NO_DATA") para mitigar alucinaciones.
- **Contratos y Validación (Pydantic):** Modelos `BaseModel` que validan las respuestas estructuradas propuestas por el LLM mediante `model_validate_json`.

---

## 3. Rúbrica Oficial de la Unidad (Escala de 3 Niveles)

| Criterio | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|---|---|---|
| **Consumo HTTP y Roles** | Cliente estructurado que maneja peticiones HTTP, roles formales (`system`/`user`), timeouts y errores de conexión sin fallos no capturados. | Cliente funcional conectando correctamente con Ollama y gestionando roles básicos. | Peticiones HTTP malformadas, sin roles estructurados o errores no gestionados. |
| **Prompt Engineering & Grounding** | Prompts parametrizados con delimitadores claros, cláusula de abstención ("NO_DATA") y mitigación comprobada de alucinaciones. | Instrucciones comprensibles con restricciones básicas de comportamiento. | Prompts ambiguos, sin delimitadores ni mecanismos de anclaje. |
| **Contratos y Validación** | Define contratos estrictos con esquemas Pydantic; valida propuestas del LLM con `model_validate_json` rechazando entradas malformadas de forma controlada. | Valida respuestas JSON mediante Pydantic en la mayoría de llamadas pero con manejo de excepciones elemental. | Parseo frágil con `json.loads()` en texto libre, sin esquemas formales ni validación. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD01_servicios_ia_locales/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD01_servicios_ia_locales) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD01_servicios_ia_locales/UD01_03_actividad_inicial/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD01_servicios_ia_locales/UD01_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD01_servicios_ia_locales/UD01_04_practica_guiada/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD01_servicios_ia_locales/UD01_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD01_servicios_ia_locales/UD01_05_practica_autonoma/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD01_servicios_ia_locales/UD01_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD01_servicios_ia_locales/UD01_06_reto_ampliacion/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD01_servicios_ia_locales/UD01_06_reto_ampliacion)
