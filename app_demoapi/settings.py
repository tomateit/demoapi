from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int
    HF_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
