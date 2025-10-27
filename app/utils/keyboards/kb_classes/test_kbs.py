from config import config
from telebot import types as tp


dev_config = config.get("development")


class TestKeyboard:
    def test_kb(self):
        test = tp.ReplyKeyboardMarkup(resize_keyboard=True)

        test.add(tp.KeyboardButton(text="Hello"))

        return test
