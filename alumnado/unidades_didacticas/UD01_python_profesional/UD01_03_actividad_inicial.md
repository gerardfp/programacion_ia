# UD01 - Actividad Inicial: Refactorizando un Notebook Desordenado

## 🎯 Objetivos
Analizar un Jupyter Notebook (`.ipynb`) monolítico con variables globales sueltas, celdas desordenadas, sin tratamiento de excepciones ni validación de datos, y proponer su refactorización a módulos independientes en Python utilizando `uv` y `Pydantic`.

---

## 📄 Cuaderno de Partida (`starter/notebook_desordenado.ipynb`)

El archivo **[notebook_desordenado.ipynb](file:///c:/Users/gerard/Desktop/programacioia/alumnado/unidades_didacticas/UD01_python_profesional/starter/notebook_desordenado.ipynb)** representa un prototipo rápido habitual creado en Jupyter Notebooks:

### Celda 1 (Imports):
```python
import requests
import json
```

### Celda 2 (Variables globales):
```python
MODELO = "llama3.2:3b"
URL = "http://localhost:11434/api/generate"
TEMP = "0.7"  # String en lugar de float
MAX_TOKENS = 500
```

### Celda 3 (Ejecución):
```python
prompt_usuario = "Explicar qué es la IA local"

payload = {
    "model": MODELO,
    "prompt": prompt_usuario,
    "temperature": float(TEMP),
    "stream": False
}

# Sin verificación de estado HTTP ni control de timeouts
res = requests.post(URL, json=payload)
res_json = json.loads(res.text)

# Acceso directo a diccionario sin get() ni tipado
print("Respuesta recibida:")
print(res_json["response"])
```

---

## ✏️ Tareas a Realizar

1. **Identificar Bad Practices:** Enumera al menos 4 problemas de mantenibilidad, ejecuciones no lineales o resiliencia derivados de trabajar en celdas de notebook.
2. **Eliminación de Estado Global:** Encapsula la lógica dentro de funciones en archivos `.py` con parámetros y tipos explícitos (`type hints`).
3. **Validación con Pydantic:** Diseña un modelo de datos `PeticionInferencia` para validar el payload de entrada antes de enviarlo.
4. **Manejo de Excepciones:** Añade un bloque `try/except` para capturar posibles errores de conexión (`requests.exceptions.RequestException`).
5. **Estructura de Proyecto:** Mueve el código refactorizado a la carpeta `starter/src/ia_utils/` dentro del proyecto empaquetado con `pyproject.toml`.
