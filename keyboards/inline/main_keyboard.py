from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# inline keyboard for main control panel definition
main_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="[🎥] Добавить медиафайл (фото/видео)", callback_data="1"
            )
        ],
        [
            InlineKeyboardButton(
                text="[🔎] Найти существующий медиафайл", callback_data="2"
            )
        ],
        [InlineKeyboardButton(text="[📒] Найти мои медиафайлы", callback_data="3")],
    ]
)
