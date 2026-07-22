import pytest
from validator import validar_peticion

def test_validar_peticion_ok():
    res = validar_peticion({"prompt": "Hola mundo", "temperatura": 0.5})
    assert res.prompt == "Hola mundo"
