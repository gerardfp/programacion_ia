# 📋 Propuesta de Diseño Curricular y Proyecto Integrador: Programación de Inteligencia Artificial (5073)

**Destinatario:** Dirección del Módulo y Comisión de Coordinación Pedagógica  
**Módulo:** Programación de Inteligencia Artificial (5073) — Modalidad Intensiva  
**Carga Horaria:** 50 horas lectivas (40 h Aprendizaje de Patrones + 10 h Proyecto Integrador)  
**Carácter del Documento:** Propuesta de diseño curricular, delimitación de responsabilidades y estándares de fiabilidad 
---

## 1. Enfoque del Módulo: De la Escritura de Sintaxis a la Ingeniería de Integración y Verificación

El módulo se plantea como una **introducción práctica al desarrollo de aplicaciones que integran inteligencia artificial generativa**, con especial atención a los patrones y problemas habituales de las aplicaciones basadas en Modelos de Lenguaje (LLMs).

El objetivo no es que el alumnado aprenda a desarrollar modelos de inteligencia artificial desde cero, ni evaluar su capacidad memorística para teclear de memoria sintaxis de librerías. En el contexto del desarrollo de software actual, el objetivo formativo se define con precisión:

> **Tesis Central del Curso:**  
> **Formar a un programador capaz de integrar IA generativa entendiendo las decisiones de ingeniería que hacen que esa integración sea segura, controlable y verificable.**  
>  
> *«No se enseña al alumno a construir ni entrenar un LLM; se le enseña a programar aplicaciones que integran LLM y a construir las fronteras de responsabilidad y control alrededor de ellos.»*

### Principios Rectores: La Tríada de Responsabilidades del Módulo
Toda la arquitectura del curso y la delimitación de responsabilidades se fundamenta en tres principios explícitos:

> [!IMPORTANT]
> **La Tríada de Responsabilidades:**
> 1. **El LLM propone; la aplicación gobierna la decisión y la ejecución.**  
>    El modelo genera sugerencias o borradores de datos y acciones; la aplicación gobierna la autorización, el estado y las operaciones con consecuencias.
> 2. **El LLM interpreta; la aplicación calcula.**  
>    El modelo procesa lenguaje y extrae intenciones o parámetros; **las operaciones deterministas que afectan al estado o a los resultados de negocio se delegan en software verificable**, como cálculos matemáticos, tarifas, disponibilidad o reglas de pedido. El modelo puede **extraer o interpretar** magnitudes expresadas por el usuario (por ejemplo, metros cuadrados), pero las operaciones que determinan cantidades económicas o estado del sistema se realizan mediante lógica determinista de la aplicación.
> 3. **La aplicación verifica lo que el LLM propone.**  
>    El software no debe confiar ciegamente en la salida del modelo: valida esquemas mediante contratos, comprueba reglas de dominio y exige confirmación humana en operaciones de impacto relevante.

Ante una línea de código como:
```python
result = llm.generate(messages, response_format=OrderData)
```
el alumno no debe limitarse a teclear la llamada; debe ser capaz de interrogar la arquitectura:
* *¿Por qué se fuerza una salida estructurada?*
* *¿Qué ocurre si el modelo devuelve una estructura no conforme y dónde se intercepta?*
* *¿Quién valida y quién decide si los datos son admisibles para el negocio?*
* *¿Qué información ha recibido el modelo en el contexto y tenía este usuario permiso para consultarla?*
* *¿Qué parte calcula el precio y las cantidades económicas?*
* *¿Qué prueba automatizada demuestra que el control de seguridad realmente existe y funciona?*

---

### Evidencias Evaluables: Artefactos Técnicos y Comprensión

Dado que el código de partida puede ser suministrado por el profesorado, generado por el alumno o producido con asistentes de IA, la competencia profesional no se mide por la autoría sintáctica original, sino por dos principios docentes cardinales:

> **La competencia profesional se evidencia mediante artefactos técnicos verificables y mediante la capacidad del alumnado para interpretarlos, modificarlos y justificarlos.**

> [!IMPORTANT]
> **Principio de Responsabilidad sobre el Código:**  
> *«La procedencia del código —profesorado, alumnado o herramienta de IA— no determina su valor educativo. Sin embargo, quien lo utiliza debe ser capaz de interpretar su funcionamiento, identificar sus riesgos, modificarlo cuando proceda y aportar evidencias de que cumple los requisitos establecidos. La delegación de la escritura no implica la delegación de la responsabilidad técnica.»*

Esta distinción delimita con nitidez dos planos complementarios e inseparables de evaluación:

1. **Artefactos Técnicos (Resultados y Evidencias de Ejecución):**
   - **Código adaptado y configurado:** Esquemas de datos Pydantic, parametrización de consultas y despacho gobernado de herramientas.
   - **Pruebas automatizadas (`pytest`):** Suites de tests que provocan deliberadamente fallos, desbordamientos o intentos de elusión para comprobar que los controles interceptan el error.
   - **Trazas y registros de ejecución:** Logs estructurados (*Audit Log*) y telemetría (Langfuse) que documentan empíricamente el comportamiento del sistema en tiempo de ejecución.

