from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import callback_data
from aiogram.dispatcher.filters import Text

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



@dp.callback_query_handler(text = "Моя анкета", state = base_state.start_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)
    del_msg = await call.message.answer(text_messages.anc_mes, reply_markup = keyboard.gen_back_keyboard())
    await state.update_data({"del_msg": del_msg})
    


@dp.callback_query_handler(text = "Заявка", state = base_state.start_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)
    del_msg = await call.message.answer(text_messages.req_mes, reply_markup = keyboard.gen_req_keyboard())
    await state.update_data({"del_msg": del_msg})
    
    # await bot.delete_message()

@dp.callback_query_handler(text = "Назад", state = base_state.start_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)
    del_msg = await call.message.answer(text = text_messages.control_mes, reply_markup = keyboard.gen_control_keyboard())
    await state.update_data({"del_msg": del_msg})



@dp.callback_query_handler(text = "Подать заявку", state = base_state.start_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)

    await state.set_state(base_state.get_form_state)

    del_msg = await call.message.answer(text_messages.format_mes, reply_markup = keyboard.gen_format_keyboard())
    await state.update_data({"del_msg": del_msg})

@dp.callback_query_handler(Text(equals= ["Онлайн", "Офлайн", "Офис"]), state = base_state.get_form_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)

    await state.set_state(base_state.get_time_state)

    del_msg = await call.message.answer(text_messages.tim_mes, reply_markup = keyboard.gen_times_keyboard())
    await state.update_data({"del_msg": del_msg})
    await state.update_data({"format": call.data})


@dp.callback_query_handler(Text(equals = ["15 мин", "20 мин", "30 мин"]), state = base_state.get_time_state)
async def callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await del_msg_from_list(state, bot, call.message)
    
    
    await state.set_state(base_state.start_state)
    

    del_msg = await call.message.answer(text_messages.end_format_mes, reply_markup = keyboard.gen_control_keyboard())
    await state.update_data({"del_msg": del_msg})
    await state.update_data({"time": call.data})
    print(await state.get_data())

