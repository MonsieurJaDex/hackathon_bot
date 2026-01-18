from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.enums import ContentType

from app.misc import MainMenuMethods

# callback types

# callback object for main menu
class MainMenuCallback(CallbackData, prefix="menu"):
    method: MainMenuMethods


# custom types

class ValidContentType(Enum):
    PHOTO = ContentType.PHOTO
    VIDEO = ContentType.VIDEO
