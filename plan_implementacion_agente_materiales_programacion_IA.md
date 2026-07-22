# Plan de implementación de un agente generador de materiales didácticos

## Módulo profesional: Programación de Inteligencia Artificial

**Duración de referencia:** 110 horas  
**Enfoque:** local-first, software libre, aprendizaje basado en proyectos y despliegue en la infraestructura del centro.

---

## 1. Propósito del plan

Este documento define la implementación de un agente capaz de diseñar, generar, revisar, mantener y versionar los materiales didácticos del módulo **Programación de Inteligencia Artificial**.

El agente no debe limitarse a producir apuntes. Debe actuar como un sistema coordinado de:

- diseño curricular;
- diseño instruccional;
- generación de materiales;
- generación de prácticas y proyectos;
- generación de código de ejemplo;
- diseño de evaluación;
- validación técnica;
- adaptación de dificultad;
- mantenimiento anual del curso.

El planteamiento adopta las siguientes restricciones:

- Prioridad para software libre y servicios locales.
- Sin dependencia obligatoria de OpenAI, Azure, AWS, GCP, Power BI u otros servicios privativos.
- Posibilidad de que el profesorado despliegue previamente los servicios más complejos.
- Progresión posterior para que el alumnado aprenda a instalar, configurar y mantener esos mismos servicios.
- Uso de repositorios Git como formato principal de entrega y mantenimiento.
- Separación clara entre materiales del alumnado, materiales del profesorado, soluciones e infraestructura.

---

## 2. Objetivos generales

El agente deberá permitir que el profesorado pueda:

1. Generar una programación docente completa y coherente con el currículo.
2. Crear unidades didácticas temporizadas.
3. Generar teoría, ejemplos, prácticas, proyectos, evaluaciones y rúbricas.
4. Adaptar los materiales a diferentes perfiles de entrada: DAM, DAW, ASIR, STI, Mecatrónica o Automatización.
5. Ajustar el nivel de dificultad sin rehacer el curso desde cero.
6. Mantener una infraestructura educativa reproducible.
7. Versionar los materiales por curso académico.
8. Actualizar tecnologías concretas sin perder la alineación curricular.
9. Evitar dependencias innecesarias de servicios externos.
10. Producir materiales accesibles, trazables y revisables.

---

## 3. Alcance funcional del agente

El agente deberá generar y mantener, como mínimo, los siguientes productos:

```text
Programacion_IA/
├── README.md
├── programacion_docente/
│   ├── programacion_general.md
│   ├── resultados_aprendizaje.md
│   ├── criterios_evaluacion.md
│   ├── temporalizacion.md
│   └── mapa_competencias.md
├── unidades_didacticas/
│   ├── UD01_python_profesional/
│   ├── UD02_servicios_ia_locales/
│   ├── UD03_aplicaciones_rag/
│   ├── UD04_agentes_inteligentes/
│   ├── UD05_apis_y_despliegue/
│   └── UD06_proyecto_final/
├── teoria/
├── presentaciones/
├── practicas/
├── proyectos/
├── evaluacion/
├── rubricas/
├── soluciones_profesor/
├── codigo_ejemplo/
├── datasets/
├── infraestructura/
├── docker/
├── scripts/
├── plantillas/
└── curso_2026_2027/
```

---

## 4. Principios de diseño

### 4.1. Local-first

Todos los servicios principales deberán poder ejecutarse dentro de la infraestructura del centro.

Tecnologías recomendadas:

- Python.
- FastAPI.
- PostgreSQL.
- Ollama o servidor de inferencia local equivalente.
- Modelos abiertos descargados previamente.
- ChromaDB, Qdrant o PostgreSQL con extensión vectorial.
- Sentence Transformers.
- PyTorch.
- OpenCV.
- Streamlit o Gradio.
- Grafana y/o Apache Superset.
- Docker y Docker Compose.
- GitLab o Gitea.
- JupyterHub, cuando resulte útil.

### 4.2. Progresión de autonomía

El aprendizaje deberá seguir esta secuencia:

1. **Uso de servicios preparados por el profesorado.**
2. **Integración de servicios en aplicaciones.**
3. **Despliegue guiado por el alumnado.**
4. **Diseño autónomo de arquitecturas.**
5. **Operación, monitorización y documentación.**

