import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from answs import accresp

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.WARNING)
TOKEN = "XXX"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Rudn bot, what i can help you with ?")


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = accresp(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    caps_handler = CommandHandler('caps', caps)

    application.add_handler(start_handler)
    application.add_handler(answer_handler)
    application.add_handler(caps_handler)
    application.run_polling()