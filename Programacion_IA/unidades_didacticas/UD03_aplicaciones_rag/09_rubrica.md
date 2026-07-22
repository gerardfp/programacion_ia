# UD03 - Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Pipeline RAG** | Ingesta, chunking, embeddings y ChromaDB integrados a la perfección. | Pipeline funcional con respuestas contextualmente correctas. | Ingesta parcial o fallos en la recuperación vectorial. | No recupera contexto ni conecta con la base vectorial. |
| **Citación y Alucinaciones** | Cita fuentes exactas y evita alucinaciones cuando no hay contexto. | Muestra las fuentes de información. | Alucina respuestas ignorando el contexto recuperado. | Sin control de alucinación ni fuentes. |
| **Persistencia** | Colección ChromaDB persistente en disco correctamente estructurada. | Persistencia funcional en disco. | Colección volátil exclusivamente en memoria. | Error en almacenamiento de vectores. |
