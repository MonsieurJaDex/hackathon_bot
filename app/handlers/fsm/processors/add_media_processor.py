import logging

from aiogram import Router, types
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Video, PhotoSize

from app.database.schemas import MediaDTO
from app.database.service import MediaService
from app.handlers.fsm import AddMediaStatesGroup
from app.misc import ValidContentType

router = Router()


# media file processing
@router.message(AddMediaStatesGroup.mediaFile)
async def process_media_file(message: types.Message, state: FSMContext) -> None:
    # message content type checking
    if message.content_type not in [
        ContentType.VIDEO,
        ContentType.PHOTO,
    ]:
        await message.answer("Медиафайлы могут быть только фото или видео 😅")
        logging.getLogger().warning(f"Got invalid content type: {message.content_type}")
        return

    # store file data and ask next
    await state.update_data(
        mediaFile=message.video if message.video else message.photo[-1]
    )

    await message.answer(
        "Получил ваше медиа 😉\nТеперь пришлите описание, которое будет закреплено за этим медиафайлом"
    )
    await state.set_state(AddMediaStatesGroup.description)


# description processing
@router.message(AddMediaStatesGroup.description)
async def process_media_description(message: types.Message, state: FSMContext) -> None:
    # message content type checking
    if message.content_type != ContentType.TEXT:
        await message.answer("Описание должно быть только текстовым!")
        return

    # store description and send data to database layer (service)
    data = await state.update_data(description=message.text)

    await state.clear()

    mediaFile: Video | PhotoSize = data["mediaFile"]
    description: str = data["description"]

    # prepare DTO
    dto = MediaDTO.model_validate(
        {
            "file_id": mediaFile.file_id,
            "file_unique_id": mediaFile.file_unique_id,
            "file_type": (
                ValidContentType.VIDEO
                if (isinstance(mediaFile, Video))
                else ValidContentType.PHOTO
            ),
            "description": description,
        }
    )

    # processing insertion
    media_id = await MediaService().insert_media(dto)

    # reply to user
    await message.answer(
        f"{message.from_user.first_name}, ваше медиа было успешно сохранено 😊\nЕго уникальный ID: {media_id}"
    )
