import os
from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapterSettings, BotFrameworkAdapter, TurnContext
from botbuilder.schema import Activity
from echo_bot import RuleBot

APP = Flask(__name__)

# Adapter settings (leave blank for local testing)
settings = BotFrameworkAdapterSettings(
    os.environ.get("MicrosoftAppId", ""), 
    os.environ.get("MicrosoftAppPassword", "")
)
adapter = BotFrameworkAdapter(settings)
bot = RuleBot()

@APP.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["Content-Type"]:
        body = request.json
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def aux_func(turn_context: TurnContext):
        await bot.on_turn(turn_context)

    task = adapter.process_activity(activity, auth_header, aux_func)
    task.result()
    return Response(status=201)

if __name__ == "__main__":
    APP.run(port=int(os.environ.get("PORT", 3978)))

