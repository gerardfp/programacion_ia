# Resultados de Aprendizaje (RA)

## RA1. Caracteriza lenguajes de programación y entornos de desarrollo para Inteligencia Artificial
- Organiza la estructura de paquetes y entornos virtuales en Python con `uv`.
- Aplica tipado estático, validación de datos con Pydantic y registro de logs.
- Diseña pruebas unitarias e integración con `pytest`.
- Gestiona el control de versiones con Git y flujos de trabajo estructurados.

## RA2. Consume servicios y modelos locales de IA mediante contratos de datos verificables
- Describe los fundamentos de la comunicación HTTP esencial (petición/respuesta, códigos de estado) hacia un endpoint local de chat provisto por el servicio de inferencia.
- Estructura diálogos formales mediante mensajes tipados y roles (`system`, `user`, `assistant`) y gestiona los límites de la ventana de contexto (*context window*) y los efectos de contextos excesivamente grandes.
- Aplica técnicas formales de *Prompt Engineering* (delimitadores, plantillas parametrizadas) e interioriza el fenómeno de las alucinaciones, la falta de garantía de veracidad factual y la necesidad del anclaje (*grounding*).
- Establece la abstención como parte del contrato de comportamiento y verifica si el modelo cumple la convención ante falta de información.
- Define y verifica contratos de datos estructurados: el modelo propone una estructura JSON según un esquema y el software valida y tipa los datos mediante esquemas Pydantic (`model_validate_json`).
- Observa el comportamiento de inferencia en tiempo real mediante streaming (demostración de Server-Sent Events).

## RA3. Desarrolla aplicaciones RAG con control de acceso en la consulta y evaluación medible
- Aplica higiene previa al particionado (descarte de documentos corruptos, normalización UTF-8) y asocia metadatos de control de acceso (departamento, nivel de acceso).
- Genera embeddings consumiendo la API de inferencia local (`str` $\rightarrow$ `list[float]`) y comprende la noción de distancia semántica en espacios vectoriales.
- Almacena vectores en PostgreSQL con `pgvector` e implementa el principio de seguridad en recuperación: *la consulta de recuperación incorpora las condiciones de acceso autorizadas para el usuario, de modo que los fragmentos no autorizados no forman parte del resultado entregado a la aplicación*.
- Diseña prompts con inyección delimitada de contexto y obligación de citación estricta de fuentes.
- Evalúa el sistema sobre un dataset cerrado de casos conocidos aplicando la lista operacional de comprobación: recuperación (*Hit Rate @ k*), información requerida, ausencia de datos no respaldados, abstención controlada y citas válidas.

## RA4. Implementa Tool Calling y ejecución segura de herramientas con autorización proporcional
- Aplica el ciclo de 5 fases del Harness: 1. Validación sintáctica (Pydantic), 2. Reglas de negocio (dominio), 3. Autorización, 4. Ejecución segura, 5. Registro de auditoría.
- Modela herramientas realistas sobre el dominio de negocio (consultas de lectura vs mutaciones de estado).
- Aplica una política de autorización y confirmación proporcional al impacto de la operación, distinguiendo acciones automatizables de bajo impacto de operaciones destructivas o críticas que exigen confirmación (*Human-in-the-Loop*).
- Diseña herramientas con garantías de idempotencia para asegurar el estado final relevante ante reintentos por cortes de red.
- Previene activamente la inyección de SQL garantizando que cuando una herramienta acceda a base de datos relacional, utilice consultas parametrizadas (`cursor.execute(sql, (param,))`).
- Previene bucles infinitos y consumo excesivo estableciendo límites explícitos de iteraciones y timeouts en el bucle de ejecución.
- Conecta herramientas a un servidor *Model Context Protocol* (MCP) de demostración para comprender el desacoplamiento estándar de servicios.

## RA5. Expone APIs con contratos explícitos, seguridad integral y robustez básica ante fallos
- Desarrolla servicios con FastAPI definiendo contratos formales de API (*API Contracts*) con esquemas Pydantic para peticiones y respuestas tipadas (incluyendo citas y métricas), con códigos de estado HTTP semánticos.
- Comprende el rol de la concurrencia y asincronía para no bloquear el bucle de eventos durante esperas de red I/O.
- Aplica la cuádruple frontera de seguridad partiendo de la identidad autenticada disponible en la aplicación (`current_user`) para evaluar la autorización en la aplicación, el control de acceso a datos y las reglas de negocio.
- Aplica el principio de seguridad ante Prompt Injection: *los delimitadores no son una barrera mágica y el prompt no es un mecanismo de autorización*; la protección reside en la arquitectura exterior.
- Clasifica y gestiona errores con robustez básica: fallos de contrato (422), violaciones de negocio (400/422), autorización (403) y timeouts de inferencia (504 con fallbacks estructurados).
- Asegura las credenciales mediante variables de entorno en `.env` excluidas del repositorio Git.

## RA6. Desarrolla, verifica y defiende un proyecto final empresarial de IA
- Integra el AI Harness sobre un *Starter Kit* docente con infraestructura provista (Docker Compose con Ollama y PostgreSQL) y andamiaje de base de datos e identidad.
- Implementa la lógica nuclear: RAG con filtros de permisos en la query, herramientas seguras con validación de negocio y contratos de API.
- Aplica pruebas automatizadas con `pytest` y evalúa el comportamiento del sistema frente a un dataset cerrado mediante la lista operacional de comprobación.
- Interpreta visualmente trazas de latencia en la herramienta de observabilidad provista para diagnosticar cuellos de botella (retrieval vs. LLM vs. herramientas).
- Defiende técnicamente ante un tribunal la solución desarrollada, respondiendo a preguntas aleatorias de un banco docente sobre arquitectura, estocasticidad y gestión de fallos.
