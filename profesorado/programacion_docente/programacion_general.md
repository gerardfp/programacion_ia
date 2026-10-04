# Programación General del Módulo: Programación de Inteligencia Artificial (Intensivo)

- **Código del módulo:** 5073
- **Duración total:** 50 horas lectivas (40 h Aprendizaje y Prácticas + 10 h Proyecto Integrador)
- **Curso académico:** 2026-2027

---

## 1. Justificación y Enfoque del Módulo

El módulo de **Programación de Inteligencia Artificial** en su modalidad intensiva de **50 horas** se plantea como una **introducción práctica al desarrollo de aplicaciones que integran inteligencia artificial generativa**, con especial atención a los patrones y problemas habituales de las aplicaciones basadas en Modelos de Lenguaje (LLMs).

El objetivo no es que el alumnado aprenda a desarrollar modelos de inteligencia artificial desde cero, ni evaluar su capacidad para memorizar sintaxis, sino que sea capaz de **identificar oportunidades de aplicación de estas tecnologías, integrarlas en aplicaciones software y establecer los mecanismos necesarios para controlar y verificar su comportamiento**.

> *«No se enseña al alumno a construir ni entrenar un LLM; se le enseña a programar aplicaciones que integran LLM y a construir las fronteras de responsabilidad y control alrededor de ellos.»*

### Las Dos Fases del Curso

* **Fase 1: Aprendizaje y prácticas independientes (40 horas):** Adquisición de conceptos, herramientas y patrones mediante prácticas independientes en dominios variados.
* **Fase 2: Proyecto final integrador (10 horas):** Integración de los conocimientos adquiridos en una aplicación web empresarial existente.

> [!IMPORTANT]
> **Transferencia de Conocimientos y Delimitación:**  
> - Las prácticas realizadas durante las primeras 40 horas **no están contextualizadas en el proyecto final**. Se utilizan contextos y dominios diferentes en cada unidad para que el alumnado aprenda los patrones de forma general y no se limite a reproducir una solución previamente construida.  
> - El proyecto final no introduce nuevas tecnologías ni nuevos conceptos fundamentales; los endpoints de CRM y pedidos forman parte del andamiaje proporcionado. Su finalidad es que el alumnado sea capaz de **reconocer qué técnicas aprendidas son adecuadas para cada problema y combinarlas para construir una solución coherente**.

### Principios Rectores: La Tríada de Responsabilidades del Módulo

Toda la arquitectura del curso y la delimitación de responsabilidades se fundamenta en tres principios explícitos:

1. **El LLM propone; la aplicación gobierna la decisión y la ejecución.**  
   El modelo genera sugerencias o borradores de datos y acciones; la aplicación gobierna la autorización, el estado y las operaciones con consecuencias.
2. **El LLM interpreta; la aplicación calcula.**  
   El modelo procesa lenguaje y extrae intenciones o parámetros; las operaciones deterministas que afectan al estado o a los resultados de negocio se delegan en software verificable, como cálculos matemáticos, tarifas, disponibilidad o reglas de pedido. El modelo puede **extraer o interpretar** magnitudes expresadas por el usuario (por ejemplo, metros cuadrados), pero las operaciones que determinan cantidades económicas o estado del sistema se realizan mediante lógica determinista de la aplicación.
3. **La aplicación verifica lo que el LLM propone.**  
   El software no debe confiar ciegamente en la salida del modelo: valida esquemas mediante contratos, comprueba reglas de dominio y exige confirmación humana en operaciones de impacto relevante.

### Evidencias Evaluables: Artefactos Técnicos y Comprensión

La evaluación profesional se articula en dos planos inseparables fundamentados en un principio docente rector:

> [!IMPORTANT]
> **Principio de Responsabilidad sobre el Código:**  
> *«La procedencia del código —profesorado, alumnado o herramienta de IA— no determina su valor educativo. Sin embargo, quien lo utiliza debe ser capaz de interpretar su funcionamiento, identificar sus riesgos, modificarlo cuando proceda y aportar evidencias de que cumple los requisitos establecidos. La delegación de la escritura no implica la delegación de la responsabilidad técnica.»*

1. **Artefactos Técnicos (Resultados y Evidencias de Ejecución):**
   - **Código adaptado y configurado:** Esquemas de datos Pydantic, parametrización de consultas y despacho gobernado de herramientas.
   - **Pruebas automatizadas (`pytest`):** Suites de tests que provocan fallos deliberados para verificar que los controles interceptan anomalías.
   - **Trazas y registros de ejecución:** Logs estructurados (*Audit Log*) y telemetría (Langfuse) que documentan empíricamente el comportamiento en tiempo de ejecución.
