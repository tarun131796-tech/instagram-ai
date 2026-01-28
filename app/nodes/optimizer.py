from langchain_core.prompts import PromptTemplate


def optimizer_node(state, llm):
    prompt = PromptTemplate.from_file("app/prompts/optimizer.txt")

    res = llm.invoke(prompt.format(posts=state["content_posts"]))

    return {"optimization_notes": res.content}
