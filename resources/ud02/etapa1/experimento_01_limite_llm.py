# resources/ud02/etapa1/experimento_01_limite_llm.py
"""
Etapa 1 - Parte 1: El límite del conocimiento paramétrico del LLM.
Comprueba qué ocurre cuando preguntamos a un LLM generalista por datos técnicos
y comerciales internos de nuestra empresa (Cerámicas Benigasló) sin proporcionarle contexto.
"""

import httpx

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:0.5b"

preguntas_internas = [
    "¿Cuál es el código de referencia, la absorción de agua y la clase antideslizante de la Serie Marina de Cerámicas Benigasló?",
    "¿Cuántos metros cuadrados exactos trae cada caja de 60x60 cm en Cerámicas Benigasló y cuál es el pedido mínimo de cajas?",
]

print("=== EXPERIMENTO 01: CONSULTA DIRECTA AL LLM SIN RAG ===\n")

for i, pregunta in enumerate(preguntas_internas, start=1):
    print(f"--- Pregunta {i} ---")
    print(f"Usuario: {pregunta}")

    response = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Eres el asistente técnico de Cerámicas Benigasló. Responde de forma concisa.",
                },
                {"role": "user", "content": pregunta},
            ],
            "stream": False,
            "options": {"temperature": 0.0},
        },
        timeout=30.0,
    )
    response.raise_for_status()
    respuesta = response.json()["message"]["content"].strip()
    print(f"LLM (sin contexto documental):\n{respuesta}\n")

print(
    "CONCLUSIÓN:\n"
    "El modelo no conoce los datos privados o actualizados de nuestra empresa:\n"
    "o bien confiesa que no dispone de la información, o bien inventa cifras verosímiles (alucinación).\n"
    "Tampoco podemos pegar los miles de documentos de la empresa en cada petición HTTP\n"
    "porque desbordaríamos la ventana de contexto y dispararíamos la latencia."
)
