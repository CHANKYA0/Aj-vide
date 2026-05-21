class ImageProvider:
    def generate_image(self, prompt: str, model: str | None = None, **kwargs) -> dict:
        raise NotImplementedError
