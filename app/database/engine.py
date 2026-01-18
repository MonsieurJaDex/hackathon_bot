from typing import Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import appConfig
from app.database.models import Base

engine = create_async_engine(
    url=appConfig.postgres_dsn,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

session_factory = async_sessionmaker(bind=engine)


async def database_healthcheck() -> Tuple[bool, Exception | None]:
    try:
        async with engine.connect() as session:
            await session.execute(text("SELECT 1;"))
            return True, None
    except Exception as e:
        return False, e


async def init_database() -> Tuple[bool, Exception | None]:
    try:
        async with engine.connect() as conn:
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()
            return True, None
    except Exception as e:
        return False, e
