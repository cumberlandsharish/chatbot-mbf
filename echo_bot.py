# echo_bot.py
from bot_logic_azure_support import BotLogic

class EchoBot:
    def __init__(self):
        self.logic = BotLogic()

    def on_message(self, message: str) -> str:
        """Process a user message and return bot reply"""
        return self.logic.get_reply(message)