2. **Comprensión y Justificación Técnica (Evidencias de Dominio):**
   - **Explicación técnica:** Capacidad de razonar qué hace cada componente, por qué está implementado de esa forma y qué riesgo neutraliza.
   - **Defensa técnica ante preguntas de arquitectura:** Capacidad de responder ante preguntas docentes sobre caídas de red, latencias o compromisos de seguridad.

### El Ciclo Metodológico de Aprendizaje (7 Etapas)

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

El aprendizaje se articula en 7 fases continuas:
1. **Actividad inicial:** Presentación del problema contextualizado y la necesidad técnica que justifica el patrón antes de abordar el código.
2. **Cuestionario conceptual (*¿He comprendido el problema?*):** Comprobación individual de conceptos fundamentales, responsabilidades y riesgos antes de tocar código.
3. **Práctica guiada:** Interpretación y manipulación de una implementación provista (*starter kit*) o generada con IA, localizando los componentes clave.
4. **Cuestionario de comprensión (*¿Entiendo lo que acabo de hacer?*):** Comprobación de que el alumno comprende el flujo de ejecución, los contratos de datos y las consecuencias de omitir controles.
5. **Modificación y adaptación:** Adaptación autónoma de la implementación para incorporar nuevos requisitos o corregir defectos deliberados.
6. **Prueba automatizada:** Diseño, adaptación y ejecución de pruebas unitarias e integración con `pytest` (casos nominales y negativos de elusión).
7. **Evidencia y defensa técnica:** Aportación de resultados, trazas de auditoría y defensa oral ante el profesorado.

> **La función dual de los cuestionarios y la verificación de la comprensión:** La combinación de los cuestionarios conceptuales y de comprensión permite evaluar con rigor si el alumno comprende los mecanismos de control con total independencia de si el código inicial fue generado con apoyo de herramientas de IA, desplazando el foco desde la autoría del código hacia la responsabilidad técnica sobre el resultado y evitando que la generación automática de código sustituya la comprensión y la capacidad de verificación del alumnado.

---

## 2. Bloques Temáticos y Horas (50 Horas)

| Bloque / Unidad Didáctica | Horas | RA | Carpeta Repo | Contenidos Nucleares y Foco de Aprendizaje |
|---|---:|:---:|:---:|---|
| **UD1. Integración de LLM en Aplicaciones** | 10 h | RA2 | `UD01_servicios_ia_locales` | **Integración y Contratos de Datos:** APIs de modelos locales, mensajes por roles (`system`/`user`/`assistant`), límites de context window, generación de texto, extracción, datos estructurados, JSON y validación con Pydantic. Limitaciones y respuestas no fiables. Demo de streaming. |
| **UD2. RAG y Acceso al Conocimiento** | 12 h | RA3 | `UD02_aplicaciones_rag` | **Recuperación y Grounding:** Embeddings, búsqueda semántica, chunking, bases de datos vectoriales con PostgreSQL (`pgvector`), grounding (respaldo en fuentes recuperadas) y citas, abstención en la aplicación ("NO_DATA"), **control de acceso filtrado en origen en la consulta SQL** y evaluación operacional sobre dataset cerrado. |
| **UD3. Tool Calling y Acciones Controladas** | 10 h | RA4 | `UD03_agentes_inteligentes` | **Herramientas y Decisiones Gobernadas:** Definición formal de herramientas, argumentos tipados, validación sintáctica, reglas de negocio, autorización según impacto (lectura vs mutación vs operación crítica), confirmación (*Human-in-the-Loop*), SQL parametrizado, límites de bucle, auditoría y demo MCP. |
| **UD4. Integración, Seguridad y Control** | 8 h | RA5 | `UD04_apis_y_despliegue` | **Arquitectura de Servicio y Resiliencia:** APIs HTTP con FastAPI y API Contracts tipados, cuádruple frontera de seguridad como modelo didáctico de defensa en profundidad (identidad autenticada disponible en la aplicación (`current_user`) $\rightarrow$ autorización en la aplicación $\rightarrow$ control de acceso a datos $\rightarrow$ reglas de negocio), gestión de secretos en `.env`, *datos $\neq$ instrucciones*, taxonomía real de errores y respuestas estructuradas de error o contingencia, introducción a multimodalidad y observabilidad. |
| **Proyecto Integrador: Empresa Cerámica** | 10 h | RA6 | `UD05_proyecto_final` | **Integración Empresarial y Transferencia:** Integración de IA en la aplicación web de una empresa cerámica ficticia del sur de Castellón: 1. Asistente técnico de catálogo (RAG + tools de stock), 2. Visualizador de ambientes (multimodal guiado), y 3. Asistente comercial/CRM con formalización de pedidos simulados y defensa oral. |
| **Total** | **50 h** | | | |

