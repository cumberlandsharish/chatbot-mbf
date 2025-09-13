import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswer import QuestionAnsweringClient

# Azure setup
AZURE_ENDPOINT = "https://t6langauageservice.cognitiveservices.azure.com/"
AZURE_KEY = "xxxx"

azure_client = QuestionAnsweringClient(endpoint=AZURE_ENDPOINT, credential=AzureKeyCredential(AZURE_KEY))

class BotLogic:
    def __init__(self):
        self.responses = {
            r"hi|hello|hey": "Hello! How can I help you today?",
            r"how are you": "I'm just a bot, but I'm doing well. Thanks for asking!",
            r"your name": "I'm a simple chatbot created for MSAI-631.",
            r"(.*) help (.*)": "Sure, I can try to help you with that.",
            r"bye|exit|quit": "Goodbye! Have a great day!"
        }

    def get_reply(self, message: str) -> str:
        text = (message or "").lower()
        # Check local regex rules first
        for pattern, response in self.responses.items():
            if re.search(pattern, text):
                return response

        # If no local match, call Azure Language Service
        try:
            qna_result = azure_client.answer_question(
                project_name="YourProjectName",  # QnA Maker project if used
                deployment_name="production",    # Deployment name
                question=message
            )
            if qna_result.answers and len(qna_result.answers) > 0:
                return qna_result.answers[0].answer
        except Exception as e:
            print(f"Azure request failed: {e}")

        # Fallback if nothing matches
        return "I'm not sure how to respond. Could you rephrase?"
