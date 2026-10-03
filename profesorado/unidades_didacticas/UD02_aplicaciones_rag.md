# UD02 - Guía Docente y Evaluación: Capa de Recuperación y Contexto (RAG)

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 12 horas (Bloque 2 / UD01 del curso intensivo)  
**Resultado de Aprendizaje:** RA3 - Desarrolla aplicaciones RAG con control de acceso en la consulta y evaluación medible.  
**Identificador Curricular Intensivo:** UD01 - RAG y Grounding con Control de Acceso  

---

## 1. Guía para el Profesorado

### Problema Técnico Central
> **¿Cómo respondo sobre datos propios con control de acceso y compruebo científicamente si la respuesta final es correcta?**  
> Un LLM desconoce los datos de la empresa y tiende a alucinar. El alumnado debe aplicar el **Principio 2 del Harness: Grounding y Contexto Controlado**. Comprenderá la distinción entre Grounding (anclaje factual general) y RAG (técnica concreta de recuperación de contexto). Aplicará higiene previa a los datos, asociará metadatos de autorización, indexará en PostgreSQL (`pgvector`), inyectará contexto delimitado y evaluará el sistema en **dos niveles sobre un dataset cerrado**: recuperación (*Hit Rate @ k*) y fidelidad factual de la respuesta generada con citas explícitas.

### Objetivos Didácticos
- Comprender el pipeline completo de RAG: Higiene de Datos $\rightarrow$ Chunking estructural $\rightarrow$ Embeddings vía API $\rightarrow$ Almacenamiento en PostgreSQL (`pgvector`) $\rightarrow$ Consulta vectorial con filtros de acceso $\rightarrow$ Inyección en prompt con citación obligatoria.
- **Calidad de Datos previa al Chunking:** Demostrar que *"un embedding malo no arregla unos datos basura"*. Detección de ficheros vacíos/corruptos, normalización UTF-8 y preservación de cabeceras.
- **Principio de Seguridad en RAG:**
  > **"Nunca se recupera información a la que el usuario no tiene derecho de acceso para filtrarla posteriormente."**  
  El filtrado por departamento y nivel de acceso se ejecuta directamente en la cláusula `WHERE` de la consulta SQL vectorial.
- **Similaridad Vectorial y Persistencia en `pgvector`:** Comprender conceptualmente la distancia coseno (`<=>`) en `pgvector`. El índice `HNSW` se explica como un acelerador de búsqueda provisto en la base de datos (sin exigir desarrollos matemáticos internos).
- **Evaluación Sistemática en DOS NIVELES sobre Dataset Cerrado:**
  - *Nivel 1 — Recuperación (Retrieval):* Medir *Hit Rate @ k* sobre un conjunto controlado de 20-30 casos conocidos (`pregunta` $\rightarrow$ `doc_esperado_id`).
  - *Nivel 2 — Generación (Fidelidad):* Evaluar si la respuesta está respaldada por el contexto recuperado, verificar citas de fuentes y comprobar la abstención estricta ("NO_DATA") ante preguntas fuera de contexto. *Recuperar el fragmento adecuado no garantiza que el modelo genere la respuesta correcta.*

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio Ollama Operativo:** Servidor local ejecutando `llama3.2:3b` y el modelo de embeddings `nomic-embed-text`.
- **Base de Datos PostgreSQL 16 con `pgvector`:** Instancia con extensión `vector` e índice preconfigurado en el Compose provisto.
- **Dataset Documental de Aula:** Corpus técnico en `alumnado/datasets/sample_dataset/` con documentos que incluyen permisos por departamento y referencias cruzadas.
- **Librerías Python locales:** `httpx`, `psycopg` (o `sqlalchemy`), `pgvector` y `pytest` gestionados mediante `uv`.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (12 horas)

#### **Sesión 1-2 (4 horas): Calidad de Datos, Ingesta y Embeddings en PostgreSQL (`pgvector`)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Límites de memoria y alucinación en LLMs: Del texto libre al Grounding mediante RAG.
  - *Diapositiva 2:* Calidad de datos previa: Limpieza, descarte de vacíos y preservación de estructura en chunking.
  - *Diapositiva 3:* Generación de embeddings vía API REST de Ollama (`POST /api/embed`) y distancia coseno en `pgvector`.
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD02_aplicaciones_rag/UD02_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Limpieza de un lote de documentos y fragmentación preservando títulos de sección.
  2. Obtención de embeddings mediante llamada a la API local (`str` $\rightarrow$ `list[float]`).
  3. Inserción de fragmentos y vectores en PostgreSQL con tabla tipada `vector`.
  4. **Actividad Inicial:** `UD02_03_actividad_inicial.md`.

