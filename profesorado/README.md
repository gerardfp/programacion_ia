# 👨‍🏫 Espacio del Profesorado: Programación de Inteligencia Artificial

Este directorio contiene la documentación docente, guías metodológicas, rúbricas de evaluación, soluciones completas de ejercicios e infraestructura del módulo **Programación de Inteligencia Artificial (5073)**.

---

## 📁 Estructura del Espacio del Profesorado

```text
profesorado/
├── README.md                      # Guía del profesorado (este archivo)
├── programacion_docente/          # Documentos curriculares oficiales
│   ├── programacion_general.md    # Programación general del módulo
│   ├── resultados_aprendizaje.md  # Relación de RA y duraciones
│   ├── criterios_evaluacion.md    # Criterios de evaluación detallados
│   ├── temporalizacion.md         # Distribución horaria por unidades
│   └── mapa_competencias.md       # Trazabilidad RA vs Criterios
├── infraestructura/               # Servicios base para el aula
│   └── profesor/                  # Docker Compose con Ollama, Postgres, etc.
├── scripts/                       # Scripts de mantenimiento y smoke tests
├── soluciones/                    # 💻 Soluciones completas de cada unidad
│   ├── UD01_python_profesional/   # Solución ejecutable UD01
│   ├── UD02_servicios_ia_locales/ # Solución ejecutable UD02
│   ├── UD03_aplicaciones_rag/     # Solución ejecutable UD03
│   ├── UD04_agentes_inteligentes/ # Solución ejecutable UD04
│   ├── UD05_apis_y_despliegue/     # Solución ejecutable UD05
│   └── UD06_proyecto_final/       # Solución ejecutable UD06
└── unidades_didacticas/           # 📄 Ficheros Markdown unificados por unidad
    ├── UD01_python_profesional.md # Guía, Evaluación y Rúbrica de la UD01
    ├── UD02_servicios_ia_locales.md # Guía, Evaluación y Rúbrica de la UD02
    ├── UD03_aplicaciones_rag.md   # Guía, Evaluación y Rúbrica de la UD03
    ├── UD04_agentes_inteligentes.md # Guía, Evaluación y Rúbrica de la UD04
    ├── UD05_apis_y_despliegue.md   # Guía, Evaluación y Rúbrica de la UD05
    └── UD06_proyecto_final.md     # Guía, Evaluación y Rúbrica de la UD06
```

---

## 🛠️ Despliegue de la Infraestructura del Aula

Para desplegar los servicios locales preparados para el alumnado (Ollama, PostgreSQL/ChromaDB):

```bash
cd profesorado/infraestructura/profesor
cp .env.example .env
docker compose up -d
```

---

## 🧪 Pruebas de Funcionamiento

Para verificar que todos los servicios y soluciones están operativos, ejecuta el script de comprobación:

```bash
python profesorado/scripts/smoke_test.py
```
