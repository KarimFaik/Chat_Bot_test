import logging  # Importing the library for logging
from telegram import Update  # Importing the Update class from the telegram library
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler  # Importing several classes from the telegram.ext library
#from answs import accresp
from mproc import *  # Importing all functions from the mproc module

# Configuring the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.WARNING)  # Setting the logging level for the httpx library
TOKEN = "your_token_here"  # Bot token for accessing the Telegram API

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! I'm the chatbot of the RUDN library. To see all available commands, type /help .")

# Function to handle the /help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"In this version of the bot, the following commands are available:\n/help - get command help\n/q - ask a question\n/feedback - leave feedback about the bot")

# Function to handle the /q command (ask a question)
async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_arg = " ".join(context.args)
    answer = accresp(user_arg)  # Calling the accresp function to get an answer to the user's question
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)  # Sending the answer to the user

# Function to handle the /feedback command (leave feedback)
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)  # Getting the feedback text from the command arguments
    userid = update.message.from_user.id  # Getting the user ID
    addfeedback(text, userid)  # Calling the addfeedback function to save the feedback
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Thank you for your feedback!')  # Sending a confirmation to the user

# Main program logic
if __name__ == '__main__':
    # Creating an application instance with the bot token
    application = ApplicationBuilder().token(TOKEN).build()

    # Creating command handlers
    start_handler = CommandHandler('start', start)
    question_handler = CommandHandler('q', question)
    feedback_handler = CommandHandler('feedback', feedback)
    help_handler = CommandHandler('help', help)
    
    # Adding command handlers to the application
    application.add_handler(start_handler)
    application.add_handler(question_handler)
    application.add_handler(feedback_handler)
    application.add_handler(help_handler)
    
    # Running the application in polling mode, waiting for incoming messages from users
    application.run_polling()
