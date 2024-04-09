# app/config/settings.py
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017/"
    mongodb_db_name: str = "STUDENT_DB"
    port:int = 8000
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()