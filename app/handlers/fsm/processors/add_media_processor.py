from multiprocessing.reduction import steal_handle
from typing import Union

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

    # use only 1 photo, because telegram by default stores photos as list[PhotoSize]
    if message.content_type == ContentType.PHOTO and len(message.photo) > 1:
        await message.answer(
            "Пока функционала альбомов не предусмотрено, поэтому будет сохранено только первое фото"
        )

    await state.update_data(
        mediaFile=message.video if message.video else message.photo[0]
    )

    await message.answer(
        "Получил ваше медиа 😉\nТеперь пришлите описание, которое будет закреплено за этим медиафайлом"
    )
    await state.set_state(AddMediaStatesGroup.description)


@router.message(AddMediaStatesGroup.description)
async def process_media(message: types.Message, state: FSMContext):
    if isinstance(message, InaccessibleMessage):
        return

    if message.content_type != ContentType.TEXT:
        await message.answer("Описание должно быть только текстовым!")
        return

    await state.update_data(description=message.text)

    await message.answer("Укажите теги для вашего файла через запятую 😊\nПример: ")

    await state.set_state(AddMediaStatesGroup.tags)


@router.message(AddMediaStatesGroup.tags)
async def process_media(message: types.Message, state: FSMContext):
    if isinstance(message, InaccessibleMessage):
        return

    if message.content_type != ContentType.TEXT:
        await message.answer("Теги должны быть только в текстовом формате!")
        return

    data = await state.update_data(description=message.text.strip().replace(" ", ""))

    await state.clear()

    await message.answer(
        f"{message.from_user.first_name}, ваше медиа было успешно сохранено 😊\nЕго уникальный ID: {data['mediaFile'].file_id}"
    )
