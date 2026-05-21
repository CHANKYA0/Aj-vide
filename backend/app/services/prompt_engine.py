from pathlib import Path

PROMPT_DIR = Path(__file__).resolve().parent.parent / "templates" / "prompts"


class PromptEngine:
    def render(self, name: str, **kwargs) -> str:
        template = (PROMPT_DIR / f"{name}.txt").read_text()
        return template.format(**kwargs)
