# Repositorio Didáctico: Programación de Inteligencia Artificial (5073)

Este repositorio contiene la estructura completa de contenidos, programaciones docentes, unidades didácticas, prácticas, ejemplos de código, arquitecturas de infraestructura y evaluaciones para el módulo **Programación de Inteligencia Artificial** (110 horas).

El repositorio está dividido claramente entre los **materiales del alumnado** (`alumnado/`) y los **recursos e infraestructura del docente** (`profesorado/`).

---

## 🎯 Enfoque Pedagógico y Tecnológico

- **Local-First & Software Libre:** Todo el módulo está diseñado para ejecutarse localmente en la infraestructura del centro educativo, sin depender de API keys de pago (OpenAI, Anthropic, Azure, etc.).
- **Gestión de Proyectos con `uv`:** Gestión ultra-rápida de entornos y dependencias reproducibles mediante `uv`, `pyproject.toml` y `uv.lock`.
- **Aprendizaje Basado en Proyectos (ABP):** Progresión práctica desde el desarrollo en Python profesional hasta el despliegue de soluciones multi-servicio contenerizadas.
- **Despliegue Progresivo:**
  1. Consumo de servicios preparados por el profesorado.
  2. Integración y desarrollo en aplicaciones cliente.
  3. Despliegue guiado de servicios por el alumnado.
  4. Diseño autónomo y operación (Docker Compose, logs, métricas, persistencia).

---

## 📚 Resumen de las Unidades del Curso

> [!NOTE]
> **Coordinación Docente:** Los contenidos iniciales de desarrollo profesional en Python (anteriormente UD01) son impartidos por otro profesor en un módulo formativo paralelo. Por tanto, este repositorio arranca directamente con la integración y explotación práctica de modelos de IA locales a partir de la **UD02**.

| Unidad | Título | Horas | RA | Tecnologías Clave | Práctica / Proyecto Resultante |
|---|---|:---:|:---:|---|---|
| **UD02** | **Servicios de IA Locales** | 15 h | RA2 | Ollama, `httpx`, Pydantic V2, `llama3.2:3b` | Cliente Python asíncrono con salida JSON estructurada y benchmarking de rendimiento (latencia, tokens/s). |
| **UD03** | **Aplicaciones RAG Locales** | 25 h | RA3 | ChromaDB, Sentence Transformers, `pgvector` | Asistente documental RAG local anti-alucinaciones con ingesta, *chunking* semántico y citación de fuentes. |
| **UD04** | **Agentes Inteligentes y Automatización** | 15 h | RA4 | Patrón ReAct, Tool Calling, PostgreSQL 16 | Agente autónomo con ejecución segura de herramientas, consultas SQL parametrizadas y logs de auditoría. |
| **UD05** | **APIs, Contenedores y Operación** | 20 h | RA5 | FastAPI, Docker, Docker Compose, `uv` | Microservicio REST de IA contenerizado con Dockerfile multi-stage, *health checks* y orquestación multi-contenedor. |
| **UD06** | **Proyecto Final Integrador** | 20 h | RA6 | Stack completo (FastAPI + Ollama + ChromaDB + Streamlit) | Solución empresarial integral contenerizada (`docker compose up`), con pruebas automáticas (`pytest`), memoria técnica y defensa en vivo. |

### 🔍 Detalle de Contenidos por Unidad

- **UD02: Servicios de IA Locales (15 h - RA2)**
  Inferencia local frente a servicios en la nube (privacidad, coste cero por token y soberanía tecnológica). Arquitectura cliente-servidor con Ollama, consumo de endpoints `/api/generate` y `/api/chat`, peticiones HTTP asíncronas con `httpx`, forzado de respuestas en formato JSON estricto y validación de esquemas con Pydantic. Medición de métricas de rendimiento: tiempo hasta el primer token (TTFT), latencia total y velocidad de generación (tokens/segundo).

- **UD03: Aplicaciones RAG Locales (25 h - RA3)**
  Ampliación del conocimiento de los modelos de lenguaje mediante recuperación semántica de datos empresariales propios sin dependencias externas. Pipeline RAG completo: ingesta documental, estrategias de particionado (*chunking*) con solapamiento, generación de embeddings densos con Sentence Transformers (`all-MiniLM-L6-v2`) e indexación vectorial en ChromaDB (o `pgvector`). Recuperación semántica k-NN e integración contextualizada en Ollama previniendo alucinaciones mediante la citación estricta de fuentes y metadatos.

