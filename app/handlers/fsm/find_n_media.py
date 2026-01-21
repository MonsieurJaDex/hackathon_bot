from aiogram.fsm.state import StatesGroup, State


# fsm states group for find latest N media
class FindNMediaByIdStatesGroup(StatesGroup):
    days = State()
