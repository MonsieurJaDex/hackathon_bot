from typing import List

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.util import await_only

from app.database.crud import CRUDMedia
from app.database.engine import session_factory
from app.database.models import MediaContent
from app.database.schemas import MediaDTO
from app.misc import Singleton


class MediaService(Singleton):
    factory: async_sessionmaker[AsyncSession]

    def __init__(self, factory: async_sessionmaker[AsyncSession] = session_factory):
        self.factory = factory

    async def insert_media(self, dto: MediaDTO) -> int:
        async with self.factory() as session:
            return await CRUDMedia.create(session, dto)

    async def get_media_by_id(self, media_id: int) -> MediaContent | None:
        async with self.factory() as session:
            return await CRUDMedia.find_by_id(session, media_id)

    async def get_all_media(self) -> list[MediaContent]:
        async with self.factory() as session:
            return await CRUDMedia.find_all(session)

    async def get_latest_n_media(self, n: int) -> list[MediaContent]:
        async with self.factory() as session:
            return await CRUDMedia.find_n_media(session, n)


# init singleton MediaService
MediaService()
