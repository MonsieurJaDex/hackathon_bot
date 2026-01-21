import logging
from typing import Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import appConfig
from app.database.models import Base

# SQLAlchemy engine definition
engine = create_async_engine(
    url=appConfig.postgres_dsn,
    echo=appConfig.DEBUG,
    pool_size=5,
    max_overflow=10,
)

# async session factory
session_factory = async_sessionmaker(bind=engine)


# database healthcheck function
async def database_healthcheck() -> Tuple[bool, Exception | None]:
    try:
        async with engine.connect() as session:
            await session.execute(text("SELECT 1;"))
            return True, None
    except Exception as e:
        return False, e


# database initialization function
async def init_database() -> Tuple[bool, Exception | None]:
    try:
        async with engine.connect() as conn:
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()
            return True, None
    except Exception as e:
        return False, e