### 4.3. Separación entre aprendizaje de IA y administración

La infraestructura no debe convertirse en una barrera inicial. En las primeras unidades el profesorado podrá facilitar:

- endpoints ya disponibles;
- modelos ya descargados;
- bases de datos inicializadas;
- imágenes Docker preparadas;
- credenciales educativas limitadas;
- repositorios plantilla.

En unidades posteriores, el alumnado deberá reproducir parcialmente o por completo esos despliegues.

### 4.4. Materiales reproducibles

Toda práctica deberá poder ejecutarse:

- desde un repositorio limpio;
- con dependencias declaradas;
- con datos de ejemplo;
- con instrucciones completas;
- sin pasos implícitos;
- con una solución verificable;
- con una versión conocida del entorno.

### 4.5. Evaluación auténtica

La evaluación deberá centrarse en productos funcionales:

- APIs;
- aplicaciones;
- pipelines;
- servicios contenerizados;
- documentación;
- pruebas;
- decisiones técnicas;
- explicaciones de seguridad, privacidad y ética.

---

## 5. Información de entrada para el agente

Antes de generar el curso, el agente deberá solicitar o recibir una ficha de contexto.

### 5.1. Datos curriculares

```yaml
modulo:
  nombre: Programación de Inteligencia Artificial
  duracion_horas: 110
  codigo: 5073

resultados_aprendizaje:
  - Caracteriza lenguajes de programación para IA.
  - Desarrolla aplicaciones de IA.
  - Evalúa la convergencia tecnológica.
  - Evalúa modelos de automatización industrial y de negocio.
```

### 5.2. Perfil del alumnado

```yaml
alumnado:
  procedencias:
    - DAM
    - DAW
    - ASIR
  conocimientos_previos:
    python: basico
    bases_datos: medio
    redes: basico
    linux: basico
    docker: no_iniciado
```

### 5.3. Infraestructura

```yaml
infraestructura:
  sistema_operativo: Ubuntu Server
  ram_gb: 64
  gpu:
    disponible: true
    modelo: NVIDIA
  docker: true
  acceso_internet:
    profesor: true
    alumnado: restringido
  servicios_disponibles:
    - GitLab
    - JupyterHub
    - PostgreSQL
    - Ollama
    - Grafana
```

### 5.4. Restricciones

```yaml
restricciones:
  servicios_pago: false
  cuentas_externas_obligatorias: false
  datos_fuera_del_centro: false
  software_libre_prioritario: true
  acceso_gpu_compartido: true
```

### 5.5. Preferencias docentes

```yaml
preferencias:
  metodologia: aprendizaje_basado_en_proyectos
  trabajo:
    individual: 40
    parejas: 30
    equipos: 30
  evaluacion_continua: true
  proyecto_final: true
  formato_materiales: markdown
```

---

## 6. Arquitectura del agente

Se propone una arquitectura multiagente coordinada.

```text
                         Coordinador
                              |
       ------------------------------------------------
       |                   |               |          |
Agente curricular   Agente pedagógico  Agente técnico  Agente evaluación
       |                   |               |          |
       ---------------- Generador de unidad ----------------
                              |
                   Validador de coherencia
                              |
                     Repositorio Git
```

### 6.1. Agente coordinador

Responsabilidades:

- recibir la ficha de contexto;
- dividir el trabajo;
- mantener coherencia global;
- resolver conflictos entre decisiones;
- controlar versiones;
- generar el índice maestro;
- impedir duplicidades;
- verificar la cobertura horaria.

### 6.2. Agente curricular

Responsabilidades:

- mapear contenidos con resultados de aprendizaje;
- relacionar actividades con criterios de evaluación;
- asegurar la cobertura del currículo;
- generar el mapa de trazabilidad;
- controlar que ningún criterio quede sin evidencia evaluable.

Salida principal:

```text
resultado de aprendizaje
→ unidad didáctica
→ actividad
→ evidencia
→ instrumento de evaluación
```

### 6.3. Agente pedagógico

Responsabilidades:

- secuenciar contenidos;
- ajustar dificultad;
- diseñar andamiaje;
- generar actividades iniciales, guiadas y autónomas;
- prever errores frecuentes;
- generar adaptaciones;
- diseñar trabajo individual y cooperativo.

### 6.4. Agente técnico

Responsabilidades:

