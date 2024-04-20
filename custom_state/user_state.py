from aiogram.dispatcher.filters.state import State, StatesGroup

class base_state(StatesGroup):
    start_state = State()
    get_form_state = State()
    get_time_state = State()