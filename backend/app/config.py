from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Book Studio API"
    environment: str = "dev"
    database_url: str = "sqlite:///./aibookstudio.db"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me"
    use_in_memory_store: bool = True


settings = Settings()
