import logging
from typing import List

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InaccessibleMessage
from aiogram import Router

from app.database.models import MediaContent
from app.database.service import MediaService
from app.handlers.fsm.find_media_by_id import FindMediaByIdStatesGroup
from app.handlers.fsm import AddMediaStatesGroup
from app.handlers.fsm.find_n_media import FindNMediaByIdStatesGroup
from app.misc import MainMenuMethods
from app.misc import MainMenuCallback

router = Router()


# callback for media adding button
@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.AddMedia))
async def add_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    # message accessible check
    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    await message.answer(
        "Окей, давайте загрузим ваш медиафайл!\nПришлите, пожалуйста, ваш файл (только фото или видео) 🎥"
    )

    # fall to fsm
    await state.set_state(AddMediaStatesGroup.mediaFile)


# callback for media finding button
@router.callback_query(MainMenuCallback.filter(F.method == MainMenuMethods.FindMedia))
async def find_media_handler(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    # message accessible check
    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    await message.answer("Отправьте ID медиафайла, который хотите найти:")

    # fall to fsm
    await state.set_state(FindMediaByIdStatesGroup.mediaId)


# callback for media find all button
@router.callback_query(
    MainMenuCallback.filter(F.method == MainMenuMethods.FindAllMedia)
)
async def find_all_media_handler(query: CallbackQuery) -> None:
    await query.answer()

    # message accessible check
    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    # request media list from database layer
    media_list: List[MediaContent] = await MediaService().get_all_media()

    # in case of empty database
    if len(media_list) == 0:
        await message.answer("Нет медиафайлов в базе данных 😥")
        return

    # print all media files
    await message.answer("\n".join([str(media) for media in media_list]))


# callback for finding N media files
@router.callback_query(
    MainMenuCallback.filter(F.method == MainMenuMethods.FindLatestNMedia)
)
async def find_latest_n_media(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()

    # message accessible check
    message: Message = query.message
    if isinstance(message, InaccessibleMessage):
        logging.getLogger().warning(
            f"Got InaccessibleMessage from {message.from_user.username}: {message}"
        )
        return

    # fall to fsm
    await state.set_state(FindNMediaByIdStatesGroup.days)
    await message.answer("Введите количество дней для поиска:")
