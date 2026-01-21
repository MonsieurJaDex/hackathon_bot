from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.enums import ContentType

from app.misc import MainMenuMethods

# patterns


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


# callback types


# callback object for main menu
class MainMenuCallback(CallbackData, prefix="menu"):
    method: MainMenuMethods


# custom types


class ValidContentType(Enum):
    PHOTO = ContentType.PHOTO
    VIDEO = ContentType.VIDEO