2. **Comprensión y Justificación Técnica (Evidencias de Dominio):**
   - **Explicación técnica:** Capacidad de razonar qué hace cada componente, por qué está implementado de esa forma y qué riesgo neutraliza.
   - **Defensa técnica ante preguntas de arquitectura:** Capacidad de responder ante preguntas docentes sobre caídas de red, latencias, saturación de la ventana de contexto o compromisos de seguridad.

> *«Si el alumno utiliza herramientas de IA para generar código o pruebas, la evaluación no se invalida: la evidencia reside en su capacidad para auditar esos artefactos, explicar sus decisiones de diseño, corregir omisiones de seguridad y demostrar mediante la defensa técnica que comprende la arquitectura.»*

---

### El Ciclo Metodológico de Aprendizaje (7 Etapas)

Para materializar este enfoque, el aprendizaje se organiza en torno a un ciclo progresivo de **siete etapas**, que separa deliberadamente la comprensión conceptual previa de la manipulación del código y de la verificación del comportamiento en tiempo de ejecución:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ 1. ACTIVIDAD    │  ──►  │ 2. CUESTIONARIO │  ──►  │ 3. PRÁCTICA     │
│    INICIAL      │       │    CONCEPTUAL   │       │    GUIADA       │
│                 │       │                 │       │                 │
│ Presentación    │       │ Comprobación de │       │ Interpretación  │
│ del problema y  │       │ conceptos y     │       │ y manipulación  │
│ contexto        │       │ responsabilidades│      │ de una solución │
└─────────────────┘       └─────────────────┘       └────────┬────────┘
                                                              │
                                                              ▼
                                                     ┌─────────────────┐
                                                     │ 4. CUESTIONARIO │
                                                     │    DE           │
                                                     │    COMPRENSIÓN  │
                                                     │                 │
                                                     │ Comprobación de │
                                                     │ la comprensión  │
                                                     │ de la solución  │
                                                     └────────┬────────┘
                                                              │
                                                              ▼
                                                     ┌─────────────────┐
                                                     │ 5. MODIFICACIÓN │
                                                     │    Y ADAPTACIÓN │
                                                     │                 │
                                                     │ Corrección o    │
                                                     │ ampliación de   │
                                                     │ la solución     │
                                                     └────────┬────────┘
                                                              │
                                                              ▼
                                                     ┌─────────────────┐
                                                     │ 6. PRUEBA       │
                                                     │    AUTOMATIZADA │
                                                     │                 │
                                                     │ Tests positivos │
                                                     │ y negativos     │
                                                     └────────┬────────┘
                                                              │
                                                              ▼
                                                     ┌─────────────────┐
                                                     │ 7. EVIDENCIA    │
                                                     │    Y DEFENSA    │
                                                     │                 │
                                                     │ Resultados,     │
                                                     │ trazas y        │
                                                     │ justificación   │
                                                     └─────────────────┘
