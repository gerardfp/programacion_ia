# Repositorio Didáctico: Programación de Inteligencia Artificial (5073)

Este repositorio contiene la estructura completa de contenidos, programaciones docentes, unidades didácticas, prácticas, ejemplos de código, arquitecturas de infraestructura y evaluaciones para el módulo **Programación de Inteligencia Artificial** en su modalidad intensiva de **50 horas**.

El repositorio está dividido claramente entre los **materiales del alumnado** (`alumnado/`) y los **recursos e infraestructura del docente** (`profesorado/`).

---

## 🎯 Enfoque Pedagógico y Tecnológico

- **Local-First & Software Libre:** Todo el módulo está diseñado para ejecutarse localmente en la infraestructura del centro educativo, sin depender de API keys de pago (OpenAI, Anthropic, Azure, etc.).
- **Gestión de Proyectos con `uv`:** Gestión ultra-rápida de entornos y dependencias reproducibles mediante `uv`, `pyproject.toml` y `uv.lock`.
- **Estructura en Dos Fases:**
  - **Fase 1: Aprendizaje y prácticas independientes (40 horas):** Adquisición de conceptos, herramientas y patrones de fiabilidad mediante prácticas acotadas en contextos variados.
  - **Fase 2: Proyecto final integrador (10 horas):** Integración de las capacidades aprendidas en una aplicación web de una empresa cerámica ficticia del sur de Castellón.
- **Principio de Transferencia de Conocimientos:** Las prácticas realizadas durante el curso no están contextualizadas en el proyecto final, garantizando que el alumnado aprenda los conceptos de forma general y no se limite a memorizar una solución preconstruida.
- **Tesis Central — El AI Harness:**
  > **El LLM propone o genera; la aplicación valida, autoriza y ejecuta.**  
  - **AI Harness:** Capa de software que gobierna, media y audita la interacción entre un modelo probabilístico y los recursos de la aplicación.
  - **Asimetría de autoridad:** El LLM no ostenta autoridad autónoma sobre los datos ni sobre las operaciones del sistema.

---

## 📚 Resumen de las Unidades del Curso Intensivo (50 Horas)

> [!NOTE]
> **Estructura Curricular:** El diseño pedagógico se estructura en **5 unidades formativas secuenciales (UD1 a UD5)**, correspondientes de forma directa y unívoca con las carpetas `UD01_...` a `UD05_...` del repositorio.

