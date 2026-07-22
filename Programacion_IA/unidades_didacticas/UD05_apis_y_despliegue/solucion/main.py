from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os

app = FastAPI(
    title="Servicio Profesional de Inferencia IA",
    version="1.0.0",
    description="API REST local-first para inferencia con modelos Ollama"
)

class PromptPayload(BaseModel):
    prompt: str = Field(..., min_length=3, example="Explica qué es Docker Compose")
    temperatura: float = Field(default=0.7, ge=0.0, le=2.0)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ia-api"}

@app.post("/api/v1/predict")
def predict(payload: PromptPayload):
    # Solución simulada de integración con Ollama u otro motor
    return {
        "status": "success",
        "prompt": payload.prompt,
        "respuesta": f"[Simulación Inferencia] Procesado correctamente el prompt con temperatura {payload.temperatura}",
        "modelo": os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    }
