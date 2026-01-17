from aiogram import types, Router
from aiogram.filters import CommandStart

from app.keyboards import inline_main_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        f"Приветствую, {message.from_user.first_name}! Я - бот, который занимается хранением фото и видео файлов 😁",
        reply_markup=inline_main_keyboard,
    )
