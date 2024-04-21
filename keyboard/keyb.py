from aiogram import types

def get_start_keyboard():
    keyb = types.InlineKeyboardMarkup(row_width = 1)
    button_workpiece = ["Отправить номер"]
    buttons = [types.InlineKeyboardButton(text = item, callback_data = item) for item in button_workpiece]
    keyb.add(*buttons)
    return keyb

def get_phone_keyboard():
    keyb = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
    button = types.KeyboardButton(text="Отправить", request_contact=True)
    keyb.add(button)
    return keyb

def get_ank_keyboard():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text="Прошлый вопрос", callback_data="Прошлый вопрос")
    keyb.add(button)
    return keyb

def gen_control_keyboard():
    keyb = types.InlineKeyboardMarkup()
    buttons_workpieces = ["Моя анкета", "Заявка"]
    buttons = [types.InlineKeyboardButton(text = i, callback_data = i) for i in buttons_workpieces]
    keyb.add(*buttons)
    return keyb

def gen_req_keyboard(data):
    keyb = types.InlineKeyboardMarkup(row_width=1)

    if data == "Не весит":
        buttons_workpieces = ["Подать заявку", "Назад"]
    else:
        buttons_workpieces = ["Снять заявку", "Назад"]

    buttons = [types.InlineKeyboardButton(text = i, callback_data = i) for i in buttons_workpieces]
    keyb.add(*buttons)
    return keyb

def gen_back_keyboard():
    keyb = types.InlineKeyboardMarkup()
    buttons = types.InlineKeyboardButton(text = "Назад", callback_data = "Назад")
    keyb.add(buttons)
    return keyb

def gen_format_keyboard():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    buttons_workpieces = ["Онлайн", "Офлайн", "Офис"]
    buttons = [types.InlineKeyboardButton(text = i, callback_data = i) for i in buttons_workpieces]
    keyb.add(*buttons)
    return keyb

def gen_times_keyboard():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    buttons_workpieces = ["15 мин", "20 мин", "30 мин"]
    buttons = [types.InlineKeyboardButton(text = i, callback_data = i) for i in buttons_workpieces]
    keyb.add(*buttons)
    return keyb

def gen_prof_keyboard():
    keyb = types.InlineKeyboardMarkup(row_width=1)
    buttons_workpieces = ["Готов(а)", "Отменить"]
    buttons = [types.InlineKeyboardButton(text = i, callback_data = i) for i in buttons_workpieces]
    keyb.add(*buttons)
    return keyb