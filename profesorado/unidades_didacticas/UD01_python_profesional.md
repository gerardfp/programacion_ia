# UD01 - Guía Docente y Evaluación: Desarrollo Profesional en Python para IA

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 15 horas  
**Resultado de Aprendizaje:** RA1 - Caracteriza lenguajes de programación y entornos de desarrollo para Inteligencia Artificial.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Convertir prototipos monolíticos (scripts o Jupyter Notebooks) en paquetes instalables y mantenibles en Python.
- Implantar el uso de gestores de proyectos ultra-rápidos con `uv`, `pyproject.toml` y el archivo de bloqueo reproducible `uv.lock`, manteniendo tipos estáticos (`type hints`) y validación rigurosa con `Pydantic`.
- Introducir las mejores prácticas de pruebas automatizadas con `pytest` y logging estructurado.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servidor Git Local (GitLab / Gitea):** Repositorio centralizado para el control de versiones y la entrega de prácticas del alumnado.
- **Requisitos de Hardware / Servicios:** No requiere servicios pesados de IA ni GPU en esta primera unidad. Conexión de red local estándar.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (15 horas)

#### **Sesión 1-2 (3 horas): Del Cuaderno de Notas a Producción con `uv`**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Del cuaderno de notas a producción (Limitaciones de Jupyter en entornos productivos).
  - *Diapositiva 2:* Gestión de proyectos con `uv`, `pyproject.toml` y `uv.lock`.
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD01_python_profesional/UD01_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Presentación de la unidad y debate sobre los problemas de despliegue de notebooks.
  2. Demostración del docente creando un proyecto con `uv init` y sincronizando dependencias con `uv sync`.
  3. **Actividad a realizar:** `UD01_03_actividad_inicial.md` (Refactorización individual de un notebook desordenado a módulos `.py`).

#### **Sesión 3-4 (3 horas): Tipado Estático y Validación con Pydantic V2**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Tipado estático en Python 3.11+ (`typing`).
  - *Diapositiva 4:* Validación de datos en tiempo de ejecución con Pydantic V2.
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación teórica sobre la importancia de garantizar tipos en las peticiones a LLMs.
  2. **Práctica Guiada (Parte 1):** Inicio de `UD01_04_practica_guiada.md` utilizando el esqueleto `starter/`. Creación de esquemas Pydantic (`PeticionInferencia`, `RespuestaInferencia`).

#### **Sesión 5-6 (3 horas): Logging Estructurado y Manejo Profesional de Excepciones**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4 (repaso):* Esquemas estrictos de entrada/salida y captura de excepciones.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación sobre la configuración del módulo `logging` estándar frente a `print()`.
  2. **Práctica Guiada (Parte 2):** Continuación de `UD01_04_practica_guiada.md`. Incorporación de registrador de logs y captura de excepciones en el paquete `ia_utils`.

#### **Sesión 7-8 (3 horas): Pruebas Automatizadas con `pytest`**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Pruebas automatizadas con `pytest` y buenas prácticas en Git.
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Explicación del framework `pytest`, aserciones y ejecución con `uv run pytest`.
  2. **Práctica Autónoma:** Desarrollo de `UD01_05_practica_autonoma.md`. El alumnado implementa individualmente los casos de prueba para validar datos de entrada y manejo de errores.

#### **Sesión 9-10 (3 horas): Control de Versiones en Git, Reto y Entrega**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5 (continuación):* Commits atómicos, `.gitignore` de `.venv` y flujo de trabajo en Git.
- **Desarrollo de la Sesión:**
  1. **Reto de Ampliación:** Trabajo en `UD01_06_reto_ampliacion.md` (Implementación de fixtures avanzadas e integración de captura de logs en `pytest`).
  2. Subida del proyecto al servidor Git del centro y entrega de la práctica.

---

### ⚠️ Errores Frecuentes del Alumnado
- Mezclar dependencias globales sin entorno virtual (`uv venv` no ejecutado).
- Usar diccionarios sin esquema ni validación de tipos Pydantic.
- Incluir la carpeta `.venv/` en las subidas a Git (falta de `.gitignore`).
- Escribir tests unitarios que dependen del estado global o de rutas absolutas locales.

---

## 2. Criterios e Instrumentos de Evaluación

### Instrumentos y Evidencias Evaluables
- **Entregable en Git:** Repositorio individual con el paquete `ia_utils` y archivo `pyproject.toml` + `uv.lock`.
- **Pruebas automatizadas:** Verificación mediante `uv run pytest` del 100% de los tests pasando.
- **Formato y Calidad:** Cumplimiento de estándares de tipado (`mypy`/`ruff`) y estructura de archivos en `src/`.

---

## 3. Rúbrica de Evaluación

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Estructura del Proyecto** | `pyproject.toml` perfecto, estructura `src/` modular y limpia con `uv.lock`. | Estructura modular correcta pero pequeños errores menores. | Falta `pyproject.toml` o mezcla scripts sueltos. | Proyecto sin estructura ni entorno virtual. |
| **Validación Pydantic** | Modelos estrictos, campos tipados y validaciones personalizadas. | Modelos funcionales sin validaciones avanzadas. | Error en tipos de datos o esquemas incompletos. | Sin validación de esquemas ni tipos. |
| **Testing pytest** | Tests exhaustivos, cubre casos límite y fixtures reutilizables. | Tests principales funcionando correctamente. | Tests incompletos o algunos fallos en ejecución. | Sin tests unitarios. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
[profesorado/soluciones/UD01_python_profesional/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD01_python_profesional)
