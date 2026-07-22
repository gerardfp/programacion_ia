import urllib.request
import json

def generar_respuesta_local(prompt: str, base_url: str = "http://localhost:11434") -> str:
    """
    TODO: Enviar petición POST a base_url + '/api/generate'
    con payload: {"model": "llama3.2:3b", "prompt": prompt, "stream": False}
    Devolver la respuesta de texto.
    """
    pass
