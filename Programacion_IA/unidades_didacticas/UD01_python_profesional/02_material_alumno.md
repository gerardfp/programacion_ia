# UD01 - Material Teórico para el Alumnado

## 1. Estructura de un Paquete Profesional en Python

En proyectos de IA, es común comenzar experimentando en un Jupyter Notebook. Sin embargo, para entornos de producción es imprescindible migrar a una estructura modular:

```text
mi_proyecto_ia/
├── pyproject.toml
├── uv.lock
├── README.md
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── config.py
│       └── core.py
└── tests/
    ├── __init__.py
    └── test_core.py
```

Utilizamos **`uv`** como herramienta integral para la gestión del proyecto:
- `uv venv`: Crea el entorno virtual optimizado.
- `uv sync`: Instala y sincroniza las dependencias declaradas en `pyproject.toml`.
- `uv lock`: Garantiza la reproducibilidad exacta generando `uv.lock`.
- `uv run pytest`: Ejecuta herramientas dentro del entorno sin necesidad de activación explícita.

## 2. Validación de Datos con Pydantic

Pydantic garantiza que los datos de entrada a modelos de IA cumplen los tipos y rangos esperados:

```python
from pydantic import BaseModel, Field

class InferenciaRequest(BaseModel):
    prompt: str = Field(..., min_length=3, description="Texto de entrada")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, gt=0)
```

## 3. Pruebas Automatizadas con pytest

`pytest` permite verificar que cada componente funciona de forma aislada:

```python
import pytest
from mi_paquete.core import procesar_prompt

def test_procesar_prompt_valido():
    resultado = procesar_prompt("Hola mundo")
    assert resultado is not None
```
