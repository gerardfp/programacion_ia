---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD06: Proyecto Final'
footer: 'Curso 2026-2027 | Módulo 5073'
style: |
  section {
    background-color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #1e3a8a;
  }
  h2 {
    color: #2563eb;
  }
  code {
    background-color: #e2e8f0;
    color: #0f172a;
  }
---

# UD06: Proyecto Final Integrador
## Presentación y Defensa Técnica de la Solución de IA

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** Integración Completa, Operatividad Real y Defensa Profesional

---

## 1. Planteamiento del Problema Empresarial

- **Definición del caso de uso:** Problema de negocio real resuelto mediante IA local.
- **Justificación de la arquitectura elegida:**
  - Por qué se optó por inferencia local (privacidad, normativa, coste).
  - Elección de modelos de lenguaje y modelos de embeddings.
  - Estrategia de ingestión y actualización de datos.

---

## 2. Arquitectura General del Sistema Integrado

```text
               +----------------------------------+
               |  Interfaz de Usuario (Streamlit) |
               +----------------+-----------------+
                                |
                                v
               +----------------+-----------------+
               |   API REST Backend (FastAPI)     |
               +-------+------------------+-------+
                       |                  |
                       v                  v
         +-------------+-----+      +-----+--------------+
         | Servicio LLM Local |      | Base Datos Vector  |
         |      (Ollama)      |      | (Chroma/pgvector)  |
         +--------------------+      +--------------------+
```

---

## 3. Calidad de Código y Gestión de Proyectos con `uv`

- **Reproducibilidad:** Proyecto empaquetado con `pyproject.toml` y `uv.lock`.
- **Pruebas y Validación:** Cobertura de pruebas unitarias en `pytest` para la API y los componentes de RAG / Agente.
- **Estructura limpia:** Separación de capas (`src/api`, `src/core`, `src/db`, `tests/`).

---

## 4. Demostración en Vivo (Live Demo)

- **Escenarios de prueba clave:**
  1. Consulta directa con respuesta estructurada JSON.
  2. Búsqueda documental RAG con citación de fuentes exactas.
  3. Ejecución de herramientas por el agente inteligente (*Tool Calling*).
  4. Resiliencia ante errores de entrada o tiempos de respuesta.

---

## 5. Evaluación de Seguridad, Ética y Conclusiones

- **Privacidad de datos:** Garantía de no filtración de datos sensibles fuera de la red del centro.
- **Auditoría:** Registro de logs de inferencia, métricas de consumo de VRAM / CPU y latencia.
- **Posibles líneas futuras:** Escalabilidad, afinado de prompts (*prompt engineering*) y guardarraíles (*guardrails*) adicionales.
