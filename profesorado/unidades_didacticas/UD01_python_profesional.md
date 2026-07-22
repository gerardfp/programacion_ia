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

### Secuencia de Sesiones (15 horas)
1. **Sesión 1-2 (3h):** De notebooks a paquetes estructurados. Estructura de directorios y `pyproject.toml`.
2. **Sesión 3-4 (3h):** Tipado en Python y validación de datos con Pydantic V2.
3. **Sesión 5-6 (3h):** Sistema de logging y gestión profesional de excepciones.
4. **Sesión 7-8 (3h):** Pruebas unitarias e integración con `pytest` y `fixtures`.
5. **Sesión 9-10 (3h):** Control de versiones Git, ramas y entrega de la práctica autónoma.

### Errores Frecuentes del Alumnado
- Mezclar dependencias globales sin entorno virtual.
- Usar diccionarios sin esquema ni validación de tipos.
- Dejar credenciales o rutas absolutas en el código.
- Escribir tests que dependen del estado global o de archivos externos no aislados.

---

## 2. Criterios e Instrumentos de Evaluación

### Instrumentos y Evidencias Evaluables
- **Entregable en Git:** Repositorio público/privado con el paquete `ia-utils`.
- **Pruebas automatizadas:** Verificación mediante `pytest` del 100% de los tests pasando.
- **Formato y Calidad:** Cumplimiento de estándares de tipado (`mypy`/`ruff`) y estructura de archivos en `src/`.

---

## 3. Rúbrica de Evaluación

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Estructura del Proyecto** | `pyproject.toml` perfecto, estructura `src/` modular y limpia. | Estructura modular correcta pero pequeños errores menores. | Falta `pyproject.toml` o mezcla scripts sueltos. | Proyecto sin estructura ni entorno virtual. |
| **Validación Pydantic** | Modelos estrictos, campos tipados y validaciones personalizadas. | Modelos funcionales sin validaciones avanzadas. | Error en tipos de datos o esquemas incompletos. | Sin validación de esquemas ni tipos. |
| **Testing pytest** | Tests exhaustivos, cubre casos límite y fixtures reutilizables. | Tests principales funcionando correctamente. | Tests incompletos o algunos fallos en ejecución. | Sin tests unitarios. |

---

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD01_python_profesional/`
