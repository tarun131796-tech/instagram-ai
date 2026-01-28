from langgraph.graph import StateGraph
from app.state import GraphState

from app.nodes.brand import brand_node
from app.nodes.planner import planner_node
from app.nodes.creator import creator_node
from app.nodes.export import export_node
from app.llm import get_llm


def build_graph():
    llm = get_llm()

    graph = StateGraph(GraphState)

    graph.add_node("brand", lambda s: brand_node(s, llm))
    graph.add_node("planner", lambda s: planner_node(s, llm))
    graph.add_node("creator", lambda s: creator_node(s, llm))
    graph.add_node("export", export_node)

    graph.set_entry_point("brand")
    graph.add_edge("brand", "planner")
    graph.add_edge("planner", "creator")
    graph.add_edge("creator", "export")

    graph.set_finish_point("export")

    return graph.compile()
