# bot_logic.py
class BotLogic:
    def get_reply(self, message: str) -> str:
        msg = message.lower()

        if "hi" in msg or "hello" in msg:
            return "Hello! How can I help you today?"
        elif "help" in msg:
            return "Sure! You can ask me about greetings, my name, or say bye."
        elif "name" in msg:
            return "I’m a simple rule-based chatbot 🤖"
        elif "bye" in msg or "goodbye" in msg:
            return "Goodbye! Have a great day!"
        else:
            return "I’m not sure how to respond to that yet."
