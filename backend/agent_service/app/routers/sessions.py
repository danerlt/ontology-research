from datetime import datetime, timezone
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from backend.agent_service.app.dependencies import RedisClient
from backend.agent_service.app.event_store import append_event, read_events
from backend.agent_service.app.routers.agents import _session_response
from backend.agent_service.app.schemas import (
    AgentEventListResponse,
    AgentEventResponse,
    AgentSessionDetailResponse,
    AgentSessionListResponse,
    AgentSessionResponse,
)
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentDefinition, AgentSession
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/sessions", tags=["Agent 会话"])


@router.get("", response_model=AgentSessionListResponse)
def list_sessions(
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    agent_id: UUID | None = None,
    status_filter: str | None = Query(default=None, alias="status"),
    version_number: int | None = Query(default=None, ge=1),
    origin_resource: str | None = Query(default=None, max_length=255),
    query: str | None = Query(default=None, max_length=160),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=50, ge=1, le=100),
) -> AgentSessionListResponse:
    statement = select(AgentSession).join(AgentDefinition).options(
        selectinload(AgentSession.agent), selectinload(AgentSession.version)
    )
    count_statement = select(func.count(AgentSession.id)).join(AgentDefinition)
    if actor.role != "admin":
        owner_filter = AgentSession.actor_id == UUID(actor.id)
        statement = statement.where(owner_filter)
        count_statement = count_statement.where(owner_filter)
    if agent_id:
        statement = statement.where(AgentSession.agent_id == agent_id)
        count_statement = count_statement.where(AgentSession.agent_id == agent_id)
    if status_filter:
        statement = statement.where(AgentSession.status == status_filter)
        count_statement = count_statement.where(AgentSession.status == status_filter)
    if version_number:
        statement = statement.where(AgentSession.version.has(version_number=version_number))
        count_statement = count_statement.where(AgentSession.version.has(version_number=version_number))
    if origin_resource:
        statement = statement.where(AgentSession.origin_resource == origin_resource)
        count_statement = count_statement.where(AgentSession.origin_resource == origin_resource)
    if query:
        term = f"%{query.strip()}%"
        search_filter = or_(
            AgentDefinition.display_name.ilike(term),
            AgentDefinition.api_name.ilike(term),
            AgentSession.origin_resource.ilike(term),
        )
        statement = statement.where(search_filter)
        count_statement = count_statement.where(search_filter)

    total = session.scalar(count_statement) or 0
    rows = session.scalars(
        statement.order_by(AgentSession.created_at.desc()).offset((page - 1) * page_size).limit(page_size)
    ).all()
    return AgentSessionListResponse(
        items=[_session_response(item) for item in rows], total=total, page=page, page_size=page_size
    )


@router.get("/{session_id}", response_model=AgentSessionDetailResponse)
def get_session_detail(
    session_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
) -> AgentSessionDetailResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    events = read_events(session, redis_client, agent_session.id)
    response = _session_response(agent_session)
    return AgentSessionDetailResponse(
        **response.model_dump(),
        config=agent_session.version.config,
        events=events,
    )


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
    return _end_session(session_id, actor, session, redis_client, status="closed")


@router.post("/{session_id}/cancel", response_model=AgentSessionResponse)
def cancel_session(
    session_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
) -> AgentSessionResponse:
    return _end_session(session_id, actor, session, redis_client, status="cancelled")


def _end_session(session_id: UUID, actor: Actor, session: Session, redis_client, *, status: str) -> AgentSessionResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    if agent_session.status != "active":
        raise HTTPException(status_code=409, detail="Agent 会话已结束")
    agent_session.status = status
    agent_session.closed_at = datetime.now(timezone.utc)
    session.commit()
    session.refresh(agent_session)
    try:
        redis_client.set(f"agent:session:{agent_session.id}:status", status, ex=86400)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Redis 会话存储暂不可用") from exc
    append_event(
        session,
        redis_client,
        agent_session.id,
        event_type=f"session.{status}",
        status="succeeded",
    )
    return _session_response(agent_session)


def _get_accessible_session(session: Session, session_id: UUID, actor: Actor) -> AgentSession:
    agent_session = session.scalar(
        select(AgentSession)
        .where(AgentSession.id == session_id)
        .options(selectinload(AgentSession.agent), selectinload(AgentSession.version))
    )
    if agent_session is None:
        raise HTTPException(status_code=404, detail="Agent 会话不存在")
    if actor.role != "admin" and agent_session.actor_id != UUID(actor.id):
        raise HTTPException(status_code=403, detail="当前账号无权访问此 Agent 会话")
    return agent_session
