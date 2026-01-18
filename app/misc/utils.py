from typing import Tuple

from sqlalchemy import text

from app.database.engine import engine


async def database_healthcheck() -> Tuple[bool, Exception | None]:
    try:
        async with engine.connect() as session:
            await session.execute(text("SELECT 1;"))
            return True, None
    except Exception as e:
        return False, e
