import time
import httpx

def evaluar_con_benchmark(prompt: str) -> dict:
    url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3.2:3b", "prompt": prompt, "format": "json", "stream": False}
    t0 = time.time()
    resp = httpx.post(url, json=payload, timeout=30.0)
    duracion = time.time() - t0
    data = resp.json()
    return {"response": data.get("response"), "duracion_segundos": duracion}
