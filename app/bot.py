import logging

from telebot import TeleBot

from config import settings
import app.models as models
from app.utils.db_manager import init_db
from app.handlers.message.message_handler import TestMessageHandler
from app.handlers.commands.start import TestCommandHandler
from app.handlers.query.query_handler import TestQueryHandler
# example: from app.handlers.commands.some_handler import SomeHandler


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("bot")


class TelegramBot:
    def __init__(self) -> None:
        self.bot = TeleBot(settings.BOT_TOKEN, parse_mode="HTML")
        self._register_handlers()

    def _register_handlers(self) -> None:
        # Initialize each class handler that registers its decorators internally
        TestMessageHandler(self.bot)
        TestCommandHandler(self.bot)
        TestQueryHandler(self.bot)
        # SomeHandler(self.bot)
        # QueryHandler(self.bot)
        # ...

    def start(self) -> None:
        init_db()  # models already imported — tables will be created

        logger.info("TeleBot started…")

        self.bot.infinity_polling(
            skip_pending=True,
            timeout=20,
            long_polling_timeout=25,
        )
