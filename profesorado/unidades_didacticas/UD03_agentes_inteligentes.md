# UD03 - Guía Docente y Evaluación: Tool Calling y Ejecución Segura

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 10 horas (Bloque 3 / UD02 del curso intensivo)  
**Resultado de Aprendizaje:** RA4 - Implementa Tool Calling y ejecución segura de herramientas con autorización proporcional.  
**Identificador Curricular Intensivo:** UD02 - Tool Calling y Ejecución Segura  

---

## 1. Guía para el Profesorado

### Problema Técnico Central
> **¿Cómo interactúa el modelo con sistemas externos de forma segura, estructurada y sin delegarle autoridad directa?**  
> Un LLM no puede ejecutar código ni modificar bases de datos por sí mismo. El alumnado asimilará el **Principio 3 del Harness: Soberanía de Ejecución y Mínimo Privilegio** (*el modelo propone la invocación; el Harness valida, autoriza y ejecuta*). Se formalizará el protocolo de Tool Calling en 8 pasos, la **tríada de validación** (sintaxis, reglas de negocio y autorización), la política de confirmación proporcional al impacto, la prevención de SQL Injection mediante consultas parametrizadas, el control de bucles y la demostración de desacoplamiento estándar con **Model Context Protocol (MCP)**.

### Objetivos Didácticos
- Formalizar el **Protocolo de Tool Calling en 8 pasos**:
  1. Petición del usuario $\rightarrow$ 2. LLM propone invocación $\rightarrow$ 3. Solicitud formal `{name, args}` $\rightarrow$ 4. Validación sintáctica con esquemas Pydantic $\rightarrow$ 5. Validación de reglas de negocio $\rightarrow$ 6. Autorización del usuario $\rightarrow$ 7. Ejecución segura en el entorno $\rightarrow$ 8. Inyección del resultado con `role: "tool"` para respuesta final.
- **La Tríada de Validación del Harness:**
  1. *Validación sintáctica:* ¿Los argumentos cumplen los tipos y formatos requeridos? (Pydantic).
  2. *Regla de negocio:* ¿La operación es admisible en el dominio empresarial? (Límites de saldo, estados válidos).
  3. *Autorización:* ¿Este usuario específico tiene permiso para ejecutar esta acción?
- **Autorización y Confirmación Proporcional al Impacto:**
  - Operaciones inocuas o de bajo impacto (consultas de lectura, registro de métricas): automatizadas con registro de auditoría.
  - Operaciones destructivas o críticas (borrar usuarios, transferir fondos): exigen confirmación explícita (*Human-in-the-Loop*).
- **Idempotencia y Resiliencia:** Diseñar herramientas que admitan reintentos seguros ante cortes de conexión, recordando que *idempotente no significa inocuo* (ej. `DELETE`).
- **Prevención de SQL Injection vs Prompt Injection:** El LLM nunca compone sentencias SQL libres en texto; las herramientas ejecutan consultas parametrizadas (`cursor.execute(sql, (params,))`).
- **Control de Bucle:** Establecer un límite explícito de iteraciones y timeouts para prevenir bucles infinitos y consumo excesivo de inferencia.
- **Demostración de MCP:** Conectar el sistema a un servidor MCP preconfigurado provisto por el profesor para observar cómo se exponen herramientas bajo un estándar abierto sin acoplamiento de código.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio LLM Ollama Operativo:** Servidor local con modelo `llama3.2:3b` o `qwen2.5:3b` con soporte para Tool Calling.
- **Base de Datos PostgreSQL de Pruebas:** Instancia relacional con tablas de negocio (`productos`, `stock`, `pedidos`).
- **Servidor MCP de Demostración:** Script provisto por el docente (`demo_mcp_server.py`) que expone herramientas sobre la base de datos.
- **Librerías Python:** `httpx`, `pydantic`, `psycopg` instaladas mediante `uv`.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (10 horas)

#### **Sesión 1-2 (4 horas): El Protocolo de Tool Calling y la Tríada de Validación**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* De Chatbot a Sistema Activo: El axioma de autoridad (*"El modelo propone, el Harness ejecuta"*).
  - *Diapositiva 2:* Diagrama secuencial del protocolo en 8 pasos y mensajes con `role: "tool"`.
  - *Diapositiva 3:* La Tríada de Validación: Sintaxis (Pydantic), Negocio (Reglas de dominio) y Autorización (Permisos de usuario).
