import time
import logging
import json
import urllib.request
from typing import Dict, Any

logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.2:3b"):
        self.base_url = base_url.rstrip("/")
        self.model = model

    def generar(self, prompt: str, system: str = "", format_json: bool = False) -> Dict[str, Any]:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        if system:
            payload["system"] = system
        if format_json:
            payload["format"] = "json"

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

        t0 = time.time()
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                duracion = time.time() - t0
                logger.info("Respuesta de Ollama recibida en %.2f segundos", duracion)
                return {
                    "response": result.get("response", ""),
                    "eval_count": result.get("eval_count", 0),
                    "duracion_segundos": duracion
                }
        except Exception as e:
            logger.error("Fallo al conectar con el servidor Ollama: %s", e)
            raise RuntimeError(f"Error en Ollama: {e}")

if __name__ == "__main__":
    client = OllamaClient()
    print("Cliente Ollama Solución preparado.")
