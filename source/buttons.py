import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ( 
    filters, ApplicationBuilder,
    ContextTypes, CommandHandler,
    MessageHandler,Application,
    CallbackQueryHandler,CommandHandler,
    ContextTypes,ConversationHandler,)
from mproc import *


# cant return to main menu from menu
# need to replace numbers with question groups
# and subgroups to answers with end..


logger = logging.getLogger(__name__)
START_ROUTES, END_ROUTES = range(2)
ONE, TWO, THREE, FOUR, FIVE, MAIN_MENU, MENU, INFO, A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,NEW,NEW_1,NEW_2,NEW_3,OPER = range(31)


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    keyboard = [
        [
            InlineKeyboardButton("Вопросы", callback_data=str(MENU)),
            InlineKeyboardButton("Переход на оператора", callback_data=str(OPER)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите:", reply_markup=reply_markup)
    return START_ROUTES

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("книги", callback_data=str(ONE)),
            InlineKeyboardButton("библ", callback_data=str(TWO)),]
        ,[
            InlineKeyboardButton("уд", callback_data=str(THREE)),
            InlineKeyboardButton("эбс", callback_data=str(FOUR)),]
        ,[
            InlineKeyboardButton("прочее", callback_data=str(FIVE))
            #,InlineKeyboardButton("Back", callback_data=str(MAIN_MENU))
        ,]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберите категорию вопроса:", reply_markup=reply_markup
    )
    return START_ROUTES


def oper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = ('Оператор: @l3xs1s')
    return query.edit_message_text(text=answer)


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("сдать книгу",callback_data=str(A3)),],#3
            [InlineKeyboardButton("задолженность", callback_data=str(A4)),#4
        ],
        [
            InlineKeyboardButton("потерял книгу", callback_data=str(A6)),],#6
            [InlineKeyboardButton("продлить книгу", callback_data=str(A7)),#7
        ],
        [
            InlineKeyboardButton("не успел сдать книгу", callback_data=str(A16))],#16
            [InlineKeyboardButton("Back", callback_data=str(MENU))
        ]
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберете вопрос про книгу:", reply_markup=reply_markup
    )
    return START_ROUTES



async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("что такое нб", callback_data=str(A9)),],#9
            [InlineKeyboardButton("как работает библиотека", callback_data=str(A10)),#10
        ],
        [
            InlineKeyboardButton("библеотека главного корпуса", callback_data=str(A12)),],#12
            [InlineKeyboardButton("что такое унибц", callback_data=str(A8)),#8
        ],
            [InlineKeyboardButton("режим работы библиотеки", callback_data=str(NEW)),#new
        ],
        [
            InlineKeyboardButton("Back", callback_data=str(MENU))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберете вопрос про библиотеку:", reply_markup=reply_markup
    )
    return START_ROUTES

async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("удаленный доступ к", callback_data=str(A13)),],#13
            [InlineKeyboardButton("электронную версию", callback_data=str(A15)),#15
        ],
        [
            InlineKeyboardButton("удоступ в базы", callback_data=str(A2)),],#2
            [InlineKeyboardButton("Back", callback_data=str(MENU))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберете вопрос про уд:", reply_markup=reply_markup
    )
    return START_ROUTES

async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("что такое эбс", callback_data=str(A14)),],#14
            [InlineKeyboardButton("вход в эбс", callback_data=str(A1)),#1
        ],
        [
            InlineKeyboardButton("Back", callback_data=str(MENU))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберете вопрос про книгу про ЭБС:", reply_markup=reply_markup
    )
    
    return START_ROUTES

async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("подписать обходной лист", callback_data=str(A5)),],#5
            [InlineKeyboardButton("сдать диссертацию", callback_data=str(A11)),#11
        ],
        [
            InlineKeyboardButton("место для мусульман", callback_data=str(A17)),],#17
            [InlineKeyboardButton("зарегистрироваться в туис", callback_data=str(A18)),#18
        ],
        [
            InlineKeyboardButton("Back", callback_data=str(MENU))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Прочее:", reply_markup=reply_markup
    )
    return START_ROUTES

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Библиотека в главном корпусе ул. Миклухо-Маклая, 6", callback_data=str(NEW_1)),],#new_1
            [InlineKeyboardButton(f"Библиотека инженерной академии и факультета\n"
                                  f"физико-математических и естественных наук ул. Орджоникидзе, 3\n", callback_data=str(NEW_2)),#new_2
        ],
        [
            InlineKeyboardButton("Библиотека института русского языка, ул. Миклухо-Маклая, 10 к.2", callback_data=str(NEW_3)),],#new_3
            [InlineKeyboardButton("Back", callback_data=str(two))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберете вашу библеатеку:", reply_markup=reply_markup
    )
    return START_ROUTES

def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = (f'В данной версии бота доступны следующие команды:\n'
              f'/help - справка о командах\n'
              f'/q - задать вопрос\n/feedback - оставить свои мнения и предложения по улучшению бота\n'
              f'/menu - менюшка\n'
              f' @l3xs1s ')
    return query.edit_message_text(text=answer)




async def new_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = (f"Библиотека в главном корпусе ул. Миклухо-Маклая, 6: \n"
                        f'пн-чт – 11.00-17.45\n'
                        f'пт - 11.00-16.45\n'
                        f'сб - 13.00-16.45\n')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def new_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = (f"Библиотека инженерной академии и факультета \n"
                        "физико-математических и естественных наук ул. Орджоникидзе, 3: \n"
                        f'пн-чт – 11.00-17.45\n'
                        f'пт - 11.00-16.45\n')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def new_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = (f"Библиотека института русского языка, ул. Миклухо-Маклая, 10 к.2: \n"
                        f'пн–пт 12.30 – 17.30')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES



async def a1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('вход в эбс')
    keyboard = [

            InlineKeyboardButton("menu", callback_data=str(MENU)), ],#menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES


async def a2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('удоступ в базы')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES


async def a3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('куда сдавать учебник')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES


async def a4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('какие книги вернуть')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('подписать обходной лист')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('что такое унибц')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('потерял книгу')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('продлить книгу')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('когда работает библиотека')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('записаться в унибц')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('сдать диссертацию')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('можно взять в библеотеке главного корпуса')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a13(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('удаленный доступ к')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a14(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('что такое эбс')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a15(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('электронную версию')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a16(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('не успел сдать книгу')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a17(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('место для мусульман')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES

async def a18(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    answer = accresp('зарегистрироваться в туис')
    keyboard = [

        InlineKeyboardButton("menu", callback_data=str(MENU)), ],  # menu

    # return query.edit_message_text(text=answer)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=answer, reply_markup=reply_markup
    )
    return START_ROUTES
