from aiogram.fsm.state import StatesGroup, State


# fsm states group for find media by id
class FindMediaByIdStatesGroup(StatesGroup):
    mediaId = State()
