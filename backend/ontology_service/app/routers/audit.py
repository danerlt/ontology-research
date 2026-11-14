from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AuditEvent
from backend.ontology_service.app.schemas.audit import AuditEventListResponse, AuditEventResponse
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/audit-events", tags=["审计记录"])


@router.get("", response_model=AuditEventListResponse)
def list_audit_events(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    event_type: str | None = None,
    resource_type: str | None = None,
    actor_id: UUID | None = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=25, ge=1, le=100),
) -> AuditEventListResponse:
    statement = select(AuditEvent).options(selectinload(AuditEvent.actor))
    count_statement = select(func.count()).select_from(AuditEvent)
    if event_type:
        statement = statement.where(AuditEvent.event_type == event_type)
        count_statement = count_statement.where(AuditEvent.event_type == event_type)
    if resource_type:
        statement = statement.where(AuditEvent.resource_type == resource_type)
        count_statement = count_statement.where(AuditEvent.resource_type == resource_type)
    if actor_id is not None:
        statement = statement.where(AuditEvent.actor_id == actor_id)
        count_statement = count_statement.where(AuditEvent.actor_id == actor_id)
    total = session.scalar(count_statement) or 0
    events = session.scalars(
        statement.order_by(AuditEvent.created_at.desc()).offset((page - 1) * page_size).limit(page_size)
    ).all()
    return AuditEventListResponse(
        data=[
            AuditEventResponse(
                id=event.id,
                actor_id=event.actor_id,
                actor_email=event.actor.email if event.actor is not None else None,
                event_type=event.event_type,
                resource_type=event.resource_type,
                resource_id=event.resource_id,
                details=event.details,
                created_at=event.created_at,
            )
            for event in events
        ],
        total=total,
        page=page,
        page_size=page_size,
    )
