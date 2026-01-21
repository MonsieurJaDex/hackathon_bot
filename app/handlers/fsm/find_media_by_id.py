from aiogram.fsm.state import StatesGroup, State


class FindMediaByIdStatesGroup(StatesGroup):
    mediaId = State()
