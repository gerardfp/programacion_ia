# 📘 Manual de Unidades Didácticas: Programación de Inteligencia Artificial (5073)
## Guía de Aprendizaje en 7 Etapas para el Alumnado

**Módulo:** Programación de Inteligencia Artificial (5073) — Modalidad Intensiva (50 horas)  
**Modalidad:** Local-First, Software Libre, Python con `uv` y Docker  
**Tesis Central del Aprendizaje:**  
> *«No aprendes a construir ni entrenar un LLM; aprendes a programar aplicaciones software que integran modelos de lenguaje y a construir las fronteras de responsabilidad, control y verificación alrededor de ellos.»*

> 💡 **Documentación Curricular y Docente:** La programación docente oficial, criterios de evaluación, infraestructura de aula y soluciones para el profesorado están disponibles en el [Espacio del Profesorado](profesorado/README.md).

---

## 🧭 La Tríada de Responsabilidades del Alumno

Durante todo el módulo, cada línea de código y cada diseño arquitectónico responde a tres principios irrenunciables:

1. **El LLM propone; la aplicación gobierna la decisión y la ejecución.**  
   El modelo genera sugerencias o borradores de datos y acciones; la aplicación gobierna la autorización, el estado y las operaciones con consecuencias.
2. **El LLM interpreta; la aplicación calcula.**  
   El modelo procesa lenguaje y extrae intenciones o parámetros; las operaciones deterministas que afectan al estado o a los resultados de negocio se delegan en software verificable (cálculos matemáticos, tarifas, disponibilidad o reglas de pedido). El modelo puede extraer o interpretar magnitudes (por ejemplo, metros cuadrados), pero la determinación de cantidades económicas y existencias la realiza la lógica determinista de la aplicación.
3. **La aplicación verifica lo que el LLM propone.**  
   El software no debe confiar ciegamente en la salida del modelo: valida esquemas mediante contratos (Pydantic), comprueba reglas de dominio y exige confirmación humana en operaciones de impacto relevante.

---

## 🔄 El Ciclo Metodológico de Aprendizaje en 7 Etapas

Cada unidad didáctica se desarrolla siguiendo una secuencia formativa estructurada en 7 etapas consecutivas:

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. ACTIVIDAD INICIAL (Contexto, problema y caso adverso)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CUESTIONARIO CONCEPTUAL (¿He comprendido el problema?)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. PRÁCTICA GUIADA (Código base provisto o generado con IA) │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. CUESTIONARIO DE COMPRENSIÓN (¿Entiendo lo implementado?) │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. PRÁCTICA AUTÓNOMA (Modificación, adaptación y controles) │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. PRUEBA AUTOMATIZADA (Diseño y ejecución con pytest)      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. RETO DE AMPLIACIÓN Y DEFENSA TÉCNICA (Trazas y oral)     │
└─────────────────────────────────────────────────────────────┘
```

---