from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session

from backend.ontology_service.app.models.audit import AuditEvent


def record_audit(
    session: Session,
    *,
    actor_id: UUID | str | None,
    event_type: str,
    resource_type: str,
    resource_id: UUID | str,
    details: dict[str, Any],
) -> AuditEvent:
    event = AuditEvent(
        project_id=session.info.get("project_id"),
        actor_id=UUID(str(actor_id)) if actor_id is not None else None,
        event_type=event_type,
        resource_type=resource_type,
        resource_id=str(resource_id),
        details=details,
    )
    session.add(event)
    return event
