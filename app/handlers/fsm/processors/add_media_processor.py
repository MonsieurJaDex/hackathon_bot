from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType
from aiogram.types import InaccessibleMessage

from app.handlers.fsm import AddMediaStatesGroup

router = Router()


@router.message(AddMediaStatesGroup.mediaFile)
async def process_media(message: types.Message, state: FSMContext):
    if isinstance(message, InaccessibleMessage):
        return

    if message.content_type not in [ContentType.VIDEO, ContentType.PHOTO]:
        await message.answer("Медиафайлы могут быть только фото или видео 😅")
        return

    await message.answer(
        "Получил ваше медиа 😉\nТеперь пришлите описание, которое будет закреплено за этим медиафайлом"
    )
    # ! to complete...
