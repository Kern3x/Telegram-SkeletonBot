from telebot import TeleBot

from config import config
from app.utils.db_manager import DBManager
from app.handlers import TestMessageHandler


dev_config = config.get("development")
base_config = config.get("base")


class TelegramBot:
    def __init__(self) -> None:
        DBManager().create_tables()

        self.bot = TeleBot(base_config.BOT_TOKEN)
        self.bot.parse_mode = "html"

        # Register message handlers
        TestMessageHandler(self.bot)

    def start(self):
        print("Telebot started...")
        self.bot.infinity_polling()
