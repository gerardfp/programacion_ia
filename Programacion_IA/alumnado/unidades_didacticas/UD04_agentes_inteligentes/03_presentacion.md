---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD04: Agentes Inteligentes'
footer: 'Curso 2026-2027 | Módulo 5073'
style: |
  section {
    background-color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #1e3a8a;
  }
  h2 {
    color: #2563eb;
  }
  code {
    background-color: #e2e8f0;
    color: #0f172a;
  }
---

# UD04: Agentes Inteligentes y Automatización
## Llamada a Herramientas (Tool Calling) y Toma de Decisiones Autonóma

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** De la Respuesta Pasiva a la Ejecución Segura de Acciones

---

## 1. Chatbots vs Agentes Inteligentes

- **Chatbot / LLM Tradicional:** Entrada de texto -> Salida de texto pasiva. No interactúa con el mundo exterior.
- **Agente Inteligente:**
  - Analiza la intención del usuario.
  - Decide qué herramienta (*tool*) necesita ejecutar.
  - Recibe el resultado técnico de la herramienta.
  - Elabora una respuesta sintetizada basada en datos reales.

---

## 2. El Patrón ReAct (Reasoning + Acting)

```text
1. Pensamiento (Thought): "El usuario pregunta por la temperatura del servidor. Debo usar 'obtener_temp_cpu'."
2. Acción (Action): Ejecutar función obtener_temp_cpu(servidor="srv-01")
3. Observación (Observation): Resultado = "45°C"
4. Respuesta Final (Final Answer): "La temperatura actual del servidor srv-01 es de 45°C."
```

---

## 3. Registro de Herramientas en Python

- Definición de funciones seguras con tipos explícitos para el motor de *Tool Calling*:

```python
def consultar_stock(producto_id: str) -> int:
    """Consulta el stock disponible de un producto en la BD local."""
    # Lógica de consulta en PostgreSQL local
    return 42

herramientas_disponibles = {
    "consultar_stock": consultar_stock
}
```

---

## 4. Consultas Seguras a Bases de Datos y Prevención de SQLi

- **Inyección SQL con LLMs:** Nunca permitir que un LLM genere sentencias SQL arbitrarias de escritura (`DROP`, `DELETE`, `UPDATE`) sin supervisión.
- **Buenas Prácticas:**
  - Uso de consultas parametrizadas u ORM (SQLAlchemy / SQLModel).
  - Usuarios de BD con permisos de **solo lectura** para el agente.
  - Validación con Pydantic antes de la ejecución de cualquier argumento de función.

---

## 5. Auditoría, Logs y Control de Autonomía

- **Trazabilidad:** Registrar cada paso (*thought*, *action*, *parameters*, *result*) en un log de auditoría.
- **Confirmación humana (*Human-in-the-Loop*):** Requerir autorización previa antes de ejecutar acciones de alto impacto (ej. reiniciar servidor, enviar correos).
- **Límites de bucles:** Prevenir iteraciones infinitas fijando un número máximo de pasos de ejecución (ej. `max_iterations = 5`).
