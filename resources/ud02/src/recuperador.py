# resources/ud02/src/recuperador.py
"""
Servicio de recuperación semántica sobre PostgreSQL + pgvector con Control de Acceso en Origen.
"""

import httpx
import psycopg
from src.contratos import FragmentoRecuperado

DEPARTAMENTOS_VALIDOS = {"comercial", "tecnico", "gerencia"}


class RecuperadorRAG:
    def __init__(
        self,
        db_url: str = "postgresql://postgres:postgres@localhost:5432/ceramica_rag",
        ollama_url: str = "http://localhost:11434",
        embed_model: str = "bge-m3",
    ):
        self.db_url = db_url
        self.ollama_url = ollama_url
        self.embed_model = embed_model

    def generar_embedding(self, texto: str) -> list[float]:
        """Convierte la consulta del usuario en un vector utilizando el mismo modelo de la ingesta."""
        try:
            response = httpx.post(
                f"{self.ollama_url}/api/embed",
                json={"model": self.embed_model, "input": texto},
                timeout=20.0,
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise ConnectionError(f"Error de comunicación con el motor de embeddings: {e}") from e

        return response.json()["embeddings"][0]

    def buscar_fragmentos_autorizados(
        self,
        pregunta: str,
        depto_usuario: str,
        limite: int = 3,
        distancia_maxima: float | None = None,
    ) -> list[FragmentoRecuperado]:
        """
        Recupera los fragmentos más cercanos a la pregunta aplicando el filtro de autorización
        en origen (dentro de la cláusula WHERE de SQL, antes de ORDER BY y LIMIT).

        Nota para Etapa 5 (Mejora A):
        En la versión inicial de la Etapa 3, 'distancia_maxima' no se filtra en la consulta SQL,
        por lo que PostgreSQL devuelve siempre 'limite' filas aunque su distancia sea muy alta.
        En la Etapa 5 deberás incorporar el filtro de umbral de distancia máxima.
        """
        if depto_usuario not in DEPARTAMENTOS_VALIDOS:
            raise ValueError(f"Departamento no válido o no autorizado: {depto_usuario!r}")

        vector_pregunta = self.generar_embedding(pregunta)

        # Consulta SQL parametrizada con filtrado de acceso en origen (WHERE departamento = %s)
        sql = """
            SELECT codigo_doc, titulo, fuente, departamento, contenido,
                   (embedding <=> %s::vector) AS distancia
            FROM fragmentos_documento
            WHERE departamento = %s
            ORDER BY distancia ASC
            LIMIT %s;
        """

        with psycopg.connect(self.db_url) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vector_pregunta, depto_usuario, limite))
                filas = cur.fetchall()

        return [
            FragmentoRecuperado(
                codigo_doc=f[0],
                titulo=f[1],
                fuente=f[2],
                departamento=f[3],
                contenido=f[4],
                distancia=float(f[5]),
            )
            for f in filas
        ]
