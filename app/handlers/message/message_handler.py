from telebot import TeleBot, types as tp

from app.utils import Keyboards


class TestMessageHandler:
    def __init__(self, bot: TeleBot) -> None:
        self.kb = Keyboards()

        @bot.message_handler(chat_types=["private"])
        def hello_message(message: tp.Message) -> None:
            bot.reply_to(message, "Hello user!", reply_markup=self.kb.test.test_kb())
