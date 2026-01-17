import asyncio
import logging

from aiogram import Dispatcher, Bot

from app.config import AppConfig
from app.handlers import messages_router, callbacks_router, fsm_router

# initializing bot dispatcher object
dp = Dispatcher()

# including routers in dispatcher
dp.include_routers(messages_router, callbacks_router, fsm_router)


# main application function
async def main():
    # main configuration object initialization
    config = AppConfig()

    # set level of logging (to be changed)
    logging.basicConfig(level=logging.INFO)

    # initialize bot instance and start polling
    bot = Bot(token=config.bot_token)
    await dp.start_polling(bot)


# run main function in case program start point is main.py file
if __name__ == "__main__":
    asyncio.run(main())
