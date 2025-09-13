
import os

class Config:
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    PORT = int(os.environ.get("PORT", 3978))