| Bloque / Unidad | Título Curricular | Horas | RA | Carpeta Repo | Contenidos Nucleares y Foco de Aprendizaje |
|---|---|:---:|:---:|:---:|---|
| **UD1** | [**Integración de LLM en Aplicaciones**](file:///home/gerard/programacion_ia/profesorado/unidades_didacticas/UD01_servicios_ia_locales.md) | **10 h** | RA2 | `UD01_servicios_ia_locales` | **Integración y Contratos de Datos:** APIs de modelos locales, mensajes por roles (`system`/`user`/`assistant`), límites de context window, generación de texto, extracción, datos estructurados, JSON y validación con Pydantic. Limitaciones y respuestas no fiables. Demo de streaming. |
| **UD2** | [**RAG y Acceso al Conocimiento**](file:///home/gerard/programacion_ia/profesorado/unidades_didacticas/UD02_aplicaciones_rag.md) | **12 h** | RA3 | `UD02_aplicaciones_rag` | **Recuperación y Grounding:** Embeddings, búsqueda semántica, chunking, bases de datos vectoriales con PostgreSQL (`pgvector`), grounding y citas, abstención ("NO_DATA"), **control de acceso dentro de la consulta SQL** y evaluación operacional sobre dataset cerrado. |
| **UD3** | [**Tool Calling y Acciones Controladas**](file:///home/gerard/programacion_ia/profesorado/unidades_didacticas/UD03_agentes_inteligentes.md) | **10 h** | RA4 | `UD03_agentes_inteligentes` | **Herramientas y Decisiones Gobernadas:** Definición formal de herramientas, argumentos tipados, tríada de validación (sintaxis, negocio, permisos), consulta vs modificación vs operaciones críticas, confirmación (*Human-in-the-Loop*), SQL parametrizado, límites de bucle, auditoría y demo MCP. |
| **UD4** | [**Integración, Seguridad y Control**](file:///home/gerard/programacion_ia/profesorado/unidades_didacticas/UD04_apis_y_despliegue.md) | **8 h** | RA5 | `UD04_apis_y_despliegue` | **Arquitectura de Servicio y Resiliencia:** APIs HTTP con FastAPI y API Contracts tipados, cuádruple frontera de seguridad, gestión de secretos en `.env`, *datos $\neq$ instrucciones*, taxonomía real de errores y robustez básica ante fallos, introducción a multimodalidad y observabilidad. |
| **UD5** | [**Proyecto Final: Empresa Cerámica**](file:///home/gerard/programacion_ia/profesorado/unidades_didacticas/UD05_proyecto_final.md) | **10 h** | RA6 | `UD05_proyecto_final` | **Integración Empresarial y Transferencia:** Integración de IA en la aplicación web de una empresa cerámica ficticia del sur de Castellón: 1. Asistente técnico de catálogo (RAG + tools de stock), 2. Visualizador de ambientes (multimodal), y 3. Asistente comercial/CRM con formalización de pedidos y defensa oral. |
| **TOTAL** | | **50 h** | | | |

---

## 🏭 Proyecto Final: Empresa Cerámica del Sur de Castellón

El proyecto final sitúa al alumnado ante un caso industrial real: integrar capacidades de IA en la aplicación web de una empresa fabricante de pavimentos y revestimientos cerámicos de Castellón (Onda, Vila-real, l'Alcora).

La aplicación base proporciona la infraestructura convencional (web, catálogo, base de datos relacional con `pgvector`, imágenes y fichas técnicas). El alumnado integra tres subsistemas:

1. **Asistente de Catálogo Técnico (RAG):** Consultas sobre especificaciones de producto (pavimentos y revestimientos, acabados y recomendaciones de colocación), con citas técnicas explícitas y herramientas de consulta de stock.
2. **Visualizador de Ambientes (Multimodal):** Integración de un servicio para proyectar el azulejo seleccionado sobre la fotografía de una estancia real del cliente.
3. **Asistente Comercial y Pedidos Simulados (Tool Calling y Pedidos):** Identificación de necesidades, cálculo matemático exacto de cajas por la aplicación y formalización de pedidos gobernada por el AI Harness (validación con Pydantic, reglas de negocio, autorización, confirmación y auditoría).

### Matriz de Transferencia de Competencias

| Durante el Curso (Prácticas Independientes - 40 h) | En el Proyecto Final Cerámico (10 h) |
|---|---|
| **Structured Output** | Extraer preferencias del cliente, metros cuadrados y datos de contacto desde el diálogo. |
| **Pydantic** | Validar rigurosamente los argumentos de pedidos y los datos del CRM antes de procesarlos. |
| **RAG** | Asistente de catálogo técnico (especificaciones y usos de pavimentos y revestimientos). |
| **Embeddings** | Búsqueda semántica de colecciones cerámicas por descripción de estilo o acabado. |
| **Control de Acceso (ACL)** | Filtrado en base de datos para impedir que usuarios sin permisos accedan a documentación interna. |
| **Tool Calling** | Consultar stock en almacén, verificar referencias y preparar borradores de pedido. |
| **Reglas de Negocio** | Verificar stock disponible y condiciones mínimas de pedido de la empresa. |
| **Autorización** | Controlar qué usuarios tienen permiso para emitir pedidos en firme. |
| **Confirmación de Acciones** | Exigir confirmación del cliente antes de registrar el pedido simulado. |
| **Persistencia** | Almacenamiento estructurado en PostgreSQL de clientes, contactos y pedidos simulados. |
| **Multimodalidad** | Visualizador de ambientes: envío de imagen de la estancia + azulejo para renderizado. |
| **Evaluación Operacional** | Comprobar respuestas del catálogo sobre el dataset cerrado de 20 casos cerámicos. |
| **Seguridad (Prompt Injection)** | Impedir que instrucciones del usuario modifiquen valores económicos calculados o eludan la confirmación. |
| **Auditoría (Audit Log)** | Registrar cada pedido simulado, usuario responsable e importe confirmado. |

---

## 📁 Estructura General del Repositorio

```text
Programacion_IA/
├── README.md                          # Visión general del repositorio y guía del módulo
│
├── alumnado/                          # 🎓 RECURSOS DIDÁCTICOS DEL ALUMNADO
│   ├── README.md                      # Guía de inicio para el alumnado
│   ├── datasets/                      # Datasets y ficheros de prueba para laboratorios
│   └── unidades_didacticas/           # Unidades UD01 a UD05 (Teoría, Prácticas, Starters)
│       ├── UD01_servicios_ia_locales/
│       ├── UD02_aplicaciones_rag/
│       ├── UD03_agentes_inteligentes/
│       ├── UD04_apis_y_despliegue/
│       └── UD05_proyecto_final/
│
└── profesorado/                       # 👨‍🏫 RECURSOS Y GESTIÓN DEL DOCENTE
    ├── README.md                      # Guía docente
    ├── programacion_docente/          # Documentación oficial (RA, CE, temporalización, mapa)
    ├── infraestructura/               # Despliegue base del centro (Ollama, DBs, Docker Compose)
    ├── scripts/                       # Scripts de mantenimiento y pruebas
    ├── soluciones/                    # Proyectos solución independientes por unidad
    │   ├── UD01_servicios_ia_locales/
    │   ├── UD02_aplicaciones_rag/
    │   ├── UD03_agentes_inteligentes/
    │   ├── UD04_apis_y_despliegue/
    │   └── UD05_proyecto_final/
    └── unidades_didacticas/           # Ficheros Markdown unificados por unidad (Guía+Eval+Rúbrica)
        ├── UD01_servicios_ia_locales.md
        ├── UD02_aplicaciones_rag.md
        ├── UD03_agentes_inteligentes.md
        ├── UD04_apis_y_despliegue.md
        └── UD05_proyecto_final.md
```

---

## 🛠️ Requisitos Rápidos de Infraestructura

- **Docker & Docker Compose** (v2+)
- **Python 3.11+**
- **uv** (Gestor de paquetes y entornos virtuales)
- **Git**
