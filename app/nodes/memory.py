from app.memory.pinecone_memory import get_brand_memory


def memory_node(state):
    memory = get_brand_memory(state["brand_id"])

    docs = memory.similarity_search("brand voice tone instagram content rules", k=3)

    context = "\n".join(d.page_content for d in docs)

    return {"brand_memory_context": context}
