# resources/ud02/etapa1/experimento_03_embeddings.py
"""
Etapa 1 - Parte 3: ¿Qué es un Embedding y cómo permite medir cercanía de significado?
Genera vectores con el modelo 'bge-m3' en Ollama y calcula la distancia coseno
entre una pregunta coloquial y tres textos distintos.
"""

import math
import httpx

OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "bge-m3"


def obtener_embedding(texto: str) -> list[float]:
    """Convierte una cadena de texto en un vector numérico (lista de floats) usando Ollama."""
    res = httpx.post(
        OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "input": texto},
        timeout=30.0,
    )
    res.raise_for_status()
    # /api/embed devuelve {"embeddings": [[float, float, ...]]}
    return res.json()["embeddings"][0]


def distancia_coseno(v1: list[float], v2: list[float]) -> float:
    """
    Calcula la distancia coseno entre dos vectores: 1 - similitud_coseno.
    - Cercana a 0.0 -> Significados muy similares (vectores en la misma dirección).
    - Cercana a 1.0 -> Significados sin relación.
    """
    producto_escalar = sum(a * b for a, b in zip(v1, v2))
    norma_v1 = math.sqrt(sum(a * a for a in v1))
    norma_v2 = math.sqrt(sum(b * b for b in v2))
    similitud = producto_escalar / (norma_v1 * norma_v2)
    return 1.0 - similitud


pregunta = "¿Qué suelo pongo en el bordillo de una piscina para no resbalar?"

fragmentos_candidatos = [
    (
        "DOC-TEC-01 (Ficha Serie Marina)",
        "Gres porcelánico con acabado antideslizante Clase C3 y absorción < 0,1%. "
        "Recomendado para zonas húmedas exteriores y playas de coronación de vasos acuáticos.",
    ),
    (
        "DOC-COM-02 (Logística y Cajas)",
        "Cada caja indivisible de formato 60x60 cm contiene 4 piezas que cubren 1,44 m2 "
        "con un peso de 31,5 kg. Pedido mínimo de 10 cajas.",
    ),
    (
        "DOC-GER-04 (EBITDA Dirección)",
        "El objetivo de EBITDA consolidado de la planta se establece en 4,8 millones de euros "
        "para devengar el bono anual del consejo de administración.",
    ),
]

print("=== EXPERIMENTO 03: INSPECCIÓN DE EMBEDDINGS Y DISTANCIA SEMÁNTICA ===\n")

vec_pregunta = obtener_embedding(pregunta)
print(f"Texto vectorizado: {pregunta!r}")
print(f"Tipo devuelto:     {type(vec_pregunta).__name__} de {type(vec_pregunta[0]).__name__}")
print(f"Dimensiones:       {len(vec_pregunta)} números decimales")
print(f"Primeros 5 valores: {[round(x, 4) for x in vec_pregunta[:5]]}\n")

print("--- Comparación de Distancia Coseno frente a la pregunta ---")
for etiqueta, texto in fragmentos_candidatos:
    vec_frag = obtener_embedding(texto)
    dist = distancia_coseno(vec_pregunta, vec_frag)
    print(f"Distancia: {dist:.4f}  |  {etiqueta}")
    print(f"                   |  Texto: {texto[:80]}...\n")

print(
    "OBSERVACIÓN CLAVE:\n"
    "Aunque la pregunta ('piscina', 'bordillo', 'resbalar') y DOC-TEC-01 ('vasos acuáticos',\n"
    "'antideslizante Clase C3') no comparten palabras, sus vectores son los más cercanos\n"
    "(menor distancia coseno) porque expresan el mismo significado."
)
