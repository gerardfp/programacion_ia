# 📊 Informe de Desviaciones: Curso vs. Currículo Oficial (BOE)

**Módulo Profesional:** Programación de Inteligencia Artificial (Código 5073)  
**Duración Referencia:** 110 horas  
**Curso Académico:** 2026-2027  

---

## 🎯 1. Resumen Ejecutivo

El diseño didáctico e implementado en este repositorio para el módulo **Programación de Inteligencia Artificial** realiza una **modernización y adaptación técnica relevante** respecto al currículo oficial redactado originalmente en el BOE.

Mientras que el currículo oficial propone un enfoque diversificado hacia herramientas de modelado visual (Knime, SPSS), servicios propietarios en la nube (Azure, AWS, Watson) y tecnologías heterogéneas (Blockchain, IoT), el presente curso adopta una filosofía **Local-First, Software Libre y Orientada a Producción de Software de IA Generativa** (Python 3.11+, `uv`, Ollama, RAG, Agentes, FastAPI y Docker Compose).

---

## 🔍 2. Anális Detallado de Desviaciones por Ámbito

### 2.1. Ecosistema Tecnológico e Infraestructura

| Aspecto | Currículo Oficial (BOE) | Diseño del Curso Implementado | Justificación Didáctica / Técnica |
|---|---|---|---|
| **Servicios de Nube y Proveedores** | Dependencia explícita de Azure, AWS, IBM Watson, Alexa, Cortana, Bixby. | **100% Local-First** mediante Ollama (`llama3.2:3b`), PostgreSQL/ChromaDB y Docker Compose. | **Soberanía tecnológica y privacidad:** Elimina costes de API keys de pago, garantiza cumplimiento de GDPR y permite el desarrollo 100% offline en la infraestructura del centro. |
| **Entornos de Modelado** | Herramientas gráficas/clásicas: Knime, IBM SPSS Modeler, Azure ML Studio. | **Desarrollo Basado en Código:** Python 3.11+, Pydantic V2, FastAPI, `uv`, `pytest`. | **Empleabilidad actual:** Las empresas demandan ingenieros capaces de construir APIs y pipelines de código mantenibles en lugar de operadores de herramientas de arrastrar y soltar (*drag-and-drop*). |
| **Lenguajes de Programación** | Dispersión entre Python, R, Java, JavaScript, Node.js y lenguajes de marcado. | **Focalización intensiva en Python 3.11+** y especificaciones JSON/Pydantic. | **Profundización vs Dispersión:** En un módulo de 110 horas, intentar abarcar 5 lenguajes impide adquirir el nivel profesional requerido en el ecosistema dominante de la IA (Python). |

---

### 2.2. Adaptación de Contenidos y Resultados de Aprendizaje

#### 🔹 RA1. Caracterización de Lenguajes de Programación para IA
* **Currículo Oficial:** Identificación de programas, características de Python, R, Java, JS y etiquetas XML/HTML.
* **Curso Implementado (UD01):** Enfoque en **Desarrollo Profesional en Python**. Se introducen herramientas modernas de gestión de proyectos (`uv`, `pyproject.toml`, `uv.lock`), tipado estático (`typing`), validación de esquemas en tiempo de ejecución (**Pydantic V2**), pruebas unitarias con `pytest` y buenas prácticas en Git.
* **Desviación:** Se eliminan R, Java y JavaScript para dedicar la carga horaria a la calidad de código y gestión profesional de dependencias en Python.

#### 🔹 RA2. Entornos de Modelado / Servicios de IA Locales
* **Currículo Oficial:** Evaluación de plataformas de IA, algoritmos predefinidos y modelado en Knime/SPSS/TensorFlow.
* **Curso Implementado (UD02):** **Consumo e Inferencia de LLMs Locales**. Arquitectura cliente-servidor con Ollama, peticiones HTTP asíncronas, *prompt engineering*, forzado de salidas JSON estructuradas y benchmarking (latencia, tokens/segundo, consumo de VRAM).
* **Desviación:** Se sustituye el modelado clásico tabular/gráfico por el consumo e integración técnica de modelos de lenguaje abiertos.