```

#### Descripción de las 7 Etapas del Ciclo:

1. **Actividad inicial:** Se presenta un problema contextualizado y se plantea la necesidad técnica o de negocio que debe resolver la tecnología o patrón correspondiente. El objetivo es situar el problema antes de introducir cualquier línea de código.
2. **Cuestionario conceptual (*¿He comprendido el problema?*):** Se comprueba individualmente que el alumnado comprende el problema, los conceptos fundamentales, las responsabilidades de cada componente y los principales riesgos antes de abordar la implementación.
3. **Práctica guiada:** Se trabaja sobre código proporcionado por el profesorado (*starter kit*), desarrollado por el alumnado o generado mediante herramientas de IA. El alumnado interpreta la implementación y aprende a identificar dónde se materializan los conceptos estudiados.
4. **Cuestionario de comprensión (*¿Entiendo lo que acabo de hacer?*):** Se comprueba individualmente que el alumnado comprende la implementación que acaba de utilizar, incluyendo el propósito de sus componentes, el flujo de ejecución y las consecuencias de eliminar o modificar determinados controles.
5. **Modificación y adaptación:** El alumnado modifica la implementación para introducir un requisito nuevo, corregir un defecto deliberado o adaptar el comportamiento a un escenario ampliado de forma autónoma y fundamentada.
6. **Prueba automatizada:** Diseña, adapta y ejecuta pruebas con `pytest` para verificar tanto comportamientos nominales como casos de error e intentos de elusión de controles.
7. **Evidencia y defensa técnica:** Aporta los resultados de las pruebas, las trazas o registros pertinentes (*audit log* / observabilidad) y justifica técnicamente las decisiones adoptadas ante el docente.

---

### La Función Dual de los Cuestionarios y la Verificación de la Comprensión

Los dos cuestionarios no son exámenes memorísticos tradicionales, sino **puntos de control formativo con funciones netamente diferenciadas**:

* **Cuestionario 1 (Conceptual — Previo al Código):**  
  Evalúa si el alumno comprende el *por qué* antes de ver el *cómo*:
  - *¿Qué ventajas aporta RAG frente a incluir directamente grandes cantidades de información en el contexto del modelo?*
  - *¿Por qué no basta con enviar la pregunta directamente al LLM?*
  - *¿Dónde debe aplicarse el control de acceso a los datos y qué riesgo introduce filtrar en memoria a posteriori?*
  - *¿Qué responsabilidad corresponde al LLM y cuál a la lógica de la aplicación?*

* **Cuestionario 2 (Comprensión de Implementación — Posterior al Código):**  
  Evalúa si el alumno comprende la materialización técnica que acaba de manipular:
  - *¿Qué función cumple la validación mediante Pydantic y qué ocurre si falla?*
  - *¿En qué punto exacto se aplica el filtro de permisos en la consulta SQL?*
  - *¿Qué ocurriría en el sistema si eliminamos esa condición de control?*
  - *¿Por qué el precio o las cantidades no las calcula el LLM?*
  - *¿Qué test unitario demostraría que un usuario sin permisos no obtiene el documento privado?*

> [!TIP]
> **Verificación de la Comprensión y Responsabilidad Técnica sobre el Código:**  
> Esta secuencia de doble verificación desacopla la autoría del código de la competencia profesional. Si un estudiante presenta un código funcional generado con un asistente de IA pero es incapaz de responder en el Cuestionario 2 qué ocurre si se elimina una condición o cómo fluye una excepción, queda en evidencia que **la existencia de código funcional no equivale a comprensión ingenieril**. La evaluación desplaza, por tanto, el foco desde la autoría del código hacia la responsabilidad técnica sobre el resultado, evitando que la generación automática de código pueda sustituir la comprensión y la capacidad de verificación del alumnado.

---

## 2. El AI Harness: Mecanismos de Control Distribuidos

Como principio transversal se introduce el concepto de **AI Harness**: un patrón arquitectónico materializado en el software que media entre el modelo de lenguaje y las capacidades de la aplicación, gobernando la información que recibe el modelo y las acciones que este puede solicitar.

> [!NOTE]
> **Definición Arquitectónica:**  
> **El término Harness no describe una librería externa ni un componente monolítico cerrado, sino el conjunto distribuido de mecanismos de software que median y gobiernan la interacción entre el modelo y las capacidades de la aplicación.**

```text
                    LLM
                     ↕ (propuestas / texto)
        ┌─────────────────────────────┐
        │         AI HARNESS          │
        │                             │
        │ Validación · Autorización   │
        │ Control de acceso · Reglas  │
        │ Límites · Auditoría         │
        └─────────────────────────────┘
             ↕            ↕          ↕
           datos        tools       APIs

                 ─────────────
                  EVALUACIÓN
                 ─────────────
                 tests + dataset
```

> *El Harness representa conceptualmente un conjunto de mecanismos distribuidos en diferentes componentes de la aplicación; no implica necesariamente una única clase o servicio. El Harness es, por tanto, la materialización software de las fronteras de responsabilidad que separan las capacidades probabilísticas del LLM de las decisiones deterministas y controladas de la aplicación.*

Bajo este enfoque, el objetivo del alumno no es *"construir un framework de AI Harness desde cero"*, sino:
> **Saber reconocer qué controles debe contener una aplicación cuando incorpora un LLM, justificar por qué son necesarios y comprobar mediante pruebas que esos controles están realmente implementados y activos.**

Si se le presenta el despachador de herramientas:
```python
tool_call = llm_response.tool_call
args = ToolArgs.model_validate(tool_call.arguments)

if not authorization.can_execute(user, tool_call.name):
    raise Forbidden("Usuario no autorizado para esta acción")

if not business_rules.is_valid(tool_call.name, args):
    raise BusinessRuleError("Violación de reglas de dominio")

