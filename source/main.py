import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
#from answs import accresp
from mproc import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.WARNING)
TOKEN = "5495273860:AAFLZNnqgygWJCLrI-_b9G7-ETmJsvBw_Fw"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    # last_name = update.message.chat.last_name
    # username = update.message.chat.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text= f"Привет, {first_name}! Я чат-бот Научной библиотеки РУДН. Чем могу быть полезен? /help .")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"В данной версии бота доступны следующие команды:\n/help - справка о командах\n/q - задать вопрос\n/feedback - оставить свои мнения и предложения по улучшению бота")

#async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    answer = accresp(update.message.text)
#    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_arg = " ".join(context.args)
    answer = accresp(user_arg)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    userid = update.message.from_user.id
    addfeedback(text, userid)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Спасибо за ваше мнение!')


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    question_handler = CommandHandler('q', question)
    #answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    feedback_handler = CommandHandler('feedback', feedback)
    help_handler = CommandHandler('help', help)
    
    application.add_handler(start_handler)
    application.add_handler(question_handler)
    application.add_handler(feedback_handler)
    application.add_handler(help_handler)

    application.run_polling()