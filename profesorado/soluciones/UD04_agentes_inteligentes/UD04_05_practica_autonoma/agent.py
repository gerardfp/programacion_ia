import logging
from tool_registry import HERRAMIENTAS

logger = logging.getLogger(__name__)

class AgenteInteligente:
    def ejecutar_herramienta(self, nombre: str, args: dict):
        tool_info = HERRAMIENTAS[nombre]
        validated_args = tool_info["schema"](**args)
        logger.info("AUDIT LOG: %s %s", nombre, validated_args)
        return tool_info["func"](validated_args)
