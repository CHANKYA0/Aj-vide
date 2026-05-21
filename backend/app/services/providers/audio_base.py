class AudioProvider:
    def generate_audio(self, text: str, voice: str | None = None, **kwargs) -> dict:
        raise NotImplementedError
