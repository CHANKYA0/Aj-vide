class AIProvider:
    def generate_text(self, prompt: str, model: str | None = None, **kwargs) -> str:
        raise NotImplementedError

    def generate_json(self, prompt: str, model: str | None = None, schema: dict | None = None, **kwargs) -> dict:
        raise NotImplementedError

    def chat(self, messages: list[dict], model: str | None = None, **kwargs) -> str:
        raise NotImplementedError
