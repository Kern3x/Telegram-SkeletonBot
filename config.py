import os

from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class BaseConfig:
    """Base configuration."""

    BOT_TOKEN = os.environ.get("TOKEN")
    DB_URL = ""


class DevelopmentConfig:
    """Development configuration."""


config = dict(base=BaseConfig, development=DevelopmentConfig)
