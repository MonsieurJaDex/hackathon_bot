import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart

from config import AppConfig

dp = Dispatcher()


@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer(
        f"Приветствую, {message.from_user.first_name}! Я - бот, который занимается хранением фото и видео файлов 😁"
    )


async def main():
    config = AppConfig()

    bot = Bot(token=config.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
