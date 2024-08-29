import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    filters, ApplicationBuilder,
    ContextTypes, CommandHandler,
    MessageHandler,Application,
    CallbackQueryHandler,CommandHandler,
    ContextTypes,ConversationHandler,)
from mproc import *
from buttons import *

import jamspell


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('ru_small.bin')



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.WARNING)
TOKEN = "*****"
# TOKEN = "*****" ~karim
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    # last_name = update.message.chat.last_name
    # username = update.message.chat.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text= f"Привет, {first_name}! Я чат-бот Научной библиотеки РУДН. Чем могу быть полезен? /menu .")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=(f"В данной версии бота доступны следующие команды:\n"
                                                                          f"/help - справка о командах\n"
                                                                          f"/q - задать вопрос\n/feedback - оставить свои мнения и предложения по улучшению бота\n"
                                                                          f"/menu - менюшка"))
 

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_arg = " ".join(context.args)
    user_arg = corrector.FixFragment(user_arg)
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
    #menu |
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("menu", main_menu)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(five, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(menu, pattern="^" + str(MENU) + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + str(MAIN_MENU) + "$"),
                CallbackQueryHandler(info, pattern="^" + str(INFO) + "$"),
                CallbackQueryHandler(a1, pattern="^" + str(A1) + "$"),
                CallbackQueryHandler(a2, pattern="^" + str(A2) + "$"),
                CallbackQueryHandler(a3, pattern="^" + str(A3) + "$"),
                CallbackQueryHandler(a4, pattern="^" + str(A4) + "$"),
                CallbackQueryHandler(a5, pattern="^" + str(A5) + "$"),
                CallbackQueryHandler(a6, pattern="^" + str(A6) + "$"),
                CallbackQueryHandler(a7, pattern="^" + str(A7) + "$"),
                CallbackQueryHandler(a8, pattern="^" + str(A8) + "$"),
                CallbackQueryHandler(a9, pattern="^" + str(A9) + "$"),
                CallbackQueryHandler(a10, pattern="^" + str(A10) + "$"),
                CallbackQueryHandler(a11, pattern="^" + str(A11) + "$"),
                CallbackQueryHandler(a12, pattern="^" + str(A12) + "$"),
                CallbackQueryHandler(a13, pattern="^" + str(A13) + "$"),
                CallbackQueryHandler(a14, pattern="^" + str(A14) + "$"),
                CallbackQueryHandler(a15, pattern="^" + str(A15) + "$"),
                CallbackQueryHandler(a16, pattern="^" + str(A16) + "$"),
                CallbackQueryHandler(a17, pattern="^" + str(A17) + "$"),
                CallbackQueryHandler(a18, pattern="^" + str(A18) + "$"),
                CallbackQueryHandler(new_1, pattern="^" + str(NEW_1) + "$"),
                CallbackQueryHandler(new_2, pattern="^" + str(NEW_2) + "$"),
                CallbackQueryHandler(new_3, pattern="^" + str(NEW_3) + "$"),
                CallbackQueryHandler(new, pattern="^" + str(NEW) + "$"),
                CallbackQueryHandler(oper, pattern="^" + str(OPER) + "$")
                
            ],
            # END_ROUTES: [
            #     CallbackQueryHandler(main_menu, pattern="^" + str(ONE) + "$"),
            # ],
        },
        fallbacks=[CommandHandler("menu", main_menu)],
    )
    

    application.add_handler(start_handler)
    application.add_handler(question_handler)
    application.add_handler(feedback_handler)
    application.add_handler(help_handler)
    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
