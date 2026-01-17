from idlelib import query

from aiogram import F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InaccessibleMessage
from aiogram import Router

from app.misc import MainMenuMethods
from app.misc import MainMenuCallback

from app.handlers.fsm import AddMediaStatesGroup

router = Router()


@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.AddMedia))
async def add_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        # ! add logs later
        return

    await message.answer(
        "Окей, давайте загрузим ваш медиафайл!\nПришлите, пожалуйста, ваш файл (только фото или видео) 🎥"
    )
    await state.set_state(AddMediaStatesGroup.mediaFile)


@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMedia))
async def find_media_handler(query: CallbackQuery, callback_data: CallbackData):
    await query.answer(
        text="Find Media",
    )


@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMyMedia))
async def find_my_media_handler(query: CallbackQuery, callback_data: CallbackData):
    await query.answer(
        text="Find MyMedia",
    )
