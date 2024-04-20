from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp
from loader import bot


from state.user_state import normal_state
import text_messages
import keyboard

    

@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer(text = text_messages.hello_mes, reply_markup = keyboard.get_phone_keyboard())
    await state.finish()
    await state.set_state(normal_state.start_state)

@dp.message_handler(content_types = types.ContentType.CONTACT, state=normal_state.start_state)
async def handler(message: types.Message, state: FSMContext):
    await message.answer(text_messages.ancet_mes)