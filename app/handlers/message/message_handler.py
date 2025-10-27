from config import config
from app.utils import Keyboards


class TestMessageHandler:
    def __init__(self, bot) -> None:
        self.kb = Keyboards()

        @bot.message_handler(chat_types=["private"])
        def hello_message(message):
            bot.reply_to(message, "Hello user!", reply_markup=self.kb.test_kb())
 