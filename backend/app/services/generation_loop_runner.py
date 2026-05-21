from app.services.ai_router import AIRouter


class GenerationLoopRunner:
    def __init__(self) -> None:
        self.ai = AIRouter()

    def run(self, project: dict, chunk_words: int = 500, max_steps: int = 50) -> dict:
        steps = 0
        while steps < max_steps and project["generated_words"] < project["target_words"] and project["status"] == "running":
            _ = self.ai.text("writer_model", f"Write {chunk_words} words for {project['title']}")
            project["generated_words"] += min(chunk_words, project["target_words"] - project["generated_words"])
            steps += 1
        if project["generated_words"] >= project["target_words"]:
            project["status"] = "completed"
        return {"steps": steps, "project": project}
