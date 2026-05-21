from app.schemas import ProjectState
from app.services.provider_router import ProviderRouter


class GenerationLoopRunner:
    def __init__(self, provider_router: ProviderRouter) -> None:
        self.provider_router = provider_router

    def run_until_complete(self, project: ProjectState, chunk_words: int, max_steps: int) -> dict:
        steps = 0
        chunks: list[dict] = []
        while steps < max_steps and project.generated_words < project.target_words:
            chapter = self._next_chapter(project)
            if chapter is None:
                project.status = "completed"
                break
            prompt = (
                f"Write next {chunk_words} words for chapter {chapter.chapter_number} "
                f"of a {project.genre} {project.mode} book titled '{project.title}'."
            )
            text = self.provider_router.generate_text(task="writer_model", prompt=prompt)
            generated = min(chunk_words, project.target_words - project.generated_words)
            chapter.generated_words += generated
            project.generated_words += generated
            chunks.append({"chapter": chapter.chapter_number, "words": generated, "preview": text[:80]})
            steps += 1

        if project.generated_words >= project.target_words:
            project.status = "completed"
        elif steps >= max_steps:
            project.status = "paused"
        else:
            project.status = "running"

        return {
            "project_id": project.id,
            "status": project.status,
            "steps": steps,
            "generated_words": project.generated_words,
            "target_words": project.target_words,
            "chunks": chunks,
        }

    @staticmethod
    def _next_chapter(project: ProjectState):
        for chapter in project.plans:
            if chapter.generated_words < chapter.target_words:
                return chapter
        return None
