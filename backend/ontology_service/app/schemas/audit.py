from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class AuditEventResponse(BaseModel):
    id: UUID
    actor_id: UUID | None
    actor_email: str | None
    event_type: str
    resource_type: str
    resource_id: str
    details: dict[str, Any]
    created_at: datetime


class AuditEventListResponse(BaseModel):
    data: list[AuditEventResponse]
    total: int
    page: int
    page_size: int
