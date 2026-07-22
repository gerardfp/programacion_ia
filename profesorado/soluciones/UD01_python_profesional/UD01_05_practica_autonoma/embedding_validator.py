import logging
from typing import List
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger(__name__)

class EmbeddingInput(BaseModel):
    textos: List[str] = Field(..., min_length=1, max_length=100)
    modelo: str = Field(default="all-MiniLM-L6-v2")
    normalizar: bool = Field(default=True)

def validar_embedding_input(payload: dict) -> EmbeddingInput:
    try:
        solicitud = EmbeddingInput(**payload)
        logger.info("EmbeddingInput validado para %d textos.", len(solicitud.textos))
        return solicitud
    except ValidationError as e:
        logger.error("Error validando embeddings: %s", e)
        raise
