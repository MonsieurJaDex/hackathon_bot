from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import MediaAddDTO
from .models import MediaContent


class CRUDMedia:
    @staticmethod
    async def create(session: AsyncSession, media: MediaAddDTO) -> int:
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

        return list(response.fetchall())
