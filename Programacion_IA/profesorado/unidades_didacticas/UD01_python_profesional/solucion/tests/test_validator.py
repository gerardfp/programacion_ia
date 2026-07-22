import pytest
from pydantic import ValidationError
from ia_utils.validator import InferenciaInput, validar_peticion

def test_validar_peticion_valida():
    payload = {
        "prompt": "¿Qué es la Inteligencia Artificial?",
        "temperatura": 0.5,
        "max_tokens": 256
    }
    resultado = validar_peticion(payload)
    assert isinstance(resultado, InferenciaInput)
    assert resultado.prompt == "¿Qué es la Inteligencia Artificial?"
    assert resultado.temperatura == 0.5
    assert resultado.max_tokens == 256

def test_validar_peticion_temperatura_invalida():
    payload = {
        "prompt": "Genera un resumen",
        "temperatura": 3.0
    }
    with pytest.raises(ValidationError):
        validar_peticion(payload)

def test_validar_peticion_prompt_demasiado_corto():
    payload = {
        "prompt": "Hola"
    }
    # Funciona porque min_length es 3
    resultado = validar_peticion(payload)
    assert resultado.prompt == "Hola"
