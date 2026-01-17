from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.misc import MainMenuMethods
from app.misc import MainMenuCallback

# inline keyboard for main control panel definition
main_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="[🎥] Добавить медиафайл (фото/видео)",
                callback_data=MainMenuCallback(method=MainMenuMethods.AddMedia).pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text="[🔎] Найти существующий медиафайл",
                callback_data=MainMenuCallback(method=MainMenuMethods.FindMedia).pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text="[📒] Найти все доступные медиафайлы",
                callback_data=MainMenuCallback(
                    method=MainMenuMethods.FindAllMedia
                ).pack(),
            )
        ],
    ]
)
