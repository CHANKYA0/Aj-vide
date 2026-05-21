import uuid


class JobService:
    def __init__(self) -> None:
        self.jobs: dict[str, dict] = {}

    def create(self, project_id: int, payload: dict) -> str:
        job_id = str(uuid.uuid4())
        self.jobs[job_id] = {"job_id": job_id, "project_id": project_id, "status": "queued", "progress": payload}
        return job_id

    def update(self, job_id: str, **kwargs) -> None:
        if job_id in self.jobs:
            self.jobs[job_id].update(kwargs)

    def get(self, job_id: str) -> dict:
        return self.jobs.get(job_id, {"status": "not_found"})

job_service = JobService()
