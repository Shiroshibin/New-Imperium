from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import Bot
from loader import dp
from loader import bot

from custom_state.user_state import base_state
from custom_state.anceta_state import anc_state
from aiogram.dispatcher.filters import Text

import text_messages
import keyboard
from web_app.db import funcs as db_fun



async def del_msg_from_list(state: State, bot: Bot, message: types.Message):
    try:
        data = await state.get_data()
        data = data["del_msg"]["message_id"]
        await bot.delete_message(message.chat.id, data) 
    except:
        pass



@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    if db_fun.get_user_by_tg_id(message.from_user.id) == None:
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
    await state.update_data({"phone": message.contact.phone_number})
    await state.set_state(anc_state.f_name_state)
    await message.answer(text_messages.ancet_mes_1)
    

@dp.message_handler(state = anc_state.f_name_state)
async def handler(message: types.Message, state: FSMContext):
    await state.update_data({"first_name": message.text})
    await state.set_state(anc_state.l_name_state)
    await message.answer(text_messages.ancet_mes_2)

@dp.message_handler(state = anc_state.l_name_state)
async def handler(message: types.Message, state: FSMContext):
    await state.update_data({"last_name": message.text})
    await state.set_state(anc_state.job_title_state)
    await message.answer(text_messages.ancet_mes_3)

@dp.message_handler(state = anc_state.job_title_state)
async def handler(message: types.Message, state: FSMContext):
    await state.update_data({"job_title": message.text})
    await state.set_state(anc_state.birth_day_state)
    await message.answer(text_messages.ancet_mes_4)

@dp.message_handler(state = anc_state.birth_day_state)
async def handler(message: types.Message, state: FSMContext):
    await state.update_data({"birth_day": message.text})
    data = await state.get_data()
    db_fun.create_user(data["phone"], message.from_user.id)
    user_id = db_fun.get_user_by_tg_id(message.from_user.id).id
    db_fun.create_profile(user_id, data["last_name"], data["first_name"], data["job_title"], data["birth_day"])

    await state.set_state(base_state.start_state)

    await message.answer(text_messages.end_ancet_mes, reply_markup=keyboard.gen_control_keyboard())