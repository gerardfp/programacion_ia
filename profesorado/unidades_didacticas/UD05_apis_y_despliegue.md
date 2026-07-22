# UD05 - Guía Docente y Evaluación: APIs, Contenedores y Operación

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 20 horas  
**Resultado de Aprendizaje:** RA5 - Publica, conteneriza y monitoriza APIs y servicios de IA.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Publicar modelos de IA locales mediante servicios API REST asíncronos en FastAPI.
- Construir imágenes de contenedor delgadas y seguras aprovechando `uv` en Dockerfiles multi-stage.
- Orquestar despliegues reproducibles con Docker Compose conectando la API con el servidor Ollama y bases de datos.
- Aplicar prácticas operativas: variables de entorno (`.env`), health checks, límites de recursos y logs de producción.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Motor Docker & Docker Compose (v2+):** Servidor Linux (Ubuntu Server / Debian) con el demonio de Docker configurado.
- **Registro de Imágenes Local (Opcional):** Docker Registry privado en la red local (`puerto 5000`) si se desea practicar la subida/descarga de imágenes creadas por el alumnado.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (20 horas)

#### **Sesión 1-4 (4 horas): Exposición de Servicios de IA con FastAPI**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* De prototipo a producción: Exponiendo modelos de IA mediante APIs REST.
  - *Diapositiva 2:* FastAPI y documentación interactiva con Swagger UI.
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD05_apis_y_despliegue/UD05_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Principios de arquitectura REST, asincronía (`async/await`) en FastAPI y Swagger UI (`/docs`).
  2. **Actividad a realizar:** `UD05_03_actividad_inicial.md` (Creación de un servidor FastAPI básico que exponga un endpoint `/health` y `/predict`).

#### **Sesión 5-8 (4 horas): Contenerización Profesional con Docker y `uv`**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Contenerización profesional con Docker y `uv`.
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Anatomía de un `Dockerfile` optimizado utilizando imágenes base `python:3.11-slim` y la binaria de `uv`.
  2. **Práctica Guiada (Parte 1):** Inicio de `UD05_04_practica_guiada.md` sobre `starter/`. Construcción de la imagen Docker de la API con `docker build`.

#### **Sesión 9-12 (4 horas): Orquestación Multi-servicio con Docker Compose**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Orquestación de microservicios con Docker Compose.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Estructura de `compose.yaml`: definición de servicios (`api`, `ollama`, `postgres`), redes aisladas y volúmenes persistentes.
  2. **Práctica Guiada (Parte 2):** Completar `UD05_04_practica_guiada.md`. Lanzamiento del stack completo mediante `docker compose up -d`.

#### **Sesión 13-16 (4 horas): Operativa, Health Checks y Variables de Entorno (`.env`)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Buenas prácticas operativas: Healthchecks, variables `.env` y monitorización.
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Configuración de `healthcheck` en Docker Compose para asegurar que la API espere a que Ollama esté totalmente listo.
  2. **Práctica Autónoma:** Desarrollo de `UD05_05_practica_autonoma.md` (Contenerización y despliegue multi-servicio completo).

#### **Sesión 17-20 (4 horas): Reto de Ampliación, Monitorización de Logs y Evaluación**
- **Desarrollo de la Sesión:**
  1. **Reto de Ampliación:** Trabajo en `UD05_06_reto_ampliacion.md` (Incorporación de límites de recursos de memoria/CPU y script de backup de volúmenes).
  2. Inspección de contenedores y evaluación de entregas frente a `profesorado/soluciones/UD05_apis_y_despliegue/`.

---

### ⚠️ Errores Frecuentes del Alumnado
- Incluir archivos `.venv` o datos pesados dentro del contexto de construcción de Docker (falta de `.dockerignore`).
- Exponer credenciales o claves privadas dentro del `Dockerfile` en lugar de pasarlas mediante archivo `.env`.
- No configurar la IP `0.0.0.0` en uvicorn (`--host 0.0.0.0`), haciendo que la API solo escuche dentro del propio contenedor y sea inaccesible.
- Olvidar la propiedad `depends_on` con `condition: service_healthy` en Docker Compose.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **API REST Operativa:** Servidor FastAPI desplegado exponiendo documentación OpenAPI.
- **Dockerfile Optimizado:** Uso de `uv` e imágenes reducidas sin secretos embebidos.
- **Orquestación Docker Compose:** Archivo `compose.yaml` funcional con `docker compose up`.

---

## 3. Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **API FastAPI & OpenAPI** | Endpoints bien estructurados, validación Pydantic estricta y Swagger completo. | API funcional exponiendo endpoints de inferencia. | Endpoints con errores de validación o fallos ocasionales. | Servidor no arranca o carece de endpoints. |
| **Contenerización Docker** | Dockerfile optimizado con `uv`, variables de entorno y HEALTHCHECK. | Imagen Docker funcional. | Dockerfile pesado o sin optimización de capas. | Fallo al construir la imagen Docker. |
| **Orquestación Compose** | Stack multi-servicio enlazado mediante redes y volúmenes persistentes. | Docker Compose arranca los servicios principales. | Fallos de red entre contenedores. | Archivo `compose.yaml` no funcional. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD05_apis_y_despliegue/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD05_apis_y_despliegue) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD05_apis_y_despliegue/UD05_03_actividad_inicial/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD05_apis_y_despliegue/UD05_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD05_apis_y_despliegue/UD05_04_practica_guiada/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD05_apis_y_despliegue/UD05_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD05_apis_y_despliegue/UD05_05_practica_autonoma/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD05_apis_y_despliegue/UD05_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD05_apis_y_despliegue/UD05_06_reto_ampliacion/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD05_apis_y_despliegue/UD05_06_reto_ampliacion)
