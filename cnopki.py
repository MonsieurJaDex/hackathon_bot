from idlelib import query

from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
    Message,
    InaccessibleMessage,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from app.misc import MainMenuMethods
from app.misc import MainMenuCallback
from app.handlers.fsm import AddMediaStatesGroup

router = Router()


# CallbackData to search for buttons
class FindMediaCallback(CallbackData, prefix="find_media"):
    action: str


# Keybord 
def find_media_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📄 Список идентификаторов",
                    callback_data=FindMediaCallback(action="list_ids").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="🆔 Контент по ID",
                    callback_data=FindMediaCallback(action="by_id").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔎 Фильтрация по параметрам",
                    callback_data=FindMediaCallback(action="filter").pack(),
                )
            ],
        ]
    )


# Add Media
@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.AddMedia))
async def add_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        return

    await message.answer(
        "Окей, давайте загрузим ваш медиафайл!\n""Пришлите, пожалуйста, ваш файл (только фото или видео) 🎥"
    )
    await state.set_state(AddMediaStatesGroup.mediaFile)


# Find Media (Shows buttons on top)
@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMedia))
async def find_media_handler(query: CallbackQuery):
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        return

    await message.answer(
        text="🔍 Выберите способ поиска медиа:",
        reply_markup=find_media_keyboard(),
    )


# Search buttons  
@router.callback_query(FindMediaCallback.filter(F.action == "list_ids"))
async def find_media_list_ids(query: CallbackQuery):
    await query.answer()
    await query.message.answer("📄 Здесь будет список идентификаторов")


@router.callback_query(FindMediaCallback.filter(F.action == "by_id"))
async def find_media_by_id(query: CallbackQuery):
    await query.answer()
    await query.message.answer("🆔 Введите ID контента")


@router.callback_query(FindMediaCallback.filter(F.action == "filter"))
async def find_media_filter(query: CallbackQuery):
    await query.answer()
    await query.message.answer("🔎 Выберите параметры фильтрации")


# Find My Media
@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMyMedia))
async def find_my_media_handler(query: CallbackQuery):
    await query.answer(text="Find MyMedia")