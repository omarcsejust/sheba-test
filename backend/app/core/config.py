from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APPLICATION_NAME: str = "Sheba Backend API"
    APPLICATION_VERSION: str = "1.0.0"
    APPLICATION_DESCRIPTION: str = "This is a sample FastAPI application."
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./dev.db"
    SECRET_KEY: str =  "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "../../.env"

settings = Settings()