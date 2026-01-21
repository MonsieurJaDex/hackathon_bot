from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.misc import ValidContentType


# media DTO scheme
class MediaDTO(BaseModel):
    id: Optional[int] = None
    file_id: str
    file_unique_id: str
    file_type: ValidContentType
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
