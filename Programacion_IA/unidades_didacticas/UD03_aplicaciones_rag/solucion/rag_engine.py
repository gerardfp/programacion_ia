import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class RAGEngineSolucion:
    def __init__(self, collection_name: str = "manuales_tecnicos"):
        self.collection_name = collection_name
        self.documentos = []
        logger.info("Inicializando Motor RAG en memoria/disco...")

    def indexar_documentos(self, textos: List[str], metadatos: List[Dict[str, Any]]):
        for idx, (txt, meta) in enumerate(zip(textos, metadatos)):
            self.documentos.append({"id": str(idx), "texto": txt, "meta": meta})
        logger.info("Indexados %d fragmentos correctamente.", len(textos))

    def buscar_similares(self, consulta: str, top_k: int = 2) -> List[Dict[str, Any]]:
        # Coincidencia semántica simple/demostrativa
        consulta_lower = consulta.lower()
        relevantes = [
            doc for doc in self.documentos if any(w in doc["texto"].lower() for w in consulta_lower.split())
        ]
        return relevantes[:top_k] if relevantes else self.documentos[:top_k]

    def responder(self, consulta: str) -> Dict[str, Any]:
        contextos = self.buscar_similares(consulta)
        contexto_str = "\n---\n".join([c["texto"] for c in contextos])
        
        prompt_final = (
            f"Basándote EXCLUSIVAMENTE en el siguiente contexto:\n{contexto_str}\n\n"
            f"Responde a la pregunta: {consulta}\n"
            f"Si la información no está en el contexto, di 'No dispongo de información suficiente'."
        )
        
        return {
            "pregunta": consulta,
            "prompt_armado": prompt_final,
            "fuentes": [c["meta"] for c in contextos]
        }

if __name__ == "__main__":
    rag = RAGEngineSolucion()
    rag.indexar_documentos(
        ["El servidor PostgreSQL escucha en el puerto 5432.", "El servicio Ollama escucha en el puerto 11434."],
        [{"fuente": "config_db.md"}, {"fuente": "config_ollama.md"}]
    )
    res = rag.responder("¿En qué puerto escucha PostgreSQL?")
    print("Respuesta generada:", res)
