from aiogram import Router, types
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext

from typing import List

from app.database.models import MediaContent
from app.database.service import MediaService
from app.handlers.fsm.find_n_media import FindNMediaByIdStatesGroup

router = Router()


@router.message(FindNMediaByIdStatesGroup.days)
async def process_find_n_media(message: types.Message, state: FSMContext) -> None:
    if message.content_type != ContentType.TEXT:
        await message.answer("Пожалуйста, введите корректное количество дней.")
        return

    days = message.text.strip()

    if not days.isdigit() or int(days) < 1:
        await message.answer("Пожалуйста, введите корректное количество дней.")
        return

    await state.clear()

    media_list: List[MediaContent] = await MediaService().get_latest_n_media(
        n=int(days)
    )

    if len(media_list) == 0:
        await message.answer("[❌] Медиафайлы с такими фильтрами не найдены 🥺")
        return

    await message.answer(
        f"[✅] Найденные видео за последние {days} дней\n\n"
        + "\n".join([str(media) for media in media_list])
    )