---

## 3. El Proyecto Integrador: Empresa Cerámica del Sur de Castellón

Como proyecto final se plantea la integración de IA generativa en una aplicación web de una **empresa ficticia de fabricación y comercialización de productos cerámicos del sur de Castellón**.

> *El andamiaje proporcionado contiene implementadas las funcionalidades convencionales, los modelos de datos, los endpoints, la interfaz, la infraestructura y plantillas de pruebas parcialmente preparadas. El trabajo del alumnado se limita a implementar la lógica de integración de IA, sus mecanismos de control y las pruebas asociadas.*

El alumnado integra tres subsistemas:

1. **Asistente de catálogo técnico (RAG):** Consultas sobre especificaciones de pavimentos y revestimientos cerámicos (formatos, usos recomendados y colocación) con citas explícitas de fuentes documentales como mecanismo de verificación, respuesta de abstención formal ("NO_DATA") ante falta de datos y tools de consulta (`consultar_stock`, `consultar_producto`).
2. **Visualizador de ambientes (Multimodal):** Integración guiada de un servicio multimodal preconfigurado donde el usuario asocia la foto de una estancia real y un producto cerámico seleccionado para generar la previsualización del espacio renovado mediante contratos de API claros (evaluando el cumplimiento del contrato de integración, parámetros y control de errores, no la calidad estética del render).
3. **Asistente comercial y pedidos simulados:** Diálogo guiado donde el LLM extrae necesidades y metros cuadrados, invocando una herramienta determinista (`calcular_cajas(producto, m2)`) para que **la aplicación calcule de forma determinista el número de cajas y el importe oficial según las reglas de negocio establecidas**, preparando el borrador de pedido y exigiendo confirmación explícita (*Human-in-the-Loop*) antes de registrar el pedido simulado con auditoría.

### Matriz de Transferencia de Competencias

| Durante el Curso (Prácticas Independientes - 40 h) | En el Proyecto Final Cerámico (10 h) |
|---|---|
| **Structured Output** | Extraer preferencias y datos del cliente desde el diálogo |
| **Pydantic** | Validar información generada por el LLM antes de procesarla por la aplicación |
| **RAG** | Asistente del catálogo técnico cerámico con citas y abstención |
| **Embeddings** | Interpretación y uso de la búsqueda semántica de colecciones y acabados en el catálogo |
| **Control de Acceso** | Filtrado en base de datos para impedir que clientes accedan a documentación interna |
| **Tool Calling** | Consultar stock en almacén y operar sobre el sistema |
| **Reglas de Negocio** | Validar stock disponible y condiciones mínimas de pedido |
| **Autorización** | Controlar qué acciones puede realizar cada perfil de usuario |
| **Confirmación de Acciones** | Exigir confirmación del cliente antes de registrar el pedido simulado |
| **Persistencia** | Almacenamiento en PostgreSQL de clientes, contactos y pedidos simulados |
| **Multimodalidad** | Visualizador de estancias renovadas con el producto cerámico |
| **Evaluación** | Comprobar respuestas del catálogo sobre el dataset cerrado de 20 casos |
| **Seguridad** | Impedir que instrucciones del usuario modifiquen valores económicos calculados o eludan la confirmación |
| **Auditoría** | Registrar acciones y formalización de pedidos simulados mediante log |

---

## 4. Delimitación del Alcance Formativo: Lo que el Módulo NO Pretende Cubrir

Para preservar el rigor pedagógico y anticipar debates institucionales, se delimita con claridad lo que queda fuera del alcance del módulo:

> [!NOTE]
> **Delimitación del Alcance:**  
> El módulo no pretende cubrir el entrenamiento de modelos de IA desde cero, el desarrollo de arquitecturas neuronales, el *fine-tuning* avanzado de pesos ni el estudio matemático profundo de los algoritmos de representación vectorial. Estos contenidos exceden el propósito y la carga lectiva del módulo (50 horas).  
>  
> El foco formativo se sitúa con total rigor en la **integración de modelos de lenguaje en aplicaciones software y en los mecanismos de validación, seguridad, control y verificación necesarios para su uso dentro de sistemas reales**.
