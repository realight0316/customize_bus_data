import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    API_PREFIX: str = '/api'
    BACKEND_ORIGINS: str = os.getenv("BACKEND_ORIGINS", "http://localhost:8080")

    KEYCODE_ENCODING: str = os.getenv("keycode_encoding", "")
    KEYCODE_DECODING: str = os.getenv("keycode_decoding", "")

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")

settings = Settings()