#### 🔹 RA3. Convergencia Tecnológica vs. Aplicaciones RAG y Agentes
* **Currículo Oficial:** Evaluación teórica de Blockchain, IoT, Cloud, convergencia de voz/imágenes y seguridad en negocios.
* **Curso Implementado (UD03 y UD04):**
  * **UD03 - Aplicaciones RAG Locales:** Ingesta de documentos, fragmentación (*chunking*), generación de embeddings locales (*Sentence Transformers*) e indexación en bases vectoriales (*ChromaDB / pgvector*).
  * **UD04 - Agentes Inteligentes:** Patrón ReAct, ejecuciones de herramientas (*Tool Calling*), conexión segura a bases relacionales (SQL anti-inyección), trazabilidad y logs de auditoría.
* **Desviación:** Se eliminan los contenidos teóricos de Blockchain e IoT por no ser pertinentes para un perfil de desarrollador de IA, reconvirtiendo la "convergencia" en la integración de LLMs con bases de datos vectoriales y relacionales.

#### 🔹 RA4. Automatización Industrial vs. APIs, Contenedores y Proyecto Final
* **Currículo Oficial:** Evaluación de estrategias corporativas, gestión de activos y modelos de automatización industrial.
* **Curso Implementado (UD05 y UD06):**
  * **UD05 - APIs y Despliegue:** Creación de APIs REST con FastAPI, contenerización con Dockerfiles optimizados (`uv`) y orquestación con Docker Compose.
  * **UD06 - Proyecto Final Integrador:** Desarrollo e integración de una solución empresarial completa desplegable en un comando.
* **Desviación:** Sustitución de los aspectos de gestión teórica industrial por competencias prácticas de **DevOps / MLOps** (despliegue de microservicios, contenerización y monitorización).

---

## 📈 3. Matriz Resumen de Cobertura y Desviaciones

| Módulo Oficial (BOE) | Unidad Didáctica en el Curso | Cobertura Currículo | Tipo de Desviación |
|---|---|:---:|---|
| **1. Caracterización de lenguajes** | UD01. Desarrollo profesional en Python | 80% | **Especialización:** Se elimina R/Java/JS para profundizar en Python profesional, `uv` y Pydantic. |
| **2. Entornos de modelado** | UD02. Servicios de IA locales | 70% | **Modernización:** Se sustituye Knime/SPSS por inferencia de LLMs locales con Ollama. |
| **3. Convergencia tecnológica** | UD03. Aplicaciones RAG locales<br>UD04. Agentes inteligentes | 60% | **Reorientación:** Se eliminan Blockchain/IoT y se incluye el desarrollo de RAG y Agentes autónomos. |
| **4. Modelos de automatización** | UD05. APIs, contenedores y operación<br>UD06. Proyecto final | 75% | **Práctica MLOps:** Se sustituye la teoría de automatización industrial por Docker, FastAPI y despliegue real. |

---

## 💡 4. Conclusiones y Valor Añadido

El curso diseñado **mantiene la duración oficial (110h)** y cumple con el espíritu del título de especialización (capacitar para programar e integrar Inteligencia Artificial), pero introduce tres mejoras fundamentales:

1. **Relevancia Laboral Directa:** Incorpora la pila tecnológica más demandada en 2026 (LLMs locales, RAG, Vector Databases, Agentes, FastAPI, Docker, `uv`).
2. **Soberanía Tecnológica y Privacidad:** El alumnado aprende a construir soluciones completas sin enviar datos a plataformas externas ni incurrir en costes de licencias/tokens.
3. **Calidad de Ingeniería de Software:** Se enseña a entregar proyectos testeados (`pytest`), tipados (`Pydantic`), empaquetados (`uv.lock`) y contenerizados (`Docker Compose`).
