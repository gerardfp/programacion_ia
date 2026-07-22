# UD06 - Guía Docente y Evaluación: Proyecto Final Integrador

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 20 horas  
**Resultado de Aprendizaje:** RA6 - Desarrolla e integra un proyecto final empresarial de IA.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Evaluar la capacidad de integración del alumnado reuniendo todos los aprendizajes del módulo: desarrollo profesional en Python con `uv`, consumo de LLMs locales con Ollama, RAG con ChromaDB, herramientas con agentes, APIs con FastAPI y contenerización con Docker Compose.
- Guiar en la redacción de la memoria técnica y el análisis de aspectos éticos, de privacidad local (GDPR) y seguridad.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Entorno de Despliegue de Stacks:** Servidor Linux con Docker Compose listo para hospedar las demostraciones de los proyectos finales si se opta por despliegue centralizado.
- **Servidor de Repositorios (GitLab / Gitea):** Plataforma para la entrega de los repositorios finales con etiquetado de versión `v1.0.0`.
- **Cañón de Proyección / Proyector de Aula:** Preparado para las sesiones de defensa pública de proyectos.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (20 horas)

#### **Sesión 1-4 (4 horas): Propuesta de Caso de Uso y Diseño de Arquitectura**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Presentación del Proyecto Empresarial (Problema de negocio planteado).
  - *Diapositiva 2:* Arquitectura del Sistema (Componentes: FastAPI, Ollama, ChromaDB, Docker Compose).
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD06_proyecto_final/UD06_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Definición del alcance del proyecto (ej. Asistente Documental de Soporte Técnico, Agente Auditor de BDs).
  2. **Actividad a realizar:** `UD06_03_actividad_inicial.md` (Redacción del anteproyecto, diagrama de arquitectura y aprobación por parte del docente).

#### **Sesión 5-12 (8 horas): Desarrollo Backend, Base Vectorial y Testing con `uv`**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Calidad de código y gestión de dependencias con `uv` (`pyproject.toml` + `uv.lock`).
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Trabajo práctico intensivo en parejas o individualmente.
  2. **Práctica Guiada / Trabajo de Campo:** Desarrollo guiado mediante `UD06_04_practica_guiada.md` y `UD06_05_practica_autonoma.md`.
  3. Ejecución continua de pruebas automáticas con `uv run pytest`.

#### **Sesión 13-16 (4 horas): Contenerización Total, Interfaz y Smoke Testing**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Demostración en vivo (Live Demo): Inferencia local, RAG y ejecución de herramientas.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Construcción del archivo `compose.yaml` integrando backend FastAPI, base vectorial ChromaDB e interfaz frontend Streamlit.
  2. **Reto / Puesta a Punto:** `UD06_06_reto_ampliacion.md` (Verificación de resiliencia, logs de auditoría e interfaz visual limpia).

#### **Sesión 17-20 (4 horas): Memoria Técnica y Defensa Pública del Proyecto**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Evaluación de seguridad, privacidad local (GDPR) y conclusiones técnicas.
- **Desarrollo de la Sesión:**
  1. Entrega de la memoria técnica y repositorio Git etiquetado.
  2. **Defensa Oral Pública (15 min por alumno/equipo):** Exposición apoyada en las diapositivas Marp y demostración funcional en vivo.
  3. Evaluación por parte del profesorado utilizando la rúbrica oficial frente al proyecto de referencia en `profesorado/soluciones/UD06_proyecto_final/`.

---

### ⚠️ Errores Frecuentes del Alumnado
- Intentar abarcar un caso de uso excesivamente amplio en lugar de centrarse en un producto mínimo viable (MVP) sólido.
- No incluir el archivo de bloqueo `uv.lock` en la entrega, provocando inconsistencias en las versiones de dependencias durante la corrección.
- Dejar rutas absolutas locales en los scripts que impiden la ejecución en el servidor del profesor.
- Omitir el análisis de aspectos éticos, de protección de datos (GDPR) o de seguridad en la memoria técnica.

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
[profesorado/soluciones/UD06_proyecto_final/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD06_proyecto_final)
