from pydantic import BaseModel, Field

class InferenciaInput(BaseModel):
    # TODO: Define los campos prompt (str), temperatura (float entre 0 y 2) y max_tokens (int > 0)
    pass

def validar_peticion(payload: dict) -> InferenciaInput:
    # TODO: Implementa la validación devolviendo una instancia de InferenciaInput
    pass
