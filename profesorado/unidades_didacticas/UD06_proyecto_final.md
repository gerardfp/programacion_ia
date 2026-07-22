# UD06 - Guía Docente y Evaluación: Proyecto Final Integrador

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 20 horas  
**Resultado de Aprendizaje:** RA6 - Desarrolla e integra un proyecto final empresarial de IA.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Evaluar la capacidad de integración del alumnado reuniendo todos los aprendizajes del módulo: desarrollo profesional en Python con `uv`, consumo de LLMs locales con Ollama, RAG con ChromaDB, herramientas con agentes, APIs con FastAPI y contenerización con Docker Compose.
- Guiar en la redacción de la memoria técnica y el análisis de aspectos éticos, de privacidad local (GDPR) y seguridad.

### Secuencia de Sesiones (20 horas)
1. **Sesión 1-4 (4h):** Análisis de requisitos, diseño de arquitectura y aprobación de propuestas.
2. **Sesión 5-12 (8h):** Desarrollo de componentes backend, base vectorial, API y pruebas unitarias con `uv run pytest`.
3. **Sesión 13-16 (4h):** Contenerización total en Docker Compose y smoke testing local.
4. **Sesión 17-20 (4h):** Elaboración de memoria técnica y defensa pública del proyecto.

---

## 2. Requisitos e Instrumentos de Evaluación

### Evidencias Evaluables
- **Proyecto Funcional:** Código ejecutable con `docker compose up` que integre IA local, backend REST, base vectorial/relacional y pruebas unitarias.
- **Reproducibilidad con `uv`:** Declaración en `pyproject.toml` y `uv.lock`.
- **Memoria Técnica y Licencias:** Documento explicativo con arquitectura, decisiones de diseño, seguridad y privacidad (GDPR local).
- **Defensa Técnica:** Presentación oral apoyada por la diapositiva con demostración en vivo.

---

## 3. Rúbrica Oficial del Proyecto Final

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Integración Tecnológica** | Combina a la perfección IA local, FastAPI, ChromaDB/PostgreSQL y Docker Compose. | Integra los componentes principales funcionando en conjunto. | Fallos menores en la comunicación inter-servicio. | No consigue integrar los componentes. |
| **Reproducibilidad & uv** | `pyproject.toml` y `uv.lock` perfectos, desplegable en un comando. | Despliegue funcional con algunos pasos manuales. | Falta el archivo de bloqueo `uv.lock`. | No ejecutable ni reproducible. |
| **Calidad y Testing** | Pruebas pasa al 100% (`uv run pytest`), tipado Pydantic y logs estructurados. | Tests principales pasando sin errores. | Cobertura de pruebas baja o fallos ocasionales. | Sin pruebas ni validación. |
| **Memoria y Defensa** | Memoria técnica impecable, análisis ético/GDPR riguroso y defensa excelente. | Memoria técnica completa y defensa clara. | Memoria incompleta o defensas vacilantes. | Sin memoria técnica ni defensa. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD06_proyecto_final/`
