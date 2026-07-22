import time
import httpx

def peticion_resiliente(prompt: str, retries: int = 3) -> str:
    url = "http://localhost:11434/api/generate"
    for intento in range(retries):
        try:
            resp = httpx.post(url, json={"model": "llama3.2:3b", "prompt": prompt, "stream": False}, timeout=10.0)
            resp.raise_for_status()
            return resp.json()["response"]
        except Exception:
            if intento == retries - 1:
                raise
            time.sleep(2 ** intento)