- seleccionar tecnologías;
- crear código;
- definir arquitecturas;
- generar Dockerfiles;
- generar `compose.yaml`;
- comprobar dependencias;
- crear datos sintéticos;
- redactar instrucciones de despliegue;
- proponer alternativas para CPU y GPU.

### 6.5. Agente de evaluación

Responsabilidades:

- diseñar rúbricas;
- generar pruebas prácticas;
- elaborar listas de cotejo;
- definir evidencias;
- crear pruebas automáticas;
- establecer mínimos;
- preparar recuperación y ampliación.

### 6.6. Agente revisor

Responsabilidades:

- detectar incoherencias;
- comprobar que el material del alumnado no contiene soluciones;
- comprobar que las soluciones son ejecutables;
- revisar accesibilidad;
- comprobar tiempos;
- revisar seguridad;
- detectar dependencias externas no autorizadas;
- validar enlaces internos y estructura.

---

## 7. Flujo de generación

### Fase 1. Inicialización

1. El profesorado completa la ficha de contexto.
2. El agente valida los datos.
3. Se fijan las decisiones tecnológicas.
4. Se genera un manifiesto del curso.
5. Se crea la estructura del repositorio.

Archivo recomendado:

```text
course-manifest.yaml
```

Ejemplo:

```yaml
curso: 2026-2027
modulo: Programacion de Inteligencia Artificial
horas: 110
lenguaje_principal: Python
backend: FastAPI
llm_local: Ollama
base_datos: PostgreSQL
base_vectorial: ChromaDB
despliegue: Docker Compose
visualizacion:
  - Streamlit
  - Grafana
```

### Fase 2. Diseño macro

El agente genera:

- programación docente;
- temporalización;
- mapa de resultados de aprendizaje;
- unidades;
- proyectos;
- estrategia de evaluación;
- calendario de despliegue de servicios.

### Fase 3. Generación por unidad

Para cada unidad se generan:

```text
UDXX/
├── 00_indice.md
├── 01_guia_profesor.md
├── 02_material_alumno.md
├── 03_presentacion.md
├── 04_actividad_inicial.md
├── 05_practica_guiada.md
├── 06_practica_autonoma.md
├── 07_reto_ampliacion.md
├── 08_evaluacion.md
├── 09_rubrica.md
├── starter/
└── solucion/
```

### Fase 4. Validación

El agente ejecuta comprobaciones:

- cobertura curricular;
- suma de horas;
- coherencia entre teoría y práctica;
- dependencias;
- ejecución del código;
- construcción de contenedores;
- separación alumno/profesor;
- licencias;
- protección de datos;
- accesibilidad documental.

### Fase 5. Revisión docente

El profesorado aprueba, rechaza o modifica:

- tecnologías;
- carga de trabajo;
- dificultad;
- entregables;
- pesos de evaluación;
- alcance del proyecto final.

### Fase 6. Publicación

El sistema crea una versión etiquetada:

```text
v2026.1
```

y genera dos distribuciones:

```text
release-alumnado/
release-profesorado/
```

---

## 8. Diseño actualizado del módulo

## Unidad 1. Desarrollo profesional en Python para IA

**Duración:** 15 horas

### Objetivos

- Convertir prototipos en software mantenible.
- Organizar proyectos Python.
- Usar tipado, validación y registro.
- Crear pruebas.
- Gestionar dependencias.
- Utilizar Git.

### Contenidos

- Estructura de paquetes.
- Entornos virtuales.
- `pyproject.toml`.
- Tipado.
- Pydantic.
- Excepciones.
- Logging.
- Pruebas con pytest.
- Git y ramas.
- Documentación de proyecto.

### Prácticas

1. Refactorización de un notebook.
2. Creación de un paquete Python.
3. Pruebas de una función de inferencia.
4. Validación de entradas con Pydantic.

### Infraestructura

No requiere servicios previos complejos.

### Evidencia evaluable

Repositorio con:

- código estructurado;
- pruebas;
- documentación;
- gestión de dependencias.

---

## Unidad 2. Servicios de IA locales

**Duración:** 15 horas

### Objetivos

- Comprender la arquitectura cliente-servidor.
- Consumir modelos locales.
- Gestionar parámetros de inferencia.
- Diseñar respuestas estructuradas.
- Comparar modelos.

### Contenidos

