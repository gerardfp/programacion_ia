# UD01 - Guía para el Profesorado

## Objetivos Didácticos
- Convertir prototipos monolíticos (scripts o Jupyter Notebooks) en paquetes instalables y mantenibles en Python.
- Implantar el uso de gestores de proyectos ultra-rápidos con `uv`, `pyproject.toml` y el archivo de bloqueo reproducible `uv.lock`, manteniendo tipos estáticos (`type hints`) y validación rigurosa con `Pydantic`.
- Introducir las mejores prácticas de pruebas automatizadas con `pytest` y logging estructurado.

## Secuencia de Sesiones (15 horas)
1. **Sesión 1-2 (3h):** De notebooks a paquetes estructurados. Estructura de directorios y `pyproject.toml`.
2. **Sesión 3-4 (3h):** Tipado en Python y validación de datos con Pydantic V2.
3. **Sesión 5-6 (3h):** Sistema de logging y gestión profesional de excepciones.
4. **Sesión 7-8 (3h):** Pruebas unitarias e integración con `pytest` y `fixtures`.
5. **Sesión 9-10 (3h):** Control de versiones Git, ramas y entrega de la práctica autónoma.

## Errores Frecuentes del Alumnado
- Meclar dependencias globales sin entorno virtual.
- Usar diccionarios sin esquema ni validación de tipos.
- Dejar credenciales o rutas absolutas en el código.
- Escribir tests que dependen del estado global o de archivos externos no aislados.
