from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import Bot
from loader import dp
from loader import bot

from custom_state.user_state import base_state

import text_messages
import keyboard



async def del_msg_from_list(state: State, bot: Bot, message: types.Message):
    try:
        data = await state.get_data()
        data = data["del_msg"]["message_id"]
        await bot.delete_message(message.chat.id, data) 
    except:
        pass



@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    if False:
        await del_msg_from_list(state, bot, message)
        del_msg = await message.answer(text = text_messages.hello_mes, reply_markup = keyboard.get_phone_keyboard())
        await state.finish()
        await state.set_state(base_state.start_state)
        await state.set_data({"del_msg": del_msg})
    else:
        await del_msg_from_list(state, bot, message)
        del_msg = await message.answer(text = text_messages.control_mes, reply_markup = keyboard.gen_control_keyboard())
        await state.finish()
        await state.set_state(base_state.start_state)
        await state.set_data({"del_msg": del_msg})

@dp.message_handler(content_types = types.ContentType.CONTACT, state=base_state.start_state)
async def handler(message: types.Message, state: FSMContext):
    await message.answer(text_messages.ancet_mes)


