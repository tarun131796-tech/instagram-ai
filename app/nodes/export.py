import json
from datetime import datetime
from pathlib import Path


def export_node(state) -> dict:
    job = {
        "job_id": f"{state.brand_id}_{datetime.now().strftime('%Y%m%d_%H%M')}",
        "brand": {
            "brand_id": state.brand_id,
            "brand_name": state.brand_name,
            "primary_color": "#1E7F6D",
            "secondary_color": "#F2EFEA",
            "font": "default",
        },
        "posts": state.posts,
    }

    Path("content_job.json").write_text(json.dumps(job, indent=2), encoding="utf-8")

    print("✅ content_job.json generated")

    return {}
