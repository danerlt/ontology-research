from typing import Annotated, Any
from uuid import UUID

import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.agent_service.app.dependencies import OntologyClient, RedisClient, bearer_token
from backend.agent_service.app.event_store import append_event
from backend.agent_service.app.ontology_client import OntologyApiClient
from backend.agent_service.app.routers.sessions import _get_accessible_session
from backend.agent_service.app.schemas import AgentConfiguration, ToolCallRequest, ToolCallResponse
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentSession
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/sessions", tags=["Agent 工具"])


@router.post("/{session_id}/tools/{tool_name}", response_model=ToolCallResponse)
def call_tool(
    session_id: UUID,
    tool_name: str,
    body: ToolCallRequest,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
    ontology_client: OntologyClient,
    token: Annotated[str, Depends(bearer_token)],
) -> ToolCallResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    result = invoke_session_tool(
        session,
        redis_client,
        ontology_client,
        token,
        actor,
        agent_session,
        tool_name,
        body.arguments,
    )
    return ToolCallResponse(session_id=agent_session.id, tool_name=tool_name, status="succeeded", result=result)


def invoke_session_tool(
    session: Session,
    redis_client,
    ontology_client: OntologyApiClient,
    token: str,
    actor: Actor,
    agent_session: AgentSession,
    tool_name: str,
    arguments: dict[str, Any],
    tool_call_id: str | None = None,
) -> Any:
    if agent_session.status != "active":
        raise HTTPException(status_code=409, detail="Agent 会话已结束")
    agent = agent_session.agent
    if not agent.enabled:
        raise HTTPException(status_code=409, detail="Agent 已停用")
    version_config = AgentConfiguration.model_validate(agent_session.version.config)
    if tool_name not in version_config.allowed_tools:
        _deny(session, redis_client, agent_session, tool_name, "Agent 未获此工具授权")
    if tool_name == "execute_action":
        action_name = arguments.get("action_api_name")
        if action_name not in version_config.allowed_actions:
            _deny(session, redis_client, agent_session, tool_name, "Agent 未获此 Action 授权")
        if actor.role not in {"admin", "editor"}:
            _deny(session, redis_client, agent_session, tool_name, "当前账号没有执行业务 Action 的权限")
    try:
        result = _execute_tool(ontology_client, token, tool_name, arguments)
    except ValueError as exc:
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="tool.called",
            tool_name=tool_name,
            status="failed",
            details={"error": str(exc)},
        )
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except httpx.HTTPError as exc:
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="tool.called",
            tool_name=tool_name,
            status="failed",
            details={"error": "本体 API 调用失败"},
        )
        raise HTTPException(status_code=502, detail="本体 API 调用失败") from exc
    append_event(
        session,
        redis_client,
        agent_session.id,
        event_type="tool.called",
        tool_name=tool_name,
        status="succeeded",
        details={"result": result, "tool_call_id": tool_call_id} if tool_call_id else {"result": result},
    )
    return result


def _execute_tool(
    client: OntologyApiClient,
    token: str,
    tool_name: str,
    arguments: dict[str, Any],
) -> Any:
    if tool_name == "search_objects":
        allowed = {"ontology_id", "object_type_api_name", "query", "page", "page_size"}
        _ensure_arguments(arguments, allowed, set())
        return client.search_objects(token, arguments)
    if tool_name == "get_object":
        _ensure_arguments(arguments, {"object_id"}, {"object_id"})
        return client.get_object(token, str(UUID(arguments["object_id"])))
    if tool_name == "execute_action":
        required = {"action_api_name", "object_id", "expected_version", "parameters"}
        _ensure_arguments(arguments, required, required)
        action_api_name = arguments["action_api_name"]
        if not isinstance(action_api_name, str) or not action_api_name:
            raise ValueError("Action API 名无效")
        object_id = str(UUID(arguments["object_id"]))
        expected_version = arguments["expected_version"]
        if not isinstance(expected_version, int) or expected_version < 1:
            raise ValueError("对象版本号无效")
        if not isinstance(arguments["parameters"], dict):
            raise ValueError("Action 参数必须是对象")
        return client.execute_action(
            token,
            action_api_name,
            {
                "object_id": object_id,
                "expected_version": expected_version,
                "parameters": arguments["parameters"],
            },
        )
    raise HTTPException(status_code=404, detail="工具不存在")


def _ensure_arguments(arguments: dict, allowed: set[str], required: set[str]) -> None:
    unknown = set(arguments) - allowed
    missing = required - set(arguments)
    if unknown:
        raise ValueError(f"工具参数不支持：{', '.join(sorted(unknown))}")
    if missing:
        raise ValueError(f"缺少工具参数：{', '.join(sorted(missing))}")


def _deny(session: Session, redis_client, agent_session: AgentSession, tool_name: str, reason: str) -> None:
    append_event(
        session,
        redis_client,
        agent_session.id,
        event_type="tool.denied",
        tool_name=tool_name,
        status="denied",
        details={"reason": reason},
    )
    raise HTTPException(status_code=403, detail=reason)
