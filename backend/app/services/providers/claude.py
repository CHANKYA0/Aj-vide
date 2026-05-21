from app.services.providers.base import AIProvider


class ClaudeProvider(AIProvider):
    def generate_text(self, prompt: str, model: str | None = None, **kwargs) -> str:
        return f"[claude:{model}] {prompt[:200]}"

    def generate_json(self, prompt: str, model: str | None = None, schema: dict | None = None, **kwargs) -> dict:
        return {"provider": "claude", "model": model, "data": prompt[:80]}

    def chat(self, messages: list[dict], model: str | None = None, **kwargs) -> str:
        return f"[claude-chat:{model}] {len(messages)} messages"
