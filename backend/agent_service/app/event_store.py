import json
from datetime import datetime, timezone
from uuid import UUID

from fastapi import HTTPException
from redis.exceptions import RedisError
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.ontology_service.app.models import AgentEvent


def append_event(
    session: Session,
    redis_client,
    session_id: UUID,
    *,
    event_type: str,
    status: str,
    tool_name: str | None = None,
    details: dict | None = None,
) -> AgentEvent:
    sequence = (session.scalar(
        select(func.max(AgentEvent.sequence)).where(AgentEvent.session_id == session_id)
    ) or 0) + 1
    event = AgentEvent(
        session_id=session_id,
        sequence=sequence,
        event_type=event_type,
        tool_name=tool_name,
        status=status,
        details=details or {},
        created_at=datetime.now(timezone.utc),
    )
    session.add(event)
    session.flush()
    session.commit()
    session.refresh(event)
    try:
        key = f"agent:session:{session_id}:events"
        redis_client.rpush(
            key,
            json.dumps(_event_payload(event), ensure_ascii=False, default=str),
        )
        redis_client.expire(key, 86400)
    except (RedisError, ConnectionError) as exc:
        raise HTTPException(status_code=503, detail="Redis 会话事件暂不可用") from exc
    return event


def read_events(session: Session, redis_client, session_id: UUID) -> list[dict]:
    try:
        cached = redis_client.lrange(f"agent:session:{session_id}:events", 0, -1)
    except (RedisError, ConnectionError) as exc:
        raise HTTPException(status_code=503, detail="Redis 会话事件暂不可用") from exc
    if cached:
        return sorted((json.loads(item) for item in cached), key=lambda item: item["sequence"])
    events = session.scalars(
        select(AgentEvent).where(AgentEvent.session_id == session_id).order_by(AgentEvent.sequence)
    ).all()
    return [_event_payload(event) for event in events]


def _event_payload(event: AgentEvent) -> dict:
    return {
        "id": str(event.id),
        "sequence": event.sequence,
        "event_type": event.event_type,
        "tool_name": event.tool_name,
        "status": event.status,
        "details": event.details,
        "created_at": event.created_at.isoformat(),
    }
