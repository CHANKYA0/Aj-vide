from sqlalchemy import select

from app.models import BookProject, Chapter, DraftChunk, Job


class ProjectRepository:
    def __init__(self, db):
        self.db = db

    def create(self, data: dict) -> BookProject:
        row = BookProject(**data)
        self.db.add(row)
        self.db.flush()
        return row

    def get(self, project_id: int) -> BookProject | None:
        return self.db.get(BookProject, project_id)

    def list(self) -> list[BookProject]:
        return list(self.db.scalars(select(BookProject).order_by(BookProject.id.desc())).all())


class ChapterRepository:
    def __init__(self, db):
        self.db = db

    def create_many(self, chapters: list[dict]) -> None:
        self.db.add_all([Chapter(**c) for c in chapters])

    def next_unfinished(self, project_id: int) -> Chapter | None:
        stmt = select(Chapter).where(Chapter.project_id == project_id).order_by(Chapter.chapter_number.asc())
        for ch in self.db.scalars(stmt):
            if ch.generated_words < ch.target_words:
                return ch
        return None


class ChunkRepository:
    def __init__(self, db):
        self.db = db

    def add(self, data: dict) -> DraftChunk:
        row = DraftChunk(**data)
        self.db.add(row)
        self.db.flush()
        return row


class JobRepository:
    def __init__(self, db):
        self.db = db

    def create(self, project_id: int, status: str = "queued", progress: dict | None = None) -> Job:
        row = Job(project_id=project_id, status=status, progress=progress or {})
        self.db.add(row)
        self.db.flush()
        return row

    def get(self, job_id: int) -> Job | None:
        return self.db.get(Job, job_id)
