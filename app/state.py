from typing import List, Dict, Optional
from pydantic import BaseModel


class GraphState(BaseModel):
    brand_id: str
    brand_name: str

    brand_strategy: Optional[str] = None
    content_plan: Optional[str] = None

    posts: List[Dict] = []
