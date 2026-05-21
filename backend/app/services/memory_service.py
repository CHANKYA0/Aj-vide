class MemoryService:
    def extract(self, text: str) -> list[dict]:
        return [{"memory_type": "plot_thread", "memory_text": text[:120]}]