result = tools[tool_call.name](args)
audit.log(user, tool_call.name, args, result)
```
el alumno debe comprender la secuencia de control y ser capaz de anticipar qué riesgo se introduce si se elimina una sola pieza (ej. *«si se elimina `authorization`, la aplicación podría ejecutar una operación solicitada por el modelo sin comprobar que el usuario actual está autorizado para realizarla»*).

---

## 3. Jerarquización Pedagógica: Analizar, Aplicar/Verificar y Reconocer

Para estructurar de forma realista las 50 horas lectivas, se adopta una **taxonomía de tres niveles de desempeño profesional**:

1. **Analizar:** El alumno identifica el problema que resuelve una técnica, explica por qué aparece en la arquitectura, reconoce sus límites y riesgos, y **distingue claramente las responsabilidades del LLM y de la aplicación**.
2. **Aplicar y verificar:** El alumno trabaja sobre una implementación existente o generada por IA: puede configurarla, modificarla, ejecutarla, inspeccionar su comportamiento en tiempo de ejecución, **escribir y ejecutar pruebas que demuestren que los controles funcionan**, e identificar errores de diseño.
3. **Reconocer:** Conoce la existencia, terminología y finalidad de tecnologías complementarias (Docker, HNSW, MCP, Langfuse, modelos multimodales), interpretando su presencia en el sistema sin necesidad de modificarlas en profundidad.

> [!IMPORTANT]
> **Declaración de Principio Docente y Metodología:**  
> **El módulo no pretende evaluar la capacidad del alumnado para memorizar y reproducir desde cero implementaciones de tecnologías concretas. Se evalúa su capacidad para comprender decisiones de ingeniería, interpretar implementaciones existentes o generadas con herramientas de IA, identificar riesgos y responsabilidades, modificar configuraciones o código cuando sea necesario y verificar mediante pruebas que el sistema cumple los controles establecidos.**  
>  
> **Las actividades podrán partir de código proporcionado por el profesorado, código generado por el propio alumnado o código generado mediante herramientas de IA.** El foco de la actividad no será la autoría del código, sino la capacidad para interpretar su funcionamiento, detectar decisiones incorrectas, modificarlo cuando proceda y aportar evidencias de que cumple los requisitos establecidos.  
>  
> **El alumnado podrá ser evaluado sobre implementaciones deliberadamente incompletas o defectuosas, debiendo identificar el problema, explicar su impacto y proponer o aplicar la corrección adecuada.**

| Concepto / Componente | Nivel | Desempeño Evaluado en el Aula |
|---|:---:|---|
| **Estructuración de Mensajes y Roles** | **Aplicar y verificar** | Interpreta y adapta listas de mensajes tipados (`system`, `user`, `assistant`) y gestiona el contexto. |
| **Contratos y Validación (Pydantic)** | **Aplicar y verificar** | Interpreta y adapta esquemas `BaseModel`, intercepta salidas estructuradas y comprueba que permiten validar las salidas antes de ser procesadas por la lógica de aplicación. |
| **RAG y Filtros de Acceso** | **Aplicar y verificar** | Interpreta y adapta consultas de recuperación para filtrar en origen según condiciones de acceso e impedir que datos no autorizados sean recuperados y alcancen el contexto. |
| **Tool Calling y Despacho Seguro** | **Aplicar y verificar** | Inspecciona el flujo de llamadas a herramientas, comprueba validación e incorpora o adapta reglas de negocio. |
| **Autorización y Confirmación (HITL)** | **Aplicar y verificar** | Verifica que las acciones críticas exigen confirmación explícita antes de ejecutarse en el sistema. |
| **Auditoría Básica (Audit Log)** | **Aplicar y verificar** | Comprueba que las acciones ejecutadas dejan constancia estructurada (timestamp, usuario, acción, resultado). |
| **API Contracts con FastAPI** | **Aplicar y verificar** | Interpreta y adapta endpoints `/query` y `/health` verificando esquemas Request/Response y códigos HTTP. |
| **Testing con `pytest`** | **Aplicar y verificar** | Ejecuta y adapta suites de pruebas unitarias sobre validadores y reglas de negocio. |
| **Prevención de SQL Injection** | **Aplicar y verificar** | Identifica concatenaciones inseguras en herramientas, comprueba y aplica consultas parametrizadas y verifica mediante pruebas que se neutralizan entradas maliciosas. |
| **Evaluación sobre Dataset Cerrado** | **Aplicar y verificar** | Ejecuta scripts de evaluación de aula comprobando recuperación (*Hit Rate*) y correspondencia con las fuentes. |
| **Idempotencia** | **Analizar** | Explica cómo la idempotencia permite que la repetición de una operación ante caídas de red produzca el mismo estado relevante, distinguiendo idempotente de inocuo. |
| **Timeouts y Fallbacks** | **Analizar** | Justifica la necesidad de capturar demoras del modelo devolviendo respuestas estructuradas de error o contingencia. |
| **Límites de la Ventana de Contexto** | **Analizar** | Explica las consecuencias del desbordamiento o saturación del contexto y sus efectos sobre la respuesta del modelo. |
| **Docker Compose** | **Reconocer** | Comprende la composición del stack multicontenedor (PostgreSQL/pgvector, servidor LLM) y su función en la arquitectura sin requerir desarrollo de infraestructura. |
| **Índice Vectorial HNSW** | **Reconocer** | Reconoce su función como acelerador de búsqueda vectorial en PostgreSQL sin necesidad de desarrollo matemático. |
| **Model Context Protocol (MCP)** | **Reconocer** | Interpreta la demo de un servidor MCP y comprende cómo desacopla herramientas bajo un estándar abierto. |
| **Multimodalidad (Imágenes)** | **Reconocer** | Interpreta el flujo de integración y el contrato de entrada/salida del servicio de imágenes preconfigurado. |
| **Observabilidad (Langfuse)** | **Reconocer** | Lee e interpreta visualmente trazas de latencia para identificar cuellos de botella entre retrieval, LLM y tools. |

---

## 4. Tipología de Prácticas en las 40 Horas de Aprendizaje

Para asegurar que las 40 horas lectivas no se conviertan en una carrera por copiar código, las actividades se articulan en **tres tipos de ejercicios complementarios**:

```text
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│  A. CONSTRUCCIÓN GUIADA │      B. AUDITORÍA       │     C. VERIFICACIÓN     │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Código parcial / starter│ Código funcional en     │ Sistema operativo con   │
│ provisto. El alumno     │ apariencia pero con     │ controles. El alumno    │
│ completa o adapta el    │ fallos o riesgos. El    │ diseña y ejecuta tests  │
│ comportamiento.         │ alumno localiza y       │ negativos que demuestran│
│                         │ justifica el problema.  │ que el control actúa.   │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

