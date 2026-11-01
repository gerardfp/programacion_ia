# resources/ud02/src/contratos.py
"""
Contratos de datos Pydantic para el sistema RAG (UD02).
Define tanto la representación tipada de los fragmentos recuperados de PostgreSQL
como el esquema estructurado de salida que se exige al modelo generativo.
"""

from typing import Literal
from pydantic import BaseModel, Field

DepartamentoValido = Literal["comercial", "tecnico", "gerencia"]


class FragmentoRecuperado(BaseModel):
    """Representa un fragmento documental (chunk) recuperado desde PostgreSQL + pgvector."""

    codigo_doc: str = Field(description="Identificador único del fragmento (ej. DOC-TEC-01)")
    titulo: str = Field(description="Título descriptivo del fragmento")
    fuente: str = Field(description="Nombre del archivo o documento de origen")
    departamento: DepartamentoValido = Field(description="Departamento propietario del documento")
    contenido: str = Field(description="Texto completo del fragmento documental")
    distancia: float = Field(description="Distancia coseno respecto a la consulta (0.0 = idéntico)")


class RespuestaRAG(BaseModel):
    """
    Contrato de salida estructurada para la síntesis del asistente RAG.
    Se envía como JSON Schema en el parámetro 'format' de Ollama y se valida en la frontera.
    """

    estado: Literal["RESPONDIDO", "NO_DATA"] = Field(
        description=(
            "Usa 'RESPONDIDO' únicamente si el contexto proporcionado contiene datos suficientes "
            "para responder la pregunta. Usa 'NO_DATA' si el contexto no contiene la respuesta."
        )
    )
    respuesta: str = Field(
        description=(
            "Respuesta redactada utilizando exclusivamente los datos del contexto recuperado. "
            "Si estado es 'NO_DATA', indica brevemente que no se dispone de información en las fuentes."
        ),
        min_length=5,
    )
    citas: list[str] = Field(
        default_factory=list,
        description=(
            "Lista de códigos de documento exactos utilizados para fundamentar la respuesta "
            "(por ejemplo: ['DOC-TEC-01']). Si estado es 'NO_DATA', debe ser una lista vacía []."
        ),
    )