- **Material Teórico:** UD03 en [README.md](file:///home/gerard/programacion_ia/README.md#ud03-agentes-inteligentes).
- **Desarrollo de la Sesión:**
  1. Definición formal de herramientas con esquemas `BaseModel` y descripciones claras.
  2. Implementación del despachador en el Harness: validación sintáctica de argumentos antes de invocar la función.
  3. Aplicación de reglas de negocio que rechazan solicitudes que violan restricciones del dominio.
  4. **Actividad Inicial:** Etapa 1 en [README.md](file:///home/gerard/programacion_ia/README.md#ud03-etapa1).

#### **Sesión 3-4 (4 horas): Impacto Proporcional, SQL Parametrizado y Límites de Bucle (Crash & Learn)**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Autorización proporcional al impacto: operaciones automáticas vs Human-in-the-Loop.
  - *Diapositiva 5:* SQL Injection vs Prompt Injection: Uso obligatorio de consultas SQL parametrizadas.
  - *Diapositiva 6:* El fallo del bucle infinito y su solución mediante límite explícito de iteraciones y timeouts.
- **Material Teórico:** Etapas 3 y 4 del manual del alumno.
- **Desarrollo de la Sesión (Crash & Learn):**
  1. **El Fallo:** Se simula un error de herramienta en un bucle sin límites; el LLM reintenta indefinidamente consumiendo CPU y saturando el contexto.
  2. **La Solución:** Inclusión de contador de pasos con corte forzado, timeout en llamadas y captura de excepciones.
  3. Implementación de confirmación humana obligatoria ante operaciones críticas.
  4. **Práctica Guiada:** Etapa 3 en [README.md](file:///home/gerard/programacion_ia/README.md#ud03-etapa3).

#### **Sesión 5 (2 horas): Demostración de Desacoplamiento con MCP**
- **Diapositivas a proyectar:** 
  - *Diapositiva 7:* Model Context Protocol (MCP) como estándar abierto para conectar herramientas externas.
  - *Diapositiva 8:* Arquitectura cliente-servidor MCP sin acoplamiento de dependencias en la aplicación principal.
- **Desarrollo de la Sesión:**
  1. Conexión del bucle de herramientas al servidor MCP provisto.
  2. Ejecución de consultas de inventario desacopladas.
  3. **Práctica Autónoma y Reto de Consolidación:** Etapas 5 y 7 en [README.md](file:///home/gerard/programacion_ia/README.md#ud03-etapa5).

---

### ⚠️ Errores Frecuentes del Alumnado
- Permitir que el LLM ejecute sentencias SQL libres generadas en texto plano en lugar de invocar herramientas con argumentos tipados y consultas parametrizadas.
- Omitir la validación de reglas de negocio asumiendo que si Pydantic valida los tipos de datos, la operación ya es segura.
- Exigir confirmación humana para todas las operaciones (incluidas lecturas o logs inocuos), generando fatiga de alertas innecesaria.
- No establecer un límite explícito de iteraciones en el bucle de ejecución de herramientas.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Despachador de Tool Calling:** Código ejecutable que implementa el ciclo de invocación validando sintácticamente argumentos con Pydantic.
- **Tríada de Validación y Autorización:** Comprobación explícita de reglas de negocio y permisos del usuario antes de invocar la herramienta.
- **Seguridad en Datos:** Consultas SQL parametrizadas que impiden SQL injection y política de confirmación para acciones críticas.
- **Control de Ciclo:** Bucle gobernado con límite de iteraciones y captura estructurada de excepciones.

---

## 3. Rúbrica Oficial de la Unidad (Escala de 3 Niveles)

| Criterio | Nivel 3: Logrado (Notable / Excelente) | Nivel 2: En Desarrollo (Básico / Suficiente) | Nivel 1: No Logrado (Insuficiente) |
|---|---|---|---|
| **Protocolo de Tool Calling** | Implementa el ciclo en 8 pasos con validación sintáctica de esquemas Pydantic y reinyección del resultado como rol `tool`. | Ejecuta herramientas mediante llamadas estructuradas pero con manejo básico del ciclo de mensajes. | Pasa texto libre al modelo o ejecuta funciones sin validación previa de argumentos. |
| **Tríada de Validación y Seguridad** | Aplica validación sintáctica, reglas de negocio y autorización; exige confirmación en operaciones críticas y utiliza SQL parametrizado. | Valida sintácticamente los datos pero no separa reglas de negocio o carece de control proporcional de impacto. | Cede autoridad directa al LLM, no verifica permisos o permite concatenación insegura de SQL. |
| **Control de Ciclo y Resiliencia** | Límite explícito de iteraciones en el bucle, gestión de timeouts y captura de excepciones con respuesta controlada al usuario. | Control básico de iteraciones pero con gestión de errores o timeouts mejorable. | Agente susceptible de entrar en bucles infinitos o caída del programa ante fallos de herramientas. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD03_agentes_inteligentes/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD03_agentes_inteligentes) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD03_agentes_inteligentes/UD03_03_actividad_inicial/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD03_agentes_inteligentes/UD03_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD03_agentes_inteligentes/UD03_04_practica_guiada/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD03_agentes_inteligentes/UD03_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD03_agentes_inteligentes/UD03_05_practica_autonoma/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD03_agentes_inteligentes/UD03_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD03_agentes_inteligentes/UD03_06_reto_ampliacion/](file:///home/gerard/programacion_ia/profesorado/soluciones/UD03_agentes_inteligentes/UD03_06_reto_ampliacion)
