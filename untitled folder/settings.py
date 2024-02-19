import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = "6653576011:AAGah5wzOymqQKylQ1yKo4Edbgufmn3tEk4"

TELEGRAM_SUPPORT_CHAT_ID = "HERE CHAT ID"
TELEGRAM_SUPPORT_CHAT_ID = int(1636611620)

WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "Hi 👋")
FEEDBACK_MESSAGE = os.getenv("FEEDBACK_MESSAGE", "Expect an answer👋")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")
