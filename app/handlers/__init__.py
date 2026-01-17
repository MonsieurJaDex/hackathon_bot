from aiogram import Router

from .messages import start_router
from .callbacks import main_menu_router
from .fsm import add_media_router

messages_router = Router()
messages_router.include_routers(start_router)

callbacks_router = Router()
callbacks_router.include_routers(main_menu_router)

fsm_router = Router()
fsm_router.include_routers(add_media_router)
