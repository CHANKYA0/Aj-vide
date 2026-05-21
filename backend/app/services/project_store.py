from app.schemas import PROJECT_PRESETS, ProjectCreate


class ProjectStore:
    def __init__(self) -> None:
        self.projects: dict[int, dict] = {}
        self.next_id = 1

    def create(self, payload: ProjectCreate) -> dict:
        preset = payload.preset.model_dump() if payload.preset else PROJECT_PRESETS.get(payload.preset_name or "Full Novel", PROJECT_PRESETS["Full Novel"])
        pid = self.next_id
        self.next_id += 1
        project = {
            "id": pid,
            "title": payload.title,
            "genre": payload.genre,
            "mode": payload.mode,
            "project_type": payload.project_type,
            "pages": preset["pages"],
            "target_words": preset["target_words"],
            "chapters": preset["chapters"],
            "generated_words": 0,
            "status": "idle",
        }
        self.projects[pid] = project
        return project

    def list(self): return list(self.projects.values())
    def get(self, pid:int): return self.projects[pid]
    def save(self, project:dict): self.projects[project['id']] = project

project_store = ProjectStore()
