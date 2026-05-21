from sqlalchemy import JSON, Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class TimestampMixin:
    created_at: Mapped[str] = mapped_column(DateTime, server_default=func.now(), index=True)


class User(Base, TimestampMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(32), default="user")


class BookProject(Base, TimestampMixin):
    __tablename__ = "book_projects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), index=True)
    title: Mapped[str] = mapped_column(String(255))
    genre: Mapped[str] = mapped_column(String(100), index=True)
    mode: Mapped[str] = mapped_column(String(100), default="fiction")
    status: Mapped[str] = mapped_column(String(32), default="idle", index=True)
    settings: Mapped[dict] = mapped_column(JSON, default={})
    progress_words: Mapped[int] = mapped_column(Integer, default=0)
    target_words: Mapped[int] = mapped_column(Integer, default=0)


class Chapter(Base, TimestampMixin):
    __tablename__ = "chapters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("book_projects.id"), index=True)
    chapter_number: Mapped[int] = mapped_column(Integer, index=True)
    title: Mapped[str] = mapped_column(String(255), default="Untitled")
    chapter_type: Mapped[str] = mapped_column(String(64), default="fiction_chapter")
    target_words: Mapped[int] = mapped_column(Integer, default=2000)
    generated_words: Mapped[int] = mapped_column(Integer, default=0)
    metadata: Mapped[dict] = mapped_column(JSON, default={})


class DraftChunk(Base, TimestampMixin):
    __tablename__ = "draft_chunks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("book_projects.id"), index=True)
    chapter_id: Mapped[int] = mapped_column(Integer, ForeignKey("chapters.id"), index=True)
    content: Mapped[str] = mapped_column(Text)
    word_count: Mapped[int] = mapped_column(Integer)
    summary: Mapped[str] = mapped_column(Text, default="")


class StoryMemory(Base, TimestampMixin):
    __tablename__ = "story_memory"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("book_projects.id"), index=True)
    memory_type: Mapped[str] = mapped_column(String(64))
    memory_text: Mapped[str] = mapped_column(Text)


class AIModelPricing(Base, TimestampMixin):
    __tablename__ = "ai_model_pricing"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    provider_name: Mapped[str] = mapped_column(String(50), index=True)
    model_name: Mapped[str] = mapped_column(String(100), index=True)
    model_type: Mapped[str] = mapped_column(String(50), index=True)
    input_cost_per_million: Mapped[int] = mapped_column(Integer, default=0)
    output_cost_per_million: Mapped[int] = mapped_column(Integer, default=0)


class AIUsageLog(Base, TimestampMixin):
    __tablename__ = "ai_usage_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    book_id: Mapped[int] = mapped_column(Integer, index=True)
    task_type: Mapped[str] = mapped_column(String(64), index=True)
    provider_name: Mapped[str] = mapped_column(String(64), index=True)
    model_name: Mapped[str] = mapped_column(String(100), index=True)
    input_tokens: Mapped[int] = mapped_column(Integer, default=0)
    output_tokens: Mapped[int] = mapped_column(Integer, default=0)
    estimated_cost_usd: Mapped[int] = mapped_column(Integer, default=0)


class ExportJob(Base, TimestampMixin):
    __tablename__ = "export_jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, index=True)
    export_type: Mapped[str] = mapped_column(String(32), index=True)
    status: Mapped[str] = mapped_column(String(32), default="pending", index=True)
    file_url: Mapped[str] = mapped_column(String(500), default="")


class ImportJob(Base, TimestampMixin):
    __tablename__ = "import_jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    book_id: Mapped[int] = mapped_column(Integer, index=True)
    file_name: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(32), default="pending", index=True)


class Job(Base, TimestampMixin):
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(Integer, index=True)
    status: Mapped[str] = mapped_column(String(32), default="queued", index=True)
    progress: Mapped[dict] = mapped_column(JSON, default={})
