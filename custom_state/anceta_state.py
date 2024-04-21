from aiogram.dispatcher.filters.state import State, StatesGroup

class anc_state(StatesGroup):
    f_name_state = State()
    l_name_state = State()
    job_title_state = State()
    birth_day_state = State()