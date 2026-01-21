import datetime

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import MediaDTO
from .models import MediaContent


class CRUDMedia:
    @staticmethod
    async def create(session: AsyncSession, media: MediaDTO) -> int:
        stmt = (
            insert(MediaContent)
            .values(
                file_id=media.file_id,
                file_unique_id=media.file_unique_id,
                file_type=media.file_type,
                description=media.description,
            )
            .returning(MediaContent.id)
        )

        response = await session.execute(stmt)
        await session.commit()
        return response.scalar_one()

    @staticmethod
    async def find_all(session: AsyncSession) -> list[MediaContent]:
        stmt = select(MediaContent)
        response = await session.execute(stmt)

        return response.scalars().all()

    @staticmethod
    async def find_by_id(session: AsyncSession, media_id: int) -> MediaContent | None:
        stmt = select(MediaContent).where(MediaContent.id == media_id)
        response = await session.execute(stmt)

        return response.scalar_one_or_none()

    @staticmethod
    async def find_n_media(session: AsyncSession, n: int) -> list[MediaContent]:
        stmt = select(MediaContent).where(
            MediaContent.created_at
            >= datetime.datetime.now() - datetime.timedelta(days=n)
        )
        response = await session.execute(stmt)

        return response.scalars().all()
