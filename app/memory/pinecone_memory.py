import os
from typing import List

# Optional imports (do NOT fail app)
try:
    from pinecone import Pinecone
    from langchain_ollama import OllamaEmbeddings
    from langchain_pinecone import PineconeVectorStore
except Exception:
    Pinecone = None


class NoOpMemory:
    """Fallback memory when Pinecone is not configured"""

    def add_texts(self, texts: List[str], metadatas=None):
        return

    def similarity_search(self, query: str, k: int = 4):
        return []


def get_brand_memory(brand_id: str):
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    # ---- Fallback mode ----
    if not api_key or not index_name or Pinecone is None:
        print("⚠️ Pinecone not configured. Running without long-term memory.")
        return NoOpMemory()

    # ---- Real Pinecone memory ----
    pc = Pinecone(api_key=api_key)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    )

    index = pc.Index(index_name)

    return PineconeVectorStore(index=index, embedding=embeddings, namespace=brand_id)
