class UsageLogger:
    def log(self, **kwargs) -> dict:
        return {"logged": True, **kwargs}
