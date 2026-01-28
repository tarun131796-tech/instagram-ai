from langchain_core.prompts import PromptTemplate
from app.utils.load_prompt import load_prompt
from app.memory.pinecone_memory import get_brand_memory


def brand_node(state, llm) -> dict:
    template = load_prompt("app/prompts/brand.txt")
    prompt = PromptTemplate.from_template(template)

    response = llm.invoke(
        prompt.format(brand_description=f"Brand name: {state.brand_name}")
    )

    brand_strategy = response.content.strip()

    # ---- Memory write (safe) ----
    memory = get_brand_memory(state.brand_id)
    try:
        memory.add_texts([brand_strategy], metadatas=[{"type": "brand_strategy"}])
    except Exception as e:
        print(f"⚠️ Memory write skipped: {e}")

    return {"brand_strategy": brand_strategy}
