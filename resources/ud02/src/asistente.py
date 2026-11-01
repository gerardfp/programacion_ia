# resources/ud02/src/asistente.py
"""
Coordinador del Asistente RAG:
1. Recupera fragmentos autorizados desde PostgreSQL.
2. Cortocircuita con abstención determinista (NO_DATA) si no hay fragmentos relevantes.
3. Inyecta el contexto delimitado y fuerza salida estructurada con RespuestaRAG.
4. Verifica en la frontera que las citas propuestas pertenezcan a los fragmentos recuperados.
"""

import httpx
from pydantic import ValidationError
from src.contratos import FragmentoRecuperado, RespuestaRAG
from src.recuperador import RecuperadorRAG


def construir_bloque_contexto(fragmentos: list[FragmentoRecuperado]) -> str:
    """Formatea los fragmentos recuperados identificando explícitamente su código y fuente."""
    bloques = []
    for f in fragmentos:
        bloques.append(
            f"[{f.codigo_doc}] (Fuente: {f.fuente} | Título: {f.titulo}):\n{f.contenido}"
        )
    return "\n\n".join(bloques)


def verificar_grounding_respuesta(
    propuesta: RespuestaRAG,
    codigos_autorizados: set[str],
) -> RespuestaRAG:
    """
    Frontera de verificación de citas (Grounding Check).

    Nota para Etapa 5 (Mejora B):
    En el RAG básico de la Etapa 3, esta función devuelve la propuesta tal cual tras pasar
    la validación sintáctica de Pydantic.
    En la Etapa 5 deberás endurecer esta función para garantizar que:
      1. Si propuesta.estado == 'NO_DATA', la lista de citas quede siempre vacía ([]).
      2. Si propuesta.estado == 'RESPONDIDO', contenga al menos una cita y TODAS las citas
         propuestas existan dentro de 'codigos_autorizados' (evitando citas inventadas).
         En caso contrario, debe devolver una RespuestaRAG con estado='NO_DATA'.
    """
    return propuesta


def responder_pregunta(
    recuperador: RecuperadorRAG,
    pregunta: str,
    depto_usuario: str,
    limite: int = 3,
    distancia_maxima: float | None = None,
    chat_model: str = "qwen2.5:0.5b",
) -> tuple[RespuestaRAG, list[FragmentoRecuperado]]:
    """
    Ejecuta el flujo completo RAG y devuelve tanto la RespuestaRAG validada
    como la lista de fragmentos recuperados para inspección/auditoría.
    """
    fragmentos = recuperador.buscar_fragmentos_autorizados(
        pregunta=pregunta,
        depto_usuario=depto_usuario,
        limite=limite,
        distancia_maxima=distancia_maxima,
    )

    # Control determinista en la aplicación: si no se recuperan fragmentos,
    # nos abstenemos de inmediato sin llamar al LLM generativo.
    if not fragmentos:
        abstencion_directa = RespuestaRAG(
            estado="NO_DATA",
            respuesta="NO_DATA: No se han encontrado documentos autorizados relevantes para esta consulta.",
            citas=[],
        )
        return abstencion_directa, []

    contexto_formateado = construir_bloque_contexto(fragmentos)
    codigos_recuperados = {f.codigo_doc for f in fragmentos}

    system_prompt = (
        "Eres el asistente técnico y documental de Cerámicas Benigasló. "
        "Responde a la pregunta del usuario utilizando EXCLUSIVAMENTE la información contenida "
        "dentro del bloque <contexto>. "
        "Si la respuesta aparece en el contexto, usa estado='RESPONDIDO' e incluye en 'citas' "
        "los códigos exactos de los documentos utilizados (por ejemplo, 'DOC-TEC-01'). "
        "Si el bloque <contexto> NO contiene los datos necesarios para responder a la pregunta, "
        "no inventes ni supongas nada: devuelve obligatoriamente estado='NO_DATA' y citas=[]."
    )

    user_prompt = (
        f"<contexto>\n{contexto_formateado}\n</contexto>\n\n"
        f"Pregunta del usuario: {pregunta}"
    )

    try:
        response = httpx.post(
            f"{recuperador.ollama_url}/api/chat",
            json={
                "model": chat_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "format": RespuestaRAG.model_json_schema(),
                "stream": False,
                "options": {"temperature": 0.0},
            },
            timeout=30.0,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        raise ConnectionError(f"Error de comunicación con Ollama ({chat_model}): {e}") from e

    raw_content = response.json()["message"]["content"]

    try:
        propuesta = RespuestaRAG.model_validate_json(raw_content)
    except ValidationError:
        return (
            RespuestaRAG(
                estado="NO_DATA",
                respuesta="NO_DATA: La propuesta del modelo incumplió el contrato de salida.",
                citas=[],
            ),
            fragmentos,
        )

    respuesta_verificada = verificar_grounding_respuesta(propuesta, codigos_recuperados)
    return respuesta_verificada, fragmentos
