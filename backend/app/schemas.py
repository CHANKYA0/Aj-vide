from pydantic import BaseModel, Field

PROJECT_PRESETS = {
    "Mini Story": {"pages": 15, "target_words": 4000, "chapters": 1},
    "Short Story": {"pages": 30, "target_words": 8000, "chapters": 3},
    "Novella": {"pages": 100, "target_words": 28000, "chapters": 10},
    "Short Novel": {"pages": 180, "target_words": 50000, "chapters": 18},
    "Full Novel": {"pages": 300, "target_words": 85000, "chapters": 30},
    "Long Novel": {"pages": 450, "target_words": 125000, "chapters": 45},
}

class LengthPreset(BaseModel):
    pages: int = Field(gt=0)
    target_words: int = Field(gt=0)
    chapters: int = Field(gt=0)

class ProjectCreate(BaseModel):
    title: str
    genre: str
    mode: str = "fiction"
    project_type: str = "Full Novel"
    preset_name: str | None = None
    preset: LengthPreset | None = None

class RunLoopRequest(BaseModel):
    chunk_words: int = Field(default=500, ge=200, le=2000)
    max_steps: int = Field(default=50, ge=1, le=2000)

class GenericPayload(BaseModel):
    data: dict = Field(default_factory=dict)
