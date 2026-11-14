from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.agent_service.app.dependencies import RedisClient
from backend.agent_service.app.event_store import append_event
from backend.agent_service.app.schemas import AgentCreate, AgentResponse, AgentSessionResponse
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentDefinition, AgentSession
from backend.ontology_service.app.security import Actor, get_current_user, require_role

router = APIRouter(prefix="/api/agents", tags=["Agent 管理"])
KNOWN_TOOLS = {"search_objects", "get_object", "execute_action"}


@router.get("", response_model=list[AgentResponse])
def list_agents(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[AgentResponse]:
    agents = session.scalars(select(AgentDefinition).order_by(AgentDefinition.display_name)).all()
    return [_agent_response(agent) for agent in agents]


@router.post("", response_model=AgentResponse, status_code=status.HTTP_201_CREATED)
def create_agent(
    body: AgentCreate,
    _actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> AgentResponse:
    unknown_tools = set(body.allowed_tools) - KNOWN_TOOLS
    if unknown_tools:
        raise HTTPException(status_code=422, detail=f"不支持的工具：{', '.join(sorted(unknown_tools))}")
    if len(body.allowed_tools) != len(set(body.allowed_tools)):
        raise HTTPException(status_code=422, detail="工具授权不能重复")
    if len(body.allowed_actions) != len(set(body.allowed_actions)):
        raise HTTPException(status_code=422, detail="Action 授权不能重复")
    duplicate = session.scalar(
        select(AgentDefinition.id).where(AgentDefinition.api_name == body.api_name)
    )
    if duplicate is not None:
        raise HTTPException(status_code=409, detail="Agent API 名已存在")
    agent = AgentDefinition(
        api_name=body.api_name,
        display_name=body.display_name,
        description=body.description,
        allowed_tools=body.allowed_tools,
        allowed_actions=body.allowed_actions,
    )
    session.add(agent)
    session.commit()
    session.refresh(agent)
    return _agent_response(agent)


@router.post("/{agent_id}/sessions", response_model=AgentSessionResponse, status_code=status.HTTP_201_CREATED)
def create_agent_session(
    agent_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
) -> AgentSessionResponse:
    agent = session.get(AgentDefinition, agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent 不存在")
    if not agent.enabled:
        raise HTTPException(status_code=409, detail="Agent 已停用")
    agent_session = AgentSession(agent_id=agent.id, actor_id=UUID(actor.id), status="active")
    session.add(agent_session)
    session.commit()
    session.refresh(agent_session)
    try:
        redis_client.set(f"agent:session:{agent_session.id}:status", "active", ex=86400)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Redis 会话存储暂不可用") from exc
    append_event(session, redis_client, agent_session.id, event_type="session.created", status="succeeded")
    return _session_response(agent_session)


def _agent_response(agent: AgentDefinition) -> AgentResponse:
    return AgentResponse(
        id=agent.id,
        api_name=agent.api_name,
        display_name=agent.display_name,
        description=agent.description,
        allowed_tools=agent.allowed_tools,
        allowed_actions=agent.allowed_actions,
        enabled=agent.enabled,
    )


def _session_response(agent_session: AgentSession) -> AgentSessionResponse:
    return AgentSessionResponse(
        id=agent_session.id,
        agent_id=agent_session.agent_id,
        status=agent_session.status,
        created_at=agent_session.created_at,
        closed_at=agent_session.closed_at,
    )
