# UD04 - Guía Docente y Evaluación: API Contracts, Seguridad y Fallos

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 8 horas (Bloque 4 / UD03 del curso intensivo)  
**Resultado de Aprendizaje:** RA5 - Expone APIs con contratos explícitos, seguridad integral y gestión de fallos.  
**Identificador Curricular Intensivo:** UD03 - API Contracts, Seguridad y Fallos  

---

## 1. Guía para el Profesorado

### Problema Técnico Central
> **¿Cómo expongo el Harness como servicio de red seguro, con contratos explícitos y alta resistencia a fallos?**  
> Una API no es simplemente una URL que ejecuta código Python; es un contrato de comunicación formal entre sistemas. El alumnado debe aplicar el **Principio 4 del Harness: Seguridad Integral y Contratos de Servicio**. Empaquetará la lógica en una API REST con FastAPI definiendo esquemas estrictos de petición y respuesta (*API Contracts*), gestionará secretos mediante variables de entorno en `.env` excluidas de Git, implementará la cuádruple frontera de seguridad y gestionará una taxonomía real de errores (contrato, negocio, autorización, infraestructura y modelo) con timeouts y fallbacks.

### Objetivos Didácticos
- Definir **API Contracts** formales: esquemas Pydantic para `QueryRequest` (pregunta, usuario, contexto) y `QueryResponse` (respuesta generada, fuentes/citas, latencia) con documentación interactiva OpenAPI.
- Comprender el propósito de la asincronía en FastAPI (`async`/`await`) para no bloquear el bucle de eventos mientras se espera respuesta de I/O de red, utilizándolo de manera proporcionada sin convertirlo en dogma evaluable.
- Implementar la **Cuádruple Frontera de Seguridad**:
  1. *Autenticación:* ¿Quién es el usuario que realiza la petición?
  2. *Autorización:* ¿Qué acciones o endpoints tiene permitido invocar?
  3. *Control de acceso a datos:* ¿Qué fragmentos puede consultar en la base de datos?
  4. *Reglas de negocio:* ¿Qué operaciones puede ejecutar en el contexto actual?
- Asimilar el principio de seguridad ante Prompt Injection:
  > **"El prompt no es un mecanismo de autorización."**  
  Los delimitadores (`"""`) y las instrucciones no son una barrera mágica; la protección reside en la arquitectura, la validación de esquemas y el mínimo privilegio.
- Aplicar una **Taxonomía Real de Errores**:
  - *Errores de entrada / contrato (HTTP 422):* Esquemas malformados o datos incompletos.
  - *Errores de negocio (HTTP 400/422):* Restricciones de dominio incumplidas.
  - *Errores de autorización (HTTP 403):* Peticiones denegadas por permisos insuficientes.
  - *Errores de infraestructura (HTTP 504 / 502):* Timeouts del LLM o caídas de BD, mitigados con reintentos y fallbacks estructurados.
  - *Errores del modelo:* Respuestas truncadas o solicitudes de formato no conformes.
- Gestión segura de secretos: exclusión estricta de tokens y contraseñas en Git mediante `.env` y `.gitignore`.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Stack Docker Compose Provisto:** Archivo `compose.yaml` listo para arrancar PostgreSQL y Ollama.
- **Framework FastAPI:** `fastapi`, `uvicorn`, `pydantic` instalados con `uv`.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (8 horas)

#### **Sesión 1-2 (4 horas): Contratos de API con FastAPI y Gestión de Secretos**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Qué es un API Contract: Esquemas formales Request/Response y códigos HTTP semánticos.
  - *Diapositiva 2:* Endpoints `/query`, `/agent` y `/health` con FastAPI y Swagger UI (`/docs`).
  - *Diapositiva 3:* Gestión de credenciales: Variables de entorno en `.env` y exclusión en `.gitignore`.
