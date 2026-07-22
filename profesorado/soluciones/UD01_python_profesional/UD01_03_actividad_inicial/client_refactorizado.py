import logging
import requests
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger(__name__)

class InferenciaInput(BaseModel):
    prompt: str = Field(..., min_length=3, description="Texto de instrucción para la IA")
    temperatura: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, gt=0)

def enviar_peticion_inferencia(url: str, payload: dict, timeout: float = 30.0) -> dict:
    """Solución UD01_03: Refactorización limpia del notebook_desordenado.ipynb."""
    try:
        solicitud = InferenciaInput(**payload)
    except ValidationError as e:
        logger.error("Error de validación en la entrada: %s", e)
        raise

    data = {
        "model": "llama3.2:3b",
        "prompt": solicitud.prompt,
        "temperature": solicitud.temperatura,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error("Fallo de red o timeout al conectar con la API: %s", e)
        raise RuntimeError(f"Error en inferencia: {e}") from e
