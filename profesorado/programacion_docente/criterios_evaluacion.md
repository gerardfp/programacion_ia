# Criterios de Evaluación y Ponderación

## 1. Ponderación de Evidencias

| Categoría de Evidencia | Ponderación Global |
|---|---:|
| **Prácticas Técnicas y Guiadas (UD1 - UD4 / Labs UD01 - UD04)** | 35 % |
| **Proyectos de Unidad / Retos de Consolidación** | 20 % |
| **Cuestionarios de Comprensión y Control Individual de Código** | 15 % |
| **Proyecto Final Integrador y Defensa Técnica (Proyecto Integrador / UD05)** | 25 % |
| **Documentación, Git y Calidad del Código** | 5 % |

---

## 2. Requisitos Mínimos de Aprobación

> [!IMPORTANT]
> **Principio de Verificación y Comprensión:**  
> **La competencia profesional se evidencia mediante artefactos técnicos verificables (código, tests, logs) y mediante la capacidad del alumnado para interpretarlos, modificarlos y justificarlos.**  
> El alumnado podrá ser evaluado sobre implementaciones deliberadamente incompletas o defectuosas, debiendo identificar el problema, explicar su impacto, aplicar la corrección y verificar mediante pruebas que el sistema cumple los controles establecidos.

1. **Ejecutabilidad y Reproducibilidad:** El código debe arrancar y ejecutar sin errores en un entorno limpio mediante `docker compose up` o `uv run pytest`, con archivo de bloqueo `uv.lock`.
2. **Ausencia de Credenciales Explícitas y Gestión de Secretos:** Prohibición absoluta de claves, tokens o contraseñas duras en el código fuente; uso estricto de variables de entorno (`.env` ignorado en Git).
3. **Privacidad Local y Soberanía:** No emitir tráfico ni datos corporativos fuera de la red local sin autorización expresa.
4. **Validación Estricta de Esquemas (Contratos):** Todo endpoint o salida propuesta por el modelo debe validarse mediante contratos de datos estructurados para permitir validar las salidas antes de ser procesadas por la lógica de la aplicación.
5. **Control de Acceso en la Recuperación:** La recuperación debe filtrar en origen según los permisos del usuario para impedir que información no autorizada sea recuperada y alcance el contexto del modelo.
6. **Ejecución Segura y Auditoría de Herramientas:** Aplicar el principio de que a mayor impacto, mayor control requerido (validación, reglas de negocio, autorización y registro de auditoría), con confirmación explícita en acciones con consecuencias (pedidos simulados).
7. **Evaluación de Fiabilidad sobre Dataset Cerrado:** Medición de recuperación (*Hit Rate @ k*) y superación de la lista operacional de comprobación sobre el conjunto cerrado de 20 casos de prueba.
8. **Defensa Técnica Oral:** Superación del protocolo individual (2 min de presentación, 6 min respondiendo a 3 preguntas aleatorias del banco docente de 12 cuestiones de arquitectura y seguridad, y 2 min de discusión técnica).

---

## 3. Rúbrica Oficial de Evaluación (Escala Formal de 3 Niveles)

| Criterio de Evaluación | Ponderación | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|:---:|---|---|---|
| **Contratos y Validación de Datos (UD1 / UD4)** | **20 %** | Identifica la necesidad de tipado estricto e interpreta, modifica y verifica contratos estructurados con Pydantic que permiten validar las salidas antes de ser procesadas por la lógica de aplicación, gestionando errores sin caídas. | Interpreta contratos básicos de datos pero muestra inconsistencias en la verificación de errores de formato. | No identifica el riesgo de procesar texto libre sin validar o es incapaz de interceptar y corregir salidas no conformes antes de transferirlas a la lógica de aplicación. |
| **Recuperación, Control de Acceso y Grounding (UD2 / Catálogo)** | **25 %** | Explica cómo la recuperación filtra en origen según los permisos del usuario; verifica que información no autorizada no sea recuperada ni alcance el contexto del modelo y valida respuestas y citas mediante pruebas sobre dataset cerrado. | Interpreta la recuperación sobre fuentes provistas pero con inconsistencias en el control de acceso o citas incompletas. | No identifica la ausencia de filtros de acceso en la consulta de recuperación o acepta como válidas respuestas no respaldadas por las fuentes recuperadas. |
| **Tool Calling y Acciones Controladas (UD3 / CRM)** | **20 %** | Identifica y justifica la necesidad de validación, reglas de negocio y autorización en el flujo de herramientas, e interpreta, adapta y verifica una implementación que las aplica con auditoría y confirmación en pedidos. | Interpreta herramientas básicas pero no diferencia el impacto de las operaciones o carece de confirmación o registro estructurado. | No detecta ni corrige consultas no parametrizadas o es incapaz de aplicar los controles de validación, autorización o confirmación requeridos ante operaciones con consecuencias. |
| **API Contracts, Seguridad y Fallos (UD4)** | **15 %** | Interpreta y verifica contratos de red en FastAPI, asegurando que las credenciales están aisladas en entorno y que el servicio responde con códigos semánticos y respuestas estructuradas de error o contingencia. | API funcional con gestión elemental de errores y variables de entorno básicas. | No identifica ni corrige la exposición de credenciales, omite contratos formales de red o no gestiona las excepciones del servicio ante demoras o caídas. |
| **Defensa Técnica y Transferencia (Proyecto Integrador)** | **20 %** | Justifica las decisiones de arquitectura adoptadas en el caso cerámico, identifica las responsabilidades del LLM y de la aplicación, interpreta el código de integración y demuestra mediante pruebas que los controles funcionan. | Explica el funcionamiento general de la solución cerámica pero muestra dudas conceptuales ante cuestiones de seguridad o arquitectura. | Incapaz de justificar las decisiones de diseño adoptadas, confunde las responsabilidades de seguridad o atribuye autoridad autónoma al modelo de lenguaje. |
