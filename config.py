import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("TOKEN")
        self.DB_URL = os.getenv("DATABASE_URL") or os.getenv("DB_URL")

        if not self.BOT_TOKEN:
            raise RuntimeError("TOKEN not set in .env")

        if not self.DB_URL:
            raise RuntimeError("DATABASE_URL/DB_URL not set in .env")


settings = Settings()
