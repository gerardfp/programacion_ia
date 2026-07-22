# UD05 - Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **API FastAPI & OpenAPI** | Endpoints bien estructurados, validación Pydantic estricta y Swagger completo. | API funcional exponiendo endpoints de inferencia. | Endpoints con errores de validación o fallos ocasionales. | Servidor no arranca o carece de endpoints. |
| **Contenerización Docker** | Dockerfile optimizado con `uv`, variables de entorno y HEALTHCHECK. | Imagen Docker funcional. | Dockerfile pesado o sin optimización de capas. | Fallo al construir la imagen Docker. |
| **Orquestación Compose** | Stack multi-servicio enlazado mediante redes y volúmenes persistentes. | Docker Compose arranca los servicios principales. | Fallos de red entre contenedores. | Archivo `compose.yaml` no funcional. |
