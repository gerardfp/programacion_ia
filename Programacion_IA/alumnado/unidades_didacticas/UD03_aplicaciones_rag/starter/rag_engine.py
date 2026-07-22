# Starter Code: Motor RAG Mínimo

class SimpleRAG:
    def __init__(self, collection_name: str = "documentos"):
        # TODO: Inicializar cliente local de ChromaDB y colección
        pass

    def indexar_documento(self, doc_id: str, texto: str, metadata: dict = None):
        # TODO: Agregar documento e indexar con modelo de embedding
        pass

    def consultar(self, pregunta: str, top_k: int = 3) -> str:
        # TODO: Búsqueda k-NN en ChromaDB y generación con Ollama
        pass
