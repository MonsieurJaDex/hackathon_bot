from aiogram import Router

from .messages import start_router

messages_router = Router()
messages_router.include_routers(start_router)
