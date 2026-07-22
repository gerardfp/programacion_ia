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

### Secuencia de Sesiones (20 horas)
1. **Sesión 1-4 (4h):** Desarrollo de endpoints REST en FastAPI con validación Pydantic.
2. **Sesión 5-8 (4h):** Creación de Dockerfiles eficientes integrando `uv` y gestión de usuarios no root.
3. **Sesión 9-12 (4h):** Orquestación multi-servicio en Docker Compose (`compose.yaml`).
4. **Sesión 13-16 (4h):** Health checks, variables de entorno y secreto de configuración.
5. **Sesión 17-20 (4h):** Pruebas de integración, smoke tests y monitorización de contenedores.

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

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD05_apis_y_despliegue/`
