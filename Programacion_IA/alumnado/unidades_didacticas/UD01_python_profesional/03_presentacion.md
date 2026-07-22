---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD01: Desarrollo Profesional en Python'
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

# UD01: Desarrollo Profesional en Python para IA
## Del prototipo en Notebook a Software en Producción

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** Local-first, Software Mantenible y Calidad de Código

---

## 1. Del Cuaderno de Notas a Producción

- **Jupyter Notebook:** Excelente para exploración inicial y prototipado rápido.
- **El problema en producción:**
  - Orden de ejecución no lineal y ocultación de estado global.
  - Dificultad para aplicar control de versiones granular en Git.
  - Ausencia de pruebas automáticas y reutilización de código.
- **La solución:** Estructuración en paquetes modulares de Python con entornos reproducibles.

---

## 2. Gestión de Proyectos con `uv`

- **`uv`**: Gestor de paquetes y entornos de ultra-alta velocidad escrito en Rust.
- **Declaración clara de dependencias (`pyproject.toml`):**
  ```toml
  [project]
  name = "mi-servicio-ia"
  version = "0.1.0"
  dependencies = ["pydantic>=2.0.0", "pytest>=7.0.0"]
  ```
- **Fijación reproducible (`uv.lock`):**
  - Garantiza que las dependencias exactas instaladas en desarrollo coincidan al 100% en el servidor de despliegue.
  - Comandos clave: `uv sync`, `uv run pytest`.

---

## 3. Tipado Estático en Python 3.11+

- El tipado estático mejora el autocompletado, previene errores en tiempo de desarrollo y documenta el código.
- Ejemplo de anotaciones de tipos:
  ```python
  from typing import List, Dict, Optional

  def procesar_prompts(prompts: List[str], temperatura: float = 0.7) -> Dict[str, str]:
      resultados: Dict[str, str] = {}
      for prompt in prompts:
          resultados[prompt] = f"Respuesta para: {prompt}"
      return resultados
  ```

---

## 4. Validación de Entradas con Pydantic V2

- Garantiza que los esquemas JSON de entrada y salida de modelos LLM sean válidos antes de procesarlos.
- **Ejemplo con Pydantic:**
  ```python
  from pydantic import BaseModel, Field

  class PeticionInferencia(BaseModel):
      prompt: str = Field(..., min_length=5, description="Instrucción para el LLM")
      temperatura: float = Field(default=0.7, ge=0.0, le=1.0)
      max_tokens: int = Field(default=256, gt=0)
  ```

---

## 5. Pruebas Automáticas y Git Profesional

- **Pruebas unitarias con `pytest`:**
  ```python
  def test_peticion_valida():
      pet = PeticionInferencia(prompt="¿Qué es RAG?")
      assert pet.temperatura == 0.7
  ```
- **Flujo Git Profesional:**
  - Uso de `.gitignore` para omitir entornos virtuales (`.venv`).
  - Commits atómicos con mensajes descriptivos.
  - Integración de comprobaciones de calidad mediante pruebas continuas.
