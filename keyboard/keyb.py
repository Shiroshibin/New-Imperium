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
    keyb = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Анкета", web_app="https://4161-2a03-d000-1403-f159-2d9a-dbc5-34ad-5ae3.ngrok-free.app")