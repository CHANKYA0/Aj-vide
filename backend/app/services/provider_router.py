from app.services.providers.stub_provider import StubProvider


class ProviderRouter:
    def __init__(self) -> None:
        self.provider = StubProvider()
        self.task_model_map = {
            "writer_model": "gemini-2.5-pro",
            "final_rewrite_model": "gpt-5.5",
            "chatbot_model": "gpt-5.5-mini",
        }

    def generate_text(self, task: str, prompt: str) -> str:
        model = self.task_model_map.get(task)
        return self.provider.generate_text(prompt=prompt, model=model)