*Ejemplo en RAG (UD2):*
1. *Construcción guiada:* Completar la consulta vectorial sobre PostgreSQL para recuperar fragmentos relevantes.
2. *Auditoría:* Se entrega un endpoint de RAG funcional pero cuya consulta no incluye las condiciones de acceso del usuario (`WHERE ... condiciones de acceso del usuario ...`). El alumno debe identificar la vulnerabilidad de fuga de datos.
3. *Verificación:* Escribir un test con `pytest` que simule un usuario sin permisos y demuestre que el sistema no entrega el documento confidencial.

---

## 5. Contenidos y Progresión Didáctica (40 Horas de Aprendizaje)

```text
  UD1 (10 h)             UD2 (12 h)             UD3 (10 h)             UD4 (8 h)
┌──────────────┐       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│Integración de│  ──►  │    RAG y     │  ──►  │ Tool Calling │  ──►  │ Integración, │
│    LLM en    │       │  Acceso al   │       │ y Acciones   │       │ Seguridad y  │
│ Aplicaciones │       │ Conocimiento │       │ Controladas  │       │   Control    │
└──────────────┘       └──────────────┘       └──────────────┘       └──────────────┘
```

### 🔹 UD1. Integración de LLM en Aplicaciones (10 horas)
Se introducen los modelos de lenguaje como componentes de software accesibles vía HTTP, comprendiendo su naturaleza stateless y la necesidad de gestión de contexto por parte de la aplicación.

* **Actividades de aplicación y verificación:**
  - De petición aislada a conversación: demostración empírica de la falta de memoria del servidor HTTP y la gestión del contexto por parte de la aplicación (del chat ingenuo con texto concatenado a mensajes estructurados con roles `system`, `user` y `assistant`).
  - Extracción y estructuración de datos: comprobación del fallo fatal al parsear texto libre con `json.loads` (*Crash & Learn*) frente al uso de modos JSON estructurados.
  - Validación de respuestas estructuradas mediante contratos Pydantic (`model_validate_json`), comprobando cómo los esquemas permiten validar las salidas antes de ser procesadas por la lógica de aplicación.
* **Aspectos de análisis:**
  - ¿Dónde reside la memoria?: comprensión de que el servidor no tiene estado persistente y que la aplicación gobierna y reenvía el contexto en cada llamada.
  - Límites de la ventana de contexto (*context window*), consumo acumulado por el historial y efectos de saturación (justificación directa de la necesidad de RAG).
  - Alucinaciones y falta de garantía de veracidad: comprender que el modelo no garantiza por sí mismo la veracidad factual ni la corrección de sus propuestas.
* **Elementos a reconocer:** Demostración de streaming (SSE) y observación de latencia total frente a tiempo hasta primer token (TTFT).

---

### 🔹 UD2. RAG y Acceso al Conocimiento (12 horas)
Se aborda la conexión del modelo con fuentes documentales externas provistas por la aplicación.

* **Actividades de aplicación y verificación:**
  - Inspección del proceso de fragmentación (*chunking*) y generación de embeddings locales.
  - Almacenamiento en PostgreSQL (`pgvector`) y ejecución de consultas de similaridad vectorial.
  - Verificación del control de acceso: **comprobar que la consulta incorpora las condiciones de acceso del usuario (filtrado en origen en la base de datos) para impedir que los datos no autorizados sean recuperados y alcancen el contexto del modelo**.
  - Evaluación sobre dataset cerrado (20-30 casos):
    - *Métricas automáticas:* Medición de *Hit Rate @ k* (proporción de casos del dataset en los que al menos uno de los fragmentos de referencia esperados aparece entre los $k$ primeros resultados recuperados) y análisis de los fragmentos recuperados.
    - *Comprobaciones operativas:* Cita correcta a la fuente, correspondencia o respaldo en las fuentes recuperadas y abstención formal ante ausencia de información.
* **Aspectos de análisis:**
  - **Grounding:** Vinculación de la respuesta con información proporcionada por las fuentes recuperadas.
  - Las citas como mecanismo de soporte y verificación para el usuario, no como garantía absoluta.
  - **La abstención como control de la aplicación:** Si la búsqueda no recupera información relevante, la aplicación emite una respuesta estructurada de abstención ("NO_DATA"), sin delegar el control en la voluntad del prompt.

---

### 🔹 UD3. Tool Calling y Acciones Controladas (10 horas)
Se introduce la interacción gobernada entre el modelo y las funciones operativas de la aplicación.

