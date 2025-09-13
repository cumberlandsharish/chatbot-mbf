from flask import Flask, request, jsonify, render_template
from echo_bot import  EchoBot

app = Flask(__name__)
bot = EchoBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    user_message = request.json.get("text", "")
    reply = bot.on_message(user_message)
    return jsonify({"reply": reply})

# Serve the chat UI
@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3978)
