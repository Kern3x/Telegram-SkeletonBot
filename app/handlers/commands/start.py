from telebot import TeleBot, types as tp

from app.utils import Keyboards
from app.models import User
from app.database import DataController


class TestCommandHandler:
    def __init__(self, bot: TeleBot) -> None:
        self.kb = Keyboards()
        self.db = DataController()

        @bot.message_handler(chat_types=["private"])
        def hello_message(message: tp.Message) -> None:
            user_id = message.from_user.id
            user = self.db.get_first(User, tg_id=user_id)

            if not user:
                self.db.add(User, tg_id=user_id, name=message.from_user.full_name)

            bot.reply_to(message, "Hello user!", reply_markup=self.kb.test.test_kb())
