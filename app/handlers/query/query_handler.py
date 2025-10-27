from telebot import TeleBot, types as tp


class TestQueryHandler:
    def __init__(self, bot: TeleBot) -> None:
        self.bot = bot

        @self.bot.callback_query_handler(func=lambda call: call.data == "test")
        def test_query(call: tp.CallbackQuery) -> None:
            self.bot.answer_callback_query(
                call.id, "Test query received!", show_alert=True
            )
