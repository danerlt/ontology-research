from datetime import datetime, timezone
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.agent_service.app.dependencies import RedisClient
from backend.agent_service.app.event_store import append_event, read_events
from backend.agent_service.app.schemas import AgentEventListResponse, AgentEventResponse, AgentSessionResponse
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentSession
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/sessions", tags=["Agent 会话"])


@router.get("/{session_id}/events", response_model=AgentEventListResponse)
def list_session_events(
    session_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
) -> AgentEventListResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    events = read_events(session, redis_client, agent_session.id)
    return AgentEventListResponse(items=[AgentEventResponse.model_validate(item) for item in events])


@router.post("/{session_id}/close", response_model=AgentSessionResponse)
def close_session(
    session_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
) -> AgentSessionResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    if agent_session.status != "active":
        raise HTTPException(status_code=409, detail="Agent 会话已结束")
    agent_session.status = "closed"
    agent_session.closed_at = datetime.now(timezone.utc)
    session.commit()
    session.refresh(agent_session)
    try:
        redis_client.set(f"agent:session:{agent_session.id}:status", "closed", ex=86400)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Redis 会话存储暂不可用") from exc
    append_event(session, redis_client, agent_session.id, event_type="session.closed", status="succeeded")
    return AgentSessionResponse(
        id=agent_session.id,
        agent_id=agent_session.agent_id,
        status=agent_session.status,
        created_at=agent_session.created_at,
        closed_at=agent_session.closed_at,
    )


def _get_accessible_session(session: Session, session_id: UUID, actor: Actor) -> AgentSession:
    agent_session = session.scalar(
        select(AgentSession)
        .where(AgentSession.id == session_id)
        .options(selectinload(AgentSession.agent))
    )
    if agent_session is None:
        raise HTTPException(status_code=404, detail="Agent 会话不存在")
    if actor.role != "admin" and agent_session.actor_id != UUID(actor.id):
        raise HTTPException(status_code=403, detail="当前账号无权访问此 Agent 会话")
    return agent_session
