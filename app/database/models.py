import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.misc import ValidContentType

# custom type for record identifiers
integer_primary_key = Annotated[int, mapped_column(primary_key=True)]


# define Base class for our models
class Base(DeclarativeBase):
    """
    Base class for all database models.
    """

    pass


# define object for media_content table
class MediaContent(Base):
    """
    SQLAlchemy declarative base class for media content table
    """

    __tablename__ = "media_content"

    # primary key, ID of a record
    id: Mapped[integer_primary_key]

    # file_id, temporary at telegram servers, need to get access to a file
    file_id: Mapped[str] = mapped_column(unique=True)

    # unique file id, not temporary
    file_unique_id: Mapped[str] = mapped_column(unique=True)

    # type of stored file
    file_type: Mapped[ValidContentType]

    # description of user's media file
    description: Mapped[str]

    # datetime of record creation
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    # datetime of record last update
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=lambda: datetime.datetime.now(datetime.UTC),
    )
