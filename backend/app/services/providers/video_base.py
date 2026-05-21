class VideoProvider:
    def generate_video(self, prompt: str, model: str | None = None, image_url: str | None = None, **kwargs) -> dict:
        raise NotImplementedError
