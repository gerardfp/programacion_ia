# resources/ud02/tests/test_rag.py
"""
Suite de pruebas automatizadas con pytest para la UD02 (Etapa 6).
Combina:
  1. Pruebas unitarias deterministas sobre el contrato Pydantic y la verificación de citas
     (no requieren llamar a Ollama ni a PostgreSQL).
  2. Pruebas de integración sobre el recuperador con pgvector (control de acceso en SQL,
     umbral de distancia máxima y evaluación Hit Rate @ 3 sobre dataset cerrado).
"""

import json
from pathlib import Path
import pytest
from pydantic import ValidationError
from src.asistente import verificar_grounding_respuesta
from src.contratos import RespuestaRAG
from src.ingesta import ingestar_corpus_json
from src.recuperador import RecuperadorRAG

RUTA_CASOS = Path(__file__).resolve().parent.parent / "datos" / "casos_evaluacion.json"


# ======================================================================================
# BLOQUE 1: TESTS UNITARIOS DETERMINISTAS DE CONTRATO Y GROUNDING (Sin LLM ni BD)
# ======================================================================================

def test_contrato_respuesta_rag_nominal():
    raw_json = (
        '{"estado": "RESPONDIDO", '
        '"respuesta": "La Serie Marina tiene clasificación antideslizante Clase C3.", '
        '"citas": ["DOC-TEC-01"]}'
    )
    obj = RespuestaRAG.model_validate_json(raw_json)
    assert obj.estado == "RESPONDIDO"
    assert obj.citas == ["DOC-TEC-01"]


def test_contrato_rechaza_estado_no_permitido():
    raw_json = '{"estado": "INVENTADO", "respuesta": "Texto válido", "citas": []}'
    with pytest.raises(ValidationError, match="estado"):
        RespuestaRAG.model_validate_json(raw_json)


def test_grounding_acepta_citas_dentro_del_contexto_recuperado():
    propuesta = RespuestaRAG(
        estado="RESPONDIDO",
        respuesta="El precio oficial es de 32 EUR/m2 con descuento del 8% por palé.",
        citas=["DOC-COM-01"],
    )
    verificada = verificar_grounding_respuesta(
        propuesta, codigos_autorizados={"DOC-COM-01", "DOC-COM-02"}
    )
    assert verificada.estado == "RESPONDIDO"
    assert verificada.citas == ["DOC-COM-01"]


def test_grounding_rechaza_cita_alucinada_fuera_del_contexto():
    # TODO (Etapa 6): Comprueba que si el LLM propone estado="RESPONDIDO" pero cita un documento
    # que NO estaba entre los fragmentos recuperados (ej. citas=["DOC-FANTASMA-99"] cuando
    # codigos_autorizados={"DOC-TEC-01", "DOC-TEC-02"}), verificar_grounding_respuesta()
    # rechaza la propuesta devolviendo estado="NO_DATA" y citas=[].
    pytest.fail("TODO: pendiente de implementar en la Etapa 6")


def test_grounding_rechaza_respondido_con_lista_de_citas_vacia():
    # TODO (Etapa 6): Comprueba que si el LLM propone estado="RESPONDIDO" pero deja citas=[],
    # verificar_grounding_respuesta() lo convierte en estado="NO_DATA".
    pytest.fail("TODO: pendiente de implementar en la Etapa 6")


def test_grounding_limpia_citas_residuales_cuando_estado_es_no_data():
    # TODO (Etapa 6): Comprueba que si el LLM devuelve estado="NO_DATA" pero incluye por error
    # citas=["DOC-TEC-01"], verificar_grounding_respuesta() devuelve estado="NO_DATA" y citas=[].
    pytest.fail("TODO: pendiente de implementar en la Etapa 6")


# ======================================================================================
# BLOQUE 2: TESTS DE RECUPERACIÓN, SEGURIDAD EN ORIGEN Y HIT RATE CON PGVECTOR
# ======================================================================================

@pytest.fixture(scope="module")
def recuperador_preparado() -> RecuperadorRAG:
    """Asegura que el corpus está indexado en PostgreSQL antes de ejecutar los tests de BD."""
    ingestar_corpus_json()
    return RecuperadorRAG()


def test_aislamiento_estricto_en_sql_impide_fuga_de_gerencia(recuperador_preparado: RecuperadorRAG):
    """
    Un usuario del departamento 'comercial' que pregunta directamente por secretos de 'gerencia'
    jamás debe recibir fragmentos con departamento != 'comercial'.
    """
    pregunta_maliciosa = (
        "¿Cuál es el coste industrial en horno de la Serie Marina, el margen bruto del 70,6% "
        "y el descuento confidencial del 35% autorizado por dirección?"
    )
    fragmentos = recuperador_preparado.buscar_fragmentos_autorizados(
        pregunta=pregunta_maliciosa,
        depto_usuario="comercial",
        limite=5,
    )
    for f in fragmentos:
        assert f.departamento == "comercial"
        assert f.codigo_doc != "DOC-GER-01"


def test_umbral_distancia_descarta_consulta_fuera_de_dominio(recuperador_preparado: RecuperadorRAG):
    # TODO (Etapa 6): Comprueba que ante una pregunta completamente ajena al catálogo cerámico
    # (ej. "¿Qué ingredientes lleva la paella valenciana tradicional?"), llamar a
    # buscar_fragmentos_autorizados(..., distancia_maxima=0.48) devuelve una lista vacía [].
    pytest.fail("TODO: pendiente de implementar en la Etapa 6")


def test_evaluacion_hit_rate_en_dataset_cerrado(recuperador_preparado: RecuperadorRAG):
    # TODO (Etapa 6): Carga los casos de prueba desde RUTA_CASOS ('datos/casos_evaluacion.json').
    # 1. Filtra los casos donde tipo == "nominal".
    # 2. Para cada caso nominal, invoca buscar_fragmentos_autorizados(pregunta, depto_usuario, limite=3, distancia_maxima=0.48).
    # 3. Calcula el Hit Rate @ 3 (proporción de casos nominales en los que 'esperado_codigo_doc'
    #    aparece entre los códigos recuperados) y verifica con assert que hit_rate >= 0.80.
    pytest.fail("TODO: pendiente de implementar en la Etapa 6")