- **UD04: Agentes Inteligentes y Automatización (15 h - RA4)**
  Transición desde chatbots reactivos hacia agentes autónomos capaces de razonar y ejecutar acciones. Implementación del bucle ReAct (*Thought -> Action -> Observation -> Final Answer*). Registro e invocación segura de herramientas (*Tool Calling*) tipadas con esquemas Pydantic. Conexión controlada con bases de datos relacionales (PostgreSQL 16) con prevención de inyección SQL, límites de iteración, confirmación previa para operaciones críticas (*Human-in-the-Loop*) y trazabilidad exhaustiva mediante registros de auditoría (*audit logs*).

- **UD05: APIs, Contenedores y Operación (20 h - RA5)**
  Paso del prototipo a la entrega de servicios listos para producción (DevOps / MLOps). Exposición de modelos y agentes mediante APIs REST asíncronas con FastAPI y documentación automática interactiva con Swagger UI. Contenerización optimizada con Dockerfiles multi-stage basados en imágenes ligeras `python:3.11-slim` y el gestor `uv`. Orquestación multi-servicio reproducible con Docker Compose conectando la API con el servidor Ollama y las bases de datos, gestionando variables de entorno (`.env`), redes aisladas, volúmenes persistentes y comprobaciones de salud (*health checks*).

- **UD06: Proyecto Final Integrador (20 h - RA6)**
  Diseño, desarrollo, empaquetado y defensa pública de una solución integral empresarial de Inteligencia Artificial. Integración de todos los componentes aprendidos: servicio de inferencia local, pipeline RAG sobre documentación corporativa, agentes con ejecución de herramientas, API REST en FastAPI, interfaz gráfica de usuario en Streamlit y orquestación completa con Docker Compose desplegable en un solo comando (`docker compose up -d`). Incluye pruebas automáticas con `pytest`, memoria técnica justificativa (cumplimiento GDPR y decisiones de arquitectura) y exposición en directo.

---

## 📁 Estructura General del Repositorio

```text
Programacion_IA/
├── README.md                          # Visión general del repositorio
├── course-manifest.yaml               # Manifiesto y metadatos del módulo
│
├── alumnado/                          # 🎓 RECURSOS DIDÁCTICOS DEL ALUMNADO
│   ├── README.md                      # Guía de inicio para el alumnado
│   ├── datasets/                      # Datasets y ficheros de prueba para laboratorios
│   └── unidades_didacticas/           # Unidades UD02 a UD06 (Teoría, Prácticas, Starters)
│       ├── UD02_servicios_ia_locales/
│       ├── UD03_aplicaciones_rag/
│       ├── UD04_agentes_inteligentes/
│       ├── UD05_apis_y_despliegue/
│       └── UD06_proyecto_final/
│
└── profesorado/                       # 👨‍🏫 RECURSOS Y GESTIÓN DEL DOCENTE
    ├── README.md                      # Guía docente
    ├── programacion_docente/          # Documentación oficial (RA, CE, temporalización)
    ├── infraestructura/               # Despliegue base del centro (Ollama, DBs, Docker Compose)
    ├── scripts/                       # Scripts de mantenimiento y pruebas
    ├── soluciones/                    # Proyectos solución independientes por unidad
    │   ├── UD02_servicios_ia_locales/
    │   ├── UD03_aplicaciones_rag/
    │   ├── UD04_agentes_inteligentes/
    │   ├── UD05_apis_y_despliegue/
    │   └── UD06_proyecto_final/
    └── unidades_didacticas/           # Ficheros Markdown unificados por unidad (Guía+Eval+Rúbrica)
        ├── UD02_servicios_ia_locales.md
        ├── UD03_aplicaciones_rag.md
        ├── UD04_agentes_inteligentes.md
        ├── UD05_apis_y_despliegue.md
        └── UD06_proyecto_final.md
```

---

## 🛠️ Requisitos Rápidos de Infraestructura

- **Docker & Docker Compose** (v2+)
- **Python 3.11+**
- **Ollama** (con modelos `llama3.2:3b` o similares)
- **PostgreSQL 16** con soporte vectorial o **ChromaDB**

Para iniciar el entorno base del profesorado:

```bash
cd profesorado/infraestructura/profesor
cp .env.example .env
docker compose up -d
```
