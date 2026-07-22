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
└── unidades_didacticas/           # Recursos didácticos del docente
    └── UDXX_nombre/
        ├── 00_indice.md           # Índice y resumen docente
        ├── 01_guia_profesor.md    # Orientaciones metodológicas y andamiaje
        ├── 08_evaluacion.md       # Instrumentos e instrucciones de evaluación
        ├── 09_rubrica.md          # Rúbricas analíticas de evaluación
        └── solucion/              # Solución funcional completa de los retos y prácticas
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
uv run python profesorado/scripts/smoke_test.py
```
