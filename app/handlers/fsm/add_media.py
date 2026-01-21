from aiogram.fsm.state import StatesGroup, State


class AddMediaStatesGroup(StatesGroup):
    mediaFile = State()
    description = State()