- Inferencia local.
- API HTTP.
- Modelos de lenguaje.
- Plantillas de instrucciones.
- Salida estructurada.
- Límites de contexto.
- Latencia.
- Uso de CPU y GPU.
- Registro de peticiones.

### Fase inicial

El profesorado despliega:

```text
Ollama
modelo local
proxy interno
```

El alumnado consume el servicio.

### Fase posterior

El alumnado:

- instala el servicio en un entorno aislado;
- descarga o importa un modelo autorizado;
- configura persistencia;
- publica el endpoint;
- documenta recursos y limitaciones.

### Prácticas

1. Cliente Python para un LLM local.
2. Generación de JSON validado.
3. Comparación de dos modelos.
4. Medición de latencia y consumo.

### Evidencia evaluable

Aplicación cliente con:

- control de errores;
- validación;
- logs;
- informe comparativo.

---

## Unidad 3. Aplicaciones RAG locales

**Duración:** 25 horas

### Objetivos

- Construir un asistente documental.
- Extraer y fragmentar documentos.
- Generar embeddings.
- Realizar búsqueda semántica.
- Incorporar fuentes en las respuestas.
- Evaluar calidad.

### Contenidos

- Ingesta documental.
- División de texto.
- Metadatos.
- Embeddings locales.
- Bases vectoriales.
- Recuperación.
- Generación aumentada.
- Evaluación de respuestas.
- Alucinaciones.
- Control de acceso.
- Actualización del índice.

### Infraestructura inicial

El profesorado puede dejar preparados:

- Ollama;
- ChromaDB o Qdrant;
- modelo de embeddings;
- conjunto documental;
- repositorio inicial.

### Infraestructura final

El alumnado deberá generar un `compose.yaml` con:

```text
app
ollama
vector_db
postgres
```

### Prácticas

1. Ingesta de documentos.
2. Búsqueda semántica.
3. RAG mínimo.
4. Interfaz de consulta.
5. Evaluación con preguntas de referencia.

### Evidencia evaluable

Asistente documental local con:

- referencias;
- filtrado por metadatos;
- registro;
- evaluación;
- documentación.

---

## Unidad 4. Agentes inteligentes y automatización

**Duración:** 15 horas

### Objetivos

- Diferenciar chatbot, flujo y agente.
- Definir herramientas.
- Conectar con bases de datos.
- Controlar acciones.
- Mantener trazabilidad.
- Diseñar límites de autonomía.

### Contenidos

- Tool calling.
- Flujos de estados.
- Memoria.
- Planificación limitada.
- Consultas SQL seguras.
- Confirmación de acciones.
- Auditoría.
- Prevención de bucles.
- Límites de permisos.

### Proyecto de unidad

Agente que:

1. recibe una petición;
2. decide si necesita una consulta;
3. ejecuta una herramienta autorizada;
4. procesa el resultado;
5. genera un informe;
6. registra todas las acciones.

### Infraestructura

Inicialmente:

- PostgreSQL preparado;
- datos de ejemplo;
- servicio LLM operativo.

Posteriormente:

- el alumnado crea la base;
- define permisos;
- despliega el agente;
- añade auditoría.

### Evidencia evaluable

Agente con al menos dos herramientas y registro completo.

---

## Unidad 5. APIs, contenedores y operación

**Duración:** 20 horas

### Objetivos

- Publicar modelos y aplicaciones.
- Crear APIs REST.
- Contenerizar servicios.
- Gestionar configuración.
- Monitorizar.
- Aplicar seguridad básica.

### Contenidos

- FastAPI.
- OpenAPI.
- Autenticación básica.
- Variables de entorno.
- Gestión de secretos.
- Dockerfile.
- Docker Compose.
- Volúmenes.
- Redes.
- Health checks.
- Logs.
- Métricas.
- Proxy inverso.
- Copias de seguridad.

### Prácticas

1. API de inferencia.
2. Dockerización.
3. Despliegue multi-servicio.
4. Monitorización.
5. Gestión de fallos.
6. Copia y restauración.

### Evidencia evaluable

Servicio desplegado, documentado y monitorizado.

---

## Unidad 6. Proyecto final

**Duración:** 20 horas

### Objetivo

Integrar los aprendizajes del módulo en una solución empresarial funcional.

### Requisitos mínimos

