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

## 📁 Estructura General del Repositorio

```text
Programacion_IA/
├── README.md                          # Visión general del repositorio
├── course-manifest.yaml               # Manifiesto y metadatos del módulo
│
├── alumnado/                          # 🎓 RECURSOS DIDÁCTICOS DEL ALUMNADO
│   ├── README.md                      # Guía de inicio para el alumnado
│   ├── datasets/                      # Datasets y ficheros de prueba para laboratorios
│   └── unidades_didacticas/           # Unidades UD01 a UD06 (Teoría, Prácticas, Starters)
│       ├── UD01_python_profesional/
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
    │   ├── UD01_python_profesional/
    │   ├── UD02_servicios_ia_locales/
    │   ├── UD03_aplicaciones_rag/
    │   ├── UD04_agentes_inteligentes/
    │   ├── UD05_apis_y_despliegue/
    │   └── UD06_proyecto_final/
    └── unidades_didacticas/           # Ficheros Markdown unificados por unidad (Guía+Eval+Rúbrica)
        ├── UD01_python_profesional.md
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
