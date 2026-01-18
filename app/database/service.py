from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.database.crud import CRUDMedia
from app.database.engine import session_factory
from app.database.schemas import MediaAddDTO
from app.misc import Singleton


class MediaService(Singleton):
    factory: async_sessionmaker[AsyncSession]

    def __init__(self, factory: async_sessionmaker[AsyncSession] = session_factory):
        self.factory = factory

    async def insert_media(self, dto: MediaAddDTO) -> int:
        async with self.factory() as session:
            await CRUDMedia.find_all(session)
            return await CRUDMedia.create(session, dto)


# init singleton MediaService
MediaService()
