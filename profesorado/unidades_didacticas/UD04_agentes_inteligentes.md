# UD04 - Guía Docente y Evaluación: Agentes Inteligentes y Automatización

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Duración:** 15 horas  
**Resultado de Aprendizaje:** RA4 - Construye agentes inteligentes con ejecución de herramientas y automatización.

---

## 1. Guía para el Profesorado

### Objetivos Didácticos
- Diferenciar flujos deterministas, chatbots conversacionales y agentes inteligentes autónomos.
- Diseñar arquitecturas de *tool calling* (ejecución de herramientas) seguras.
- Conectar agentes con fuentes de datos relacionales (PostgreSQL) garantizando consultas parametrizadas sin inyección de código.
- Implementar registros de auditoría (*audit logs*), límites de iteración y confirmación previa para acciones destructivas.

---

### 🛠️ Preparación e Infraestructura Necesaria

- **Servicio LLM Ollama Operativo:** Servidor con modelo `llama3.2:3b` listo para recibir prompts de razonamiento y Tool Calling.
- **Base de Datos Relacional de Pruebas (PostgreSQL 16):** Instancia con una base de datos de ejemplo (ej. `empresa_db`) precargada con tablas de productos, stock y usuarios de prueba.
- **Usuario de BD con Permisos Limitados:** Rol `lectura_agente` con permisos exclusivamente de `SELECT` para evitar alteraciones accidentales durante las prácticas del alumnado.

---

### ⏱️ Secuencia y Desarrollo Detallado de las Sesiones (15 horas)

#### **Sesión 1-3 (3 horas): Chatbot vs Agente y el Patrón ReAct**
- **Diapositivas a proyectar:** 
  - *Diapositiva 1:* Chatbot vs Agente (De responder preguntas a ejecutar acciones).
  - *Diapositiva 2:* Patrón ReAct (Reasoning + Acting) y llamada a herramientas (*tool calling*).
- **Material Teórico:** Secciones 1 y 2 de `alumnado/unidades_didacticas/UD04_agentes_inteligentes/UD04_01_material.md`.
- **Desarrollo de la Sesión:**
  1. Comparativa entre un modelo pasivo y un agente que decide ejecutar código externo.
  2. **Actividad a realizar:** `UD04_03_actividad_inicial.md` (Traza manual paso a paso de un bucle ReAct: *Thought -> Action -> Observation -> Final Answer*).

#### **Sesión 4-6 (3 horas): Registro de Herramientas y Validación con Pydantic**
- **Diapositivas a proyectar:** 
  - *Diapositiva 3:* Registro de funciones seguras en Python gestionado con `uv`.
- **Material Teórico:** Sección 3 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Creación del registro de herramientas (*Tool Registry*) asignando nombres, descripciones y tipos Pydantic.
  2. **Práctica Guiada (Parte 1):** Inicio de `UD04_04_practica_guiada.md` sobre el esqueleto `starter/`. Registro de la función `consultar_stock()`.

#### **Sesión 7-9 (3 horas): Conexión a Bases de Datos Relacionales y Seguridad anti-SQLi**
- **Diapositivas a proyectar:** 
  - *Diapositiva 4:* Conexión con bases de datos relacionales y prevención de inyección SQL.
- **Material Teórico:** Sección 4 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Riesgos de inyección SQL provocados por LLMs y cómo mitigarlos con ORM o consultas parametrizadas.
  2. **Práctica Guiada (Parte 2):** Completar `UD04_04_practica_guiada.md`. Conexión del agente a la base de datos PostgreSQL del aula.

#### **Sesión 10-12 (3 horas): Auditoría, Trazabilidad y Control de Autonomía**
- **Diapositivas a proyectar:** 
  - *Diapositiva 5:* Trazabilidad, logs de auditoría y contención de riesgos (*Human-in-the-Loop*).
- **Material Teórico:** Sección 5 del material del alumno.
- **Desarrollo de la Sesión:**
  1. Diseño del sistema de logs de auditoría (*Audit Log*) para guardar cada acción ejecutada por el agente.
  2. **Práctica Autónoma:** Desarrollo de `UD04_05_practica_autonoma.md` (Agente de consulta de base de datos con trazabilidad completa).

#### **Sesión 13-15 (3 horas): Reto de Ampliación, Control de Bucles y Evaluación**
- **Desarrollo de la Sesión:**
  1. **Reto de Ampliación:** Trabajo en `UD04_06_reto_ampliacion.md` (Implementación del límite de iteraciones `max_iterations = 5` y mecanismo de confirmación humana previa para acciones críticas).
  2. Evaluación final de entregas frente a la solución en `profesorado/soluciones/UD04_agentes_inteligentes/`.

---

### ⚠️ Errores Frecuentes del Alumnado
- Permitir que el LLM ejecute sentencias SQL crudas sin formatear ni parametrizar, abriendo vulnerabilidades de inyección SQL.
- No definir descripciones claras en las herramientas (causando que el LLM no sepa cuándo o cómo invocarlas).
- Olvidar poner un límite máximo de pasos (*max_iterations*), provocando bucles infinitos cuando el LLM entra en confusión.
- No aislar las excepciones de la herramienta, haciendo que un fallo en la base de datos detenga abruptamente todo el agente.

---

## 2. Criterios e Instrumentos de Evaluación

### Evidencias Evaluables
- **Registro Seguro de Herramientas:** Lista blanca estricta con comprobación de tipos Pydantic.
- **Trazabilidad y Auditoría:** Guardado transparente de cada llamada efectuada por el agente.
- **Control de Autonomía:** Prevención de llamadas arbitrarias o bucles infinitos.

---

## 3. Rúbrica de la Unidad

| Criterio | 4 - Excelente | 3 - Adecuado | 2 - En desarrollo | 1 - Insuficiente |
|---|---|---|---|---|
| **Tool Calling & Selección** | El agente selecciona la herramienta correcta y ejecuta argumentos válidos. | Ejecución correcta de herramientas registradas. | Fallos en la selección de argumentos o herramientas. | Invocaciones erróneas o no autorizadas. |
| **Auditoría y Logs** | Trazabilidad completa con marcas de tiempo y argumentos parseados. | Registra las acciones en un historial. | Auditoría incompleta o parcial. | Sin registro de auditoría. |
| **Seguridad y Control** | Valida esquemas estrictos y limita las iteraciones máximas. | Control básico de errores. | Sin validación de parámetros de entrada. | Permite la ejecución de código arbitrario no autorizado. |

---

## 💻 Soluciones de las Actividades
Las soluciones ejecutables de esta unidad se encuentran dentro de la carpeta [profesorado/soluciones/UD04_agentes_inteligentes/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD04_agentes_inteligentes) organizadas por actividad:
- **Actividad Inicial:** [profesorado/soluciones/UD04_agentes_inteligentes/UD04_03_actividad_inicial/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD04_agentes_inteligentes/UD04_03_actividad_inicial)
- **Práctica Guiada:** [profesorado/soluciones/UD04_agentes_inteligentes/UD04_04_practica_guiada/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD04_agentes_inteligentes/UD04_04_practica_guiada)
- **Práctica Autónoma:** [profesorado/soluciones/UD04_agentes_inteligentes/UD04_05_practica_autonoma/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD04_agentes_inteligentes/UD04_05_practica_autonoma)
- **Reto de Ampliación:** [profesorado/soluciones/UD04_agentes_inteligentes/UD04_06_reto_ampliacion/](file:///c:/Users/gerard/Desktop/programacioia/profesorado/soluciones/UD04_agentes_inteligentes/UD04_06_reto_ampliacion)
