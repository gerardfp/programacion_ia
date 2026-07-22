# UD01 - Práctica Autónoma: Validador de Entradas de Inferencia

## Enunciado
El alumnado deberá ampliar la librería `ia_utils` agregando una nueva clase Pydantic llamada `EmbeddingInput` con los siguientes campos:
- `textos`: Lista de cadenas de texto (mínimo 1 elemento, máximo 100 elementos).
- `modelo`: Cadena con el nombre del modelo de embeddings (por defecto `"all-MiniLM-L6-v2"`).
- `normalizar`: Booleano (por defecto `True`).

Además, escribirá pruebas unitarias en `tests/test_embedding_validator.py` utilizando `pytest`.
