from pydantic import BaseModel

from app.misc import ValidContentType


class MediaAddDTO(BaseModel):
    file_id: str
    file_unique_id: str
    file_type: ValidContentType
    description: str
