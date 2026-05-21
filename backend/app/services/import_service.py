class Service:
    def run(self, payload: dict) -> dict:
        return {"status": "ok", "payload": payload}
