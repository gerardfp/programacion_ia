# UD04 - Material Teórico para el Alumnado

## 1. ¿Qué es un Agente Inteligente?

A diferencia de un chatbot tradicional, un agente inteligente combina un LLM con **herramientas externas** (funciones de código, consultas SQL, APIs) y un bucle de toma de decisiones:

```text
[ Instrucción ] ──► [ LLM (Decisión) ] ──► [ Herramienta Seleccionada ]
                          ▲                        │
                          └──── [ Resultado ] ◄────┘
```

## 2. Ejecución de Herramientas (Tool Calling)

Cada herramienta debe contar con:
- Nombre único y descripción clara de su propósito.
- Esquema estricto de parámetros de entrada (definido mediante Pydantic).
- Función Python ejecutable y segura.

## 3. Seguridad y Auditoría en Agentes
- **Lista blanca:** Ejecutar únicamente funciones registradas explícitamente.
- **Prevención de bucles infinitos:** Límite máximo de pasos por petición (ej. máximo 5 iteraciones).
- **Auditoría:** Guardar en un log cada herramienta invocada con sus argumentos y resultados.
