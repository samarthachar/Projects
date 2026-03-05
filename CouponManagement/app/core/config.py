import os

from pydantic_settings import BaseSettings # type: ignore
from dotenv import load_dotenv # type: ignore


class Settings(BaseSettings):
    app_name: str = "Coupon Management API"
    environment: str = "dev"

    secret_key: str = "change_me"
    
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()