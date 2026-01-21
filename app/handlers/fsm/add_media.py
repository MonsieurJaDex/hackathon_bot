from aiogram.fsm.state import StatesGroup, State


# fsm states group for adding media file
class AddMediaStatesGroup(StatesGroup):
    mediaFile = State()
    description = State()