- IA local.
- Backend.
- Datos persistentes.
- Interfaz.
- API.
- Docker Compose.
- Pruebas.
- Logs.
- Documentación.
- Análisis de seguridad, privacidad y ética.

### Entregables

```text
proyecto/
├── README.md
├── docs/
├── src/
├── tests/
├── data_sample/
├── Dockerfile
├── compose.yaml
├── .env.example
├── LICENSE
└── memoria_tecnica.md
```

---

## 9. Proyectos de referencia

### Proyecto 1. Asistente documental privado

Caso:

Una organización necesita consultar normativa, manuales o documentación interna sin sacar los datos del centro.

Tecnologías:

- FastAPI.
- Ollama.
- ChromaDB o Qdrant.
- Sentence Transformers.
- Streamlit.
- Docker Compose.

### Proyecto 2. Copiloto para soporte técnico

Funciones:

- clasificar incidencias;
- recuperar soluciones;
- sugerir pasos;
- registrar decisiones;
- escalar casos.

### Proyecto 3. Agente de análisis empresarial

Funciones:

- consultar PostgreSQL;
- calcular indicadores;
- generar gráficos;
- redactar un informe;
- mantener auditoría.

### Proyecto 4. Inspección visual local

Funciones:

- recibir imágenes;
- ejecutar inferencia;
- marcar incidencias;
- almacenar resultados;
- mostrar métricas.

Tecnologías:

- OpenCV.
- PyTorch.
- modelo de visión abierto.
- FastAPI.
- Grafana.

---

## 10. Estrategia de despliegue progresivo

| Etapa | Responsable principal | Servicios |
|---|---|---|
| Inicio | Profesorado | Git, Ollama, base de datos, Jupyter |
| Integración | Compartida | API, embeddings, vector DB |
| Despliegue guiado | Alumnado | App y servicios en Docker |
| Proyecto final | Alumnado | Arquitectura completa |
| Operación | Alumnado | Logs, métricas, copias y documentación |

### 10.1. Modo profesorado

El agente debe generar:

```text
infraestructura/profesor/
├── compose.yaml
├── .env.example
├── init-db/
├── modelos.md
├── backup.md
├── restore.md
└── troubleshooting.md
```

### 10.2. Modo alumnado

El agente debe generar retos graduales:

- completar un Dockerfile;
- conectar dos servicios;
- crear un volumen;
- definir un health check;
- limitar recursos;
- configurar una red;
- desplegar un stack completo.

---

## 11. Plantilla de unidad didáctica

Cada unidad deberá incluir:

```markdown
# Título de la unidad

## Duración

## Resultados de aprendizaje

## Criterios de evaluación

## Requisitos previos

## Objetivos

## Conceptos clave

## Secuencia de sesiones

## Actividad inicial

## Explicación teórica

## Demostración

## Práctica guiada

## Práctica autónoma

## Reto de ampliación

## Evidencias

## Instrumentos de evaluación

## Errores frecuentes

## Adaptaciones

## Recursos del profesor

## Checklist de publicación
```

---

## 12. Plantilla de práctica

```markdown
# Práctica: título

## Contexto profesional

## Objetivos

## Duración estimada

## Requisitos

## Infraestructura disponible

## Enunciado

## Restricciones

## Tareas

## Entregables

## Criterios de aceptación

## Pruebas mínimas

## Rúbrica

## Ampliaciones

## Ayuda escalonada
```

La ayuda escalonada deberá organizarse en:

1. pista conceptual;
2. pista técnica;
3. fragmento parcial;
4. solución completa exclusiva del profesorado.

---

## 13. Generación de código

El agente deberá crear tres niveles de código.

### 13.1. Starter

Incluye estructura, contratos y TODOs.

### 13.2. Referencia

Incluye una solución mínima y clara para el profesorado.

### 13.3. Producción educativa

Incluye:

- tipado;
- validación;
- logs;
- pruebas;
- configuración;
- documentación;
- seguridad básica.

El agente deberá evitar:

- credenciales embebidas;
- rutas absolutas;
- dependencias no declaradas;
- código sin control de errores;
- ejemplos que requieran una cuenta externa;
- uso de datos personales reales.

---

## 14. Datasets

El agente deberá priorizar:

- datos sintéticos;
- datos públicos con licencia compatible;
- datos anonimizados;
- conjuntos pequeños para prácticas;
- versiones reducidas para CPU;
- versiones ampliadas para GPU.

