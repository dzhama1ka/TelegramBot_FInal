# ======================================= модуль ДЗ
# -----------------------------------------------------------------------
import datetime


def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Первое":
        dz1(bot, chat_id)

    elif ms_text == "Второе":
        dz2(bot, chat_id)

    elif ms_text == "Третье":
        dz3(bot, chat_id)

    elif ms_text == "Четвертое":
        dz4(bot, chat_id)

    elif ms_text == "Пятое":
        dz5(bot, chat_id)

    elif ms_text == "Шестое":
        dz6(bot, chat_id)

    elif ms_text == "Седьмое":
        dz7(bot, chat_id)

# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, text="Меня зовут Джамал")
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    bot.send_message(chat_id, text="Мне 20 лет")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    bot.send_message(chat_id, text="Джамал Джамал Джамал Джамал Джамал")
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    dz4_ResponseHandler = lambda message: bot.send_message(chat_id,
                                                           f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz4_ResponseHandler)
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "А лет то сколько Вам?", dz5_ResponseHandler)

def dz5_ResponseHandler(bot, chat_id, age):
    age == int(age)
    bot.send_message(chat_id, text=f"Ого, да Вам уже " +  str(int(age)) + "? По Вам не скажешь, я бы дал, от силы, лет 14!")
    if  int(age) > 60 and  int(age) < 100:
        bot.send_message(chat_id, text=f"Да Вы мне в дедули, а может даже и в бабули, годитесь!")

    if  int(age) > 18 and  int(age) < 59:
        bot.send_message(chat_id, text=f"Почти ровесник/ца!")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    qwerty = lambda message: bot.send_message(chat_id, "{}\n{}\n{}\n{}".format(message.text.upper(), message.text.lower(),
                                                                               message.text.capitalize(),
                                                                               message.text[0].lower() + message.text[1:].upper()))
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)
#---------------------------------------------------------------------------------------
def dz7(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько будет 4+8*2?", dz7_ResponseHandler)

def dz7_ResponseHandler(bot, chat_id, otv):
    otv == int(otv)
    if int(otv) == int("20"):
        bot.send_message(chat_id, text=f"Невероятно, мужик! Это и правда {int(otv)}")
    else:
        bot.send_message(chat_id, text=f"Сожалею, мужик, но это не {int(otv)}...")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = message.text
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
        # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
        # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

# ----------------------------------------------------------------------


dt = datetime.datetime.now()
f"http://numbersapi.com/{dt.year}/{dt.day}/date"

