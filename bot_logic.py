
import re

responses = {
    r"hi|hello|hey": "Hello! How can I help you today?",
    r"how are you": "I'm just a bot, but I'm doing well. Thanks for asking!",
    r"your name": "I'm a simple chatbot created for MSAI-631.",
    r"(.*) help (.*)": "Sure, I can try to help you with that.",
    r"bye|exit|quit": "Goodbye! Have a great day!"
}

def chatbot_response(user_input: str) -> str:
    text = (user_input or "").lower()
    for pattern, response in responses.items():
        if re.search(pattern, text):
            return response
    return "I'm not sure I understand. Could you rephrase?"