* **Modelo didáctico de referencia:**  
  > **A mayor impacto de una acción, mayor nivel de control requerido.**
  - *Lectura:* Autorización básica (`consultar_stock`).
  - *Mutación:* Autorización + Validación sintáctica + Auditoría (`actualizar_contacto`).
  - *Operación crítica:* Autorización + Reglas de negocio + Confirmación explícita (*HITL*) + Auditoría (`confirmar_pedido`).
* **Actividades de aplicación y verificación:**
  - Inspección de definiciones de herramientas con esquemas estructurados.
  - Modificación del despachador del Harness: validación de tipos con Pydantic, comprobación de reglas de dominio y verificación de permisos.
  - Prevención de SQL Injection: identificación de concatenaciones inseguras en herramientas, comprobación y aplicación de consultas parametrizadas y verificación mediante pruebas de la neutralización de entradas maliciosas.
  - Verificación de la confirmación explícita antes de ejecutar acciones de consecuencias relevantes.
  - Comprobación del registro de auditoría en log estructurado.
* **Aspectos de análisis:**
  - Idempotencia: explica cómo la idempotencia permite que la repetición de una operación ante caídas de red produzca el mismo estado relevante, distinguiendo idempotente de inocuo.
  - Límites de iteraciones en el bucle para prevenir ciclos infinitos de invocación.
* **Elementos a reconocer:** Demostración de conexión a un servidor Model Context Protocol (MCP) preconfigurado.

---

### 🔹 UD4. Integración, Seguridad y Control (8 horas)
Se integran los patrones trabajados en servicios de red completos.

* **Actividades de aplicación y verificación:**
  - Inspección y adaptación de endpoints FastAPI con contratos tipados (`QueryRequest` / `QueryResponse`).
  - Verificación de que las credenciales están aisladas en `.env` (excluido en `.gitignore`).
  - Ejecución de pruebas unitarias con `pytest` sobre validadores y reglas de negocio.
* **Aspectos de análisis:**
  - **Modelo didáctico de defensa en profundidad:** Como modelo didáctico de defensa en profundidad, se distinguen cuatro fronteras de control en la aplicación: **identidad autenticada disponible en la aplicación (`current_user`) $\rightarrow$ autorización en la aplicación $\rightarrow$ control de acceso a datos en la consulta $\rightarrow$ reglas de negocio**.
  - Seguridad ante Prompt Injection: *"el prompt no es un mecanismo de autorización"*.
  - Gestión básica de fallos: respuestas estructuradas de error o contingencia ante demoras del LLM.
* **Elementos a reconocer:**
  - Multimodalidad: interpretación del flujo de integración del servicio de renderizado de imágenes a partir de prompt y fotografía base.
  - Observabilidad: lectura de trazas visuales en Langfuse para desglosar tiempos de retrieval, LLM y tools.

---

## 6. Proyecto Final: Integración en una Empresa Cerámica (10 Horas)

Como proyecto final se plantea la integración de capacidades de IA generativa en una aplicación web de una **empresa ficticia de fabricación y comercialización de productos cerámicos del sur de Castellón** (azulejos, pavimentos y revestimientos).

### El Andamiaje de la Aplicación Base Cerámica
> [!NOTE]
> **Delimitación del Andamiaje Provisto:**  
> El andamiaje contiene implementadas las funcionalidades convencionales, los modelos de datos, los endpoints, la interfaz web, la infraestructura en Docker y **plantillas de pruebas unitarias parcialmente preparadas**.  
> El trabajo del alumnado se concentra en **interpretar, adaptar y verificar la lógica de integración de IA y sus mecanismos de control**.  
> Los endpoints de CRM y pedidos forman parte del andamiaje proporcionado y **no constituyen contenidos nuevos del proyecto**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│             APLICACIÓN WEB EMPRESA CERÁMICA (CASTELLÓN)                │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌────────────────┐ │
│   │ 1. Asistente        │  │ 2. Visualizador     │  │ 3. Asistente   │ │
│   │    Catálogo y RAG   │  │    de Ambientes     │  │    Comercial   │ │
│   │ • Fichas técnicas   │  │ • Foto de estancia  │  │    y Pedidos   │ │
│   │ • Usos y formatos   │  │ • Selección azulejo │  │ • Extracción   │ │
│   │ • Citas técnicas    │  │ • Renderizado       │  │ • Validación   │ │
│   │ • Consulta stock    │  │   multimodal guiado │  │ • Confirmación │ │
│   └─────────────────────┘  └─────────────────────┘  └────────────────┘ │
│              │                        │                      │         │
└──────────────┼────────────────────────┼──────────────────────┼─────────┘
                ▼                        ▼                      ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        AI HARNESS DEL ALUMNO                           │
