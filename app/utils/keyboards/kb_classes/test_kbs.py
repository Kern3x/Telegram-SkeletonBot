from telebot import types as tp


class TestKeyboard:
    def test_kb(self) -> tp.ReplyKeyboardMarkup:
        test = tp.ReplyKeyboardMarkup(resize_keyboard=True)

        test.add(tp.KeyboardButton(text="Hello"))

        return test

    def make_inline_test_kb(self) -> tp.InlineKeyboardMarkup:
        kb = tp.InlineKeyboardMarkup(row_width=3)

        kb.add(tp.InlineKeyboardButton("Open website", url="https://example.com"))

        return kb
