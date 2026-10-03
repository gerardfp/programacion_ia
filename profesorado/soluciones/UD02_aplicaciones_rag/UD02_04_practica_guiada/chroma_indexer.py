import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documentos_centro")

def indexar_texto(doc_id: str, texto: str, categoria: str):
    vector = model.encode(texto).tolist()
    collection.add(ids=[doc_id], embeddings=[vector], documents=[texto], metadatas=[{"categoria": categoria}])
