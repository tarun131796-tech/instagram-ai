import re
from langchain_core.prompts import PromptTemplate
from app.utils.load_prompt import load_prompt


def creator_node(state, llm) -> dict:
    template = load_prompt("app/prompts/creator.txt")
    prompt = PromptTemplate.from_template(template)

    response = llm.invoke(
        prompt.format(
            brand_strategy=state.brand_strategy,
            brand_memory="",
            content_plan=state.content_plan,
        )
    )

    text = response.content.strip()
    posts = []

    blocks = text.split("### POST")

    for idx, block in enumerate(blocks):
        if not block.strip():
            continue

        post = {
            "post_id": f"post_{len(state.posts) + idx + 1}",
            "post_type": "reel" if "REEL_SCENES" in block else "carousel",
            "caption": {},
            "hashtags": [],
        }

        # ---- CAPTION ----
        hook = re.search(r"Hook:(.*)", block)
        body = re.search(r"Full caption:(.*)", block, re.S)
        cta = re.search(r"CTA:(.*)", block)

        post["caption"] = {
            "hook": hook.group(1).strip() if hook else "",
            "body": body.group(1).strip() if body else "",
            "cta": cta.group(1).strip() if cta else "",
        }

        # ---- HASHTAGS ----
        post["hashtags"] = re.findall(r"#\w+", block)

        # ---- REEL ----
        if "REEL_SCENES" in block:
            scenes = []
            scene_blocks = re.findall(
                r"Scene Number:\s*(\d+).*?"
                r"Duration:\s*(\d+)s.*?"
                r"Image Prompt:(.*?)"
                r"On-screen Text:(.*?)"
                r"Transition:",
                block,
                re.S,
            )

            for s in scene_blocks:
                scenes.append(
                    {
                        "scene_id": int(s[0]),
                        "duration": int(s[1]),
                        "image_prompt": s[2].strip(),
                        "overlay_text": s[3].strip(),
                    }
                )

            post["reel"] = {"aspect_ratio": "9:16", "scenes": scenes}

        # ---- CAROUSEL ----
        else:
            slides = []
            slide_prompts = re.findall(r"Prompt:(.*?)Style:", block, re.S)

            for i, p in enumerate(slide_prompts):
                slides.append({"slide_id": i + 1, "image_prompt": p.strip()})

            post["carousel"] = {"aspect_ratio": "4:5", "slides": slides}

        posts.append(post)

    return {"posts": state.posts + posts}
