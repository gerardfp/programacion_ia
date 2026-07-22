import logging
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger(__name__)

class InferenciaInput(BaseModel):
    prompt: str = Field(..., min_length=3, description="Texto o instrucción de entrada para la IA")
    temperatura: float = Field(default=0.7, ge=0.0, le=2.0, description="Temperatura de inferencia")
    max_tokens: int = Field(default=512, gt=0, le=4096, description="Límite máximo de tokens generados")

def validar_peticion(payload: dict) -> InferenciaInput:
    """Valida un diccionario convirtiéndolo en un objeto InferenciaInput estructurado."""
    try:
        solicitud = InferenciaInput(**payload)
        logger.info("Solicitud de inferencia validada correctamente para prompt de longitud %d", len(solicitud.prompt))
        return solicitud
    except ValidationError as e:
        logger.error("Error de validación en la solicitud de inferencia: %s", e)
        raise
