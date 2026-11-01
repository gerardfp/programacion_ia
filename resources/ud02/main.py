# resources/ud02/main.py
"""
Script principal de prueba y diagnóstico del sistema RAG (Etapas 3 y 5).
Ejecuta cuatro escenarios representativos mostrando los fragmentos recuperados,
sus distancias coseno y la respuesta validada mediante RespuestaRAG.
"""

from src.asistente import responder_pregunta
from src.ingesta import ingestar_corpus_json
from src.recuperador import RecuperadorRAG

ESCENARIOS = [
    {
        "nombre": "Escenario 1: Consulta técnica nominal (Autorizada)",
        "depto_usuario": "tecnico",
        "pregunta": "¿Qué suelo cerámico podemos instalar alrededor de una piscina para evitar resbalones?",
    },
    {
        "nombre": "Escenario 2: Consulta comercial nominal (Autorizada)",
        "depto_usuario": "comercial",
        "pregunta": "¿Cuál es el precio oficial por m2 de la Serie Marina y qué descuento tiene por palé?",
    },
    {
        "nombre": "Escenario 3: Intento de consultar datos confidenciales de otro departamento",
        "depto_usuario": "comercial",
        "pregunta": "¿A cuántos euros por tonelada pagamos la arcilla blanca atomizada y el gas de los hornos?",
    },
    {
        "nombre": "Escenario 4: Consulta completamente fuera de dominio",
        "depto_usuario": "comercial",
        "pregunta": "¿Qué ingredientes lleva la receta tradicional de la paella valenciana?",
    },
]


def main() -> None:
    print("Verificando e indexando el corpus en PostgreSQL + pgvector...")
    ingestar_corpus_json()

    recuperador = RecuperadorRAG()

    for esc in ESCENARIOS:
        print("\n" + "=" * 80)
        print(f"{esc['nombre']}")
        print(f"Usuario (depto='{esc['depto_usuario']}') pregunta: {esc['pregunta']}")
        print("-" * 80)

        respuesta, fragmentos = responder_pregunta(
            recuperador=recuperador,
            pregunta=esc["pregunta"],
            depto_usuario=esc["depto_usuario"],
            limite=3,
            distancia_maxima=0.48,  # En Etapa 3 aún no surte efecto hasta completar Mejora A en Etapa 5
        )

        if not fragmentos:
            print("Fragmentos recuperados: [] (Cortocircuito en origen: NO se llamó al LLM)")
        else:
            print(f"Fragmentos recuperados de PostgreSQL ({len(fragmentos)}):")
            for f in fragmentos:
                print(
                    f"  -> [{f.codigo_doc}] depto={f.departamento:<9} | "
                    f"distancia={f.distancia:.4f} | {f.titulo}"
                )

        print("\nRespuesta final entregada por la aplicación:")
        print(f"  Estado:    {respuesta.estado}")
        print(f"  Citas:     {respuesta.citas}")
        print(f"  Respuesta: {respuesta.respuesta}")


if __name__ == "__main__":
    main()