- **Material Teórico:** UD04 en [README.md](file:///home/gerard/programacion_ia/README.md#ud04-apis-y-despliegue).
- **Desarrollo de la Sesión:**
  1. Definición de contratos Pydantic para peticiones y respuestas con citas y metadatos.
  2. Construcción de endpoints en FastAPI validando tipos y cabeceras.
  3. Comprobación interactiva en `/docs` y verificación de que `.env` no se versiona en Git.
  4. **Actividad Inicial:** Etapa 1 en [README.md](file:///home/gerard/programacion_ia/README.md#ud04-etapa1).

#### **Sesión 3-4 (4 horas): Cuádruple Frontera de Seguridad y Taxonomía de Errores (Crash & Learn)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* La Cuádruple Frontera: Autenticación vs Autorización vs Acceso a datos vs Negocio.
  - *Diapositiva 5:* Prompt Injection: Por qué el prompt no es una barrera de seguridad (*"El prompt no autoriza"*).
  - *Diapositiva 6:* Taxonomía real de errores: De timeouts de inferencia (504) a fallbacks estructurados.
- **Material Teórico:** Etapas 3 a 5 del manual del alumno.
- **Desarrollo de la Sesión (Crash & Learn):**
  1. **El Fallo:** Se inyecta una instrucción maliciosa en el input simulando evasión de permisos y se fuerza un timeout desconectando el LLM. La API sin defensas devuelve trazas internas o ejecuta acciones no autorizadas.
  2. **La Solución:** Separación tajante entre datos e instrucciones, autorización externa en el Harness y manejadores de excepciones que devuelven respuestas controladas de fallback.
  3. **Práctica Guiada y Práctica Autónoma:** Etapas 3 y 5 en [README.md](file:///home/gerard/programacion_ia/README.md#ud04-etapa3).
  4. **Reto de Consolidación:** Etapa 7 en [README.md](file:///home/gerard/programacion_ia/README.md#ud04-etapa7).

---

### ⚠️ Errores Frecuentes del Alumnado
- Creer que pedirle al modelo en el prompt "no ejecutes esto si el usuario no es admin" es una medida de seguridad válida.
- Exponer credenciales o contraseñas en el código fuente o comitear el archivo `.env` en el repositorio.
- Devolver errores 500 no gestionados con trazas de pila completas cuando el LLM sufre un timeout de inferencia.
- No validar el payload de entrada, permitiendo que peticiones vacías lleguen a consumir recursos del LLM.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Servicio FastAPI con Contratos de API:** Endpoints `/query`, `/agent` y `/health` con esquemas Pydantic tipados y respuestas con citas.
- **Gestión de Secretos:** Configuración mediante variables de entorno en `.env` correctamente excluido del control de versiones.
- **Manejo Estructurado de Excepciones:** Respuestas HTTP semánticas (400, 403, 422, 504) con mensajes controlados de fallback ante timeouts o caídas de infraestructura.
- **Frontera de Seguridad:** Separación de roles y comprobación de que el prompt no actúa como mecanismo de autorización.

---

## 3. Rúbrica Oficial de la Unidad (Escala de 3 Niveles)

| Criterio | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|---|---|---|
| **Contratos de API y Validación** | Define esquemas Request/Response tipados con Pydantic; valida entradas y genera respuestas estructuradas con citas y códigos HTTP semánticos. | Endpoints funcionales con validación básica de esquemas en FastAPI. | Respuestas no estructuradas, ausencia de contratos formales o errores de validación sin capturar. |
| **Seguridad y Gestión de Secretos** | Credenciales aisladas en `.env` ignorado en Git; aplica la cuádruple frontera y el principio de que el prompt no autoriza acciones. | Variables de entorno configuradas pero con separación conceptual de seguridad mejorable. | Claves duras en el código, `.env` comiteado en Git o delegación de permisos al texto del prompt. |
| **Resiliencia y Taxonomía de Errores** | Captura timeouts de inferencia y caídas de infraestructura devolviendo respuestas controladas de fallback (HTTP 504/502). | Manejo básico de excepciones pero con posibles caídas no controladas ante fallos de red. | Errores 500 con exposición de trazas de pila o cuelgue del servicio ante timeouts. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD04_apis_y_despliegue/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD04_apis_y_despliegue) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD04_apis_y_despliegue/UD04_03_actividad_inicial/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD04_apis_y_despliegue/UD04_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD04_apis_y_despliegue/UD04_04_practica_guiada/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD04_apis_y_despliegue/UD04_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD04_apis_y_despliegue/UD04_05_practica_autonoma/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD04_apis_y_despliegue/UD04_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD04_apis_y_despliegue/UD04_06_reto_ampliacion/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD04_apis_y_despliegue/UD04_06_reto_ampliacion)
