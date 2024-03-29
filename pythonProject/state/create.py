from aiogram.fsm.state import StatesGroup, State


class CreateState(StatesGroup):
    jalousie = State()
    jalousie_type = State()
    jalousie_number = State()
    jalousie_control = State()
    jalousie_fix = State()
    jalousie_hor_size = State()
    jalousie_vert_size = State()
    jalousie_order = State()
    windowsill = State()
    windowsill_colour = State()
    windowsill_plug = State()
    windowsill_number = State()
    windowsill_size = State()
    windowsill_order = State()
    glazing = State()
    glazing_type = State()
    glazing_number = State()
    hor_size_glazing = State()
    vert_size_glazing = State()
    glazing_order = State()
    reflux = State()
    reflux_type = State()
    reflux_number = State()
    reflux_size = State()
    reflux_order = State()
    mosquito = State()
    mosquito_type = State()
    mosquito_number = State()
    hor_size_mosquito = State()
    vert_size_mosquito = State()
    mosquito_order = State()
    text_msg = State()
    user_text_msg = State()
    text_msg_one = State()
    select_user = State()
    select_table = State()
    order_info = State()
    order_table = State()
