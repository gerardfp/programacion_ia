# 🎓 Materiales Didácticos para el Alumnado

Bienvenido al repositorio de materiales didácticos del módulo **Programación de Inteligencia Artificial**.

En este espacio encontrarás todos los recursos necesarios para seguir las clases, realizar los laboratorios prácticos y desarrollar los proyectos del curso.

---

## 📁 Estructura del Espacio del Alumnado

```text
alumnado/
├── README.md                      # Guía del estudiante (este archivo)
├── datasets/                      # Conjuntos de datos para ejercicios y prácticas
└── unidades_didacticas/           # Contenidos y actividades por unidad
    ├── UD01_python_profesional/   # Desarrollo profesional en Python
    ├── UD02_servicios_ia_locales/ # Inferencia y consumo de LLMs locales (Ollama)
    ├── UD03_aplicaciones_rag/     # Asistentes documentales y bases vectoriales
    ├── UD04_agentes_inteligentes/ # Agentes, ejecuciones de herramientas y memoria
    ├── UD05_apis_y_despliegue/     # FastAPI, Docker Compose y monitorización
    └── UD06_proyecto_final/       # Proyecto integrador final
```

---

## 📄 Contenido de cada Unidad Didáctica

Dentro de cada carpeta de unidad didáctica (`UDXX`) dispones de los siguientes documentos y carpetas:

- `02_material_alumno.md`: Guía de teoría y conceptos clave de la unidad.
- `03_presentacion.md`: Resumen y diapositivas de la unidad.
- `04_actividad_inicial.md`: Ejercicio de activación y toma de contacto.
- `05_practica_guiada.md`: Tutorial paso a paso guiado por el profesorado.
- `06_practica_autonoma.md`: Enunciado del trabajo práctico individual o en parejas.
- `07_reto_ampliacion.md`: Ejercicio opcional de profundización para ampliar nota.
- `starter/`: Esqueleto de código inicial o plantilla para comenzar las prácticas con `uv`.

---

## 🚀 Cómo empezar una práctica

1. Navega a la unidad correspondiente (ej. `alumnado/unidades_didacticas/UD01_python_profesional/starter`).
2. Crea tu entorno e instala dependencias con `uv`:
   ```bash
   uv sync
   ```
3. Ejecuta tus scripts o pruebas utilizando `uv run`:
   ```bash
   uv run pytest
   ```
