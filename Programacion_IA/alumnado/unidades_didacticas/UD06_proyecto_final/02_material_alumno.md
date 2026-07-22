# UD06 - Guía del Proyecto Final para el Alumnado

## 🎯 Objetivo

Desarrollar un sistema completo de Inteligencia Artificial para un caso de uso real empresarial en local.

## 📋 Requisitos Mínimos Obligatorios

1. **Inferencia Local:** Integración con Ollama (`llama3.2` o equivalente).
2. **Backend API:** Exposición de endpoints REST mediante `FastAPI`.
3. **Persistencia Vectorial / Relacional:** Uso de `ChromaDB` para RAG o `PostgreSQL` para almacenamiento.
4. **Contenerización Total:** Archivo `compose.yaml` funcional que arranque todo el sistema con `docker compose up`.
5. **Calidad de Software:** Pruebas unitarias con `pytest` y validación de tipos con `Pydantic`.
6. **Memoria Técnica y Licencias:** Documento explicativo de la arquitectura, decisiones de diseño y privacidad (GDPR local).
