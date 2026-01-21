import datetime

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import MediaDTO
from .models import MediaContent


# class with static CRUD methods
class CRUDMedia:
    @staticmethod
    async def create(session: AsyncSession, media: MediaDTO) -> int:
        """
        Create new media record
        :param session: Database session
        :param media: Media object
        :return: New media identifier
        """

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
        """
        Get all media records
        :param session: Database session
        :return: List of media records
        """

        stmt = select(MediaContent)
        response = await session.execute(stmt)

        return response.scalars().all()

    @staticmethod
    async def find_by_id(session: AsyncSession, media_id: int) -> MediaContent | None:
        """
        Get media record by ID
        :param session: Database session
        :param media_id: Media identifier
        :return: Media object or None
        """

        stmt = select(MediaContent).where(MediaContent.id == media_id)
        response = await session.execute(stmt)

        return response.scalar_one_or_none()

    @staticmethod
    async def find_n_media(session: AsyncSession, n: int) -> list[MediaContent]:
        """
        Get last n media records
        :param session: Database session
        :param n: Amount of days
        :return: List of media records
        """
        stmt = select(MediaContent).where(
            MediaContent.created_at
            >= datetime.datetime.now() - datetime.timedelta(days=n)
        )
        response = await session.execute(stmt)

        return response.scalars().all()
