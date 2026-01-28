from langchain_core.prompts import PromptTemplate
from app.utils.load_prompt import load_prompt


def planner_node(state, llm) -> dict:
    template = load_prompt("app/prompts/planner.txt")
    prompt = PromptTemplate.from_template(template)

    response = llm.invoke(prompt.format(brand_strategy=state.brand_strategy))

    content_plan = response.content.strip()

    return {"content_plan": content_plan}
