from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import MediaAddDTO
from .models import MediaContent


class CRUDMedia:
    @staticmethod
    async def create(session: AsyncSession, media: MediaAddDTO) -> int:
        stmt = insert(MediaContent).values(
            file_id=media.file_id,
            file_unique_id=media.file_unique_id,
            file_type=media.file_type,
            description=media.description,
        )

        response = await session.execute(stmt)
        print(response)
        return 0
