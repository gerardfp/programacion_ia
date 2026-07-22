# notebook_desordenado.py (Ejemplo de script/notebook monolítico sin estructurar)
import requests
import json

# Variables globales desordenadas
MODELO = "llama3.2:3b"
URL = "http://localhost:11434/api/generate"
TEMP = "0.7"  # String en lugar de float
MAX_TOKENS = 500

prompt_usuario = "Explicar qué es la IA local"

# Petición HTTP directa sin try/except ni validación de esquema
payload = {
    "model": MODELO,
    "prompt": prompt_usuario,
    "temperature": float(TEMP),
    "stream": False
}

# Sin verificación de estado HTTP ni control de timeouts
res = requests.post(URL, json=payload)
res_json = json.loads(res.text)

# Acceso directo a diccionario sin get() ni tipado
print("Respuesta recibida:")
print(res_json["response"])
