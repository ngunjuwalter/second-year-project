import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application configuration loaded from environment variables."""

    DATABASE_URL: str = "mysql+pymysql://root:12345@localhost:3306/sample"


settings = Settings()
print("DATABASE_URL:", settings.DATABASE_URL)