Cada dataset deberá incluir:

```text
dataset/
├── README.md
├── LICENSE
├── schema.json
├── sample.csv
└── data_dictionary.md
```

---

## 15. Evaluación

### 15.1. Propuesta de ponderación

| Evidencia | Peso |
|---|---:|
| Prácticas técnicas | 35 % |
| Proyecto de unidad | 20 % |
| Pruebas individuales | 15 % |
| Proyecto final | 25 % |
| Documentación y profesionalidad | 5 % |

### 15.2. Dimensiones de las rúbricas

- Funcionamiento.
- Calidad del código.
- Arquitectura.
- Pruebas.
- Documentación.
- Seguridad.
- Privacidad.
- Explicación técnica.
- Reproducibilidad.
- Trabajo en equipo.

### 15.3. Rúbrica base

| Nivel | Descripción |
|---|---|
| 4. Excelente | Funciona, está probado, documentado, es reproducible y justifica decisiones. |
| 3. Adecuado | Cumple los requisitos principales con errores menores. |
| 2. En desarrollo | Funciona parcialmente o presenta carencias relevantes. |
| 1. Insuficiente | No cumple los mínimos o no puede reproducirse. |

### 15.4. Mínimos obligatorios

No podrá superarse una entrega si:

- no arranca;
- no existe README;
- contiene credenciales;
- depende de un servicio externo no autorizado;
- no incluye código fuente;
- no permite reproducir el resultado;
- incumple las reglas de tratamiento de datos.

---

## 16. Pruebas automáticas del material

El agente deberá generar una canalización de validación.

```text
lint
→ tests
→ build image
→ start services
→ health checks
→ smoke tests
→ stop services
```

Herramientas posibles:

- Ruff.
- Pytest.
- MyPy.
- Docker Compose.
- scripts de smoke test.
- GitLab CI.

Ejemplo conceptual:

```yaml
stages:
  - lint
  - test
  - build
  - integration

lint:
  script:
    - ruff check src tests

test:
  script:
    - pytest

build:
  script:
    - docker build -t app-ia .

integration:
  script:
    - docker compose up -d
    - python scripts/smoke_test.py
    - docker compose down
```

---

## 17. Seguridad y privacidad

El agente debe comprobar que los materiales incluyan:

- datos sintéticos o autorizados;
- minimización de datos;
- control de acceso;
- separación de roles;
- variables de entorno;
- protección de secretos;
- validación de entradas;
- límites de tamaño;
- registros sin datos sensibles;
- copias de seguridad;
- eliminación segura;
- revisión de sesgos;
- explicación de limitaciones.

Para agentes con herramientas:

- lista blanca de herramientas;
- consultas parametrizadas;
- permisos mínimos;
- confirmación antes de acciones destructivas;
- auditoría de cada acción;
- límite de iteraciones;
- timeout;
- control de errores.

---

## 18. Accesibilidad

El agente deberá generar materiales que:

- utilicen encabezados jerárquicos;
- eviten depender únicamente del color;
- incluyan texto alternativo para diagramas;
- proporcionen transcripciones;
- utilicen lenguaje claro;
- separen instrucciones y contexto;
- permitan navegación por teclado en interfaces;
- incluyan ejemplos legibles;
- ofrezcan formatos alternativos cuando sea necesario.

---

## 19. Adaptación por perfil de entrada

### DAM y DAW

Refuerzo en:

- APIs;
- arquitectura;
- testing;
- interfaces;
- despliegue.

### ASIR

Refuerzo en:

- Python;
- diseño de software;
- APIs;
- tratamiento de datos.

Aprovechamiento de:

- Linux;
- redes;
- servicios;
- contenedores.

### Automatización y Mecatrónica

Refuerzo en:

- programación;
- bases de datos;
- APIs.

Contextos prioritarios:

- sensores;
- mantenimiento predictivo;
- visión;
- alarmas;
- procesos industriales.

---

## 20. Adaptación de dificultad

Cada actividad deberá generarse en tres niveles.

### Básico

- pasos detallados;
- infraestructura preparada;
- código inicial abundante;
- dataset pequeño.

### Estándar

- requisitos funcionales;
- código inicial limitado;
- decisiones técnicas guiadas.

