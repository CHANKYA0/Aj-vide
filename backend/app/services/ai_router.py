from app.services.providers.gemini import GeminiProvider
from app.services.providers.openai import OpenAIProvider
from app.services.providers.claude import ClaudeProvider
from app.services.providers.openrouter import OpenRouterProvider
from app.services.providers.ollama import OllamaProvider


class AIRouter:
    def __init__(self) -> None:
        self.providers = {
            "gemini": GeminiProvider(),
            "openai": OpenAIProvider(),
            "claude": ClaudeProvider(),
            "openrouter": OpenRouterProvider(),
            "ollama": OllamaProvider(),
        }
        self.task_map = {k: ("openai", "gpt-5.5-mini") for k in [
            "writer_model","summary_model","memory_model","critic_model","chatbot_model","research_model",
            "fact_check_model","poetry_model","image_prompt_model","image_generation_model","cover_generation_model",
            "layout_model","ebook_model","marketing_model","video_prompt_model","video_generation_model","voiceover_model",
            "final_rewrite_model","translation_model"
        ]}
        self.task_map["writer_model"] = ("gemini", "gemini-2.5-pro")

    def text(self, task: str, prompt: str) -> str:
        provider_name, model = self.task_map.get(task, ("openai", "gpt-5.5-mini"))
        return self.providers[provider_name].generate_text(prompt=prompt, model=model)
