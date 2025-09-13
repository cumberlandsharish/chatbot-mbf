
from botbuilder.core import ActivityHandler, TurnContext
from bot_logic import chatbot_response

class RuleBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_text = turn_context.activity.text
        reply = chatbot_response(user_text)
        await turn_context.send_activity(reply)
