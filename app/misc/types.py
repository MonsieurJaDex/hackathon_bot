from aiogram.filters.callback_data import CallbackData

from app.misc import MainMenuMethods

# callback object for main menu
class MainMenuCallback(CallbackData, prefix="menu"):
    method: MainMenuMethods
