import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot

from app.config import appConfig
from app.handlers import messages_router, callbacks_router, fsm_router
from app.misc import database_healthcheck

# initializing bot dispatcher object
dp = Dispatcher()

# including routers in dispatcher
dp.include_routers(messages_router, callbacks_router, fsm_router)


# main application function
async def main():
    # set level of logging (to be changed)
    logging.basicConfig(level=logging.INFO if appConfig.DEBUG else logging.WARN)

    # initialize bot instance and start polling
    bot = Bot(token=appConfig.BOT_TOKEN)

    # database healthcheck
    status, exception = await database_healthcheck()
    if not status:
        logging.getLogger().error("Database healthcheck failed: " + str(exception))
        sys.exit(1)

    await dp.start_polling(bot)


# run main function in case program start point is main.py file
if __name__ == "__main__":
    asyncio.run(main())
