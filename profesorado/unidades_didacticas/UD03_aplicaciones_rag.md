# UD03 - Guía Docente y Evaluación: Aplicaciones RAG Locales

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 25 horas  
**Resultado de Aprendizaje:** RA3 - Desarrolla aplicaciones RAG (Retrieval-Augmented Generation) locales.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Construir un motor de recuperación de información semántica sin enviar datos a internet.
- Comprender las fases del pipeline RAG: Ingesta -> Fragmentación (Chunking) -> Embeddings -> Almacenamiento Vectorial -> Recuperación k-NN -> Inferencia Contextualizada.
- Evaluar y prevenir alucinaciones mediante citación de fuentes originales y metadatos.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio Ollama Operativo:** Servidor local ejecutando `llama3.2:3b` accesible por HTTP.
- **Dataset de Muestra Disponible:** Repositorio documental inicial precargado en `alumnado/datasets/sample_dataset/` (ficheros JSON y Markdown de prueba).
- **Servicio Opcional de Base de Datos:** PostgreSQL 16 con la extensión `pgvector` habilitada para alumnos que opten por persistencia SQL vectorial.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (25 horas)

#### **Sesión 1-4 (4 horas): Ingesta Documental y Estrategias de Fragmentación (Chunking)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* El problema del límite de memoria y las alucinaciones en los LLMs.
  - *Diapositiva 2:* Arquitectura RAG (Recuperación semántica de conocimiento interno).
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD03_aplicaciones_rag/UD03_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Concepto de RAG y análisis de por qué los LLMs alucinan al no tener datos de la empresa.
  2. **Actividad a realizar:** `UD03_03_actividad_inicial.md` (Analizar el dataset sintético en `alumnado/datasets/sample_dataset/sample.json` y diseñar estrategias de chunking con solapamiento).

#### **Sesión 5-8 (4 horas): Embeddings Locales y Vectores Densos**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Modelos de Embeddings locales y Bases de Datos Vectoriales.
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación matemática/conceptual del espacio vectorial y similitud de cosenos.
  2. Uso del modelo `sentence-transformers/all-MiniLM-L6-v2` local sin llamadas a APIs externas.
  3. **Práctica Guiada (Parte 1):** Inicio de `UD03_04_practica_guiada.md` con la plantilla `starter/`. Vectorización de fragmentos de texto.

#### **Sesión 9-12 (4 horas): Almacenamiento Vectorial e Indexación con ChromaDB**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3 (continuación):* ChromaDB / pgvector, indexación k-NN y metadatos.
- **Material Teórico:** Sección 3 (continuación) del material del alumno.
- **Desarrollo de la Sesión:**
  1. Creación de colecciones en ChromaDB y almacenamiento persistente en disco.
  2. **Práctica Guiada (Parte 2):** Completar `UD03_04_practica_guiada.md`. Ingesta masiva y consultas por k vecinos más cercanos (k-NN).

#### **Sesión 13-16 (4 horas): Construcción del Pipeline RAG Completo con Ollama**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Construcción del motor RAG con `uv` e integración con Ollama.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Integración del contexto recuperado en el prompt enviado a Ollama.
  2. **Práctica Autónoma (Parte 1):** Inicio de `UD03_05_practica_autonoma.md` (Construcción del motor RAG unificado).

#### **Sesión 17-20 (4 horas): Evaluación de Fidelidad, Citación de Fuentes y Anti-alucinación**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Evaluación de fidelidad y citación de fuentes para auditoría.
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Técnicas de prompt engineering para forzar que el modelo responda *"No dispongo de información suficiente en el contexto"* si la distancia vectorial supera un umbral.
  2. **Práctica Autónoma (Parte 2):** Finalización de `UD03_05_practica_autonoma.md` con trazabilidad de documentos de origen.

#### **Sesión 21-25 (5 horas): Reto de Ampliación, Interfaz de Usuario y Evaluación**
- **Desarrollo de la Sesión:**
  1. **Reto de Ampliación:** Trabajo en `UD03_06_reto_ampliacion.md` (Incorporar filtrado por metadatos dinámicos e interfaz gráfica ligera con Streamlit).
  2. Evaluación y contraste de las soluciones frente a `profesorado/soluciones/UD03_aplicaciones_rag/`.

---

### ⚠️ Errores Frecuentes del Alumnado
- Elegir un tamaño de chunk demasiado grande (superando el límite del modelo de embeddings) o demasiado pequeño (perdiendo el contexto semántico).
- No guardar la base de datos ChromaDB en un directorio persistente (`Client(path="./chroma_db")`), perdiendo los vectores al reiniciar el script.
- Pasar todo el contenido del PDF/documento sin haber limpiado caracteres extraños ni encabezados repetidos.
- Permitir que el LLM responda con su conocimiento general en lugar de restringirse estrictamente al contexto proporcionado.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Pipeline RAG Funcional:** Código en Git con ingestión, almacenamiento vectorial en ChromaDB y generación contextualizada.
- **Fidelidad y Mitigación de Alucinaciones:** Instrucciones claras en el prompt para no responder sin datos en el contexto.
- **Citación de Fuentes:** Inclusión explícita de metadatos de los documentos de origen.

---

## 3. Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Pipeline RAG** | Ingesta, chunking, embeddings y ChromaDB integrados a la perfección. | Pipeline funcional con respuestas contextualmente correctas. | Ingesta parcial o fallos en la recuperación vectorial. | No recupera contexto ni conecta con la base vectorial. |
| **Citación y Alucinaciones** | Cita fuentes exactas y evita alucinaciones cuando no hay contexto. | Muestra las fuentes de información. | Alucina respuestas ignorando el contexto recuperado. | Sin control de alucinación ni fuentes. |
| **Persistencia** | Colección ChromaDB persistente en disco correctamente estructurada. | Persistencia funcional en disco. | Colección volátil exclusivamente en memoria. | Error en almacenamiento de vectores. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
[profesorado/soluciones/UD03_aplicaciones_rag/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD03_aplicaciones_rag)
