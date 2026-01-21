import logging
from typing import List

from aiogram import F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InaccessibleMessage
from aiogram import Router

from app.database.models import MediaContent
from app.database.schemas import MediaDTO
from app.database.service import MediaService
from app.handlers.fsm.find_media_by_id import FindMediaByIdStatesGroup
from app.handlers.fsm.find_n_media import FindNMediaByIdStatesGroup
from app.misc import MainMenuMethods
from app.misc import MainMenuCallback

from app.handlers.fsm import AddMediaStatesGroup

router = Router()


@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.AddMedia))
async def add_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    await message.answer(
        "Окей, давайте загрузим ваш медиафайл!\nПришлите, пожалуйста, ваш файл (только фото или видео) 🎥"
    )
    await state.set_state(AddMediaStatesGroup.mediaFile)


@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMedia))
async def find_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    await message.answer("Отправьте ID медиафайла, который хотите найти:")

    await state.set_state(FindMediaByIdStatesGroup.mediaId)


@router.callback_query(
    MainMenuCallback.filter(F.method == MainMenuMethods.FindAllMedia)
)
async def find_all_media_handler(query: CallbackQuery) -> None:
    await query.answer()

    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    media_list: List[MediaContent] = await MediaService().get_all_media()

    if len(media_list) == 0:
        await message.answer("Нет медиафайлов в базе данных 😥")
        return

    await message.answer("\n".join([str(media) for media in media_list]))


@router.callback_query(
    MainMenuCallback.filter(F.method == MainMenuMethods.FindLatestNMedia)
)
async def find_latest_n_media(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    message: Message = query.message

    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    await state.set_state(FindNMediaByIdStatesGroup.days)
    await message.answer("Введите количество дней для поиска:")
