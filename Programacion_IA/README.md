# Repositorio Didáctico: Programación de Inteligencia Artificial (5073)

Este repositorio contiene la estructura completa de contenidos, programaciones docentes, unidades didácticas, prácticas, ejemplos de código, arquitecturas de infraestructura y evaluaciones para el módulo **Programación de Inteligencia Artificial** (110 horas).

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

## 📁 Estructura del Repositorio

```text
Programacion_IA/
├── README.md
├── course-manifest.yaml
├── programacion_docente/
│   ├── programacion_general.md
│   ├── resultados_aprendizaje.md
│   ├── criterios_evaluacion.md
│   ├── temporalizacion.md
│   └── mapa_competencias.md
├── unidades_didacticas/
│   ├── UD01_python_profesional/
│   ├── UD02_servicios_ia_locales/
│   ├── UD03_aplicaciones_rag/
│   ├── UD04_agentes_inteligentes/
│   ├── UD05_apis_y_despliegue/
│   └── UD06_proyecto_final/
├── infraestructura/
│   └── profesor/
│       ├── compose.yaml
│       └── .env.example
├── datasets/
│   └── sample_dataset/
└── scripts/
    └── smoke_test.py
```

---

## 🛠️ Requisitos Rápidos de Infraestructura

- **Docker & Docker Compose** (v2+)
- **Python 3.11+**
- **Ollama** (con modelos `llama3.2:3b` o similares)
- **PostgreSQL 16** con soporte vectorial o **ChromaDB**

Para iniciar el entorno base del profesorado:

```bash
cd infraestructura/profesor
cp .env.example .env
docker compose up -d
```
