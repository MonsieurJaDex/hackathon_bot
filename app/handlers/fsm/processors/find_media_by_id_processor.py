from aiogram import Router, types
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext

from app.database.service import MediaService
from app.database.models import MediaContent
from app.handlers.fsm.find_media_by_id import FindMediaByIdStatesGroup
from app.misc import ValidContentType

router = Router()


@router.message(FindMediaByIdStatesGroup.mediaId)
async def find_media_by_id(message: types.Message, state: FSMContext) -> None:
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите корректный ID.")
        return

    media_id = message.text.strip()
    if not media_id.isdigit():
        await message.answer("Пожалуйста, введите корректный ID.")
        return

    media_id = int(media_id)
    media: MediaContent = await MediaService().get_media_by_id(media_id)
    if not media:
        await message.answer(f"Медиафайла с ID {media_id} не найдено 😥")
        await state.clear()
        return

    file = media.file_id
    caption = f"ID: {media.id}\nОписание: {media.description or ''}"

    if media.file_type == ValidContentType.PHOTO:
        await message.answer_photo(photo=file, caption=caption)
    else:
        await message.answer_video(video=file, caption=caption)
