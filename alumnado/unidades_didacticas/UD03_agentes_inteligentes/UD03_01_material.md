# UD03 - Material Teórico para el Alumnado

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

## 4. ⚠️ El Fallo del Bucle Manual de Cadenas (Crash & Learn)

El enfoque ingenuo consiste en pedirle al LLM que escriba una frase especial como `Action: consultar_stock(item='laptop')` y parsearla en Python con `split()` o regex. **¿Por qué falla estrepitosamente?**
1. **Rupturas de sintaxis:** En cuanto el modelo responde *"Acción:"* (con tilde) o añade comillas dobles en vez de simples, el código de Python lanza un `IndexError` o `ValueError`.
2. **Bucles infinitos:** Si la herramienta devuelve un error, el LLM no sabe corregirse y vuelve a invocar la misma función repetidamente hasta colgar el sistema.

## 5. ✅ La Solución de la Industria: Model Context Protocol (MCP)

El **Model Context Protocol (MCP)** es el estándar abierto adoptado por la industria para conectar agentes con herramientas y fuentes de datos:
- **Estandarización JSON-RPC:** La comunicación entre el agente y la herramienta no depende de parsear texto libre; sigue un protocolo estricto y universal.
- **Servidores MCP Desacoplados:** Creamos un servidor MCP en Python que expone las herramientas (`consultar_stock_mcp`, `consultar_pedidos_mcp`) con validación automática Pydantic. Cualquier agente compatible puede conectarse a él de forma segura.
