from dotenv import load_dotenv

load_dotenv()

from app.graph import build_graph


if __name__ == "__main__":
    graph = build_graph()

    graph.invoke({"brand_id": "clean_skincare_india", "brand_name": "YourBrandName"})
