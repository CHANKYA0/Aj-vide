from app.services.providers.base import AIProvider


class StubProvider(AIProvider):
    def generate_text(self, prompt: str, model: str | None = None, **kwargs) -> str:
        return f"[stub:{model or 'default'}] {prompt[:300]}"

    def generate_json(self, prompt: str, model: str | None = None, schema: dict | None = None, **kwargs) -> dict:
        return {"model": model or "default", "prompt_preview": prompt[:120], "schema": schema or {}}

    def chat(self, messages: list[dict], model: str | None = None, **kwargs) -> str:
        return f"[chat-stub:{model or 'default'}] messages={len(messages)}"
