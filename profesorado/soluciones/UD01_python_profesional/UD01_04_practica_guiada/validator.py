import logging
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger(__name__)

class InferenciaInput(BaseModel):
    prompt: str = Field(..., min_length=3)
    temperatura: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, gt=0)

def validar_peticion(payload: dict) -> InferenciaInput:
    try:
        solicitud = InferenciaInput(**payload)
        logger.info("Solicitud validada correctamente.")
        return solicitud
    except ValidationError as e:
        logger.error("Error de validación: %s", e)
        raise
