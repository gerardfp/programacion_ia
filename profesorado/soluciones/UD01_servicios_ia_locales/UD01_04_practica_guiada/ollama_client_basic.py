import httpx

def consultar_ollama(prompt: str, base_url: str = "http://localhost:11434") -> str:
    url = f"{base_url}/api/generate"
    payload = {"model": "llama3.2:3b", "prompt": prompt, "stream": False}
    resp = httpx.post(url, json=payload, timeout=30.0)
    resp.raise_for_status()
    return resp.json().get("response", "")