│  Contratos Pydantic • Control de Acceso • Reglas de Pedido • Auditoría │
└────────────────────────────────────────────────────────────────────────┘
```

### Los 3 Subsistemas Integrados

1. **Asistente de Catálogo Técnico (RAG):**  
   Consultas sobre especificaciones de producto (pavimentos exteriores vs interiores, acabados y recomendaciones de colocación). El alumno verifica que las respuestas están respaldadas por las fuentes documentales provistas, que se citan las fichas técnicas y que la aplicación emite abstención formal ("NO_DATA") ante consultas sin documentación de respaldo. Dispone además de herramientas de consulta (`consultar_stock`, `consultar_producto`).

2. **Visualizador de Ambientes (Integración Multimodal Guiada):**  
   Permite al usuario asociar una imagen de una estancia con un producto del catálogo para generar la representación visual del espacio renovado mediante el servicio multimodal preconfigurado. El objetivo evaluable se centra estrictamente en interpretar y gestionar el contrato de la API de integración (parámetros, latencia, respuestas tipadas y manejo de errores), no en la calidad estética o artística del renderizado generado.

3. **Asistente Comercial y Pedidos Simulados:**  
   Bajo la tríada rectora del curso:
   > **El LLM interpreta; la aplicación calcula.**
   - El modelo puede extraer o interpretar del diálogo las necesidades del cliente y los metros cuadrados solicitados.
   - Invoca una herramienta determinista provista (`calcular_cajas(producto, m2)`) para que **la aplicación calcule de forma determinista el número de cajas y el importe oficial según las reglas de negocio establecidas**.
   - Presenta el resumen del pedido simulado al usuario.
   - **Exige confirmación explícita (*Human-in-the-Loop*)** antes de llamar al endpoint de registro simulado (`POST /api/orders/confirm`), dejando constancia en el log de auditoría.

---

## 7. Matriz de Transferencia de Competencias

El proyecto comprueba la capacidad de transferir patrones trabajados en prácticas independientes hacia un dominio empresarial concreto:

| Patrón Trabajado en las Prácticas (40 h) | Aplicación en el Proyecto Final Cerámico (10 h) |
|---|---|
| **Structured Output** | Extraer preferencias del cliente, metros cuadrados y datos de contacto desde el diálogo. |
| **Pydantic** | Validar rigurosamente los argumentos de pedidos y los datos del CRM antes de procesarlos. |
| **RAG** | Asistente de catálogo técnico (fichas técnicas, características de pavimentos y revestimientos). |
| **Embeddings** | Interpretación y uso de la búsqueda semántica de colecciones cerámicas por descripción de estilo o acabado. |
| **Control de Acceso** | Evitar mediante filtrado en base de datos que usuarios no autorizados recuperen documentación restringida. |
| **Tool Calling** | Consultar stock en almacén, verificar referencias y preparar borradores de pedido. |
| **Reglas de Negocio** | Verificar stock disponible y reglas de pedido de la empresa. |
| **Autorización** | Controlar qué usuarios tienen permiso para registrar pedidos en firme. |
| **Confirmación de Acciones** | Exigir confirmación explícita del cliente antes de registrar el pedido simulado. |
| **Multimodalidad** | Visualizador de ambientes: envío de imagen de estancia + producto cerámico para renderizado. |
| **Evaluación Operacional** | Comprobar respuestas del catálogo sobre el dataset cerrado de 20 casos cerámicos. |
| **Seguridad (Prompt Injection)** | Impedir que instrucciones del usuario modifiquen valores económicos calculados por la aplicación o permitan eludir la confirmación del pedido. |
| **Auditoría Básica** | Registrar en log cada pedido simulado, usuario responsable e importe confirmado. |

---

## 8. Rúbrica Oficial de Evaluación (Escala Formal de 3 Niveles)

La evaluación mide **comprensión arquitectónica, rigor de verificación y capacidad de justificación técnica**.

> [!IMPORTANT]
> **Criterios Rectores de la Evaluación:**  
> - **Variabilidad de la implementación:** La implementación concreta de cada patrón podrá variar entre actividades. La evaluación se centrará en la capacidad del alumnado para reconocer el problema de ingeniería, interpretar la solución propuesta, adaptarla a un requisito y demostrar mediante evidencias que el control funciona.  
> - **Capacidades transferibles:** Los criterios de evaluación describen capacidades transferibles y no exigen reproducir una implementación concreta ni utilizar una API, librería o estructura de código determinada, salvo cuando esta se haya establecido expresamente como parte de la actividad.  
> - **Verificación mediante casos adversos:** La evaluación no considera suficiente que el sistema produzca resultados correctos en casos nominales. Se valorará especialmente la capacidad para diseñar o ejecutar casos adversos que permitan demostrar que los controles actúan ante entradas inválidas, datos no autorizados, errores de servicio o intentos de elusión.

| Criterio de Evaluación | Ponderación | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|:---:|---|---|---|
| **Contratos y Validación de Datos (UD1 / UD4)** | **20 %** | Identifica la necesidad de tipado estricto e interpreta, modifica y verifica contratos estructurados con Pydantic que permiten validar las salidas antes de ser procesadas por la lógica de aplicación, gestionando adecuadamente los errores de validación y evitando que una entrada no conforme se propague a la lógica de aplicación. | Interpreta contratos básicos de datos pero muestra inconsistencias en la verificación de errores de formato. | No identifica el riesgo de procesar texto libre sin validar o es incapaz de interceptar y corregir salidas no conformes antes de transferirlas a la lógica de aplicación. |
| **Recuperación, Control de Acceso y Grounding (UD2 / Catálogo)** | **25 %** | Explica cómo la recuperación filtra en origen según los permisos del usuario; verifica que información no autorizada no sea recuperada ni alcance el contexto del modelo y valida respuestas y citas mediante pruebas sobre dataset cerrado. | Interpreta la recuperación sobre fuentes provistas pero muestra inconsistencias en la verificación del control de acceso o en el respaldo de las citas. | No identifica la ausencia de filtros de acceso en la consulta de recuperación o acepta como válidas respuestas no respaldadas por las fuentes recuperadas. |
| **Tool Calling y Acciones Controladas (UD3 / CRM)** | **20 %** | Identifica y justifica la necesidad de validación, reglas de negocio y autorización en el flujo de herramientas, e interpreta, adapta y verifica una implementación que las aplica con auditoría y confirmación en pedidos. | Interpreta y ejecuta herramientas básicas pero no diferencia el impacto de las operaciones u omite controles de confirmación o registro estructurado. | No detecta ni corrige consultas no parametrizadas o es incapaz de aplicar los controles de validación, autorización o confirmación requeridos ante operaciones con consecuencias. |
| **API Contracts, Seguridad y Fallos (UD4)** | **15 %** | Interpreta y verifica contratos de red en FastAPI, identifica y corrige la exposición de credenciales, y comprueba que el servicio responde con códigos semánticos y respuestas estructuradas de error o contingencia. | Interpreta y adapta una API funcional, aplicando una gestión elemental de errores y variables de entorno básicas. | No identifica ni corrige la exposición de credenciales, omite contratos formales de red o no gestiona las excepciones del servicio ante demoras o caídas. |
| **Defensa Técnica y Transferencia (Proyecto Integrador)** | **20 %** | Justifica las decisiones de arquitectura adoptadas en el caso cerámico, identifica las responsabilidades del LLM y de la aplicación, interpreta el código de integración y demuestra mediante pruebas que los controles funcionan. | Explica el funcionamiento general de la solución cerámica pero muestra dudas conceptuales ante cuestiones de seguridad o arquitectura. | Incapaz de justificar las decisiones de diseño adoptadas, confunde las responsabilidades de seguridad o asume una delegación indebida de autoridad en el modelo de lenguaje. |

---

## 9. Delimitación del Alcance: Lo que el Módulo NO Pretende Cubrir

Para dotar a la propuesta de la máxima claridad y blindaje institucional ante la Comisión de Coordinación Pedagógica, se delimita explícitamente lo que queda fuera del programa formativo:

> [!NOTE]
> **Delimitación del Alcance Formativo:**  
> El módulo no pretende cubrir el entrenamiento de modelos de inteligencia artificial desde cero, el diseño de arquitecturas neuronales profundas, el *fine-tuning* de pesos ni el estudio matemático abstracto de los algoritmos de representación vectorial. Estos contenidos exceden con creces el propósito profesional y la carga lectiva del módulo (50 horas).  
>  
> El foco formativo se sitúa con total rigor en la **ingeniería de integración de modelos de lenguaje en aplicaciones software y en los mecanismos de validación, seguridad, gobernanza y verificación necesarios para su despliegue en sistemas reales**.  
>  
> *«No se enseña al alumno a construir ni entrenar un LLM; se le enseña a programar aplicaciones que integran LLM y a construir las fronteras de responsabilidad y control alrededor de ellos.»*

---

## 10. Conclusión y Propuesta Curricular

La propuesta presentada:
1. **Adopta una perspectiva pedagógica moderna y realista:** No pretende forzar al alumnado a memorizar sintaxis desde cero en 50 horas; lo capacita para comprender decisiones de ingeniería, auditar código existente o generado con IA, aplicar controles estrictos y verificar su comportamiento.
2. **Presenta el AI Harness como un conjunto de mecanismos de control distribuidos**, articulando el sistema bajo la Tríada de Responsabilidades: *«1. El LLM propone; la aplicación gobierna la decisión y la ejecución. 2. El LLM interpreta; la aplicación calcula. 3. La aplicación verifica lo que el LLM propone»*.
3. **Asegura la transferencia real de conocimientos**, articulando 40 horas de aprendizaje mediante prácticas específicas de cada patrón (construcción, auditoría y verificación) y 10 horas de integración sobre una empresa cerámica representativa con pedidos simulados sobre un andamiaje preparado.
4. **Capacita al alumnado para integrar y controlar capacidades de IA generativa con criterios de ingeniería de software**, dotándolo de una competencia profesional duradera, rigurosa y verificable.

Por todo ello, se eleva esta **propuesta de diseño curricular y proyecto integrador** para su aprobación formal por la Dirección del Módulo y la Comisión de Coordinación Pedagógica.

---

[← Volver al Índice General](README.md)
