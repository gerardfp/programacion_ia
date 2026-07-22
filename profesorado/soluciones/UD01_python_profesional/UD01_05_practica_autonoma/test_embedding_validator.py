import pytest
from embedding_validator import validar_embedding_input

def test_embedding_valido():
    res = validar_embedding_input({"textos": ["Texto 1", "Texto 2"]})
    assert len(res.textos) == 2
