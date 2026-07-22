# Resultados de Aprendizaje (RA)

## RA1. Caracteriza lenguajes de programación y entornos de desarrollo para Inteligencia Artificial
- Organiza la estructura de paquetes y entornos virtuales en Python.
- Aplica tipado estático, validación de datos con Pydantic y registro de logs.
- Diseña pruebas unitarias e integración con `pytest`.
- Gestiona el control de versiones con Git y flujos de trabajo estructurados.

## RA2. Integra y consume servicios y modelos locales de IA
- Describe la arquitectura cliente-servidor de inferencia en LLMs locales.
- Consume servicios como Ollama mediante peticiones HTTP/REST y librerías cliente en Python.
- Diseña prompts y genera respuestas estructuradas en formato JSON.
- Evalúa métricas de latencia, consumo de memoria/CPU/GPU y límites de contexto.

## RA3. Desarrolla aplicaciones RAG (Retrieval-Augmented Generation) locales
- Extrae, limpia y fragmenta documentos en diversos formatos (.pdf, .md, .txt).
- Genera embeddings semánticos utilizando modelos locales (Sentence Transformers).
- Almacena e indexa vectores en bases de datos (ChromaDB / PostgreSQL pgvector).
- Construye un pipeline completo de consulta semántica, recuperación y generación documentada.

## RA4. Construye agentes inteligentes con ejecución de herramientas y automatización
- Diferencia flujos deterministas, chatbots sencillos y agentes autónomos con *tool calling*.
- Conecta agentes con bases de datos relacionales ejecutando consultas parametrizadas seguras.
- Diseña mecanismos de trazabilidad, auditoría, memoria conversacional y límites de autonomía.

## RA5. Publica, conteneriza y monitoriza APIs y servicios de IA
- Desarrolla APIs REST avanzadas con FastAPI exponiendo endpoints de inferencia e ingesta.
- Conteneriza aplicaciones y dependencias empleando Docker y Dockerfiles optimizados.
- Orquesta stacks multi-servicio (API, Ollama, DB, Vector DB) mediante Docker Compose.
- Configura health checks, métricas y gestión de secretos con `.env`.

## RA6. Desarrolla e integra un proyecto final empresarial de IA
- Integra modelos locales, backend FastAPI, base de datos vectorial/relacional e interfaz de usuario.
- Implementa suites de prueba, integración continua local y documentación técnica completa.
- Evalúa aspectos de seguridad, privacidad (GDPR local) y sesgos éticos.
