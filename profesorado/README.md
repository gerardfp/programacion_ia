# 👨‍🏫 Espacio del Profesorado

Este directorio contiene la documentación docente, guías unificadas por unidad, planificación oficial y soluciones de referencia para el módulo **Programación de Inteligencia Artificial**.

---

## 📁 Estructura del Espacio del Profesorado

```text
profesorado/
├── README.md                      # Guía del profesorado (este archivo)
├── infraestructura/               # Guías de despliegue de aula (Ollama, PostgreSQL, Docker)
├── programacion_docente/          # Documentos macro del currículo oficial
├── soluciones/                    # Soluciones por código de actividad (UDXX_03 a UDXX_06)
│   ├── UD01_03/                   # Solución Actividad Inicial UD01
│   ├── UD01_04/                   # Solución Práctica Guiada UD01
│   ├── UD01_05/                   # Solución Práctica Autónoma UD01
│   ├── UD01_06/                   # Solución Reto Ampliación UD01
│   ├── ...                        # (Hasta UD06_06)
├── scripts/                       # Tests de verificación (smoke_test.py)
└── unidades_didacticas/           # Guías unificadas del profesorado en Markdown
    ├── UD01_python_profesional.md
    ├── UD02_servicios_ia_locales.md
    ├── UD03_aplicaciones_rag.md
    ├── UD04_agentes_inteligentes.md
    ├── UD05_apis_y_despliegue.md
    └── UD06_proyecto_final.md
```

---

## 🛠️ Ejecución de Verificación Estructural
Para comprobar que todos los recursos, guías y soluciones por actividad cumplen con la estructura oficial:

```bash
python profesorado/scripts/smoke_test.py
```