### Avanzado

- requisitos abiertos;
- despliegue propio;
- métricas;
- seguridad;
- comparación de alternativas.

---

## 21. Flujo de uso durante el curso

### Antes del curso

1. Configurar contexto.
2. Generar versión inicial.
3. Validar infraestructura.
4. Probar prácticas.
5. Crear cuentas.
6. Publicar materiales iniciales.

### Durante el curso

El profesorado podrá pedir al agente:

- reducir una práctica;
- crear una versión de recuperación;
- generar pistas;
- producir un dataset alternativo;
- cambiar una tecnología;
- crear una prueba individual;
- adaptar una actividad a CPU;
- generar una rúbrica específica.

### Después del curso

1. Recoger incidencias.
2. Analizar tiempos reales.
3. Registrar errores frecuentes.
4. archivar entregas de ejemplo;
5. actualizar dependencias;
6. generar la versión siguiente.

---

## 22. Versionado

Se recomienda:

```text
curso-2026.1
curso-2026.2
curso-2027.1
```

Cada versión deberá incluir un changelog:

```markdown
# Changelog

## 2026.2

- Reducida la práctica RAG de 8 a 6 horas.
- Sustituida la base vectorial.
- Añadidos tests de integración.
- Creada variante sin GPU.
```

---

## 23. Criterios de aceptación del agente

El sistema se considerará válido cuando:

1. Genere el repositorio completo.
2. Cubra las 110 horas.
3. Relacione todas las actividades con el currículo.
4. Genere materiales separados para alumnado y profesorado.
5. Produzca código ejecutable.
6. Genere despliegues locales.
7. No requiera servicios de pago.
8. Incluya pruebas y rúbricas.
9. Genere una variante CPU.
10. Documente seguridad y privacidad.
11. Permita regenerar una unidad sin alterar las demás.
12. Mantenga un historial de cambios.
13. Genere un proyecto final completo.
14. Permita revisión humana antes de publicar.

---

## 24. Hoja de ruta de implementación del agente

### Fase 1. Prototipo mínimo

Objetivo:

Generar una unidad completa a partir de una plantilla.

Entregables:

- esquema de entrada;
- plantilla de unidad;
- generador Markdown;
- práctica;
- rúbrica;
- solución;
- validación básica.

### Fase 2. Generación curricular completa

Objetivo:

Generar las seis unidades y la programación docente.

Entregables:

- mapa curricular;
- temporalización;
- unidades;
- evaluación;
- proyecto final.

### Fase 3. Generación técnica

Objetivo:

Crear repositorios ejecutables.

Entregables:

- starters;
- soluciones;
- Docker;
- tests;
- datasets;
- scripts.

### Fase 4. Validación automática

Objetivo:

Comprobar que los materiales funcionan.

Entregables:

- CI;
- pruebas;
- validación de enlaces;
- construcción de imágenes;
- smoke tests.

### Fase 5. Interfaz docente

Objetivo:

Permitir regenerar y adaptar materiales.

Funciones:

- seleccionar unidad;
- variar dificultad;
- cambiar duración;
- cambiar tecnología;
- generar recuperación;
- exportar alumnado/profesorado.

### Fase 6. Mantenimiento

Objetivo:

Actualizar el curso sin perder trazabilidad.

Funciones:

- diff entre versiones;
- actualización de dependencias;
- registro de incidencias;
- migración tecnológica;
- archivo anual.

---

## 25. Stack sugerido para implementar el agente

### Núcleo

- Python.
- Pydantic.
- FastAPI.
- Jinja2.
- Git.

### Orquestación

- Flujo basado en estados.
- Tareas idempotentes.
- Salidas estructuradas.
- Validadores independientes.

### Persistencia

- PostgreSQL para metadatos.
- Repositorio Git para materiales.
- Almacenamiento local para artefactos.

### Ejecución segura

- Contenedores aislados.
- Límites de CPU y memoria.
- Sin acceso libre a la red.
- Directorios temporales.
- Registro de ejecución.

### Modelos

- LLM local.
- Modelo pequeño para tareas rutinarias.
- Modelo mayor para diseño y revisión.
- Embeddings locales para consultar currículo y materiales previos.

---

## 26. Modelo de datos mínimo

