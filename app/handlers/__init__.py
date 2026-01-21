from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .messages import start_router
from .callbacks import main_menu_router
from .fsm import add_media_router, find_media_router, find_n_media_router

# combined router for messages
messages_router = Router()
messages_router.include_routers(start_router)

# combined router for callbacks
callbacks_router = Router()
callbacks_router.include_routers(main_menu_router)

# combined router for FSM
fsm_router = Router()
fsm_router.include_routers(add_media_router, find_media_router, find_n_media_router)


# cancel command handler for FSM processing methods
@fsm_router.message(Command("cancel"))
async def cancel_processing(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state is None:
        return

    await state.clear()
    await message.answer("Операция ввода данных прервана 👍")
