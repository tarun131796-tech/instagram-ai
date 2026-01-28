from pathlib import Path


def load_prompt(path: str) -> str:
    """
    Safely load prompt text files.
    Avoids deprecated PromptTemplate.from_file usage.
    """
    return Path(path).read_text(encoding="utf-8")