#### **Sesión 3-4 (4 horas): Control de Acceso en la Consulta de Recuperación y Citación**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Seguridad en RAG: Filtrar en la consulta vs filtrar en memoria (*"Nunca recuperar para filtrar después"*).
  - *Diapositiva 5:* Consultas SQL vectoriales con filtros combinados (`WHERE departamento = :dep AND rol <= :rol`).
  - *Diapositiva 6:* Construcción de prompts delimitados con inyección de contexto y citación obligatoria de fuentes.
- **Material Teórico:** Secciones 3 y 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Implementación de la consulta SQL vectorial con filtros de autorización integrados.
  2. Ensamblado del prompt con delimitadores claros para separar contexto de instrucciones.
  3. Comprobación de que usuarios sin permisos reciben abstención al no haber recuperado documentos confidenciales.
  4. **Práctica Guiada:** `UD02_04_practica_guiada.md`.

#### **Sesión 5-6 (4 horas): Evaluación en Dos Niveles (Retrieval + Fidelidad de Generación)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 7:* Por qué evaluar en dos niveles: el desacoplamiento entre recuperación y generación.
  - *Diapositiva 8:* Métrica de recuperación (*Hit Rate @ k*) y verificación de fidelidad factual sobre dataset cerrado.
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Ejecución de suite de evaluación sobre el dataset de aula (20-30 preguntas controladas).
  2. Medición cuantitativa del *Hit Rate @ k*.
  3. Evaluación de respuestas generadas comprobando citación exacta y respuesta "NO_DATA" en preguntas sin contexto.
  4. **Práctica Autónoma y Reto de Consolidación:** `UD02_05_practica_autonoma.md` y `UD02_06_reto_ampliacion.md`.

---

### ⚠️ Errores Frecuentes del Alumnado
- Recuperar los $k$ documentos más similares en SQL y luego filtrarlos por permisos con un `if` en Python (violación de seguridad que expone datos en memoria).
- Intentar comparar vectores calculados con modelos de embeddings diferentes (incompatibilidad dimensional o espacial).
- Olvidar la cláusula estricta de abstención en el prompt del sistema, provocando que el LLM invente datos cuando el retrieval no aporta fragmentos relevantes.
- Asumir que un *Hit Rate* del 100% asegura que la respuesta generada sea correcta sin evaluar la fidelidad al contexto.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Pipeline RAG en PostgreSQL:** Ingesta de documentos con metadatos y almacenamiento vectorial en `pgvector`.
- **Filtro de Permisos en Consulta:** Consultas SQL que unen similaridad vectorial (`<=>`) con filtros de autorización en la cláusula `WHERE`.
- **Generación Fundamentada con Citas:** Respuestas ancladas en el contexto con indicación de fuentes y abstención controlada ante ausencia de datos.
- **Script de Evaluación en Dos Niveles:** Código ejecutable que calcule el *Hit Rate @ k* y evalúe la fidelidad en el dataset cerrado de prueba.

---

## 3. Rúbrica Oficial de la Unidad (Escala de 3 Niveles)

| Criterio | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|---|---|---|
| **Almacenamiento y Recuperación Vectorial** | Ingesta limpia, cálculo de embeddings vía API local e inserción estructurada en PostgreSQL con `pgvector` y búsqueda vectorial funcional. | Ingesta básica con `pgvector` y recuperación vectorial operativa. | Errores en embeddings, tipos vectoriales incorrectos o fallos en la consulta a la base de datos. |
| **Control de Acceso y Permisos** | El filtrado de departamento y permisos se ejecuta estrictamente dentro de la consulta SQL vectorial; ningún dato no autorizado se recupera en memoria. | Aplica filtros de acceso pero con inconsistencias menores o filtros parciales en código Python posterior. | No restringe acceso a datos confidenciales o recupera fragmentos privados antes de filtrarlos. |
| **Grounding y Citación** | Respuestas fundamentadas en el contexto con citas precisas de las fuentes; abstención estricta ("NO_DATA") ante falta de contexto. | Respuestas ancladas con mención de fuentes, aunque con imprecisiones en casos frontera. | Alucinación recurrente, respuestas desancladas del contexto o sin citación de fuentes. |
| **Evaluación en Dos Niveles** | Script automatizado que mide *Hit Rate @ k* y evalúa la fidelidad factual de la respuesta sobre un dataset cerrado de casos controlados. | Mide la recuperación con *Hit Rate* pero no verifica sistemáticamente la fidelidad de la respuesta generada. | Sin script de evaluación cuantitativa o sin métricas verificables. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD02_aplicaciones_rag/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD02_aplicaciones_rag) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD02_aplicaciones_rag/UD02_03_actividad_inicial/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD02_aplicaciones_rag/UD02_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD02_aplicaciones_rag/UD02_04_practica_guiada/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD02_aplicaciones_rag/UD02_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD02_aplicaciones_rag/UD02_05_practica_autonoma/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD02_aplicaciones_rag/UD02_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD02_aplicaciones_rag/UD02_06_reto_ampliacion/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD02_aplicaciones_rag/UD02_06_reto_ampliacion)
