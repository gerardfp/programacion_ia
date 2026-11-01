# resources/ud02/evaluar_rag.py
"""
Script de evaluación cuantitativa sobre el dataset cerrado 'datos/casos_evaluacion.json' (Etapa 5 - Mejora C).
Calcula:
  1. Hit Rate @ k en los casos nominales (proporción de preguntas donde el documento esperado
     aparece entre los k primeros fragmentos recuperados).
  2. Tasa de Rechazo en Origen en los casos 'fuera_de_dominio' y 'no_autorizado' (proporción de
     preguntas que devuelven [] gracias al filtro SQL y al umbral de distancia máxima, evitando
     invocar innecesariamente al LLM).
"""

import json
from pathlib import Path
from src.ingesta import ingestar_corpus_json
from src.recuperador import RecuperadorRAG

RUTA_CASOS = Path(__file__).resolve().parent / "datos" / "casos_evaluacion.json"


def evaluar_con_umbral(
    recuperador: RecuperadorRAG,
    casos: list[dict],
    limite: int = 3,
    distancia_maxima: float | None = 0.48,
) -> dict:
    nominales = [c for c in casos if c["tipo"] == "nominal"]
    adversos = [c for c in casos if c["tipo"] in ("fuera_de_dominio", "no_autorizado")]

    aciertos_nominales = 0
    rechazos_adversos = 0

    print(f"\n--- Evaluando con limite={limite}, distancia_maxima={distancia_maxima} ---")

    for caso in nominales:
        frags = recuperador.buscar_fragmentos_autorizados(
            pregunta=caso["pregunta"],
            depto_usuario=caso["depto_usuario"],
            limite=limite,
            distancia_maxima=distancia_maxima,
        )
        codigos = [f.codigo_doc for f in frags]
        acierto = caso["esperado_codigo_doc"] in codigos
        if acierto:
            aciertos_nominales += 1
        estado_str = "OK  " if acierto else "FALLO"
        print(
            f"  [Nominal #{caso['id']:02d} - {estado_str}] Esperado: {caso['esperado_codigo_doc']} "
            f"| Recuperados: {codigos}"
        )

    for caso in adversos:
        frags = recuperador.buscar_fragmentos_autorizados(
            pregunta=caso["pregunta"],
            depto_usuario=caso["depto_usuario"],
            limite=limite,
            distancia_maxima=distancia_maxima,
        )
        codigos = [f.codigo_doc for f in frags]
        rechazado_en_origen = len(frags) == 0
        if rechazado_en_origen:
            rechazos_adversos += 1
        estado_str = "CORTADO EN ORIGEN" if rechazado_en_origen else f"DEJÓ PASAR {len(frags)} FRAGS"
        print(
            f"  [Adverso #{caso['id']:02d} ({caso['tipo']}) - {estado_str}] "
            f"Recuperados: {codigos}"
        )

    hit_rate = aciertos_nominales / len(nominales) if nominales else 0.0
    tasa_rechazo = rechazos_adversos / len(adversos) if adversos else 0.0

    print(
        f"RESULTADO -> Hit Rate @ {limite}: {hit_rate:.1%} ({aciertos_nominales}/{len(nominales)}) | "
        f"Rechazo en Origen de Adversos: {tasa_rechazo:.1%} ({rechazos_adversos}/{len(adversos)})"
    )
    return {"hit_rate": hit_rate, "tasa_rechazo_adversos": tasa_rechazo}


if __name__ == "__main__":
    ingestar_corpus_json()
    casos_eval = json.loads(RUTA_CASOS.read_text(encoding="utf-8"))
    rec = RecuperadorRAG()

    # Comparamos el efecto de distintos umbrales de distancia máxima:
    # 1. Sin umbral (None): alto Hit Rate, pero 0% de rechazo en origen ante ruido.
    # 2. Umbral calibrado (0.48): mantiene el Hit Rate alto y corta en origen las consultas ajenas.
    # 3. Umbral excesivamente estricto (0.20): rechaza todo, hundiendo el Hit Rate de consultas legítimas.
    for umbral in (None, 0.48, 0.20):
        evaluar_con_umbral(rec, casos_eval, limite=3, distancia_maxima=umbral)
