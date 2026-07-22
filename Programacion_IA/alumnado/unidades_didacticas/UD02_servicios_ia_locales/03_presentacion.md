---
marp: true
theme: default
paginate: true
header: 'Programación de IA (5073) | UD02: Servicios de IA Locales'
footer: 'Curso 2026-2027 | Módulo 5073'
style: |
  section {
    background-color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #1e3a8a;
  }
  h2 {
    color: #2563eb;
  }
  code {
    background-color: #e2e8f0;
    color: #0f172a;
  }
---

# UD02: Servicios de IA Locales
## Inferencia Cliente-Servidor con Ollama

**Módulo:** Programación de Inteligencia Artificial (5073)  
**Enfoque:** Local-First, Privacidad Total y Coste Cero por Token

---

## 1. Inferencia Local vs Nube

- **Inferencia en Nube:** Dependencia de API Keys externas, costes por token y salida de datos del centro.
- **Inferencia Local (Ollama):**
  - **Privacidad total:** Los datos nunca abandonan la red local.
  - **Coste cero por token:** Inferencia ilimitada en infraestructura propia.
  - **Latencia predecible:** Independiente del estado de servicios externos.

---

## 2. Arquitectura de Ollama

- Servidor local en segundo plano que gestiona la carga de modelos LLM en memoria/GPU.
- **Comandos habituales CLI:**
  - `ollama pull llama3.2:3b` -> Descarga del modelo local.
  - `ollama run llama3.2:3b` -> Ejecución interactiva.
- Exposición de una **API HTTP REST** en el puerto `11434` (endpoints `/api/generate` y `/api/chat`).

---

## 3. Consumo de la API de Ollama desde Python (`uv`)

```python
import httpx

def consultar_ollama(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
    response = httpx.post(url, json=payload, timeout=30.0)
    return response.json().get("response", "")
```

---

## 4. Respuestas Estructuradas con Modo JSON y Pydantic

- Forzar al LLM a responder exclusivamente en formato JSON válido.
- **Integración:**
  ```python
  from pydantic import BaseModel

  class AnalisisSentimiento(BaseModel):
      sentimiento: str  # "positivo", "neutro", "negativo"
      confianza: float

  # Solicitud estructurada enviando format="json" a Ollama
  ```

---

## 5. Medición de Rendimiento y Métricas

- **Parámetros clave de inferencia:**
  - `num_predict` (Max tokens).
  - `temperature` (Creatividad vs Determinismo).
- **Métricas de calidad y eficiencia:**
  - Tokens por segundo (eval_count / eval_duration).
  - Tiempo hasta el primer token (Time to First Token - TTFT).
  - Consumo de VRAM / RAM del sistema.
