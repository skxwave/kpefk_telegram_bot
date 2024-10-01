from aiogram.fsm.state import State, StatesGroup


class SetGroupState(StatesGroup):
    group = State()