```yaml
Course:
  id: string
  academic_year: string
  duration: integer
  constraints: object
  infrastructure: object

Unit:
  id: string
  title: string
  hours: integer
  learning_outcomes: list
  assessment_criteria: list
  dependencies: list

Activity:
  id: string
  type: string
  duration: integer
  difficulty: string
  evidence: list
  rubric_id: string

Artifact:
  path: string
  audience: student|teacher
  version: string
  checksum: string
```

---

## 27. Prompts funcionales del sistema

### Generación de unidad

```text
Genera una unidad didáctica alineada con los resultados de aprendizaje
indicados. Usa únicamente tecnologías permitidas. La duración total debe
coincidir con las horas asignadas. Incluye teoría, práctica guiada,
práctica autónoma, evaluación, rúbrica, starter y solución.
```

### Revisión técnica

```text
Revisa el repositorio como responsable técnico. Comprueba dependencias,
seguridad, reproducibilidad, variables de entorno, pruebas, Docker y
ausencia de servicios externos no autorizados.
```

### Revisión pedagógica

```text
Revisa la progresión cognitiva, los conocimientos previos, el tiempo,
las ayudas, la carga de trabajo y la correspondencia entre actividad
y evidencia evaluable.
```

### Adaptación

```text
Adapta esta práctica a alumnado sin experiencia previa en Docker.
Conserva los mismos resultados de aprendizaje y criterios de evaluación.
Reduce la carga de administración sin eliminar la competencia de despliegue.
```

---

## 28. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Material generado pero no ejecutable | Pruebas automáticas obligatorias |
| Exceso de contenido | Presupuesto horario por unidad |
| Dependencias externas | Lista blanca tecnológica |
| Soluciones filtradas al alumnado | Builds separados |
| Cambios de versiones | Lockfiles e imágenes versionadas |
| Saturación de GPU | Modelos pequeños, colas y cuotas |
| Alumnado bloqueado por infraestructura | Servicios preparados al inicio |
| Pérdida de aprendizaje técnico | Despliegue progresivo posterior |
| Material genérico | Contextos empresariales y criterios de aceptación |
| Evaluación superficial | Evidencias funcionales y defensa técnica |

---

## 29. Resultado final esperado

Al finalizar la implantación se dispondrá de:

- un agente generador de materiales;
- un repositorio vivo del módulo;
- una infraestructura local reproducible;
- materiales diferenciados;
- prácticas ejecutables;
- evaluación trazable;
- proyectos empresariales;
- versiones CPU y GPU;
- despliegue progresivo;
- documentación de operación;
- un proceso anual de mejora.

El alumnado finalizará el módulo siendo capaz de:

- desarrollar aplicaciones de IA;
- consumir e integrar modelos locales;
- crear APIs;
- construir sistemas RAG;
- desarrollar agentes con herramientas;
- contenerizar servicios;
- desplegar soluciones;
- monitorizar aplicaciones;
- documentar arquitecturas;
- aplicar criterios de seguridad, privacidad y ética.

---

## 30. Checklist de puesta en marcha

### Currículo

- [ ] Resultados de aprendizaje cargados.
- [ ] Criterios de evaluación mapeados.
- [ ] Temporalización validada.
- [ ] Instrumentos de evaluación definidos.

### Infraestructura

- [ ] Docker instalado.
- [ ] Repositorio Git operativo.
- [ ] Base de datos disponible.
- [ ] Servicio de inferencia local operativo.
- [ ] Modelo de embeddings disponible.
- [ ] Copias de seguridad configuradas.
- [ ] Cuotas de recursos definidas.

### Materiales

- [ ] Guías de profesor.
- [ ] Materiales de alumnado.
- [ ] Prácticas.
- [ ] Soluciones.
- [ ] Rúbricas.
- [ ] Datasets.
- [ ] Código inicial.
- [ ] Proyecto final.

### Validación

- [ ] Código probado.
- [ ] Contenedores construidos.
- [ ] Health checks correctos.
- [ ] Enlaces revisados.
- [ ] Dependencias fijadas.
- [ ] Licencias documentadas.
- [ ] Revisión de privacidad.
- [ ] Revisión de accesibilidad.

### Publicación

- [ ] Release del alumnado.
- [ ] Release del profesorado.
- [ ] Etiqueta de versión.
- [ ] Changelog.
- [ ] Plan de recuperación.
- [ ] Registro de incidencias.
