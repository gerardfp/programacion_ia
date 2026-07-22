import chromadb
import httpx
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self, chroma_path: str = "./chroma_db"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.client.get_or_create_collection("documentos_centro")

    def responder_consulta(self, pregunta: str) -> str:
        q_vector = self.model.encode(pregunta).tolist()
        res = self.collection.query(query_embeddings=[q_vector], n_results=2)
        docs = res.get("documents", [[]])[0]
        contexto = "
---
".join(docs) if docs else "Sin contexto"
        prompt = f"Contexto:
{contexto}

Pregunta: {pregunta}"
        resp = httpx.post("http://localhost:11434/api/generate", json={"model": "llama3.2:3b", "prompt": prompt, "stream": False})
        return resp.json().get("response", "")
