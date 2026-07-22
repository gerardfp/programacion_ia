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

### Secuencia de Sesiones (15 horas)
1. **Sesión 1-3 (3h):** Concepto de Agente, Bucle de razonamiento (ReAct) y declaración de herramientas.
2. **Sesión 4-6 (3h):** Implementación del registro de herramientas y validación de argumentos con Pydantic y `uv`.
3. **Sesión 7-9 (3h):** Conexión segura a bases de datos relacionales y gestión de listas blancas.
4. **Sesión 10-12 (3h):** Auditoría, trazabilidad de llamadas e historial conversacional.
5. **Sesión 13-15 (3h):** Prueba e integración de agentes de automatización.

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

## 💻 Solución del Proyecto
La solución ejecutable completa de esta unidad se encuentra disponible en:
`profesorado/soluciones/UD04_agentes_inteligentes/`
